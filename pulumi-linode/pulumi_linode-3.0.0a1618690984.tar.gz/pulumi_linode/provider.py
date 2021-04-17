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
                 api_version: Optional[pulumi.Input[str]] = None,
                 max_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 min_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 skip_instance_ready_poll: Optional[pulumi.Input[bool]] = None,
                 ua_prefix: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] token: The token that allows you access to your Linode account
        :param pulumi.Input[str] api_version: An HTTP User-Agent Prefix to prepend in API requests.
        :param pulumi.Input[int] max_retry_delay_ms: Maximum delay in milliseconds before retrying a request.
        :param pulumi.Input[int] min_retry_delay_ms: Minimum delay in milliseconds before retrying a request.
        :param pulumi.Input[bool] skip_instance_ready_poll: Skip waiting for a linode_instance resource to be running.
        :param pulumi.Input[str] ua_prefix: An HTTP User-Agent Prefix to prepend in API requests.
        :param pulumi.Input[str] url: The HTTP(S) API address of the Linode API to use.
        """
        pulumi.set(__self__, "token", token)
        if api_version is None:
            api_version = _utilities.get_env('LINODE_API_VERSION')
        if api_version is not None:
            pulumi.set(__self__, "api_version", api_version)
        if max_retry_delay_ms is not None:
            pulumi.set(__self__, "max_retry_delay_ms", max_retry_delay_ms)
        if min_retry_delay_ms is not None:
            pulumi.set(__self__, "min_retry_delay_ms", min_retry_delay_ms)
        if skip_instance_ready_poll is not None:
            pulumi.set(__self__, "skip_instance_ready_poll", skip_instance_ready_poll)
        if ua_prefix is None:
            ua_prefix = _utilities.get_env('LINODE_UA_PREFIX')
        if ua_prefix is not None:
            pulumi.set(__self__, "ua_prefix", ua_prefix)
        if url is None:
            url = _utilities.get_env('LINODE_URL')
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def token(self) -> pulumi.Input[str]:
        """
        The token that allows you access to your Linode account
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: pulumi.Input[str]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        An HTTP User-Agent Prefix to prepend in API requests.
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter(name="maxRetryDelayMs")
    def max_retry_delay_ms(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum delay in milliseconds before retrying a request.
        """
        return pulumi.get(self, "max_retry_delay_ms")

    @max_retry_delay_ms.setter
    def max_retry_delay_ms(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_retry_delay_ms", value)

    @property
    @pulumi.getter(name="minRetryDelayMs")
    def min_retry_delay_ms(self) -> Optional[pulumi.Input[int]]:
        """
        Minimum delay in milliseconds before retrying a request.
        """
        return pulumi.get(self, "min_retry_delay_ms")

    @min_retry_delay_ms.setter
    def min_retry_delay_ms(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_retry_delay_ms", value)

    @property
    @pulumi.getter(name="skipInstanceReadyPoll")
    def skip_instance_ready_poll(self) -> Optional[pulumi.Input[bool]]:
        """
        Skip waiting for a linode_instance resource to be running.
        """
        return pulumi.get(self, "skip_instance_ready_poll")

    @skip_instance_ready_poll.setter
    def skip_instance_ready_poll(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_instance_ready_poll", value)

    @property
    @pulumi.getter(name="uaPrefix")
    def ua_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        An HTTP User-Agent Prefix to prepend in API requests.
        """
        return pulumi.get(self, "ua_prefix")

    @ua_prefix.setter
    def ua_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ua_prefix", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP(S) API address of the Linode API to use.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 max_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 min_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 skip_instance_ready_poll: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 ua_prefix: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The provider type for the linode package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: An HTTP User-Agent Prefix to prepend in API requests.
        :param pulumi.Input[int] max_retry_delay_ms: Maximum delay in milliseconds before retrying a request.
        :param pulumi.Input[int] min_retry_delay_ms: Minimum delay in milliseconds before retrying a request.
        :param pulumi.Input[bool] skip_instance_ready_poll: Skip waiting for a linode_instance resource to be running.
        :param pulumi.Input[str] token: The token that allows you access to your Linode account
        :param pulumi.Input[str] ua_prefix: An HTTP User-Agent Prefix to prepend in API requests.
        :param pulumi.Input[str] url: The HTTP(S) API address of the Linode API to use.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the linode package. By default, resources use package-wide configuration
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
                 api_version: Optional[pulumi.Input[str]] = None,
                 max_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 min_retry_delay_ms: Optional[pulumi.Input[int]] = None,
                 skip_instance_ready_poll: Optional[pulumi.Input[bool]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 ua_prefix: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
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

            if api_version is None:
                api_version = _utilities.get_env('LINODE_API_VERSION')
            __props__.__dict__["api_version"] = api_version
            __props__.__dict__["max_retry_delay_ms"] = pulumi.Output.from_input(max_retry_delay_ms).apply(pulumi.runtime.to_json) if max_retry_delay_ms is not None else None
            __props__.__dict__["min_retry_delay_ms"] = pulumi.Output.from_input(min_retry_delay_ms).apply(pulumi.runtime.to_json) if min_retry_delay_ms is not None else None
            __props__.__dict__["skip_instance_ready_poll"] = pulumi.Output.from_input(skip_instance_ready_poll).apply(pulumi.runtime.to_json) if skip_instance_ready_poll is not None else None
            if token is None and not opts.urn:
                raise TypeError("Missing required property 'token'")
            __props__.__dict__["token"] = token
            if ua_prefix is None:
                ua_prefix = _utilities.get_env('LINODE_UA_PREFIX')
            __props__.__dict__["ua_prefix"] = ua_prefix
            if url is None:
                url = _utilities.get_env('LINODE_URL')
            __props__.__dict__["url"] = url
        super(Provider, __self__).__init__(
            'linode',
            resource_name,
            __props__,
            opts)

