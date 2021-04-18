# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .aggregate_v2 import *
from .flavor import *
from .flavor_access import *
from .floating_ip import *
from .floating_ip_associate import *
from .get_aggregate_v2 import *
from .get_availability_zones import *
from .get_flavor import *
from .get_hypervisor_v2 import *
from .get_instance_v2 import *
from .get_keypair import *
from .instance import *
from .interface_attach import *
from .keypair import *
from .quota_set_v2 import *
from .sec_group import *
from .server_group import *
from .volume_attach import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "openstack:compute/aggregateV2:AggregateV2":
                return AggregateV2(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/flavor:Flavor":
                return Flavor(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/flavorAccess:FlavorAccess":
                return FlavorAccess(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/floatingIp:FloatingIp":
                return FloatingIp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/floatingIpAssociate:FloatingIpAssociate":
                return FloatingIpAssociate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/instance:Instance":
                return Instance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/interfaceAttach:InterfaceAttach":
                return InterfaceAttach(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/keypair:Keypair":
                return Keypair(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/quotaSetV2:QuotaSetV2":
                return QuotaSetV2(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/secGroup:SecGroup":
                return SecGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/serverGroup:ServerGroup":
                return ServerGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:compute/volumeAttach:VolumeAttach":
                return VolumeAttach(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("openstack", "compute/aggregateV2", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/flavor", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/flavorAccess", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/floatingIp", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/floatingIpAssociate", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/instance", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/interfaceAttach", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/keypair", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/quotaSetV2", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/secGroup", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/serverGroup", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "compute/volumeAttach", _module_instance)

_register_module()
