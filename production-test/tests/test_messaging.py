"""Tests for the messaging API."""

from telstra.messaging.v3 import message, virtual_number


def test_create_numbers():
    """
    GIVEN credentials in the environment
    WHEN create, get and delete are called
    THEN no errors are raised.
    """
    vn_response = virtual_number.assign()
    virtual_number.get(virtual_number=vn_response.virtual_number)
    virtual_number.delete(virtual_number=vn_response.virtual_number)


def test_send_get_message():
    """
    GIVEN credentials in the environment
    WHEN send is called
    THEN no errors are raised.
    """
    virtual_numbers = virtual_number.get_all()
    if len(virtual_numbers.virtual_numbers) > 0:
        message_response = message.send(
            to=virtual_numbers.virtual_numbers[0].virtual_number,
            from_="privateNumber",
            message_content="Prod Test",
        )
        message.get(message_id=message_response.message_id)
    else:
        vn_response = virtual_number.assign()
        message_response = message.send(
            to=vn_response.virtual_number,
            from_="privateNumber",
            message_content="Prod Test",
        )
        message.get(message_id=message_response.message_id)
        virtual_number.delete(virtual_number=vn_response.virtual_number)
