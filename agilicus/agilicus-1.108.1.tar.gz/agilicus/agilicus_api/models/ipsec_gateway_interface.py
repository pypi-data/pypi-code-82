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


class IpsecGatewayInterface(object):
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
        'hostname': 'str',
        'certificate_dn': 'str'
    }

    attribute_map = {
        'name': 'name',
        'hostname': 'hostname',
        'certificate_dn': 'certificate_dn'
    }

    def __init__(self, name=None, hostname=None, certificate_dn=None, local_vars_configuration=None):  # noqa: E501
        """IpsecGatewayInterface - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._hostname = None
        self._certificate_dn = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if hostname is not None:
            self.hostname = hostname
        if certificate_dn is not None:
            self.certificate_dn = certificate_dn

    @property
    def name(self):
        """Gets the name of this IpsecGatewayInterface.  # noqa: E501

        Name of the gateway interface. This name must be a legal RFC1123 label, and corresponds to the subdomain of the gateway interface.   # noqa: E501

        :return: The name of this IpsecGatewayInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IpsecGatewayInterface.

        Name of the gateway interface. This name must be a legal RFC1123 label, and corresponds to the subdomain of the gateway interface.   # noqa: E501

        :param name: The name of this IpsecGatewayInterface.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 63):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `63`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])/`")  # noqa: E501

        self._name = name

    @property
    def hostname(self):
        """Gets the hostname of this IpsecGatewayInterface.  # noqa: E501

        The hostname of the gateway interface. This is readOnly, and is generated from the name plus the gateway domain name.   # noqa: E501

        :return: The hostname of this IpsecGatewayInterface.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this IpsecGatewayInterface.

        The hostname of the gateway interface. This is readOnly, and is generated from the name plus the gateway domain name.   # noqa: E501

        :param hostname: The hostname of this IpsecGatewayInterface.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def certificate_dn(self):
        """Gets the certificate_dn of this IpsecGatewayInterface.  # noqa: E501

        Certificate distinguished name (DN) subject of the gateway interface  # noqa: E501

        :return: The certificate_dn of this IpsecGatewayInterface.  # noqa: E501
        :rtype: str
        """
        return self._certificate_dn

    @certificate_dn.setter
    def certificate_dn(self, certificate_dn):
        """Sets the certificate_dn of this IpsecGatewayInterface.

        Certificate distinguished name (DN) subject of the gateway interface  # noqa: E501

        :param certificate_dn: The certificate_dn of this IpsecGatewayInterface.  # noqa: E501
        :type: str
        """

        self._certificate_dn = certificate_dn

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
        if not isinstance(other, IpsecGatewayInterface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpsecGatewayInterface):
            return True

        return self.to_dict() != other.to_dict()
