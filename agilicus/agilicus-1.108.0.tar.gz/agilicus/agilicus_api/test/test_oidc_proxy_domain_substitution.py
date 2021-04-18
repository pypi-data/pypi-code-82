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
from agilicus_api.models.oidc_proxy_domain_substitution import OIDCProxyDomainSubstitution  # noqa: E501
from agilicus_api.rest import ApiException

class TestOIDCProxyDomainSubstitution(unittest.TestCase):
    """OIDCProxyDomainSubstitution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OIDCProxyDomainSubstitution
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.oidc_proxy_domain_substitution.OIDCProxyDomainSubstitution()  # noqa: E501
        if include_optional :
            return OIDCProxyDomainSubstitution(
                standard_headers = agilicus_api.models.oidc_proxy_standard_header.OIDCProxyStandardHeader(
                    location = True, 
                    origin = True, 
                    host = True, ), 
                other_headers = [
                    agilicus_api.models.oidc_proxy_header_mapping.OIDCProxyHeaderMapping(
                        name = 'Accept-Encoding', 
                        value = '*', )
                    ]
            )
        else :
            return OIDCProxyDomainSubstitution(
        )

    def testOIDCProxyDomainSubstitution(self):
        """Test OIDCProxyDomainSubstitution"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
