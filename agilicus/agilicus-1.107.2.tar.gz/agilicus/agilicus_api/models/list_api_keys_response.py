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


class ListAPIKeysResponse(object):
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
        'api_keys': 'list[APIKey]',
        'limit': 'int'
    }

    attribute_map = {
        'api_keys': 'api_keys',
        'limit': 'limit'
    }

    def __init__(self, api_keys=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """ListAPIKeysResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_keys = None
        self._limit = None
        self.discriminator = None

        self.api_keys = api_keys
        self.limit = limit

    @property
    def api_keys(self):
        """Gets the api_keys of this ListAPIKeysResponse.  # noqa: E501

        The matching APIKey objects  # noqa: E501

        :return: The api_keys of this ListAPIKeysResponse.  # noqa: E501
        :rtype: list[APIKey]
        """
        return self._api_keys

    @api_keys.setter
    def api_keys(self, api_keys):
        """Sets the api_keys of this ListAPIKeysResponse.

        The matching APIKey objects  # noqa: E501

        :param api_keys: The api_keys of this ListAPIKeysResponse.  # noqa: E501
        :type: list[APIKey]
        """
        if self.local_vars_configuration.client_side_validation and api_keys is None:  # noqa: E501
            raise ValueError("Invalid value for `api_keys`, must not be `None`")  # noqa: E501

        self._api_keys = api_keys

    @property
    def limit(self):
        """Gets the limit of this ListAPIKeysResponse.  # noqa: E501

        Limit on the number of rows in the response  # noqa: E501

        :return: The limit of this ListAPIKeysResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListAPIKeysResponse.

        Limit on the number of rows in the response  # noqa: E501

        :param limit: The limit of this ListAPIKeysResponse.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

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
        if not isinstance(other, ListAPIKeysResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListAPIKeysResponse):
            return True

        return self.to_dict() != other.to_dict()
