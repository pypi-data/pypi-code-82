# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AccessApplicationArgs', 'AccessApplication']

@pulumi.input_type
class AccessApplicationArgs:
    def __init__(__self__, *,
                 domain: pulumi.Input[str],
                 name: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 allowed_idps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 auto_redirect_to_identity: Optional[pulumi.Input[bool]] = None,
                 cors_headers: Optional[pulumi.Input[Sequence[pulumi.Input['AccessApplicationCorsHeaderArgs']]]] = None,
                 custom_deny_message: Optional[pulumi.Input[str]] = None,
                 custom_deny_url: Optional[pulumi.Input[str]] = None,
                 enable_binding_cookie: Optional[pulumi.Input[bool]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessApplication resource.
        :param pulumi.Input[str] domain: The complete URL of the asset you wish to put
               Cloudflare Access in front of. Can include subdomains or paths. Or both.
        :param pulumi.Input[str] name: Friendly name of the Access Application.
        :param pulumi.Input[str] account_id: The account to which the access application should be added. Conflicts with `zone_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_idps: The identity providers selected for the application.
        :param pulumi.Input[bool] auto_redirect_to_identity: Option to skip identity provider
               selection if only one is configured in allowed_idps. Defaults to `false`
               (disabled).
        :param pulumi.Input[Sequence[pulumi.Input['AccessApplicationCorsHeaderArgs']]] cors_headers: CORS configuration for the Access Application. See
               below for reference structure.
        :param pulumi.Input[str] custom_deny_message: Option that returns a custom error message when a user is denied access to the application.
        :param pulumi.Input[str] custom_deny_url: Option that redirects to a custom URL when a user is denied access to the application.
        :param pulumi.Input[bool] enable_binding_cookie: Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to `false`.
        :param pulumi.Input[str] session_duration: How often a user will be forced to
               re-authorise. Must be in the format `"48h"` or `"2h45m"`.
               Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. Defaults to `24h`.
        :param pulumi.Input[str] zone_id: The DNS zone to which the access application should be added. Conflicts with `account_id`.
        """
        pulumi.set(__self__, "domain", domain)
        pulumi.set(__self__, "name", name)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if allowed_idps is not None:
            pulumi.set(__self__, "allowed_idps", allowed_idps)
        if auto_redirect_to_identity is not None:
            pulumi.set(__self__, "auto_redirect_to_identity", auto_redirect_to_identity)
        if cors_headers is not None:
            pulumi.set(__self__, "cors_headers", cors_headers)
        if custom_deny_message is not None:
            pulumi.set(__self__, "custom_deny_message", custom_deny_message)
        if custom_deny_url is not None:
            pulumi.set(__self__, "custom_deny_url", custom_deny_url)
        if enable_binding_cookie is not None:
            pulumi.set(__self__, "enable_binding_cookie", enable_binding_cookie)
        if session_duration is not None:
            pulumi.set(__self__, "session_duration", session_duration)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Input[str]:
        """
        The complete URL of the asset you wish to put
        Cloudflare Access in front of. Can include subdomains or paths. Or both.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Friendly name of the Access Application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account to which the access application should be added. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="allowedIdps")
    def allowed_idps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The identity providers selected for the application.
        """
        return pulumi.get(self, "allowed_idps")

    @allowed_idps.setter
    def allowed_idps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_idps", value)

    @property
    @pulumi.getter(name="autoRedirectToIdentity")
    def auto_redirect_to_identity(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to skip identity provider
        selection if only one is configured in allowed_idps. Defaults to `false`
        (disabled).
        """
        return pulumi.get(self, "auto_redirect_to_identity")

    @auto_redirect_to_identity.setter
    def auto_redirect_to_identity(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_redirect_to_identity", value)

    @property
    @pulumi.getter(name="corsHeaders")
    def cors_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessApplicationCorsHeaderArgs']]]]:
        """
        CORS configuration for the Access Application. See
        below for reference structure.
        """
        return pulumi.get(self, "cors_headers")

    @cors_headers.setter
    def cors_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessApplicationCorsHeaderArgs']]]]):
        pulumi.set(self, "cors_headers", value)

    @property
    @pulumi.getter(name="customDenyMessage")
    def custom_deny_message(self) -> Optional[pulumi.Input[str]]:
        """
        Option that returns a custom error message when a user is denied access to the application.
        """
        return pulumi.get(self, "custom_deny_message")

    @custom_deny_message.setter
    def custom_deny_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_deny_message", value)

    @property
    @pulumi.getter(name="customDenyUrl")
    def custom_deny_url(self) -> Optional[pulumi.Input[str]]:
        """
        Option that redirects to a custom URL when a user is denied access to the application.
        """
        return pulumi.get(self, "custom_deny_url")

    @custom_deny_url.setter
    def custom_deny_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_deny_url", value)

    @property
    @pulumi.getter(name="enableBindingCookie")
    def enable_binding_cookie(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to `false`.
        """
        return pulumi.get(self, "enable_binding_cookie")

    @enable_binding_cookie.setter
    def enable_binding_cookie(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_binding_cookie", value)

    @property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> Optional[pulumi.Input[str]]:
        """
        How often a user will be forced to
        re-authorise. Must be in the format `"48h"` or `"2h45m"`.
        Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. Defaults to `24h`.
        """
        return pulumi.get(self, "session_duration")

    @session_duration.setter
    def session_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_duration", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone to which the access application should be added. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _AccessApplicationState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 allowed_idps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 aud: Optional[pulumi.Input[str]] = None,
                 auto_redirect_to_identity: Optional[pulumi.Input[bool]] = None,
                 cors_headers: Optional[pulumi.Input[Sequence[pulumi.Input['AccessApplicationCorsHeaderArgs']]]] = None,
                 custom_deny_message: Optional[pulumi.Input[str]] = None,
                 custom_deny_url: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 enable_binding_cookie: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessApplication resources.
        :param pulumi.Input[str] account_id: The account to which the access application should be added. Conflicts with `zone_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_idps: The identity providers selected for the application.
        :param pulumi.Input[str] aud: Application Audience (AUD) Tag of the application
        :param pulumi.Input[bool] auto_redirect_to_identity: Option to skip identity provider
               selection if only one is configured in allowed_idps. Defaults to `false`
               (disabled).
        :param pulumi.Input[Sequence[pulumi.Input['AccessApplicationCorsHeaderArgs']]] cors_headers: CORS configuration for the Access Application. See
               below for reference structure.
        :param pulumi.Input[str] custom_deny_message: Option that returns a custom error message when a user is denied access to the application.
        :param pulumi.Input[str] custom_deny_url: Option that redirects to a custom URL when a user is denied access to the application.
        :param pulumi.Input[str] domain: The complete URL of the asset you wish to put
               Cloudflare Access in front of. Can include subdomains or paths. Or both.
        :param pulumi.Input[bool] enable_binding_cookie: Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to `false`.
        :param pulumi.Input[str] name: Friendly name of the Access Application.
        :param pulumi.Input[str] session_duration: How often a user will be forced to
               re-authorise. Must be in the format `"48h"` or `"2h45m"`.
               Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. Defaults to `24h`.
        :param pulumi.Input[str] zone_id: The DNS zone to which the access application should be added. Conflicts with `account_id`.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if allowed_idps is not None:
            pulumi.set(__self__, "allowed_idps", allowed_idps)
        if aud is not None:
            pulumi.set(__self__, "aud", aud)
        if auto_redirect_to_identity is not None:
            pulumi.set(__self__, "auto_redirect_to_identity", auto_redirect_to_identity)
        if cors_headers is not None:
            pulumi.set(__self__, "cors_headers", cors_headers)
        if custom_deny_message is not None:
            pulumi.set(__self__, "custom_deny_message", custom_deny_message)
        if custom_deny_url is not None:
            pulumi.set(__self__, "custom_deny_url", custom_deny_url)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if enable_binding_cookie is not None:
            pulumi.set(__self__, "enable_binding_cookie", enable_binding_cookie)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if session_duration is not None:
            pulumi.set(__self__, "session_duration", session_duration)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The account to which the access application should be added. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="allowedIdps")
    def allowed_idps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The identity providers selected for the application.
        """
        return pulumi.get(self, "allowed_idps")

    @allowed_idps.setter
    def allowed_idps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_idps", value)

    @property
    @pulumi.getter
    def aud(self) -> Optional[pulumi.Input[str]]:
        """
        Application Audience (AUD) Tag of the application
        """
        return pulumi.get(self, "aud")

    @aud.setter
    def aud(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aud", value)

    @property
    @pulumi.getter(name="autoRedirectToIdentity")
    def auto_redirect_to_identity(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to skip identity provider
        selection if only one is configured in allowed_idps. Defaults to `false`
        (disabled).
        """
        return pulumi.get(self, "auto_redirect_to_identity")

    @auto_redirect_to_identity.setter
    def auto_redirect_to_identity(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_redirect_to_identity", value)

    @property
    @pulumi.getter(name="corsHeaders")
    def cors_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AccessApplicationCorsHeaderArgs']]]]:
        """
        CORS configuration for the Access Application. See
        below for reference structure.
        """
        return pulumi.get(self, "cors_headers")

    @cors_headers.setter
    def cors_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AccessApplicationCorsHeaderArgs']]]]):
        pulumi.set(self, "cors_headers", value)

    @property
    @pulumi.getter(name="customDenyMessage")
    def custom_deny_message(self) -> Optional[pulumi.Input[str]]:
        """
        Option that returns a custom error message when a user is denied access to the application.
        """
        return pulumi.get(self, "custom_deny_message")

    @custom_deny_message.setter
    def custom_deny_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_deny_message", value)

    @property
    @pulumi.getter(name="customDenyUrl")
    def custom_deny_url(self) -> Optional[pulumi.Input[str]]:
        """
        Option that redirects to a custom URL when a user is denied access to the application.
        """
        return pulumi.get(self, "custom_deny_url")

    @custom_deny_url.setter
    def custom_deny_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_deny_url", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The complete URL of the asset you wish to put
        Cloudflare Access in front of. Can include subdomains or paths. Or both.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="enableBindingCookie")
    def enable_binding_cookie(self) -> Optional[pulumi.Input[bool]]:
        """
        Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to `false`.
        """
        return pulumi.get(self, "enable_binding_cookie")

    @enable_binding_cookie.setter
    def enable_binding_cookie(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_binding_cookie", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of the Access Application.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> Optional[pulumi.Input[str]]:
        """
        How often a user will be forced to
        re-authorise. Must be in the format `"48h"` or `"2h45m"`.
        Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. Defaults to `24h`.
        """
        return pulumi.get(self, "session_duration")

    @session_duration.setter
    def session_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "session_duration", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The DNS zone to which the access application should be added. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class AccessApplication(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 allowed_idps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 auto_redirect_to_identity: Optional[pulumi.Input[bool]] = None,
                 cors_headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApplicationCorsHeaderArgs']]]]] = None,
                 custom_deny_message: Optional[pulumi.Input[str]] = None,
                 custom_deny_url: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 enable_binding_cookie: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Cloudflare Access Application resource. Access Applications
        are used to restrict access to a whole application using an
        authorisation gateway managed by Cloudflare.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # With CORS configuration
        staging_app = cloudflare.AccessApplication("stagingApp",
            cors_headers=[cloudflare.AccessApplicationCorsHeaderArgs(
                allow_credentials=True,
                allowed_methods=[
                    "GET",
                    "POST",
                    "OPTIONS",
                ],
                allowed_origins=["https://example.com"],
                max_age=10,
            )],
            domain="staging.example.com",
            name="staging application",
            session_duration="24h",
            zone_id="1d5fdc9e88c8a8c4518b068cd94331fe")
        ```

        ## Import

        Access Applications can be imported using a composite ID formed of zone ID and application ID.

        ```sh
         $ pulumi import cloudflare:index/accessApplication:AccessApplication staging cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account to which the access application should be added. Conflicts with `zone_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_idps: The identity providers selected for the application.
        :param pulumi.Input[bool] auto_redirect_to_identity: Option to skip identity provider
               selection if only one is configured in allowed_idps. Defaults to `false`
               (disabled).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApplicationCorsHeaderArgs']]]] cors_headers: CORS configuration for the Access Application. See
               below for reference structure.
        :param pulumi.Input[str] custom_deny_message: Option that returns a custom error message when a user is denied access to the application.
        :param pulumi.Input[str] custom_deny_url: Option that redirects to a custom URL when a user is denied access to the application.
        :param pulumi.Input[str] domain: The complete URL of the asset you wish to put
               Cloudflare Access in front of. Can include subdomains or paths. Or both.
        :param pulumi.Input[bool] enable_binding_cookie: Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to `false`.
        :param pulumi.Input[str] name: Friendly name of the Access Application.
        :param pulumi.Input[str] session_duration: How often a user will be forced to
               re-authorise. Must be in the format `"48h"` or `"2h45m"`.
               Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. Defaults to `24h`.
        :param pulumi.Input[str] zone_id: The DNS zone to which the access application should be added. Conflicts with `account_id`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessApplicationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Cloudflare Access Application resource. Access Applications
        are used to restrict access to a whole application using an
        authorisation gateway managed by Cloudflare.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        # With CORS configuration
        staging_app = cloudflare.AccessApplication("stagingApp",
            cors_headers=[cloudflare.AccessApplicationCorsHeaderArgs(
                allow_credentials=True,
                allowed_methods=[
                    "GET",
                    "POST",
                    "OPTIONS",
                ],
                allowed_origins=["https://example.com"],
                max_age=10,
            )],
            domain="staging.example.com",
            name="staging application",
            session_duration="24h",
            zone_id="1d5fdc9e88c8a8c4518b068cd94331fe")
        ```

        ## Import

        Access Applications can be imported using a composite ID formed of zone ID and application ID.

        ```sh
         $ pulumi import cloudflare:index/accessApplication:AccessApplication staging cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
        ```

        :param str resource_name: The name of the resource.
        :param AccessApplicationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessApplicationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 allowed_idps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 auto_redirect_to_identity: Optional[pulumi.Input[bool]] = None,
                 cors_headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApplicationCorsHeaderArgs']]]]] = None,
                 custom_deny_message: Optional[pulumi.Input[str]] = None,
                 custom_deny_url: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 enable_binding_cookie: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 session_duration: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccessApplicationArgs.__new__(AccessApplicationArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["allowed_idps"] = allowed_idps
            __props__.__dict__["auto_redirect_to_identity"] = auto_redirect_to_identity
            __props__.__dict__["cors_headers"] = cors_headers
            __props__.__dict__["custom_deny_message"] = custom_deny_message
            __props__.__dict__["custom_deny_url"] = custom_deny_url
            if domain is None and not opts.urn:
                raise TypeError("Missing required property 'domain'")
            __props__.__dict__["domain"] = domain
            __props__.__dict__["enable_binding_cookie"] = enable_binding_cookie
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["session_duration"] = session_duration
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["aud"] = None
        super(AccessApplication, __self__).__init__(
            'cloudflare:index/accessApplication:AccessApplication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            allowed_idps: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            aud: Optional[pulumi.Input[str]] = None,
            auto_redirect_to_identity: Optional[pulumi.Input[bool]] = None,
            cors_headers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApplicationCorsHeaderArgs']]]]] = None,
            custom_deny_message: Optional[pulumi.Input[str]] = None,
            custom_deny_url: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            enable_binding_cookie: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            session_duration: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'AccessApplication':
        """
        Get an existing AccessApplication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The account to which the access application should be added. Conflicts with `zone_id`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_idps: The identity providers selected for the application.
        :param pulumi.Input[str] aud: Application Audience (AUD) Tag of the application
        :param pulumi.Input[bool] auto_redirect_to_identity: Option to skip identity provider
               selection if only one is configured in allowed_idps. Defaults to `false`
               (disabled).
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AccessApplicationCorsHeaderArgs']]]] cors_headers: CORS configuration for the Access Application. See
               below for reference structure.
        :param pulumi.Input[str] custom_deny_message: Option that returns a custom error message when a user is denied access to the application.
        :param pulumi.Input[str] custom_deny_url: Option that redirects to a custom URL when a user is denied access to the application.
        :param pulumi.Input[str] domain: The complete URL of the asset you wish to put
               Cloudflare Access in front of. Can include subdomains or paths. Or both.
        :param pulumi.Input[bool] enable_binding_cookie: Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to `false`.
        :param pulumi.Input[str] name: Friendly name of the Access Application.
        :param pulumi.Input[str] session_duration: How often a user will be forced to
               re-authorise. Must be in the format `"48h"` or `"2h45m"`.
               Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. Defaults to `24h`.
        :param pulumi.Input[str] zone_id: The DNS zone to which the access application should be added. Conflicts with `account_id`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessApplicationState.__new__(_AccessApplicationState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["allowed_idps"] = allowed_idps
        __props__.__dict__["aud"] = aud
        __props__.__dict__["auto_redirect_to_identity"] = auto_redirect_to_identity
        __props__.__dict__["cors_headers"] = cors_headers
        __props__.__dict__["custom_deny_message"] = custom_deny_message
        __props__.__dict__["custom_deny_url"] = custom_deny_url
        __props__.__dict__["domain"] = domain
        __props__.__dict__["enable_binding_cookie"] = enable_binding_cookie
        __props__.__dict__["name"] = name
        __props__.__dict__["session_duration"] = session_duration
        __props__.__dict__["zone_id"] = zone_id
        return AccessApplication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The account to which the access application should be added. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="allowedIdps")
    def allowed_idps(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The identity providers selected for the application.
        """
        return pulumi.get(self, "allowed_idps")

    @property
    @pulumi.getter
    def aud(self) -> pulumi.Output[str]:
        """
        Application Audience (AUD) Tag of the application
        """
        return pulumi.get(self, "aud")

    @property
    @pulumi.getter(name="autoRedirectToIdentity")
    def auto_redirect_to_identity(self) -> pulumi.Output[Optional[bool]]:
        """
        Option to skip identity provider
        selection if only one is configured in allowed_idps. Defaults to `false`
        (disabled).
        """
        return pulumi.get(self, "auto_redirect_to_identity")

    @property
    @pulumi.getter(name="corsHeaders")
    def cors_headers(self) -> pulumi.Output[Optional[Sequence['outputs.AccessApplicationCorsHeader']]]:
        """
        CORS configuration for the Access Application. See
        below for reference structure.
        """
        return pulumi.get(self, "cors_headers")

    @property
    @pulumi.getter(name="customDenyMessage")
    def custom_deny_message(self) -> pulumi.Output[Optional[str]]:
        """
        Option that returns a custom error message when a user is denied access to the application.
        """
        return pulumi.get(self, "custom_deny_message")

    @property
    @pulumi.getter(name="customDenyUrl")
    def custom_deny_url(self) -> pulumi.Output[Optional[str]]:
        """
        Option that redirects to a custom URL when a user is denied access to the application.
        """
        return pulumi.get(self, "custom_deny_url")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[str]:
        """
        The complete URL of the asset you wish to put
        Cloudflare Access in front of. Can include subdomains or paths. Or both.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="enableBindingCookie")
    def enable_binding_cookie(self) -> pulumi.Output[Optional[bool]]:
        """
        Option to provide increased security against compromised authorization tokens and CSRF attacks by requiring an additional "binding" cookie on requests. Defaults to `false`.
        """
        return pulumi.get(self, "enable_binding_cookie")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Friendly name of the Access Application.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sessionDuration")
    def session_duration(self) -> pulumi.Output[Optional[str]]:
        """
        How often a user will be forced to
        re-authorise. Must be in the format `"48h"` or `"2h45m"`.
        Valid time units are `ns`, `us` (or `µs`), `ms`, `s`, `m`, `h`. Defaults to `24h`.
        """
        return pulumi.get(self, "session_duration")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[str]:
        """
        The DNS zone to which the access application should be added. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

