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
                 api_token: Optional[pulumi.Input[str]] = None,
                 backoff: Optional[pulumi.Input[bool]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 log_level: Optional[pulumi.Input[int]] = None,
                 max_retries: Optional[pulumi.Input[int]] = None,
                 max_wait_seconds: Optional[pulumi.Input[int]] = None,
                 min_wait_seconds: Optional[pulumi.Input[int]] = None,
                 org_name: Optional[pulumi.Input[str]] = None,
                 parallelism: Optional[pulumi.Input[int]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 request_timeout: Optional[pulumi.Input[int]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] api_token: API Token granting privileges to Okta API.
        :param pulumi.Input[bool] backoff: Use exponential back off strategy for rate limits.
        :param pulumi.Input[str] base_url: The Okta url. (Use 'oktapreview.com' for Okta testing)
        :param pulumi.Input[str] client_id: API Token granting privileges to Okta API.
        :param pulumi.Input[int] log_level: providers log level. Minimum is 1 (TRACE), and maximum is 5 (ERROR)
        :param pulumi.Input[int] max_retries: maximum number of retries to attempt before erroring out.
        :param pulumi.Input[int] max_wait_seconds: maximum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.
        :param pulumi.Input[int] min_wait_seconds: minimum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.
        :param pulumi.Input[str] org_name: The organization to manage in Okta.
        :param pulumi.Input[int] parallelism: Number of concurrent requests to make within a resource where bulk operations are not possible. Take note of
               https://developer.okta.com/docs/api/getting_started/rate-limits.
        :param pulumi.Input[str] private_key: API Token granting privileges to Okta API.
        :param pulumi.Input[int] request_timeout: Timeout for single request (in seconds) which is made to Okta, the default is `0` (means no limit is set). The maximum
               value can be `100`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: API Token granting privileges to Okta API.
        """
        if api_token is not None:
            pulumi.set(__self__, "api_token", api_token)
        if backoff is not None:
            pulumi.set(__self__, "backoff", backoff)
        if base_url is not None:
            pulumi.set(__self__, "base_url", base_url)
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if log_level is not None:
            pulumi.set(__self__, "log_level", log_level)
        if max_retries is not None:
            pulumi.set(__self__, "max_retries", max_retries)
        if max_wait_seconds is not None:
            pulumi.set(__self__, "max_wait_seconds", max_wait_seconds)
        if min_wait_seconds is not None:
            pulumi.set(__self__, "min_wait_seconds", min_wait_seconds)
        if org_name is not None:
            pulumi.set(__self__, "org_name", org_name)
        if parallelism is not None:
            pulumi.set(__self__, "parallelism", parallelism)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if request_timeout is not None:
            pulumi.set(__self__, "request_timeout", request_timeout)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> Optional[pulumi.Input[str]]:
        """
        API Token granting privileges to Okta API.
        """
        return pulumi.get(self, "api_token")

    @api_token.setter
    def api_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_token", value)

    @property
    @pulumi.getter
    def backoff(self) -> Optional[pulumi.Input[bool]]:
        """
        Use exponential back off strategy for rate limits.
        """
        return pulumi.get(self, "backoff")

    @backoff.setter
    def backoff(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "backoff", value)

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> Optional[pulumi.Input[str]]:
        """
        The Okta url. (Use 'oktapreview.com' for Okta testing)
        """
        return pulumi.get(self, "base_url")

    @base_url.setter
    def base_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_url", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        API Token granting privileges to Okta API.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[int]]:
        """
        providers log level. Minimum is 1 (TRACE), and maximum is 5 (ERROR)
        """
        return pulumi.get(self, "log_level")

    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "log_level", value)

    @property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[int]]:
        """
        maximum number of retries to attempt before erroring out.
        """
        return pulumi.get(self, "max_retries")

    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_retries", value)

    @property
    @pulumi.getter(name="maxWaitSeconds")
    def max_wait_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        maximum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.
        """
        return pulumi.get(self, "max_wait_seconds")

    @max_wait_seconds.setter
    def max_wait_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_wait_seconds", value)

    @property
    @pulumi.getter(name="minWaitSeconds")
    def min_wait_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        minimum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.
        """
        return pulumi.get(self, "min_wait_seconds")

    @min_wait_seconds.setter
    def min_wait_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_wait_seconds", value)

    @property
    @pulumi.getter(name="orgName")
    def org_name(self) -> Optional[pulumi.Input[str]]:
        """
        The organization to manage in Okta.
        """
        return pulumi.get(self, "org_name")

    @org_name.setter
    def org_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_name", value)

    @property
    @pulumi.getter
    def parallelism(self) -> Optional[pulumi.Input[int]]:
        """
        Number of concurrent requests to make within a resource where bulk operations are not possible. Take note of
        https://developer.okta.com/docs/api/getting_started/rate-limits.
        """
        return pulumi.get(self, "parallelism")

    @parallelism.setter
    def parallelism(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "parallelism", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        API Token granting privileges to Okta API.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="requestTimeout")
    def request_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Timeout for single request (in seconds) which is made to Okta, the default is `0` (means no limit is set). The maximum
        value can be `100`.
        """
        return pulumi.get(self, "request_timeout")

    @request_timeout.setter
    def request_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "request_timeout", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        API Token granting privileges to Okta API.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 backoff: Optional[pulumi.Input[bool]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 log_level: Optional[pulumi.Input[int]] = None,
                 max_retries: Optional[pulumi.Input[int]] = None,
                 max_wait_seconds: Optional[pulumi.Input[int]] = None,
                 min_wait_seconds: Optional[pulumi.Input[int]] = None,
                 org_name: Optional[pulumi.Input[str]] = None,
                 parallelism: Optional[pulumi.Input[int]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 request_timeout: Optional[pulumi.Input[int]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The provider type for the okta package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_token: API Token granting privileges to Okta API.
        :param pulumi.Input[bool] backoff: Use exponential back off strategy for rate limits.
        :param pulumi.Input[str] base_url: The Okta url. (Use 'oktapreview.com' for Okta testing)
        :param pulumi.Input[str] client_id: API Token granting privileges to Okta API.
        :param pulumi.Input[int] log_level: providers log level. Minimum is 1 (TRACE), and maximum is 5 (ERROR)
        :param pulumi.Input[int] max_retries: maximum number of retries to attempt before erroring out.
        :param pulumi.Input[int] max_wait_seconds: maximum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.
        :param pulumi.Input[int] min_wait_seconds: minimum seconds to wait when rate limit is hit. We use exponential backoffs when backoff is enabled.
        :param pulumi.Input[str] org_name: The organization to manage in Okta.
        :param pulumi.Input[int] parallelism: Number of concurrent requests to make within a resource where bulk operations are not possible. Take note of
               https://developer.okta.com/docs/api/getting_started/rate-limits.
        :param pulumi.Input[str] private_key: API Token granting privileges to Okta API.
        :param pulumi.Input[int] request_timeout: Timeout for single request (in seconds) which is made to Okta, the default is `0` (means no limit is set). The maximum
               value can be `100`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: API Token granting privileges to Okta API.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the okta package. By default, resources use package-wide configuration
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
                 api_token: Optional[pulumi.Input[str]] = None,
                 backoff: Optional[pulumi.Input[bool]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 log_level: Optional[pulumi.Input[int]] = None,
                 max_retries: Optional[pulumi.Input[int]] = None,
                 max_wait_seconds: Optional[pulumi.Input[int]] = None,
                 min_wait_seconds: Optional[pulumi.Input[int]] = None,
                 org_name: Optional[pulumi.Input[str]] = None,
                 parallelism: Optional[pulumi.Input[int]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 request_timeout: Optional[pulumi.Input[int]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
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

            __props__.__dict__["api_token"] = api_token
            __props__.__dict__["backoff"] = pulumi.Output.from_input(backoff).apply(pulumi.runtime.to_json) if backoff is not None else None
            __props__.__dict__["base_url"] = base_url
            __props__.__dict__["client_id"] = client_id
            __props__.__dict__["log_level"] = pulumi.Output.from_input(log_level).apply(pulumi.runtime.to_json) if log_level is not None else None
            __props__.__dict__["max_retries"] = pulumi.Output.from_input(max_retries).apply(pulumi.runtime.to_json) if max_retries is not None else None
            __props__.__dict__["max_wait_seconds"] = pulumi.Output.from_input(max_wait_seconds).apply(pulumi.runtime.to_json) if max_wait_seconds is not None else None
            __props__.__dict__["min_wait_seconds"] = pulumi.Output.from_input(min_wait_seconds).apply(pulumi.runtime.to_json) if min_wait_seconds is not None else None
            __props__.__dict__["org_name"] = org_name
            __props__.__dict__["parallelism"] = pulumi.Output.from_input(parallelism).apply(pulumi.runtime.to_json) if parallelism is not None else None
            __props__.__dict__["private_key"] = private_key
            __props__.__dict__["request_timeout"] = pulumi.Output.from_input(request_timeout).apply(pulumi.runtime.to_json) if request_timeout is not None else None
            __props__.__dict__["scopes"] = pulumi.Output.from_input(scopes).apply(pulumi.runtime.to_json) if scopes is not None else None
        super(Provider, __self__).__init__(
            'okta',
            resource_name,
            __props__,
            opts)

