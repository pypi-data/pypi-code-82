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
from agilicus_api.models.oidc_upstream_identity_provider import OIDCUpstreamIdentityProvider  # noqa: E501
from agilicus_api.rest import ApiException

class TestOIDCUpstreamIdentityProvider(unittest.TestCase):
    """OIDCUpstreamIdentityProvider unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OIDCUpstreamIdentityProvider
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.oidc_upstream_identity_provider.OIDCUpstreamIdentityProvider()  # noqa: E501
        if include_optional :
            return OIDCUpstreamIdentityProvider(
                name = '0', 
                icon = 'city-login', 
                issuer = '0', 
                client_id = '0', 
                client_secret = '0', 
                issuer_external_host = '0', 
                username_key = '0', 
                email_key = '0', 
                email_verification_required = True, 
                request_user_info = True, 
                user_id_key = '0', 
                auto_create_status = 'active'
            )
        else :
            return OIDCUpstreamIdentityProvider(
                name = '0',
                issuer = '0',
                client_id = '0',
        )

    def testOIDCUpstreamIdentityProvider(self):
        """Test OIDCUpstreamIdentityProvider"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
