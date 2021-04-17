# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['KafkaSchemaArgs', 'KafkaSchema']

@pulumi.input_type
class KafkaSchemaArgs:
    def __init__(__self__, *,
                 project: pulumi.Input[str],
                 schema: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 subject_name: pulumi.Input[str],
                 compatibility_level: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KafkaSchema resource.
        :param pulumi.Input[str] project: and `service_name` - (Required) define the project and service the Kafka Schemas belongs to. 
               They should be defined using reference as shown above to set up dependencies correctly.
        :param pulumi.Input[str] schema: is Kafka Schema configuration should be a valid Avro Schema JSON format.
        :param pulumi.Input[str] service_name: Service to link the Kafka Schema to
        :param pulumi.Input[str] subject_name: is Kafka Schema subject name.
        :param pulumi.Input[str] compatibility_level: configuration compatibility level overrides specific subject
               resource. If the compatibility level not specified for the individual subject by default,
               it takes a global value. Allowed values: `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`,
               `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, `NONE`.
        """
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "schema", schema)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "subject_name", subject_name)
        if compatibility_level is not None:
            pulumi.set(__self__, "compatibility_level", compatibility_level)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        and `service_name` - (Required) define the project and service the Kafka Schemas belongs to. 
        They should be defined using reference as shown above to set up dependencies correctly.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Input[str]:
        """
        is Kafka Schema configuration should be a valid Avro Schema JSON format.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: pulumi.Input[str]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        Service to link the Kafka Schema to
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> pulumi.Input[str]:
        """
        is Kafka Schema subject name.
        """
        return pulumi.get(self, "subject_name")

    @subject_name.setter
    def subject_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "subject_name", value)

    @property
    @pulumi.getter(name="compatibilityLevel")
    def compatibility_level(self) -> Optional[pulumi.Input[str]]:
        """
        configuration compatibility level overrides specific subject
        resource. If the compatibility level not specified for the individual subject by default,
        it takes a global value. Allowed values: `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`,
        `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, `NONE`.
        """
        return pulumi.get(self, "compatibility_level")

    @compatibility_level.setter
    def compatibility_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compatibility_level", value)


@pulumi.input_type
class _KafkaSchemaState:
    def __init__(__self__, *,
                 compatibility_level: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 subject_name: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering KafkaSchema resources.
        :param pulumi.Input[str] compatibility_level: configuration compatibility level overrides specific subject
               resource. If the compatibility level not specified for the individual subject by default,
               it takes a global value. Allowed values: `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`,
               `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, `NONE`.
        :param pulumi.Input[str] project: and `service_name` - (Required) define the project and service the Kafka Schemas belongs to. 
               They should be defined using reference as shown above to set up dependencies correctly.
        :param pulumi.Input[str] schema: is Kafka Schema configuration should be a valid Avro Schema JSON format.
        :param pulumi.Input[str] service_name: Service to link the Kafka Schema to
        :param pulumi.Input[str] subject_name: is Kafka Schema subject name.
        :param pulumi.Input[int] version: Kafka Schema configuration version
        """
        if compatibility_level is not None:
            pulumi.set(__self__, "compatibility_level", compatibility_level)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if schema is not None:
            pulumi.set(__self__, "schema", schema)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if subject_name is not None:
            pulumi.set(__self__, "subject_name", subject_name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="compatibilityLevel")
    def compatibility_level(self) -> Optional[pulumi.Input[str]]:
        """
        configuration compatibility level overrides specific subject
        resource. If the compatibility level not specified for the individual subject by default,
        it takes a global value. Allowed values: `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`,
        `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, `NONE`.
        """
        return pulumi.get(self, "compatibility_level")

    @compatibility_level.setter
    def compatibility_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "compatibility_level", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        and `service_name` - (Required) define the project and service the Kafka Schemas belongs to. 
        They should be defined using reference as shown above to set up dependencies correctly.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter
    def schema(self) -> Optional[pulumi.Input[str]]:
        """
        is Kafka Schema configuration should be a valid Avro Schema JSON format.
        """
        return pulumi.get(self, "schema")

    @schema.setter
    def schema(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        Service to link the Kafka Schema to
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> Optional[pulumi.Input[str]]:
        """
        is Kafka Schema subject name.
        """
        return pulumi.get(self, "subject_name")

    @subject_name.setter
    def subject_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subject_name", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[int]]:
        """
        Kafka Schema configuration version
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "version", value)


class KafkaSchema(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compatibility_level: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 subject_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## # Kafka Schema Resource

        The Kafka Schema resource allows the creation and management of Aiven Kafka Schemas.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        kafka_schema1 = aiven.KafkaSchema("kafka-schema1",
            project=aiven_project["kafka-schemas-project1"]["project"],
            service_name=aiven_service["kafka-service1"]["service_name"],
            subject_name="kafka-schema1",
            compatibility_level="FORWARD",
            schema=\"\"\"    {
               "doc": "example",
               "fields": [{
                   "default": 5,
                   "doc": "my test number",
                   "name": "test",
                   "namespace": "test",
                   "type": "int"
               }],
               "name": "example",
               "namespace": "example",
               "type": "record"
            }
        \"\"\")
        ```

        You can also load the schema from an external file:

        ```python
        import pulumi
        import pulumi_aiven as aiven

        kafka_schema2 = aiven.KafkaSchema("kafka-schema2",
            project=aiven_project["kafka-schemas-project1"]["project"],
            service_name=aiven_service["kafka-service1"]["service_name"],
            subject_name="kafka-schema2",
            compatibility_level="FORWARD",
            schema=(lambda path: open(path).read())(f"{path['module']}/external_schema.avsc"))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compatibility_level: configuration compatibility level overrides specific subject
               resource. If the compatibility level not specified for the individual subject by default,
               it takes a global value. Allowed values: `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`,
               `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, `NONE`.
        :param pulumi.Input[str] project: and `service_name` - (Required) define the project and service the Kafka Schemas belongs to. 
               They should be defined using reference as shown above to set up dependencies correctly.
        :param pulumi.Input[str] schema: is Kafka Schema configuration should be a valid Avro Schema JSON format.
        :param pulumi.Input[str] service_name: Service to link the Kafka Schema to
        :param pulumi.Input[str] subject_name: is Kafka Schema subject name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KafkaSchemaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Kafka Schema Resource

        The Kafka Schema resource allows the creation and management of Aiven Kafka Schemas.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aiven as aiven

        kafka_schema1 = aiven.KafkaSchema("kafka-schema1",
            project=aiven_project["kafka-schemas-project1"]["project"],
            service_name=aiven_service["kafka-service1"]["service_name"],
            subject_name="kafka-schema1",
            compatibility_level="FORWARD",
            schema=\"\"\"    {
               "doc": "example",
               "fields": [{
                   "default": 5,
                   "doc": "my test number",
                   "name": "test",
                   "namespace": "test",
                   "type": "int"
               }],
               "name": "example",
               "namespace": "example",
               "type": "record"
            }
        \"\"\")
        ```

        You can also load the schema from an external file:

        ```python
        import pulumi
        import pulumi_aiven as aiven

        kafka_schema2 = aiven.KafkaSchema("kafka-schema2",
            project=aiven_project["kafka-schemas-project1"]["project"],
            service_name=aiven_service["kafka-service1"]["service_name"],
            subject_name="kafka-schema2",
            compatibility_level="FORWARD",
            schema=(lambda path: open(path).read())(f"{path['module']}/external_schema.avsc"))
        ```

        :param str resource_name: The name of the resource.
        :param KafkaSchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KafkaSchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 compatibility_level: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 schema: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 subject_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = KafkaSchemaArgs.__new__(KafkaSchemaArgs)

            __props__.__dict__["compatibility_level"] = compatibility_level
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if schema is None and not opts.urn:
                raise TypeError("Missing required property 'schema'")
            __props__.__dict__["schema"] = schema
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if subject_name is None and not opts.urn:
                raise TypeError("Missing required property 'subject_name'")
            __props__.__dict__["subject_name"] = subject_name
            __props__.__dict__["version"] = None
        super(KafkaSchema, __self__).__init__(
            'aiven:index/kafkaSchema:KafkaSchema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            compatibility_level: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            schema: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            subject_name: Optional[pulumi.Input[str]] = None,
            version: Optional[pulumi.Input[int]] = None) -> 'KafkaSchema':
        """
        Get an existing KafkaSchema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] compatibility_level: configuration compatibility level overrides specific subject
               resource. If the compatibility level not specified for the individual subject by default,
               it takes a global value. Allowed values: `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`,
               `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, `NONE`.
        :param pulumi.Input[str] project: and `service_name` - (Required) define the project and service the Kafka Schemas belongs to. 
               They should be defined using reference as shown above to set up dependencies correctly.
        :param pulumi.Input[str] schema: is Kafka Schema configuration should be a valid Avro Schema JSON format.
        :param pulumi.Input[str] service_name: Service to link the Kafka Schema to
        :param pulumi.Input[str] subject_name: is Kafka Schema subject name.
        :param pulumi.Input[int] version: Kafka Schema configuration version
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KafkaSchemaState.__new__(_KafkaSchemaState)

        __props__.__dict__["compatibility_level"] = compatibility_level
        __props__.__dict__["project"] = project
        __props__.__dict__["schema"] = schema
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["subject_name"] = subject_name
        __props__.__dict__["version"] = version
        return KafkaSchema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="compatibilityLevel")
    def compatibility_level(self) -> pulumi.Output[Optional[str]]:
        """
        configuration compatibility level overrides specific subject
        resource. If the compatibility level not specified for the individual subject by default,
        it takes a global value. Allowed values: `BACKWARD`, `BACKWARD_TRANSITIVE`, `FORWARD`,
        `FORWARD_TRANSITIVE`, `FULL`, `FULL_TRANSITIVE`, `NONE`.
        """
        return pulumi.get(self, "compatibility_level")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        and `service_name` - (Required) define the project and service the Kafka Schemas belongs to. 
        They should be defined using reference as shown above to set up dependencies correctly.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def schema(self) -> pulumi.Output[str]:
        """
        is Kafka Schema configuration should be a valid Avro Schema JSON format.
        """
        return pulumi.get(self, "schema")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        Service to link the Kafka Schema to
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> pulumi.Output[str]:
        """
        is Kafka Schema subject name.
        """
        return pulumi.get(self, "subject_name")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        """
        Kafka Schema configuration version
        """
        return pulumi.get(self, "version")

