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


class OIDCUpstreamIdentityProvider(object):
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
        'icon': 'str',
        'issuer': 'str',
        'client_id': 'str',
        'client_secret': 'str',
        'issuer_external_host': 'str',
        'username_key': 'str',
        'email_key': 'str',
        'email_verification_required': 'bool',
        'request_user_info': 'bool',
        'user_id_key': 'str',
        'auto_create_status': 'AutoCreateStatus'
    }

    attribute_map = {
        'name': 'name',
        'icon': 'icon',
        'issuer': 'issuer',
        'client_id': 'client_id',
        'client_secret': 'client_secret',
        'issuer_external_host': 'issuer_external_host',
        'username_key': 'username_key',
        'email_key': 'email_key',
        'email_verification_required': 'email_verification_required',
        'request_user_info': 'request_user_info',
        'user_id_key': 'user_id_key',
        'auto_create_status': 'auto_create_status'
    }

    def __init__(self, name=None, icon=None, issuer=None, client_id=None, client_secret=None, issuer_external_host=None, username_key=None, email_key=None, email_verification_required=True, request_user_info=None, user_id_key=None, auto_create_status=None, local_vars_configuration=None):  # noqa: E501
        """OIDCUpstreamIdentityProvider - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._icon = None
        self._issuer = None
        self._client_id = None
        self._client_secret = None
        self._issuer_external_host = None
        self._username_key = None
        self._email_key = None
        self._email_verification_required = None
        self._request_user_info = None
        self._user_id_key = None
        self._auto_create_status = None
        self.discriminator = None

        self.name = name
        if icon is not None:
            self.icon = icon
        self.issuer = issuer
        self.client_id = client_id
        if client_secret is not None:
            self.client_secret = client_secret
        if issuer_external_host is not None:
            self.issuer_external_host = issuer_external_host
        if username_key is not None:
            self.username_key = username_key
        if email_key is not None:
            self.email_key = email_key
        if email_verification_required is not None:
            self.email_verification_required = email_verification_required
        if request_user_info is not None:
            self.request_user_info = request_user_info
        if user_id_key is not None:
            self.user_id_key = user_id_key
        if auto_create_status is not None:
            self.auto_create_status = auto_create_status

    @property
    def name(self):
        """Gets the name of this OIDCUpstreamIdentityProvider.  # noqa: E501

        A name used to uniquely refer to the upstream identity provider configuration. This is the text that will be displayed when presenting the upstream identity for login.  # noqa: E501

        :return: The name of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OIDCUpstreamIdentityProvider.

        A name used to uniquely refer to the upstream identity provider configuration. This is the text that will be displayed when presenting the upstream identity for login.  # noqa: E501

        :param name: The name of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 100):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def icon(self):
        """Gets the icon of this OIDCUpstreamIdentityProvider.  # noqa: E501

        The icon file to be used, limited to: numbers, letters, underscores, hyphens and periods. It is part of a css class (with the periods replaced by underscores).  To use a custom icon than the provided default you will need to add the icon the static/img folder and update the static css file to add a new css button like below ```json .dex-btn-icon--<your-logo_svg> {   background-image: url(../static/img/<your-logo.svg>); } ```  To use a default icon simply enter an icon name from the pre-provided defaults found in the static/img folder The default icons are   - bitbucket   - coreos   - email   - github   - gitlab   - google   - ldap   - linkedin   - microsoft   - oidc   - saml   # noqa: E501

        :return: The icon of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this OIDCUpstreamIdentityProvider.

        The icon file to be used, limited to: numbers, letters, underscores, hyphens and periods. It is part of a css class (with the periods replaced by underscores).  To use a custom icon than the provided default you will need to add the icon the static/img folder and update the static css file to add a new css button like below ```json .dex-btn-icon--<your-logo_svg> {   background-image: url(../static/img/<your-logo.svg>); } ```  To use a default icon simply enter an icon name from the pre-provided defaults found in the static/img folder The default icons are   - bitbucket   - coreos   - email   - github   - gitlab   - google   - ldap   - linkedin   - microsoft   - oidc   - saml   # noqa: E501

        :param icon: The icon of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                icon is not None and len(icon) > 50):
            raise ValueError("Invalid value for `icon`, length must be less than or equal to `50`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                icon is not None and not re.search(r'^$|^[0-9a-zA-Z-_.]+$', icon)):  # noqa: E501
            raise ValueError(r"Invalid value for `icon`, must be a follow pattern or equal to `/^$|^[0-9a-zA-Z-_.]+$/`")  # noqa: E501

        self._icon = icon

    @property
    def issuer(self):
        """Gets the issuer of this OIDCUpstreamIdentityProvider.  # noqa: E501

        The upstream issuer uri. This is the URI which identifies the issuer against which users selecting this OIDCUpstreamIdentityProvider will authenticate. The issuer must support the OpenID Connect discovery document described here: https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig.  # noqa: E501

        :return: The issuer of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this OIDCUpstreamIdentityProvider.

        The upstream issuer uri. This is the URI which identifies the issuer against which users selecting this OIDCUpstreamIdentityProvider will authenticate. The issuer must support the OpenID Connect discovery document described here: https://openid.net/specs/openid-connect-discovery-1_0.html#ProviderConfig.  # noqa: E501

        :param issuer: The issuer of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and issuer is None:  # noqa: E501
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                issuer is not None and len(issuer) > 511):
            raise ValueError("Invalid value for `issuer`, length must be less than or equal to `511`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                issuer is not None and len(issuer) < 1):
            raise ValueError("Invalid value for `issuer`, length must be greater than or equal to `1`")  # noqa: E501

        self._issuer = issuer

    @property
    def client_id(self):
        """Gets the client_id of this OIDCUpstreamIdentityProvider.  # noqa: E501

        The client ID for the upstream identity provider  # noqa: E501

        :return: The client_id of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OIDCUpstreamIdentityProvider.

        The client ID for the upstream identity provider  # noqa: E501

        :param client_id: The client_id of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and client_id is None:  # noqa: E501
            raise ValueError("Invalid value for `client_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                client_id is not None and len(client_id) > 100):
            raise ValueError("Invalid value for `client_id`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                client_id is not None and len(client_id) < 1):
            raise ValueError("Invalid value for `client_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._client_id = client_id

    @property
    def client_secret(self):
        """Gets the client_secret of this OIDCUpstreamIdentityProvider.  # noqa: E501

        The secret presented to the upstream during any workflows which require authentication  # noqa: E501

        :return: The client_secret of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """Sets the client_secret of this OIDCUpstreamIdentityProvider.

        The secret presented to the upstream during any workflows which require authentication  # noqa: E501

        :param client_secret: The client_secret of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                client_secret is not None and len(client_secret) > 255):
            raise ValueError("Invalid value for `client_secret`, length must be less than or equal to `255`")  # noqa: E501

        self._client_secret = client_secret

    @property
    def issuer_external_host(self):
        """Gets the issuer_external_host of this OIDCUpstreamIdentityProvider.  # noqa: E501

        A proxy standing in for the main issuer host. Use this if fronting the upstream through the Agilicus infrastructure  # noqa: E501

        :return: The issuer_external_host of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._issuer_external_host

    @issuer_external_host.setter
    def issuer_external_host(self, issuer_external_host):
        """Sets the issuer_external_host of this OIDCUpstreamIdentityProvider.

        A proxy standing in for the main issuer host. Use this if fronting the upstream through the Agilicus infrastructure  # noqa: E501

        :param issuer_external_host: The issuer_external_host of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                issuer_external_host is not None and len(issuer_external_host) > 255):
            raise ValueError("Invalid value for `issuer_external_host`, length must be less than or equal to `255`")  # noqa: E501

        self._issuer_external_host = issuer_external_host

    @property
    def username_key(self):
        """Gets the username_key of this OIDCUpstreamIdentityProvider.  # noqa: E501

        Allows changing the key in the OIDC response claims used to determine the full name of the user. If not present, defaults to the standard name  # noqa: E501

        :return: The username_key of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._username_key

    @username_key.setter
    def username_key(self, username_key):
        """Sets the username_key of this OIDCUpstreamIdentityProvider.

        Allows changing the key in the OIDC response claims used to determine the full name of the user. If not present, defaults to the standard name  # noqa: E501

        :param username_key: The username_key of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                username_key is not None and len(username_key) > 255):
            raise ValueError("Invalid value for `username_key`, length must be less than or equal to `255`")  # noqa: E501

        self._username_key = username_key

    @property
    def email_key(self):
        """Gets the email_key of this OIDCUpstreamIdentityProvider.  # noqa: E501

        Allows changing the key in the OIDC response claims used to determine the email address of the user. If not present, defaults to the standard email  # noqa: E501

        :return: The email_key of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._email_key

    @email_key.setter
    def email_key(self, email_key):
        """Sets the email_key of this OIDCUpstreamIdentityProvider.

        Allows changing the key in the OIDC response claims used to determine the email address of the user. If not present, defaults to the standard email  # noqa: E501

        :param email_key: The email_key of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                email_key is not None and len(email_key) > 255):
            raise ValueError("Invalid value for `email_key`, length must be less than or equal to `255`")  # noqa: E501

        self._email_key = email_key

    @property
    def email_verification_required(self):
        """Gets the email_verification_required of this OIDCUpstreamIdentityProvider.  # noqa: E501

        Controls whether email verification is required for this OIDC provider. Some OIDC providers do not take steps to verify the email address of users, or may not do so in all cases. Setting this value to true will reject any successful upstream logins for users which have not had their email address verified.  # noqa: E501

        :return: The email_verification_required of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: bool
        """
        return self._email_verification_required

    @email_verification_required.setter
    def email_verification_required(self, email_verification_required):
        """Sets the email_verification_required of this OIDCUpstreamIdentityProvider.

        Controls whether email verification is required for this OIDC provider. Some OIDC providers do not take steps to verify the email address of users, or may not do so in all cases. Setting this value to true will reject any successful upstream logins for users which have not had their email address verified.  # noqa: E501

        :param email_verification_required: The email_verification_required of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: bool
        """

        self._email_verification_required = email_verification_required

    @property
    def request_user_info(self):
        """Gets the request_user_info of this OIDCUpstreamIdentityProvider.  # noqa: E501

        Controls whether the system will retrieve extra information about the user from the provider's user_info endpoint. This can be useful if the initial OIDC response does not contain sufficient information to determine the email address or user's name. Setting this value to true will cause extra requests to be generated to the upstream every time a user logs in to it.  # noqa: E501

        :return: The request_user_info of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: bool
        """
        return self._request_user_info

    @request_user_info.setter
    def request_user_info(self, request_user_info):
        """Sets the request_user_info of this OIDCUpstreamIdentityProvider.

        Controls whether the system will retrieve extra information about the user from the provider's user_info endpoint. This can be useful if the initial OIDC response does not contain sufficient information to determine the email address or user's name. Setting this value to true will cause extra requests to be generated to the upstream every time a user logs in to it.  # noqa: E501

        :param request_user_info: The request_user_info of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: bool
        """

        self._request_user_info = request_user_info

    @property
    def user_id_key(self):
        """Gets the user_id_key of this OIDCUpstreamIdentityProvider.  # noqa: E501

        Changes the key used to determine the id of the user in this upstream. The key will be used to retrieve the user id from the id token claims returned from the upstream when the user logs in. This user id is in turn used to link the user to its identity within the system. If not present, the system will fall back on the default, which is `sub`.   # noqa: E501

        :return: The user_id_key of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: str
        """
        return self._user_id_key

    @user_id_key.setter
    def user_id_key(self, user_id_key):
        """Sets the user_id_key of this OIDCUpstreamIdentityProvider.

        Changes the key used to determine the id of the user in this upstream. The key will be used to retrieve the user id from the id token claims returned from the upstream when the user logs in. This user id is in turn used to link the user to its identity within the system. If not present, the system will fall back on the default, which is `sub`.   # noqa: E501

        :param user_id_key: The user_id_key of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                user_id_key is not None and len(user_id_key) > 255):
            raise ValueError("Invalid value for `user_id_key`, length must be less than or equal to `255`")  # noqa: E501

        self._user_id_key = user_id_key

    @property
    def auto_create_status(self):
        """Gets the auto_create_status of this OIDCUpstreamIdentityProvider.  # noqa: E501


        :return: The auto_create_status of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :rtype: AutoCreateStatus
        """
        return self._auto_create_status

    @auto_create_status.setter
    def auto_create_status(self, auto_create_status):
        """Sets the auto_create_status of this OIDCUpstreamIdentityProvider.


        :param auto_create_status: The auto_create_status of this OIDCUpstreamIdentityProvider.  # noqa: E501
        :type: AutoCreateStatus
        """

        self._auto_create_status = auto_create_status

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
        if not isinstance(other, OIDCUpstreamIdentityProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OIDCUpstreamIdentityProvider):
            return True

        return self.to_dict() != other.to_dict()
