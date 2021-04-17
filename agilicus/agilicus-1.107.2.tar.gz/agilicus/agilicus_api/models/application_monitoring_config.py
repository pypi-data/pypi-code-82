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


class ApplicationMonitoringConfig(object):
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
        'port': 'int',
        'path': 'str'
    }

    attribute_map = {
        'port': 'port',
        'path': 'path'
    }

    def __init__(self, port=None, path='/metrics', local_vars_configuration=None):  # noqa: E501
        """ApplicationMonitoringConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._port = None
        self._path = None
        self.discriminator = None

        self.port = port
        if path is not None:
            self.path = path

    @property
    def port(self):
        """Gets the port of this ApplicationMonitoringConfig.  # noqa: E501

        The port to access for metrics. If unset uses the application's port.  # noqa: E501

        :return: The port of this ApplicationMonitoringConfig.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ApplicationMonitoringConfig.

        The port to access for metrics. If unset uses the application's port.  # noqa: E501

        :param port: The port of this ApplicationMonitoringConfig.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                port is not None and port > 65535):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value less than or equal to `65535`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                port is not None and port < 1):  # noqa: E501
            raise ValueError("Invalid value for `port`, must be a value greater than or equal to `1`")  # noqa: E501

        self._port = port

    @property
    def path(self):
        """Gets the path of this ApplicationMonitoringConfig.  # noqa: E501

        The path to scrape prometheus metrics from  # noqa: E501

        :return: The path of this ApplicationMonitoringConfig.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ApplicationMonitoringConfig.

        The path to scrape prometheus metrics from  # noqa: E501

        :param path: The path of this ApplicationMonitoringConfig.  # noqa: E501
        :type: str
        """

        self._path = path

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
        if not isinstance(other, ApplicationMonitoringConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplicationMonitoringConfig):
            return True

        return self.to_dict() != other.to_dict()
