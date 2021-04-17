# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CertificateArgs', 'Certificate']

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 cert: pulumi.Input[str],
                 key: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Certificate resource.
        :param pulumi.Input[str] cert: Cert of the Certificate in which the Certificate will add.
        :param pulumi.Input[str] key: Key of the Certificate in which the Certificate will add.
        :param pulumi.Input[str] name: Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        """
        pulumi.set(__self__, "cert", cert)
        pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def cert(self) -> pulumi.Input[str]:
        """
        Cert of the Certificate in which the Certificate will add.
        """
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: pulumi.Input[str]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Key of the Certificate in which the Certificate will add.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _CertificateState:
    def __init__(__self__, *,
                 cert: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Certificate resources.
        :param pulumi.Input[str] cert: Cert of the Certificate in which the Certificate will add.
        :param pulumi.Input[str] key: Key of the Certificate in which the Certificate will add.
        :param pulumi.Input[str] name: Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        """
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[str]]:
        """
        Cert of the Certificate in which the Certificate will add.
        """
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Key of the Certificate in which the Certificate will add.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class Certificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cert: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a CAS Certificate resource.

        > **NOTE:** The Certificate name which you want to add must be already registered and had not added by another account. Every Certificate name can only exist in a unique group.

        > **NOTE:** The Cas Certificate region only support cn-hangzhou, ap-south-1, me-east-1, eu-central-1, ap-northeast-1, ap-southeast-2.

        > **NOTE:** Available in 1.35.0+ .

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Add a new Certificate.
        cert = alicloud.cas.Certificate("cert",
            cert=(lambda path: open(path).read())(f"{path['module']}/test.crt"),
            key=(lambda path: open(path).read())(f"{path['module']}/test.key"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cert: Cert of the Certificate in which the Certificate will add.
        :param pulumi.Input[str] key: Key of the Certificate in which the Certificate will add.
        :param pulumi.Input[str] name: Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a CAS Certificate resource.

        > **NOTE:** The Certificate name which you want to add must be already registered and had not added by another account. Every Certificate name can only exist in a unique group.

        > **NOTE:** The Cas Certificate region only support cn-hangzhou, ap-south-1, me-east-1, eu-central-1, ap-northeast-1, ap-southeast-2.

        > **NOTE:** Available in 1.35.0+ .

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Add a new Certificate.
        cert = alicloud.cas.Certificate("cert",
            cert=(lambda path: open(path).read())(f"{path['module']}/test.crt"),
            key=(lambda path: open(path).read())(f"{path['module']}/test.key"))
        ```

        :param str resource_name: The name of the resource.
        :param CertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cert: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = CertificateArgs.__new__(CertificateArgs)

            if cert is None and not opts.urn:
                raise TypeError("Missing required property 'cert'")
            __props__.__dict__["cert"] = cert
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["name"] = name
        super(Certificate, __self__).__init__(
            'alicloud:cas/certificate:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cert: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None) -> 'Certificate':
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cert: Cert of the Certificate in which the Certificate will add.
        :param pulumi.Input[str] key: Key of the Certificate in which the Certificate will add.
        :param pulumi.Input[str] name: Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CertificateState.__new__(_CertificateState)

        __props__.__dict__["cert"] = cert
        __props__.__dict__["key"] = key
        __props__.__dict__["name"] = name
        return Certificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cert(self) -> pulumi.Output[str]:
        """
        Cert of the Certificate in which the Certificate will add.
        """
        return pulumi.get(self, "cert")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        Key of the Certificate in which the Certificate will add.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Certificate. This name without suffix can have a string of 1 to 63 characters, must contain only alphanumeric characters or "-", and must not begin or end with "-", and "-" must not in the 3th and 4th character positions at the same time. Suffix `.sh` and `.tel` are not supported.
        """
        return pulumi.get(self, "name")

