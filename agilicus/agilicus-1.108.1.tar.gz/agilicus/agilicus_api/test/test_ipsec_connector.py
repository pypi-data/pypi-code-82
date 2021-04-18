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
from agilicus_api.models.ipsec_connector import IpsecConnector  # noqa: E501
from agilicus_api.rest import ApiException

class TestIpsecConnector(unittest.TestCase):
    """IpsecConnector unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IpsecConnector
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.ipsec_connector.IpsecConnector()  # noqa: E501
        if include_optional :
            return IpsecConnector(
                metadata = {"id":"ac233asaksjfF","created":"2017-07-07T15:49:51.230+00:00","updated":"2020-01-27T12:19:46.430+00:00"}, 
                spec = agilicus_api.models.ipsec_connector_spec.IpsecConnectorSpec(
                    name = 'ipsec1', 
                    name_slug = 'a', 
                    org_id = '123', 
                    ipsec_gateway_id = '1234', 
                    connections = [
                        agilicus_api.models.ipsec_connection.IpsecConnection(
                            name = '0', 
                            inherit_from = '0', 
                            gateway_interface = agilicus_api.models.ipsec_gateway_interface.IpsecGatewayInterface(
                                name = 'a', 
                                hostname = 'vpn-1', 
                                certificate_dn = 'C=US, O=LetsEncrypt, CN=R3', ), )
                        ], ), 
                status = agilicus_api.models.ipsec_connector_status.IpsecConnectorStatus(
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
                        ], )
            )
        else :
            return IpsecConnector(
        )

    def testIpsecConnector(self):
        """Test IpsecConnector"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
