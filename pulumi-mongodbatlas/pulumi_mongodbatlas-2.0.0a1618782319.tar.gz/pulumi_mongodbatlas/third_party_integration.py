# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ThirdPartyIntegrationArgs', 'ThirdPartyIntegration']

@pulumi.input_type
class ThirdPartyIntegrationArgs:
    def __init__(__self__, *,
                 project_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 account_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 flow_name: Optional[pulumi.Input[str]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 org_name: Optional[pulumi.Input[str]] = None,
                 read_token: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 service_key: Optional[pulumi.Input[str]] = None,
                 team_name: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 write_token: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ThirdPartyIntegration resource.
        :param pulumi.Input[str] project_id: The unique ID for the project to get all Third-Party service integrations
        :param pulumi.Input[str] type: Third-Party Integration Settings type 
               * PAGER_DUTY
               * DATADOG
               * NEW_RELIC
               * OPS_GENIE
               * VICTOR_OPS
               * FLOWDOCK
               * WEBHOOK
        :param pulumi.Input[str] account_id: Unique identifier of your New Relic account.
        :param pulumi.Input[str] api_key: Your API Key.
        :param pulumi.Input[str] api_token: Your API Token.
        :param pulumi.Input[str] flow_name: Your Flowdock Flow name.
        :param pulumi.Input[str] license_key: Your License Key.
        :param pulumi.Input[str] org_name: Your Flowdock organization name.
               * `WEBHOOK`
        :param pulumi.Input[str] read_token: Your Insights Query Key.
               * `OPS_GENIE`
        :param pulumi.Input[str] region: Indicates which API URL to use, either US or EU. Opsgenie will use US by default.
               * `VICTOR_OPS`
        :param pulumi.Input[str] routing_key: An optional field for your Routing Key.
               * `FLOWDOCK`
        :param pulumi.Input[str] secret: An optional field for your webhook secret.
        :param pulumi.Input[str] service_key: Your Service Key.
               * `DATADOG`
        :param pulumi.Input[str] url: Your webhook URL.
        :param pulumi.Input[str] write_token: Your Insights Insert Key.
        """
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "type", type)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if api_token is not None:
            pulumi.set(__self__, "api_token", api_token)
        if channel_name is not None:
            pulumi.set(__self__, "channel_name", channel_name)
        if flow_name is not None:
            pulumi.set(__self__, "flow_name", flow_name)
        if license_key is not None:
            pulumi.set(__self__, "license_key", license_key)
        if org_name is not None:
            pulumi.set(__self__, "org_name", org_name)
        if read_token is not None:
            pulumi.set(__self__, "read_token", read_token)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if routing_key is not None:
            pulumi.set(__self__, "routing_key", routing_key)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)
        if service_key is not None:
            pulumi.set(__self__, "service_key", service_key)
        if team_name is not None:
            pulumi.set(__self__, "team_name", team_name)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if write_token is not None:
            pulumi.set(__self__, "write_token", write_token)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Input[str]:
        """
        The unique ID for the project to get all Third-Party service integrations
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Third-Party Integration Settings type 
        * PAGER_DUTY
        * DATADOG
        * NEW_RELIC
        * OPS_GENIE
        * VICTOR_OPS
        * FLOWDOCK
        * WEBHOOK
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of your New Relic account.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        Your API Key.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> Optional[pulumi.Input[str]]:
        """
        Your API Token.
        """
        return pulumi.get(self, "api_token")

    @api_token.setter
    def api_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_token", value)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "channel_name")

    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_name", value)

    @property
    @pulumi.getter(name="flowName")
    def flow_name(self) -> Optional[pulumi.Input[str]]:
        """
        Your Flowdock Flow name.
        """
        return pulumi.get(self, "flow_name")

    @flow_name.setter
    def flow_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "flow_name", value)

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[pulumi.Input[str]]:
        """
        Your License Key.
        """
        return pulumi.get(self, "license_key")

    @license_key.setter
    def license_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_key", value)

    @property
    @pulumi.getter(name="orgName")
    def org_name(self) -> Optional[pulumi.Input[str]]:
        """
        Your Flowdock organization name.
        * `WEBHOOK`
        """
        return pulumi.get(self, "org_name")

    @org_name.setter
    def org_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_name", value)

    @property
    @pulumi.getter(name="readToken")
    def read_token(self) -> Optional[pulumi.Input[str]]:
        """
        Your Insights Query Key.
        * `OPS_GENIE`
        """
        return pulumi.get(self, "read_token")

    @read_token.setter
    def read_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "read_token", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates which API URL to use, either US or EU. Opsgenie will use US by default.
        * `VICTOR_OPS`
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="routingKey")
    def routing_key(self) -> Optional[pulumi.Input[str]]:
        """
        An optional field for your Routing Key.
        * `FLOWDOCK`
        """
        return pulumi.get(self, "routing_key")

    @routing_key.setter
    def routing_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_key", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        """
        An optional field for your webhook secret.
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> Optional[pulumi.Input[str]]:
        """
        Your Service Key.
        * `DATADOG`
        """
        return pulumi.get(self, "service_key")

    @service_key.setter
    def service_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_key", value)

    @property
    @pulumi.getter(name="teamName")
    def team_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "team_name")

    @team_name.setter
    def team_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_name", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        Your webhook URL.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="writeToken")
    def write_token(self) -> Optional[pulumi.Input[str]]:
        """
        Your Insights Insert Key.
        """
        return pulumi.get(self, "write_token")

    @write_token.setter
    def write_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "write_token", value)


@pulumi.input_type
class _ThirdPartyIntegrationState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 flow_name: Optional[pulumi.Input[str]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 org_name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 read_token: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 service_key: Optional[pulumi.Input[str]] = None,
                 team_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 write_token: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ThirdPartyIntegration resources.
        :param pulumi.Input[str] account_id: Unique identifier of your New Relic account.
        :param pulumi.Input[str] api_key: Your API Key.
        :param pulumi.Input[str] api_token: Your API Token.
        :param pulumi.Input[str] flow_name: Your Flowdock Flow name.
        :param pulumi.Input[str] license_key: Your License Key.
        :param pulumi.Input[str] org_name: Your Flowdock organization name.
               * `WEBHOOK`
        :param pulumi.Input[str] project_id: The unique ID for the project to get all Third-Party service integrations
        :param pulumi.Input[str] read_token: Your Insights Query Key.
               * `OPS_GENIE`
        :param pulumi.Input[str] region: Indicates which API URL to use, either US or EU. Opsgenie will use US by default.
               * `VICTOR_OPS`
        :param pulumi.Input[str] routing_key: An optional field for your Routing Key.
               * `FLOWDOCK`
        :param pulumi.Input[str] secret: An optional field for your webhook secret.
        :param pulumi.Input[str] service_key: Your Service Key.
               * `DATADOG`
        :param pulumi.Input[str] type: Third-Party Integration Settings type 
               * PAGER_DUTY
               * DATADOG
               * NEW_RELIC
               * OPS_GENIE
               * VICTOR_OPS
               * FLOWDOCK
               * WEBHOOK
        :param pulumi.Input[str] url: Your webhook URL.
        :param pulumi.Input[str] write_token: Your Insights Insert Key.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if api_key is not None:
            pulumi.set(__self__, "api_key", api_key)
        if api_token is not None:
            pulumi.set(__self__, "api_token", api_token)
        if channel_name is not None:
            pulumi.set(__self__, "channel_name", channel_name)
        if flow_name is not None:
            pulumi.set(__self__, "flow_name", flow_name)
        if license_key is not None:
            pulumi.set(__self__, "license_key", license_key)
        if org_name is not None:
            pulumi.set(__self__, "org_name", org_name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if read_token is not None:
            pulumi.set(__self__, "read_token", read_token)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if routing_key is not None:
            pulumi.set(__self__, "routing_key", routing_key)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)
        if service_key is not None:
            pulumi.set(__self__, "service_key", service_key)
        if team_name is not None:
            pulumi.set(__self__, "team_name", team_name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if write_token is not None:
            pulumi.set(__self__, "write_token", write_token)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of your New Relic account.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        Your API Key.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> Optional[pulumi.Input[str]]:
        """
        Your API Token.
        """
        return pulumi.get(self, "api_token")

    @api_token.setter
    def api_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_token", value)

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "channel_name")

    @channel_name.setter
    def channel_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_name", value)

    @property
    @pulumi.getter(name="flowName")
    def flow_name(self) -> Optional[pulumi.Input[str]]:
        """
        Your Flowdock Flow name.
        """
        return pulumi.get(self, "flow_name")

    @flow_name.setter
    def flow_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "flow_name", value)

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[pulumi.Input[str]]:
        """
        Your License Key.
        """
        return pulumi.get(self, "license_key")

    @license_key.setter
    def license_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "license_key", value)

    @property
    @pulumi.getter(name="orgName")
    def org_name(self) -> Optional[pulumi.Input[str]]:
        """
        Your Flowdock organization name.
        * `WEBHOOK`
        """
        return pulumi.get(self, "org_name")

    @org_name.setter
    def org_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "org_name", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique ID for the project to get all Third-Party service integrations
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="readToken")
    def read_token(self) -> Optional[pulumi.Input[str]]:
        """
        Your Insights Query Key.
        * `OPS_GENIE`
        """
        return pulumi.get(self, "read_token")

    @read_token.setter
    def read_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "read_token", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates which API URL to use, either US or EU. Opsgenie will use US by default.
        * `VICTOR_OPS`
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="routingKey")
    def routing_key(self) -> Optional[pulumi.Input[str]]:
        """
        An optional field for your Routing Key.
        * `FLOWDOCK`
        """
        return pulumi.get(self, "routing_key")

    @routing_key.setter
    def routing_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_key", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        """
        An optional field for your webhook secret.
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> Optional[pulumi.Input[str]]:
        """
        Your Service Key.
        * `DATADOG`
        """
        return pulumi.get(self, "service_key")

    @service_key.setter
    def service_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_key", value)

    @property
    @pulumi.getter(name="teamName")
    def team_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "team_name")

    @team_name.setter
    def team_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Third-Party Integration Settings type 
        * PAGER_DUTY
        * DATADOG
        * NEW_RELIC
        * OPS_GENIE
        * VICTOR_OPS
        * FLOWDOCK
        * WEBHOOK
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        Your webhook URL.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter(name="writeToken")
    def write_token(self) -> Optional[pulumi.Input[str]]:
        """
        Your Insights Insert Key.
        """
        return pulumi.get(self, "write_token")

    @write_token.setter
    def write_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "write_token", value)


class ThirdPartyIntegration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 flow_name: Optional[pulumi.Input[str]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 org_name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 read_token: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 service_key: Optional[pulumi.Input[str]] = None,
                 team_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 write_token: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        Third-Party Integration Settings can be imported using project ID and the integration type, in the format `project_id`-`type`, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/thirdPartyIntegration:ThirdPartyIntegration my_user 1112222b3bf99403840e8934-OPS_GENIE
        ```

         See [MongoDB Atlas API](https://docs.atlas.mongodb.com/reference/api/third-party-integration-settings-create/) Documentation for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Unique identifier of your New Relic account.
        :param pulumi.Input[str] api_key: Your API Key.
        :param pulumi.Input[str] api_token: Your API Token.
        :param pulumi.Input[str] flow_name: Your Flowdock Flow name.
        :param pulumi.Input[str] license_key: Your License Key.
        :param pulumi.Input[str] org_name: Your Flowdock organization name.
               * `WEBHOOK`
        :param pulumi.Input[str] project_id: The unique ID for the project to get all Third-Party service integrations
        :param pulumi.Input[str] read_token: Your Insights Query Key.
               * `OPS_GENIE`
        :param pulumi.Input[str] region: Indicates which API URL to use, either US or EU. Opsgenie will use US by default.
               * `VICTOR_OPS`
        :param pulumi.Input[str] routing_key: An optional field for your Routing Key.
               * `FLOWDOCK`
        :param pulumi.Input[str] secret: An optional field for your webhook secret.
        :param pulumi.Input[str] service_key: Your Service Key.
               * `DATADOG`
        :param pulumi.Input[str] type: Third-Party Integration Settings type 
               * PAGER_DUTY
               * DATADOG
               * NEW_RELIC
               * OPS_GENIE
               * VICTOR_OPS
               * FLOWDOCK
               * WEBHOOK
        :param pulumi.Input[str] url: Your webhook URL.
        :param pulumi.Input[str] write_token: Your Insights Insert Key.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ThirdPartyIntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        Third-Party Integration Settings can be imported using project ID and the integration type, in the format `project_id`-`type`, e.g.

        ```sh
         $ pulumi import mongodbatlas:index/thirdPartyIntegration:ThirdPartyIntegration my_user 1112222b3bf99403840e8934-OPS_GENIE
        ```

         See [MongoDB Atlas API](https://docs.atlas.mongodb.com/reference/api/third-party-integration-settings-create/) Documentation for more information.

        :param str resource_name: The name of the resource.
        :param ThirdPartyIntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ThirdPartyIntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 channel_name: Optional[pulumi.Input[str]] = None,
                 flow_name: Optional[pulumi.Input[str]] = None,
                 license_key: Optional[pulumi.Input[str]] = None,
                 org_name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 read_token: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 service_key: Optional[pulumi.Input[str]] = None,
                 team_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 write_token: Optional[pulumi.Input[str]] = None,
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
            __props__ = ThirdPartyIntegrationArgs.__new__(ThirdPartyIntegrationArgs)

            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["api_key"] = api_key
            __props__.__dict__["api_token"] = api_token
            __props__.__dict__["channel_name"] = channel_name
            __props__.__dict__["flow_name"] = flow_name
            __props__.__dict__["license_key"] = license_key
            __props__.__dict__["org_name"] = org_name
            if project_id is None and not opts.urn:
                raise TypeError("Missing required property 'project_id'")
            __props__.__dict__["project_id"] = project_id
            __props__.__dict__["read_token"] = read_token
            __props__.__dict__["region"] = region
            __props__.__dict__["routing_key"] = routing_key
            __props__.__dict__["secret"] = secret
            __props__.__dict__["service_key"] = service_key
            __props__.__dict__["team_name"] = team_name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["url"] = url
            __props__.__dict__["write_token"] = write_token
        super(ThirdPartyIntegration, __self__).__init__(
            'mongodbatlas:index/thirdPartyIntegration:ThirdPartyIntegration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            api_key: Optional[pulumi.Input[str]] = None,
            api_token: Optional[pulumi.Input[str]] = None,
            channel_name: Optional[pulumi.Input[str]] = None,
            flow_name: Optional[pulumi.Input[str]] = None,
            license_key: Optional[pulumi.Input[str]] = None,
            org_name: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            read_token: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            routing_key: Optional[pulumi.Input[str]] = None,
            secret: Optional[pulumi.Input[str]] = None,
            service_key: Optional[pulumi.Input[str]] = None,
            team_name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None,
            write_token: Optional[pulumi.Input[str]] = None) -> 'ThirdPartyIntegration':
        """
        Get an existing ThirdPartyIntegration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Unique identifier of your New Relic account.
        :param pulumi.Input[str] api_key: Your API Key.
        :param pulumi.Input[str] api_token: Your API Token.
        :param pulumi.Input[str] flow_name: Your Flowdock Flow name.
        :param pulumi.Input[str] license_key: Your License Key.
        :param pulumi.Input[str] org_name: Your Flowdock organization name.
               * `WEBHOOK`
        :param pulumi.Input[str] project_id: The unique ID for the project to get all Third-Party service integrations
        :param pulumi.Input[str] read_token: Your Insights Query Key.
               * `OPS_GENIE`
        :param pulumi.Input[str] region: Indicates which API URL to use, either US or EU. Opsgenie will use US by default.
               * `VICTOR_OPS`
        :param pulumi.Input[str] routing_key: An optional field for your Routing Key.
               * `FLOWDOCK`
        :param pulumi.Input[str] secret: An optional field for your webhook secret.
        :param pulumi.Input[str] service_key: Your Service Key.
               * `DATADOG`
        :param pulumi.Input[str] type: Third-Party Integration Settings type 
               * PAGER_DUTY
               * DATADOG
               * NEW_RELIC
               * OPS_GENIE
               * VICTOR_OPS
               * FLOWDOCK
               * WEBHOOK
        :param pulumi.Input[str] url: Your webhook URL.
        :param pulumi.Input[str] write_token: Your Insights Insert Key.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ThirdPartyIntegrationState.__new__(_ThirdPartyIntegrationState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["api_key"] = api_key
        __props__.__dict__["api_token"] = api_token
        __props__.__dict__["channel_name"] = channel_name
        __props__.__dict__["flow_name"] = flow_name
        __props__.__dict__["license_key"] = license_key
        __props__.__dict__["org_name"] = org_name
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["read_token"] = read_token
        __props__.__dict__["region"] = region
        __props__.__dict__["routing_key"] = routing_key
        __props__.__dict__["secret"] = secret
        __props__.__dict__["service_key"] = service_key
        __props__.__dict__["team_name"] = team_name
        __props__.__dict__["type"] = type
        __props__.__dict__["url"] = url
        __props__.__dict__["write_token"] = write_token
        return ThirdPartyIntegration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[Optional[str]]:
        """
        Unique identifier of your New Relic account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        """
        Your API Key.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> pulumi.Output[Optional[str]]:
        """
        Your API Token.
        """
        return pulumi.get(self, "api_token")

    @property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "channel_name")

    @property
    @pulumi.getter(name="flowName")
    def flow_name(self) -> pulumi.Output[Optional[str]]:
        """
        Your Flowdock Flow name.
        """
        return pulumi.get(self, "flow_name")

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> pulumi.Output[Optional[str]]:
        """
        Your License Key.
        """
        return pulumi.get(self, "license_key")

    @property
    @pulumi.getter(name="orgName")
    def org_name(self) -> pulumi.Output[Optional[str]]:
        """
        Your Flowdock organization name.
        * `WEBHOOK`
        """
        return pulumi.get(self, "org_name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The unique ID for the project to get all Third-Party service integrations
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="readToken")
    def read_token(self) -> pulumi.Output[Optional[str]]:
        """
        Your Insights Query Key.
        * `OPS_GENIE`
        """
        return pulumi.get(self, "read_token")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates which API URL to use, either US or EU. Opsgenie will use US by default.
        * `VICTOR_OPS`
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="routingKey")
    def routing_key(self) -> pulumi.Output[Optional[str]]:
        """
        An optional field for your Routing Key.
        * `FLOWDOCK`
        """
        return pulumi.get(self, "routing_key")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[Optional[str]]:
        """
        An optional field for your webhook secret.
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter(name="serviceKey")
    def service_key(self) -> pulumi.Output[Optional[str]]:
        """
        Your Service Key.
        * `DATADOG`
        """
        return pulumi.get(self, "service_key")

    @property
    @pulumi.getter(name="teamName")
    def team_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "team_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Third-Party Integration Settings type 
        * PAGER_DUTY
        * DATADOG
        * NEW_RELIC
        * OPS_GENIE
        * VICTOR_OPS
        * FLOWDOCK
        * WEBHOOK
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[Optional[str]]:
        """
        Your webhook URL.
        """
        return pulumi.get(self, "url")

    @property
    @pulumi.getter(name="writeToken")
    def write_token(self) -> pulumi.Output[Optional[str]]:
        """
        Your Insights Insert Key.
        """
        return pulumi.get(self, "write_token")

