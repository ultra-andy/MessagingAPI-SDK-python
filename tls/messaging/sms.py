"""Used to send messages."""

import dataclasses
import json
import re
import typing
from urllib import error, request

from tls.messaging.utils import phone_number

from . import exceptions, oauth, types
from .utils import phone_number

_URL = "https://tapi.telstra.com/v2/messages/sms"


@dataclasses.dataclass
class TSms:
    """
    A sms.

    Attrs:
        to: The destination mobile number.
        delivery_status: Whether the delivery has been completed.
        message_id: Unique identifier.
        message_status_url: URL to retrieve the current delivery status.

    """

    to: typing.Union[types.TTo, typing.List[types.TTo]]
    delivery_status: str
    message_id: types.TMessageId
    message_status_url: str


_VALID_FROM = re.compile(r"^[a-zA-Z0-9]+$")


def _send_validate_to(to: typing.Union[types.TTo, typing.List[types.TTo]]) -> None:
    """Calidate the to parameter for send."""
    if not isinstance(to, str) and not isinstance(to, list):
        raise exceptions.SmsError(
            f'the value of "to" is not valid, expecting a string or a list of string, '
            f'received "{to}"'
        )
    if isinstance(to, str):
        result = phone_number.check(value=to)
        if not result.valid:
            raise exceptions.SmsError(
                f'the value of "to" is not valid, {result.reason}'
            )
    if isinstance(to, list):
        first_invalid_result = next(
            filter(lambda result: not result.valid, map(phone_number.check, to)),
            None,
        )
        if first_invalid_result is not None:
            raise exceptions.SmsError(
                f'the value of "to" is not valid, {first_invalid_result.reason}'
            )


def _send_validate_from(from_: typing.Optional[str]) -> None:
    """Calidate the from_ parameter for send."""
    if from_ is not None:
        if not isinstance(from_, str):
            raise exceptions.SmsError(
                'the value of "from_" is not valid, expected a string, received '
                f'"{from_}"'
            )
        if len(from_) > 11:
            raise exceptions.SmsError(
                'the value of "from_" has too many characters, expected at most 11 '
                f'characters, received "{from_}"'
            )
        if not _VALID_FROM.search(from_):
            raise exceptions.SmsError(
                'the value of "from_" contains invalid characters, expected alpha '
                f'numeric characters, received "{from_}"'
            )
        result = phone_number.check(value=from_)
        if result.valid:
            raise exceptions.SmsError(
                'the value of "from_" is a phone number, expected alpha '
                f'numeric characters that are not phone numbers, received "{from_}"'
            )


def send(
    to: typing.Union[types.TTo, typing.List[types.TTo]],
    body: types.TBody,
    from_: typing.Optional[str] = None,
    validity: typing.Optional[int] = None,
    scheduled_delivery: typing.Optional[int] = None,
) -> TSms:
    """
    Send an SMS.

    Raises SmsError is anything goes wrong whilst sending a message.

    Args:
        to: The destination mobile number.
        body: The body of the message.
        from: Alpha numeric sender identity.
        validity: How long the platform should attempt to deliver the message for
            (in minutes).
        scheduled_delivery: How long the platform should wait before attempting to send
            the message (in minutes).

    Returns:
        The message that was sent.

    """
    # Validate to
    _send_validate_to(to)
    # Validate body
    if not isinstance(body, str):
        raise exceptions.SmsError(
            f'the value of "body" is not valid, expected a string, received "{body}"'
        )
    # Validate from_
    _send_validate_from(from_)
    # Validate validity
    if validity is not None:
        if not isinstance(validity, int) or isinstance(validity, bool):
            raise exceptions.SmsError(
                'the value of "validity" is not valid, expected an integer, received '
                f'"{validity}"'
            )
    # Validate scheduled_delivery
    if scheduled_delivery is not None:
        if not isinstance(scheduled_delivery, int) or isinstance(
            scheduled_delivery, bool
        ):
            raise exceptions.SmsError(
                'the value of "scheduled_delivery" is not valid, expected an integer, '
                f'received "{scheduled_delivery}"'
            )

    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.SmsError(f"Could not retrieve an OAuth token: {exc}") from exc

    data: typing.Dict[str, typing.Union[str, typing.List[str], int]] = {
        "to": to,
        "body": body,
    }
    if from_ is not None:
        data["from"] = from_
    if validity is not None:
        data["validity"] = validity
    if scheduled_delivery is not None:
        data["scheduledDelivery"] = scheduled_delivery
    data_str = json.dumps(data).encode()
    headers = {
        "Content-Type": "application/json",
        "Authorization": token.authorization,
    }
    sms_request = request.Request(_URL, data=data_str, headers=headers, method="POST")
    try:
        with request.urlopen(sms_request) as response:
            sms_dict = json.loads(response.read().decode())
            return TSms(
                to=sms_dict["messages"][0]["to"],
                delivery_status=sms_dict["messages"][0]["deliveryStatus"],
                message_id=sms_dict["messages"][0]["messageId"],
                message_status_url=sms_dict["messages"][0]["messageStatusURL"],
            )
    except error.HTTPError as exc:
        raise exceptions.SmsError(f"Could not send SMS: {exc}") from exc


@dataclasses.dataclass
class TReply:
    """
    A reply.

    Attrs:
        destination_address: Where the message is delivered to.
        sender_address: Who the message is from.
        status: Whether the delivery has been completed.
        message: The body of the message.
        message_id: Unique identifier for the message.
        sent_timestamp: When the message was sent.

    """

    destination_address: str
    sender_address: str
    status: str
    message: str
    message_id: str
    sent_timestamp: str


def get_next_unread_reply() -> TReply:
    """
    Get the next unread reply that have been received.

    Raises SmsError is anything goes wrong whilst retrieving replies.

    Returns:
        The next unread reply.

    """
    try:
        token = oauth.get_token()
    except exceptions.CredentialError as exc:
        raise exceptions.SmsError(f"Could not retrieve an OAuth token: {exc}") from exc

    headers = {"Authorization": token.authorization}
    reply_request = request.Request(_URL, headers=headers, method="GET")
    try:
        with request.urlopen(reply_request) as response:
            reply_dict = json.loads(response.read().decode())
            return TReply(
                status=reply_dict["status"],
                destination_address=reply_dict["destinationAddress"],
                sender_address=reply_dict["senderAddress"],
                message_id=reply_dict["messageId"],
                message=reply_dict["message"],
                sent_timestamp=reply_dict["sentTimestamp"],
            )
    except error.HTTPError as exc:
        raise exceptions.SmsError(f"Could not send SMS: {exc}") from exc
