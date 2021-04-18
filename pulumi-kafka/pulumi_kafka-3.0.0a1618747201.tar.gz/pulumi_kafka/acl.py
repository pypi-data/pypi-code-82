# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AclArgs', 'Acl']

@pulumi.input_type
class AclArgs:
    def __init__(__self__, *,
                 acl_host: pulumi.Input[str],
                 acl_operation: pulumi.Input[str],
                 acl_permission_type: pulumi.Input[str],
                 acl_principal: pulumi.Input[str],
                 acl_resource_name: pulumi.Input[str],
                 acl_resource_type: pulumi.Input[str],
                 resource_pattern_type_filter: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Acl resource.
        :param pulumi.Input[str] acl_host: Host from which principal listed in `acl_principal`
               will have access.
        :param pulumi.Input[str] acl_operation: Operation that is being allowed or denied. Valid
               values are `Unknown`, `Any`, `All`, `Read`, `Write`, `Create`, `Delete`, `Alter`,
               `Describe`, `ClusterAction`, `DescribeConfigs`, `AlterConfigs`, `IdempotentWrite`.
        :param pulumi.Input[str] acl_permission_type: Type of permission. Valid values are `Unknown`,
               `Any`, `Allow`, `Deny`.
        :param pulumi.Input[str] acl_principal: Principal that is being allowed or denied.
        :param pulumi.Input[str] acl_resource_name: The name of the resource.
        :param pulumi.Input[str] acl_resource_type: The type of resource. Valid values are `Unknown`,
               `Any`, `Topic`, `Group`, `Cluster`, `TransactionalID`.
        :param pulumi.Input[str] resource_pattern_type_filter: The pattern filter. Valid values
               are `Prefixed`, `Any`, `Match`, `Literal`.
        """
        pulumi.set(__self__, "acl_host", acl_host)
        pulumi.set(__self__, "acl_operation", acl_operation)
        pulumi.set(__self__, "acl_permission_type", acl_permission_type)
        pulumi.set(__self__, "acl_principal", acl_principal)
        pulumi.set(__self__, "acl_resource_name", acl_resource_name)
        pulumi.set(__self__, "acl_resource_type", acl_resource_type)
        if resource_pattern_type_filter is not None:
            pulumi.set(__self__, "resource_pattern_type_filter", resource_pattern_type_filter)

    @property
    @pulumi.getter(name="aclHost")
    def acl_host(self) -> pulumi.Input[str]:
        """
        Host from which principal listed in `acl_principal`
        will have access.
        """
        return pulumi.get(self, "acl_host")

    @acl_host.setter
    def acl_host(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_host", value)

    @property
    @pulumi.getter(name="aclOperation")
    def acl_operation(self) -> pulumi.Input[str]:
        """
        Operation that is being allowed or denied. Valid
        values are `Unknown`, `Any`, `All`, `Read`, `Write`, `Create`, `Delete`, `Alter`,
        `Describe`, `ClusterAction`, `DescribeConfigs`, `AlterConfigs`, `IdempotentWrite`.
        """
        return pulumi.get(self, "acl_operation")

    @acl_operation.setter
    def acl_operation(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_operation", value)

    @property
    @pulumi.getter(name="aclPermissionType")
    def acl_permission_type(self) -> pulumi.Input[str]:
        """
        Type of permission. Valid values are `Unknown`,
        `Any`, `Allow`, `Deny`.
        """
        return pulumi.get(self, "acl_permission_type")

    @acl_permission_type.setter
    def acl_permission_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_permission_type", value)

    @property
    @pulumi.getter(name="aclPrincipal")
    def acl_principal(self) -> pulumi.Input[str]:
        """
        Principal that is being allowed or denied.
        """
        return pulumi.get(self, "acl_principal")

    @acl_principal.setter
    def acl_principal(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_principal", value)

    @property
    @pulumi.getter(name="aclResourceName")
    def acl_resource_name(self) -> pulumi.Input[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "acl_resource_name")

    @acl_resource_name.setter
    def acl_resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_resource_name", value)

    @property
    @pulumi.getter(name="aclResourceType")
    def acl_resource_type(self) -> pulumi.Input[str]:
        """
        The type of resource. Valid values are `Unknown`,
        `Any`, `Topic`, `Group`, `Cluster`, `TransactionalID`.
        """
        return pulumi.get(self, "acl_resource_type")

    @acl_resource_type.setter
    def acl_resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "acl_resource_type", value)

    @property
    @pulumi.getter(name="resourcePatternTypeFilter")
    def resource_pattern_type_filter(self) -> Optional[pulumi.Input[str]]:
        """
        The pattern filter. Valid values
        are `Prefixed`, `Any`, `Match`, `Literal`.
        """
        return pulumi.get(self, "resource_pattern_type_filter")

    @resource_pattern_type_filter.setter
    def resource_pattern_type_filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_pattern_type_filter", value)


@pulumi.input_type
class _AclState:
    def __init__(__self__, *,
                 acl_host: Optional[pulumi.Input[str]] = None,
                 acl_operation: Optional[pulumi.Input[str]] = None,
                 acl_permission_type: Optional[pulumi.Input[str]] = None,
                 acl_principal: Optional[pulumi.Input[str]] = None,
                 acl_resource_name: Optional[pulumi.Input[str]] = None,
                 acl_resource_type: Optional[pulumi.Input[str]] = None,
                 resource_pattern_type_filter: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Acl resources.
        :param pulumi.Input[str] acl_host: Host from which principal listed in `acl_principal`
               will have access.
        :param pulumi.Input[str] acl_operation: Operation that is being allowed or denied. Valid
               values are `Unknown`, `Any`, `All`, `Read`, `Write`, `Create`, `Delete`, `Alter`,
               `Describe`, `ClusterAction`, `DescribeConfigs`, `AlterConfigs`, `IdempotentWrite`.
        :param pulumi.Input[str] acl_permission_type: Type of permission. Valid values are `Unknown`,
               `Any`, `Allow`, `Deny`.
        :param pulumi.Input[str] acl_principal: Principal that is being allowed or denied.
        :param pulumi.Input[str] acl_resource_name: The name of the resource.
        :param pulumi.Input[str] acl_resource_type: The type of resource. Valid values are `Unknown`,
               `Any`, `Topic`, `Group`, `Cluster`, `TransactionalID`.
        :param pulumi.Input[str] resource_pattern_type_filter: The pattern filter. Valid values
               are `Prefixed`, `Any`, `Match`, `Literal`.
        """
        if acl_host is not None:
            pulumi.set(__self__, "acl_host", acl_host)
        if acl_operation is not None:
            pulumi.set(__self__, "acl_operation", acl_operation)
        if acl_permission_type is not None:
            pulumi.set(__self__, "acl_permission_type", acl_permission_type)
        if acl_principal is not None:
            pulumi.set(__self__, "acl_principal", acl_principal)
        if acl_resource_name is not None:
            pulumi.set(__self__, "acl_resource_name", acl_resource_name)
        if acl_resource_type is not None:
            pulumi.set(__self__, "acl_resource_type", acl_resource_type)
        if resource_pattern_type_filter is not None:
            pulumi.set(__self__, "resource_pattern_type_filter", resource_pattern_type_filter)

    @property
    @pulumi.getter(name="aclHost")
    def acl_host(self) -> Optional[pulumi.Input[str]]:
        """
        Host from which principal listed in `acl_principal`
        will have access.
        """
        return pulumi.get(self, "acl_host")

    @acl_host.setter
    def acl_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_host", value)

    @property
    @pulumi.getter(name="aclOperation")
    def acl_operation(self) -> Optional[pulumi.Input[str]]:
        """
        Operation that is being allowed or denied. Valid
        values are `Unknown`, `Any`, `All`, `Read`, `Write`, `Create`, `Delete`, `Alter`,
        `Describe`, `ClusterAction`, `DescribeConfigs`, `AlterConfigs`, `IdempotentWrite`.
        """
        return pulumi.get(self, "acl_operation")

    @acl_operation.setter
    def acl_operation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_operation", value)

    @property
    @pulumi.getter(name="aclPermissionType")
    def acl_permission_type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of permission. Valid values are `Unknown`,
        `Any`, `Allow`, `Deny`.
        """
        return pulumi.get(self, "acl_permission_type")

    @acl_permission_type.setter
    def acl_permission_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_permission_type", value)

    @property
    @pulumi.getter(name="aclPrincipal")
    def acl_principal(self) -> Optional[pulumi.Input[str]]:
        """
        Principal that is being allowed or denied.
        """
        return pulumi.get(self, "acl_principal")

    @acl_principal.setter
    def acl_principal(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_principal", value)

    @property
    @pulumi.getter(name="aclResourceName")
    def acl_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "acl_resource_name")

    @acl_resource_name.setter
    def acl_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_resource_name", value)

    @property
    @pulumi.getter(name="aclResourceType")
    def acl_resource_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of resource. Valid values are `Unknown`,
        `Any`, `Topic`, `Group`, `Cluster`, `TransactionalID`.
        """
        return pulumi.get(self, "acl_resource_type")

    @acl_resource_type.setter
    def acl_resource_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acl_resource_type", value)

    @property
    @pulumi.getter(name="resourcePatternTypeFilter")
    def resource_pattern_type_filter(self) -> Optional[pulumi.Input[str]]:
        """
        The pattern filter. Valid values
        are `Prefixed`, `Any`, `Match`, `Literal`.
        """
        return pulumi.get(self, "resource_pattern_type_filter")

    @resource_pattern_type_filter.setter
    def resource_pattern_type_filter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_pattern_type_filter", value)


class Acl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_host: Optional[pulumi.Input[str]] = None,
                 acl_operation: Optional[pulumi.Input[str]] = None,
                 acl_permission_type: Optional[pulumi.Input[str]] = None,
                 acl_principal: Optional[pulumi.Input[str]] = None,
                 acl_resource_name: Optional[pulumi.Input[str]] = None,
                 acl_resource_type: Optional[pulumi.Input[str]] = None,
                 resource_pattern_type_filter: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        A resource for managing Kafka ACLs.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_kafka as kafka

        test = kafka.Acl("test",
            acl_resource_name="syslog",
            acl_resource_type="Topic",
            acl_principal="User:Alice",
            acl_host="*",
            acl_operation="Write",
            acl_permission_type="Deny")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_host: Host from which principal listed in `acl_principal`
               will have access.
        :param pulumi.Input[str] acl_operation: Operation that is being allowed or denied. Valid
               values are `Unknown`, `Any`, `All`, `Read`, `Write`, `Create`, `Delete`, `Alter`,
               `Describe`, `ClusterAction`, `DescribeConfigs`, `AlterConfigs`, `IdempotentWrite`.
        :param pulumi.Input[str] acl_permission_type: Type of permission. Valid values are `Unknown`,
               `Any`, `Allow`, `Deny`.
        :param pulumi.Input[str] acl_principal: Principal that is being allowed or denied.
        :param pulumi.Input[str] acl_resource_name: The name of the resource.
        :param pulumi.Input[str] acl_resource_type: The type of resource. Valid values are `Unknown`,
               `Any`, `Topic`, `Group`, `Cluster`, `TransactionalID`.
        :param pulumi.Input[str] resource_pattern_type_filter: The pattern filter. Valid values
               are `Prefixed`, `Any`, `Match`, `Literal`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AclArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A resource for managing Kafka ACLs.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_kafka as kafka

        test = kafka.Acl("test",
            acl_resource_name="syslog",
            acl_resource_type="Topic",
            acl_principal="User:Alice",
            acl_host="*",
            acl_operation="Write",
            acl_permission_type="Deny")
        ```

        :param str resource_name: The name of the resource.
        :param AclArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AclArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl_host: Optional[pulumi.Input[str]] = None,
                 acl_operation: Optional[pulumi.Input[str]] = None,
                 acl_permission_type: Optional[pulumi.Input[str]] = None,
                 acl_principal: Optional[pulumi.Input[str]] = None,
                 acl_resource_name: Optional[pulumi.Input[str]] = None,
                 acl_resource_type: Optional[pulumi.Input[str]] = None,
                 resource_pattern_type_filter: Optional[pulumi.Input[str]] = None,
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
            __props__ = AclArgs.__new__(AclArgs)

            if acl_host is None and not opts.urn:
                raise TypeError("Missing required property 'acl_host'")
            __props__.__dict__["acl_host"] = acl_host
            if acl_operation is None and not opts.urn:
                raise TypeError("Missing required property 'acl_operation'")
            __props__.__dict__["acl_operation"] = acl_operation
            if acl_permission_type is None and not opts.urn:
                raise TypeError("Missing required property 'acl_permission_type'")
            __props__.__dict__["acl_permission_type"] = acl_permission_type
            if acl_principal is None and not opts.urn:
                raise TypeError("Missing required property 'acl_principal'")
            __props__.__dict__["acl_principal"] = acl_principal
            if acl_resource_name is None and not opts.urn:
                raise TypeError("Missing required property 'acl_resource_name'")
            __props__.__dict__["acl_resource_name"] = acl_resource_name
            if acl_resource_type is None and not opts.urn:
                raise TypeError("Missing required property 'acl_resource_type'")
            __props__.__dict__["acl_resource_type"] = acl_resource_type
            __props__.__dict__["resource_pattern_type_filter"] = resource_pattern_type_filter
        super(Acl, __self__).__init__(
            'kafka:index/acl:Acl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl_host: Optional[pulumi.Input[str]] = None,
            acl_operation: Optional[pulumi.Input[str]] = None,
            acl_permission_type: Optional[pulumi.Input[str]] = None,
            acl_principal: Optional[pulumi.Input[str]] = None,
            acl_resource_name: Optional[pulumi.Input[str]] = None,
            acl_resource_type: Optional[pulumi.Input[str]] = None,
            resource_pattern_type_filter: Optional[pulumi.Input[str]] = None) -> 'Acl':
        """
        Get an existing Acl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acl_host: Host from which principal listed in `acl_principal`
               will have access.
        :param pulumi.Input[str] acl_operation: Operation that is being allowed or denied. Valid
               values are `Unknown`, `Any`, `All`, `Read`, `Write`, `Create`, `Delete`, `Alter`,
               `Describe`, `ClusterAction`, `DescribeConfigs`, `AlterConfigs`, `IdempotentWrite`.
        :param pulumi.Input[str] acl_permission_type: Type of permission. Valid values are `Unknown`,
               `Any`, `Allow`, `Deny`.
        :param pulumi.Input[str] acl_principal: Principal that is being allowed or denied.
        :param pulumi.Input[str] acl_resource_name: The name of the resource.
        :param pulumi.Input[str] acl_resource_type: The type of resource. Valid values are `Unknown`,
               `Any`, `Topic`, `Group`, `Cluster`, `TransactionalID`.
        :param pulumi.Input[str] resource_pattern_type_filter: The pattern filter. Valid values
               are `Prefixed`, `Any`, `Match`, `Literal`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AclState.__new__(_AclState)

        __props__.__dict__["acl_host"] = acl_host
        __props__.__dict__["acl_operation"] = acl_operation
        __props__.__dict__["acl_permission_type"] = acl_permission_type
        __props__.__dict__["acl_principal"] = acl_principal
        __props__.__dict__["acl_resource_name"] = acl_resource_name
        __props__.__dict__["acl_resource_type"] = acl_resource_type
        __props__.__dict__["resource_pattern_type_filter"] = resource_pattern_type_filter
        return Acl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aclHost")
    def acl_host(self) -> pulumi.Output[str]:
        """
        Host from which principal listed in `acl_principal`
        will have access.
        """
        return pulumi.get(self, "acl_host")

    @property
    @pulumi.getter(name="aclOperation")
    def acl_operation(self) -> pulumi.Output[str]:
        """
        Operation that is being allowed or denied. Valid
        values are `Unknown`, `Any`, `All`, `Read`, `Write`, `Create`, `Delete`, `Alter`,
        `Describe`, `ClusterAction`, `DescribeConfigs`, `AlterConfigs`, `IdempotentWrite`.
        """
        return pulumi.get(self, "acl_operation")

    @property
    @pulumi.getter(name="aclPermissionType")
    def acl_permission_type(self) -> pulumi.Output[str]:
        """
        Type of permission. Valid values are `Unknown`,
        `Any`, `Allow`, `Deny`.
        """
        return pulumi.get(self, "acl_permission_type")

    @property
    @pulumi.getter(name="aclPrincipal")
    def acl_principal(self) -> pulumi.Output[str]:
        """
        Principal that is being allowed or denied.
        """
        return pulumi.get(self, "acl_principal")

    @property
    @pulumi.getter(name="aclResourceName")
    def acl_resource_name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "acl_resource_name")

    @property
    @pulumi.getter(name="aclResourceType")
    def acl_resource_type(self) -> pulumi.Output[str]:
        """
        The type of resource. Valid values are `Unknown`,
        `Any`, `Topic`, `Group`, `Cluster`, `TransactionalID`.
        """
        return pulumi.get(self, "acl_resource_type")

    @property
    @pulumi.getter(name="resourcePatternTypeFilter")
    def resource_pattern_type_filter(self) -> pulumi.Output[Optional[str]]:
        """
        The pattern filter. Valid values
        are `Prefixed`, `Any`, `Match`, `Literal`.
        """
        return pulumi.get(self, "resource_pattern_type_filter")

