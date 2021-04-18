# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .big_ip_license import *
from .dns import *
from .i_app import *
from .ntp import *
from .provision import *
from .snmp import *
from .snmp_traps import *
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
            if typ == "f5bigip:sys/bigIpLicense:BigIpLicense":
                return BigIpLicense(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "f5bigip:sys/dns:Dns":
                return Dns(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "f5bigip:sys/iApp:IApp":
                return IApp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "f5bigip:sys/ntp:Ntp":
                return Ntp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "f5bigip:sys/provision:Provision":
                return Provision(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "f5bigip:sys/snmp:Snmp":
                return Snmp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "f5bigip:sys/snmpTraps:SnmpTraps":
                return SnmpTraps(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("f5bigip", "sys/bigIpLicense", _module_instance)
    pulumi.runtime.register_resource_module("f5bigip", "sys/dns", _module_instance)
    pulumi.runtime.register_resource_module("f5bigip", "sys/iApp", _module_instance)
    pulumi.runtime.register_resource_module("f5bigip", "sys/ntp", _module_instance)
    pulumi.runtime.register_resource_module("f5bigip", "sys/provision", _module_instance)
    pulumi.runtime.register_resource_module("f5bigip", "sys/snmp", _module_instance)
    pulumi.runtime.register_resource_module("f5bigip", "sys/snmpTraps", _module_instance)

_register_module()
