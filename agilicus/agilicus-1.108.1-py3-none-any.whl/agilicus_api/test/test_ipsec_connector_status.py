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
from agilicus_api.models.ipsec_connector_status import IpsecConnectorStatus  # noqa: E501
from agilicus_api.rest import ApiException

class TestIpsecConnectorStatus(unittest.TestCase):
    """IpsecConnectorStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IpsecConnectorStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.ipsec_connector_status.IpsecConnectorStatus()  # noqa: E501
        if include_optional :
            return IpsecConnectorStatus(
                application_services = [
                    agilicus_api.models.application_service.ApplicationService(
                        created = '2015-07-07T15:49:51.230+02:00', 
                        id = '123', 
                        name = 'my-local-service', 
                        org_id = '0', 
                        hostname = 'db.example.com', 
                        ipv4_addresses = [
                            '192.0.2.1'
                            ], 
                        name_resolution = 'static', 
                        port = 56, 
                        protocol = 'tcp', 
                        assignments = [
                            agilicus_api.models.application_service_assignment.ApplicationServiceAssignment(
                                app_id = '0', 
                                environment_name = '0', 
                                org_id = '0', )
                            ], 
                        updated = '2015-07-07T15:49:51.230+02:00', 
                        service_type = 'vpn', 
                        service_protocol_type = 'ip', 
                        tls_enabled = True, 
                        tls_verify = True, 
                        connector_id = '123', 
                        connection_uri = '0', )
                    ]
            )
        else :
            return IpsecConnectorStatus(
        )

    def testIpsecConnectorStatus(self):
        """Test IpsecConnectorStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
