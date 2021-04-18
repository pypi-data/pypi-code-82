# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .get_server import *
from .get_server_policy import *
from .get_server_scopes import *
from .server import *
from .server_claim import *
from .server_policy import *
from .server_policy_claim import *
from .server_policy_rule import *
from .server_scope import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "okta:auth/server:Server":
                return Server(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "okta:auth/serverClaim:ServerClaim":
                return ServerClaim(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "okta:auth/serverPolicy:ServerPolicy":
                return ServerPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "okta:auth/serverPolicyClaim:ServerPolicyClaim":
                return ServerPolicyClaim(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "okta:auth/serverPolicyRule:ServerPolicyRule":
                return ServerPolicyRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "okta:auth/serverScope:ServerScope":
                return ServerScope(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("okta", "auth/server", _module_instance)
    pulumi.runtime.register_resource_module("okta", "auth/serverClaim", _module_instance)
    pulumi.runtime.register_resource_module("okta", "auth/serverPolicy", _module_instance)
    pulumi.runtime.register_resource_module("okta", "auth/serverPolicyClaim", _module_instance)
    pulumi.runtime.register_resource_module("okta", "auth/serverPolicyRule", _module_instance)
    pulumi.runtime.register_resource_module("okta", "auth/serverScope", _module_instance)

_register_module()
