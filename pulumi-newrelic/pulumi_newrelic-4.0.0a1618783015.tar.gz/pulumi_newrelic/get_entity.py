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
    'GetEntityResult',
    'AwaitableGetEntityResult',
    'get_entity',
]

@pulumi.output_type
class GetEntityResult:
    """
    A collection of values returned by getEntity.
    """
    def __init__(__self__, account_id=None, application_id=None, domain=None, guid=None, id=None, ignore_case=None, name=None, serving_apm_application_id=None, tag=None, type=None):
        if account_id and not isinstance(account_id, int):
            raise TypeError("Expected argument 'account_id' to be a int")
        pulumi.set(__self__, "account_id", account_id)
        if application_id and not isinstance(application_id, int):
            raise TypeError("Expected argument 'application_id' to be a int")
        pulumi.set(__self__, "application_id", application_id)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if guid and not isinstance(guid, str):
            raise TypeError("Expected argument 'guid' to be a str")
        pulumi.set(__self__, "guid", guid)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ignore_case and not isinstance(ignore_case, bool):
            raise TypeError("Expected argument 'ignore_case' to be a bool")
        pulumi.set(__self__, "ignore_case", ignore_case)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if serving_apm_application_id and not isinstance(serving_apm_application_id, int):
            raise TypeError("Expected argument 'serving_apm_application_id' to be a int")
        pulumi.set(__self__, "serving_apm_application_id", serving_apm_application_id)
        if tag and not isinstance(tag, dict):
            raise TypeError("Expected argument 'tag' to be a dict")
        pulumi.set(__self__, "tag", tag)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> int:
        """
        The New Relic account ID associated with this entity.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> int:
        """
        The domain-specific application ID of the entity. Only returned for APM and Browser applications.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter
    def domain(self) -> str:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def guid(self) -> str:
        """
        The unique GUID of the entity.
        """
        return pulumi.get(self, "guid")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ignoreCase")
    def ignore_case(self) -> Optional[bool]:
        return pulumi.get(self, "ignore_case")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="servingApmApplicationId")
    def serving_apm_application_id(self) -> int:
        return pulumi.get(self, "serving_apm_application_id")

    @property
    @pulumi.getter
    def tag(self) -> Optional['outputs.GetEntityTagResult']:
        return pulumi.get(self, "tag")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


class AwaitableGetEntityResult(GetEntityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEntityResult(
            account_id=self.account_id,
            application_id=self.application_id,
            domain=self.domain,
            guid=self.guid,
            id=self.id,
            ignore_case=self.ignore_case,
            name=self.name,
            serving_apm_application_id=self.serving_apm_application_id,
            tag=self.tag,
            type=self.type)


def get_entity(domain: Optional[str] = None,
               ignore_case: Optional[bool] = None,
               name: Optional[str] = None,
               tag: Optional[pulumi.InputType['GetEntityTagArgs']] = None,
               type: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEntityResult:
    """
    Use this data source to get information about a specific entity in New Relic One that already exists.


    :param str domain: The entity's domain. Valid values are APM, BROWSER, INFRA, MOBILE, SYNTH, and VIZ. If not specified, all domains are searched.
    :param bool ignore_case: Ignore case of the `name` when searching for the entity. Defaults to false.
    :param str name: The name of the entity in New Relic One.  The first entity matching this name for the given search parameters will be returned.
    :param str type: The entity's type. Valid values are APPLICATION, DASHBOARD, HOST, MONITOR, and WORKLOAD.
    """
    __args__ = dict()
    __args__['domain'] = domain
    __args__['ignoreCase'] = ignore_case
    __args__['name'] = name
    __args__['tag'] = tag
    __args__['type'] = type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('newrelic:index/getEntity:getEntity', __args__, opts=opts, typ=GetEntityResult).value

    return AwaitableGetEntityResult(
        account_id=__ret__.account_id,
        application_id=__ret__.application_id,
        domain=__ret__.domain,
        guid=__ret__.guid,
        id=__ret__.id,
        ignore_case=__ret__.ignore_case,
        name=__ret__.name,
        serving_apm_application_id=__ret__.serving_apm_application_id,
        tag=__ret__.tag,
        type=__ret__.type)
