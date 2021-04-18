# coding: utf-8

"""
    Agilicus API

    Agilicus API endpoints  # noqa: E501

    The version of the OpenAPI document: 2021.04.16
    Contact: dev@agilicus.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from agilicus_api.configuration import Configuration


class AccessRequestsStatus(object):
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
        'user': 'User',
        'user_requests': 'list[UserRequestInfo]'
    }

    attribute_map = {
        'user': 'user',
        'user_requests': 'user_requests'
    }

    def __init__(self, user=None, user_requests=None, local_vars_configuration=None):  # noqa: E501
        """AccessRequestsStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._user_requests = None
        self.discriminator = None

        self.user = user
        self.user_requests = user_requests

    @property
    def user(self):
        """Gets the user of this AccessRequestsStatus.  # noqa: E501


        :return: The user of this AccessRequestsStatus.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AccessRequestsStatus.


        :param user: The user of this AccessRequestsStatus.  # noqa: E501
        :type: User
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def user_requests(self):
        """Gets the user_requests of this AccessRequestsStatus.  # noqa: E501

        The matching UserRequestInfo objects  # noqa: E501

        :return: The user_requests of this AccessRequestsStatus.  # noqa: E501
        :rtype: list[UserRequestInfo]
        """
        return self._user_requests

    @user_requests.setter
    def user_requests(self, user_requests):
        """Sets the user_requests of this AccessRequestsStatus.

        The matching UserRequestInfo objects  # noqa: E501

        :param user_requests: The user_requests of this AccessRequestsStatus.  # noqa: E501
        :type: list[UserRequestInfo]
        """
        if self.local_vars_configuration.client_side_validation and user_requests is None:  # noqa: E501
            raise ValueError("Invalid value for `user_requests`, must not be `None`")  # noqa: E501

        self._user_requests = user_requests

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
        if not isinstance(other, AccessRequestsStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessRequestsStatus):
            return True

        return self.to_dict() != other.to_dict()
