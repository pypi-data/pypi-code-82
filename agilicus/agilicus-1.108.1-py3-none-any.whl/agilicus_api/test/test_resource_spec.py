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
from agilicus_api.models.resource_spec import ResourceSpec  # noqa: E501
from agilicus_api.rest import ApiException

class TestResourceSpec(unittest.TestCase):
    """ResourceSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ResourceSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.resource_spec.ResourceSpec()  # noqa: E501
        if include_optional :
            return ResourceSpec(
                name = 'my-application', 
                resource_type = 'fileshare', 
                org_id = 'S38d8dk3Xirt69', 
                name_slug = 'a'
            )
        else :
            return ResourceSpec(
                name = 'my-application',
                resource_type = 'fileshare',
                org_id = 'S38d8dk3Xirt69',
        )

    def testResourceSpec(self):
        """Test ResourceSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
