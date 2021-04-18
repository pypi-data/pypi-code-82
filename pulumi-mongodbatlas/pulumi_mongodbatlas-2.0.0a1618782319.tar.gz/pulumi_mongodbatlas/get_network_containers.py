# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetNetworkContainersResult',
    'AwaitableGetNetworkContainersResult',
    'get_network_containers',
]

@pulumi.output_type
class GetNetworkContainersResult:
    """
    A collection of values returned by getNetworkContainers.
    """
    def __init__(__self__, id=None, project_id=None, provider_name=None, results=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if provider_name and not isinstance(provider_name, str):
            raise TypeError("Expected argument 'provider_name' to be a str")
        pulumi.set(__self__, "provider_name", provider_name)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> str:
        """
        Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.
        """
        return pulumi.get(self, "provider_name")

    @property
    @pulumi.getter
    def results(self) -> Sequence['outputs.GetNetworkContainersResultResult']:
        """
        A list where each represents a Network Peering Container.
        """
        return pulumi.get(self, "results")


class AwaitableGetNetworkContainersResult(GetNetworkContainersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkContainersResult(
            id=self.id,
            project_id=self.project_id,
            provider_name=self.provider_name,
            results=self.results)


def get_network_containers(project_id: Optional[str] = None,
                           provider_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkContainersResult:
    """
    `getNetworkContainers` describes all Network Peering Containers. The data source requires your Project ID.

    > **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.

    ## Example Usage
    ### Basic Example.

    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    test_network_container = mongodbatlas.NetworkContainer("testNetworkContainer",
        project_id="<YOUR-PROJECT-ID>",
        atlas_cidr_block="10.8.0.0/21",
        provider_name="AWS",
        region_name="US_EAST_1")
    test_network_containers = pulumi.Output.all(test_network_container.project_id, test_network_container.provider_name).apply(lambda project_id, provider_name: mongodbatlas.get_network_containers(project_id=project_id,
        provider_name=provider_name))
    ```


    :param str project_id: The unique ID for the project to create the database user.
    :param str provider_name: Cloud provider for this Network peering container. Accepted values are AWS, GCP, and Azure.
    """
    __args__ = dict()
    __args__['projectId'] = project_id
    __args__['providerName'] = provider_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getNetworkContainers:getNetworkContainers', __args__, opts=opts, typ=GetNetworkContainersResult).value

    return AwaitableGetNetworkContainersResult(
        id=__ret__.id,
        project_id=__ret__.project_id,
        provider_name=__ret__.provider_name,
        results=__ret__.results)
