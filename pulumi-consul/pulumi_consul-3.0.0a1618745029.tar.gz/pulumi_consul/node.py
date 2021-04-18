# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['NodeArgs', 'Node']

@pulumi.input_type
class NodeArgs:
    def __init__(__self__, *,
                 address: pulumi.Input[str],
                 datacenter: Optional[pulumi.Input[str]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Node resource.
        :param pulumi.Input[str] address: The address of the node being added to,
               or referenced in the catalog.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the agent's
               default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] meta: Key/value pairs that are associated with the node.
        :param pulumi.Input[str] name: The name of the node being added to, or
               referenced in the catalog.
        """
        pulumi.set(__self__, "address", address)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if meta is not None:
            pulumi.set(__self__, "meta", meta)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Input[str]:
        """
        The address of the node being added to,
        or referenced in the catalog.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: pulumi.Input[str]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The datacenter to use. This overrides the agent's
        default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter
    def meta(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key/value pairs that are associated with the node.
        """
        return pulumi.get(self, "meta")

    @meta.setter
    def meta(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "meta", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the node being added to, or
        referenced in the catalog.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


@pulumi.input_type
class _NodeState:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Node resources.
        :param pulumi.Input[str] address: The address of the node being added to,
               or referenced in the catalog.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the agent's
               default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] meta: Key/value pairs that are associated with the node.
        :param pulumi.Input[str] name: The name of the node being added to, or
               referenced in the catalog.
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if meta is not None:
            pulumi.set(__self__, "meta", meta)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        The address of the node being added to,
        or referenced in the catalog.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The datacenter to use. This overrides the agent's
        default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter
    def meta(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key/value pairs that are associated with the node.
        """
        return pulumi.get(self, "meta")

    @meta.setter
    def meta(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "meta", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the node being added to, or
        referenced in the catalog.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


class Node(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides access to Node data in Consul. This can be used to define a
        node. Currently, defining health checks is not supported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_consul as consul

        foobar = consul.Node("foobar", address="192.168.10.10")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The address of the node being added to,
               or referenced in the catalog.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the agent's
               default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] meta: Key/value pairs that are associated with the node.
        :param pulumi.Input[str] name: The name of the node being added to, or
               referenced in the catalog.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NodeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides access to Node data in Consul. This can be used to define a
        node. Currently, defining health checks is not supported.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_consul as consul

        foobar = consul.Node("foobar", address="192.168.10.10")
        ```

        :param str resource_name: The name of the resource.
        :param NodeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NodeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
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
            __props__ = NodeArgs.__new__(NodeArgs)

            if address is None and not opts.urn:
                raise TypeError("Missing required property 'address'")
            __props__.__dict__["address"] = address
            __props__.__dict__["datacenter"] = datacenter
            __props__.__dict__["meta"] = meta
            __props__.__dict__["name"] = name
            __props__.__dict__["token"] = token
        super(Node, __self__).__init__(
            'consul:index/node:Node',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[str]] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            meta: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None) -> 'Node':
        """
        Get an existing Node resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The address of the node being added to,
               or referenced in the catalog.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the agent's
               default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] meta: Key/value pairs that are associated with the node.
        :param pulumi.Input[str] name: The name of the node being added to, or
               referenced in the catalog.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NodeState.__new__(_NodeState)

        __props__.__dict__["address"] = address
        __props__.__dict__["datacenter"] = datacenter
        __props__.__dict__["meta"] = meta
        __props__.__dict__["name"] = name
        __props__.__dict__["token"] = token
        return Node(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        The address of the node being added to,
        or referenced in the catalog.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def datacenter(self) -> pulumi.Output[str]:
        """
        The datacenter to use. This overrides the agent's
        default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter
    def meta(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key/value pairs that are associated with the node.
        """
        return pulumi.get(self, "meta")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the node being added to, or
        referenced in the catalog.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "token")

