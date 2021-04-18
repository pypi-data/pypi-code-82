# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserAttributeMapperArgs', 'UserAttributeMapper']

@pulumi.input_type
class UserAttributeMapperArgs:
    def __init__(__self__, *,
                 ldap_attribute: pulumi.Input[str],
                 ldap_user_federation_id: pulumi.Input[str],
                 realm_id: pulumi.Input[str],
                 user_model_attribute: pulumi.Input[str],
                 always_read_value_from_ldap: Optional[pulumi.Input[bool]] = None,
                 is_mandatory_in_ldap: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a UserAttributeMapper resource.
        :param pulumi.Input[str] ldap_attribute: Name of the mapped attribute on the LDAP object.
        :param pulumi.Input[str] ldap_user_federation_id: The ID of the LDAP user federation provider to attach this mapper to.
        :param pulumi.Input[str] realm_id: The realm that this LDAP mapper will exist in.
        :param pulumi.Input[str] user_model_attribute: Name of the user property or attribute you want to map the LDAP attribute into.
        :param pulumi.Input[bool] always_read_value_from_ldap: When `true`, the value fetched from LDAP will override the value stored in Keycloak. Defaults to `false`.
        :param pulumi.Input[bool] is_mandatory_in_ldap: When `true`, this attribute must exist in LDAP. Defaults to `false`.
        :param pulumi.Input[str] name: Display name of this mapper when displayed in the console.
        :param pulumi.Input[bool] read_only: When `true`, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Defaults to `false`.
        """
        pulumi.set(__self__, "ldap_attribute", ldap_attribute)
        pulumi.set(__self__, "ldap_user_federation_id", ldap_user_federation_id)
        pulumi.set(__self__, "realm_id", realm_id)
        pulumi.set(__self__, "user_model_attribute", user_model_attribute)
        if always_read_value_from_ldap is not None:
            pulumi.set(__self__, "always_read_value_from_ldap", always_read_value_from_ldap)
        if is_mandatory_in_ldap is not None:
            pulumi.set(__self__, "is_mandatory_in_ldap", is_mandatory_in_ldap)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if read_only is not None:
            pulumi.set(__self__, "read_only", read_only)

    @property
    @pulumi.getter(name="ldapAttribute")
    def ldap_attribute(self) -> pulumi.Input[str]:
        """
        Name of the mapped attribute on the LDAP object.
        """
        return pulumi.get(self, "ldap_attribute")

    @ldap_attribute.setter
    def ldap_attribute(self, value: pulumi.Input[str]):
        pulumi.set(self, "ldap_attribute", value)

    @property
    @pulumi.getter(name="ldapUserFederationId")
    def ldap_user_federation_id(self) -> pulumi.Input[str]:
        """
        The ID of the LDAP user federation provider to attach this mapper to.
        """
        return pulumi.get(self, "ldap_user_federation_id")

    @ldap_user_federation_id.setter
    def ldap_user_federation_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ldap_user_federation_id", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Input[str]:
        """
        The realm that this LDAP mapper will exist in.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter(name="userModelAttribute")
    def user_model_attribute(self) -> pulumi.Input[str]:
        """
        Name of the user property or attribute you want to map the LDAP attribute into.
        """
        return pulumi.get(self, "user_model_attribute")

    @user_model_attribute.setter
    def user_model_attribute(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_model_attribute", value)

    @property
    @pulumi.getter(name="alwaysReadValueFromLdap")
    def always_read_value_from_ldap(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, the value fetched from LDAP will override the value stored in Keycloak. Defaults to `false`.
        """
        return pulumi.get(self, "always_read_value_from_ldap")

    @always_read_value_from_ldap.setter
    def always_read_value_from_ldap(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "always_read_value_from_ldap", value)

    @property
    @pulumi.getter(name="isMandatoryInLdap")
    def is_mandatory_in_ldap(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, this attribute must exist in LDAP. Defaults to `false`.
        """
        return pulumi.get(self, "is_mandatory_in_ldap")

    @is_mandatory_in_ldap.setter
    def is_mandatory_in_ldap(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_mandatory_in_ldap", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of this mapper when displayed in the console.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Defaults to `false`.
        """
        return pulumi.get(self, "read_only")

    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "read_only", value)


@pulumi.input_type
class _UserAttributeMapperState:
    def __init__(__self__, *,
                 always_read_value_from_ldap: Optional[pulumi.Input[bool]] = None,
                 is_mandatory_in_ldap: Optional[pulumi.Input[bool]] = None,
                 ldap_attribute: Optional[pulumi.Input[str]] = None,
                 ldap_user_federation_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 user_model_attribute: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserAttributeMapper resources.
        :param pulumi.Input[bool] always_read_value_from_ldap: When `true`, the value fetched from LDAP will override the value stored in Keycloak. Defaults to `false`.
        :param pulumi.Input[bool] is_mandatory_in_ldap: When `true`, this attribute must exist in LDAP. Defaults to `false`.
        :param pulumi.Input[str] ldap_attribute: Name of the mapped attribute on the LDAP object.
        :param pulumi.Input[str] ldap_user_federation_id: The ID of the LDAP user federation provider to attach this mapper to.
        :param pulumi.Input[str] name: Display name of this mapper when displayed in the console.
        :param pulumi.Input[bool] read_only: When `true`, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Defaults to `false`.
        :param pulumi.Input[str] realm_id: The realm that this LDAP mapper will exist in.
        :param pulumi.Input[str] user_model_attribute: Name of the user property or attribute you want to map the LDAP attribute into.
        """
        if always_read_value_from_ldap is not None:
            pulumi.set(__self__, "always_read_value_from_ldap", always_read_value_from_ldap)
        if is_mandatory_in_ldap is not None:
            pulumi.set(__self__, "is_mandatory_in_ldap", is_mandatory_in_ldap)
        if ldap_attribute is not None:
            pulumi.set(__self__, "ldap_attribute", ldap_attribute)
        if ldap_user_federation_id is not None:
            pulumi.set(__self__, "ldap_user_federation_id", ldap_user_federation_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if read_only is not None:
            pulumi.set(__self__, "read_only", read_only)
        if realm_id is not None:
            pulumi.set(__self__, "realm_id", realm_id)
        if user_model_attribute is not None:
            pulumi.set(__self__, "user_model_attribute", user_model_attribute)

    @property
    @pulumi.getter(name="alwaysReadValueFromLdap")
    def always_read_value_from_ldap(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, the value fetched from LDAP will override the value stored in Keycloak. Defaults to `false`.
        """
        return pulumi.get(self, "always_read_value_from_ldap")

    @always_read_value_from_ldap.setter
    def always_read_value_from_ldap(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "always_read_value_from_ldap", value)

    @property
    @pulumi.getter(name="isMandatoryInLdap")
    def is_mandatory_in_ldap(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, this attribute must exist in LDAP. Defaults to `false`.
        """
        return pulumi.get(self, "is_mandatory_in_ldap")

    @is_mandatory_in_ldap.setter
    def is_mandatory_in_ldap(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_mandatory_in_ldap", value)

    @property
    @pulumi.getter(name="ldapAttribute")
    def ldap_attribute(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the mapped attribute on the LDAP object.
        """
        return pulumi.get(self, "ldap_attribute")

    @ldap_attribute.setter
    def ldap_attribute(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ldap_attribute", value)

    @property
    @pulumi.getter(name="ldapUserFederationId")
    def ldap_user_federation_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the LDAP user federation provider to attach this mapper to.
        """
        return pulumi.get(self, "ldap_user_federation_id")

    @ldap_user_federation_id.setter
    def ldap_user_federation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ldap_user_federation_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of this mapper when displayed in the console.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[bool]]:
        """
        When `true`, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Defaults to `false`.
        """
        return pulumi.get(self, "read_only")

    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "read_only", value)

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> Optional[pulumi.Input[str]]:
        """
        The realm that this LDAP mapper will exist in.
        """
        return pulumi.get(self, "realm_id")

    @realm_id.setter
    def realm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "realm_id", value)

    @property
    @pulumi.getter(name="userModelAttribute")
    def user_model_attribute(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the user property or attribute you want to map the LDAP attribute into.
        """
        return pulumi.get(self, "user_model_attribute")

    @user_model_attribute.setter
    def user_model_attribute(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_model_attribute", value)


class UserAttributeMapper(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 always_read_value_from_ldap: Optional[pulumi.Input[bool]] = None,
                 is_mandatory_in_ldap: Optional[pulumi.Input[bool]] = None,
                 ldap_attribute: Optional[pulumi.Input[str]] = None,
                 ldap_user_federation_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 user_model_attribute: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Allows for creating and managing user attribute mappers for Keycloak users
        federated via LDAP.

        The LDAP user attribute mapper can be used to map a single LDAP attribute
        to an attribute on the Keycloak user model.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        ldap_user_federation = keycloak.ldap.UserFederation("ldapUserFederation",
            realm_id=realm.id,
            username_ldap_attribute="cn",
            rdn_ldap_attribute="cn",
            uuid_ldap_attribute="entryDN",
            user_object_classes=[
                "simpleSecurityObject",
                "organizationalRole",
            ],
            connection_url="ldap://openldap",
            users_dn="dc=example,dc=org",
            bind_dn="cn=admin,dc=example,dc=org",
            bind_credential="admin")
        ldap_user_attribute_mapper = keycloak.ldap.UserAttributeMapper("ldapUserAttributeMapper",
            realm_id=realm.id,
            ldap_user_federation_id=ldap_user_federation.id,
            user_model_attribute="foo",
            ldap_attribute="bar")
        ```

        ## Import

        LDAP mappers can be imported using the format `{{realm_id}}/{{ldap_user_federation_id}}/{{ldap_mapper_id}}`. The ID of the LDAP user federation provider and the mapper can be found within the Keycloak GUI, and they are typically GUIDs. Examplebash

        ```sh
         $ pulumi import keycloak:ldap/userAttributeMapper:UserAttributeMapper ldap_user_attribute_mapper my-realm/af2a6ca3-e4d7-49c3-b08b-1b3c70b4b860/3d923ece-1a91-4bf7-adaf-3b82f2a12b67
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] always_read_value_from_ldap: When `true`, the value fetched from LDAP will override the value stored in Keycloak. Defaults to `false`.
        :param pulumi.Input[bool] is_mandatory_in_ldap: When `true`, this attribute must exist in LDAP. Defaults to `false`.
        :param pulumi.Input[str] ldap_attribute: Name of the mapped attribute on the LDAP object.
        :param pulumi.Input[str] ldap_user_federation_id: The ID of the LDAP user federation provider to attach this mapper to.
        :param pulumi.Input[str] name: Display name of this mapper when displayed in the console.
        :param pulumi.Input[bool] read_only: When `true`, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Defaults to `false`.
        :param pulumi.Input[str] realm_id: The realm that this LDAP mapper will exist in.
        :param pulumi.Input[str] user_model_attribute: Name of the user property or attribute you want to map the LDAP attribute into.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserAttributeMapperArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Allows for creating and managing user attribute mappers for Keycloak users
        federated via LDAP.

        The LDAP user attribute mapper can be used to map a single LDAP attribute
        to an attribute on the Keycloak user model.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_keycloak as keycloak

        realm = keycloak.Realm("realm",
            realm="my-realm",
            enabled=True)
        ldap_user_federation = keycloak.ldap.UserFederation("ldapUserFederation",
            realm_id=realm.id,
            username_ldap_attribute="cn",
            rdn_ldap_attribute="cn",
            uuid_ldap_attribute="entryDN",
            user_object_classes=[
                "simpleSecurityObject",
                "organizationalRole",
            ],
            connection_url="ldap://openldap",
            users_dn="dc=example,dc=org",
            bind_dn="cn=admin,dc=example,dc=org",
            bind_credential="admin")
        ldap_user_attribute_mapper = keycloak.ldap.UserAttributeMapper("ldapUserAttributeMapper",
            realm_id=realm.id,
            ldap_user_federation_id=ldap_user_federation.id,
            user_model_attribute="foo",
            ldap_attribute="bar")
        ```

        ## Import

        LDAP mappers can be imported using the format `{{realm_id}}/{{ldap_user_federation_id}}/{{ldap_mapper_id}}`. The ID of the LDAP user federation provider and the mapper can be found within the Keycloak GUI, and they are typically GUIDs. Examplebash

        ```sh
         $ pulumi import keycloak:ldap/userAttributeMapper:UserAttributeMapper ldap_user_attribute_mapper my-realm/af2a6ca3-e4d7-49c3-b08b-1b3c70b4b860/3d923ece-1a91-4bf7-adaf-3b82f2a12b67
        ```

        :param str resource_name: The name of the resource.
        :param UserAttributeMapperArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserAttributeMapperArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 always_read_value_from_ldap: Optional[pulumi.Input[bool]] = None,
                 is_mandatory_in_ldap: Optional[pulumi.Input[bool]] = None,
                 ldap_attribute: Optional[pulumi.Input[str]] = None,
                 ldap_user_federation_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 read_only: Optional[pulumi.Input[bool]] = None,
                 realm_id: Optional[pulumi.Input[str]] = None,
                 user_model_attribute: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserAttributeMapperArgs.__new__(UserAttributeMapperArgs)

            __props__.__dict__["always_read_value_from_ldap"] = always_read_value_from_ldap
            __props__.__dict__["is_mandatory_in_ldap"] = is_mandatory_in_ldap
            if ldap_attribute is None and not opts.urn:
                raise TypeError("Missing required property 'ldap_attribute'")
            __props__.__dict__["ldap_attribute"] = ldap_attribute
            if ldap_user_federation_id is None and not opts.urn:
                raise TypeError("Missing required property 'ldap_user_federation_id'")
            __props__.__dict__["ldap_user_federation_id"] = ldap_user_federation_id
            __props__.__dict__["name"] = name
            __props__.__dict__["read_only"] = read_only
            if realm_id is None and not opts.urn:
                raise TypeError("Missing required property 'realm_id'")
            __props__.__dict__["realm_id"] = realm_id
            if user_model_attribute is None and not opts.urn:
                raise TypeError("Missing required property 'user_model_attribute'")
            __props__.__dict__["user_model_attribute"] = user_model_attribute
        super(UserAttributeMapper, __self__).__init__(
            'keycloak:ldap/userAttributeMapper:UserAttributeMapper',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            always_read_value_from_ldap: Optional[pulumi.Input[bool]] = None,
            is_mandatory_in_ldap: Optional[pulumi.Input[bool]] = None,
            ldap_attribute: Optional[pulumi.Input[str]] = None,
            ldap_user_federation_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            read_only: Optional[pulumi.Input[bool]] = None,
            realm_id: Optional[pulumi.Input[str]] = None,
            user_model_attribute: Optional[pulumi.Input[str]] = None) -> 'UserAttributeMapper':
        """
        Get an existing UserAttributeMapper resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] always_read_value_from_ldap: When `true`, the value fetched from LDAP will override the value stored in Keycloak. Defaults to `false`.
        :param pulumi.Input[bool] is_mandatory_in_ldap: When `true`, this attribute must exist in LDAP. Defaults to `false`.
        :param pulumi.Input[str] ldap_attribute: Name of the mapped attribute on the LDAP object.
        :param pulumi.Input[str] ldap_user_federation_id: The ID of the LDAP user federation provider to attach this mapper to.
        :param pulumi.Input[str] name: Display name of this mapper when displayed in the console.
        :param pulumi.Input[bool] read_only: When `true`, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Defaults to `false`.
        :param pulumi.Input[str] realm_id: The realm that this LDAP mapper will exist in.
        :param pulumi.Input[str] user_model_attribute: Name of the user property or attribute you want to map the LDAP attribute into.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserAttributeMapperState.__new__(_UserAttributeMapperState)

        __props__.__dict__["always_read_value_from_ldap"] = always_read_value_from_ldap
        __props__.__dict__["is_mandatory_in_ldap"] = is_mandatory_in_ldap
        __props__.__dict__["ldap_attribute"] = ldap_attribute
        __props__.__dict__["ldap_user_federation_id"] = ldap_user_federation_id
        __props__.__dict__["name"] = name
        __props__.__dict__["read_only"] = read_only
        __props__.__dict__["realm_id"] = realm_id
        __props__.__dict__["user_model_attribute"] = user_model_attribute
        return UserAttributeMapper(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="alwaysReadValueFromLdap")
    def always_read_value_from_ldap(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, the value fetched from LDAP will override the value stored in Keycloak. Defaults to `false`.
        """
        return pulumi.get(self, "always_read_value_from_ldap")

    @property
    @pulumi.getter(name="isMandatoryInLdap")
    def is_mandatory_in_ldap(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, this attribute must exist in LDAP. Defaults to `false`.
        """
        return pulumi.get(self, "is_mandatory_in_ldap")

    @property
    @pulumi.getter(name="ldapAttribute")
    def ldap_attribute(self) -> pulumi.Output[str]:
        """
        Name of the mapped attribute on the LDAP object.
        """
        return pulumi.get(self, "ldap_attribute")

    @property
    @pulumi.getter(name="ldapUserFederationId")
    def ldap_user_federation_id(self) -> pulumi.Output[str]:
        """
        The ID of the LDAP user federation provider to attach this mapper to.
        """
        return pulumi.get(self, "ldap_user_federation_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Display name of this mapper when displayed in the console.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> pulumi.Output[Optional[bool]]:
        """
        When `true`, this attribute is not saved back to LDAP when the user attribute is updated in Keycloak. Defaults to `false`.
        """
        return pulumi.get(self, "read_only")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> pulumi.Output[str]:
        """
        The realm that this LDAP mapper will exist in.
        """
        return pulumi.get(self, "realm_id")

    @property
    @pulumi.getter(name="userModelAttribute")
    def user_model_attribute(self) -> pulumi.Output[str]:
        """
        Name of the user property or attribute you want to map the LDAP attribute into.
        """
        return pulumi.get(self, "user_model_attribute")

