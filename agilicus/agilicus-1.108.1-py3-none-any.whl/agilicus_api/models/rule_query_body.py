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


class RuleQueryBody(object):
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
        'json': 'list[RuleQueryBodyJSON]'
    }

    attribute_map = {
        'json': 'json'
    }

    def __init__(self, json=None, local_vars_configuration=None):  # noqa: E501
        """RuleQueryBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._json = None
        self.discriminator = None

        if json is not None:
            self.json = json

    @property
    def json(self):
        """Gets the json of this RuleQueryBody.  # noqa: E501

        Rule query body array  # noqa: E501

        :return: The json of this RuleQueryBody.  # noqa: E501
        :rtype: list[RuleQueryBodyJSON]
        """
        return self._json

    @json.setter
    def json(self, json):
        """Sets the json of this RuleQueryBody.

        Rule query body array  # noqa: E501

        :param json: The json of this RuleQueryBody.  # noqa: E501
        :type: list[RuleQueryBodyJSON]
        """

        self._json = json

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
        if not isinstance(other, RuleQueryBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RuleQueryBody):
            return True

        return self.to_dict() != other.to_dict()
