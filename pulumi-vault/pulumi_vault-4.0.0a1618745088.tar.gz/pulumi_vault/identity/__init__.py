# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .entity import *
from .entity_alias import *
from .entity_policies import *
from .get_entity import *
from .get_group import *
from .group import *
from .group_alias import *
from .group_member_entity_ids import *
from .group_policies import *
from .oidc import *
from .oidc_key import *
from .oidc_key_allowed_client_id import *
from .oidc_role import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "vault:identity/entity:Entity":
                return Entity(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/entityAlias:EntityAlias":
                return EntityAlias(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/entityPolicies:EntityPolicies":
                return EntityPolicies(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/group:Group":
                return Group(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/groupAlias:GroupAlias":
                return GroupAlias(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/groupMemberEntityIds:GroupMemberEntityIds":
                return GroupMemberEntityIds(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/groupPolicies:GroupPolicies":
                return GroupPolicies(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/oidc:Oidc":
                return Oidc(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/oidcKey:OidcKey":
                return OidcKey(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/oidcKeyAllowedClientID:OidcKeyAllowedClientID":
                return OidcKeyAllowedClientID(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:identity/oidcRole:OidcRole":
                return OidcRole(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("vault", "identity/entity", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/entityAlias", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/entityPolicies", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/group", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/groupAlias", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/groupMemberEntityIds", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/groupPolicies", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/oidc", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/oidcKey", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/oidcKeyAllowedClientID", _module_instance)
    pulumi.runtime.register_resource_module("vault", "identity/oidcRole", _module_instance)

_register_module()
