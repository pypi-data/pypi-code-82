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
    'GetCatalogNodesResult',
    'AwaitableGetCatalogNodesResult',
    'get_catalog_nodes',
]

@pulumi.output_type
class GetCatalogNodesResult:
    """
    A collection of values returned by getCatalogNodes.
    """
    def __init__(__self__, datacenter=None, id=None, node_ids=None, node_names=None, nodes=None, query_options=None):
        if datacenter and not isinstance(datacenter, str):
            raise TypeError("Expected argument 'datacenter' to be a str")
        pulumi.set(__self__, "datacenter", datacenter)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if node_ids and not isinstance(node_ids, list):
            raise TypeError("Expected argument 'node_ids' to be a list")
        pulumi.set(__self__, "node_ids", node_ids)
        if node_names and not isinstance(node_names, list):
            raise TypeError("Expected argument 'node_names' to be a list")
        pulumi.set(__self__, "node_names", node_names)
        if nodes and not isinstance(nodes, list):
            raise TypeError("Expected argument 'nodes' to be a list")
        pulumi.set(__self__, "nodes", nodes)
        if query_options and not isinstance(query_options, list):
            raise TypeError("Expected argument 'query_options' to be a list")
        pulumi.set(__self__, "query_options", query_options)

    @property
    @pulumi.getter
    def datacenter(self) -> str:
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="nodeIds")
    def node_ids(self) -> Sequence[str]:
        return pulumi.get(self, "node_ids")

    @property
    @pulumi.getter(name="nodeNames")
    def node_names(self) -> Sequence[str]:
        return pulumi.get(self, "node_names")

    @property
    @pulumi.getter
    def nodes(self) -> Sequence['outputs.GetCatalogNodesNodeResult']:
        return pulumi.get(self, "nodes")

    @property
    @pulumi.getter(name="queryOptions")
    def query_options(self) -> Optional[Sequence['outputs.GetCatalogNodesQueryOptionResult']]:
        return pulumi.get(self, "query_options")


class AwaitableGetCatalogNodesResult(GetCatalogNodesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCatalogNodesResult(
            datacenter=self.datacenter,
            id=self.id,
            node_ids=self.node_ids,
            node_names=self.node_names,
            nodes=self.nodes,
            query_options=self.query_options)


def get_catalog_nodes(query_options: Optional[Sequence[pulumi.InputType['GetCatalogNodesQueryOptionArgs']]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCatalogNodesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['queryOptions'] = query_options
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('consul:index/getCatalogNodes:getCatalogNodes', __args__, opts=opts, typ=GetCatalogNodesResult).value

    return AwaitableGetCatalogNodesResult(
        datacenter=__ret__.datacenter,
        id=__ret__.id,
        node_ids=__ret__.node_ids,
        node_names=__ret__.node_names,
        nodes=__ret__.nodes,
        query_options=__ret__.query_options)
