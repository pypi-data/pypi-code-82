# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['RoleArgs', 'Role']

@pulumi.input_type
class RoleArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]] = None):
        """
        The set of arguments for constructing a Role resource.
        :param pulumi.Input[str] name: Name of the role.
        :param pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]] permissions: Set of objects containing the permission ID and the name of the permissions granted to this role.
        """
        pulumi.set(__self__, "name", name)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the role.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]]:
        """
        Set of objects containing the permission ID and the name of the permissions granted to this role.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]]):
        pulumi.set(self, "permissions", value)


@pulumi.input_type
class _RoleState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]] = None,
                 user_count: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Role resources.
        :param pulumi.Input[str] name: Name of the role.
        :param pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]] permissions: Set of objects containing the permission ID and the name of the permissions granted to this role.
        :param pulumi.Input[int] user_count: Number of users that have this role.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if permissions is not None:
            pulumi.set(__self__, "permissions", permissions)
        if user_count is not None:
            pulumi.set(__self__, "user_count", user_count)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the role.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def permissions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]]:
        """
        Set of objects containing the permission ID and the name of the permissions granted to this role.
        """
        return pulumi.get(self, "permissions")

    @permissions.setter
    def permissions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RolePermissionArgs']]]]):
        pulumi.set(self, "permissions", value)

    @property
    @pulumi.getter(name="userCount")
    def user_count(self) -> Optional[pulumi.Input[int]]:
        """
        Number of users that have this role.
        """
        return pulumi.get(self, "user_count")

    @user_count.setter
    def user_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "user_count", value)


class Role(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Datadog role resource. This can be used to create and manage Datadog roles.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datadog as datadog

        bar = datadog.get_permissions()
        # Create a new Datadog role
        foo = datadog.Role("foo",
            name="foo",
            permissions=[
                datadog.RolePermissionArgs(
                    id=bar.permissions["monitorsDowntime"],
                ),
                datadog.RolePermissionArgs(
                    id=bar.permissions["monitorsWrite"],
                ),
            ])
        ```

        ## Import

        Roles can be imported using their ID, e.g.

        ```sh
         $ pulumi import datadog:index/role:Role example_role 000000-0000-0000-0000-000000000000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the role.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]] permissions: Set of objects containing the permission ID and the name of the permissions granted to this role.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Datadog role resource. This can be used to create and manage Datadog roles.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datadog as datadog

        bar = datadog.get_permissions()
        # Create a new Datadog role
        foo = datadog.Role("foo",
            name="foo",
            permissions=[
                datadog.RolePermissionArgs(
                    id=bar.permissions["monitorsDowntime"],
                ),
                datadog.RolePermissionArgs(
                    id=bar.permissions["monitorsWrite"],
                ),
            ])
        ```

        ## Import

        Roles can be imported using their ID, e.g.

        ```sh
         $ pulumi import datadog:index/role:Role example_role 000000-0000-0000-0000-000000000000
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
                 name: Optional[pulumi.Input[str]] = None,
                 permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]]] = None,
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

            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["permissions"] = permissions
            __props__.__dict__["user_count"] = None
        super(Role, __self__).__init__(
            'datadog:index/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            permissions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]]] = None,
            user_count: Optional[pulumi.Input[int]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the role.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RolePermissionArgs']]]] permissions: Set of objects containing the permission ID and the name of the permissions granted to this role.
        :param pulumi.Input[int] user_count: Number of users that have this role.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RoleState.__new__(_RoleState)

        __props__.__dict__["name"] = name
        __props__.__dict__["permissions"] = permissions
        __props__.__dict__["user_count"] = user_count
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the role.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permissions(self) -> pulumi.Output[Optional[Sequence['outputs.RolePermission']]]:
        """
        Set of objects containing the permission ID and the name of the permissions granted to this role.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="userCount")
    def user_count(self) -> pulumi.Output[int]:
        """
        Number of users that have this role.
        """
        return pulumi.get(self, "user_count")

