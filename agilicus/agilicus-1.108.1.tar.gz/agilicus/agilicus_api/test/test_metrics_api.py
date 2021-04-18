# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2021.04.16
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import agilicus_api
from agilicus_api.api.metrics_api import MetricsApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestMetricsApi(unittest.TestCase):
    """MetricsApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.metrics_api.MetricsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list_active_users(self):
        """Test case for list_active_users

        View number of active users  # noqa: E501
        """
        pass

    def test_list_top_users(self):
        """Test case for list_top_users

        View top users  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
