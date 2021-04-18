# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['NetworkAreaArgs', 'NetworkArea']

@pulumi.input_type
class NetworkAreaArgs:
    def __init__(__self__, *,
                 peer_datacenter: pulumi.Input[str],
                 datacenter: Optional[pulumi.Input[str]] = None,
                 retry_joins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 use_tls: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a NetworkArea resource.
        :param pulumi.Input[str] peer_datacenter: The name of the Consul datacenter that will be
               joined to form the area.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] retry_joins: Specifies a list of Consul servers to attempt to
               join. Servers can be given as `IP`, `IP:port`, `hostname`, or `hostname:port`.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        :param pulumi.Input[bool] use_tls: Specifies whether gossip over this area should be
               encrypted with TLS if possible. Defaults to `false`.
        """
        pulumi.set(__self__, "peer_datacenter", peer_datacenter)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if retry_joins is not None:
            pulumi.set(__self__, "retry_joins", retry_joins)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if use_tls is not None:
            pulumi.set(__self__, "use_tls", use_tls)

    @property
    @pulumi.getter(name="peerDatacenter")
    def peer_datacenter(self) -> pulumi.Input[str]:
        """
        The name of the Consul datacenter that will be
        joined to form the area.
        """
        return pulumi.get(self, "peer_datacenter")

    @peer_datacenter.setter
    def peer_datacenter(self, value: pulumi.Input[str]):
        pulumi.set(self, "peer_datacenter", value)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The datacenter to use. This overrides the
        agent's default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter(name="retryJoins")
    def retry_joins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of Consul servers to attempt to
        join. Servers can be given as `IP`, `IP:port`, `hostname`, or `hostname:port`.
        """
        return pulumi.get(self, "retry_joins")

    @retry_joins.setter
    def retry_joins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "retry_joins", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The ACL token to use. This overrides the
        token that the agent provides by default.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter(name="useTls")
    def use_tls(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether gossip over this area should be
        encrypted with TLS if possible. Defaults to `false`.
        """
        return pulumi.get(self, "use_tls")

    @use_tls.setter
    def use_tls(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_tls", value)


@pulumi.input_type
class _NetworkAreaState:
    def __init__(__self__, *,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 peer_datacenter: Optional[pulumi.Input[str]] = None,
                 retry_joins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 use_tls: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering NetworkArea resources.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[str] peer_datacenter: The name of the Consul datacenter that will be
               joined to form the area.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] retry_joins: Specifies a list of Consul servers to attempt to
               join. Servers can be given as `IP`, `IP:port`, `hostname`, or `hostname:port`.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        :param pulumi.Input[bool] use_tls: Specifies whether gossip over this area should be
               encrypted with TLS if possible. Defaults to `false`.
        """
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if peer_datacenter is not None:
            pulumi.set(__self__, "peer_datacenter", peer_datacenter)
        if retry_joins is not None:
            pulumi.set(__self__, "retry_joins", retry_joins)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if use_tls is not None:
            pulumi.set(__self__, "use_tls", use_tls)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The datacenter to use. This overrides the
        agent's default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter(name="peerDatacenter")
    def peer_datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Consul datacenter that will be
        joined to form the area.
        """
        return pulumi.get(self, "peer_datacenter")

    @peer_datacenter.setter
    def peer_datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_datacenter", value)

    @property
    @pulumi.getter(name="retryJoins")
    def retry_joins(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies a list of Consul servers to attempt to
        join. Servers can be given as `IP`, `IP:port`, `hostname`, or `hostname:port`.
        """
        return pulumi.get(self, "retry_joins")

    @retry_joins.setter
    def retry_joins(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "retry_joins", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The ACL token to use. This overrides the
        token that the agent provides by default.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter(name="useTls")
    def use_tls(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether gossip over this area should be
        encrypted with TLS if possible. Defaults to `false`.
        """
        return pulumi.get(self, "use_tls")

    @use_tls.setter
    def use_tls(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_tls", value)


class NetworkArea(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 peer_datacenter: Optional[pulumi.Input[str]] = None,
                 retry_joins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 use_tls: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        > **NOTE:** This feature requires [Consul Enterprise](https://www.consul.io/docs/enterprise/index.html).

        The `NetworkArea` resource manages a relationship between servers in two
        different Consul datacenters.

        Unlike Consul's WAN feature, network areas use just the server RPC port for
        communication, and relationships can be made between independent pairs of
        datacenters, so not all servers need to be fully connected. This allows for
        complex topologies among Consul datacenters like hub/spoke and more general trees.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_consul as consul

        dc2 = consul.NetworkArea("dc2",
            peer_datacenter="dc2",
            retry_joins=["1.2.3.4"],
            use_tls=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[str] peer_datacenter: The name of the Consul datacenter that will be
               joined to form the area.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] retry_joins: Specifies a list of Consul servers to attempt to
               join. Servers can be given as `IP`, `IP:port`, `hostname`, or `hostname:port`.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        :param pulumi.Input[bool] use_tls: Specifies whether gossip over this area should be
               encrypted with TLS if possible. Defaults to `false`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkAreaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        > **NOTE:** This feature requires [Consul Enterprise](https://www.consul.io/docs/enterprise/index.html).

        The `NetworkArea` resource manages a relationship between servers in two
        different Consul datacenters.

        Unlike Consul's WAN feature, network areas use just the server RPC port for
        communication, and relationships can be made between independent pairs of
        datacenters, so not all servers need to be fully connected. This allows for
        complex topologies among Consul datacenters like hub/spoke and more general trees.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_consul as consul

        dc2 = consul.NetworkArea("dc2",
            peer_datacenter="dc2",
            retry_joins=["1.2.3.4"],
            use_tls=True)
        ```

        :param str resource_name: The name of the resource.
        :param NetworkAreaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkAreaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 peer_datacenter: Optional[pulumi.Input[str]] = None,
                 retry_joins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 use_tls: Optional[pulumi.Input[bool]] = None,
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
            __props__ = NetworkAreaArgs.__new__(NetworkAreaArgs)

            __props__.__dict__["datacenter"] = datacenter
            if peer_datacenter is None and not opts.urn:
                raise TypeError("Missing required property 'peer_datacenter'")
            __props__.__dict__["peer_datacenter"] = peer_datacenter
            __props__.__dict__["retry_joins"] = retry_joins
            __props__.__dict__["token"] = token
            __props__.__dict__["use_tls"] = use_tls
        super(NetworkArea, __self__).__init__(
            'consul:index/networkArea:NetworkArea',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            peer_datacenter: Optional[pulumi.Input[str]] = None,
            retry_joins: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            token: Optional[pulumi.Input[str]] = None,
            use_tls: Optional[pulumi.Input[bool]] = None) -> 'NetworkArea':
        """
        Get an existing NetworkArea resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[str] peer_datacenter: The name of the Consul datacenter that will be
               joined to form the area.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] retry_joins: Specifies a list of Consul servers to attempt to
               join. Servers can be given as `IP`, `IP:port`, `hostname`, or `hostname:port`.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        :param pulumi.Input[bool] use_tls: Specifies whether gossip over this area should be
               encrypted with TLS if possible. Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NetworkAreaState.__new__(_NetworkAreaState)

        __props__.__dict__["datacenter"] = datacenter
        __props__.__dict__["peer_datacenter"] = peer_datacenter
        __props__.__dict__["retry_joins"] = retry_joins
        __props__.__dict__["token"] = token
        __props__.__dict__["use_tls"] = use_tls
        return NetworkArea(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def datacenter(self) -> pulumi.Output[str]:
        """
        The datacenter to use. This overrides the
        agent's default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter(name="peerDatacenter")
    def peer_datacenter(self) -> pulumi.Output[str]:
        """
        The name of the Consul datacenter that will be
        joined to form the area.
        """
        return pulumi.get(self, "peer_datacenter")

    @property
    @pulumi.getter(name="retryJoins")
    def retry_joins(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies a list of Consul servers to attempt to
        join. Servers can be given as `IP`, `IP:port`, `hostname`, or `hostname:port`.
        """
        return pulumi.get(self, "retry_joins")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[str]]:
        """
        The ACL token to use. This overrides the
        token that the agent provides by default.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter(name="useTls")
    def use_tls(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether gossip over this area should be
        encrypted with TLS if possible. Defaults to `false`.
        """
        return pulumi.get(self, "use_tls")

