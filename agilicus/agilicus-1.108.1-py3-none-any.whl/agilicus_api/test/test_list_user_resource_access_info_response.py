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
from agilicus_api.models.list_user_resource_access_info_response import ListUserResourceAccessInfoResponse  # noqa: E501
from agilicus_api.rest import ApiException

class TestListUserResourceAccessInfoResponse(unittest.TestCase):
    """ListUserResourceAccessInfoResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListUserResourceAccessInfoResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.list_user_resource_access_info_response.ListUserResourceAccessInfoResponse()  # noqa: E501
        if include_optional :
            return ListUserResourceAccessInfoResponse(
                user_resource_access_info = [
                    agilicus_api.models.user_resource_access_info.UserResourceAccessInfo(
                        status = agilicus_api.models.user_resource_access_info_status.UserResourceAccessInfoStatus(
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
                            roles = ["owner","viewer"], ), )
                    ], 
                limit = 56
            )
        else :
            return ListUserResourceAccessInfoResponse(
                user_resource_access_info = [
                    agilicus_api.models.user_resource_access_info.UserResourceAccessInfo(
                        status = agilicus_api.models.user_resource_access_info_status.UserResourceAccessInfoStatus(
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
                            roles = ["owner","viewer"], ), )
                    ],
                limit = 56,
        )

    def testListUserResourceAccessInfoResponse(self):
        """Test ListUserResourceAccessInfoResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
