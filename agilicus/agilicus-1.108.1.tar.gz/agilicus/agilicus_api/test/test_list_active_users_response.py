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
import datetime

import agilicus_api
from agilicus_api.models.list_active_users_response import ListActiveUsersResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListActiveUsersResponse(unittest.TestCase):
    """ListActiveUsersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListActiveUsersResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_active_users_response.ListActiveUsersResponse()  # noqa: E501
        if include_optional :
            return ListActiveUsersResponse(
                active_users = [
                    agilicus_api.models.time_interval_metrics.TimeIntervalMetrics(
                        time = '2019-05-16T19:11:18Z', 
                        metric = 1, )
                    ]
            )
        else :
            return ListActiveUsersResponse(
        )

    def testListActiveUsersResponse(self):
        """Test ListActiveUsersResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
