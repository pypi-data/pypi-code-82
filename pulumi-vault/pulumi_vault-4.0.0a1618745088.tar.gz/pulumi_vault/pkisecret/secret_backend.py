# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SecretBackendArgs', 'SecretBackend']

@pulumi.input_type
class SecretBackendArgs:
    def __init__(__self__, *,
                 path: pulumi.Input[str],
                 default_lease_ttl_seconds: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_lease_ttl_seconds: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a SecretBackend resource.
        :param pulumi.Input[str] path: The unique path this backend should be mounted at. Must not begin or end with a `/`.
        :param pulumi.Input[int] default_lease_ttl_seconds: The default TTL for credentials issued by this backend.
        :param pulumi.Input[str] description: A human-friendly description for this backend.
        :param pulumi.Input[int] max_lease_ttl_seconds: The maximum TTL that can be requested for credentials issued by this backend.
        """
        pulumi.set(__self__, "path", path)
        if default_lease_ttl_seconds is not None:
            pulumi.set(__self__, "default_lease_ttl_seconds", default_lease_ttl_seconds)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if max_lease_ttl_seconds is not None:
            pulumi.set(__self__, "max_lease_ttl_seconds", max_lease_ttl_seconds)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        The unique path this backend should be mounted at. Must not begin or end with a `/`.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="defaultLeaseTtlSeconds")
    def default_lease_ttl_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The default TTL for credentials issued by this backend.
        """
        return pulumi.get(self, "default_lease_ttl_seconds")

    @default_lease_ttl_seconds.setter
    def default_lease_ttl_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_lease_ttl_seconds", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A human-friendly description for this backend.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="maxLeaseTtlSeconds")
    def max_lease_ttl_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum TTL that can be requested for credentials issued by this backend.
        """
        return pulumi.get(self, "max_lease_ttl_seconds")

    @max_lease_ttl_seconds.setter
    def max_lease_ttl_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_lease_ttl_seconds", value)


@pulumi.input_type
class _SecretBackendState:
    def __init__(__self__, *,
                 default_lease_ttl_seconds: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_lease_ttl_seconds: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecretBackend resources.
        :param pulumi.Input[int] default_lease_ttl_seconds: The default TTL for credentials issued by this backend.
        :param pulumi.Input[str] description: A human-friendly description for this backend.
        :param pulumi.Input[int] max_lease_ttl_seconds: The maximum TTL that can be requested for credentials issued by this backend.
        :param pulumi.Input[str] path: The unique path this backend should be mounted at. Must not begin or end with a `/`.
        """
        if default_lease_ttl_seconds is not None:
            pulumi.set(__self__, "default_lease_ttl_seconds", default_lease_ttl_seconds)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if max_lease_ttl_seconds is not None:
            pulumi.set(__self__, "max_lease_ttl_seconds", max_lease_ttl_seconds)
        if path is not None:
            pulumi.set(__self__, "path", path)

    @property
    @pulumi.getter(name="defaultLeaseTtlSeconds")
    def default_lease_ttl_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The default TTL for credentials issued by this backend.
        """
        return pulumi.get(self, "default_lease_ttl_seconds")

    @default_lease_ttl_seconds.setter
    def default_lease_ttl_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "default_lease_ttl_seconds", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A human-friendly description for this backend.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="maxLeaseTtlSeconds")
    def max_lease_ttl_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum TTL that can be requested for credentials issued by this backend.
        """
        return pulumi.get(self, "max_lease_ttl_seconds")

    @max_lease_ttl_seconds.setter
    def max_lease_ttl_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_lease_ttl_seconds", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        The unique path this backend should be mounted at. Must not begin or end with a `/`.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)


class SecretBackend(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_lease_ttl_seconds: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_lease_ttl_seconds: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an PKI Secret Backend for Vault. PKI secret backends can then issue certificates, once a role has been added to
        the backend.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vault as vault

        pki = vault.pki_secret.SecretBackend("pki",
            default_lease_ttl_seconds=3600,
            max_lease_ttl_seconds=86400,
            path="pki")
        ```

        ## Import

        PKI secret backends can be imported using the `path`, e.g.

        ```sh
         $ pulumi import vault:pkiSecret/secretBackend:SecretBackend pki pki
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] default_lease_ttl_seconds: The default TTL for credentials issued by this backend.
        :param pulumi.Input[str] description: A human-friendly description for this backend.
        :param pulumi.Input[int] max_lease_ttl_seconds: The maximum TTL that can be requested for credentials issued by this backend.
        :param pulumi.Input[str] path: The unique path this backend should be mounted at. Must not begin or end with a `/`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecretBackendArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an PKI Secret Backend for Vault. PKI secret backends can then issue certificates, once a role has been added to
        the backend.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vault as vault

        pki = vault.pki_secret.SecretBackend("pki",
            default_lease_ttl_seconds=3600,
            max_lease_ttl_seconds=86400,
            path="pki")
        ```

        ## Import

        PKI secret backends can be imported using the `path`, e.g.

        ```sh
         $ pulumi import vault:pkiSecret/secretBackend:SecretBackend pki pki
        ```

        :param str resource_name: The name of the resource.
        :param SecretBackendArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecretBackendArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_lease_ttl_seconds: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 max_lease_ttl_seconds: Optional[pulumi.Input[int]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecretBackendArgs.__new__(SecretBackendArgs)

            __props__.__dict__["default_lease_ttl_seconds"] = default_lease_ttl_seconds
            __props__.__dict__["description"] = description
            __props__.__dict__["max_lease_ttl_seconds"] = max_lease_ttl_seconds
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
        super(SecretBackend, __self__).__init__(
            'vault:pkiSecret/secretBackend:SecretBackend',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_lease_ttl_seconds: Optional[pulumi.Input[int]] = None,
            description: Optional[pulumi.Input[str]] = None,
            max_lease_ttl_seconds: Optional[pulumi.Input[int]] = None,
            path: Optional[pulumi.Input[str]] = None) -> 'SecretBackend':
        """
        Get an existing SecretBackend resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] default_lease_ttl_seconds: The default TTL for credentials issued by this backend.
        :param pulumi.Input[str] description: A human-friendly description for this backend.
        :param pulumi.Input[int] max_lease_ttl_seconds: The maximum TTL that can be requested for credentials issued by this backend.
        :param pulumi.Input[str] path: The unique path this backend should be mounted at. Must not begin or end with a `/`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecretBackendState.__new__(_SecretBackendState)

        __props__.__dict__["default_lease_ttl_seconds"] = default_lease_ttl_seconds
        __props__.__dict__["description"] = description
        __props__.__dict__["max_lease_ttl_seconds"] = max_lease_ttl_seconds
        __props__.__dict__["path"] = path
        return SecretBackend(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultLeaseTtlSeconds")
    def default_lease_ttl_seconds(self) -> pulumi.Output[int]:
        """
        The default TTL for credentials issued by this backend.
        """
        return pulumi.get(self, "default_lease_ttl_seconds")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A human-friendly description for this backend.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="maxLeaseTtlSeconds")
    def max_lease_ttl_seconds(self) -> pulumi.Output[int]:
        """
        The maximum TTL that can be requested for credentials issued by this backend.
        """
        return pulumi.get(self, "max_lease_ttl_seconds")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[str]:
        """
        The unique path this backend should be mounted at. Must not begin or end with a `/`.
        """
        return pulumi.get(self, "path")

