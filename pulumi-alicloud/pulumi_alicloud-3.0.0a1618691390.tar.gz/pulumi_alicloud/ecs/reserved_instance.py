# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ReservedInstanceArgs', 'ReservedInstance']

@pulumi.input_type
class ReservedInstanceArgs:
    def __init__(__self__, *,
                 instance_type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 instance_amount: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offering_type: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 period_unit: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ReservedInstance resource.
        :param pulumi.Input[str] instance_type: Instance type of the RI. For more information, see [Instance type families](https://www.alibabacloud.com/help/doc-detail/25378.html).
        :param pulumi.Input[str] description: Description of the RI. 2 to 256 English or Chinese characters. It cannot start with http:// or https://.
        :param pulumi.Input[int] instance_amount: Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).
        :param pulumi.Input[str] name: Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (_), and hyphens. It must start with a letter. It cannot start with http:// or https://.
        :param pulumi.Input[str] offering_type: Payment type of the RI. Optional values: `No Upfront`: No upfront payment is required., `Partial Upfront`: A portion of upfront payment is required.`All Upfront`: Full upfront payment is required.
        :param pulumi.Input[str] period_unit: Term unit. Optional value: Year.
        :param pulumi.Input[str] platform: The operating system type of the image used by the instance. Optional values: `Windows`, `Linux`. Default is `Linux`.
        :param pulumi.Input[str] resource_group_id: Resource group ID.
        :param pulumi.Input[str] scope: Scope of the RI. Optional values: `Region`: region-level, `Zone`: zone-level. Default is `Region`.
        :param pulumi.Input[str] zone_id: ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see [DescribeZones](https://www.alibabacloud.com/help/doc-detail/25610.html).
        """
        pulumi.set(__self__, "instance_type", instance_type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_amount is not None:
            pulumi.set(__self__, "instance_amount", instance_amount)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if offering_type is not None:
            pulumi.set(__self__, "offering_type", offering_type)
        if period is not None:
            pulumi.set(__self__, "period", period)
        if period_unit is not None:
            pulumi.set(__self__, "period_unit", period_unit)
        if platform is not None:
            pulumi.set(__self__, "platform", platform)
        if resource_group_id is not None:
            pulumi.set(__self__, "resource_group_id", resource_group_id)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[str]:
        """
        Instance type of the RI. For more information, see [Instance type families](https://www.alibabacloud.com/help/doc-detail/25378.html).
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the RI. 2 to 256 English or Chinese characters. It cannot start with http:// or https://.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceAmount")
    def instance_amount(self) -> Optional[pulumi.Input[int]]:
        """
        Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).
        """
        return pulumi.get(self, "instance_amount")

    @instance_amount.setter
    def instance_amount(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_amount", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (_), and hyphens. It must start with a letter. It cannot start with http:// or https://.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> Optional[pulumi.Input[str]]:
        """
        Payment type of the RI. Optional values: `No Upfront`: No upfront payment is required., `Partial Upfront`: A portion of upfront payment is required.`All Upfront`: Full upfront payment is required.
        """
        return pulumi.get(self, "offering_type")

    @offering_type.setter
    def offering_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "offering_type", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter(name="periodUnit")
    def period_unit(self) -> Optional[pulumi.Input[str]]:
        """
        Term unit. Optional value: Year.
        """
        return pulumi.get(self, "period_unit")

    @period_unit.setter
    def period_unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "period_unit", value)

    @property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[str]]:
        """
        The operating system type of the image used by the instance. Optional values: `Windows`, `Linux`. Default is `Linux`.
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platform", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource group ID.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        Scope of the RI. Optional values: `Region`: region-level, `Zone`: zone-level. Default is `Region`.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see [DescribeZones](https://www.alibabacloud.com/help/doc-detail/25610.html).
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _ReservedInstanceState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_amount: Optional[pulumi.Input[int]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offering_type: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 period_unit: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ReservedInstance resources.
        :param pulumi.Input[str] description: Description of the RI. 2 to 256 English or Chinese characters. It cannot start with http:// or https://.
        :param pulumi.Input[int] instance_amount: Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).
        :param pulumi.Input[str] instance_type: Instance type of the RI. For more information, see [Instance type families](https://www.alibabacloud.com/help/doc-detail/25378.html).
        :param pulumi.Input[str] name: Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (_), and hyphens. It must start with a letter. It cannot start with http:// or https://.
        :param pulumi.Input[str] offering_type: Payment type of the RI. Optional values: `No Upfront`: No upfront payment is required., `Partial Upfront`: A portion of upfront payment is required.`All Upfront`: Full upfront payment is required.
        :param pulumi.Input[str] period_unit: Term unit. Optional value: Year.
        :param pulumi.Input[str] platform: The operating system type of the image used by the instance. Optional values: `Windows`, `Linux`. Default is `Linux`.
        :param pulumi.Input[str] resource_group_id: Resource group ID.
        :param pulumi.Input[str] scope: Scope of the RI. Optional values: `Region`: region-level, `Zone`: zone-level. Default is `Region`.
        :param pulumi.Input[str] zone_id: ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see [DescribeZones](https://www.alibabacloud.com/help/doc-detail/25610.html).
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if instance_amount is not None:
            pulumi.set(__self__, "instance_amount", instance_amount)
        if instance_type is not None:
            pulumi.set(__self__, "instance_type", instance_type)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if offering_type is not None:
            pulumi.set(__self__, "offering_type", offering_type)
        if period is not None:
            pulumi.set(__self__, "period", period)
        if period_unit is not None:
            pulumi.set(__self__, "period_unit", period_unit)
        if platform is not None:
            pulumi.set(__self__, "platform", platform)
        if resource_group_id is not None:
            pulumi.set(__self__, "resource_group_id", resource_group_id)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the RI. 2 to 256 English or Chinese characters. It cannot start with http:// or https://.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="instanceAmount")
    def instance_amount(self) -> Optional[pulumi.Input[int]]:
        """
        Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).
        """
        return pulumi.get(self, "instance_amount")

    @instance_amount.setter
    def instance_amount(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_amount", value)

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> Optional[pulumi.Input[str]]:
        """
        Instance type of the RI. For more information, see [Instance type families](https://www.alibabacloud.com/help/doc-detail/25378.html).
        """
        return pulumi.get(self, "instance_type")

    @instance_type.setter
    def instance_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (_), and hyphens. It must start with a letter. It cannot start with http:// or https://.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> Optional[pulumi.Input[str]]:
        """
        Payment type of the RI. Optional values: `No Upfront`: No upfront payment is required., `Partial Upfront`: A portion of upfront payment is required.`All Upfront`: Full upfront payment is required.
        """
        return pulumi.get(self, "offering_type")

    @offering_type.setter
    def offering_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "offering_type", value)

    @property
    @pulumi.getter
    def period(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "period")

    @period.setter
    def period(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "period", value)

    @property
    @pulumi.getter(name="periodUnit")
    def period_unit(self) -> Optional[pulumi.Input[str]]:
        """
        Term unit. Optional value: Year.
        """
        return pulumi.get(self, "period_unit")

    @period_unit.setter
    def period_unit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "period_unit", value)

    @property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input[str]]:
        """
        The operating system type of the image used by the instance. Optional values: `Windows`, `Linux`. Default is `Linux`.
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "platform", value)

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource group ID.
        """
        return pulumi.get(self, "resource_group_id")

    @resource_group_id.setter
    def resource_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_group_id", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        Scope of the RI. Optional values: `Region`: region-level, `Zone`: zone-level. Default is `Region`.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see [DescribeZones](https://www.alibabacloud.com/help/doc-detail/25610.html).
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class ReservedInstance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_amount: Optional[pulumi.Input[int]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offering_type: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 period_unit: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides an Reserved Instance resource.

        > **NOTE:** Available in 1.65.0+

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.ReservedInstance("default",
            instance_type="ecs.g6.large",
            instance_amount=1,
            period_unit="Year",
            offering_type="All Upfront",
            description="ReservedInstance",
            zone_id="cn-hangzhou-h",
            scope="Zone",
            period=1)
        ```

        ## Import

        reservedInstance can be imported using id, e.g.

        ```sh
         $ pulumi import alicloud:ecs/reservedInstance:ReservedInstance default ecsri-uf6df4xm0h3licit****
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the RI. 2 to 256 English or Chinese characters. It cannot start with http:// or https://.
        :param pulumi.Input[int] instance_amount: Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).
        :param pulumi.Input[str] instance_type: Instance type of the RI. For more information, see [Instance type families](https://www.alibabacloud.com/help/doc-detail/25378.html).
        :param pulumi.Input[str] name: Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (_), and hyphens. It must start with a letter. It cannot start with http:// or https://.
        :param pulumi.Input[str] offering_type: Payment type of the RI. Optional values: `No Upfront`: No upfront payment is required., `Partial Upfront`: A portion of upfront payment is required.`All Upfront`: Full upfront payment is required.
        :param pulumi.Input[str] period_unit: Term unit. Optional value: Year.
        :param pulumi.Input[str] platform: The operating system type of the image used by the instance. Optional values: `Windows`, `Linux`. Default is `Linux`.
        :param pulumi.Input[str] resource_group_id: Resource group ID.
        :param pulumi.Input[str] scope: Scope of the RI. Optional values: `Region`: region-level, `Zone`: zone-level. Default is `Region`.
        :param pulumi.Input[str] zone_id: ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see [DescribeZones](https://www.alibabacloud.com/help/doc-detail/25610.html).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReservedInstanceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Reserved Instance resource.

        > **NOTE:** Available in 1.65.0+

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.ReservedInstance("default",
            instance_type="ecs.g6.large",
            instance_amount=1,
            period_unit="Year",
            offering_type="All Upfront",
            description="ReservedInstance",
            zone_id="cn-hangzhou-h",
            scope="Zone",
            period=1)
        ```

        ## Import

        reservedInstance can be imported using id, e.g.

        ```sh
         $ pulumi import alicloud:ecs/reservedInstance:ReservedInstance default ecsri-uf6df4xm0h3licit****
        ```

        :param str resource_name: The name of the resource.
        :param ReservedInstanceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReservedInstanceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 instance_amount: Optional[pulumi.Input[int]] = None,
                 instance_type: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 offering_type: Optional[pulumi.Input[str]] = None,
                 period: Optional[pulumi.Input[int]] = None,
                 period_unit: Optional[pulumi.Input[str]] = None,
                 platform: Optional[pulumi.Input[str]] = None,
                 resource_group_id: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = ReservedInstanceArgs.__new__(ReservedInstanceArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["instance_amount"] = instance_amount
            if instance_type is None and not opts.urn:
                raise TypeError("Missing required property 'instance_type'")
            __props__.__dict__["instance_type"] = instance_type
            __props__.__dict__["name"] = name
            __props__.__dict__["offering_type"] = offering_type
            __props__.__dict__["period"] = period
            __props__.__dict__["period_unit"] = period_unit
            __props__.__dict__["platform"] = platform
            __props__.__dict__["resource_group_id"] = resource_group_id
            __props__.__dict__["scope"] = scope
            __props__.__dict__["zone_id"] = zone_id
        super(ReservedInstance, __self__).__init__(
            'alicloud:ecs/reservedInstance:ReservedInstance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            instance_amount: Optional[pulumi.Input[int]] = None,
            instance_type: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            offering_type: Optional[pulumi.Input[str]] = None,
            period: Optional[pulumi.Input[int]] = None,
            period_unit: Optional[pulumi.Input[str]] = None,
            platform: Optional[pulumi.Input[str]] = None,
            resource_group_id: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'ReservedInstance':
        """
        Get an existing ReservedInstance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the RI. 2 to 256 English or Chinese characters. It cannot start with http:// or https://.
        :param pulumi.Input[int] instance_amount: Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).
        :param pulumi.Input[str] instance_type: Instance type of the RI. For more information, see [Instance type families](https://www.alibabacloud.com/help/doc-detail/25378.html).
        :param pulumi.Input[str] name: Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (_), and hyphens. It must start with a letter. It cannot start with http:// or https://.
        :param pulumi.Input[str] offering_type: Payment type of the RI. Optional values: `No Upfront`: No upfront payment is required., `Partial Upfront`: A portion of upfront payment is required.`All Upfront`: Full upfront payment is required.
        :param pulumi.Input[str] period_unit: Term unit. Optional value: Year.
        :param pulumi.Input[str] platform: The operating system type of the image used by the instance. Optional values: `Windows`, `Linux`. Default is `Linux`.
        :param pulumi.Input[str] resource_group_id: Resource group ID.
        :param pulumi.Input[str] scope: Scope of the RI. Optional values: `Region`: region-level, `Zone`: zone-level. Default is `Region`.
        :param pulumi.Input[str] zone_id: ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see [DescribeZones](https://www.alibabacloud.com/help/doc-detail/25610.html).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ReservedInstanceState.__new__(_ReservedInstanceState)

        __props__.__dict__["description"] = description
        __props__.__dict__["instance_amount"] = instance_amount
        __props__.__dict__["instance_type"] = instance_type
        __props__.__dict__["name"] = name
        __props__.__dict__["offering_type"] = offering_type
        __props__.__dict__["period"] = period
        __props__.__dict__["period_unit"] = period_unit
        __props__.__dict__["platform"] = platform
        __props__.__dict__["resource_group_id"] = resource_group_id
        __props__.__dict__["scope"] = scope
        __props__.__dict__["zone_id"] = zone_id
        return ReservedInstance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the RI. 2 to 256 English or Chinese characters. It cannot start with http:// or https://.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="instanceAmount")
    def instance_amount(self) -> pulumi.Output[int]:
        """
        Number of instances allocated to an RI (An RI is a coupon that includes one or more allocated instances.).
        """
        return pulumi.get(self, "instance_amount")

    @property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Output[str]:
        """
        Instance type of the RI. For more information, see [Instance type families](https://www.alibabacloud.com/help/doc-detail/25378.html).
        """
        return pulumi.get(self, "instance_type")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the RI. The name must be a string of 2 to 128 characters in length and can contain letters, numbers, colons (:), underscores (_), and hyphens. It must start with a letter. It cannot start with http:// or https://.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="offeringType")
    def offering_type(self) -> pulumi.Output[Optional[str]]:
        """
        Payment type of the RI. Optional values: `No Upfront`: No upfront payment is required., `Partial Upfront`: A portion of upfront payment is required.`All Upfront`: Full upfront payment is required.
        """
        return pulumi.get(self, "offering_type")

    @property
    @pulumi.getter
    def period(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "period")

    @property
    @pulumi.getter(name="periodUnit")
    def period_unit(self) -> pulumi.Output[Optional[str]]:
        """
        Term unit. Optional value: Year.
        """
        return pulumi.get(self, "period_unit")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output[str]:
        """
        The operating system type of the image used by the instance. Optional values: `Windows`, `Linux`. Default is `Linux`.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> pulumi.Output[str]:
        """
        Resource group ID.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        Scope of the RI. Optional values: `Region`: region-level, `Zone`: zone-level. Default is `Region`.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the zone to which the RI belongs. When Scope is set to Zone, this parameter is required. For information about the zone list, see [DescribeZones](https://www.alibabacloud.com/help/doc-detail/25610.html).
        """
        return pulumi.get(self, "zone_id")

