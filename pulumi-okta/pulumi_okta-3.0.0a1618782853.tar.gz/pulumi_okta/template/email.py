# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['EmailArgs', 'Email']

@pulumi.input_type
class EmailArgs:
    def __init__(__self__, *,
                 translations: pulumi.Input[Sequence[pulumi.Input['EmailTranslationArgs']]],
                 type: pulumi.Input[str],
                 default_language: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Email resource.
        :param pulumi.Input[Sequence[pulumi.Input['EmailTranslationArgs']]] translations: Set of translations for a particular template.
        :param pulumi.Input[str] type: Email template type
        :param pulumi.Input[str] default_language: The default language, by default is set to `"en"`.
        """
        pulumi.set(__self__, "translations", translations)
        pulumi.set(__self__, "type", type)
        if default_language is not None:
            pulumi.set(__self__, "default_language", default_language)

    @property
    @pulumi.getter
    def translations(self) -> pulumi.Input[Sequence[pulumi.Input['EmailTranslationArgs']]]:
        """
        Set of translations for a particular template.
        """
        return pulumi.get(self, "translations")

    @translations.setter
    def translations(self, value: pulumi.Input[Sequence[pulumi.Input['EmailTranslationArgs']]]):
        pulumi.set(self, "translations", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Email template type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="defaultLanguage")
    def default_language(self) -> Optional[pulumi.Input[str]]:
        """
        The default language, by default is set to `"en"`.
        """
        return pulumi.get(self, "default_language")

    @default_language.setter
    def default_language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_language", value)


@pulumi.input_type
class _EmailState:
    def __init__(__self__, *,
                 default_language: Optional[pulumi.Input[str]] = None,
                 translations: Optional[pulumi.Input[Sequence[pulumi.Input['EmailTranslationArgs']]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Email resources.
        :param pulumi.Input[str] default_language: The default language, by default is set to `"en"`.
        :param pulumi.Input[Sequence[pulumi.Input['EmailTranslationArgs']]] translations: Set of translations for a particular template.
        :param pulumi.Input[str] type: Email template type
        """
        if default_language is not None:
            pulumi.set(__self__, "default_language", default_language)
        if translations is not None:
            pulumi.set(__self__, "translations", translations)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="defaultLanguage")
    def default_language(self) -> Optional[pulumi.Input[str]]:
        """
        The default language, by default is set to `"en"`.
        """
        return pulumi.get(self, "default_language")

    @default_language.setter
    def default_language(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_language", value)

    @property
    @pulumi.getter
    def translations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EmailTranslationArgs']]]]:
        """
        Set of translations for a particular template.
        """
        return pulumi.get(self, "translations")

    @translations.setter
    def translations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EmailTranslationArgs']]]]):
        pulumi.set(self, "translations", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Email template type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Email(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_language: Optional[pulumi.Input[str]] = None,
                 translations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailTranslationArgs']]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates an Okta Email Template.

        This resource allows you to create and configure an Okta Email Template.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.template.Email("example",
            translations=[
                okta.template.EmailTranslationArgs(
                    language="en",
                    subject="Stuff",
                    template=f"Hi {user['firstName']},<br/><br/>Blah blah {reset_password_link}",
                ),
                okta.template.EmailTranslationArgs(
                    language="es",
                    subject="Cosas",
                    template=f"Hola {user['firstName']},<br/><br/>Puedo ir al bano {reset_password_link}",
                ),
            ],
            type="email.forgotPassword")
        ```

        ## Import

        An Okta Email Template can be imported via the template type.

        ```sh
         $ pulumi import okta:template/email:Email example <template type>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_language: The default language, by default is set to `"en"`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailTranslationArgs']]]] translations: Set of translations for a particular template.
        :param pulumi.Input[str] type: Email template type
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EmailArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an Okta Email Template.

        This resource allows you to create and configure an Okta Email Template.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_okta as okta

        example = okta.template.Email("example",
            translations=[
                okta.template.EmailTranslationArgs(
                    language="en",
                    subject="Stuff",
                    template=f"Hi {user['firstName']},<br/><br/>Blah blah {reset_password_link}",
                ),
                okta.template.EmailTranslationArgs(
                    language="es",
                    subject="Cosas",
                    template=f"Hola {user['firstName']},<br/><br/>Puedo ir al bano {reset_password_link}",
                ),
            ],
            type="email.forgotPassword")
        ```

        ## Import

        An Okta Email Template can be imported via the template type.

        ```sh
         $ pulumi import okta:template/email:Email example <template type>
        ```

        :param str resource_name: The name of the resource.
        :param EmailArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EmailArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_language: Optional[pulumi.Input[str]] = None,
                 translations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailTranslationArgs']]]]] = None,
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
            __props__ = EmailArgs.__new__(EmailArgs)

            __props__.__dict__["default_language"] = default_language
            if translations is None and not opts.urn:
                raise TypeError("Missing required property 'translations'")
            __props__.__dict__["translations"] = translations
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(Email, __self__).__init__(
            'okta:template/email:Email',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_language: Optional[pulumi.Input[str]] = None,
            translations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailTranslationArgs']]]]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Email':
        """
        Get an existing Email resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_language: The default language, by default is set to `"en"`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['EmailTranslationArgs']]]] translations: Set of translations for a particular template.
        :param pulumi.Input[str] type: Email template type
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EmailState.__new__(_EmailState)

        __props__.__dict__["default_language"] = default_language
        __props__.__dict__["translations"] = translations
        __props__.__dict__["type"] = type
        return Email(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultLanguage")
    def default_language(self) -> pulumi.Output[Optional[str]]:
        """
        The default language, by default is set to `"en"`.
        """
        return pulumi.get(self, "default_language")

    @property
    @pulumi.getter
    def translations(self) -> pulumi.Output[Sequence['outputs.EmailTranslation']]:
        """
        Set of translations for a particular template.
        """
        return pulumi.get(self, "translations")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Email template type
        """
        return pulumi.get(self, "type")

