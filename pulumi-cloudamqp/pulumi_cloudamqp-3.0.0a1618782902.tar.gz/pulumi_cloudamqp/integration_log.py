# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['IntegrationLogArgs', 'IntegrationLog']

@pulumi.input_type
class IntegrationLogArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[int],
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 client_email: Optional[pulumi.Input[str]] = None,
                 host_port: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IntegrationLog resource.
        :param pulumi.Input[int] instance_id: Instance identifier used to make proxy calls
        :param pulumi.Input[str] access_key_id: AWS access key identifier.
        :param pulumi.Input[str] api_key: The API key.
        :param pulumi.Input[str] client_email: The client email registered for the integration service.
        :param pulumi.Input[str] host_port: Destination to send the logs.
        :param pulumi.Input[str] name: The name of the third party log integration. See
        :param pulumi.Input[str] private_key: The private access key.
        :param pulumi.Input[str] project_id: The project identifier.
        :param pulumi.Input[str] region: Region hosting the integration service.
        :param pulumi.Input[str] secret_access_key: AWS secret access key.
        :param pulumi.Input[str] tags: Tag the integration, e.g. env=prod, region=europe.
        :param pulumi.Input[str] token: Token used for authentication.
        :param pulumi.Input[str] url: Endpoint to log integration.
        """
        pulumi.set(__self__, "instance_id", instance_id)
        if access_key_id is not None:
            pulumi.set(__self__, "access_key_id", access_key_id)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if client_email is not None:
            pulumi.set(__self__, "client_email", client_email)
        if host_port is not None:
            pulumi.set(__self__, "host_port", host_port)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if secret_access_key is not None:
            pulumi.set(__self__, "secret_access_key", secret_access_key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[int]:
        """
        Instance identifier used to make proxy calls
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS access key identifier.
        """
        return pulumi.get(self, "access_key_id")

    @access_key_id.setter
    def access_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key_id", value)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API key.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="clientEmail")
    def client_email(self) -> Optional[pulumi.Input[str]]:
        """
        The client email registered for the integration service.
        """
        return pulumi.get(self, "client_email")

    @client_email.setter
    def client_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_email", value)

    @property
    @pulumi.getter(name="hostPort")
    def host_port(self) -> Optional[pulumi.Input[str]]:
        """
        Destination to send the logs.
        """
        return pulumi.get(self, "host_port")

    @host_port.setter
    def host_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_port", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the third party log integration. See
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        The private access key.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project identifier.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region hosting the integration service.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        AWS secret access key.
        """
        return pulumi.get(self, "secret_access_key")

    @secret_access_key.setter
    def secret_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_access_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[str]]:
        """
        Tag the integration, e.g. env=prod, region=europe.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        Token used for authentication.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        Endpoint to log integration.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


@pulumi.input_type
class _IntegrationLogState:
    def __init__(__self__, *,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 client_email: Optional[pulumi.Input[str]] = None,
                 host_port: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IntegrationLog resources.
        :param pulumi.Input[str] access_key_id: AWS access key identifier.
        :param pulumi.Input[str] api_key: The API key.
        :param pulumi.Input[str] client_email: The client email registered for the integration service.
        :param pulumi.Input[str] host_port: Destination to send the logs.
        :param pulumi.Input[int] instance_id: Instance identifier used to make proxy calls
        :param pulumi.Input[str] name: The name of the third party log integration. See
        :param pulumi.Input[str] private_key: The private access key.
        :param pulumi.Input[str] project_id: The project identifier.
        :param pulumi.Input[str] region: Region hosting the integration service.
        :param pulumi.Input[str] secret_access_key: AWS secret access key.
        :param pulumi.Input[str] tags: Tag the integration, e.g. env=prod, region=europe.
        :param pulumi.Input[str] token: Token used for authentication.
        :param pulumi.Input[str] url: Endpoint to log integration.
        """
        if access_key_id is not None:
            pulumi.set(__self__, "access_key_id", access_key_id)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if client_email is not None:
            pulumi.set(__self__, "client_email", client_email)
        if host_port is not None:
            pulumi.set(__self__, "host_port", host_port)
        if instance_id is not None:
            pulumi.set(__self__, "instance_id", instance_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if secret_access_key is not None:
            pulumi.set(__self__, "secret_access_key", secret_access_key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS access key identifier.
        """
        return pulumi.get(self, "access_key_id")

    @access_key_id.setter
    def access_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "access_key_id", value)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API key.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="clientEmail")
    def client_email(self) -> Optional[pulumi.Input[str]]:
        """
        The client email registered for the integration service.
        """
        return pulumi.get(self, "client_email")

    @client_email.setter
    def client_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_email", value)

    @property
    @pulumi.getter(name="hostPort")
    def host_port(self) -> Optional[pulumi.Input[str]]:
        """
        Destination to send the logs.
        """
        return pulumi.get(self, "host_port")

    @host_port.setter
    def host_port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host_port", value)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[pulumi.Input[int]]:
        """
        Instance identifier used to make proxy calls
        """
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the third party log integration. See
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        The private access key.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The project identifier.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Region hosting the integration service.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> Optional[pulumi.Input[str]]:
        """
        AWS secret access key.
        """
        return pulumi.get(self, "secret_access_key")

    @secret_access_key.setter
    def secret_access_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret_access_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[str]]:
        """
        Tag the integration, e.g. env=prod, region=europe.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        Token used for authentication.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        Endpoint to log integration.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class IntegrationLog(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_key_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 client_email: Optional[pulumi.Input[str]] = None,
                 host_port: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resource allows you to create and manage third party log integrations for a CloudAMQP instance. Once configured, the logs produced will be forward to corresponding integration.

        Only available for dedicated subscription plans.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudamqp as cloudamqp

        cloudwatch = cloudamqp.IntegrationLog("cloudwatch",
            instance_id=cloudamqp_instance["instance"]["id"],
            access_key_id=var["aws_access_key_id"],
            secret_access_key=var["aws_secret_access_key"],
            region=var["aws_region"])
        logentries = cloudamqp.IntegrationLog("logentries",
            instance_id=cloudamqp_instance["instance"]["id"],
            token=var["logentries_token"])
        loggly = cloudamqp.IntegrationLog("loggly",
            instance_id=cloudamqp_instance["instance"]["id"],
            token=var["loggly_token"])
        papertrail = cloudamqp.IntegrationLog("papertrail",
            instance_id=cloudamqp_instance["instance"]["id"],
            url=var["papertrail_url"])
        splunk = cloudamqp.IntegrationLog("splunk",
            instance_id=cloudamqp_instance["instance"]["id"],
            token=var["splunk_token"],
            host_port=var["splunk_host_port"])
        datadog = cloudamqp.IntegrationLog("datadog",
            instance_id=cloudamqp_instance["instance"]["id"],
            region=var["datadog_region"],
            api_key=var["datadog_api_key"],
            tags=var["datadog_tags"])
        stackdriver = cloudamqp.IntegrationLog("stackdriver",
            instance_id=cloudamqp_instance["instance"]["id"],
            project_id=var["stackdriver_project_id"],
            private_key=var["stackdriver_private_key"],
            client_email=var["stackdriver_client_email"])
        ```
        ## Argument Reference (cloudwatchlog)

        Cloudwatch argument reference and example. Create an IAM user with programmatic access and the following permissions:

        * CreateLogGroup
        * CreateLogStream
        * DescribeLogGroups
        * DescribeLogStreams
        * PutLogEvents

        ## Integration service reference

        Valid names for third party log integration.

        | Name       | Description |
        |------------|---------------------------------------------------------------|
        | cloudwatchlog | Create a IAM with programmatic access. |
        | logentries | Create a Logentries token at https://logentries.com/app#/add-log/manual  |
        | loggly     | Create a Loggly token at https://{your-company}.loggly.com/tokens |
        | papertrail | Create a Papertrail endpoint https://papertrailapp.com/systems/setup |
        | splunk     | Create a HTTP Event Collector token at https://.cloud.splunk.com/en-US/manager/search/http-eventcollector |
        | datadog       | Create a Datadog API key at app.datadoghq.com |
        | stackdriver   | Create a service account and add 'monitor metrics writer' role, then download credentials. |

        ## Integration Type reference

        Valid arguments for third party log integrations.

        Required arguments for all integrations: name

        | Name | Type | Required arguments |
        | ---- | ---- | ---- |
        | CloudWatch | cloudwatchlog | access_key_id, secret_access_key, region |
        | Log Entries | logentries | token |
        | Loggly | loggly | token |
        | Papertrail | papertrail | url |
        | Splunk | splunk | token, host_port |
        | Data Dog | datadog | region, api_keys, tags |
        | Stackdriver | stackdriver | project_id, private_key, client_email |

        ## Dependency

        This resource depends on CloudAMQP instance identifier, `cloudamqp_instance.instance.id`.

        ## Import

        `cloudamqp_integration_log`can be imported using the name argument of the resource together with CloudAMQP instance identifier. The name and identifier are CSV separated, see example below.

        ```sh
         $ pulumi import cloudamqp:index/integrationLog:IntegrationLog <resource_name> <name>,<instance_id>`
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key_id: AWS access key identifier.
        :param pulumi.Input[str] api_key: The API key.
        :param pulumi.Input[str] client_email: The client email registered for the integration service.
        :param pulumi.Input[str] host_port: Destination to send the logs.
        :param pulumi.Input[int] instance_id: Instance identifier used to make proxy calls
        :param pulumi.Input[str] name: The name of the third party log integration. See
        :param pulumi.Input[str] private_key: The private access key.
        :param pulumi.Input[str] project_id: The project identifier.
        :param pulumi.Input[str] region: Region hosting the integration service.
        :param pulumi.Input[str] secret_access_key: AWS secret access key.
        :param pulumi.Input[str] tags: Tag the integration, e.g. env=prod, region=europe.
        :param pulumi.Input[str] token: Token used for authentication.
        :param pulumi.Input[str] url: Endpoint to log integration.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationLogArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to create and manage third party log integrations for a CloudAMQP instance. Once configured, the logs produced will be forward to corresponding integration.

        Only available for dedicated subscription plans.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_cloudamqp as cloudamqp

        cloudwatch = cloudamqp.IntegrationLog("cloudwatch",
            instance_id=cloudamqp_instance["instance"]["id"],
            access_key_id=var["aws_access_key_id"],
            secret_access_key=var["aws_secret_access_key"],
            region=var["aws_region"])
        logentries = cloudamqp.IntegrationLog("logentries",
            instance_id=cloudamqp_instance["instance"]["id"],
            token=var["logentries_token"])
        loggly = cloudamqp.IntegrationLog("loggly",
            instance_id=cloudamqp_instance["instance"]["id"],
            token=var["loggly_token"])
        papertrail = cloudamqp.IntegrationLog("papertrail",
            instance_id=cloudamqp_instance["instance"]["id"],
            url=var["papertrail_url"])
        splunk = cloudamqp.IntegrationLog("splunk",
            instance_id=cloudamqp_instance["instance"]["id"],
            token=var["splunk_token"],
            host_port=var["splunk_host_port"])
        datadog = cloudamqp.IntegrationLog("datadog",
            instance_id=cloudamqp_instance["instance"]["id"],
            region=var["datadog_region"],
            api_key=var["datadog_api_key"],
            tags=var["datadog_tags"])
        stackdriver = cloudamqp.IntegrationLog("stackdriver",
            instance_id=cloudamqp_instance["instance"]["id"],
            project_id=var["stackdriver_project_id"],
            private_key=var["stackdriver_private_key"],
            client_email=var["stackdriver_client_email"])
        ```
        ## Argument Reference (cloudwatchlog)

        Cloudwatch argument reference and example. Create an IAM user with programmatic access and the following permissions:

        * CreateLogGroup
        * CreateLogStream
        * DescribeLogGroups
        * DescribeLogStreams
        * PutLogEvents

        ## Integration service reference

        Valid names for third party log integration.

        | Name       | Description |
        |------------|---------------------------------------------------------------|
        | cloudwatchlog | Create a IAM with programmatic access. |
        | logentries | Create a Logentries token at https://logentries.com/app#/add-log/manual  |
        | loggly     | Create a Loggly token at https://{your-company}.loggly.com/tokens |
        | papertrail | Create a Papertrail endpoint https://papertrailapp.com/systems/setup |
        | splunk     | Create a HTTP Event Collector token at https://.cloud.splunk.com/en-US/manager/search/http-eventcollector |
        | datadog       | Create a Datadog API key at app.datadoghq.com |
        | stackdriver   | Create a service account and add 'monitor metrics writer' role, then download credentials. |

        ## Integration Type reference

        Valid arguments for third party log integrations.

        Required arguments for all integrations: name

        | Name | Type | Required arguments |
        | ---- | ---- | ---- |
        | CloudWatch | cloudwatchlog | access_key_id, secret_access_key, region |
        | Log Entries | logentries | token |
        | Loggly | loggly | token |
        | Papertrail | papertrail | url |
        | Splunk | splunk | token, host_port |
        | Data Dog | datadog | region, api_keys, tags |
        | Stackdriver | stackdriver | project_id, private_key, client_email |

        ## Dependency

        This resource depends on CloudAMQP instance identifier, `cloudamqp_instance.instance.id`.

        ## Import

        `cloudamqp_integration_log`can be imported using the name argument of the resource together with CloudAMQP instance identifier. The name and identifier are CSV separated, see example below.

        ```sh
         $ pulumi import cloudamqp:index/integrationLog:IntegrationLog <resource_name> <name>,<instance_id>`
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationLogArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationLogArgs, pulumi.ResourceOptions, *args, **kwargs)
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
                 host_port: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 secret_access_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
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
            __props__ = IntegrationLogArgs.__new__(IntegrationLogArgs)

            __props__.__dict__["access_key_id"] = access_key_id
            __props__.__dict__["api_key"] = api_key
            __props__.__dict__["client_email"] = client_email
            __props__.__dict__["host_port"] = host_port
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["name"] = name
            __props__.__dict__["private_key"] = private_key
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["region"] = region
            __props__.__dict__["secret_access_key"] = secret_access_key
            __props__.__dict__["tags"] = tags
            __props__.__dict__["token"] = token
            __props__.__dict__["url"] = url
        super(IntegrationLog, __self__).__init__(
            'cloudamqp:index/integrationLog:IntegrationLog',
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
            host_port: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            secret_access_key: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'IntegrationLog':
        """
        Get an existing IntegrationLog resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key_id: AWS access key identifier.
        :param pulumi.Input[str] api_key: The API key.
        :param pulumi.Input[str] client_email: The client email registered for the integration service.
        :param pulumi.Input[str] host_port: Destination to send the logs.
        :param pulumi.Input[int] instance_id: Instance identifier used to make proxy calls
        :param pulumi.Input[str] name: The name of the third party log integration. See
        :param pulumi.Input[str] private_key: The private access key.
        :param pulumi.Input[str] project_id: The project identifier.
        :param pulumi.Input[str] region: Region hosting the integration service.
        :param pulumi.Input[str] secret_access_key: AWS secret access key.
        :param pulumi.Input[str] tags: Tag the integration, e.g. env=prod, region=europe.
        :param pulumi.Input[str] token: Token used for authentication.
        :param pulumi.Input[str] url: Endpoint to log integration.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationLogState.__new__(_IntegrationLogState)

        __props__.__dict__["access_key_id"] = access_key_id
        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["client_email"] = client_email
        __props__.__dict__["host_port"] = host_port
        __props__.__dict__["instance_id"] = instance_id
        __props__.__dict__["name"] = name
        __props__.__dict__["private_key"] = private_key
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["region"] = region
        __props__.__dict__["secret_access_key"] = secret_access_key
        __props__.__dict__["tags"] = tags
        __props__.__dict__["token"] = token
        __props__.__dict__["url"] = url
        return IntegrationLog(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKeyId")
    def access_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        AWS access key identifier.
        """
        return pulumi.get(self, "access_key_id")

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        """
        The API key.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="clientEmail")
    def client_email(self) -> pulumi.Output[Optional[str]]:
        """
        The client email registered for the integration service.
        """
        return pulumi.get(self, "client_email")

    @property
    @pulumi.getter(name="hostPort")
    def host_port(self) -> pulumi.Output[Optional[str]]:
        """
        Destination to send the logs.
        """
        return pulumi.get(self, "host_port")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[int]:
        """
        Instance identifier used to make proxy calls
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the third party log integration. See
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[Optional[str]]:
        """
        The private access key.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[Optional[str]]:
        """
        The project identifier.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        Region hosting the integration service.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="secretAccessKey")
    def secret_access_key(self) -> pulumi.Output[Optional[str]]:
        """
        AWS secret access key.
        """
        return pulumi.get(self, "secret_access_key")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[str]]:
        """
        Tag the integration, e.g. env=prod, region=europe.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[str]]:
        """
        Token used for authentication.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        """
        Endpoint to log integration.
        """
        return pulumi.get(self, "url")

