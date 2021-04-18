# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccessServiceTokenArgs', 'AccessServiceToken']

@pulumi.input_type
class AccessServiceTokenArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccessServiceToken resource.
        :param pulumi.Input[str] name: Friendly name of the token's intent.
        :param pulumi.Input[str] account_id: The ID of the account where the Access Service is being created. Conflicts with `zone_id`.
        :param pulumi.Input[str] zone_id: The ID of the zone where the Access Service is being created. Conflicts with `account_id`.
        """
        pulumi.set(__self__, "name", name)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Friendly name of the token's intent.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the account where the Access Service is being created. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the zone where the Access Service is being created. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


@pulumi.input_type
class _AccessServiceTokenState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 client_id: Optional[pulumi.Input[str]] = None,
                 client_secret: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccessServiceToken resources.
        :param pulumi.Input[str] account_id: The ID of the account where the Access Service is being created. Conflicts with `zone_id`.
        :param pulumi.Input[str] client_id: UUID client ID associated with the Service Token.
        :param pulumi.Input[str] client_secret: A secret for interacting with Access protocols.
        :param pulumi.Input[str] name: Friendly name of the token's intent.
        :param pulumi.Input[str] zone_id: The ID of the zone where the Access Service is being created. Conflicts with `account_id`.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if client_id is not None:
            pulumi.set(__self__, "client_id", client_id)
        if client_secret is not None:
            pulumi.set(__self__, "client_secret", client_secret)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if zone_id is not None:
            pulumi.set(__self__, "zone_id", zone_id)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the account where the Access Service is being created. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[str]]:
        """
        UUID client ID associated with the Service Token.
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        A secret for interacting with Access protocols.
        """
        return pulumi.get(self, "client_secret")

    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_secret", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of the token's intent.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the zone where the Access Service is being created. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

    @zone_id.setter
    def zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_id", value)


class AccessServiceToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 zone_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Access Service Tokens are used for service-to-service communication
        when an application is behind Cloudflare Access.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        my_app = cloudflare.AccessServiceToken("myApp",
            account_id="d41d8cd98f00b204e9800998ecf8427e",
            name="CI/CD app")
        ```

        ## Import

        ~> **Important:** If you are importing an Access Service Token you will not have the `client_secret` available in the state for use. The `client_secret` is only available once, at creation. In most cases, it is better to just create a new resource should you need to reference it in other resources. Access Service Tokens can be imported using a composite ID formed of account ID and Service Token ID.

        ```sh
         $ pulumi import cloudflare:index/accessServiceToken:AccessServiceToken my_app cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
        ```

         where * `cb029e245cfdd66dc8d2e570d5dd3322` - Account ID * `d41d8cd98f00b204e9800998ecf8427e` - Access Service Token ID

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the account where the Access Service is being created. Conflicts with `zone_id`.
        :param pulumi.Input[str] name: Friendly name of the token's intent.
        :param pulumi.Input[str] zone_id: The ID of the zone where the Access Service is being created. Conflicts with `account_id`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccessServiceTokenArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Access Service Tokens are used for service-to-service communication
        when an application is behind Cloudflare Access.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudflare as cloudflare

        my_app = cloudflare.AccessServiceToken("myApp",
            account_id="d41d8cd98f00b204e9800998ecf8427e",
            name="CI/CD app")
        ```

        ## Import

        ~> **Important:** If you are importing an Access Service Token you will not have the `client_secret` available in the state for use. The `client_secret` is only available once, at creation. In most cases, it is better to just create a new resource should you need to reference it in other resources. Access Service Tokens can be imported using a composite ID formed of account ID and Service Token ID.

        ```sh
         $ pulumi import cloudflare:index/accessServiceToken:AccessServiceToken my_app cb029e245cfdd66dc8d2e570d5dd3322/d41d8cd98f00b204e9800998ecf8427e
        ```

         where * `cb029e245cfdd66dc8d2e570d5dd3322` - Account ID * `d41d8cd98f00b204e9800998ecf8427e` - Access Service Token ID

        :param str resource_name: The name of the resource.
        :param AccessServiceTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccessServiceTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccessServiceTokenArgs.__new__(AccessServiceTokenArgs)

            __props__.__dict__["account_id"] = account_id
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["zone_id"] = zone_id
            __props__.__dict__["client_id"] = None
            __props__.__dict__["client_secret"] = None
        super(AccessServiceToken, __self__).__init__(
            'cloudflare:index/accessServiceToken:AccessServiceToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            client_id: Optional[pulumi.Input[str]] = None,
            client_secret: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            zone_id: Optional[pulumi.Input[str]] = None) -> 'AccessServiceToken':
        """
        Get an existing AccessServiceToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The ID of the account where the Access Service is being created. Conflicts with `zone_id`.
        :param pulumi.Input[str] client_id: UUID client ID associated with the Service Token.
        :param pulumi.Input[str] client_secret: A secret for interacting with Access protocols.
        :param pulumi.Input[str] name: Friendly name of the token's intent.
        :param pulumi.Input[str] zone_id: The ID of the zone where the Access Service is being created. Conflicts with `account_id`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccessServiceTokenState.__new__(_AccessServiceTokenState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["client_id"] = client_id
        __props__.__dict__["client_secret"] = client_secret
        __props__.__dict__["name"] = name
        __props__.__dict__["zone_id"] = zone_id
        return AccessServiceToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the account where the Access Service is being created. Conflicts with `zone_id`.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Output[str]:
        """
        UUID client ID associated with the Service Token.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> pulumi.Output[str]:
        """
        A secret for interacting with Access protocols.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Friendly name of the token's intent.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="zoneId")
    def zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the zone where the Access Service is being created. Conflicts with `account_id`.
        """
        return pulumi.get(self, "zone_id")

