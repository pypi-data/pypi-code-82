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

__all__ = ['PolicyArgs', 'Policy']

@pulumi.input_type
class PolicyArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 controls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 published_copy: Optional[pulumi.Input[str]] = None,
                 requires: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]]] = None,
                 strategy: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Policy resource.
        :param pulumi.Input[str] name: Name of the Policy ( policy name should be in full path which is combination of partition and policy name )
        :param pulumi.Input[Sequence[pulumi.Input[str]]] controls: Specifies the controls
        :param pulumi.Input[str] published_copy: If you want to publish the policy else it will be deployed in Drafts mode.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] requires: Specifies the protocol
        :param pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]] rules: Rules can be applied using the policy
        :param pulumi.Input[str] strategy: Specifies the match strategy
        """
        pulumi.set(__self__, "name", name)
        if controls is not None:
            pulumi.set(__self__, "controls", controls)
        if published_copy is not None:
            pulumi.set(__self__, "published_copy", published_copy)
        if requires is not None:
            pulumi.set(__self__, "requires", requires)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if strategy is not None:
            pulumi.set(__self__, "strategy", strategy)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the Policy ( policy name should be in full path which is combination of partition and policy name )
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def controls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the controls
        """
        return pulumi.get(self, "controls")

    @controls.setter
    def controls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "controls", value)

    @property
    @pulumi.getter(name="publishedCopy")
    def published_copy(self) -> Optional[pulumi.Input[str]]:
        """
        If you want to publish the policy else it will be deployed in Drafts mode.
        """
        return pulumi.get(self, "published_copy")

    @published_copy.setter
    def published_copy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "published_copy", value)

    @property
    @pulumi.getter
    def requires(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the protocol
        """
        return pulumi.get(self, "requires")

    @requires.setter
    def requires(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "requires", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]]]:
        """
        Rules can be applied using the policy
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the match strategy
        """
        return pulumi.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strategy", value)


@pulumi.input_type
class _PolicyState:
    def __init__(__self__, *,
                 controls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 published_copy: Optional[pulumi.Input[str]] = None,
                 requires: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]]] = None,
                 strategy: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Policy resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] controls: Specifies the controls
        :param pulumi.Input[str] name: Name of the Policy ( policy name should be in full path which is combination of partition and policy name )
        :param pulumi.Input[str] published_copy: If you want to publish the policy else it will be deployed in Drafts mode.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] requires: Specifies the protocol
        :param pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]] rules: Rules can be applied using the policy
        :param pulumi.Input[str] strategy: Specifies the match strategy
        """
        if controls is not None:
            pulumi.set(__self__, "controls", controls)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if published_copy is not None:
            pulumi.set(__self__, "published_copy", published_copy)
        if requires is not None:
            pulumi.set(__self__, "requires", requires)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if strategy is not None:
            pulumi.set(__self__, "strategy", strategy)

    @property
    @pulumi.getter
    def controls(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the controls
        """
        return pulumi.get(self, "controls")

    @controls.setter
    def controls(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "controls", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Policy ( policy name should be in full path which is combination of partition and policy name )
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publishedCopy")
    def published_copy(self) -> Optional[pulumi.Input[str]]:
        """
        If you want to publish the policy else it will be deployed in Drafts mode.
        """
        return pulumi.get(self, "published_copy")

    @published_copy.setter
    def published_copy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "published_copy", value)

    @property
    @pulumi.getter
    def requires(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Specifies the protocol
        """
        return pulumi.get(self, "requires")

    @requires.setter
    def requires(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "requires", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]]]:
        """
        Rules can be applied using the policy
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def strategy(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the match strategy
        """
        return pulumi.get(self, "strategy")

    @strategy.setter
    def strategy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "strategy", value)


class Policy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 controls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 published_copy: Optional[pulumi.Input[str]] = None,
                 requires: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyRuleArgs']]]]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        `ltm.Policy` Configures ltm policies to manage traffic assigned to a virtual server

        For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        mypool = f5bigip.ltm.Pool("mypool",
            name="/Common/test-pool",
            allow_nat="yes",
            allow_snat="yes",
            load_balancing_mode="round-robin")
        test_policy = f5bigip.ltm.Policy("test-policy",
            name="/Common/test-policy",
            strategy="first-match",
            requires=["http"],
            controls=["forwarding"],
            rules=[f5bigip.ltm.PolicyRuleArgs(
                name="rule6",
                actions=[f5bigip.ltm.PolicyRuleActionArgs(
                    forward=True,
                    pool=mypool.name,
                )],
            )],
            opts=pulumi.ResourceOptions(depends_on=[mypool]))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] controls: Specifies the controls
        :param pulumi.Input[str] name: Name of the Policy ( policy name should be in full path which is combination of partition and policy name )
        :param pulumi.Input[str] published_copy: If you want to publish the policy else it will be deployed in Drafts mode.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] requires: Specifies the protocol
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyRuleArgs']]]] rules: Rules can be applied using the policy
        :param pulumi.Input[str] strategy: Specifies the match strategy
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        `ltm.Policy` Configures ltm policies to manage traffic assigned to a virtual server

        For resources should be named with their "full path". The full path is the combination of the partition + name of the resource. For example /Common/my-pool.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_f5bigip as f5bigip

        mypool = f5bigip.ltm.Pool("mypool",
            name="/Common/test-pool",
            allow_nat="yes",
            allow_snat="yes",
            load_balancing_mode="round-robin")
        test_policy = f5bigip.ltm.Policy("test-policy",
            name="/Common/test-policy",
            strategy="first-match",
            requires=["http"],
            controls=["forwarding"],
            rules=[f5bigip.ltm.PolicyRuleArgs(
                name="rule6",
                actions=[f5bigip.ltm.PolicyRuleActionArgs(
                    forward=True,
                    pool=mypool.name,
                )],
            )],
            opts=pulumi.ResourceOptions(depends_on=[mypool]))
        ```

        :param str resource_name: The name of the resource.
        :param PolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 controls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 published_copy: Optional[pulumi.Input[str]] = None,
                 requires: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyRuleArgs']]]]] = None,
                 strategy: Optional[pulumi.Input[str]] = None,
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
            __props__ = PolicyArgs.__new__(PolicyArgs)

            __props__.__dict__["controls"] = controls
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            __props__.__dict__["published_copy"] = published_copy
            __props__.__dict__["requires"] = requires
            __props__.__dict__["rules"] = rules
            __props__.__dict__["strategy"] = strategy
        super(Policy, __self__).__init__(
            'f5bigip:ltm/policy:Policy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            controls: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            published_copy: Optional[pulumi.Input[str]] = None,
            requires: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyRuleArgs']]]]] = None,
            strategy: Optional[pulumi.Input[str]] = None) -> 'Policy':
        """
        Get an existing Policy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] controls: Specifies the controls
        :param pulumi.Input[str] name: Name of the Policy ( policy name should be in full path which is combination of partition and policy name )
        :param pulumi.Input[str] published_copy: If you want to publish the policy else it will be deployed in Drafts mode.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] requires: Specifies the protocol
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyRuleArgs']]]] rules: Rules can be applied using the policy
        :param pulumi.Input[str] strategy: Specifies the match strategy
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PolicyState.__new__(_PolicyState)

        __props__.__dict__["controls"] = controls
        __props__.__dict__["name"] = name
        __props__.__dict__["published_copy"] = published_copy
        __props__.__dict__["requires"] = requires
        __props__.__dict__["rules"] = rules
        __props__.__dict__["strategy"] = strategy
        return Policy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def controls(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies the controls
        """
        return pulumi.get(self, "controls")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Policy ( policy name should be in full path which is combination of partition and policy name )
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publishedCopy")
    def published_copy(self) -> pulumi.Output[Optional[str]]:
        """
        If you want to publish the policy else it will be deployed in Drafts mode.
        """
        return pulumi.get(self, "published_copy")

    @property
    @pulumi.getter
    def requires(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Specifies the protocol
        """
        return pulumi.get(self, "requires")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence['outputs.PolicyRule']]]:
        """
        Rules can be applied using the policy
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def strategy(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the match strategy
        """
        return pulumi.get(self, "strategy")

