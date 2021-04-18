# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetClusterTemplateResult',
    'AwaitableGetClusterTemplateResult',
    'get_cluster_template',
]

@pulumi.output_type
class GetClusterTemplateResult:
    """
    A collection of values returned by getClusterTemplate.
    """
    def __init__(__self__, apiserver_port=None, cluster_distro=None, coe=None, created_at=None, dns_nameserver=None, docker_storage_driver=None, docker_volume_size=None, external_network_id=None, fixed_network=None, fixed_subnet=None, flavor=None, floating_ip_enabled=None, http_proxy=None, https_proxy=None, id=None, image=None, insecure_registry=None, keypair_id=None, labels=None, master_flavor=None, master_lb_enabled=None, name=None, network_driver=None, no_proxy=None, project_id=None, public=None, region=None, registry_enabled=None, server_type=None, tls_disabled=None, updated_at=None, user_id=None, volume_driver=None):
        if apiserver_port and not isinstance(apiserver_port, int):
            raise TypeError("Expected argument 'apiserver_port' to be a int")
        pulumi.set(__self__, "apiserver_port", apiserver_port)
        if cluster_distro and not isinstance(cluster_distro, str):
            raise TypeError("Expected argument 'cluster_distro' to be a str")
        pulumi.set(__self__, "cluster_distro", cluster_distro)
        if coe and not isinstance(coe, str):
            raise TypeError("Expected argument 'coe' to be a str")
        pulumi.set(__self__, "coe", coe)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if dns_nameserver and not isinstance(dns_nameserver, str):
            raise TypeError("Expected argument 'dns_nameserver' to be a str")
        pulumi.set(__self__, "dns_nameserver", dns_nameserver)
        if docker_storage_driver and not isinstance(docker_storage_driver, str):
            raise TypeError("Expected argument 'docker_storage_driver' to be a str")
        pulumi.set(__self__, "docker_storage_driver", docker_storage_driver)
        if docker_volume_size and not isinstance(docker_volume_size, int):
            raise TypeError("Expected argument 'docker_volume_size' to be a int")
        pulumi.set(__self__, "docker_volume_size", docker_volume_size)
        if external_network_id and not isinstance(external_network_id, str):
            raise TypeError("Expected argument 'external_network_id' to be a str")
        pulumi.set(__self__, "external_network_id", external_network_id)
        if fixed_network and not isinstance(fixed_network, str):
            raise TypeError("Expected argument 'fixed_network' to be a str")
        pulumi.set(__self__, "fixed_network", fixed_network)
        if fixed_subnet and not isinstance(fixed_subnet, str):
            raise TypeError("Expected argument 'fixed_subnet' to be a str")
        pulumi.set(__self__, "fixed_subnet", fixed_subnet)
        if flavor and not isinstance(flavor, str):
            raise TypeError("Expected argument 'flavor' to be a str")
        pulumi.set(__self__, "flavor", flavor)
        if floating_ip_enabled and not isinstance(floating_ip_enabled, bool):
            raise TypeError("Expected argument 'floating_ip_enabled' to be a bool")
        pulumi.set(__self__, "floating_ip_enabled", floating_ip_enabled)
        if http_proxy and not isinstance(http_proxy, str):
            raise TypeError("Expected argument 'http_proxy' to be a str")
        pulumi.set(__self__, "http_proxy", http_proxy)
        if https_proxy and not isinstance(https_proxy, str):
            raise TypeError("Expected argument 'https_proxy' to be a str")
        pulumi.set(__self__, "https_proxy", https_proxy)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image and not isinstance(image, str):
            raise TypeError("Expected argument 'image' to be a str")
        pulumi.set(__self__, "image", image)
        if insecure_registry and not isinstance(insecure_registry, str):
            raise TypeError("Expected argument 'insecure_registry' to be a str")
        pulumi.set(__self__, "insecure_registry", insecure_registry)
        if keypair_id and not isinstance(keypair_id, str):
            raise TypeError("Expected argument 'keypair_id' to be a str")
        pulumi.set(__self__, "keypair_id", keypair_id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if master_flavor and not isinstance(master_flavor, str):
            raise TypeError("Expected argument 'master_flavor' to be a str")
        pulumi.set(__self__, "master_flavor", master_flavor)
        if master_lb_enabled and not isinstance(master_lb_enabled, bool):
            raise TypeError("Expected argument 'master_lb_enabled' to be a bool")
        pulumi.set(__self__, "master_lb_enabled", master_lb_enabled)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_driver and not isinstance(network_driver, str):
            raise TypeError("Expected argument 'network_driver' to be a str")
        pulumi.set(__self__, "network_driver", network_driver)
        if no_proxy and not isinstance(no_proxy, str):
            raise TypeError("Expected argument 'no_proxy' to be a str")
        pulumi.set(__self__, "no_proxy", no_proxy)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if public and not isinstance(public, bool):
            raise TypeError("Expected argument 'public' to be a bool")
        pulumi.set(__self__, "public", public)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if registry_enabled and not isinstance(registry_enabled, bool):
            raise TypeError("Expected argument 'registry_enabled' to be a bool")
        pulumi.set(__self__, "registry_enabled", registry_enabled)
        if server_type and not isinstance(server_type, str):
            raise TypeError("Expected argument 'server_type' to be a str")
        pulumi.set(__self__, "server_type", server_type)
        if tls_disabled and not isinstance(tls_disabled, bool):
            raise TypeError("Expected argument 'tls_disabled' to be a bool")
        pulumi.set(__self__, "tls_disabled", tls_disabled)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)
        if volume_driver and not isinstance(volume_driver, str):
            raise TypeError("Expected argument 'volume_driver' to be a str")
        pulumi.set(__self__, "volume_driver", volume_driver)

    @property
    @pulumi.getter(name="apiserverPort")
    def apiserver_port(self) -> int:
        """
        The API server port for the Container Orchestration
        Engine for this cluster template.
        """
        return pulumi.get(self, "apiserver_port")

    @property
    @pulumi.getter(name="clusterDistro")
    def cluster_distro(self) -> str:
        """
        The distro for the cluster (fedora-atomic, coreos, etc.).
        """
        return pulumi.get(self, "cluster_distro")

    @property
    @pulumi.getter
    def coe(self) -> str:
        """
        The Container Orchestration Engine for this cluster template.
        """
        return pulumi.get(self, "coe")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time at which cluster template was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="dnsNameserver")
    def dns_nameserver(self) -> str:
        """
        Address of the DNS nameserver that is used in nodes of the
        cluster.
        """
        return pulumi.get(self, "dns_nameserver")

    @property
    @pulumi.getter(name="dockerStorageDriver")
    def docker_storage_driver(self) -> str:
        """
        Docker storage driver. Changing this updates the
        Docker storage driver of the existing cluster template.
        """
        return pulumi.get(self, "docker_storage_driver")

    @property
    @pulumi.getter(name="dockerVolumeSize")
    def docker_volume_size(self) -> int:
        """
        The size (in GB) of the Docker volume.
        """
        return pulumi.get(self, "docker_volume_size")

    @property
    @pulumi.getter(name="externalNetworkId")
    def external_network_id(self) -> str:
        """
        The ID of the external network that will be used for
        the cluster.
        """
        return pulumi.get(self, "external_network_id")

    @property
    @pulumi.getter(name="fixedNetwork")
    def fixed_network(self) -> str:
        """
        The fixed network that will be attached to the cluster.
        """
        return pulumi.get(self, "fixed_network")

    @property
    @pulumi.getter(name="fixedSubnet")
    def fixed_subnet(self) -> str:
        """
        =The fixed subnet that will be attached to the cluster.
        """
        return pulumi.get(self, "fixed_subnet")

    @property
    @pulumi.getter
    def flavor(self) -> str:
        """
        The flavor for the nodes of the cluster.
        """
        return pulumi.get(self, "flavor")

    @property
    @pulumi.getter(name="floatingIpEnabled")
    def floating_ip_enabled(self) -> bool:
        """
        Indicates whether created cluster should create IP
        floating IP for every node or not.
        """
        return pulumi.get(self, "floating_ip_enabled")

    @property
    @pulumi.getter(name="httpProxy")
    def http_proxy(self) -> str:
        """
        The address of a proxy for receiving all HTTP requests and
        relay them.
        """
        return pulumi.get(self, "http_proxy")

    @property
    @pulumi.getter(name="httpsProxy")
    def https_proxy(self) -> str:
        """
        The address of a proxy for receiving all HTTPS requests and
        relay them.
        """
        return pulumi.get(self, "https_proxy")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def image(self) -> str:
        """
        The reference to an image that is used for nodes of the cluster.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter(name="insecureRegistry")
    def insecure_registry(self) -> str:
        """
        The insecure registry URL for the cluster template.
        """
        return pulumi.get(self, "insecure_registry")

    @property
    @pulumi.getter(name="keypairId")
    def keypair_id(self) -> str:
        """
        The name of the Compute service SSH keypair.
        """
        return pulumi.get(self, "keypair_id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, Any]:
        """
        The list of key value pairs representing additional properties
        of the cluster template.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="masterFlavor")
    def master_flavor(self) -> str:
        """
        The flavor for the master nodes.
        """
        return pulumi.get(self, "master_flavor")

    @property
    @pulumi.getter(name="masterLbEnabled")
    def master_lb_enabled(self) -> bool:
        """
        Indicates whether created cluster should has a
        loadbalancer for master nodes or not.
        """
        return pulumi.get(self, "master_lb_enabled")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkDriver")
    def network_driver(self) -> str:
        """
        The name of the driver for the container network.
        """
        return pulumi.get(self, "network_driver")

    @property
    @pulumi.getter(name="noProxy")
    def no_proxy(self) -> str:
        """
        A comma-separated list of IP addresses that shouldn't be used in
        the cluster.
        """
        return pulumi.get(self, "no_proxy")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The project of the cluster template.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def public(self) -> bool:
        """
        Indicates whether cluster template should be public.
        """
        return pulumi.get(self, "public")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        See Argument Reference above.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="registryEnabled")
    def registry_enabled(self) -> bool:
        """
        Indicates whether Docker registry is enabled in the
        cluster.
        """
        return pulumi.get(self, "registry_enabled")

    @property
    @pulumi.getter(name="serverType")
    def server_type(self) -> str:
        """
        The server type for the cluster template.
        """
        return pulumi.get(self, "server_type")

    @property
    @pulumi.getter(name="tlsDisabled")
    def tls_disabled(self) -> bool:
        """
        Indicates whether the TLS should be disabled in the cluster.
        """
        return pulumi.get(self, "tls_disabled")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The time at which cluster template was updated.
        """
        return pulumi.get(self, "updated_at")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        The user of the cluster template.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter(name="volumeDriver")
    def volume_driver(self) -> str:
        """
        The name of the driver that is used for the volumes of the
        cluster nodes.
        """
        return pulumi.get(self, "volume_driver")


class AwaitableGetClusterTemplateResult(GetClusterTemplateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterTemplateResult(
            apiserver_port=self.apiserver_port,
            cluster_distro=self.cluster_distro,
            coe=self.coe,
            created_at=self.created_at,
            dns_nameserver=self.dns_nameserver,
            docker_storage_driver=self.docker_storage_driver,
            docker_volume_size=self.docker_volume_size,
            external_network_id=self.external_network_id,
            fixed_network=self.fixed_network,
            fixed_subnet=self.fixed_subnet,
            flavor=self.flavor,
            floating_ip_enabled=self.floating_ip_enabled,
            http_proxy=self.http_proxy,
            https_proxy=self.https_proxy,
            id=self.id,
            image=self.image,
            insecure_registry=self.insecure_registry,
            keypair_id=self.keypair_id,
            labels=self.labels,
            master_flavor=self.master_flavor,
            master_lb_enabled=self.master_lb_enabled,
            name=self.name,
            network_driver=self.network_driver,
            no_proxy=self.no_proxy,
            project_id=self.project_id,
            public=self.public,
            region=self.region,
            registry_enabled=self.registry_enabled,
            server_type=self.server_type,
            tls_disabled=self.tls_disabled,
            updated_at=self.updated_at,
            user_id=self.user_id,
            volume_driver=self.volume_driver)


def get_cluster_template(name: Optional[str] = None,
                         region: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterTemplateResult:
    """
    Use this data source to get the ID of an available OpenStack Magnum cluster
    template.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openstack as openstack

    clustertemplate1 = openstack.containerinfra.get_cluster_template(name="clustertemplate_1")
    ```


    :param str name: The name of the cluster template.
    :param str region: The region in which to obtain the V1 Container Infra
           client.
           If omitted, the `region` argument of the provider is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:containerinfra/getClusterTemplate:getClusterTemplate', __args__, opts=opts, typ=GetClusterTemplateResult).value

    return AwaitableGetClusterTemplateResult(
        apiserver_port=__ret__.apiserver_port,
        cluster_distro=__ret__.cluster_distro,
        coe=__ret__.coe,
        created_at=__ret__.created_at,
        dns_nameserver=__ret__.dns_nameserver,
        docker_storage_driver=__ret__.docker_storage_driver,
        docker_volume_size=__ret__.docker_volume_size,
        external_network_id=__ret__.external_network_id,
        fixed_network=__ret__.fixed_network,
        fixed_subnet=__ret__.fixed_subnet,
        flavor=__ret__.flavor,
        floating_ip_enabled=__ret__.floating_ip_enabled,
        http_proxy=__ret__.http_proxy,
        https_proxy=__ret__.https_proxy,
        id=__ret__.id,
        image=__ret__.image,
        insecure_registry=__ret__.insecure_registry,
        keypair_id=__ret__.keypair_id,
        labels=__ret__.labels,
        master_flavor=__ret__.master_flavor,
        master_lb_enabled=__ret__.master_lb_enabled,
        name=__ret__.name,
        network_driver=__ret__.network_driver,
        no_proxy=__ret__.no_proxy,
        project_id=__ret__.project_id,
        public=__ret__.public,
        region=__ret__.region,
        registry_enabled=__ret__.registry_enabled,
        server_type=__ret__.server_type,
        tls_disabled=__ret__.tls_disabled,
        updated_at=__ret__.updated_at,
        user_id=__ret__.user_id,
        volume_driver=__ret__.volume_driver)
