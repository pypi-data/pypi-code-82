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
from agilicus_api.models.file_share_service import FileShareService  # noqa: E501
from agilicus_api.rest import ApiException

class TestFileShareService(unittest.TestCase):
    """FileShareService unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileShareService
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.file_share_service.FileShareService()  # noqa: E501
        if include_optional :
            return FileShareService(
                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                spec = agilicus_api.models.file_share_service_spec.FileShareServiceSpec(
                    name = 'share1', 
                    share_name = 'share1', 
                    org_id = '123', 
                    local_path = '/home/agilicus/public/share1', 
                    connector_id = '123', 
                    share_index = 1, 
                    transport_end_to_end_tls = True, 
                    transport_base_domain = '0', ), 
                status = agilicus_api.models.file_share_service_status.FileShareServiceStatus(
                    share_base_app_name = '0', 
                    instance_id = 'asdas9Gk4asdaTH', 
                    instance_org_id = '39ddfGAaslts8qX', 
                    share_uri = 'https://share-4.cloud.egov.city/', )
            )
        else :
            return FileShareService(
                spec = agilicus_api.models.file_share_service_spec.FileShareServiceSpec(
                    name = 'share1', 
                    share_name = 'share1', 
                    org_id = '123', 
                    local_path = '/home/agilicus/public/share1', 
                    connector_id = '123', 
                    share_index = 1, 
                    transport_end_to_end_tls = True, 
                    transport_base_domain = '0', ),
        )

    def testFileShareService(self):
        """Test FileShareService"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
