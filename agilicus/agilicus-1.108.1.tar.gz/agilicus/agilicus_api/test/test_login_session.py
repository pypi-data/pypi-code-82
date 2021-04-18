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
from agilicus_api.models.login_session import LoginSession  # noqa: E501
from agilicus_api.rest import ApiException

class TestLoginSession(unittest.TestCase):
    """LoginSession unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LoginSession
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = agilicus_api.models.login_session.LoginSession()  # noqa: E501
        if include_optional :
            return LoginSession(
                session_id = 'abc123iamaguid', 
                number_of_logins = 3, 
                number_of_failed_multi_factor_challenges = 3, 
                single_sign_on_time = '2015-07-07T15:49:51.230+02:00', 
                user_is_authenticated = True, 
                user_is_authenticated_by_upstream = True, 
                user_is_authenticated_by_cache = True
            )
        else :
            return LoginSession(
                session_id = 'abc123iamaguid',
                number_of_logins = 3,
                number_of_failed_multi_factor_challenges = 3,
                single_sign_on_time = '2015-07-07T15:49:51.230+02:00',
                user_is_authenticated = True,
                user_is_authenticated_by_upstream = True,
                user_is_authenticated_by_cache = True,
        )

    def testLoginSession(self):
        """Test LoginSession"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
