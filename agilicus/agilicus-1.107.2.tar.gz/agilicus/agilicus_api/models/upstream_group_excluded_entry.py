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


class UpstreamGroupExcludedEntry(object):
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
        'upstream_group_name': 'str',
        'upstream_name_is_a_guid': 'bool'
    }

    attribute_map = {
        'upstream_group_name': 'upstream_group_name',
        'upstream_name_is_a_guid': 'upstream_name_is_a_guid'
    }

    def __init__(self, upstream_group_name=None, upstream_name_is_a_guid=None, local_vars_configuration=None):  # noqa: E501
        """UpstreamGroupExcludedEntry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._upstream_group_name = None
        self._upstream_name_is_a_guid = None
        self.discriminator = None

        self.upstream_group_name = upstream_group_name
        if upstream_name_is_a_guid is not None:
            self.upstream_name_is_a_guid = upstream_name_is_a_guid

    @property
    def upstream_group_name(self):
        """Gets the upstream_group_name of this UpstreamGroupExcludedEntry.  # noqa: E501

        The name of the group in your upstream identity provider that you want to map. This can be in the form of a regular expression.   # noqa: E501

        :return: The upstream_group_name of this UpstreamGroupExcludedEntry.  # noqa: E501
        :rtype: str
        """
        return self._upstream_group_name

    @upstream_group_name.setter
    def upstream_group_name(self, upstream_group_name):
        """Sets the upstream_group_name of this UpstreamGroupExcludedEntry.

        The name of the group in your upstream identity provider that you want to map. This can be in the form of a regular expression.   # noqa: E501

        :param upstream_group_name: The upstream_group_name of this UpstreamGroupExcludedEntry.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and upstream_group_name is None:  # noqa: E501
            raise ValueError("Invalid value for `upstream_group_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                upstream_group_name is not None and len(upstream_group_name) > 100):
            raise ValueError("Invalid value for `upstream_group_name`, length must be less than or equal to `100`")  # noqa: E501

        self._upstream_group_name = upstream_group_name

    @property
    def upstream_name_is_a_guid(self):
        """Gets the upstream_name_is_a_guid of this UpstreamGroupExcludedEntry.  # noqa: E501

        Indicates that the supplied upstream_group_name will be found in the list of group IDs  # noqa: E501

        :return: The upstream_name_is_a_guid of this UpstreamGroupExcludedEntry.  # noqa: E501
        :rtype: bool
        """
        return self._upstream_name_is_a_guid

    @upstream_name_is_a_guid.setter
    def upstream_name_is_a_guid(self, upstream_name_is_a_guid):
        """Sets the upstream_name_is_a_guid of this UpstreamGroupExcludedEntry.

        Indicates that the supplied upstream_group_name will be found in the list of group IDs  # noqa: E501

        :param upstream_name_is_a_guid: The upstream_name_is_a_guid of this UpstreamGroupExcludedEntry.  # noqa: E501
        :type: bool
        """

        self._upstream_name_is_a_guid = upstream_name_is_a_guid

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
        if not isinstance(other, UpstreamGroupExcludedEntry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpstreamGroupExcludedEntry):
            return True

        return self.to_dict() != other.to_dict()
