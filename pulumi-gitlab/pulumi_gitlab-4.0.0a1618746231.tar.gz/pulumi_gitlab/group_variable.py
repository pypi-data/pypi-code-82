# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['GroupVariableArgs', 'GroupVariable']

@pulumi.input_type
class GroupVariableArgs:
    def __init__(__self__, *,
                 group: pulumi.Input[str],
                 key: pulumi.Input[str],
                 value: pulumi.Input[str],
                 masked: Optional[pulumi.Input[bool]] = None,
                 protected: Optional[pulumi.Input[bool]] = None,
                 variable_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GroupVariable resource.
        :param pulumi.Input[str] group: The name or id of the group to add the hook to.
        :param pulumi.Input[str] key: The name of the variable.
        :param pulumi.Input[str] value: The value of the variable.
        :param pulumi.Input[bool] protected: If set to `true`, the variable will be passed only to pipelines running on protected branches and tags. Defaults to `false`.
        :param pulumi.Input[str] variable_type: The type of a variable. Available types are: env_var (default) and file.
        """
        pulumi.set(__self__, "group", group)
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)
        if masked is not None:
            pulumi.set(__self__, "masked", masked)
        if protected is not None:
            pulumi.set(__self__, "protected", protected)
        if variable_type is not None:
            pulumi.set(__self__, "variable_type", variable_type)

    @property
    @pulumi.getter
    def group(self) -> pulumi.Input[str]:
        """
        The name or id of the group to add the hook to.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: pulumi.Input[str]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The name of the variable.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the variable.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def masked(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "masked")

    @masked.setter
    def masked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "masked", value)

    @property
    @pulumi.getter
    def protected(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to `true`, the variable will be passed only to pipelines running on protected branches and tags. Defaults to `false`.
        """
        return pulumi.get(self, "protected")

    @protected.setter
    def protected(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "protected", value)

    @property
    @pulumi.getter(name="variableType")
    def variable_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of a variable. Available types are: env_var (default) and file.
        """
        return pulumi.get(self, "variable_type")

    @variable_type.setter
    def variable_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "variable_type", value)


@pulumi.input_type
class _GroupVariableState:
    def __init__(__self__, *,
                 group: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 masked: Optional[pulumi.Input[bool]] = None,
                 protected: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 variable_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering GroupVariable resources.
        :param pulumi.Input[str] group: The name or id of the group to add the hook to.
        :param pulumi.Input[str] key: The name of the variable.
        :param pulumi.Input[bool] protected: If set to `true`, the variable will be passed only to pipelines running on protected branches and tags. Defaults to `false`.
        :param pulumi.Input[str] value: The value of the variable.
        :param pulumi.Input[str] variable_type: The type of a variable. Available types are: env_var (default) and file.
        """
        if group is not None:
            pulumi.set(__self__, "group", group)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if masked is not None:
            pulumi.set(__self__, "masked", masked)
        if protected is not None:
            pulumi.set(__self__, "protected", protected)
        if value is not None:
            pulumi.set(__self__, "value", value)
        if variable_type is not None:
            pulumi.set(__self__, "variable_type", variable_type)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        The name or id of the group to add the hook to.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the variable.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def masked(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "masked")

    @masked.setter
    def masked(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "masked", value)

    @property
    @pulumi.getter
    def protected(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to `true`, the variable will be passed only to pipelines running on protected branches and tags. Defaults to `false`.
        """
        return pulumi.get(self, "protected")

    @protected.setter
    def protected(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "protected", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the variable.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="variableType")
    def variable_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of a variable. Available types are: env_var (default) and file.
        """
        return pulumi.get(self, "variable_type")

    @variable_type.setter
    def variable_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "variable_type", value)


class GroupVariable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 masked: Optional[pulumi.Input[bool]] = None,
                 protected: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 variable_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## # gitlab\_group\_variable

        This resource allows you to create and manage CI/CD variables for your GitLab groups.
        For further information on variables, consult the [gitlab
        documentation](https://docs.gitlab.com/ce/ci/variables/README.html#variables).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        example = gitlab.GroupVariable("example",
            group="12345",
            key="group_variable_key",
            masked=False,
            protected=False,
            value="group_variable_value")
        ```

        ## Import

        GitLab group variables can be imported using an id made up of `groupid:variablename`, e.g.

        ```sh
         $ pulumi import gitlab:index/groupVariable:GroupVariable example 12345:group_variable_key
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group: The name or id of the group to add the hook to.
        :param pulumi.Input[str] key: The name of the variable.
        :param pulumi.Input[bool] protected: If set to `true`, the variable will be passed only to pipelines running on protected branches and tags. Defaults to `false`.
        :param pulumi.Input[str] value: The value of the variable.
        :param pulumi.Input[str] variable_type: The type of a variable. Available types are: env_var (default) and file.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupVariableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # gitlab\_group\_variable

        This resource allows you to create and manage CI/CD variables for your GitLab groups.
        For further information on variables, consult the [gitlab
        documentation](https://docs.gitlab.com/ce/ci/variables/README.html#variables).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        example = gitlab.GroupVariable("example",
            group="12345",
            key="group_variable_key",
            masked=False,
            protected=False,
            value="group_variable_value")
        ```

        ## Import

        GitLab group variables can be imported using an id made up of `groupid:variablename`, e.g.

        ```sh
         $ pulumi import gitlab:index/groupVariable:GroupVariable example 12345:group_variable_key
        ```

        :param str resource_name: The name of the resource.
        :param GroupVariableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupVariableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 masked: Optional[pulumi.Input[bool]] = None,
                 protected: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 variable_type: Optional[pulumi.Input[str]] = None,
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
            __props__ = GroupVariableArgs.__new__(GroupVariableArgs)

            if group is None and not opts.urn:
                raise TypeError("Missing required property 'group'")
            __props__.__dict__["group"] = group
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["masked"] = masked
            __props__.__dict__["protected"] = protected
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = value
            __props__.__dict__["variable_type"] = variable_type
        super(GroupVariable, __self__).__init__(
            'gitlab:index/groupVariable:GroupVariable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            masked: Optional[pulumi.Input[bool]] = None,
            protected: Optional[pulumi.Input[bool]] = None,
            value: Optional[pulumi.Input[str]] = None,
            variable_type: Optional[pulumi.Input[str]] = None) -> 'GroupVariable':
        """
        Get an existing GroupVariable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group: The name or id of the group to add the hook to.
        :param pulumi.Input[str] key: The name of the variable.
        :param pulumi.Input[bool] protected: If set to `true`, the variable will be passed only to pipelines running on protected branches and tags. Defaults to `false`.
        :param pulumi.Input[str] value: The value of the variable.
        :param pulumi.Input[str] variable_type: The type of a variable. Available types are: env_var (default) and file.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupVariableState.__new__(_GroupVariableState)

        __props__.__dict__["group"] = group
        __props__.__dict__["key"] = key
        __props__.__dict__["masked"] = masked
        __props__.__dict__["protected"] = protected
        __props__.__dict__["value"] = value
        __props__.__dict__["variable_type"] = variable_type
        return GroupVariable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def group(self) -> pulumi.Output[str]:
        """
        The name or id of the group to add the hook to.
        """
        return pulumi.get(self, "group")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The name of the variable.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def masked(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "masked")

    @property
    @pulumi.getter
    def protected(self) -> pulumi.Output[Optional[bool]]:
        """
        If set to `true`, the variable will be passed only to pipelines running on protected branches and tags. Defaults to `false`.
        """
        return pulumi.get(self, "protected")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of the variable.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="variableType")
    def variable_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of a variable. Available types are: env_var (default) and file.
        """
        return pulumi.get(self, "variable_type")

