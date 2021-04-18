# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['AclRoleArgs', 'AclRole']

@pulumi.input_type
class AclRoleArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_identities: Optional[pulumi.Input[Sequence[pulumi.Input['AclRoleServiceIdentityArgs']]]] = None):
        """
        The set of arguments for constructing a AclRole resource.
        :param pulumi.Input[str] description: A free form human readable description of the role.
        :param pulumi.Input[str] name: The name of the ACL role.
        :param pulumi.Input[str] namespace: The namespace to create the role within.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: The list of policies that should be applied to the role.
        :param pulumi.Input[Sequence[pulumi.Input['AclRoleServiceIdentityArgs']]] service_identities: The list of service identities that should
               be applied to the role.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if service_identities is not None:
            pulumi.set(__self__, "service_identities", service_identities)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A free form human readable description of the role.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ACL role.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the role within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of policies that should be applied to the role.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter(name="serviceIdentities")
    def service_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AclRoleServiceIdentityArgs']]]]:
        """
        The list of service identities that should
        be applied to the role.
        """
        return pulumi.get(self, "service_identities")

    @service_identities.setter
    def service_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AclRoleServiceIdentityArgs']]]]):
        pulumi.set(self, "service_identities", value)


@pulumi.input_type
class _AclRoleState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_identities: Optional[pulumi.Input[Sequence[pulumi.Input['AclRoleServiceIdentityArgs']]]] = None):
        """
        Input properties used for looking up and filtering AclRole resources.
        :param pulumi.Input[str] description: A free form human readable description of the role.
        :param pulumi.Input[str] name: The name of the ACL role.
        :param pulumi.Input[str] namespace: The namespace to create the role within.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: The list of policies that should be applied to the role.
        :param pulumi.Input[Sequence[pulumi.Input['AclRoleServiceIdentityArgs']]] service_identities: The list of service identities that should
               be applied to the role.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if policies is not None:
            pulumi.set(__self__, "policies", policies)
        if service_identities is not None:
            pulumi.set(__self__, "service_identities", service_identities)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A free form human readable description of the role.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the ACL role.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the role within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of policies that should be applied to the role.
        """
        return pulumi.get(self, "policies")

    @policies.setter
    def policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "policies", value)

    @property
    @pulumi.getter(name="serviceIdentities")
    def service_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AclRoleServiceIdentityArgs']]]]:
        """
        The list of service identities that should
        be applied to the role.
        """
        return pulumi.get(self, "service_identities")

    @service_identities.setter
    def service_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AclRoleServiceIdentityArgs']]]]):
        pulumi.set(self, "service_identities", value)


class AclRole(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_identities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclRoleServiceIdentityArgs']]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Starting with Consul 1.5.0, the AclRole can be used to managed Consul ACL roles.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_consul as consul

        read_policy = consul.AclPolicy("read-policy",
            datacenters=["dc1"],
            rules="node \"\" { policy = \"read\" }")
        read = consul.AclRole("read",
            description="bar",
            policies=[read_policy.id],
            service_identities=[consul.AclRoleServiceIdentityArgs(
                service_name="foo",
            )])
        ```

        ## Import

        `consul_acl_role` can be imported

        ```sh
         $ pulumi import consul:index/aclRole:AclRole read 816a195f-6cb1-2e8d-92af-3011ae706318
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A free form human readable description of the role.
        :param pulumi.Input[str] name: The name of the ACL role.
        :param pulumi.Input[str] namespace: The namespace to create the role within.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: The list of policies that should be applied to the role.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclRoleServiceIdentityArgs']]]] service_identities: The list of service identities that should
               be applied to the role.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[AclRoleArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Starting with Consul 1.5.0, the AclRole can be used to managed Consul ACL roles.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_consul as consul

        read_policy = consul.AclPolicy("read-policy",
            datacenters=["dc1"],
            rules="node \"\" { policy = \"read\" }")
        read = consul.AclRole("read",
            description="bar",
            policies=[read_policy.id],
            service_identities=[consul.AclRoleServiceIdentityArgs(
                service_name="foo",
            )])
        ```

        ## Import

        `consul_acl_role` can be imported

        ```sh
         $ pulumi import consul:index/aclRole:AclRole read 816a195f-6cb1-2e8d-92af-3011ae706318
        ```

        :param str resource_name: The name of the resource.
        :param AclRoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AclRoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 service_identities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclRoleServiceIdentityArgs']]]]] = None,
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
            __props__ = AclRoleArgs.__new__(AclRoleArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["policies"] = policies
            __props__.__dict__["service_identities"] = service_identities
        super(AclRole, __self__).__init__(
            'consul:index/aclRole:AclRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            policies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            service_identities: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclRoleServiceIdentityArgs']]]]] = None) -> 'AclRole':
        """
        Get an existing AclRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: A free form human readable description of the role.
        :param pulumi.Input[str] name: The name of the ACL role.
        :param pulumi.Input[str] namespace: The namespace to create the role within.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] policies: The list of policies that should be applied to the role.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['AclRoleServiceIdentityArgs']]]] service_identities: The list of service identities that should
               be applied to the role.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AclRoleState.__new__(_AclRoleState)

        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["policies"] = policies
        __props__.__dict__["service_identities"] = service_identities
        return AclRole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A free form human readable description of the role.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the ACL role.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace to create the role within.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def policies(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of policies that should be applied to the role.
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter(name="serviceIdentities")
    def service_identities(self) -> pulumi.Output[Optional[Sequence['outputs.AclRoleServiceIdentity']]]:
        """
        The list of service identities that should
        be applied to the role.
        """
        return pulumi.get(self, "service_identities")

