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


class ServiceForwarderStatus(object):
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
        'connection_uri': 'str',
        'application_service': 'ApplicationService'
    }

    attribute_map = {
        'connection_uri': 'connection_uri',
        'application_service': 'application_service'
    }

    def __init__(self, connection_uri=None, application_service=None, local_vars_configuration=None):  # noqa: E501
        """ServiceForwarderStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._connection_uri = None
        self._application_service = None
        self.discriminator = None

        if connection_uri is not None:
            self.connection_uri = connection_uri
        if application_service is not None:
            self.application_service = application_service

    @property
    def connection_uri(self):
        """Gets the connection_uri of this ServiceForwarderStatus.  # noqa: E501

        The connection uri used to connect to the application service.   # noqa: E501

        :return: The connection_uri of this ServiceForwarderStatus.  # noqa: E501
        :rtype: str
        """
        return self._connection_uri

    @connection_uri.setter
    def connection_uri(self, connection_uri):
        """Sets the connection_uri of this ServiceForwarderStatus.

        The connection uri used to connect to the application service.   # noqa: E501

        :param connection_uri: The connection_uri of this ServiceForwarderStatus.  # noqa: E501
        :type: str
        """

        self._connection_uri = connection_uri

    @property
    def application_service(self):
        """Gets the application_service of this ServiceForwarderStatus.  # noqa: E501


        :return: The application_service of this ServiceForwarderStatus.  # noqa: E501
        :rtype: ApplicationService
        """
        return self._application_service

    @application_service.setter
    def application_service(self, application_service):
        """Sets the application_service of this ServiceForwarderStatus.


        :param application_service: The application_service of this ServiceForwarderStatus.  # noqa: E501
        :type: ApplicationService
        """

        self._application_service = application_service

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
        if not isinstance(other, ServiceForwarderStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ServiceForwarderStatus):
            return True

        return self.to_dict() != other.to_dict()
