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

__all__ = ['KeyPrefixArgs', 'KeyPrefix']

@pulumi.input_type
class KeyPrefixArgs:
    def __init__(__self__, *,
                 path_prefix: pulumi.Input[str],
                 datacenter: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 subkey_collection: Optional[pulumi.Input[Sequence[pulumi.Input['KeyPrefixSubkeyCollectionArgs']]]] = None,
                 subkeys: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KeyPrefix resource.
        :param pulumi.Input[str] path_prefix: Specifies the common prefix shared by all keys
               that will be managed by this resource instance. In most cases this will
               end with a slash, to manage a "folder" of keys.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[str] namespace: The namespace to create the keys within.
        :param pulumi.Input[Sequence[pulumi.Input['KeyPrefixSubkeyCollectionArgs']]] subkey_collection: A subkey to add. Supported values documented below.
               Multiple blocks supported.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] subkeys: A mapping from subkey name (which will be appended
               to the given `path_prefix`) to the value that should be stored at that key.
               Use slashes, as shown in the above example, to create "sub-folders" under
               the given path prefix.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        """
        pulumi.set(__self__, "path_prefix", path_prefix)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if subkey_collection is not None:
            pulumi.set(__self__, "subkey_collection", subkey_collection)
        if subkeys is not None:
            pulumi.set(__self__, "subkeys", subkeys)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="pathPrefix")
    def path_prefix(self) -> pulumi.Input[str]:
        """
        Specifies the common prefix shared by all keys
        that will be managed by this resource instance. In most cases this will
        end with a slash, to manage a "folder" of keys.
        """
        return pulumi.get(self, "path_prefix")

    @path_prefix.setter
    def path_prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "path_prefix", value)

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
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the keys within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="subkeyCollection")
    def subkey_collection(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KeyPrefixSubkeyCollectionArgs']]]]:
        """
        A subkey to add. Supported values documented below.
        Multiple blocks supported.
        """
        return pulumi.get(self, "subkey_collection")

    @subkey_collection.setter
    def subkey_collection(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KeyPrefixSubkeyCollectionArgs']]]]):
        pulumi.set(self, "subkey_collection", value)

    @property
    @pulumi.getter
    def subkeys(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping from subkey name (which will be appended
        to the given `path_prefix`) to the value that should be stored at that key.
        Use slashes, as shown in the above example, to create "sub-folders" under
        the given path prefix.
        """
        return pulumi.get(self, "subkeys")

    @subkeys.setter
    def subkeys(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "subkeys", value)

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
class _KeyPrefixState:
    def __init__(__self__, *,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 path_prefix: Optional[pulumi.Input[str]] = None,
                 subkey_collection: Optional[pulumi.Input[Sequence[pulumi.Input['KeyPrefixSubkeyCollectionArgs']]]] = None,
                 subkeys: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering KeyPrefix resources.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[str] namespace: The namespace to create the keys within.
        :param pulumi.Input[str] path_prefix: Specifies the common prefix shared by all keys
               that will be managed by this resource instance. In most cases this will
               end with a slash, to manage a "folder" of keys.
        :param pulumi.Input[Sequence[pulumi.Input['KeyPrefixSubkeyCollectionArgs']]] subkey_collection: A subkey to add. Supported values documented below.
               Multiple blocks supported.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] subkeys: A mapping from subkey name (which will be appended
               to the given `path_prefix`) to the value that should be stored at that key.
               Use slashes, as shown in the above example, to create "sub-folders" under
               the given path prefix.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        """
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if path_prefix is not None:
            pulumi.set(__self__, "path_prefix", path_prefix)
        if subkey_collection is not None:
            pulumi.set(__self__, "subkey_collection", subkey_collection)
        if subkeys is not None:
            pulumi.set(__self__, "subkeys", subkeys)
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
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the keys within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="pathPrefix")
    def path_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the common prefix shared by all keys
        that will be managed by this resource instance. In most cases this will
        end with a slash, to manage a "folder" of keys.
        """
        return pulumi.get(self, "path_prefix")

    @path_prefix.setter
    def path_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path_prefix", value)

    @property
    @pulumi.getter(name="subkeyCollection")
    def subkey_collection(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['KeyPrefixSubkeyCollectionArgs']]]]:
        """
        A subkey to add. Supported values documented below.
        Multiple blocks supported.
        """
        return pulumi.get(self, "subkey_collection")

    @subkey_collection.setter
    def subkey_collection(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['KeyPrefixSubkeyCollectionArgs']]]]):
        pulumi.set(self, "subkey_collection", value)

    @property
    @pulumi.getter
    def subkeys(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A mapping from subkey name (which will be appended
        to the given `path_prefix`) to the value that should be stored at that key.
        Use slashes, as shown in the above example, to create "sub-folders" under
        the given path prefix.
        """
        return pulumi.get(self, "subkeys")

    @subkeys.setter
    def subkeys(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "subkeys", value)

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


class KeyPrefix(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 path_prefix: Optional[pulumi.Input[str]] = None,
                 subkey_collection: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyPrefixSubkeyCollectionArgs']]]]] = None,
                 subkeys: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        `consul_key_prefix` can be imported. This is useful when the path already and you know all keys in path must be removed.

        ```sh
         $ pulumi import consul:index/keyPrefix:KeyPrefix myapp_config myapp/config/
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[str] namespace: The namespace to create the keys within.
        :param pulumi.Input[str] path_prefix: Specifies the common prefix shared by all keys
               that will be managed by this resource instance. In most cases this will
               end with a slash, to manage a "folder" of keys.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyPrefixSubkeyCollectionArgs']]]] subkey_collection: A subkey to add. Supported values documented below.
               Multiple blocks supported.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] subkeys: A mapping from subkey name (which will be appended
               to the given `path_prefix`) to the value that should be stored at that key.
               Use slashes, as shown in the above example, to create "sub-folders" under
               the given path prefix.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KeyPrefixArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        `consul_key_prefix` can be imported. This is useful when the path already and you know all keys in path must be removed.

        ```sh
         $ pulumi import consul:index/keyPrefix:KeyPrefix myapp_config myapp/config/
        ```

        :param str resource_name: The name of the resource.
        :param KeyPrefixArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyPrefixArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 path_prefix: Optional[pulumi.Input[str]] = None,
                 subkey_collection: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyPrefixSubkeyCollectionArgs']]]]] = None,
                 subkeys: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = KeyPrefixArgs.__new__(KeyPrefixArgs)

            __props__.__dict__["datacenter"] = datacenter
            __props__.__dict__["namespace"] = namespace
            if path_prefix is None and not opts.urn:
                raise TypeError("Missing required property 'path_prefix'")
            __props__.__dict__["path_prefix"] = path_prefix
            __props__.__dict__["subkey_collection"] = subkey_collection
            __props__.__dict__["subkeys"] = subkeys
            __props__.__dict__["token"] = token
        super(KeyPrefix, __self__).__init__(
            'consul:index/keyPrefix:KeyPrefix',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            path_prefix: Optional[pulumi.Input[str]] = None,
            subkey_collection: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyPrefixSubkeyCollectionArgs']]]]] = None,
            subkeys: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            token: Optional[pulumi.Input[str]] = None) -> 'KeyPrefix':
        """
        Get an existing KeyPrefix resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] datacenter: The datacenter to use. This overrides the
               agent's default datacenter and the datacenter in the provider setup.
        :param pulumi.Input[str] namespace: The namespace to create the keys within.
        :param pulumi.Input[str] path_prefix: Specifies the common prefix shared by all keys
               that will be managed by this resource instance. In most cases this will
               end with a slash, to manage a "folder" of keys.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['KeyPrefixSubkeyCollectionArgs']]]] subkey_collection: A subkey to add. Supported values documented below.
               Multiple blocks supported.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] subkeys: A mapping from subkey name (which will be appended
               to the given `path_prefix`) to the value that should be stored at that key.
               Use slashes, as shown in the above example, to create "sub-folders" under
               the given path prefix.
        :param pulumi.Input[str] token: The ACL token to use. This overrides the
               token that the agent provides by default.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KeyPrefixState.__new__(_KeyPrefixState)

        __props__.__dict__["datacenter"] = datacenter
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["path_prefix"] = path_prefix
        __props__.__dict__["subkey_collection"] = subkey_collection
        __props__.__dict__["subkeys"] = subkeys
        __props__.__dict__["token"] = token
        return KeyPrefix(resource_name, opts=opts, __props__=__props__)

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
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace to create the keys within.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="pathPrefix")
    def path_prefix(self) -> pulumi.Output[str]:
        """
        Specifies the common prefix shared by all keys
        that will be managed by this resource instance. In most cases this will
        end with a slash, to manage a "folder" of keys.
        """
        return pulumi.get(self, "path_prefix")

    @property
    @pulumi.getter(name="subkeyCollection")
    def subkey_collection(self) -> pulumi.Output[Optional[Sequence['outputs.KeyPrefixSubkeyCollection']]]:
        """
        A subkey to add. Supported values documented below.
        Multiple blocks supported.
        """
        return pulumi.get(self, "subkey_collection")

    @property
    @pulumi.getter
    def subkeys(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A mapping from subkey name (which will be appended
        to the given `path_prefix`) to the value that should be stored at that key.
        Use slashes, as shown in the above example, to create "sub-folders" under
        the given path prefix.
        """
        return pulumi.get(self, "subkeys")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[str]]:
        """
        The ACL token to use. This overrides the
        token that the agent provides by default.
        """
        return pulumi.get(self, "token")

