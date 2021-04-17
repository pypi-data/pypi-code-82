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


class IpsecConnection(object):
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
        'name': 'str',
        'inherit_from': 'str',
        'gateway_interface': 'IpsecGatewayInterface',
        'spec': 'IpsecConnectionSpec'
    }

    attribute_map = {
        'name': 'name',
        'inherit_from': 'inherit_from',
        'gateway_interface': 'gateway_interface',
        'spec': 'spec'
    }

    def __init__(self, name=None, inherit_from=None, gateway_interface=None, spec=None, local_vars_configuration=None):  # noqa: E501
        """IpsecConnection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._inherit_from = None
        self._gateway_interface = None
        self._spec = None
        self.discriminator = None

        self.name = name
        if inherit_from is not None:
            self.inherit_from = inherit_from
        if gateway_interface is not None:
            self.gateway_interface = gateway_interface
        if spec is not None:
            self.spec = spec

    @property
    def name(self):
        """Gets the name of this IpsecConnection.  # noqa: E501

        A descriptive name for the ipsec connection. The name must be a unique within a connectors connections.   # noqa: E501

        :return: The name of this IpsecConnection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpsecConnection.

        A descriptive name for the ipsec connection. The name must be a unique within a connectors connections.   # noqa: E501

        :param name: The name of this IpsecConnection.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def inherit_from(self):
        """Gets the inherit_from of this IpsecConnection.  # noqa: E501

        Allows inheriting from a named spec object. If any configuration in this object is Null or undefined, it will inherit from the named source that is part of the connector. Loops are not permitted, ie. A->B->A, and will result in a bad request.   # noqa: E501

        :return: The inherit_from of this IpsecConnection.  # noqa: E501
        :rtype: str
        """
        return self._inherit_from

    @inherit_from.setter
    def inherit_from(self, inherit_from):
        """Sets the inherit_from of this IpsecConnection.

        Allows inheriting from a named spec object. If any configuration in this object is Null or undefined, it will inherit from the named source that is part of the connector. Loops are not permitted, ie. A->B->A, and will result in a bad request.   # noqa: E501

        :param inherit_from: The inherit_from of this IpsecConnection.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                inherit_from is not None and len(inherit_from) > 100):
            raise ValueError("Invalid value for `inherit_from`, length must be less than or equal to `100`")  # noqa: E501

        self._inherit_from = inherit_from

    @property
    def gateway_interface(self):
        """Gets the gateway_interface of this IpsecConnection.  # noqa: E501


        :return: The gateway_interface of this IpsecConnection.  # noqa: E501
        :rtype: IpsecGatewayInterface
        """
        return self._gateway_interface

    @gateway_interface.setter
    def gateway_interface(self, gateway_interface):
        """Sets the gateway_interface of this IpsecConnection.


        :param gateway_interface: The gateway_interface of this IpsecConnection.  # noqa: E501
        :type: IpsecGatewayInterface
        """

        self._gateway_interface = gateway_interface

    @property
    def spec(self):
        """Gets the spec of this IpsecConnection.  # noqa: E501


        :return: The spec of this IpsecConnection.  # noqa: E501
        :rtype: IpsecConnectionSpec
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this IpsecConnection.


        :param spec: The spec of this IpsecConnection.  # noqa: E501
        :type: IpsecConnectionSpec
        """

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
        if not isinstance(other, IpsecConnection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpsecConnection):
            return True

        return self.to_dict() != other.to_dict()
