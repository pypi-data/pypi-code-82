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
from agilicus_api.models.local_auth_upstream_identity_provider import LocalAuthUpstreamIdentityProvider  # noqa: E501
from agilicus_api.rest import ApiException

class TestLocalAuthUpstreamIdentityProvider(unittest.TestCase):
    """LocalAuthUpstreamIdentityProvider unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LocalAuthUpstreamIdentityProvider
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.local_auth_upstream_identity_provider.LocalAuthUpstreamIdentityProvider()  # noqa: E501
        if include_optional :
            return LocalAuthUpstreamIdentityProvider(
                name = '0', 
                issuer = '0', 
                upstream_type = 'oidc', 
                icon = 'city-login', 
                auto_create_status = 'active', 
                upstream_id = '123'
            )
        else :
            return LocalAuthUpstreamIdentityProvider(
                upstream_id = '123',
        )

    def testLocalAuthUpstreamIdentityProvider(self):
        """Test LocalAuthUpstreamIdentityProvider"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
