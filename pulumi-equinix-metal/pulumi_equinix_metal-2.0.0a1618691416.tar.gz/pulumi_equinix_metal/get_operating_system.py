# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetOperatingSystemResult',
    'AwaitableGetOperatingSystemResult',
    'get_operating_system',
]

@pulumi.output_type
class GetOperatingSystemResult:
    """
    A collection of values returned by getOperatingSystem.
    """
    def __init__(__self__, distro=None, id=None, name=None, provisionable_on=None, slug=None, version=None):
        if distro and not isinstance(distro, str):
            raise TypeError("Expected argument 'distro' to be a str")
        pulumi.set(__self__, "distro", distro)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisionable_on and not isinstance(provisionable_on, str):
            raise TypeError("Expected argument 'provisionable_on' to be a str")
        pulumi.set(__self__, "provisionable_on", provisionable_on)
        if slug and not isinstance(slug, str):
            raise TypeError("Expected argument 'slug' to be a str")
        pulumi.set(__self__, "slug", slug)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def distro(self) -> Optional[str]:
        return pulumi.get(self, "distro")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisionableOn")
    def provisionable_on(self) -> Optional[str]:
        return pulumi.get(self, "provisionable_on")

    @property
    @pulumi.getter
    def slug(self) -> str:
        """
        Operating system slug (same as `id`)
        """
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


class AwaitableGetOperatingSystemResult(GetOperatingSystemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOperatingSystemResult(
            distro=self.distro,
            id=self.id,
            name=self.name,
            provisionable_on=self.provisionable_on,
            slug=self.slug,
            version=self.version)


def get_operating_system(distro: Optional[str] = None,
                         name: Optional[str] = None,
                         provisionable_on: Optional[str] = None,
                         version: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOperatingSystemResult:
    """
    Use this data source to get Equinix Metal Operating System image.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_equinix_metal as equinix_metal

    example = equinix_metal.get_operating_system(name="Container Linux",
        distro="coreos",
        version="alpha",
        provisionable_on="c1.small.x86")
    server = equinix_metal.Device("server",
        hostname="tf.coreos2",
        plan="c1.small.x86",
        facilities=["ewr1"],
        operating_system=example.id,
        billing_cycle="hourly",
        project_id=local["project_id"])
    ```


    :param str distro: Name of the OS distribution.
    :param str name: Name or part of the name of the distribution. Case insensitive.
    :param str provisionable_on: Plan name.
    :param str version: Version of the distribution
    """
    __args__ = dict()
    __args__['distro'] = distro
    __args__['name'] = name
    __args__['provisionableOn'] = provisionable_on
    __args__['version'] = version
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('equinix-metal:index/getOperatingSystem:getOperatingSystem', __args__, opts=opts, typ=GetOperatingSystemResult).value

    return AwaitableGetOperatingSystemResult(
        distro=__ret__.distro,
        id=__ret__.id,
        name=__ret__.name,
        provisionable_on=__ret__.provisionable_on,
        slug=__ret__.slug,
        version=__ret__.version)
