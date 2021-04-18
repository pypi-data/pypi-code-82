# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AddressScopeArgs', 'AddressScope']

@pulumi.input_type
class AddressScopeArgs:
    def __init__(__self__, *,
                 ip_version: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 shared: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a AddressScope resource.
        :param pulumi.Input[int] ip_version: IP version, either 4 (default) or 6. Changing this
               creates a new address-scope.
        :param pulumi.Input[str] name: The name of the address-scope. Changing this updates the
               name of the existing address-scope.
        :param pulumi.Input[str] project_id: The owner of the address-scope. Required if admin
               wants to create a address-scope for another project. Changing this creates a
               new address-scope.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron address-scope. If omitted,
               the `region` argument of the provider is used. Changing this creates a new
               address-scope.
        :param pulumi.Input[bool] shared: Indicates whether this address-scope is shared across
               all projects. Changing this updates the shared status of the existing
               address-scope.
        """
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if shared is not None:
            pulumi.set(__self__, "shared", shared)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[int]]:
        """
        IP version, either 4 (default) or 6. Changing this
        creates a new address-scope.
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ip_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the address-scope. Changing this updates the
        name of the existing address-scope.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The owner of the address-scope. Required if admin
        wants to create a address-scope for another project. Changing this creates a
        new address-scope.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create a Neutron address-scope. If omitted,
        the `region` argument of the provider is used. Changing this creates a new
        address-scope.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def shared(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether this address-scope is shared across
        all projects. Changing this updates the shared status of the existing
        address-scope.
        """
        return pulumi.get(self, "shared")

    @shared.setter
    def shared(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "shared", value)


@pulumi.input_type
class _AddressScopeState:
    def __init__(__self__, *,
                 ip_version: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 shared: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering AddressScope resources.
        :param pulumi.Input[int] ip_version: IP version, either 4 (default) or 6. Changing this
               creates a new address-scope.
        :param pulumi.Input[str] name: The name of the address-scope. Changing this updates the
               name of the existing address-scope.
        :param pulumi.Input[str] project_id: The owner of the address-scope. Required if admin
               wants to create a address-scope for another project. Changing this creates a
               new address-scope.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron address-scope. If omitted,
               the `region` argument of the provider is used. Changing this creates a new
               address-scope.
        :param pulumi.Input[bool] shared: Indicates whether this address-scope is shared across
               all projects. Changing this updates the shared status of the existing
               address-scope.
        """
        if ip_version is not None:
            pulumi.set(__self__, "ip_version", ip_version)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if shared is not None:
            pulumi.set(__self__, "shared", shared)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[pulumi.Input[int]]:
        """
        IP version, either 4 (default) or 6. Changing this
        creates a new address-scope.
        """
        return pulumi.get(self, "ip_version")

    @ip_version.setter
    def ip_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "ip_version", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the address-scope. Changing this updates the
        name of the existing address-scope.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The owner of the address-scope. Required if admin
        wants to create a address-scope for another project. Changing this creates a
        new address-scope.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create a Neutron address-scope. If omitted,
        the `region` argument of the provider is used. Changing this creates a new
        address-scope.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def shared(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether this address-scope is shared across
        all projects. Changing this updates the shared status of the existing
        address-scope.
        """
        return pulumi.get(self, "shared")

    @shared.setter
    def shared(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "shared", value)


class AddressScope(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_version: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 shared: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V2 Neutron addressscope resource within OpenStack.

        ## Example Usage
        ### Create an Address-scope

        ```python
        import pulumi
        import pulumi_openstack as openstack

        addressscope1 = openstack.networking.AddressScope("addressscope1", ip_version=6)
        ```
        ### Create a Subnet Pool from an Address-scope

        ```python
        import pulumi
        import pulumi_openstack as openstack

        addressscope1 = openstack.networking.AddressScope("addressscope1", ip_version=6)
        subnetpool1 = openstack.networking.SubnetPool("subnetpool1",
            address_scope_id=addressscope1.id,
            prefixes=[
                "fdf7:b13d:dead:beef::/64",
                "fd65:86cc:a334:39b7::/64",
            ])
        ```

        ## Import

        Address-scopes can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:networking/addressScope:AddressScope addressscope_1 9cc35860-522a-4d35-974d-51d4b011801e
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] ip_version: IP version, either 4 (default) or 6. Changing this
               creates a new address-scope.
        :param pulumi.Input[str] name: The name of the address-scope. Changing this updates the
               name of the existing address-scope.
        :param pulumi.Input[str] project_id: The owner of the address-scope. Required if admin
               wants to create a address-scope for another project. Changing this creates a
               new address-scope.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron address-scope. If omitted,
               the `region` argument of the provider is used. Changing this creates a new
               address-scope.
        :param pulumi.Input[bool] shared: Indicates whether this address-scope is shared across
               all projects. Changing this updates the shared status of the existing
               address-scope.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AddressScopeArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a V2 Neutron addressscope resource within OpenStack.

        ## Example Usage
        ### Create an Address-scope

        ```python
        import pulumi
        import pulumi_openstack as openstack

        addressscope1 = openstack.networking.AddressScope("addressscope1", ip_version=6)
        ```
        ### Create a Subnet Pool from an Address-scope

        ```python
        import pulumi
        import pulumi_openstack as openstack

        addressscope1 = openstack.networking.AddressScope("addressscope1", ip_version=6)
        subnetpool1 = openstack.networking.SubnetPool("subnetpool1",
            address_scope_id=addressscope1.id,
            prefixes=[
                "fdf7:b13d:dead:beef::/64",
                "fd65:86cc:a334:39b7::/64",
            ])
        ```

        ## Import

        Address-scopes can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:networking/addressScope:AddressScope addressscope_1 9cc35860-522a-4d35-974d-51d4b011801e
        ```

        :param str resource_name: The name of the resource.
        :param AddressScopeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AddressScopeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_version: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 shared: Optional[pulumi.Input[bool]] = None,
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
            __props__ = AddressScopeArgs.__new__(AddressScopeArgs)

            __props__.__dict__["ip_version"] = ip_version
            __props__.__dict__["name"] = name
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["region"] = region
            __props__.__dict__["shared"] = shared
        super(AddressScope, __self__).__init__(
            'openstack:networking/addressScope:AddressScope',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ip_version: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            shared: Optional[pulumi.Input[bool]] = None) -> 'AddressScope':
        """
        Get an existing AddressScope resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] ip_version: IP version, either 4 (default) or 6. Changing this
               creates a new address-scope.
        :param pulumi.Input[str] name: The name of the address-scope. Changing this updates the
               name of the existing address-scope.
        :param pulumi.Input[str] project_id: The owner of the address-scope. Required if admin
               wants to create a address-scope for another project. Changing this creates a
               new address-scope.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron address-scope. If omitted,
               the `region` argument of the provider is used. Changing this creates a new
               address-scope.
        :param pulumi.Input[bool] shared: Indicates whether this address-scope is shared across
               all projects. Changing this updates the shared status of the existing
               address-scope.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AddressScopeState.__new__(_AddressScopeState)

        __props__.__dict__["ip_version"] = ip_version
        __props__.__dict__["name"] = name
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["region"] = region
        __props__.__dict__["shared"] = shared
        return AddressScope(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> pulumi.Output[Optional[int]]:
        """
        IP version, either 4 (default) or 6. Changing this
        creates a new address-scope.
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the address-scope. Changing this updates the
        name of the existing address-scope.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The owner of the address-scope. Required if admin
        wants to create a address-scope for another project. Changing this creates a
        new address-scope.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create a Neutron address-scope. If omitted,
        the `region` argument of the provider is used. Changing this creates a new
        address-scope.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def shared(self) -> pulumi.Output[bool]:
        """
        Indicates whether this address-scope is shared across
        all projects. Changing this updates the shared status of the existing
        address-scope.
        """
        return pulumi.get(self, "shared")

