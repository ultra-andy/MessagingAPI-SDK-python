# coding: utf-8

"""
    Telstra Messaging API

     The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator.  It also allows your application to track the delivery status of both sent and received SMS messages.   # noqa: E501

    OpenAPI spec version: 2.2.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from Telstra_Messaging.api_client import ApiClient


class MessagingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_mms_status(self, messageid, **kwargs):  # noqa: E501
        """Get MMS Status  # noqa: E501

        Get MMS Status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_mms_status(messageid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str messageid: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms (required)
        :return: OutboundPollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_mms_status_with_http_info(messageid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_mms_status_with_http_info(messageid, **kwargs)  # noqa: E501
            return data

    def get_mms_status_with_http_info(self, messageid, **kwargs):  # noqa: E501
        """Get MMS Status  # noqa: E501

        Get MMS Status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_mms_status_with_http_info(messageid, async=True)
        >>> result = thread.get()

        :param async bool
        :param str messageid: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/mms (required)
        :return: OutboundPollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['messageid']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_mms_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'messageid' is set
        if ('messageid' not in params or
                params['messageid'] is None):
            raise ValueError("Missing the required parameter `messageid` when calling `get_mms_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'messageid' in params:
            path_params['messageid'] = params['messageid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/mms/{messageid}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OutboundPollResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sms_status(self, message_id, **kwargs):  # noqa: E501
        """Get SMS Status  # noqa: E501

        Get Message Status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sms_status(message_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str message_id: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms (required)
        :return: OutboundPollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_sms_status_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sms_status_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def get_sms_status_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """Get SMS Status  # noqa: E501

        Get Message Status  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_sms_status_with_http_info(message_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str message_id: Unique identifier of a message - it is the value returned from a previous POST call to https://api.telstra.com/v2/messages/sms (required)
        :return: OutboundPollResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sms_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `get_sms_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'message_id' in params:
            path_params['messageId'] = params['message_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/sms/{messageId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OutboundPollResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def retrieve_sms_responses(self, **kwargs):  # noqa: E501
        """Retrieve SMS Responses  # noqa: E501

        Retrieve Messages  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_sms_responses(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[InboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.retrieve_sms_responses_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.retrieve_sms_responses_with_http_info(**kwargs)  # noqa: E501
            return data

    def retrieve_sms_responses_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve SMS Responses  # noqa: E501

        Retrieve Messages  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.retrieve_sms_responses_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: list[InboundPollResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_sms_responses" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/sms', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InboundPollResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_mms(self, body, **kwargs):  # noqa: E501
        """Send MMS  # noqa: E501

        Send MMS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_mms(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendMmsRequest body: A JSON or XML payload containing the recipient's phone number and MMS message.The recipient number should be in the format '04xxxxxxxx' where x is a digit (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.send_mms_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.send_mms_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def send_mms_with_http_info(self, body, **kwargs):  # noqa: E501
        """Send MMS  # noqa: E501

        Send MMS  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_mms_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendMmsRequest body: A JSON or XML payload containing the recipient's phone number and MMS message.The recipient number should be in the format '04xxxxxxxx' where x is a digit (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_mms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_mms`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/mms', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def send_sms(self, payload, **kwargs):  # noqa: E501
        """Send SMS  # noqa: E501

        Send Message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_sms(payload, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendSMSRequest payload: A JSON or XML payload containing the recipient's phone number and text message. The recipient number should be in the format '04xxxxxxxx' where x is a digit (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.send_sms_with_http_info(payload, **kwargs)  # noqa: E501
        else:
            (data) = self.send_sms_with_http_info(payload, **kwargs)  # noqa: E501
            return data

    def send_sms_with_http_info(self, payload, **kwargs):  # noqa: E501
        """Send SMS  # noqa: E501

        Send Message  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.send_sms_with_http_info(payload, async=True)
        >>> result = thread.get()

        :param async bool
        :param SendSMSRequest payload: A JSON or XML payload containing the recipient's phone number and text message. The recipient number should be in the format '04xxxxxxxx' where x is a digit (required)
        :return: MessageSentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payload']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payload' is set
        if ('payload' not in params or
                params['payload'] is None):
            raise ValueError("Missing the required parameter `payload` when calling `send_sms`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'payload' in params:
            body_params = params['payload']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['auth']  # noqa: E501

        return self.api_client.call_api(
            '/messages/sms', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageSentResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
