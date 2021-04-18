# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ComputeClusterHostGroupArgs', 'ComputeClusterHostGroup']

@pulumi.input_type
class ComputeClusterHostGroupArgs:
    def __init__(__self__, *,
                 compute_cluster_id: pulumi.Input[str],
                 host_system_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ComputeClusterHostGroup resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_system_ids: The managed object IDs of
               the hosts to put in the cluster.
        :param pulumi.Input[str] name: The name of the host group. This must be unique in the
               cluster. Forces a new resource if changed.
        """
        pulumi.set(__self__, "compute_cluster_id", compute_cluster_id)
        if host_system_ids is not None:
            pulumi.set(__self__, "host_system_ids", host_system_ids)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="computeClusterId")
    def compute_cluster_id(self) -> pulumi.Input[str]:
        """
        The managed object reference
        ID of the cluster to put the group in.  Forces a new
        resource if changed.
        """
        return pulumi.get(self, "compute_cluster_id")

    @compute_cluster_id.setter
    def compute_cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "compute_cluster_id", value)

    @property
    @pulumi.getter(name="hostSystemIds")
    def host_system_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The managed object IDs of
        the hosts to put in the cluster.
        """
        return pulumi.get(self, "host_system_ids")

    @host_system_ids.setter
    def host_system_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "host_system_ids", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the host group. This must be unique in the
        cluster. Forces a new resource if changed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ComputeClusterHostGroupState:
    def __init__(__self__, *,
                 compute_cluster_id: Optional[pulumi.Input[str]] = None,
                 host_system_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ComputeClusterHostGroup resources.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_system_ids: The managed object IDs of
               the hosts to put in the cluster.
        :param pulumi.Input[str] name: The name of the host group. This must be unique in the
               cluster. Forces a new resource if changed.
        """
        if compute_cluster_id is not None:
            pulumi.set(__self__, "compute_cluster_id", compute_cluster_id)
        if host_system_ids is not None:
            pulumi.set(__self__, "host_system_ids", host_system_ids)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="computeClusterId")
    def compute_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The managed object reference
        ID of the cluster to put the group in.  Forces a new
        resource if changed.
        """
        return pulumi.get(self, "compute_cluster_id")

    @compute_cluster_id.setter
    def compute_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compute_cluster_id", value)

    @property
    @pulumi.getter(name="hostSystemIds")
    def host_system_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The managed object IDs of
        the hosts to put in the cluster.
        """
        return pulumi.get(self, "host_system_ids")

    @host_system_ids.setter
    def host_system_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "host_system_ids", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the host group. This must be unique in the
        cluster. Forces a new resource if changed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class ComputeClusterHostGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_cluster_id: Optional[pulumi.Input[str]] = None,
                 host_system_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a ComputeClusterHostGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_system_ids: The managed object IDs of
               the hosts to put in the cluster.
        :param pulumi.Input[str] name: The name of the host group. This must be unique in the
               cluster. Forces a new resource if changed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ComputeClusterHostGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a ComputeClusterHostGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ComputeClusterHostGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ComputeClusterHostGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compute_cluster_id: Optional[pulumi.Input[str]] = None,
                 host_system_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ComputeClusterHostGroupArgs.__new__(ComputeClusterHostGroupArgs)

            if compute_cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'compute_cluster_id'")
            __props__.__dict__["compute_cluster_id"] = compute_cluster_id
            __props__.__dict__["host_system_ids"] = host_system_ids
            __props__.__dict__["name"] = name
        super(ComputeClusterHostGroup, __self__).__init__(
            'vsphere:index/computeClusterHostGroup:ComputeClusterHostGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compute_cluster_id: Optional[pulumi.Input[str]] = None,
            host_system_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'ComputeClusterHostGroup':
        """
        Get an existing ComputeClusterHostGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compute_cluster_id: The managed object reference
               ID of the cluster to put the group in.  Forces a new
               resource if changed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_system_ids: The managed object IDs of
               the hosts to put in the cluster.
        :param pulumi.Input[str] name: The name of the host group. This must be unique in the
               cluster. Forces a new resource if changed.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ComputeClusterHostGroupState.__new__(_ComputeClusterHostGroupState)

        __props__.__dict__["compute_cluster_id"] = compute_cluster_id
        __props__.__dict__["host_system_ids"] = host_system_ids
        __props__.__dict__["name"] = name
        return ComputeClusterHostGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="computeClusterId")
    def compute_cluster_id(self) -> pulumi.Output[str]:
        """
        The managed object reference
        ID of the cluster to put the group in.  Forces a new
        resource if changed.
        """
        return pulumi.get(self, "compute_cluster_id")

    @property
    @pulumi.getter(name="hostSystemIds")
    def host_system_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The managed object IDs of
        the hosts to put in the cluster.
        """
        return pulumi.get(self, "host_system_ids")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the host group. This must be unique in the
        cluster. Forces a new resource if changed.
        """
        return pulumi.get(self, "name")

