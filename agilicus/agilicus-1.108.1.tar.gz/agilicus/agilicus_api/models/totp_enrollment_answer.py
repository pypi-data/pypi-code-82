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


class TOTPEnrollmentAnswer(object):
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
        'answer': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'answer': 'answer'
    }

    def __init__(self, user_id=None, answer=None, local_vars_configuration=None):  # noqa: E501
        """TOTPEnrollmentAnswer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._answer = None
        self.discriminator = None

        self.user_id = user_id
        self.answer = answer

    @property
    def user_id(self):
        """Gets the user_id of this TOTPEnrollmentAnswer.  # noqa: E501

        Unique identifier  # noqa: E501

        :return: The user_id of this TOTPEnrollmentAnswer.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TOTPEnrollmentAnswer.

        Unique identifier  # noqa: E501

        :param user_id: The user_id of this TOTPEnrollmentAnswer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and user_id is None:  # noqa: E501
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def answer(self):
        """Gets the answer of this TOTPEnrollmentAnswer.  # noqa: E501

        An opaque string used to answer the challenge.  # noqa: E501

        :return: The answer of this TOTPEnrollmentAnswer.  # noqa: E501
        :rtype: str
        """
        return self._answer

    @answer.setter
    def answer(self, answer):
        """Sets the answer of this TOTPEnrollmentAnswer.

        An opaque string used to answer the challenge.  # noqa: E501

        :param answer: The answer of this TOTPEnrollmentAnswer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and answer is None:  # noqa: E501
            raise ValueError("Invalid value for `answer`, must not be `None`")  # noqa: E501

        self._answer = answer

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
        if not isinstance(other, TOTPEnrollmentAnswer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TOTPEnrollmentAnswer):
            return True

        return self.to_dict() != other.to_dict()
