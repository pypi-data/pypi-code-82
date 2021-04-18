# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['LicenseArgs', 'License']

@pulumi.input_type
class LicenseArgs:
    def __init__(__self__, *,
                 license_key: pulumi.Input[str],
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a License resource.
        :param pulumi.Input[str] license_key: The license key to add.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A map of key/value pairs to be attached as labels (tags) to the license key.
        """
        pulumi.set(__self__, "license_key", license_key)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> pulumi.Input[str]:
        """
        The license key to add.
        """
        return pulumi.get(self, "license_key")

    @license_key.setter
    def license_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "license_key", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of key/value pairs to be attached as labels (tags) to the license key.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)


@pulumi.input_type
class _LicenseState:
    def __init__(__self__, *,
                 edition_key: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 total: Optional[pulumi.Input[int]] = None,
                 used: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering License resources.
        :param pulumi.Input[str] edition_key: The product edition of the license key.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A map of key/value pairs to be attached as labels (tags) to the license key.
        :param pulumi.Input[str] license_key: The license key to add.
        :param pulumi.Input[str] name: The display name for the license.
        :param pulumi.Input[int] total: Total number of units (example: CPUs) contained in the license.
        :param pulumi.Input[int] used: The number of units (example: CPUs) assigned to this license.
        """
        if edition_key is not None:
            pulumi.set(__self__, "edition_key", edition_key)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if license_key is not None:
            pulumi.set(__self__, "license_key", license_key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if total is not None:
            pulumi.set(__self__, "total", total)
        if used is not None:
            pulumi.set(__self__, "used", used)

    @property
    @pulumi.getter(name="editionKey")
    def edition_key(self) -> Optional[pulumi.Input[str]]:
        """
        The product edition of the license key.
        """
        return pulumi.get(self, "edition_key")

    @edition_key.setter
    def edition_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "edition_key", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of key/value pairs to be attached as labels (tags) to the license key.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[pulumi.Input[str]]:
        """
        The license key to add.
        """
        return pulumi.get(self, "license_key")

    @license_key.setter
    def license_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name for the license.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def total(self) -> Optional[pulumi.Input[int]]:
        """
        Total number of units (example: CPUs) contained in the license.
        """
        return pulumi.get(self, "total")

    @total.setter
    def total(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "total", value)

    @property
    @pulumi.getter
    def used(self) -> Optional[pulumi.Input[int]]:
        """
        The number of units (example: CPUs) assigned to this license.
        """
        return pulumi.get(self, "used")

    @used.setter
    def used(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "used", value)


class License(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a VMware vSphere license resource. This can be used to add and remove license keys.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        license_key = vsphere.License("licenseKey",
            labels={
                "VpxClientLicenseLabel": "Hello World",
                "Workflow": "Hello World",
            },
            license_key="452CQ-2EK54-K8742-00000-00000")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A map of key/value pairs to be attached as labels (tags) to the license key.
        :param pulumi.Input[str] license_key: The license key to add.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LicenseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a VMware vSphere license resource. This can be used to add and remove license keys.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        license_key = vsphere.License("licenseKey",
            labels={
                "VpxClientLicenseLabel": "Hello World",
                "Workflow": "Hello World",
            },
            license_key="452CQ-2EK54-K8742-00000-00000")
        ```

        :param str resource_name: The name of the resource.
        :param LicenseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LicenseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
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
            __props__ = LicenseArgs.__new__(LicenseArgs)

            __props__.__dict__["labels"] = labels
            if license_key is None and not opts.urn:
                raise TypeError("Missing required property 'license_key'")
            __props__.__dict__["license_key"] = license_key
            __props__.__dict__["edition_key"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["total"] = None
            __props__.__dict__["used"] = None
        super(License, __self__).__init__(
            'vsphere:index/license:License',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            edition_key: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            license_key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            total: Optional[pulumi.Input[int]] = None,
            used: Optional[pulumi.Input[int]] = None) -> 'License':
        """
        Get an existing License resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] edition_key: The product edition of the license key.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] labels: A map of key/value pairs to be attached as labels (tags) to the license key.
        :param pulumi.Input[str] license_key: The license key to add.
        :param pulumi.Input[str] name: The display name for the license.
        :param pulumi.Input[int] total: Total number of units (example: CPUs) contained in the license.
        :param pulumi.Input[int] used: The number of units (example: CPUs) assigned to this license.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LicenseState.__new__(_LicenseState)

        __props__.__dict__["edition_key"] = edition_key
        __props__.__dict__["labels"] = labels
        __props__.__dict__["license_key"] = license_key
        __props__.__dict__["name"] = name
        __props__.__dict__["total"] = total
        __props__.__dict__["used"] = used
        return License(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="editionKey")
    def edition_key(self) -> pulumi.Output[str]:
        """
        The product edition of the license key.
        """
        return pulumi.get(self, "edition_key")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of key/value pairs to be attached as labels (tags) to the license key.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> pulumi.Output[str]:
        """
        The license key to add.
        """
        return pulumi.get(self, "license_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The display name for the license.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def total(self) -> pulumi.Output[int]:
        """
        Total number of units (example: CPUs) contained in the license.
        """
        return pulumi.get(self, "total")

    @property
    @pulumi.getter
    def used(self) -> pulumi.Output[int]:
        """
        The number of units (example: CPUs) assigned to this license.
        """
        return pulumi.get(self, "used")

