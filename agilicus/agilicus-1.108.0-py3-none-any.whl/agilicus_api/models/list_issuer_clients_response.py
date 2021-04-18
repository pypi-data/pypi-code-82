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


class ListIssuerClientsResponse(object):
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
        'clients': 'list[IssuerClient]',
        'limit': 'int'
    }

    attribute_map = {
        'clients': 'clients',
        'limit': 'limit'
    }

    def __init__(self, clients=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """ListIssuerClientsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._clients = None
        self._limit = None
        self.discriminator = None

        if clients is not None:
            self.clients = clients
        self.limit = limit

    @property
    def clients(self):
        """Gets the clients of this ListIssuerClientsResponse.  # noqa: E501

        List of IssuerClients  # noqa: E501

        :return: The clients of this ListIssuerClientsResponse.  # noqa: E501
        :rtype: list[IssuerClient]
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this ListIssuerClientsResponse.

        List of IssuerClients  # noqa: E501

        :param clients: The clients of this ListIssuerClientsResponse.  # noqa: E501
        :type: list[IssuerClient]
        """

        self._clients = clients

    @property
    def limit(self):
        """Gets the limit of this ListIssuerClientsResponse.  # noqa: E501

        Limit of IssuerClients in the response  # noqa: E501

        :return: The limit of this ListIssuerClientsResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListIssuerClientsResponse.

        Limit of IssuerClients in the response  # noqa: E501

        :param limit: The limit of this ListIssuerClientsResponse.  # noqa: E501
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
        if not isinstance(other, ListIssuerClientsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListIssuerClientsResponse):
            return True

        return self.to_dict() != other.to_dict()
