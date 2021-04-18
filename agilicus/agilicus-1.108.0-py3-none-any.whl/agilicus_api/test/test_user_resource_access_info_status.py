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
from agilicus_api.models.user_resource_access_info_status import UserResourceAccessInfoStatus  # noqa: E501
from agilicus_api.rest import ApiException

class TestUserResourceAccessInfoStatus(unittest.TestCase):
    """UserResourceAccessInfoStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserResourceAccessInfoStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.user_resource_access_info_status.UserResourceAccessInfoStatus()  # noqa: E501
        if include_optional :
            return UserResourceAccessInfoStatus(
                user_id = 'tuU7smH86zAXMl76sua6xQ', 
                org_id = 'IAsl3dl40aSsfLKiU76', 
                org_name = 'egov', 
                parent_org_id = 'G99q3lasls29wsk', 
                parent_org_name = 'root', 
                resource_id = '123', 
                resource_name = 'public', 
                resource_type = 'fileshare', 
                resource_uri = 'https://share.cloud.egov.city/public', 
                access_level = 'granted', 
                roles = ["owner","viewer"]
            )
        else :
            return UserResourceAccessInfoStatus(
                user_id = 'tuU7smH86zAXMl76sua6xQ',
                org_id = 'IAsl3dl40aSsfLKiU76',
                org_name = 'egov',
                resource_id = '123',
                resource_name = 'public',
                resource_type = 'fileshare',
                access_level = 'granted',
        )

    def testUserResourceAccessInfoStatus(self):
        """Test UserResourceAccessInfoStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
