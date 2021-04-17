# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IntegrationMetricArgs', 'IntegrationMetric']

@pulumi.input_type
class IntegrationMetricArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[int],
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 client_email: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 queue_allowlist: Optional[pulumi.Input[str]] = None,
                 queue_whitelist: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 vhost_allowlist: Optional[pulumi.Input[str]] = None,
                 vhost_whitelist: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IntegrationMetric resource.
        :param pulumi.Input[int] instance_id: Instance identifier
        :param pulumi.Input[str] access_key_id: AWS access key identifier. (Cloudwatch)
        :param pulumi.Input[str] api_key: The API key for the integration service. (Librato)
        :param pulumi.Input[str] client_email: The client email. (Stackdriver)
        :param pulumi.Input[str] email: The email address registred for the integration service. (Librato)
        :param pulumi.Input[str] license_key: The license key registred for the integration service. (New Relic)
        :param pulumi.Input[str] name: The name of metrics integration
        :param pulumi.Input[str] private_key: The private key. (Stackdriver)
        :param pulumi.Input[str] project_id: Project ID. (Stackdriver)
        :param pulumi.Input[str] queue_allowlist: (optional) allowlist using regular expression
        :param pulumi.Input[str] queue_whitelist: **Deprecated**
        :param pulumi.Input[str] region: AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)
        :param pulumi.Input[str] secret_access_key: AWS secret key. (Cloudwatch)
        :param pulumi.Input[str] tags: (optional) tags. E.g. env=prod,region=europe
        :param pulumi.Input[str] vhost_allowlist: (optional) allowlist using regular expression
        :param pulumi.Input[str] vhost_whitelist: **Deprecated**
        """
        pulumi.set(__self__, "instance_id", instance_id)
        if access_key_id is not None:
            pulumi.set(__self__, "access_key_id", access_key_id)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if client_email is not None:
            pulumi.set(__self__, "client_email", client_email)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if license_key is not None:
            pulumi.set(__self__, "license_key", license_key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if queue_allowlist is not None:
            pulumi.set(__self__, "queue_allowlist", queue_allowlist)
        if queue_whitelist is not None:
            warnings.warn("""use queue_allowlist instead""", DeprecationWarning)
            pulumi.log.warn("""queue_whitelist is deprecated: use queue_allowlist instead""")
        if queue_whitelist is not None:
            pulumi.set(__self__, "queue_whitelist", queue_whitelist)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if secret_access_key is not None:
            pulumi.set(__self__, "secret_access_key", secret_access_key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vhost_allowlist is not None:
            pulumi.set(__self__, "vhost_allowlist", vhost_allowlist)
        if vhost_whitelist is not None:
            warnings.warn("""use vhost_allowlist instead""", DeprecationWarning)
            pulumi.log.warn("""vhost_whitelist is deprecated: use vhost_allowlist instead""")
        if vhost_whitelist is not None:
            pulumi.set(__self__, "vhost_whitelist", vhost_whitelist)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[int]:
        """
        Instance identifier
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS access key identifier. (Cloudwatch)
        """
        return pulumi.get(self, "access_key_id")

    @access_key_id.setter
    def access_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key_id", value)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API key for the integration service. (Librato)
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="clientEmail")
    def client_email(self) -> Optional[pulumi.Input[str]]:
        """
        The client email. (Stackdriver)
        """
        return pulumi.get(self, "client_email")

    @client_email.setter
    def client_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_email", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The email address registred for the integration service. (Librato)
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[pulumi.Input[str]]:
        """
        The license key registred for the integration service. (New Relic)
        """
        return pulumi.get(self, "license_key")

    @license_key.setter
    def license_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of metrics integration
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        The private key. (Stackdriver)
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project ID. (Stackdriver)
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="queueAllowlist")
    def queue_allowlist(self) -> Optional[pulumi.Input[str]]:
        """
        (optional) allowlist using regular expression
        """
        return pulumi.get(self, "queue_allowlist")

    @queue_allowlist.setter
    def queue_allowlist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue_allowlist", value)

    @property
    @pulumi.getter(name="queueWhitelist")
    def queue_whitelist(self) -> Optional[pulumi.Input[str]]:
        """
        **Deprecated**
        """
        return pulumi.get(self, "queue_whitelist")

    @queue_whitelist.setter
    def queue_whitelist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue_whitelist", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        AWS secret key. (Cloudwatch)
        """
        return pulumi.get(self, "secret_access_key")

    @secret_access_key.setter
    def secret_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_access_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[str]]:
        """
        (optional) tags. E.g. env=prod,region=europe
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vhostAllowlist")
    def vhost_allowlist(self) -> Optional[pulumi.Input[str]]:
        """
        (optional) allowlist using regular expression
        """
        return pulumi.get(self, "vhost_allowlist")

    @vhost_allowlist.setter
    def vhost_allowlist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vhost_allowlist", value)

    @property
    @pulumi.getter(name="vhostWhitelist")
    def vhost_whitelist(self) -> Optional[pulumi.Input[str]]:
        """
        **Deprecated**
        """
        return pulumi.get(self, "vhost_whitelist")

    @vhost_whitelist.setter
    def vhost_whitelist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vhost_whitelist", value)


@pulumi.input_type
class _IntegrationMetricState:
    def __init__(__self__, *,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 client_email: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 queue_allowlist: Optional[pulumi.Input[str]] = None,
                 queue_whitelist: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 vhost_allowlist: Optional[pulumi.Input[str]] = None,
                 vhost_whitelist: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IntegrationMetric resources.
        :param pulumi.Input[str] access_key_id: AWS access key identifier. (Cloudwatch)
        :param pulumi.Input[str] api_key: The API key for the integration service. (Librato)
        :param pulumi.Input[str] client_email: The client email. (Stackdriver)
        :param pulumi.Input[str] email: The email address registred for the integration service. (Librato)
        :param pulumi.Input[int] instance_id: Instance identifier
        :param pulumi.Input[str] license_key: The license key registred for the integration service. (New Relic)
        :param pulumi.Input[str] name: The name of metrics integration
        :param pulumi.Input[str] private_key: The private key. (Stackdriver)
        :param pulumi.Input[str] project_id: Project ID. (Stackdriver)
        :param pulumi.Input[str] queue_allowlist: (optional) allowlist using regular expression
        :param pulumi.Input[str] queue_whitelist: **Deprecated**
        :param pulumi.Input[str] region: AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)
        :param pulumi.Input[str] secret_access_key: AWS secret key. (Cloudwatch)
        :param pulumi.Input[str] tags: (optional) tags. E.g. env=prod,region=europe
        :param pulumi.Input[str] vhost_allowlist: (optional) allowlist using regular expression
        :param pulumi.Input[str] vhost_whitelist: **Deprecated**
        """
        if access_key_id is not None:
            pulumi.set(__self__, "access_key_id", access_key_id)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if client_email is not None:
            pulumi.set(__self__, "client_email", client_email)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if license_key is not None:
            pulumi.set(__self__, "license_key", license_key)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if queue_allowlist is not None:
            pulumi.set(__self__, "queue_allowlist", queue_allowlist)
        if queue_whitelist is not None:
            warnings.warn("""use queue_allowlist instead""", DeprecationWarning)
            pulumi.log.warn("""queue_whitelist is deprecated: use queue_allowlist instead""")
        if queue_whitelist is not None:
            pulumi.set(__self__, "queue_whitelist", queue_whitelist)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if secret_access_key is not None:
            pulumi.set(__self__, "secret_access_key", secret_access_key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vhost_allowlist is not None:
            pulumi.set(__self__, "vhost_allowlist", vhost_allowlist)
        if vhost_whitelist is not None:
            warnings.warn("""use vhost_allowlist instead""", DeprecationWarning)
            pulumi.log.warn("""vhost_whitelist is deprecated: use vhost_allowlist instead""")
        if vhost_whitelist is not None:
            pulumi.set(__self__, "vhost_whitelist", vhost_whitelist)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS access key identifier. (Cloudwatch)
        """
        return pulumi.get(self, "access_key_id")

    @access_key_id.setter
    def access_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key_id", value)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API key for the integration service. (Librato)
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="clientEmail")
    def client_email(self) -> Optional[pulumi.Input[str]]:
        """
        The client email. (Stackdriver)
        """
        return pulumi.get(self, "client_email")

    @client_email.setter
    def client_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_email", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        The email address registred for the integration service. (Librato)
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[int]]:
        """
        Instance identifier
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[pulumi.Input[str]]:
        """
        The license key registred for the integration service. (New Relic)
        """
        return pulumi.get(self, "license_key")

    @license_key.setter
    def license_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_key", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of metrics integration
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        The private key. (Stackdriver)
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Project ID. (Stackdriver)
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="queueAllowlist")
    def queue_allowlist(self) -> Optional[pulumi.Input[str]]:
        """
        (optional) allowlist using regular expression
        """
        return pulumi.get(self, "queue_allowlist")

    @queue_allowlist.setter
    def queue_allowlist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue_allowlist", value)

    @property
    @pulumi.getter(name="queueWhitelist")
    def queue_whitelist(self) -> Optional[pulumi.Input[str]]:
        """
        **Deprecated**
        """
        return pulumi.get(self, "queue_whitelist")

    @queue_whitelist.setter
    def queue_whitelist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue_whitelist", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        AWS secret key. (Cloudwatch)
        """
        return pulumi.get(self, "secret_access_key")

    @secret_access_key.setter
    def secret_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_access_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[str]]:
        """
        (optional) tags. E.g. env=prod,region=europe
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="vhostAllowlist")
    def vhost_allowlist(self) -> Optional[pulumi.Input[str]]:
        """
        (optional) allowlist using regular expression
        """
        return pulumi.get(self, "vhost_allowlist")

    @vhost_allowlist.setter
    def vhost_allowlist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vhost_allowlist", value)

    @property
    @pulumi.getter(name="vhostWhitelist")
    def vhost_whitelist(self) -> Optional[pulumi.Input[str]]:
        """
        **Deprecated**
        """
        return pulumi.get(self, "vhost_whitelist")

    @vhost_whitelist.setter
    def vhost_whitelist(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vhost_whitelist", value)


class IntegrationMetric(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 client_email: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 queue_allowlist: Optional[pulumi.Input[str]] = None,
                 queue_whitelist: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 vhost_allowlist: Optional[pulumi.Input[str]] = None,
                 vhost_whitelist: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a IntegrationMetric resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key_id: AWS access key identifier. (Cloudwatch)
        :param pulumi.Input[str] api_key: The API key for the integration service. (Librato)
        :param pulumi.Input[str] client_email: The client email. (Stackdriver)
        :param pulumi.Input[str] email: The email address registred for the integration service. (Librato)
        :param pulumi.Input[int] instance_id: Instance identifier
        :param pulumi.Input[str] license_key: The license key registred for the integration service. (New Relic)
        :param pulumi.Input[str] name: The name of metrics integration
        :param pulumi.Input[str] private_key: The private key. (Stackdriver)
        :param pulumi.Input[str] project_id: Project ID. (Stackdriver)
        :param pulumi.Input[str] queue_allowlist: (optional) allowlist using regular expression
        :param pulumi.Input[str] queue_whitelist: **Deprecated**
        :param pulumi.Input[str] region: AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)
        :param pulumi.Input[str] secret_access_key: AWS secret key. (Cloudwatch)
        :param pulumi.Input[str] tags: (optional) tags. E.g. env=prod,region=europe
        :param pulumi.Input[str] vhost_allowlist: (optional) allowlist using regular expression
        :param pulumi.Input[str] vhost_whitelist: **Deprecated**
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationMetricArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a IntegrationMetric resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param IntegrationMetricArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationMetricArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 client_email: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 queue_allowlist: Optional[pulumi.Input[str]] = None,
                 queue_whitelist: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 vhost_allowlist: Optional[pulumi.Input[str]] = None,
                 vhost_whitelist: Optional[pulumi.Input[str]] = None,
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
            __props__ = IntegrationMetricArgs.__new__(IntegrationMetricArgs)

            __props__.__dict__["access_key_id"] = access_key_id
            __props__.__dict__["api_key"] = api_key
            __props__.__dict__["client_email"] = client_email
            __props__.__dict__["email"] = email
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["license_key"] = license_key
            __props__.__dict__["name"] = name
            __props__.__dict__["private_key"] = private_key
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["queue_allowlist"] = queue_allowlist
            if queue_whitelist is not None and not opts.urn:
                warnings.warn("""use queue_allowlist instead""", DeprecationWarning)
                pulumi.log.warn("""queue_whitelist is deprecated: use queue_allowlist instead""")
            __props__.__dict__["queue_whitelist"] = queue_whitelist
            __props__.__dict__["region"] = region
            __props__.__dict__["secret_access_key"] = secret_access_key
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vhost_allowlist"] = vhost_allowlist
            if vhost_whitelist is not None and not opts.urn:
                warnings.warn("""use vhost_allowlist instead""", DeprecationWarning)
                pulumi.log.warn("""vhost_whitelist is deprecated: use vhost_allowlist instead""")
            __props__.__dict__["vhost_whitelist"] = vhost_whitelist
        super(IntegrationMetric, __self__).__init__(
            'cloudamqp:index/integrationMetric:IntegrationMetric',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_key_id: Optional[pulumi.Input[str]] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            client_email: Optional[pulumi.Input[str]] = None,
            email: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[int]] = None,
            license_key: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            queue_allowlist: Optional[pulumi.Input[str]] = None,
            queue_whitelist: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            secret_access_key: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[str]] = None,
            vhost_allowlist: Optional[pulumi.Input[str]] = None,
            vhost_whitelist: Optional[pulumi.Input[str]] = None) -> 'IntegrationMetric':
        """
        Get an existing IntegrationMetric resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key_id: AWS access key identifier. (Cloudwatch)
        :param pulumi.Input[str] api_key: The API key for the integration service. (Librato)
        :param pulumi.Input[str] client_email: The client email. (Stackdriver)
        :param pulumi.Input[str] email: The email address registred for the integration service. (Librato)
        :param pulumi.Input[int] instance_id: Instance identifier
        :param pulumi.Input[str] license_key: The license key registred for the integration service. (New Relic)
        :param pulumi.Input[str] name: The name of metrics integration
        :param pulumi.Input[str] private_key: The private key. (Stackdriver)
        :param pulumi.Input[str] project_id: Project ID. (Stackdriver)
        :param pulumi.Input[str] queue_allowlist: (optional) allowlist using regular expression
        :param pulumi.Input[str] queue_whitelist: **Deprecated**
        :param pulumi.Input[str] region: AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)
        :param pulumi.Input[str] secret_access_key: AWS secret key. (Cloudwatch)
        :param pulumi.Input[str] tags: (optional) tags. E.g. env=prod,region=europe
        :param pulumi.Input[str] vhost_allowlist: (optional) allowlist using regular expression
        :param pulumi.Input[str] vhost_whitelist: **Deprecated**
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationMetricState.__new__(_IntegrationMetricState)

        __props__.__dict__["access_key_id"] = access_key_id
        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["client_email"] = client_email
        __props__.__dict__["email"] = email
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["license_key"] = license_key
        __props__.__dict__["name"] = name
        __props__.__dict__["private_key"] = private_key
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["queue_allowlist"] = queue_allowlist
        __props__.__dict__["queue_whitelist"] = queue_whitelist
        __props__.__dict__["region"] = region
        __props__.__dict__["secret_access_key"] = secret_access_key
        __props__.__dict__["tags"] = tags
        __props__.__dict__["vhost_allowlist"] = vhost_allowlist
        __props__.__dict__["vhost_whitelist"] = vhost_whitelist
        return IntegrationMetric(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        AWS access key identifier. (Cloudwatch)
        """
        return pulumi.get(self, "access_key_id")

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        """
        The API key for the integration service. (Librato)
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="clientEmail")
    def client_email(self) -> pulumi.Output[Optional[str]]:
        """
        The client email. (Stackdriver)
        """
        return pulumi.get(self, "client_email")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[Optional[str]]:
        """
        The email address registred for the integration service. (Librato)
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[int]:
        """
        Instance identifier
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> pulumi.Output[Optional[str]]:
        """
        The license key registred for the integration service. (New Relic)
        """
        return pulumi.get(self, "license_key")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of metrics integration
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[Optional[str]]:
        """
        The private key. (Stackdriver)
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[Optional[str]]:
        """
        Project ID. (Stackdriver)
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="queueAllowlist")
    def queue_allowlist(self) -> pulumi.Output[Optional[str]]:
        """
        (optional) allowlist using regular expression
        """
        return pulumi.get(self, "queue_allowlist")

    @property
    @pulumi.getter(name="queueWhitelist")
    def queue_whitelist(self) -> pulumi.Output[Optional[str]]:
        """
        **Deprecated**
        """
        return pulumi.get(self, "queue_whitelist")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> pulumi.Output[Optional[str]]:
        """
        AWS secret key. (Cloudwatch)
        """
        return pulumi.get(self, "secret_access_key")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[str]]:
        """
        (optional) tags. E.g. env=prod,region=europe
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="vhostAllowlist")
    def vhost_allowlist(self) -> pulumi.Output[Optional[str]]:
        """
        (optional) allowlist using regular expression
        """
        return pulumi.get(self, "vhost_allowlist")

    @property
    @pulumi.getter(name="vhostWhitelist")
    def vhost_whitelist(self) -> pulumi.Output[Optional[str]]:
        """
        **Deprecated**
        """
        return pulumi.get(self, "vhost_whitelist")

