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

__all__ = ['TemplateSmsArgs', 'TemplateSms']

@pulumi.input_type
class TemplateSmsArgs:
    def __init__(__self__, *,
                 template: pulumi.Input[str],
                 type: pulumi.Input[str],
                 translations: Optional[pulumi.Input[Sequence[pulumi.Input['TemplateSmsTranslationArgs']]]] = None):
        """
        The set of arguments for constructing a TemplateSms resource.
        :param pulumi.Input[str] template: The SMS message.
        :param pulumi.Input[str] type: SMS template type
        :param pulumi.Input[Sequence[pulumi.Input['TemplateSmsTranslationArgs']]] translations: Set of translations for a particular template.
        """
        pulumi.set(__self__, "template", template)
        pulumi.set(__self__, "type", type)
        if translations is not None:
            pulumi.set(__self__, "translations", translations)

    @property
    @pulumi.getter
    def template(self) -> pulumi.Input[str]:
        """
        The SMS message.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: pulumi.Input[str]):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        SMS template type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def translations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TemplateSmsTranslationArgs']]]]:
        """
        Set of translations for a particular template.
        """
        return pulumi.get(self, "translations")

    @translations.setter
    def translations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TemplateSmsTranslationArgs']]]]):
        pulumi.set(self, "translations", value)


@pulumi.input_type
class _TemplateSmsState:
    def __init__(__self__, *,
                 template: Optional[pulumi.Input[str]] = None,
                 translations: Optional[pulumi.Input[Sequence[pulumi.Input['TemplateSmsTranslationArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TemplateSms resources.
        :param pulumi.Input[str] template: The SMS message.
        :param pulumi.Input[Sequence[pulumi.Input['TemplateSmsTranslationArgs']]] translations: Set of translations for a particular template.
        :param pulumi.Input[str] type: SMS template type
        """
        if template is not None:
            pulumi.set(__self__, "template", template)
        if translations is not None:
            pulumi.set(__self__, "translations", translations)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def template(self) -> Optional[pulumi.Input[str]]:
        """
        The SMS message.
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter
    def translations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TemplateSmsTranslationArgs']]]]:
        """
        Set of translations for a particular template.
        """
        return pulumi.get(self, "translations")

    @translations.setter
    def translations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TemplateSmsTranslationArgs']]]]):
        pulumi.set(self, "translations", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        SMS template type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class TemplateSms(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 template: Optional[pulumi.Input[str]] = None,
                 translations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TemplateSmsTranslationArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an Okta SMS Template.

        This resource allows you to create and configure an Okta SMS Template.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.TemplateSms("example",
            template=f"Your {org['name']} code is: {code}",
            translations=[
                okta.TemplateSmsTranslationArgs(
                    language="en",
                    template=f"Your {org['name']} code is: {code}",
                ),
                okta.TemplateSmsTranslationArgs(
                    language="es",
                    template=f"Tu código de {org['name']} es: {code}.",
                ),
            ],
            type="SMS_VERIFY_CODE")
        ```

        ## Import

        An Okta SMS Template can be imported via the template type.

        ```sh
         $ pulumi import okta:index/templateSms:TemplateSms example <template type>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] template: The SMS message.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TemplateSmsTranslationArgs']]]] translations: Set of translations for a particular template.
        :param pulumi.Input[str] type: SMS template type
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TemplateSmsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an Okta SMS Template.

        This resource allows you to create and configure an Okta SMS Template.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.TemplateSms("example",
            template=f"Your {org['name']} code is: {code}",
            translations=[
                okta.TemplateSmsTranslationArgs(
                    language="en",
                    template=f"Your {org['name']} code is: {code}",
                ),
                okta.TemplateSmsTranslationArgs(
                    language="es",
                    template=f"Tu código de {org['name']} es: {code}.",
                ),
            ],
            type="SMS_VERIFY_CODE")
        ```

        ## Import

        An Okta SMS Template can be imported via the template type.

        ```sh
         $ pulumi import okta:index/templateSms:TemplateSms example <template type>
        ```

        :param str resource_name: The name of the resource.
        :param TemplateSmsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TemplateSmsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 template: Optional[pulumi.Input[str]] = None,
                 translations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TemplateSmsTranslationArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
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
            __props__ = TemplateSmsArgs.__new__(TemplateSmsArgs)

            if template is None and not opts.urn:
                raise TypeError("Missing required property 'template'")
            __props__.__dict__["template"] = template
            __props__.__dict__["translations"] = translations
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(TemplateSms, __self__).__init__(
            'okta:index/templateSms:TemplateSms',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            template: Optional[pulumi.Input[str]] = None,
            translations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TemplateSmsTranslationArgs']]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'TemplateSms':
        """
        Get an existing TemplateSms resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] template: The SMS message.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TemplateSmsTranslationArgs']]]] translations: Set of translations for a particular template.
        :param pulumi.Input[str] type: SMS template type
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TemplateSmsState.__new__(_TemplateSmsState)

        __props__.__dict__["template"] = template
        __props__.__dict__["translations"] = translations
        __props__.__dict__["type"] = type
        return TemplateSms(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def template(self) -> pulumi.Output[str]:
        """
        The SMS message.
        """
        return pulumi.get(self, "template")

    @property
    @pulumi.getter
    def translations(self) -> pulumi.Output[Optional[Sequence['outputs.TemplateSmsTranslation']]]:
        """
        Set of translations for a particular template.
        """
        return pulumi.get(self, "translations")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        SMS template type
        """
        return pulumi.get(self, "type")

