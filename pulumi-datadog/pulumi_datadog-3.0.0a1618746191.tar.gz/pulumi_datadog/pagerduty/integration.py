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

__all__ = ['IntegrationArgs', 'Integration']

@pulumi.input_type
class IntegrationArgs:
    def __init__(__self__, *,
                 subdomain: pulumi.Input[str],
                 api_token: Optional[pulumi.Input[str]] = None,
                 individual_services: Optional[pulumi.Input[bool]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationServiceArgs']]]] = None):
        """
        The set of arguments for constructing a Integration resource.
        :param pulumi.Input[str] subdomain: Your PagerDuty account’s personalized subdomain name.
        :param pulumi.Input[str] api_token: Your PagerDuty API token.
        :param pulumi.Input[bool] individual_services: Boolean to specify whether or not individual service objects specified by
               [datadog_integration_pagerduty_service_object](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_pagerduty_service_object)
               resource are to be used. Mutually exclusive with `services` key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] schedules: Array of your schedule URLs.
        :param pulumi.Input[Sequence[pulumi.Input['IntegrationServiceArgs']]] services: A list of service names and service keys.
        """
        pulumi.set(__self__, "subdomain", subdomain)
        if api_token is not None:
            pulumi.set(__self__, "api_token", api_token)
        if individual_services is not None:
            pulumi.set(__self__, "individual_services", individual_services)
        if schedules is not None:
            pulumi.set(__self__, "schedules", schedules)
        if services is not None:
            warnings.warn("""set \"individual_services\" to true and use datadog_pagerduty_integration_service_object""", DeprecationWarning)
            pulumi.log.warn("""services is deprecated: set \"individual_services\" to true and use datadog_pagerduty_integration_service_object""")
        if services is not None:
            pulumi.set(__self__, "services", services)

    @property
    @pulumi.getter
    def subdomain(self) -> pulumi.Input[str]:
        """
        Your PagerDuty account’s personalized subdomain name.
        """
        return pulumi.get(self, "subdomain")

    @subdomain.setter
    def subdomain(self, value: pulumi.Input[str]):
        pulumi.set(self, "subdomain", value)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> Optional[pulumi.Input[str]]:
        """
        Your PagerDuty API token.
        """
        return pulumi.get(self, "api_token")

    @api_token.setter
    def api_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_token", value)

    @property
    @pulumi.getter(name="individualServices")
    def individual_services(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean to specify whether or not individual service objects specified by
        [datadog_integration_pagerduty_service_object](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_pagerduty_service_object)
        resource are to be used. Mutually exclusive with `services` key.
        """
        return pulumi.get(self, "individual_services")

    @individual_services.setter
    def individual_services(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "individual_services", value)

    @property
    @pulumi.getter
    def schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Array of your schedule URLs.
        """
        return pulumi.get(self, "schedules")

    @schedules.setter
    def schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "schedules", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationServiceArgs']]]]:
        """
        A list of service names and service keys.
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationServiceArgs']]]]):
        pulumi.set(self, "services", value)


@pulumi.input_type
class _IntegrationState:
    def __init__(__self__, *,
                 api_token: Optional[pulumi.Input[str]] = None,
                 individual_services: Optional[pulumi.Input[bool]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationServiceArgs']]]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Integration resources.
        :param pulumi.Input[str] api_token: Your PagerDuty API token.
        :param pulumi.Input[bool] individual_services: Boolean to specify whether or not individual service objects specified by
               [datadog_integration_pagerduty_service_object](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_pagerduty_service_object)
               resource are to be used. Mutually exclusive with `services` key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] schedules: Array of your schedule URLs.
        :param pulumi.Input[Sequence[pulumi.Input['IntegrationServiceArgs']]] services: A list of service names and service keys.
        :param pulumi.Input[str] subdomain: Your PagerDuty account’s personalized subdomain name.
        """
        if api_token is not None:
            pulumi.set(__self__, "api_token", api_token)
        if individual_services is not None:
            pulumi.set(__self__, "individual_services", individual_services)
        if schedules is not None:
            pulumi.set(__self__, "schedules", schedules)
        if services is not None:
            warnings.warn("""set \"individual_services\" to true and use datadog_pagerduty_integration_service_object""", DeprecationWarning)
            pulumi.log.warn("""services is deprecated: set \"individual_services\" to true and use datadog_pagerduty_integration_service_object""")
        if services is not None:
            pulumi.set(__self__, "services", services)
        if subdomain is not None:
            pulumi.set(__self__, "subdomain", subdomain)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> Optional[pulumi.Input[str]]:
        """
        Your PagerDuty API token.
        """
        return pulumi.get(self, "api_token")

    @api_token.setter
    def api_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_token", value)

    @property
    @pulumi.getter(name="individualServices")
    def individual_services(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean to specify whether or not individual service objects specified by
        [datadog_integration_pagerduty_service_object](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_pagerduty_service_object)
        resource are to be used. Mutually exclusive with `services` key.
        """
        return pulumi.get(self, "individual_services")

    @individual_services.setter
    def individual_services(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "individual_services", value)

    @property
    @pulumi.getter
    def schedules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Array of your schedule URLs.
        """
        return pulumi.get(self, "schedules")

    @schedules.setter
    def schedules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "schedules", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationServiceArgs']]]]:
        """
        A list of service names and service keys.
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationServiceArgs']]]]):
        pulumi.set(self, "services", value)

    @property
    @pulumi.getter
    def subdomain(self) -> Optional[pulumi.Input[str]]:
        """
        Your PagerDuty account’s personalized subdomain name.
        """
        return pulumi.get(self, "subdomain")

    @subdomain.setter
    def subdomain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subdomain", value)


class Integration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 individual_services: Optional[pulumi.Input[bool]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationServiceArgs']]]]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Datadog - PagerDuty resource. This can be used to create and manage Datadog - PagerDuty integration. This resource is deprecated and should only be used for legacy purposes.

        ## Example Usage
        ### Services as Individual Resources

        ```python
        import pulumi
        import pulumi_datadog as datadog

        pd = datadog.pagerduty.Integration("pd",
            api_token="38457822378273432587234242874",
            individual_services=True,
            schedules=[
                "https://ddog.pagerduty.com/schedules/X123VF",
                "https://ddog.pagerduty.com/schedules/X321XX",
            ],
            subdomain="ddog")
        testing_foo = datadog.pagerduty.ServiceObject("testingFoo",
            service_key="9876543210123456789",
            service_name="testing_foo",
            opts=pulumi.ResourceOptions(depends_on=["datadog_integration_pagerduty.pd"]))
        testing_bar = datadog.pagerduty.ServiceObject("testingBar",
            service_key="54321098765432109876",
            service_name="testing_bar",
            opts=pulumi.ResourceOptions(depends_on=["datadog_integration_pagerduty.pd"]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_token: Your PagerDuty API token.
        :param pulumi.Input[bool] individual_services: Boolean to specify whether or not individual service objects specified by
               [datadog_integration_pagerduty_service_object](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_pagerduty_service_object)
               resource are to be used. Mutually exclusive with `services` key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] schedules: Array of your schedule URLs.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationServiceArgs']]]] services: A list of service names and service keys.
        :param pulumi.Input[str] subdomain: Your PagerDuty account’s personalized subdomain name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Datadog - PagerDuty resource. This can be used to create and manage Datadog - PagerDuty integration. This resource is deprecated and should only be used for legacy purposes.

        ## Example Usage
        ### Services as Individual Resources

        ```python
        import pulumi
        import pulumi_datadog as datadog

        pd = datadog.pagerduty.Integration("pd",
            api_token="38457822378273432587234242874",
            individual_services=True,
            schedules=[
                "https://ddog.pagerduty.com/schedules/X123VF",
                "https://ddog.pagerduty.com/schedules/X321XX",
            ],
            subdomain="ddog")
        testing_foo = datadog.pagerduty.ServiceObject("testingFoo",
            service_key="9876543210123456789",
            service_name="testing_foo",
            opts=pulumi.ResourceOptions(depends_on=["datadog_integration_pagerduty.pd"]))
        testing_bar = datadog.pagerduty.ServiceObject("testingBar",
            service_key="54321098765432109876",
            service_name="testing_bar",
            opts=pulumi.ResourceOptions(depends_on=["datadog_integration_pagerduty.pd"]))
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_token: Optional[pulumi.Input[str]] = None,
                 individual_services: Optional[pulumi.Input[bool]] = None,
                 schedules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationServiceArgs']]]]] = None,
                 subdomain: Optional[pulumi.Input[str]] = None,
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
            __props__ = IntegrationArgs.__new__(IntegrationArgs)

            __props__.__dict__["api_token"] = api_token
            __props__.__dict__["individual_services"] = individual_services
            __props__.__dict__["schedules"] = schedules
            if services is not None and not opts.urn:
                warnings.warn("""set \"individual_services\" to true and use datadog_pagerduty_integration_service_object""", DeprecationWarning)
                pulumi.log.warn("""services is deprecated: set \"individual_services\" to true and use datadog_pagerduty_integration_service_object""")
            __props__.__dict__["services"] = services
            if subdomain is None and not opts.urn:
                raise TypeError("Missing required property 'subdomain'")
            __props__.__dict__["subdomain"] = subdomain
        super(Integration, __self__).__init__(
            'datadog:pagerduty/integration:Integration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            api_token: Optional[pulumi.Input[str]] = None,
            individual_services: Optional[pulumi.Input[bool]] = None,
            schedules: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            services: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationServiceArgs']]]]] = None,
            subdomain: Optional[pulumi.Input[str]] = None) -> 'Integration':
        """
        Get an existing Integration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_token: Your PagerDuty API token.
        :param pulumi.Input[bool] individual_services: Boolean to specify whether or not individual service objects specified by
               [datadog_integration_pagerduty_service_object](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_pagerduty_service_object)
               resource are to be used. Mutually exclusive with `services` key.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] schedules: Array of your schedule URLs.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationServiceArgs']]]] services: A list of service names and service keys.
        :param pulumi.Input[str] subdomain: Your PagerDuty account’s personalized subdomain name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationState.__new__(_IntegrationState)

        __props__.__dict__["api_token"] = api_token
        __props__.__dict__["individual_services"] = individual_services
        __props__.__dict__["schedules"] = schedules
        __props__.__dict__["services"] = services
        __props__.__dict__["subdomain"] = subdomain
        return Integration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiToken")
    def api_token(self) -> pulumi.Output[Optional[str]]:
        """
        Your PagerDuty API token.
        """
        return pulumi.get(self, "api_token")

    @property
    @pulumi.getter(name="individualServices")
    def individual_services(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean to specify whether or not individual service objects specified by
        [datadog_integration_pagerduty_service_object](https://registry.terraform.io/providers/DataDog/datadog/latest/docs/resources/integration_pagerduty_service_object)
        resource are to be used. Mutually exclusive with `services` key.
        """
        return pulumi.get(self, "individual_services")

    @property
    @pulumi.getter
    def schedules(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Array of your schedule URLs.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def services(self) -> pulumi.Output[Optional[Sequence['outputs.IntegrationService']]]:
        """
        A list of service names and service keys.
        """
        return pulumi.get(self, "services")

    @property
    @pulumi.getter
    def subdomain(self) -> pulumi.Output[str]:
        """
        Your PagerDuty account’s personalized subdomain name.
        """
        return pulumi.get(self, "subdomain")

