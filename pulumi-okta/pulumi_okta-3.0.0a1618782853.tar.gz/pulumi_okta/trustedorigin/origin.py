# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['OriginArgs', 'Origin']

@pulumi.input_type
class OriginArgs:
    def __init__(__self__, *,
                 origin: pulumi.Input[str],
                 scopes: pulumi.Input[Sequence[pulumi.Input[str]]],
                 active: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Origin resource.
        :param pulumi.Input[str] origin: Unique origin URL for this trusted origin.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes of the Trusted Origin - can be `"CORS"` and/or `"REDIRECT"`.
        :param pulumi.Input[bool] active: Whether the Trusted Origin is active or not - can only be issued post-creation. By default, it is 'true'.
        :param pulumi.Input[str] name: Unique name for this trusted origin.
        """
        pulumi.set(__self__, "origin", origin)
        pulumi.set(__self__, "scopes", scopes)
        if active is not None:
            pulumi.set(__self__, "active", active)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def origin(self) -> pulumi.Input[str]:
        """
        Unique origin URL for this trusted origin.
        """
        return pulumi.get(self, "origin")

    @origin.setter
    def origin(self, value: pulumi.Input[str]):
        pulumi.set(self, "origin", value)

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Scopes of the Trusted Origin - can be `"CORS"` and/or `"REDIRECT"`.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the Trusted Origin is active or not - can only be issued post-creation. By default, it is 'true'.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name for this trusted origin.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _OriginState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 origin: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Origin resources.
        :param pulumi.Input[bool] active: Whether the Trusted Origin is active or not - can only be issued post-creation. By default, it is 'true'.
        :param pulumi.Input[str] name: Unique name for this trusted origin.
        :param pulumi.Input[str] origin: Unique origin URL for this trusted origin.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes of the Trusted Origin - can be `"CORS"` and/or `"REDIRECT"`.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if origin is not None:
            pulumi.set(__self__, "origin", origin)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the Trusted Origin is active or not - can only be issued post-creation. By default, it is 'true'.
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Unique name for this trusted origin.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def origin(self) -> Optional[pulumi.Input[str]]:
        """
        Unique origin URL for this trusted origin.
        """
        return pulumi.get(self, "origin")

    @origin.setter
    def origin(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Scopes of the Trusted Origin - can be `"CORS"` and/or `"REDIRECT"`.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)


class Origin(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 origin: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a Trusted Origin.

        This resource allows you to create and configure a Trusted Origin.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.trustedorigin.Origin("example",
            origin="https://example.com",
            scopes=["CORS"])
        ```

        ## Import

        A Trusted Origin can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:trustedorigin/origin:Origin example <trusted origin id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Whether the Trusted Origin is active or not - can only be issued post-creation. By default, it is 'true'.
        :param pulumi.Input[str] name: Unique name for this trusted origin.
        :param pulumi.Input[str] origin: Unique origin URL for this trusted origin.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes of the Trusted Origin - can be `"CORS"` and/or `"REDIRECT"`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OriginArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Trusted Origin.

        This resource allows you to create and configure a Trusted Origin.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.trustedorigin.Origin("example",
            origin="https://example.com",
            scopes=["CORS"])
        ```

        ## Import

        A Trusted Origin can be imported via the Okta ID.

        ```sh
         $ pulumi import okta:trustedorigin/origin:Origin example <trusted origin id>
        ```

        :param str resource_name: The name of the resource.
        :param OriginArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OriginArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 origin: Optional[pulumi.Input[str]] = None,
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
            __props__ = OriginArgs.__new__(OriginArgs)

            __props__.__dict__["active"] = active
            __props__.__dict__["name"] = name
            if origin is None and not opts.urn:
                raise TypeError("Missing required property 'origin'")
            __props__.__dict__["origin"] = origin
            if scopes is None and not opts.urn:
                raise TypeError("Missing required property 'scopes'")
            __props__.__dict__["scopes"] = scopes
        super(Origin, __self__).__init__(
            'okta:trustedorigin/origin:Origin',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            origin: Optional[pulumi.Input[str]] = None,
            scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None) -> 'Origin':
        """
        Get an existing Origin resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: Whether the Trusted Origin is active or not - can only be issued post-creation. By default, it is 'true'.
        :param pulumi.Input[str] name: Unique name for this trusted origin.
        :param pulumi.Input[str] origin: Unique origin URL for this trusted origin.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: Scopes of the Trusted Origin - can be `"CORS"` and/or `"REDIRECT"`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OriginState.__new__(_OriginState)

        __props__.__dict__["active"] = active
        __props__.__dict__["name"] = name
        __props__.__dict__["origin"] = origin
        __props__.__dict__["scopes"] = scopes
        return Origin(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the Trusted Origin is active or not - can only be issued post-creation. By default, it is 'true'.
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Unique name for this trusted origin.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def origin(self) -> pulumi.Output[str]:
        """
        Unique origin URL for this trusted origin.
        """
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        Scopes of the Trusted Origin - can be `"CORS"` and/or `"REDIRECT"`.
        """
        return pulumi.get(self, "scopes")

