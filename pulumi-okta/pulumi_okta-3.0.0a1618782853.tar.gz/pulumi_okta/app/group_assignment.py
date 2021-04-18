# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['GroupAssignmentArgs', 'GroupAssignment']

@pulumi.input_type
class GroupAssignmentArgs:
    def __init__(__self__, *,
                 app_id: pulumi.Input[str],
                 group_id: pulumi.Input[str],
                 priority: Optional[pulumi.Input[int]] = None,
                 profile: Optional[pulumi.Input[str]] = None,
                 retain_assignment: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a GroupAssignment resource.
        :param pulumi.Input[str] app_id: The ID of the application to assign a group to.
        :param pulumi.Input[str] group_id: The ID of the group to assign the app to.
        :param pulumi.Input[str] profile: JSON document containing [application profile](https://developer.okta.com/docs/reference/api/apps/#profile-object)
        :param pulumi.Input[bool] retain_assignment: Retain the group assignment on destroy. If set to true, the resource will be removed from state but not from the Okta app.
        """
        pulumi.set(__self__, "app_id", app_id)
        pulumi.set(__self__, "group_id", group_id)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if profile is not None:
            pulumi.set(__self__, "profile", profile)
        if retain_assignment is not None:
            pulumi.set(__self__, "retain_assignment", retain_assignment)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[str]:
        """
        The ID of the application to assign a group to.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Input[str]:
        """
        The ID of the group to assign the app to.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[str]]:
        """
        JSON document containing [application profile](https://developer.okta.com/docs/reference/api/apps/#profile-object)
        """
        return pulumi.get(self, "profile")

    @profile.setter
    def profile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile", value)

    @property
    @pulumi.getter(name="retainAssignment")
    def retain_assignment(self) -> Optional[pulumi.Input[bool]]:
        """
        Retain the group assignment on destroy. If set to true, the resource will be removed from state but not from the Okta app.
        """
        return pulumi.get(self, "retain_assignment")

    @retain_assignment.setter
    def retain_assignment(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "retain_assignment", value)


@pulumi.input_type
class _GroupAssignmentState:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 profile: Optional[pulumi.Input[str]] = None,
                 retain_assignment: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering GroupAssignment resources.
        :param pulumi.Input[str] app_id: The ID of the application to assign a group to.
        :param pulumi.Input[str] group_id: The ID of the group to assign the app to.
        :param pulumi.Input[str] profile: JSON document containing [application profile](https://developer.okta.com/docs/reference/api/apps/#profile-object)
        :param pulumi.Input[bool] retain_assignment: Retain the group assignment on destroy. If set to true, the resource will be removed from state but not from the Okta app.
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if profile is not None:
            pulumi.set(__self__, "profile", profile)
        if retain_assignment is not None:
            pulumi.set(__self__, "retain_assignment", retain_assignment)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the application to assign a group to.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the group to assign the app to.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def profile(self) -> Optional[pulumi.Input[str]]:
        """
        JSON document containing [application profile](https://developer.okta.com/docs/reference/api/apps/#profile-object)
        """
        return pulumi.get(self, "profile")

    @profile.setter
    def profile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "profile", value)

    @property
    @pulumi.getter(name="retainAssignment")
    def retain_assignment(self) -> Optional[pulumi.Input[bool]]:
        """
        Retain the group assignment on destroy. If set to true, the resource will be removed from state but not from the Okta app.
        """
        return pulumi.get(self, "retain_assignment")

    @retain_assignment.setter
    def retain_assignment(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "retain_assignment", value)


class GroupAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 profile: Optional[pulumi.Input[str]] = None,
                 retain_assignment: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        An application group assignment can be imported via the `app_id` and the `group_id`.

        ```sh
         $ pulumi import okta:app/groupAssignment:GroupAssignment example <app_id>/<group_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: The ID of the application to assign a group to.
        :param pulumi.Input[str] group_id: The ID of the group to assign the app to.
        :param pulumi.Input[str] profile: JSON document containing [application profile](https://developer.okta.com/docs/reference/api/apps/#profile-object)
        :param pulumi.Input[bool] retain_assignment: Retain the group assignment on destroy. If set to true, the resource will be removed from state but not from the Okta app.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GroupAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        An application group assignment can be imported via the `app_id` and the `group_id`.

        ```sh
         $ pulumi import okta:app/groupAssignment:GroupAssignment example <app_id>/<group_id>
        ```

        :param str resource_name: The name of the resource.
        :param GroupAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GroupAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 profile: Optional[pulumi.Input[str]] = None,
                 retain_assignment: Optional[pulumi.Input[bool]] = None,
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
            __props__ = GroupAssignmentArgs.__new__(GroupAssignmentArgs)

            if app_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_id'")
            __props__.__dict__["app_id"] = app_id
            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["priority"] = priority
            __props__.__dict__["profile"] = profile
            __props__.__dict__["retain_assignment"] = retain_assignment
        super(GroupAssignment, __self__).__init__(
            'okta:app/groupAssignment:GroupAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            profile: Optional[pulumi.Input[str]] = None,
            retain_assignment: Optional[pulumi.Input[bool]] = None) -> 'GroupAssignment':
        """
        Get an existing GroupAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: The ID of the application to assign a group to.
        :param pulumi.Input[str] group_id: The ID of the group to assign the app to.
        :param pulumi.Input[str] profile: JSON document containing [application profile](https://developer.okta.com/docs/reference/api/apps/#profile-object)
        :param pulumi.Input[bool] retain_assignment: Retain the group assignment on destroy. If set to true, the resource will be removed from state but not from the Okta app.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GroupAssignmentState.__new__(_GroupAssignmentState)

        __props__.__dict__["app_id"] = app_id
        __props__.__dict__["group_id"] = group_id
        __props__.__dict__["priority"] = priority
        __props__.__dict__["profile"] = profile
        __props__.__dict__["retain_assignment"] = retain_assignment
        return GroupAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        The ID of the application to assign a group to.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The ID of the group to assign the app to.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def profile(self) -> pulumi.Output[Optional[str]]:
        """
        JSON document containing [application profile](https://developer.okta.com/docs/reference/api/apps/#profile-object)
        """
        return pulumi.get(self, "profile")

    @property
    @pulumi.getter(name="retainAssignment")
    def retain_assignment(self) -> pulumi.Output[Optional[bool]]:
        """
        Retain the group assignment on destroy. If set to true, the resource will be removed from state but not from the Okta app.
        """
        return pulumi.get(self, "retain_assignment")

