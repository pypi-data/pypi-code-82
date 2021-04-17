# coding: utf-8

"""
    MailSlurp API

    MailSlurp is an API for sending and receiving emails from dynamically allocated email addresses. It's designed for developers and QA teams to test applications, process inbound emails, send templated notifications, attachments, and more.   ## Resources - [Homepage](https://www.mailslurp.com) - Get an [API KEY](https://app.mailslurp.com/sign-up/) - Generated [SDK Clients](https://www.mailslurp.com/docs/) - [Examples](https://github.com/mailslurp/examples) repository   # noqa: E501

    The version of the OpenAPI document: 6.5.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from mailslurp_client.configuration import Configuration


class MissedEmail(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'attachment_count': 'int',
        'bcc': 'list[str]',
        'body_excerpt': 'str',
        'cc': 'list[str]',
        'created_at': 'datetime',
        '_from': 'str',
        'id': 'str',
        'inbox_ids': 'list[str]',
        'subject': 'str',
        'to': 'list[str]',
        'updated_at': 'datetime',
        'user_id': 'str'
    }

    attribute_map = {
        'attachment_count': 'attachmentCount',
        'bcc': 'bcc',
        'body_excerpt': 'bodyExcerpt',
        'cc': 'cc',
        'created_at': 'createdAt',
        '_from': 'from',
        'id': 'id',
        'inbox_ids': 'inboxIds',
        'subject': 'subject',
        'to': 'to',
        'updated_at': 'updatedAt',
        'user_id': 'userId'
    }

    def __init__(self, attachment_count=None, bcc=None, body_excerpt=None, cc=None, created_at=None, _from=None, id=None, inbox_ids=None, subject=None, to=None, updated_at=None, user_id=None, local_vars_configuration=None):  # noqa: E501
        """MissedEmail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attachment_count = None
        self._bcc = None
        self._body_excerpt = None
        self._cc = None
        self._created_at = None
        self.__from = None
        self._id = None
        self._inbox_ids = None
        self._subject = None
        self._to = None
        self._updated_at = None
        self._user_id = None
        self.discriminator = None

        self.attachment_count = attachment_count
        self.bcc = bcc
        if body_excerpt is not None:
            self.body_excerpt = body_excerpt
        self.cc = cc
        self.created_at = created_at
        if _from is not None:
            self._from = _from
        if id is not None:
            self.id = id
        self.inbox_ids = inbox_ids
        if subject is not None:
            self.subject = subject
        self.to = to
        self.updated_at = updated_at
        self.user_id = user_id

    @property
    def attachment_count(self):
        """Gets the attachment_count of this MissedEmail.  # noqa: E501


        :return: The attachment_count of this MissedEmail.  # noqa: E501
        :rtype: int
        """
        return self._attachment_count

    @attachment_count.setter
    def attachment_count(self, attachment_count):
        """Sets the attachment_count of this MissedEmail.


        :param attachment_count: The attachment_count of this MissedEmail.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and attachment_count is None:  # noqa: E501
            raise ValueError("Invalid value for `attachment_count`, must not be `None`")  # noqa: E501

        self._attachment_count = attachment_count

    @property
    def bcc(self):
        """Gets the bcc of this MissedEmail.  # noqa: E501


        :return: The bcc of this MissedEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this MissedEmail.


        :param bcc: The bcc of this MissedEmail.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and bcc is None:  # noqa: E501
            raise ValueError("Invalid value for `bcc`, must not be `None`")  # noqa: E501

        self._bcc = bcc

    @property
    def body_excerpt(self):
        """Gets the body_excerpt of this MissedEmail.  # noqa: E501


        :return: The body_excerpt of this MissedEmail.  # noqa: E501
        :rtype: str
        """
        return self._body_excerpt

    @body_excerpt.setter
    def body_excerpt(self, body_excerpt):
        """Sets the body_excerpt of this MissedEmail.


        :param body_excerpt: The body_excerpt of this MissedEmail.  # noqa: E501
        :type: str
        """

        self._body_excerpt = body_excerpt

    @property
    def cc(self):
        """Gets the cc of this MissedEmail.  # noqa: E501


        :return: The cc of this MissedEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this MissedEmail.


        :param cc: The cc of this MissedEmail.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and cc is None:  # noqa: E501
            raise ValueError("Invalid value for `cc`, must not be `None`")  # noqa: E501

        self._cc = cc

    @property
    def created_at(self):
        """Gets the created_at of this MissedEmail.  # noqa: E501


        :return: The created_at of this MissedEmail.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MissedEmail.


        :param created_at: The created_at of this MissedEmail.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def _from(self):
        """Gets the _from of this MissedEmail.  # noqa: E501


        :return: The _from of this MissedEmail.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this MissedEmail.


        :param _from: The _from of this MissedEmail.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def id(self):
        """Gets the id of this MissedEmail.  # noqa: E501


        :return: The id of this MissedEmail.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MissedEmail.


        :param id: The id of this MissedEmail.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inbox_ids(self):
        """Gets the inbox_ids of this MissedEmail.  # noqa: E501


        :return: The inbox_ids of this MissedEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._inbox_ids

    @inbox_ids.setter
    def inbox_ids(self, inbox_ids):
        """Sets the inbox_ids of this MissedEmail.


        :param inbox_ids: The inbox_ids of this MissedEmail.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and inbox_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `inbox_ids`, must not be `None`")  # noqa: E501

        self._inbox_ids = inbox_ids

    @property
    def subject(self):
        """Gets the subject of this MissedEmail.  # noqa: E501


        :return: The subject of this MissedEmail.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this MissedEmail.


        :param subject: The subject of this MissedEmail.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def to(self):
        """Gets the to of this MissedEmail.  # noqa: E501


        :return: The to of this MissedEmail.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this MissedEmail.


        :param to: The to of this MissedEmail.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def updated_at(self):
        """Gets the updated_at of this MissedEmail.  # noqa: E501


        :return: The updated_at of this MissedEmail.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this MissedEmail.


        :param updated_at: The updated_at of this MissedEmail.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this MissedEmail.  # noqa: E501


        :return: The user_id of this MissedEmail.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MissedEmail.


        :param user_id: The user_id of this MissedEmail.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MissedEmail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MissedEmail):
            return True

        return self.to_dict() != other.to_dict()
