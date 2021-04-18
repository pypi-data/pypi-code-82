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

__all__ = ['KeysArgs', 'Keys']

@pulumi.input_type
class KeysArgs:
    def __init__(__self__, *,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 keys: Optional[pulumi.Input[Sequence[pulumi.Input['KeysKeyArgs']]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Keys resource.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[Sequence[pulumi.Input['KeysKeyArgs']]] keys: Specifies a key in Consul to be written.
               Supported values documented below.
        :param pulumi.Input[str] namespace: The namespace to create the keys within.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        """
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The datacenter to use. This overrides the
        agent's default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KeysKeyArgs']]]]:
        """
        Specifies a key in Consul to be written.
        Supported values documented below.
        """
        return pulumi.get(self, "keys")

    @keys.setter
    def keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KeysKeyArgs']]]]):
        pulumi.set(self, "keys", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the keys within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The ACL token to use. This overrides the
        token that the agent provides by default.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


@pulumi.input_type
class _KeysState:
    def __init__(__self__, *,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 keys: Optional[pulumi.Input[Sequence[pulumi.Input['KeysKeyArgs']]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 var: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Keys resources.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[Sequence[pulumi.Input['KeysKeyArgs']]] keys: Specifies a key in Consul to be written.
               Supported values documented below.
        :param pulumi.Input[str] namespace: The namespace to create the keys within.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        """
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if var is not None:
            pulumi.set(__self__, "var", var)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The datacenter to use. This overrides the
        agent's default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter
    def keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KeysKeyArgs']]]]:
        """
        Specifies a key in Consul to be written.
        Supported values documented below.
        """
        return pulumi.get(self, "keys")

    @keys.setter
    def keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KeysKeyArgs']]]]):
        pulumi.set(self, "keys", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the keys within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The ACL token to use. This overrides the
        token that the agent provides by default.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def var(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "var")

    @var.setter
    def var(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "var", value)


class Keys(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeysKeyArgs']]]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a Keys resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeysKeyArgs']]]] keys: Specifies a key in Consul to be written.
               Supported values documented below.
        :param pulumi.Input[str] namespace: The namespace to create the keys within.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[KeysArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Keys resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param KeysArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeysArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeysKeyArgs']]]]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
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
            __props__ = KeysArgs.__new__(KeysArgs)

            __props__.__dict__["datacenter"] = datacenter
            __props__.__dict__["keys"] = keys
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["token"] = token
            __props__.__dict__["var"] = None
        super(Keys, __self__).__init__(
            'consul:index/keys:Keys',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeysKeyArgs']]]]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None,
            var: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Keys':
        """
        Get an existing Keys resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeysKeyArgs']]]] keys: Specifies a key in Consul to be written.
               Supported values documented below.
        :param pulumi.Input[str] namespace: The namespace to create the keys within.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KeysState.__new__(_KeysState)

        __props__.__dict__["datacenter"] = datacenter
        __props__.__dict__["keys"] = keys
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["token"] = token
        __props__.__dict__["var"] = var
        return Keys(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def datacenter(self) -> pulumi.Output[str]:
        """
        The datacenter to use. This overrides the
        agent's default datacenter and the datacenter in the provider setup.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter
    def keys(self) -> pulumi.Output[Optional[Sequence['outputs.KeysKey']]]:
        """
        Specifies a key in Consul to be written.
        Supported values documented below.
        """
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace to create the keys within.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[str]]:
        """
        The ACL token to use. This overrides the
        token that the agent provides by default.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def var(self) -> pulumi.Output[Mapping[str, str]]:
        return pulumi.get(self, "var")

