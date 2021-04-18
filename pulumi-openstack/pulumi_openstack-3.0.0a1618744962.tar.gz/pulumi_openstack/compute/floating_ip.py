# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['FloatingIpArgs', 'FloatingIp']

@pulumi.input_type
class FloatingIpArgs:
    def __init__(__self__, *,
                 pool: pulumi.Input[str],
                 region: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FloatingIp resource.
        :param pulumi.Input[str] pool: The name of the pool from which to obtain the floating
               IP. Changing this creates a new floating IP.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a floating IP that can be used with
               a compute instance. If omitted, the `region` argument of the provider
               is used. Changing this creates a new floating IP (which may or may not
               have a different address).
        """
        pulumi.set(__self__, "pool", pool)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def pool(self) -> pulumi.Input[str]:
        """
        The name of the pool from which to obtain the floating
        IP. Changing this creates a new floating IP.
        """
        return pulumi.get(self, "pool")

    @pool.setter
    def pool(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Compute client.
        A Compute client is needed to create a floating IP that can be used with
        a compute instance. If omitted, the `region` argument of the provider
        is used. Changing this creates a new floating IP (which may or may not
        have a different address).
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


@pulumi.input_type
class _FloatingIpState:
    def __init__(__self__, *,
                 address: Optional[pulumi.Input[str]] = None,
                 fixed_ip: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FloatingIp resources.
        :param pulumi.Input[str] address: The actual floating IP address itself.
        :param pulumi.Input[str] fixed_ip: The fixed IP address corresponding to the floating IP.
        :param pulumi.Input[str] instance_id: UUID of the compute instance associated with the floating IP.
        :param pulumi.Input[str] pool: The name of the pool from which to obtain the floating
               IP. Changing this creates a new floating IP.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a floating IP that can be used with
               a compute instance. If omitted, the `region` argument of the provider
               is used. Changing this creates a new floating IP (which may or may not
               have a different address).
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if fixed_ip is not None:
            pulumi.set(__self__, "fixed_ip", fixed_ip)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if pool is not None:
            pulumi.set(__self__, "pool", pool)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def address(self) -> Optional[pulumi.Input[str]]:
        """
        The actual floating IP address itself.
        """
        return pulumi.get(self, "address")

    @address.setter
    def address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address", value)

    @property
    @pulumi.getter(name="fixedIp")
    def fixed_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The fixed IP address corresponding to the floating IP.
        """
        return pulumi.get(self, "fixed_ip")

    @fixed_ip.setter
    def fixed_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fixed_ip", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        UUID of the compute instance associated with the floating IP.
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def pool(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the pool from which to obtain the floating
        IP. Changing this creates a new floating IP.
        """
        return pulumi.get(self, "pool")

    @pool.setter
    def pool(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Compute client.
        A Compute client is needed to create a floating IP that can be used with
        a compute instance. If omitted, the `region` argument of the provider
        is used. Changing this creates a new floating IP (which may or may not
        have a different address).
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)


class FloatingIp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V2 floating IP resource within OpenStack Nova (compute)
        that can be used for compute instances.

        Please note that managing floating IPs through the OpenStack Compute API has
        been deprecated. Unless you are using an older OpenStack environment, it is
        recommended to use the `networking.FloatingIp`
        resource instead, which uses the OpenStack Networking API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        floatip1 = openstack.compute.FloatingIp("floatip1", pool="public")
        ```

        ## Import

        Floating IPs can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:compute/floatingIp:FloatingIp floatip_1 89c60255-9bd6-460c-822a-e2b959ede9d2
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] pool: The name of the pool from which to obtain the floating
               IP. Changing this creates a new floating IP.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a floating IP that can be used with
               a compute instance. If omitted, the `region` argument of the provider
               is used. Changing this creates a new floating IP (which may or may not
               have a different address).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FloatingIpArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a V2 floating IP resource within OpenStack Nova (compute)
        that can be used for compute instances.

        Please note that managing floating IPs through the OpenStack Compute API has
        been deprecated. Unless you are using an older OpenStack environment, it is
        recommended to use the `networking.FloatingIp`
        resource instead, which uses the OpenStack Networking API.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        floatip1 = openstack.compute.FloatingIp("floatip1", pool="public")
        ```

        ## Import

        Floating IPs can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:compute/floatingIp:FloatingIp floatip_1 89c60255-9bd6-460c-822a-e2b959ede9d2
        ```

        :param str resource_name: The name of the resource.
        :param FloatingIpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FloatingIpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
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
            __props__ = FloatingIpArgs.__new__(FloatingIpArgs)

            if pool is None and not opts.urn:
                raise TypeError("Missing required property 'pool'")
            __props__.__dict__["pool"] = pool
            __props__.__dict__["region"] = region
            __props__.__dict__["address"] = None
            __props__.__dict__["fixed_ip"] = None
            __props__.__dict__["instance_id"] = None
        super(FloatingIp, __self__).__init__(
            'openstack:compute/floatingIp:FloatingIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[str]] = None,
            fixed_ip: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            pool: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'FloatingIp':
        """
        Get an existing FloatingIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The actual floating IP address itself.
        :param pulumi.Input[str] fixed_ip: The fixed IP address corresponding to the floating IP.
        :param pulumi.Input[str] instance_id: UUID of the compute instance associated with the floating IP.
        :param pulumi.Input[str] pool: The name of the pool from which to obtain the floating
               IP. Changing this creates a new floating IP.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               A Compute client is needed to create a floating IP that can be used with
               a compute instance. If omitted, the `region` argument of the provider
               is used. Changing this creates a new floating IP (which may or may not
               have a different address).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FloatingIpState.__new__(_FloatingIpState)

        __props__.__dict__["address"] = address
        __props__.__dict__["fixed_ip"] = fixed_ip
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["pool"] = pool
        __props__.__dict__["region"] = region
        return FloatingIp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        The actual floating IP address itself.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="fixedIp")
    def fixed_ip(self) -> pulumi.Output[str]:
        """
        The fixed IP address corresponding to the floating IP.
        """
        return pulumi.get(self, "fixed_ip")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        UUID of the compute instance associated with the floating IP.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def pool(self) -> pulumi.Output[str]:
        """
        The name of the pool from which to obtain the floating
        IP. Changing this creates a new floating IP.
        """
        return pulumi.get(self, "pool")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Compute client.
        A Compute client is needed to create a floating IP that can be used with
        a compute instance. If omitted, the `region` argument of the provider
        is used. Changing this creates a new floating IP (which may or may not
        have a different address).
        """
        return pulumi.get(self, "region")

