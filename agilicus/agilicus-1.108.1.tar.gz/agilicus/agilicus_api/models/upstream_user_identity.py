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


class UpstreamUserIdentity(object):
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
        'metadata': 'MetadataWithId',
        'spec': 'UpstreamUserIdentitySpec'
    }

    attribute_map = {
        'metadata': 'metadata',
        'spec': 'spec'
    }

    def __init__(self, metadata=None, spec=None, local_vars_configuration=None):  # noqa: E501
        """UpstreamUserIdentity - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._metadata = None
        self._spec = None
        self.discriminator = None

        if metadata is not None:
            self.metadata = metadata
        self.spec = spec

    @property
    def metadata(self):
        """Gets the metadata of this UpstreamUserIdentity.  # noqa: E501


        :return: The metadata of this UpstreamUserIdentity.  # noqa: E501
        :rtype: MetadataWithId
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpstreamUserIdentity.


        :param metadata: The metadata of this UpstreamUserIdentity.  # noqa: E501
        :type: MetadataWithId
        """

        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this UpstreamUserIdentity.  # noqa: E501


        :return: The spec of this UpstreamUserIdentity.  # noqa: E501
        :rtype: UpstreamUserIdentitySpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this UpstreamUserIdentity.


        :param spec: The spec of this UpstreamUserIdentity.  # noqa: E501
        :type: UpstreamUserIdentitySpec
        """
        if self.local_vars_configuration.client_side_validation and spec is None:  # noqa: E501
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

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
        if not isinstance(other, UpstreamUserIdentity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpstreamUserIdentity):
            return True

        return self.to_dict() != other.to_dict()
