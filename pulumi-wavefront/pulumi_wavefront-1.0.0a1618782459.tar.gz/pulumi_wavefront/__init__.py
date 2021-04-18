# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .alert import *
from .alert_target import *
from .cloud_integration_app_dynamics import *
from .cloud_integration_aws_external_id import *
from .cloud_integration_azure import *
from .cloud_integration_azure_activity_log import *
from .cloud_integration_cloud_trail import *
from .cloud_integration_cloud_watch import *
from .cloud_integration_ec2 import *
from .cloud_integration_gcp import *
from .cloud_integration_gcp_billing import *
from .cloud_integration_new_relic import *
from .cloud_integration_tesla import *
from .dashboard import *
from .dashboard_json import *
from .derived_metric import *
from .external_link import *
from .get_default_user_group import *
from .ingestion_policy import *
from .maintenance_window import *
from .provider import *
from .role import *
from .service_account import *
from .user import *
from .user_group import *
from ._inputs import *
from . import outputs

# Make subpackages available:
from . import (
    config,
)

def _register_module():
    import pulumi
    from . import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "wavefront:index/alert:Alert":
                return Alert(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/alertTarget:AlertTarget":
                return AlertTarget(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationAppDynamics:CloudIntegrationAppDynamics":
                return CloudIntegrationAppDynamics(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationAwsExternalId:CloudIntegrationAwsExternalId":
                return CloudIntegrationAwsExternalId(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationAzure:CloudIntegrationAzure":
                return CloudIntegrationAzure(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationAzureActivityLog:CloudIntegrationAzureActivityLog":
                return CloudIntegrationAzureActivityLog(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationCloudTrail:CloudIntegrationCloudTrail":
                return CloudIntegrationCloudTrail(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationCloudWatch:CloudIntegrationCloudWatch":
                return CloudIntegrationCloudWatch(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationEc2:CloudIntegrationEc2":
                return CloudIntegrationEc2(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationGcp:CloudIntegrationGcp":
                return CloudIntegrationGcp(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationGcpBilling:CloudIntegrationGcpBilling":
                return CloudIntegrationGcpBilling(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationNewRelic:CloudIntegrationNewRelic":
                return CloudIntegrationNewRelic(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/cloudIntegrationTesla:CloudIntegrationTesla":
                return CloudIntegrationTesla(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/dashboard:Dashboard":
                return Dashboard(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/dashboardJson:DashboardJson":
                return DashboardJson(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/derivedMetric:DerivedMetric":
                return DerivedMetric(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/externalLink:ExternalLink":
                return ExternalLink(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/ingestionPolicy:IngestionPolicy":
                return IngestionPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/maintenanceWindow:MaintenanceWindow":
                return MaintenanceWindow(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/role:Role":
                return Role(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/serviceAccount:ServiceAccount":
                return ServiceAccount(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/user:User":
                return User(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "wavefront:index/userGroup:UserGroup":
                return UserGroup(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("wavefront", "index/alert", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/alertTarget", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationAppDynamics", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationAwsExternalId", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationAzure", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationAzureActivityLog", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationCloudTrail", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationCloudWatch", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationEc2", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationGcp", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationGcpBilling", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationNewRelic", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/cloudIntegrationTesla", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/dashboard", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/dashboardJson", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/derivedMetric", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/externalLink", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/ingestionPolicy", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/maintenanceWindow", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/role", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/serviceAccount", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/user", _module_instance)
    pulumi.runtime.register_resource_module("wavefront", "index/userGroup", _module_instance)


    class Package(pulumi.runtime.ResourcePackage):
        _version = _utilities.get_semver_version()

        def version(self):
            return Package._version

        def construct_provider(self, name: str, typ: str, urn: str) -> pulumi.ProviderResource:
            if typ != "pulumi:providers:wavefront":
                raise Exception(f"unknown provider type {typ}")
            return Provider(name, pulumi.ResourceOptions(urn=urn))


    pulumi.runtime.register_resource_package("wavefront", Package())

_register_module()
