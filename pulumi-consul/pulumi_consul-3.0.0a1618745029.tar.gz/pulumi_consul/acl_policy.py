# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AclPolicyArgs', 'AclPolicy']

@pulumi.input_type
class AclPolicyArgs:
    def __init__(__self__, *,
                 rules: pulumi.Input[str],
                 datacenters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AclPolicy resource.
        :param pulumi.Input[str] rules: The rules of the policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datacenters: The datacenters of the policy.
        :param pulumi.Input[str] description: The description of the policy.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] namespace: The namespace to create the policy within.
        """
        pulumi.set(__self__, "rules", rules)
        if datacenters is not None:
            pulumi.set(__self__, "datacenters", datacenters)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[str]:
        """
        The rules of the policy.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[str]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def datacenters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The datacenters of the policy.
        """
        return pulumi.get(self, "datacenters")

    @datacenters.setter
    def datacenters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "datacenters", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the policy within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)


@pulumi.input_type
class _AclPolicyState:
    def __init__(__self__, *,
                 datacenters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AclPolicy resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datacenters: The datacenters of the policy.
        :param pulumi.Input[str] description: The description of the policy.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] namespace: The namespace to create the policy within.
        :param pulumi.Input[str] rules: The rules of the policy.
        """
        if datacenters is not None:
            pulumi.set(__self__, "datacenters", datacenters)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter
    def datacenters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The datacenters of the policy.
        """
        return pulumi.get(self, "datacenters")

    @datacenters.setter
    def datacenters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "datacenters", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the policy.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace to create the policy within.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[str]]:
        """
        The rules of the policy.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rules", value)


class AclPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Starting with Consul 1.4.0, the AclPolicy can be used to managed Consul ACL policies.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_consul as consul

        test = consul.AclPolicy("test",
            datacenters=["dc1"],
            rules=\"\"\"node_prefix "" {
          policy = "read"
        }

        \"\"\")
        ```

        ## Import

        `consul_acl_policy` can be imported

        ```sh
         $ pulumi import consul:index/aclPolicy:AclPolicy my-policy 1c90ef03-a6dd-6a8c-ac49-042ad3752896
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datacenters: The datacenters of the policy.
        :param pulumi.Input[str] description: The description of the policy.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] namespace: The namespace to create the policy within.
        :param pulumi.Input[str] rules: The rules of the policy.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AclPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Starting with Consul 1.4.0, the AclPolicy can be used to managed Consul ACL policies.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_consul as consul

        test = consul.AclPolicy("test",
            datacenters=["dc1"],
            rules=\"\"\"node_prefix "" {
          policy = "read"
        }

        \"\"\")
        ```

        ## Import

        `consul_acl_policy` can be imported

        ```sh
         $ pulumi import consul:index/aclPolicy:AclPolicy my-policy 1c90ef03-a6dd-6a8c-ac49-042ad3752896
        ```

        :param str resource_name: The name of the resource.
        :param AclPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AclPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 datacenters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[str]] = None,
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
            __props__ = AclPolicyArgs.__new__(AclPolicyArgs)

            __props__.__dict__["datacenters"] = datacenters
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace"] = namespace
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
        super(AclPolicy, __self__).__init__(
            'consul:index/aclPolicy:AclPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            datacenters: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[str]] = None) -> 'AclPolicy':
        """
        Get an existing AclPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] datacenters: The datacenters of the policy.
        :param pulumi.Input[str] description: The description of the policy.
        :param pulumi.Input[str] name: The name of the policy.
        :param pulumi.Input[str] namespace: The namespace to create the policy within.
        :param pulumi.Input[str] rules: The rules of the policy.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AclPolicyState.__new__(_AclPolicyState)

        __props__.__dict__["datacenters"] = datacenters
        __props__.__dict__["description"] = description
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["rules"] = rules
        return AclPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def datacenters(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The datacenters of the policy.
        """
        return pulumi.get(self, "datacenters")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the policy.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The namespace to create the policy within.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[str]:
        """
        The rules of the policy.
        """
        return pulumi.get(self, "rules")

