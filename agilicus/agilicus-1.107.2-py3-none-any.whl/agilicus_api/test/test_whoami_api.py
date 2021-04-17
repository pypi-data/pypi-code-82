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
from agilicus_api.api.whoami_api import WhoamiApi  # noqa: E501
from agilicus_api.rest import ApiException


class TestWhoamiApi(unittest.TestCase):
    """WhoamiApi unit test stubs"""

    def setUp(self):
        self.api = agilicus_api.api.whoami_api.WhoamiApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_whoami(self):
        """Test case for create_whoami

        login through whoami  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
