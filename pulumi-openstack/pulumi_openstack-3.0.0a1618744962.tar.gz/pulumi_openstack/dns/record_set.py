# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RecordSetArgs', 'RecordSet']

@pulumi.input_type
class RecordSetArgs:
    def __init__(__self__, *,
                 zone_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a RecordSet resource.
        :param pulumi.Input[str] zone_id: The ID of the zone in which to create the record set.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[str] description: A description of the  record set.
        :param pulumi.Input[str] name: The name of the record set. Note the `.` at the end of the name.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] records: An array of DNS records. _Note:_ if an IPv6 address
               contains brackets (`[ ]`), the brackets will be stripped and the modified
               address will be recorded in the state.
        :param pulumi.Input[str] region: The region in which to obtain the V2 DNS client.
               If omitted, the `region` argument of the provider is used.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[int] ttl: The time to live (TTL) of the record set.
        :param pulumi.Input[str] type: The type of record set. Examples: "A", "MX".
               Changing this creates a new DNS  record set.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options. Changing this creates a
               new record set.
        """
        pulumi.set(__self__, "zone_id", zone_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if records is not None:
            pulumi.set(__self__, "records", records)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value_specs is not None:
            pulumi.set(__self__, "value_specs", value_specs)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Input[str]:
        """
        The ID of the zone in which to create the record set.
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the  record set.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the record set. Note the `.` at the end of the name.
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of DNS records. _Note:_ if an IPv6 address
        contains brackets (`[ ]`), the brackets will be stripped and the modified
        address will be recorded in the state.
        """
        return pulumi.get(self, "records")

    @records.setter
    def records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "records", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 DNS client.
        If omitted, the `region` argument of the provider is used.
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        The time to live (TTL) of the record set.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of record set. Examples: "A", "MX".
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="valueSpecs")
    def value_specs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of additional options. Changing this creates a
        new record set.
        """
        return pulumi.get(self, "value_specs")

    @value_specs.setter
    def value_specs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "value_specs", value)


@pulumi.input_type
class _RecordSetState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RecordSet resources.
        :param pulumi.Input[str] description: A description of the  record set.
        :param pulumi.Input[str] name: The name of the record set. Note the `.` at the end of the name.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] records: An array of DNS records. _Note:_ if an IPv6 address
               contains brackets (`[ ]`), the brackets will be stripped and the modified
               address will be recorded in the state.
        :param pulumi.Input[str] region: The region in which to obtain the V2 DNS client.
               If omitted, the `region` argument of the provider is used.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[int] ttl: The time to live (TTL) of the record set.
        :param pulumi.Input[str] type: The type of record set. Examples: "A", "MX".
               Changing this creates a new DNS  record set.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options. Changing this creates a
               new record set.
        :param pulumi.Input[str] zone_id: The ID of the zone in which to create the record set.
               Changing this creates a new DNS  record set.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if records is not None:
            pulumi.set(__self__, "records", records)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if ttl is not None:
            pulumi.set(__self__, "ttl", ttl)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if value_specs is not None:
            pulumi.set(__self__, "value_specs", value_specs)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the  record set.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the record set. Note the `.` at the end of the name.
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def records(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array of DNS records. _Note:_ if an IPv6 address
        contains brackets (`[ ]`), the brackets will be stripped and the modified
        address will be recorded in the state.
        """
        return pulumi.get(self, "records")

    @records.setter
    def records(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "records", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 DNS client.
        If omitted, the `region` argument of the provider is used.
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def ttl(self) -> Optional[pulumi.Input[int]]:
        """
        The time to live (TTL) of the record set.
        """
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of record set. Examples: "A", "MX".
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="valueSpecs")
    def value_specs(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Map of additional options. Changing this creates a
        new record set.
        """
        return pulumi.get(self, "value_specs")

    @value_specs.setter
    def value_specs(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "value_specs", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the zone in which to create the record set.
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class RecordSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a DNS record set in the OpenStack DNS Service.

        ## Example Usage
        ### Automatically detect the correct network

        ```python
        import pulumi
        import pulumi_openstack as openstack

        example_zone = openstack.dns.Zone("exampleZone",
            description="a zone",
            email="email2@example.com",
            ttl=6000,
            type="PRIMARY")
        rs_example_com = openstack.dns.RecordSet("rsExampleCom",
            description="An example record set",
            records=["10.0.0.1"],
            ttl=3000,
            type="A",
            zone_id=example_zone.id)
        ```

        ## Import

        This resource can be imported by specifying the zone ID and recordset ID, separated by a forward slash.

        ```sh
         $ pulumi import openstack:dns/recordSet:RecordSet recordset_1 <zone_id>/<recordset_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the  record set.
        :param pulumi.Input[str] name: The name of the record set. Note the `.` at the end of the name.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] records: An array of DNS records. _Note:_ if an IPv6 address
               contains brackets (`[ ]`), the brackets will be stripped and the modified
               address will be recorded in the state.
        :param pulumi.Input[str] region: The region in which to obtain the V2 DNS client.
               If omitted, the `region` argument of the provider is used.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[int] ttl: The time to live (TTL) of the record set.
        :param pulumi.Input[str] type: The type of record set. Examples: "A", "MX".
               Changing this creates a new DNS  record set.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options. Changing this creates a
               new record set.
        :param pulumi.Input[str] zone_id: The ID of the zone in which to create the record set.
               Changing this creates a new DNS  record set.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RecordSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a DNS record set in the OpenStack DNS Service.

        ## Example Usage
        ### Automatically detect the correct network

        ```python
        import pulumi
        import pulumi_openstack as openstack

        example_zone = openstack.dns.Zone("exampleZone",
            description="a zone",
            email="email2@example.com",
            ttl=6000,
            type="PRIMARY")
        rs_example_com = openstack.dns.RecordSet("rsExampleCom",
            description="An example record set",
            records=["10.0.0.1"],
            ttl=3000,
            type="A",
            zone_id=example_zone.id)
        ```

        ## Import

        This resource can be imported by specifying the zone ID and recordset ID, separated by a forward slash.

        ```sh
         $ pulumi import openstack:dns/recordSet:RecordSet recordset_1 <zone_id>/<recordset_id>
        ```

        :param str resource_name: The name of the resource.
        :param RecordSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RecordSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 ttl: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
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
            __props__ = RecordSetArgs.__new__(RecordSetArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["records"] = records
            __props__.__dict__["region"] = region
            __props__.__dict__["ttl"] = ttl
            __props__.__dict__["type"] = type
            __props__.__dict__["value_specs"] = value_specs
            if zone_id is None and not opts.urn:
                raise TypeError("Missing required property 'zone_id'")
            __props__.__dict__["zone_id"] = zone_id
        super(RecordSet, __self__).__init__(
            'openstack:dns/recordSet:RecordSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            records: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            region: Optional[pulumi.Input[str]] = None,
            ttl: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'RecordSet':
        """
        Get an existing RecordSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A description of the  record set.
        :param pulumi.Input[str] name: The name of the record set. Note the `.` at the end of the name.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] records: An array of DNS records. _Note:_ if an IPv6 address
               contains brackets (`[ ]`), the brackets will be stripped and the modified
               address will be recorded in the state.
        :param pulumi.Input[str] region: The region in which to obtain the V2 DNS client.
               If omitted, the `region` argument of the provider is used.
               Changing this creates a new DNS  record set.
        :param pulumi.Input[int] ttl: The time to live (TTL) of the record set.
        :param pulumi.Input[str] type: The type of record set. Examples: "A", "MX".
               Changing this creates a new DNS  record set.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options. Changing this creates a
               new record set.
        :param pulumi.Input[str] zone_id: The ID of the zone in which to create the record set.
               Changing this creates a new DNS  record set.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RecordSetState.__new__(_RecordSetState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["records"] = records
        __props__.__dict__["region"] = region
        __props__.__dict__["ttl"] = ttl
        __props__.__dict__["type"] = type
        __props__.__dict__["value_specs"] = value_specs
        __props__.__dict__["zone_id"] = zone_id
        return RecordSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the  record set.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the record set. Note the `.` at the end of the name.
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def records(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        An array of DNS records. _Note:_ if an IPv6 address
        contains brackets (`[ ]`), the brackets will be stripped and the modified
        address will be recorded in the state.
        """
        return pulumi.get(self, "records")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 DNS client.
        If omitted, the `region` argument of the provider is used.
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Output[int]:
        """
        The time to live (TTL) of the record set.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of record set. Examples: "A", "MX".
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="valueSpecs")
    def value_specs(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Map of additional options. Changing this creates a
        new record set.
        """
        return pulumi.get(self, "value_specs")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The ID of the zone in which to create the record set.
        Changing this creates a new DNS  record set.
        """
        return pulumi.get(self, "zone_id")

