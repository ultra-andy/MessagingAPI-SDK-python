# coding: utf-8

"""
    Telstra Messaging API

     The Telstra SMS Messaging API allows your applications to send and receive SMS text messages from Australia's leading network operator.  It also allows your application to track the delivery status of both sent and received SMS messages.   # noqa: E501

    OpenAPI spec version: 2.2.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import Telstra_Messaging
from Telstra_Messaging.api.provisioning_api import ProvisioningApi  # noqa: E501
from Telstra_Messaging.rest import ApiException


class TestProvisioningApi(unittest.TestCase):
    """ProvisioningApi unit test stubs"""

    def setUp(self):
        self.api = Telstra_Messaging.api.provisioning_api.ProvisioningApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_subscription(self):
        """Test case for create_subscription

        Create Subscription  # noqa: E501
        """
        pass

    def test_delete_subscription(self):
        """Test case for delete_subscription

        Delete Subscription  # noqa: E501
        """
        pass

    def test_get_subscription(self):
        """Test case for get_subscription

        Get Subscription  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
