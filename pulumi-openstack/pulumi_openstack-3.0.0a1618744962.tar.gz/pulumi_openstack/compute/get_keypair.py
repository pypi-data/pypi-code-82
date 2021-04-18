# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetKeypairResult',
    'AwaitableGetKeypairResult',
    'get_keypair',
]

@pulumi.output_type
class GetKeypairResult:
    """
    A collection of values returned by getKeypair.
    """
    def __init__(__self__, fingerprint=None, id=None, name=None, public_key=None, region=None):
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        """
        The fingerprint of the OpenSSH key.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        """
        The OpenSSH-formatted public key of the keypair.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "region")


class AwaitableGetKeypairResult(GetKeypairResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeypairResult(
            fingerprint=self.fingerprint,
            id=self.id,
            name=self.name,
            public_key=self.public_key,
            region=self.region)


def get_keypair(name: Optional[str] = None,
                region: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeypairResult:
    """
    Use this data source to get the ID and public key of an OpenStack keypair.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openstack as openstack

    kp = openstack.compute.get_keypair(name="sand")
    ```


    :param str name: The unique name of the keypair.
    :param str region: The region in which to obtain the V2 Compute client.
           If omitted, the `region` argument of the provider is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:compute/getKeypair:getKeypair', __args__, opts=opts, typ=GetKeypairResult).value

    return AwaitableGetKeypairResult(
        fingerprint=__ret__.fingerprint,
        id=__ret__.id,
        name=__ret__.name,
        public_key=__ret__.public_key,
        region=__ret__.region)
