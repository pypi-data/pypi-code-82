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


class RawToken(object):
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
        'token': 'str',
        'session': 'str',
        'time_validity': 'TimeValidity'
    }

    attribute_map = {
        'token': 'token',
        'session': 'session',
        'time_validity': 'time_validity'
    }

    def __init__(self, token=None, session=None, time_validity=None, local_vars_configuration=None):  # noqa: E501
        """RawToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._token = None
        self._session = None
        self._time_validity = None
        self.discriminator = None

        self.token = token
        if session is not None:
            self.session = session
        if time_validity is not None:
            self.time_validity = time_validity

    @property
    def token(self):
        """Gets the token of this RawToken.  # noqa: E501

        token string  # noqa: E501

        :return: The token of this RawToken.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this RawToken.

        token string  # noqa: E501

        :param token: The token of this RawToken.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and token is None:  # noqa: E501
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501

        self._token = token

    @property
    def session(self):
        """Gets the session of this RawToken.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The session of this RawToken.  # noqa: E501
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """Sets the session of this RawToken.

        Unique identifier  # noqa: E501

        :param session: The session of this RawToken.  # noqa: E501
        :type: str
        """

        self._session = session

    @property
    def time_validity(self):
        """Gets the time_validity of this RawToken.  # noqa: E501


        :return: The time_validity of this RawToken.  # noqa: E501
        :rtype: TimeValidity
        """
        return self._time_validity

    @time_validity.setter
    def time_validity(self, time_validity):
        """Sets the time_validity of this RawToken.


        :param time_validity: The time_validity of this RawToken.  # noqa: E501
        :type: TimeValidity
        """

        self._time_validity = time_validity

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
        if not isinstance(other, RawToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RawToken):
            return True

        return self.to_dict() != other.to_dict()
