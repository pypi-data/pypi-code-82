# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .configuration import *
from .database import *
from .instance import *
from .user import *
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
            if typ == "openstack:database/configuration:Configuration":
                return Configuration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:database/database:Database":
                return Database(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:database/instance:Instance":
                return Instance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "openstack:database/user:User":
                return User(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("openstack", "database/configuration", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "database/database", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "database/instance", _module_instance)
    pulumi.runtime.register_resource_module("openstack", "database/user", _module_instance)

_register_module()
