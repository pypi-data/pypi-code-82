# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 token: pulumi.Input[str],
                 base_url: Optional[pulumi.Input[str]] = None,
                 cacert_file: Optional[pulumi.Input[str]] = None,
                 client_cert: Optional[pulumi.Input[str]] = None,
                 client_key: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] token: The OAuth token used to connect to GitLab.
        :param pulumi.Input[str] base_url: The GitLab Base API URL
        :param pulumi.Input[str] cacert_file: A file containing the ca certificate to use in case ssl certificate is not from a standard chain
        :param pulumi.Input[str] client_cert: File path to client certificate when GitLab instance is behind company proxy. File must contain PEM encoded data.
        :param pulumi.Input[str] client_key: File path to client key when GitLab instance is behind company proxy. File must contain PEM encoded data.
        :param pulumi.Input[bool] insecure: Disable SSL verification of API calls
        """
        pulumi.set(__self__, "token", token)
        if base_url is not None:
            pulumi.set(__self__, "base_url", base_url)
        if cacert_file is not None:
            pulumi.set(__self__, "cacert_file", cacert_file)
        if client_cert is not None:
            pulumi.set(__self__, "client_cert", client_cert)
        if client_key is not None:
            pulumi.set(__self__, "client_key", client_key)
        if insecure is not None:
            pulumi.set(__self__, "insecure", insecure)

    @property
    @pulumi.getter
    def token(self) -> pulumi.Input[str]:
        """
        The OAuth token used to connect to GitLab.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: pulumi.Input[str]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> Optional[pulumi.Input[str]]:
        """
        The GitLab Base API URL
        """
        return pulumi.get(self, "base_url")

    @base_url.setter
    def base_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_url", value)

    @property
    @pulumi.getter(name="cacertFile")
    def cacert_file(self) -> Optional[pulumi.Input[str]]:
        """
        A file containing the ca certificate to use in case ssl certificate is not from a standard chain
        """
        return pulumi.get(self, "cacert_file")

    @cacert_file.setter
    def cacert_file(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cacert_file", value)

    @property
    @pulumi.getter(name="clientCert")
    def client_cert(self) -> Optional[pulumi.Input[str]]:
        """
        File path to client certificate when GitLab instance is behind company proxy. File must contain PEM encoded data.
        """
        return pulumi.get(self, "client_cert")

    @client_cert.setter
    def client_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_cert", value)

    @property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> Optional[pulumi.Input[str]]:
        """
        File path to client key when GitLab instance is behind company proxy. File must contain PEM encoded data.
        """
        return pulumi.get(self, "client_key")

    @client_key.setter
    def client_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_key", value)

    @property
    @pulumi.getter
    def insecure(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable SSL verification of API calls
        """
        return pulumi.get(self, "insecure")

    @insecure.setter
    def insecure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 cacert_file: Optional[pulumi.Input[str]] = None,
                 client_cert: Optional[pulumi.Input[str]] = None,
                 client_key: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The provider type for the gitlab package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_url: The GitLab Base API URL
        :param pulumi.Input[str] cacert_file: A file containing the ca certificate to use in case ssl certificate is not from a standard chain
        :param pulumi.Input[str] client_cert: File path to client certificate when GitLab instance is behind company proxy. File must contain PEM encoded data.
        :param pulumi.Input[str] client_key: File path to client key when GitLab instance is behind company proxy. File must contain PEM encoded data.
        :param pulumi.Input[bool] insecure: Disable SSL verification of API calls
        :param pulumi.Input[str] token: The OAuth token used to connect to GitLab.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the gitlab package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 cacert_file: Optional[pulumi.Input[str]] = None,
                 client_cert: Optional[pulumi.Input[str]] = None,
                 client_key: Optional[pulumi.Input[str]] = None,
                 insecure: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
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
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["base_url"] = base_url
            __props__.__dict__["cacert_file"] = cacert_file
            __props__.__dict__["client_cert"] = client_cert
            __props__.__dict__["client_key"] = client_key
            __props__.__dict__["insecure"] = pulumi.Output.from_input(insecure).apply(pulumi.runtime.to_json) if insecure is not None else None
            if token is None and not opts.urn:
                raise TypeError("Missing required property 'token'")
            __props__.__dict__["token"] = token
        super(Provider, __self__).__init__(
            'gitlab',
            resource_name,
            __props__,
            opts)

