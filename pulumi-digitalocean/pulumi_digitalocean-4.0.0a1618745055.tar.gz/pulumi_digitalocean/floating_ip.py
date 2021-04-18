# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FloatingIpArgs', 'FloatingIp']

@pulumi.input_type
class FloatingIpArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 droplet_id: Optional[pulumi.Input[int]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FloatingIp resource.
        :param pulumi.Input[str] region: The region that the Floating IP is reserved to.
        :param pulumi.Input[int] droplet_id: The ID of Droplet that the Floating IP will be assigned to.
        :param pulumi.Input[str] ip_address: The IP Address of the resource
        """
        pulumi.set(__self__, "region", region)
        if droplet_id is not None:
            pulumi.set(__self__, "droplet_id", droplet_id)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        """
        The region that the Floating IP is reserved to.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="dropletId")
    def droplet_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of Droplet that the Floating IP will be assigned to.
        """
        return pulumi.get(self, "droplet_id")

    @droplet_id.setter
    def droplet_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "droplet_id", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP Address of the resource
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)


@pulumi.input_type
class _FloatingIpState:
    def __init__(__self__, *,
                 droplet_id: Optional[pulumi.Input[int]] = None,
                 floating_ip_urn: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FloatingIp resources.
        :param pulumi.Input[int] droplet_id: The ID of Droplet that the Floating IP will be assigned to.
        :param pulumi.Input[str] floating_ip_urn: The uniform resource name of the floating ip
        :param pulumi.Input[str] ip_address: The IP Address of the resource
        :param pulumi.Input[str] region: The region that the Floating IP is reserved to.
        """
        if droplet_id is not None:
            pulumi.set(__self__, "droplet_id", droplet_id)
        if floating_ip_urn is not None:
            pulumi.set(__self__, "floating_ip_urn", floating_ip_urn)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if region is not None:
            pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter(name="dropletId")
    def droplet_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of Droplet that the Floating IP will be assigned to.
        """
        return pulumi.get(self, "droplet_id")

    @droplet_id.setter
    def droplet_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "droplet_id", value)

    @property
    @pulumi.getter(name="floatingIpUrn")
    def floating_ip_urn(self) -> Optional[pulumi.Input[str]]:
        """
        The uniform resource name of the floating ip
        """
        return pulumi.get(self, "floating_ip_urn")

    @floating_ip_urn.setter
    def floating_ip_urn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "floating_ip_urn", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        The IP Address of the resource
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region that the Floating IP is reserved to.
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
                 droplet_id: Optional[pulumi.Input[int]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a DigitalOcean Floating IP to represent a publicly-accessible static IP addresses that can be mapped to one of your Droplets.

        > **NOTE:** Floating IPs can be assigned to a Droplet either directly on the `FloatingIp` resource by setting a `droplet_id` or using the `FloatingIpAssignment` resource, but the two cannot be used together.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        foobar_droplet = digitalocean.Droplet("foobarDroplet",
            size="s-1vcpu-1gb",
            image="ubuntu-18-04-x64",
            region="sgp1",
            ipv6=True,
            private_networking=True)
        foobar_floating_ip = digitalocean.FloatingIp("foobarFloatingIp",
            droplet_id=foobar_droplet.id,
            region=foobar_droplet.region)
        ```

        ## Import

        Floating IPs can be imported using the `ip`, e.g.

        ```sh
         $ pulumi import digitalocean:index/floatingIp:FloatingIp myip 192.168.0.1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] droplet_id: The ID of Droplet that the Floating IP will be assigned to.
        :param pulumi.Input[str] ip_address: The IP Address of the resource
        :param pulumi.Input[str] region: The region that the Floating IP is reserved to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FloatingIpArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a DigitalOcean Floating IP to represent a publicly-accessible static IP addresses that can be mapped to one of your Droplets.

        > **NOTE:** Floating IPs can be assigned to a Droplet either directly on the `FloatingIp` resource by setting a `droplet_id` or using the `FloatingIpAssignment` resource, but the two cannot be used together.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_digitalocean as digitalocean

        foobar_droplet = digitalocean.Droplet("foobarDroplet",
            size="s-1vcpu-1gb",
            image="ubuntu-18-04-x64",
            region="sgp1",
            ipv6=True,
            private_networking=True)
        foobar_floating_ip = digitalocean.FloatingIp("foobarFloatingIp",
            droplet_id=foobar_droplet.id,
            region=foobar_droplet.region)
        ```

        ## Import

        Floating IPs can be imported using the `ip`, e.g.

        ```sh
         $ pulumi import digitalocean:index/floatingIp:FloatingIp myip 192.168.0.1
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
                 droplet_id: Optional[pulumi.Input[int]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
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

            __props__.__dict__["droplet_id"] = droplet_id
            __props__.__dict__["ip_address"] = ip_address
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["floating_ip_urn"] = None
        super(FloatingIp, __self__).__init__(
            'digitalocean:index/floatingIp:FloatingIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            droplet_id: Optional[pulumi.Input[int]] = None,
            floating_ip_urn: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'FloatingIp':
        """
        Get an existing FloatingIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] droplet_id: The ID of Droplet that the Floating IP will be assigned to.
        :param pulumi.Input[str] floating_ip_urn: The uniform resource name of the floating ip
        :param pulumi.Input[str] ip_address: The IP Address of the resource
        :param pulumi.Input[str] region: The region that the Floating IP is reserved to.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FloatingIpState.__new__(_FloatingIpState)

        __props__.__dict__["droplet_id"] = droplet_id
        __props__.__dict__["floating_ip_urn"] = floating_ip_urn
        __props__.__dict__["ip_address"] = ip_address
        __props__.__dict__["region"] = region
        return FloatingIp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dropletId")
    def droplet_id(self) -> pulumi.Output[Optional[int]]:
        """
        The ID of Droplet that the Floating IP will be assigned to.
        """
        return pulumi.get(self, "droplet_id")

    @property
    @pulumi.getter(name="floatingIpUrn")
    def floating_ip_urn(self) -> pulumi.Output[str]:
        """
        The uniform resource name of the floating ip
        """
        return pulumi.get(self, "floating_ip_urn")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        The IP Address of the resource
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region that the Floating IP is reserved to.
        """
        return pulumi.get(self, "region")

