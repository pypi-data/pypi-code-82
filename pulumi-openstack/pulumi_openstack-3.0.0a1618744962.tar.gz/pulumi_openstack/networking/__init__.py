# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .address_scope import *
from .floating_ip import *
from .floating_ip_associate import *
from .get_address_scope import *
from .get_floating_ip import *
from .get_network import *
from .get_port import *
from .get_port_ids import *
from .get_qos_bandwidth_limit_rule import *
from .get_qos_dscp_marking_rule import *
from .get_qos_minimum_bandwidth_rule import *
from .get_qos_policy import *
from .get_router import *
from .get_sec_group import *
from .get_subnet import *
from .get_subnet_ids_v2 import *
from .get_subnet_pool import *
from .get_trunk import *
from .network import *
from .port import *
from .port_forwarding_v2 import *
from .port_sec_group_associate import *
from .qos_bandwidth_limit_rule import *
from .qos_dscp_marking_rule import *
from .qos_minimum_bandwidth_rule import *
from .qos_policy import *
from .quota_v2 import *
from .rbac_policy_v2 import *
from .router import *
from .router_interface import *
from .router_route import *
from .sec_group import *
from .sec_group_rule import *
from .subnet import *
from .subnet_pool import *
from .subnet_route import *
from .trunk import *
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
            if typ == "openstack:networking/addressScope:AddressScope":
                return AddressScope(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/floatingIp:FloatingIp":
                return FloatingIp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/floatingIpAssociate:FloatingIpAssociate":
                return FloatingIpAssociate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/network:Network":
                return Network(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/port:Port":
                return Port(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/portForwardingV2:PortForwardingV2":
                return PortForwardingV2(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/portSecGroupAssociate:PortSecGroupAssociate":
                return PortSecGroupAssociate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/qosBandwidthLimitRule:QosBandwidthLimitRule":
                return QosBandwidthLimitRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/qosDscpMarkingRule:QosDscpMarkingRule":
                return QosDscpMarkingRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/qosMinimumBandwidthRule:QosMinimumBandwidthRule":
                return QosMinimumBandwidthRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/qosPolicy:QosPolicy":
                return QosPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/quotaV2:QuotaV2":
                return QuotaV2(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/rbacPolicyV2:RbacPolicyV2":
                return RbacPolicyV2(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/router:Router":
                return Router(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/routerInterface:RouterInterface":
                return RouterInterface(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/routerRoute:RouterRoute":
                return RouterRoute(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/secGroup:SecGroup":
                return SecGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/secGroupRule:SecGroupRule":
                return SecGroupRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/subnet:Subnet":
                return Subnet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/subnetPool:SubnetPool":
                return SubnetPool(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/subnetRoute:SubnetRoute":
                return SubnetRoute(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:networking/trunk:Trunk":
                return Trunk(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("openstack", "networking/addressScope", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/floatingIp", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/floatingIpAssociate", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/network", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/port", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/portForwardingV2", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/portSecGroupAssociate", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/qosBandwidthLimitRule", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/qosDscpMarkingRule", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/qosMinimumBandwidthRule", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/qosPolicy", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/quotaV2", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/rbacPolicyV2", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/router", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/routerInterface", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/routerRoute", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/secGroup", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/secGroupRule", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/subnet", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/subnetPool", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/subnetRoute", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "networking/trunk", _module_instance)

_register_module()
