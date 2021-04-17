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
    'GetElasticSearchAclResult',
    'AwaitableGetElasticSearchAclResult',
    'get_elastic_search_acl',
]

@pulumi.output_type
class GetElasticSearchAclResult:
    """
    A collection of values returned by getElasticSearchAcl.
    """
    def __init__(__self__, acls=None, enabled=None, extended_acl=None, id=None, project=None, service_name=None):
        if acls and not isinstance(acls, list):
            raise TypeError("Expected argument 'acls' to be a list")
        pulumi.set(__self__, "acls", acls)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if extended_acl and not isinstance(extended_acl, bool):
            raise TypeError("Expected argument 'extended_acl' to be a bool")
        pulumi.set(__self__, "extended_acl", extended_acl)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if project and not isinstance(project, str):
            raise TypeError("Expected argument 'project' to be a str")
        pulumi.set(__self__, "project", project)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter
    def acls(self) -> Optional[Sequence['outputs.GetElasticSearchAclAclResult']]:
        return pulumi.get(self, "acls")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        enables or disables Elasticsearch ACLs.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="extendedAcl")
    def extended_acl(self) -> Optional[bool]:
        """
        Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs 
        (and only those) by enabling the ExtendedAcl option for the service. When it is enabled, users can use
        these APIs as long as all operations only target indexes they have been granted access to.
        """
        return pulumi.get(self, "extended_acl")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def project(self) -> str:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        return pulumi.get(self, "service_name")


class AwaitableGetElasticSearchAclResult(GetElasticSearchAclResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetElasticSearchAclResult(
            acls=self.acls,
            enabled=self.enabled,
            extended_acl=self.extended_acl,
            id=self.id,
            project=self.project,
            service_name=self.service_name)


def get_elastic_search_acl(acls: Optional[Sequence[pulumi.InputType['GetElasticSearchAclAclArgs']]] = None,
                           enabled: Optional[bool] = None,
                           extended_acl: Optional[bool] = None,
                           project: Optional[str] = None,
                           service_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetElasticSearchAclResult:
    """
    ## # Elasticsearch ACL Data Source

    The Elasticsearch ACL data source provides information about the existing Aiven Elasticsearch ACL
    for Elasticsearch service.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aiven as aiven

    es_acls = aiven.get_elastic_search_acl(project=aiven_project["es-project"]["project"],
        service_name=aiven_service["es"]["service_name"])
    ```


    :param bool enabled: enables or disables Elasticsearch ACLs.
    :param bool extended_acl: Index rules can be applied in a limited fashion to the _mget, _msearch and _bulk APIs 
           (and only those) by enabling the ExtendedAcl option for the service. When it is enabled, users can use
           these APIs as long as all operations only target indexes they have been granted access to.
    :param str project: and `service_name` - (Required) define the project and service the ACL belongs to. 
           They should be defined using reference as shown above to set up dependencies correctly.
    """
    __args__ = dict()
    __args__['acls'] = acls
    __args__['enabled'] = enabled
    __args__['extendedAcl'] = extended_acl
    __args__['project'] = project
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aiven:index/getElasticSearchAcl:getElasticSearchAcl', __args__, opts=opts, typ=GetElasticSearchAclResult).value

    return AwaitableGetElasticSearchAclResult(
        acls=__ret__.acls,
        enabled=__ret__.enabled,
        extended_acl=__ret__.extended_acl,
        id=__ret__.id,
        project=__ret__.project,
        service_name=__ret__.service_name)
