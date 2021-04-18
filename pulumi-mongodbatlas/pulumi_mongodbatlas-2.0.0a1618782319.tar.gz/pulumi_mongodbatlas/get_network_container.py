# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetNetworkContainerResult',
    'AwaitableGetNetworkContainerResult',
    'get_network_container',
]

@pulumi.output_type
class GetNetworkContainerResult:
    """
    A collection of values returned by getNetworkContainer.
    """
    def __init__(__self__, atlas_cidr_block=None, azure_subscription_id=None, container_id=None, gcp_project_id=None, id=None, network_name=None, project_id=None, provider_name=None, provisioned=None, region=None, region_name=None, vnet_name=None, vpc_id=None):
        if atlas_cidr_block and not isinstance(atlas_cidr_block, str):
            raise TypeError("Expected argument 'atlas_cidr_block' to be a str")
        pulumi.set(__self__, "atlas_cidr_block", atlas_cidr_block)
        if azure_subscription_id and not isinstance(azure_subscription_id, str):
            raise TypeError("Expected argument 'azure_subscription_id' to be a str")
        pulumi.set(__self__, "azure_subscription_id", azure_subscription_id)
        if container_id and not isinstance(container_id, str):
            raise TypeError("Expected argument 'container_id' to be a str")
        pulumi.set(__self__, "container_id", container_id)
        if gcp_project_id and not isinstance(gcp_project_id, str):
            raise TypeError("Expected argument 'gcp_project_id' to be a str")
        pulumi.set(__self__, "gcp_project_id", gcp_project_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if network_name and not isinstance(network_name, str):
            raise TypeError("Expected argument 'network_name' to be a str")
        pulumi.set(__self__, "network_name", network_name)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if provider_name and not isinstance(provider_name, str):
            raise TypeError("Expected argument 'provider_name' to be a str")
        pulumi.set(__self__, "provider_name", provider_name)
        if provisioned and not isinstance(provisioned, bool):
            raise TypeError("Expected argument 'provisioned' to be a bool")
        pulumi.set(__self__, "provisioned", provisioned)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if region_name and not isinstance(region_name, str):
            raise TypeError("Expected argument 'region_name' to be a str")
        pulumi.set(__self__, "region_name", region_name)
        if vnet_name and not isinstance(vnet_name, str):
            raise TypeError("Expected argument 'vnet_name' to be a str")
        pulumi.set(__self__, "vnet_name", vnet_name)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="atlasCidrBlock")
    def atlas_cidr_block(self) -> str:
        """
        CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following [private networks](https://tools.ietf.org/html/rfc1918.html#section-3).
        """
        return pulumi.get(self, "atlas_cidr_block")

    @property
    @pulumi.getter(name="azureSubscriptionId")
    def azure_subscription_id(self) -> str:
        """
        Unique identifer of the Azure subscription in which the VNet resides.
        """
        return pulumi.get(self, "azure_subscription_id")

    @property
    @pulumi.getter(name="containerId")
    def container_id(self) -> str:
        return pulumi.get(self, "container_id")

    @property
    @pulumi.getter(name="gcpProjectId")
    def gcp_project_id(self) -> str:
        """
        Unique identifier of the GCP project in which the Network Peering connection resides.
        """
        return pulumi.get(self, "gcp_project_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="networkName")
    def network_name(self) -> str:
        """
        Name of the Network Peering connection in the Atlas project.
        """
        return pulumi.get(self, "network_name")

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
    def provisioned(self) -> bool:
        """
        Indicates whether the project has Network Peering connections deployed in the container.
        """
        return pulumi.get(self, "provisioned")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The Atlas Azure region name for where this container will exist.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="regionName")
    def region_name(self) -> str:
        """
        The Atlas AWS region name for where this container will exist.
        """
        return pulumi.get(self, "region_name")

    @property
    @pulumi.getter(name="vnetName")
    def vnet_name(self) -> str:
        """
        The name of the Azure VNet. This value is null until you provision an Azure VNet in the container.
        """
        return pulumi.get(self, "vnet_name")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> str:
        """
        Unique identifier of the project’s VPC.
        """
        return pulumi.get(self, "vpc_id")


class AwaitableGetNetworkContainerResult(GetNetworkContainerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkContainerResult(
            atlas_cidr_block=self.atlas_cidr_block,
            azure_subscription_id=self.azure_subscription_id,
            container_id=self.container_id,
            gcp_project_id=self.gcp_project_id,
            id=self.id,
            network_name=self.network_name,
            project_id=self.project_id,
            provider_name=self.provider_name,
            provisioned=self.provisioned,
            region=self.region,
            region_name=self.region_name,
            vnet_name=self.vnet_name,
            vpc_id=self.vpc_id)


def get_network_container(container_id: Optional[str] = None,
                          project_id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkContainerResult:
    """
    `NetworkContainer` describes a Network Peering Container. The resource requires your Project ID and container ID.

    > **IMPORTANT:** This resource creates one Network Peering container into which Atlas can deploy Network Peering connections. An Atlas project can have a maximum of one container for each cloud provider. You must have either the Project Owner or Organization Owner role to successfully call this endpoint.

    > **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.

    ## Example Usage


    :param str container_id: The Network Peering Container ID.
    :param str project_id: The unique ID for the project to create the database user.
    """
    __args__ = dict()
    __args__['containerId'] = container_id
    __args__['projectId'] = project_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getNetworkContainer:getNetworkContainer', __args__, opts=opts, typ=GetNetworkContainerResult).value

    return AwaitableGetNetworkContainerResult(
        atlas_cidr_block=__ret__.atlas_cidr_block,
        azure_subscription_id=__ret__.azure_subscription_id,
        container_id=__ret__.container_id,
        gcp_project_id=__ret__.gcp_project_id,
        id=__ret__.id,
        network_name=__ret__.network_name,
        project_id=__ret__.project_id,
        provider_name=__ret__.provider_name,
        provisioned=__ret__.provisioned,
        region=__ret__.region,
        region_name=__ret__.region_name,
        vnet_name=__ret__.vnet_name,
        vpc_id=__ret__.vpc_id)
