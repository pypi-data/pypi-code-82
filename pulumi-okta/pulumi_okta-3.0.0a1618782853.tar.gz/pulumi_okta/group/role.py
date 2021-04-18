# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RoleArgs', 'Role']

@pulumi.input_type
class RoleArgs:
    def __init__(__self__, *,
                 group_id: pulumi.Input[str],
                 role_type: pulumi.Input[str],
                 target_app_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 target_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Role resource.
        :param pulumi.Input[str] group_id: The ID of group to attach admin roles to.
        :param pulumi.Input[str] role_type: Admin role assigned to the group. It can be any one of the following values `"SUPER_ADMIN"`
               , `"ORG_ADMIN"`, `"APP_ADMIN"`, `"USER_ADMIN"`, `"HELP_DESK_ADMIN"`, `"READ_ONLY_ADMIN"`
               , `"MOBILE_ADMIN"`, `"API_ACCESS_MANAGEMENT_ADMIN"`, `"REPORT_ADMIN"`, `"GROUP_MEMBERSHIP_ADMIN"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_app_lists: A list of app names (name represents set of app instances, like 'salesforce' or '
               facebook'), or a combination of app name and app instance ID (like 'facebook.0oapsqQ6dv19pqyEo0g3') you would like as
               the targets of the admin role.
               - Only supported when used with the role type `"APP_ADMIN"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_group_lists: A list of group IDs you would like as the targets of the admin role.
               - Only supported when used with the role types: `GROUP_MEMBERSHIP_ADMIN`, `HELP_DESK_ADMIN`, or `USER_ADMIN`.
        """
        pulumi.set(__self__, "group_id", group_id)
        pulumi.set(__self__, "role_type", role_type)
        if target_app_lists is not None:
            pulumi.set(__self__, "target_app_lists", target_app_lists)
        if target_group_lists is not None:
            pulumi.set(__self__, "target_group_lists", target_group_lists)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The ID of group to attach admin roles to.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> pulumi.Input[str]:
        """
        Admin role assigned to the group. It can be any one of the following values `"SUPER_ADMIN"`
        , `"ORG_ADMIN"`, `"APP_ADMIN"`, `"USER_ADMIN"`, `"HELP_DESK_ADMIN"`, `"READ_ONLY_ADMIN"`
        , `"MOBILE_ADMIN"`, `"API_ACCESS_MANAGEMENT_ADMIN"`, `"REPORT_ADMIN"`, `"GROUP_MEMBERSHIP_ADMIN"`.
        """
        return pulumi.get(self, "role_type")

    @role_type.setter
    def role_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_type", value)

    @property
    @pulumi.getter(name="targetAppLists")
    def target_app_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of app names (name represents set of app instances, like 'salesforce' or '
        facebook'), or a combination of app name and app instance ID (like 'facebook.0oapsqQ6dv19pqyEo0g3') you would like as
        the targets of the admin role.
        - Only supported when used with the role type `"APP_ADMIN"`.
        """
        return pulumi.get(self, "target_app_lists")

    @target_app_lists.setter
    def target_app_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "target_app_lists", value)

    @property
    @pulumi.getter(name="targetGroupLists")
    def target_group_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of group IDs you would like as the targets of the admin role.
        - Only supported when used with the role types: `GROUP_MEMBERSHIP_ADMIN`, `HELP_DESK_ADMIN`, or `USER_ADMIN`.
        """
        return pulumi.get(self, "target_group_lists")

    @target_group_lists.setter
    def target_group_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "target_group_lists", value)


@pulumi.input_type
class _RoleState:
    def __init__(__self__, *,
                 group_id: Optional[pulumi.Input[str]] = None,
                 role_type: Optional[pulumi.Input[str]] = None,
                 target_app_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 target_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Role resources.
        :param pulumi.Input[str] group_id: The ID of group to attach admin roles to.
        :param pulumi.Input[str] role_type: Admin role assigned to the group. It can be any one of the following values `"SUPER_ADMIN"`
               , `"ORG_ADMIN"`, `"APP_ADMIN"`, `"USER_ADMIN"`, `"HELP_DESK_ADMIN"`, `"READ_ONLY_ADMIN"`
               , `"MOBILE_ADMIN"`, `"API_ACCESS_MANAGEMENT_ADMIN"`, `"REPORT_ADMIN"`, `"GROUP_MEMBERSHIP_ADMIN"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_app_lists: A list of app names (name represents set of app instances, like 'salesforce' or '
               facebook'), or a combination of app name and app instance ID (like 'facebook.0oapsqQ6dv19pqyEo0g3') you would like as
               the targets of the admin role.
               - Only supported when used with the role type `"APP_ADMIN"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_group_lists: A list of group IDs you would like as the targets of the admin role.
               - Only supported when used with the role types: `GROUP_MEMBERSHIP_ADMIN`, `HELP_DESK_ADMIN`, or `USER_ADMIN`.
        """
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if role_type is not None:
            pulumi.set(__self__, "role_type", role_type)
        if target_app_lists is not None:
            pulumi.set(__self__, "target_app_lists", target_app_lists)
        if target_group_lists is not None:
            pulumi.set(__self__, "target_group_lists", target_group_lists)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of group to attach admin roles to.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> Optional[pulumi.Input[str]]:
        """
        Admin role assigned to the group. It can be any one of the following values `"SUPER_ADMIN"`
        , `"ORG_ADMIN"`, `"APP_ADMIN"`, `"USER_ADMIN"`, `"HELP_DESK_ADMIN"`, `"READ_ONLY_ADMIN"`
        , `"MOBILE_ADMIN"`, `"API_ACCESS_MANAGEMENT_ADMIN"`, `"REPORT_ADMIN"`, `"GROUP_MEMBERSHIP_ADMIN"`.
        """
        return pulumi.get(self, "role_type")

    @role_type.setter
    def role_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "role_type", value)

    @property
    @pulumi.getter(name="targetAppLists")
    def target_app_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of app names (name represents set of app instances, like 'salesforce' or '
        facebook'), or a combination of app name and app instance ID (like 'facebook.0oapsqQ6dv19pqyEo0g3') you would like as
        the targets of the admin role.
        - Only supported when used with the role type `"APP_ADMIN"`.
        """
        return pulumi.get(self, "target_app_lists")

    @target_app_lists.setter
    def target_app_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "target_app_lists", value)

    @property
    @pulumi.getter(name="targetGroupLists")
    def target_group_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of group IDs you would like as the targets of the admin role.
        - Only supported when used with the role types: `GROUP_MEMBERSHIP_ADMIN`, `HELP_DESK_ADMIN`, or `USER_ADMIN`.
        """
        return pulumi.get(self, "target_group_lists")

    @target_group_lists.setter
    def target_group_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "target_group_lists", value)


class Role(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 role_type: Optional[pulumi.Input[str]] = None,
                 target_app_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 target_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Assigns Admin roles to Okta Groups.

        This resource allows you to assign Okta administrator roles to Okta Groups. This resource provides a one-to-one
        interface between the Okta group and the admin role.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.group.Role("example",
            group_id="<group id>",
            role_type="READ_ONLY_ADMIN")
        ```

        ## Import

        Individual admin role assignment can be imported by passing the group and role assignment IDs as follows

        ```sh
         $ pulumi import okta:group/role:Role example <group id>/<role id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The ID of group to attach admin roles to.
        :param pulumi.Input[str] role_type: Admin role assigned to the group. It can be any one of the following values `"SUPER_ADMIN"`
               , `"ORG_ADMIN"`, `"APP_ADMIN"`, `"USER_ADMIN"`, `"HELP_DESK_ADMIN"`, `"READ_ONLY_ADMIN"`
               , `"MOBILE_ADMIN"`, `"API_ACCESS_MANAGEMENT_ADMIN"`, `"REPORT_ADMIN"`, `"GROUP_MEMBERSHIP_ADMIN"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_app_lists: A list of app names (name represents set of app instances, like 'salesforce' or '
               facebook'), or a combination of app name and app instance ID (like 'facebook.0oapsqQ6dv19pqyEo0g3') you would like as
               the targets of the admin role.
               - Only supported when used with the role type `"APP_ADMIN"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_group_lists: A list of group IDs you would like as the targets of the admin role.
               - Only supported when used with the role types: `GROUP_MEMBERSHIP_ADMIN`, `HELP_DESK_ADMIN`, or `USER_ADMIN`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Assigns Admin roles to Okta Groups.

        This resource allows you to assign Okta administrator roles to Okta Groups. This resource provides a one-to-one
        interface between the Okta group and the admin role.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.group.Role("example",
            group_id="<group id>",
            role_type="READ_ONLY_ADMIN")
        ```

        ## Import

        Individual admin role assignment can be imported by passing the group and role assignment IDs as follows

        ```sh
         $ pulumi import okta:group/role:Role example <group id>/<role id>
        ```

        :param str resource_name: The name of the resource.
        :param RoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 role_type: Optional[pulumi.Input[str]] = None,
                 target_app_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 target_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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
            __props__ = RoleArgs.__new__(RoleArgs)

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            if role_type is None and not opts.urn:
                raise TypeError("Missing required property 'role_type'")
            __props__.__dict__["role_type"] = role_type
            __props__.__dict__["target_app_lists"] = target_app_lists
            __props__.__dict__["target_group_lists"] = target_group_lists
        super(Role, __self__).__init__(
            'okta:group/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            role_type: Optional[pulumi.Input[str]] = None,
            target_app_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            target_group_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The ID of group to attach admin roles to.
        :param pulumi.Input[str] role_type: Admin role assigned to the group. It can be any one of the following values `"SUPER_ADMIN"`
               , `"ORG_ADMIN"`, `"APP_ADMIN"`, `"USER_ADMIN"`, `"HELP_DESK_ADMIN"`, `"READ_ONLY_ADMIN"`
               , `"MOBILE_ADMIN"`, `"API_ACCESS_MANAGEMENT_ADMIN"`, `"REPORT_ADMIN"`, `"GROUP_MEMBERSHIP_ADMIN"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_app_lists: A list of app names (name represents set of app instances, like 'salesforce' or '
               facebook'), or a combination of app name and app instance ID (like 'facebook.0oapsqQ6dv19pqyEo0g3') you would like as
               the targets of the admin role.
               - Only supported when used with the role type `"APP_ADMIN"`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_group_lists: A list of group IDs you would like as the targets of the admin role.
               - Only supported when used with the role types: `GROUP_MEMBERSHIP_ADMIN`, `HELP_DESK_ADMIN`, or `USER_ADMIN`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoleState.__new__(_RoleState)

        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["role_type"] = role_type
        __props__.__dict__["target_app_lists"] = target_app_lists
        __props__.__dict__["target_group_lists"] = target_group_lists
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The ID of group to attach admin roles to.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="roleType")
    def role_type(self) -> pulumi.Output[str]:
        """
        Admin role assigned to the group. It can be any one of the following values `"SUPER_ADMIN"`
        , `"ORG_ADMIN"`, `"APP_ADMIN"`, `"USER_ADMIN"`, `"HELP_DESK_ADMIN"`, `"READ_ONLY_ADMIN"`
        , `"MOBILE_ADMIN"`, `"API_ACCESS_MANAGEMENT_ADMIN"`, `"REPORT_ADMIN"`, `"GROUP_MEMBERSHIP_ADMIN"`.
        """
        return pulumi.get(self, "role_type")

    @property
    @pulumi.getter(name="targetAppLists")
    def target_app_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of app names (name represents set of app instances, like 'salesforce' or '
        facebook'), or a combination of app name and app instance ID (like 'facebook.0oapsqQ6dv19pqyEo0g3') you would like as
        the targets of the admin role.
        - Only supported when used with the role type `"APP_ADMIN"`.
        """
        return pulumi.get(self, "target_app_lists")

    @property
    @pulumi.getter(name="targetGroupLists")
    def target_group_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of group IDs you would like as the targets of the admin role.
        - Only supported when used with the role types: `GROUP_MEMBERSHIP_ADMIN`, `HELP_DESK_ADMIN`, or `USER_ADMIN`.
        """
        return pulumi.get(self, "target_group_lists")

