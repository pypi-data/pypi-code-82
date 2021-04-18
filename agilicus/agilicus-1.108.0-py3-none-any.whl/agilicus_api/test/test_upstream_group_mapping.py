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
from agilicus_api.models.upstream_group_mapping import UpstreamGroupMapping  # noqa: E501
from agilicus_api.rest import ApiException

class TestUpstreamGroupMapping(unittest.TestCase):
    """UpstreamGroupMapping unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UpstreamGroupMapping
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.upstream_group_mapping.UpstreamGroupMapping()  # noqa: E501
        if include_optional :
            return UpstreamGroupMapping(
                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                spec = agilicus_api.models.upstream_group_mapping_spec.UpstreamGroupMappingSpec(
                    upstream_issuer = 'https://login.microsoftonline.com/c945d377-ea94-4a7d-9c83-0615e7ff0022/v2.0', 
                    org_id = 'asdfg123hjkl', 
                    group_mappings = [
                        agilicus_api.models.upstream_group_mapping_entry.UpstreamGroupMappingEntry(
                            priority = 1, 
                            upstream_group_name = 'Company Team (.*)', 
                            upstream_name_is_a_guid = False, 
                            agilicus_group_name = 'Agilicus {0}', 
                            group_org_id = 'asdfg123hjkl', )
                        ], 
                    excluded_groups = [
                        agilicus_api.models.upstream_group_excluded_entry.UpstreamGroupExcludedEntry(
                            upstream_group_name = 'Admin*', 
                            upstream_name_is_a_guid = False, )
                        ], )
            )
        else :
            return UpstreamGroupMapping(
                spec = agilicus_api.models.upstream_group_mapping_spec.UpstreamGroupMappingSpec(
                    upstream_issuer = 'https://login.microsoftonline.com/c945d377-ea94-4a7d-9c83-0615e7ff0022/v2.0', 
                    org_id = 'asdfg123hjkl', 
                    group_mappings = [
                        agilicus_api.models.upstream_group_mapping_entry.UpstreamGroupMappingEntry(
                            priority = 1, 
                            upstream_group_name = 'Company Team (.*)', 
                            upstream_name_is_a_guid = False, 
                            agilicus_group_name = 'Agilicus {0}', 
                            group_org_id = 'asdfg123hjkl', )
                        ], 
                    excluded_groups = [
                        agilicus_api.models.upstream_group_excluded_entry.UpstreamGroupExcludedEntry(
                            upstream_group_name = 'Admin*', 
                            upstream_name_is_a_guid = False, )
                        ], ),
        )

    def testUpstreamGroupMapping(self):
        """Test UpstreamGroupMapping"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
