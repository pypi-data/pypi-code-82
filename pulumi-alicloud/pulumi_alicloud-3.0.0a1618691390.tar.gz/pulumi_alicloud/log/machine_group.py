# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MachineGroupArgs', 'MachineGroup']

@pulumi.input_type
class MachineGroupArgs:
    def __init__(__self__, *,
                 identify_lists: pulumi.Input[Sequence[pulumi.Input[str]]],
                 project: pulumi.Input[str],
                 identify_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MachineGroup resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identify_lists: The specific machine identification, which can be an IP address or user-defined identity.
        :param pulumi.Input[str] project: The project name to the machine group belongs.
        :param pulumi.Input[str] identify_type: The machine identification type, including IP and user-defined identity. Valid values are "ip" and "userdefined". Default to "ip".
        :param pulumi.Input[str] name: The machine group name, which is unique in the same project.
        :param pulumi.Input[str] topic: The topic of a machine group.
        """
        pulumi.set(__self__, "identify_lists", identify_lists)
        pulumi.set(__self__, "project", project)
        if identify_type is not None:
            pulumi.set(__self__, "identify_type", identify_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="identifyLists")
    def identify_lists(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The specific machine identification, which can be an IP address or user-defined identity.
        """
        return pulumi.get(self, "identify_lists")

    @identify_lists.setter
    def identify_lists(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "identify_lists", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The project name to the machine group belongs.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="identifyType")
    def identify_type(self) -> Optional[pulumi.Input[str]]:
        """
        The machine identification type, including IP and user-defined identity. Valid values are "ip" and "userdefined". Default to "ip".
        """
        return pulumi.get(self, "identify_type")

    @identify_type.setter
    def identify_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identify_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The machine group name, which is unique in the same project.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        The topic of a machine group.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)


@pulumi.input_type
class _MachineGroupState:
    def __init__(__self__, *,
                 identify_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 identify_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MachineGroup resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identify_lists: The specific machine identification, which can be an IP address or user-defined identity.
        :param pulumi.Input[str] identify_type: The machine identification type, including IP and user-defined identity. Valid values are "ip" and "userdefined". Default to "ip".
        :param pulumi.Input[str] name: The machine group name, which is unique in the same project.
        :param pulumi.Input[str] project: The project name to the machine group belongs.
        :param pulumi.Input[str] topic: The topic of a machine group.
        """
        if identify_lists is not None:
            pulumi.set(__self__, "identify_lists", identify_lists)
        if identify_type is not None:
            pulumi.set(__self__, "identify_type", identify_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)

    @property
    @pulumi.getter(name="identifyLists")
    def identify_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The specific machine identification, which can be an IP address or user-defined identity.
        """
        return pulumi.get(self, "identify_lists")

    @identify_lists.setter
    def identify_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "identify_lists", value)

    @property
    @pulumi.getter(name="identifyType")
    def identify_type(self) -> Optional[pulumi.Input[str]]:
        """
        The machine identification type, including IP and user-defined identity. Valid values are "ip" and "userdefined". Default to "ip".
        """
        return pulumi.get(self, "identify_type")

    @identify_type.setter
    def identify_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identify_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The machine group name, which is unique in the same project.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The project name to the machine group belongs.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        The topic of a machine group.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)


class MachineGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identify_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 identify_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        Log machine group can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:log/machineGroup:MachineGroup example tf-log:tf-machine-group
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identify_lists: The specific machine identification, which can be an IP address or user-defined identity.
        :param pulumi.Input[str] identify_type: The machine identification type, including IP and user-defined identity. Valid values are "ip" and "userdefined". Default to "ip".
        :param pulumi.Input[str] name: The machine group name, which is unique in the same project.
        :param pulumi.Input[str] project: The project name to the machine group belongs.
        :param pulumi.Input[str] topic: The topic of a machine group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MachineGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        Log machine group can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:log/machineGroup:MachineGroup example tf-log:tf-machine-group
        ```

        :param str resource_name: The name of the resource.
        :param MachineGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MachineGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identify_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 identify_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
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
            __props__ = MachineGroupArgs.__new__(MachineGroupArgs)

            if identify_lists is None and not opts.urn:
                raise TypeError("Missing required property 'identify_lists'")
            __props__.__dict__["identify_lists"] = identify_lists
            __props__.__dict__["identify_type"] = identify_type
            __props__.__dict__["name"] = name
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            __props__.__dict__["topic"] = topic
        super(MachineGroup, __self__).__init__(
            'alicloud:log/machineGroup:MachineGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            identify_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            identify_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            topic: Optional[pulumi.Input[str]] = None) -> 'MachineGroup':
        """
        Get an existing MachineGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] identify_lists: The specific machine identification, which can be an IP address or user-defined identity.
        :param pulumi.Input[str] identify_type: The machine identification type, including IP and user-defined identity. Valid values are "ip" and "userdefined". Default to "ip".
        :param pulumi.Input[str] name: The machine group name, which is unique in the same project.
        :param pulumi.Input[str] project: The project name to the machine group belongs.
        :param pulumi.Input[str] topic: The topic of a machine group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MachineGroupState.__new__(_MachineGroupState)

        __props__.__dict__["identify_lists"] = identify_lists
        __props__.__dict__["identify_type"] = identify_type
        __props__.__dict__["name"] = name
        __props__.__dict__["project"] = project
        __props__.__dict__["topic"] = topic
        return MachineGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="identifyLists")
    def identify_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        The specific machine identification, which can be an IP address or user-defined identity.
        """
        return pulumi.get(self, "identify_lists")

    @property
    @pulumi.getter(name="identifyType")
    def identify_type(self) -> pulumi.Output[Optional[str]]:
        """
        The machine identification type, including IP and user-defined identity. Valid values are "ip" and "userdefined". Default to "ip".
        """
        return pulumi.get(self, "identify_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The machine group name, which is unique in the same project.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The project name to the machine group belongs.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[Optional[str]]:
        """
        The topic of a machine group.
        """
        return pulumi.get(self, "topic")

