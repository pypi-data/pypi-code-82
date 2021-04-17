# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mailslurp_client
from mailslurp_client.models.page_contact_projection import PageContactProjection  # noqa: E501
from mailslurp_client.rest import ApiException

class TestPageContactProjection(unittest.TestCase):
    """PageContactProjection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PageContactProjection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mailslurp_client.models.page_contact_projection.PageContactProjection()  # noqa: E501
        if include_optional :
            return PageContactProjection(
                content = [
                    mailslurp_client.models.contact_projection.ContactProjection(
                        company = '0', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        email_addresses = [
                            '0'
                            ], 
                        first_name = '0', 
                        group_id = '0', 
                        id = '0', 
                        last_name = '0', 
                        opt_out = True, )
                    ], 
                empty = True, 
                first = True, 
                last = True, 
                number = 56, 
                number_of_elements = 56, 
                pageable = mailslurp_client.models.pageable.Pageable(
                    offset = 56, 
                    page_number = 56, 
                    page_size = 56, 
                    paged = True, 
                    sort = mailslurp_client.models.sort.Sort(
                        empty = True, 
                        sorted = True, 
                        unsorted = True, ), 
                    unpaged = True, ), 
                size = 56, 
                sort = mailslurp_client.models.sort.Sort(
                    empty = True, 
                    sorted = True, 
                    unsorted = True, ), 
                total_elements = 56, 
                total_pages = 56
            )
        else :
            return PageContactProjection(
        )

    def testPageContactProjection(self):
        """Test PageContactProjection"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
