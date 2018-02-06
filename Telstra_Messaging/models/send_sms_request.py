# coding: utf-8

"""
    Telstra Messaging API

     The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator.  It also allows your application to track the delivery status of both sent and received SMS messages.   # noqa: E501

    OpenAPI spec version: 2.2.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SendSMSRequest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'to': 'str',
        'body': 'str',
        '_from': 'str',
        'validity': 'int',
        'scheduled_delivery': 'int',
        'notify_url': 'str',
        'reply_request': 'bool'
    }

    attribute_map = {
        'to': 'to',
        'body': 'body',
        '_from': 'from',
        'validity': 'validity',
        'scheduled_delivery': 'scheduledDelivery',
        'notify_url': 'notifyURL',
        'reply_request': 'replyRequest'
    }

    def __init__(self, to=None, body=None, _from=None, validity=None, scheduled_delivery=None, notify_url=None, reply_request=None):  # noqa: E501
        """SendSMSRequest - a model defined in Swagger"""  # noqa: E501

        self._to = None
        self._body = None
        self.__from = None
        self._validity = None
        self._scheduled_delivery = None
        self._notify_url = None
        self._reply_request = None
        self.discriminator = None

        self.to = to
        self.body = body
        if _from is not None:
            self._from = _from
        if validity is not None:
            self.validity = validity
        if scheduled_delivery is not None:
            self.scheduled_delivery = scheduled_delivery
        if notify_url is not None:
            self.notify_url = notify_url
        if reply_request is not None:
            self.reply_request = reply_request

    @property
    def to(self):
        """Gets the to of this SendSMSRequest.  # noqa: E501

        Phone number (in E.164 format) to send the SMS to. This number can be in international format if preceeded by a ‘+’, or in national format.  # noqa: E501

        :return: The to of this SendSMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendSMSRequest.

        Phone number (in E.164 format) to send the SMS to. This number can be in international format if preceeded by a ‘+’, or in national format.  # noqa: E501

        :param to: The to of this SendSMSRequest.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def body(self):
        """Gets the body of this SendSMSRequest.  # noqa: E501

        The text body of the message. Messages longer than 160 characters will be counted as multiple messages.  # noqa: E501

        :return: The body of this SendSMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this SendSMSRequest.

        The text body of the message. Messages longer than 160 characters will be counted as multiple messages.  # noqa: E501

        :param body: The body of this SendSMSRequest.  # noqa: E501
        :type: str
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")  # noqa: E501

        self._body = body

    @property
    def _from(self):
        """Gets the _from of this SendSMSRequest.  # noqa: E501

        Phone number (in E.164 format) the SMS was sent from. If not present, the serverice will use the mobile number associated with the application, or it be an Alphanumeric address of up to 11 characters.  # noqa: E501

        :return: The _from of this SendSMSRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendSMSRequest.

        Phone number (in E.164 format) the SMS was sent from. If not present, the serverice will use the mobile number associated with the application, or it be an Alphanumeric address of up to 11 characters.  # noqa: E501

        :param _from: The _from of this SendSMSRequest.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def validity(self):
        """Gets the validity of this SendSMSRequest.  # noqa: E501

        How long the platform should attempt to deliver the message for. This period is specified in minutes from the message  # noqa: E501

        :return: The validity of this SendSMSRequest.  # noqa: E501
        :rtype: int
        """
        return self._validity

    @validity.setter
    def validity(self, validity):
        """Sets the validity of this SendSMSRequest.

        How long the platform should attempt to deliver the message for. This period is specified in minutes from the message  # noqa: E501

        :param validity: The validity of this SendSMSRequest.  # noqa: E501
        :type: int
        """

        self._validity = validity

    @property
    def scheduled_delivery(self):
        """Gets the scheduled_delivery of this SendSMSRequest.  # noqa: E501

        How long the platform should wait before attempting to send the message - specified in minutes.  # noqa: E501

        :return: The scheduled_delivery of this SendSMSRequest.  # noqa: E501
        :rtype: int
        """
        return self._scheduled_delivery

    @scheduled_delivery.setter
    def scheduled_delivery(self, scheduled_delivery):
        """Sets the scheduled_delivery of this SendSMSRequest.

        How long the platform should wait before attempting to send the message - specified in minutes.  # noqa: E501

        :param scheduled_delivery: The scheduled_delivery of this SendSMSRequest.  # noqa: E501
        :type: int
        """

        self._scheduled_delivery = scheduled_delivery

    @property
    def notify_url(self):
        """Gets the notify_url of this SendSMSRequest.  # noqa: E501

        Contains a URL that will be called once your message has been processed. The status may be delivered, expired, deleted, etc.  # noqa: E501

        :return: The notify_url of this SendSMSRequest.  # noqa: E501
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this SendSMSRequest.

        Contains a URL that will be called once your message has been processed. The status may be delivered, expired, deleted, etc.  # noqa: E501

        :param notify_url: The notify_url of this SendSMSRequest.  # noqa: E501
        :type: str
        """

        self._notify_url = notify_url

    @property
    def reply_request(self):
        """Gets the reply_request of this SendSMSRequest.  # noqa: E501

        If set to true, the reply message functionality will be implemented and the to address will be ignored if present. If false or not present, then normal message handling is implemented.  # noqa: E501

        :return: The reply_request of this SendSMSRequest.  # noqa: E501
        :rtype: bool
        """
        return self._reply_request

    @reply_request.setter
    def reply_request(self, reply_request):
        """Sets the reply_request of this SendSMSRequest.

        If set to true, the reply message functionality will be implemented and the to address will be ignored if present. If false or not present, then normal message handling is implemented.  # noqa: E501

        :param reply_request: The reply_request of this SendSMSRequest.  # noqa: E501
        :type: bool
        """

        self._reply_request = reply_request

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SendSMSRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
