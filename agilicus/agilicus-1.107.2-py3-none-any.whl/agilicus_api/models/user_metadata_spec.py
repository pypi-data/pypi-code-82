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


class UserMetadataSpec(object):
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
        'user_id': 'str',
        'org_id': 'str',
        'app_id': 'str',
        'name': 'str',
        'data_type': 'str',
        'data': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'org_id': 'org_id',
        'app_id': 'app_id',
        'name': 'name',
        'data_type': 'data_type',
        'data': 'data'
    }

    def __init__(self, user_id=None, org_id=None, app_id=None, name=None, data_type=None, data=None, local_vars_configuration=None):  # noqa: E501
        """UserMetadataSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._org_id = None
        self._app_id = None
        self._name = None
        self._data_type = None
        self._data = None
        self.discriminator = None

        self.user_id = user_id
        self.org_id = org_id
        self.app_id = app_id
        if name is not None:
            self.name = name
        if data_type is not None:
            self.data_type = data_type
        if data is not None:
            self.data = data

    @property
    def user_id(self):
        """Gets the user_id of this UserMetadataSpec.  # noqa: E501

        The unique id of the User to which this record applies.   # noqa: E501

        :return: The user_id of this UserMetadataSpec.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserMetadataSpec.

        The unique id of the User to which this record applies.   # noqa: E501

        :param user_id: The user_id of this UserMetadataSpec.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) > 40):
            raise ValueError("Invalid value for `user_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                user_id is not None and len(user_id) < 1):
            raise ValueError("Invalid value for `user_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._user_id = user_id

    @property
    def org_id(self):
        """Gets the org_id of this UserMetadataSpec.  # noqa: E501

        The unique id of the Organisation to which this record applies.   # noqa: E501

        :return: The org_id of this UserMetadataSpec.  # noqa: E501
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this UserMetadataSpec.

        The unique id of the Organisation to which this record applies.   # noqa: E501

        :param org_id: The org_id of this UserMetadataSpec.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                org_id is not None and len(org_id) > 40):
            raise ValueError("Invalid value for `org_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                org_id is not None and len(org_id) < 1):
            raise ValueError("Invalid value for `org_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._org_id = org_id

    @property
    def app_id(self):
        """Gets the app_id of this UserMetadataSpec.  # noqa: E501

        The unique id of the application to which this record applies.   # noqa: E501

        :return: The app_id of this UserMetadataSpec.  # noqa: E501
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UserMetadataSpec.

        The unique id of the application to which this record applies.   # noqa: E501

        :param app_id: The app_id of this UserMetadataSpec.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                app_id is not None and len(app_id) > 40):
            raise ValueError("Invalid value for `app_id`, length must be less than or equal to `40`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                app_id is not None and len(app_id) < 1):
            raise ValueError("Invalid value for `app_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._app_id = app_id

    @property
    def name(self):
        """Gets the name of this UserMetadataSpec.  # noqa: E501

        A descriptive name for this metadata entry  # noqa: E501

        :return: The name of this UserMetadataSpec.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserMetadataSpec.

        A descriptive name for this metadata entry  # noqa: E501

        :param name: The name of this UserMetadataSpec.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501

        self._name = name

    @property
    def data_type(self):
        """Gets the data_type of this UserMetadataSpec.  # noqa: E501

        The type of data present in the configuration. This informs consumers of how to use the data present. The 'json' type means no internal interpretation is done, it is a string-in/string-out. On query this can be deep-merged with member groups.   # noqa: E501

        :return: The data_type of this UserMetadataSpec.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this UserMetadataSpec.

        The type of data present in the configuration. This informs consumers of how to use the data present. The 'json' type means no internal interpretation is done, it is a string-in/string-out. On query this can be deep-merged with member groups.   # noqa: E501

        :param data_type: The data_type of this UserMetadataSpec.  # noqa: E501
        :type: str
        """
        allowed_values = ["mfa_enrollment_expiry", "user_app_data", "user_org_data", "json"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(data_type, allowed_values)
            )

        self._data_type = data_type

    @property
    def data(self):
        """Gets the data of this UserMetadataSpec.  # noqa: E501

        The string representation of the data. This value is interpretted differently based on the data_type  # noqa: E501

        :return: The data of this UserMetadataSpec.  # noqa: E501
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UserMetadataSpec.

        The string representation of the data. This value is interpretted differently based on the data_type  # noqa: E501

        :param data: The data of this UserMetadataSpec.  # noqa: E501
        :type: str
        """

        self._data = data

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
        if not isinstance(other, UserMetadataSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserMetadataSpec):
            return True

        return self.to_dict() != other.to_dict()
