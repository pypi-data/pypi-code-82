# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .alert_policy import *
from .api_integration import *
from .custom_role import *
from .email_integration import *
from .escalation import *
from .get_escalation import *
from .get_heartbeat import *
from .get_schedule import *
from .get_service import *
from .get_team import *
from .get_user import *
from .heartbeat import *
from .incident_template import *
from .integration_action import *
from .maintenance import *
from .notification_policy import *
from .notification_rule import *
from .provider import *
from .schedule import *
from .schedule_rotation import *
from .service import *
from .service_incident_rule import *
from .team import *
from .team_routing_rule import *
from .user import *
from .user_contact import *
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
            if typ == "opsgenie:index/alertPolicy:AlertPolicy":
                return AlertPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/apiIntegration:ApiIntegration":
                return ApiIntegration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/customRole:CustomRole":
                return CustomRole(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/emailIntegration:EmailIntegration":
                return EmailIntegration(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/escalation:Escalation":
                return Escalation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/heartbeat:Heartbeat":
                return Heartbeat(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/incidentTemplate:IncidentTemplate":
                return IncidentTemplate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/integrationAction:IntegrationAction":
                return IntegrationAction(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/maintenance:Maintenance":
                return Maintenance(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/notificationPolicy:NotificationPolicy":
                return NotificationPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/notificationRule:NotificationRule":
                return NotificationRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/schedule:Schedule":
                return Schedule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/scheduleRotation:ScheduleRotation":
                return ScheduleRotation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/service:Service":
                return Service(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/serviceIncidentRule:ServiceIncidentRule":
                return ServiceIncidentRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/team:Team":
                return Team(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/teamRoutingRule:TeamRoutingRule":
                return TeamRoutingRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/user:User":
                return User(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "opsgenie:index/userContact:UserContact":
                return UserContact(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("opsgenie", "index/alertPolicy", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/apiIntegration", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/customRole", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/emailIntegration", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/escalation", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/heartbeat", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/incidentTemplate", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/integrationAction", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/maintenance", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/notificationPolicy", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/notificationRule", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/schedule", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/scheduleRotation", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/service", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/serviceIncidentRule", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/team", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/teamRoutingRule", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/user", _module_instance)
    pulumi.runtime.register_resource_module("opsgenie", "index/userContact", _module_instance)


    class Package(pulumi.runtime.ResourcePackage):
        _version = _utilities.get_semver_version()

        def version(self):
            return Package._version

        def construct_provider(self, name: str, typ: str, urn: str) -> pulumi.ProviderResource:
            if typ != "pulumi:providers:opsgenie":
                raise Exception(f"unknown provider type {typ}")
            return Provider(name, pulumi.ResourceOptions(urn=urn))


    pulumi.runtime.register_resource_package("opsgenie", Package())

_register_module()
