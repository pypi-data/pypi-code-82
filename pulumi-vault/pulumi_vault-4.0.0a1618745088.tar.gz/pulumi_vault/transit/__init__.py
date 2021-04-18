# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .get_decrypt import *
from .get_encrypt import *
from .secret_backend_key import *
from .secret_cache_config import *

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "vault:transit/secretBackendKey:SecretBackendKey":
                return SecretBackendKey(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "vault:transit/secretCacheConfig:SecretCacheConfig":
                return SecretCacheConfig(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("vault", "transit/secretBackendKey", _module_instance)
    pulumi.runtime.register_resource_module("vault", "transit/secretCacheConfig", _module_instance)

_register_module()
