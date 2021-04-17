# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetSecretV2Result',
    'AwaitableGetSecretV2Result',
    'get_secret_v2',
]

@pulumi.output_type
class GetSecretV2Result:
    """
    A collection of values returned by getSecretV2.
    """
    def __init__(__self__, annotations=None, cluster_id=None, data=None, id=None, immutable=None, labels=None, name=None, namespace=None, resource_version=None, type=None):
        if annotations and not isinstance(annotations, dict):
            raise TypeError("Expected argument 'annotations' to be a dict")
        pulumi.set(__self__, "annotations", annotations)
        if cluster_id and not isinstance(cluster_id, str):
            raise TypeError("Expected argument 'cluster_id' to be a str")
        pulumi.set(__self__, "cluster_id", cluster_id)
        if data and not isinstance(data, dict):
            raise TypeError("Expected argument 'data' to be a dict")
        pulumi.set(__self__, "data", data)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if immutable and not isinstance(immutable, bool):
            raise TypeError("Expected argument 'immutable' to be a bool")
        pulumi.set(__self__, "immutable", immutable)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if resource_version and not isinstance(resource_version, str):
            raise TypeError("Expected argument 'resource_version' to be a str")
        pulumi.set(__self__, "resource_version", resource_version)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def annotations(self) -> Mapping[str, Any]:
        """
        (Computed) Annotations for the secret v2 (map)
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> str:
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter
    def data(self) -> Mapping[str, Any]:
        """
        (Computed/Sensitive) The data of the secret v2 (map)
        """
        return pulumi.get(self, "data")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def immutable(self) -> bool:
        """
        (Computed) If set to true, any secret update will remove and recreate the secret. This is a beta field enabled by k8s `ImmutableEphemeralVolumes` feature gate (bool)
        """
        return pulumi.get(self, "immutable")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, Any]:
        """
        (Computed) Labels for the secret v2 (map)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="resourceVersion")
    def resource_version(self) -> str:
        """
        (Computed) The k8s resource version (string)
        """
        return pulumi.get(self, "resource_version")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        (Computed) The type of the k8s secret, used to facilitate programmatic handling of secret data, [More info](https://github.com/kubernetes/api/blob/release-1.20/core/v1/types.go#L5772) about k8s secret types and expected format (string)
        """
        return pulumi.get(self, "type")


class AwaitableGetSecretV2Result(GetSecretV2Result):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretV2Result(
            annotations=self.annotations,
            cluster_id=self.cluster_id,
            data=self.data,
            id=self.id,
            immutable=self.immutable,
            labels=self.labels,
            name=self.name,
            namespace=self.namespace,
            resource_version=self.resource_version,
            type=self.type)


def get_secret_v2(cluster_id: Optional[str] = None,
                  name: Optional[str] = None,
                  namespace: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretV2Result:
    """
    Use this data source to retrieve information about a Rancher2 secret v2.


    :param str cluster_id: The cluster id of the secret V2 (string)
    :param str name: The name of the secret v2 (string)
    :param str namespace: The namespaces of the secret v2. Default: `default` (string)
    """
    __args__ = dict()
    __args__['clusterId'] = cluster_id
    __args__['name'] = name
    __args__['namespace'] = namespace
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('rancher2:index/getSecretV2:getSecretV2', __args__, opts=opts, typ=GetSecretV2Result).value

    return AwaitableGetSecretV2Result(
        annotations=__ret__.annotations,
        cluster_id=__ret__.cluster_id,
        data=__ret__.data,
        id=__ret__.id,
        immutable=__ret__.immutable,
        labels=__ret__.labels,
        name=__ret__.name,
        namespace=__ret__.namespace,
        resource_version=__ret__.resource_version,
        type=__ret__.type)
