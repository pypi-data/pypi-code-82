# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetWafGroupsResult',
    'AwaitableGetWafGroupsResult',
    'get_waf_groups',
]

@pulumi.output_type
class GetWafGroupsResult:
    """
    A collection of values returned by getWafGroups.
    """
    def __init__(__self__, filter=None, groups=None, id=None, package_id=None, zone_id=None):
        if filter and not isinstance(filter, dict):
            raise TypeError("Expected argument 'filter' to be a dict")
        pulumi.set(__self__, "filter", filter)
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if package_id and not isinstance(package_id, str):
            raise TypeError("Expected argument 'package_id' to be a str")
        pulumi.set(__self__, "package_id", package_id)
        if zone_id and not isinstance(zone_id, str):
            raise TypeError("Expected argument 'zone_id' to be a str")
        pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.GetWafGroupsFilterResult']:
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def groups(self) -> Sequence['outputs.GetWafGroupsGroupResult']:
        """
        A map of WAF Rule Groups details. Full list below:
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="packageId")
    def package_id(self) -> Optional[str]:
        """
        The ID of the WAF Rule Package that contains the WAF Rule Group
        """
        return pulumi.get(self, "package_id")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> str:
        return pulumi.get(self, "zone_id")


class AwaitableGetWafGroupsResult(GetWafGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWafGroupsResult(
            filter=self.filter,
            groups=self.groups,
            id=self.id,
            package_id=self.package_id,
            zone_id=self.zone_id)


def get_waf_groups(filter: Optional[pulumi.InputType['GetWafGroupsFilterArgs']] = None,
                   package_id: Optional[str] = None,
                   zone_id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWafGroupsResult:
    """
    Use this data source to look up [WAF Rule Groups](https://api.cloudflare.com/#waf-rule-groups-properties).


    :param pulumi.InputType['GetWafGroupsFilterArgs'] filter: One or more values used to look up WAF Rule Groups. If more than one value is given all
           values must match in order to be included, see below for full list.
    :param str package_id: The ID of the WAF Rule Package in which to search for the WAF Rule Groups.
    :param str zone_id: The ID of the DNS zone in which to search for the WAF Rule Groups.
    """
    __args__ = dict()
    __args__['filter'] = filter
    __args__['packageId'] = package_id
    __args__['zoneId'] = zone_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('cloudflare:index/getWafGroups:getWafGroups', __args__, opts=opts, typ=GetWafGroupsResult).value

    return AwaitableGetWafGroupsResult(
        filter=__ret__.filter,
        groups=__ret__.groups,
        id=__ret__.id,
        package_id=__ret__.package_id,
        zone_id=__ret__.zone_id)
