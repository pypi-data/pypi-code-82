# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IpSetArgs', 'IpSet']

@pulumi.input_type
class IpSetArgs:
    def __init__(__self__, *,
                 accelerate_region_id: pulumi.Input[str],
                 accelerator_id: pulumi.Input[str],
                 bandwidth: Optional[pulumi.Input[int]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IpSet resource.
        :param pulumi.Input[str] accelerate_region_id: The ID of an acceleration region.
        :param pulumi.Input[str] accelerator_id: The ID of the Global Accelerator (GA) instance.
        :param pulumi.Input[int] bandwidth: The bandwidth allocated to the acceleration region.
        :param pulumi.Input[str] ip_version: The IP protocol used by the GA instance. Valid values: `IPv4`, `IPv6`. Default value is `IPv4`.
        """
        pulumi.set(__self__, "accelerate_region_id", accelerate_region_id)
        pulumi.set(__self__, "accelerator_id", accelerator_id)
        if bandwidth is not None:
            pulumi.set(__self__, "bandwidth", bandwidth)
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)

    @property
    @pulumi.getter(name="accelerateRegionId")
    def accelerate_region_id(self) -> pulumi.Input[str]:
        """
        The ID of an acceleration region.
        """
        return pulumi.get(self, "accelerate_region_id")

    @accelerate_region_id.setter
    def accelerate_region_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "accelerate_region_id", value)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Input[str]:
        """
        The ID of the Global Accelerator (GA) instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter
    def bandwidth(self) -> Optional[pulumi.Input[int]]:
        """
        The bandwidth allocated to the acceleration region.
        """
        return pulumi.get(self, "bandwidth")

    @bandwidth.setter
    def bandwidth(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bandwidth", value)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[str]]:
        """
        The IP protocol used by the GA instance. Valid values: `IPv4`, `IPv6`. Default value is `IPv4`.
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_version", value)


@pulumi.input_type
class _IpSetState:
    def __init__(__self__, *,
                 accelerate_region_id: Optional[pulumi.Input[str]] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 bandwidth: Optional[pulumi.Input[int]] = None,
                 ip_address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IpSet resources.
        :param pulumi.Input[str] accelerate_region_id: The ID of an acceleration region.
        :param pulumi.Input[str] accelerator_id: The ID of the Global Accelerator (GA) instance.
        :param pulumi.Input[int] bandwidth: The bandwidth allocated to the acceleration region.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_address_lists: The list of accelerated IP addresses in the acceleration region.
        :param pulumi.Input[str] ip_version: The IP protocol used by the GA instance. Valid values: `IPv4`, `IPv6`. Default value is `IPv4`.
        :param pulumi.Input[str] status: The status of the acceleration region.
        """
        if accelerate_region_id is not None:
            pulumi.set(__self__, "accelerate_region_id", accelerate_region_id)
        if accelerator_id is not None:
            pulumi.set(__self__, "accelerator_id", accelerator_id)
        if bandwidth is not None:
            pulumi.set(__self__, "bandwidth", bandwidth)
        if ip_address_lists is not None:
            pulumi.set(__self__, "ip_address_lists", ip_address_lists)
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="accelerateRegionId")
    def accelerate_region_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of an acceleration region.
        """
        return pulumi.get(self, "accelerate_region_id")

    @accelerate_region_id.setter
    def accelerate_region_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerate_region_id", value)

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Global Accelerator (GA) instance.
        """
        return pulumi.get(self, "accelerator_id")

    @accelerator_id.setter
    def accelerator_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerator_id", value)

    @property
    @pulumi.getter
    def bandwidth(self) -> Optional[pulumi.Input[int]]:
        """
        The bandwidth allocated to the acceleration region.
        """
        return pulumi.get(self, "bandwidth")

    @bandwidth.setter
    def bandwidth(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bandwidth", value)

    @property
    @pulumi.getter(name="ipAddressLists")
    def ip_address_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of accelerated IP addresses in the acceleration region.
        """
        return pulumi.get(self, "ip_address_lists")

    @ip_address_lists.setter
    def ip_address_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ip_address_lists", value)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[str]]:
        """
        The IP protocol used by the GA instance. Valid values: `IPv4`, `IPv6`. Default value is `IPv4`.
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_version", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the acceleration region.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class IpSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerate_region_id: Optional[pulumi.Input[str]] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 bandwidth: Optional[pulumi.Input[int]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Global Accelerator (GA) Ip Set resource.

        For information about Global Accelerator (GA) Ip Set and how to use it, see [What is Ip Set](https://www.alibabacloud.com/help/en/doc-detail/153246.htm).

        > **NOTE:** Available in v1.113.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_accelerator = alicloud.ga.Accelerator("exampleAccelerator",
            duration=1,
            auto_use_coupon=True,
            spec="1")
        example_bandwidth_package = alicloud.ga.BandwidthPackage("exampleBandwidthPackage",
            bandwidth=20,
            type="Basic",
            bandwidth_type="Basic",
            duration="1",
            auto_pay=True,
            ratio=30)
        example_bandwidth_package_attachment = alicloud.ga.BandwidthPackageAttachment("exampleBandwidthPackageAttachment",
            accelerator_id=example_accelerator.id,
            bandwidth_package_id=example_bandwidth_package.id)
        example_ip_set = alicloud.ga.IpSet("exampleIpSet",
            accelerate_region_id="cn-hangzhou",
            bandwidth=5,
            accelerator_id=example_accelerator.id,
            opts=pulumi.ResourceOptions(depends_on=[example_bandwidth_package_attachment]))
        ```

        ## Import

        Ga Ip Set can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/ipSet:IpSet example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerate_region_id: The ID of an acceleration region.
        :param pulumi.Input[str] accelerator_id: The ID of the Global Accelerator (GA) instance.
        :param pulumi.Input[int] bandwidth: The bandwidth allocated to the acceleration region.
        :param pulumi.Input[str] ip_version: The IP protocol used by the GA instance. Valid values: `IPv4`, `IPv6`. Default value is `IPv4`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IpSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global Accelerator (GA) Ip Set resource.

        For information about Global Accelerator (GA) Ip Set and how to use it, see [What is Ip Set](https://www.alibabacloud.com/help/en/doc-detail/153246.htm).

        > **NOTE:** Available in v1.113.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_accelerator = alicloud.ga.Accelerator("exampleAccelerator",
            duration=1,
            auto_use_coupon=True,
            spec="1")
        example_bandwidth_package = alicloud.ga.BandwidthPackage("exampleBandwidthPackage",
            bandwidth=20,
            type="Basic",
            bandwidth_type="Basic",
            duration="1",
            auto_pay=True,
            ratio=30)
        example_bandwidth_package_attachment = alicloud.ga.BandwidthPackageAttachment("exampleBandwidthPackageAttachment",
            accelerator_id=example_accelerator.id,
            bandwidth_package_id=example_bandwidth_package.id)
        example_ip_set = alicloud.ga.IpSet("exampleIpSet",
            accelerate_region_id="cn-hangzhou",
            bandwidth=5,
            accelerator_id=example_accelerator.id,
            opts=pulumi.ResourceOptions(depends_on=[example_bandwidth_package_attachment]))
        ```

        ## Import

        Ga Ip Set can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ga/ipSet:IpSet example <id>
        ```

        :param str resource_name: The name of the resource.
        :param IpSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IpSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerate_region_id: Optional[pulumi.Input[str]] = None,
                 accelerator_id: Optional[pulumi.Input[str]] = None,
                 bandwidth: Optional[pulumi.Input[int]] = None,
                 ip_version: Optional[pulumi.Input[str]] = None,
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
            __props__ = IpSetArgs.__new__(IpSetArgs)

            if accelerate_region_id is None and not opts.urn:
                raise TypeError("Missing required property 'accelerate_region_id'")
            __props__.__dict__["accelerate_region_id"] = accelerate_region_id
            if accelerator_id is None and not opts.urn:
                raise TypeError("Missing required property 'accelerator_id'")
            __props__.__dict__["accelerator_id"] = accelerator_id
            __props__.__dict__["bandwidth"] = bandwidth
            __props__.__dict__["ip_version"] = ip_version
            __props__.__dict__["ip_address_lists"] = None
            __props__.__dict__["status"] = None
        super(IpSet, __self__).__init__(
            'alicloud:ga/ipSet:IpSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accelerate_region_id: Optional[pulumi.Input[str]] = None,
            accelerator_id: Optional[pulumi.Input[str]] = None,
            bandwidth: Optional[pulumi.Input[int]] = None,
            ip_address_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            ip_version: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'IpSet':
        """
        Get an existing IpSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerate_region_id: The ID of an acceleration region.
        :param pulumi.Input[str] accelerator_id: The ID of the Global Accelerator (GA) instance.
        :param pulumi.Input[int] bandwidth: The bandwidth allocated to the acceleration region.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ip_address_lists: The list of accelerated IP addresses in the acceleration region.
        :param pulumi.Input[str] ip_version: The IP protocol used by the GA instance. Valid values: `IPv4`, `IPv6`. Default value is `IPv4`.
        :param pulumi.Input[str] status: The status of the acceleration region.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IpSetState.__new__(_IpSetState)

        __props__.__dict__["accelerate_region_id"] = accelerate_region_id
        __props__.__dict__["accelerator_id"] = accelerator_id
        __props__.__dict__["bandwidth"] = bandwidth
        __props__.__dict__["ip_address_lists"] = ip_address_lists
        __props__.__dict__["ip_version"] = ip_version
        __props__.__dict__["status"] = status
        return IpSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accelerateRegionId")
    def accelerate_region_id(self) -> pulumi.Output[str]:
        """
        The ID of an acceleration region.
        """
        return pulumi.get(self, "accelerate_region_id")

    @property
    @pulumi.getter(name="acceleratorId")
    def accelerator_id(self) -> pulumi.Output[str]:
        """
        The ID of the Global Accelerator (GA) instance.
        """
        return pulumi.get(self, "accelerator_id")

    @property
    @pulumi.getter
    def bandwidth(self) -> pulumi.Output[Optional[int]]:
        """
        The bandwidth allocated to the acceleration region.
        """
        return pulumi.get(self, "bandwidth")

    @property
    @pulumi.getter(name="ipAddressLists")
    def ip_address_lists(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of accelerated IP addresses in the acceleration region.
        """
        return pulumi.get(self, "ip_address_lists")

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> pulumi.Output[Optional[str]]:
        """
        The IP protocol used by the GA instance. Valid values: `IPv4`, `IPv6`. Default value is `IPv4`.
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the acceleration region.
        """
        return pulumi.get(self, "status")

