# coding: utf-8

"""
    Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.os_hosts_api import OsHostsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestOsHostsApi(unittest.TestCase):
    """OsHostsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.os_hosts_api.OsHostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_v21_os_hosts_get(self):
        """Test case for v21_os_hosts_get

        """
        pass

    def test_v21_os_hosts_host_name_get(self):
        """Test case for v21_os_hosts_host_name_get

        """
        pass

    def test_v21_os_hosts_host_name_put(self):
        """Test case for v21_os_hosts_host_name_put

        """
        pass

    def test_v21_os_hosts_host_name_reboot_get(self):
        """Test case for v21_os_hosts_host_name_reboot_get

        """
        pass

    def test_v21_os_hosts_host_name_shutdown_get(self):
        """Test case for v21_os_hosts_host_name_shutdown_get

        """
        pass

    def test_v21_os_hosts_host_name_startup_get(self):
        """Test case for v21_os_hosts_host_name_startup_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
