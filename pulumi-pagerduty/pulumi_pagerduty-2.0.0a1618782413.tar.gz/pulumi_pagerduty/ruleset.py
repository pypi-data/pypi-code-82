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

__all__ = ['RulesetArgs', 'Ruleset']

@pulumi.input_type
class RulesetArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 team: Optional[pulumi.Input['RulesetTeamArgs']] = None):
        """
        The set of arguments for constructing a Ruleset resource.
        :param pulumi.Input[str] name: Name of the ruleset.
        :param pulumi.Input['RulesetTeamArgs'] team: Reference to the team that owns the ruleset. If none is specified, only admins have access.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if team is not None:
            pulumi.set(__self__, "team", team)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the ruleset.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def team(self) -> Optional[pulumi.Input['RulesetTeamArgs']]:
        """
        Reference to the team that owns the ruleset. If none is specified, only admins have access.
        """
        return pulumi.get(self, "team")

    @team.setter
    def team(self, value: Optional[pulumi.Input['RulesetTeamArgs']]):
        pulumi.set(self, "team", value)


@pulumi.input_type
class _RulesetState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 routing_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team: Optional[pulumi.Input['RulesetTeamArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Ruleset resources.
        :param pulumi.Input[str] name: Name of the ruleset.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] routing_keys: Routing keys routed to this ruleset.
        :param pulumi.Input['RulesetTeamArgs'] team: Reference to the team that owns the ruleset. If none is specified, only admins have access.
        :param pulumi.Input[str] type: Type of ruleset. Currently only sets to `global`.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if routing_keys is not None:
            pulumi.set(__self__, "routing_keys", routing_keys)
        if team is not None:
            pulumi.set(__self__, "team", team)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the ruleset.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="routingKeys")
    def routing_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Routing keys routed to this ruleset.
        """
        return pulumi.get(self, "routing_keys")

    @routing_keys.setter
    def routing_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "routing_keys", value)

    @property
    @pulumi.getter
    def team(self) -> Optional[pulumi.Input['RulesetTeamArgs']]:
        """
        Reference to the team that owns the ruleset. If none is specified, only admins have access.
        """
        return pulumi.get(self, "team")

    @team.setter
    def team(self, value: Optional[pulumi.Input['RulesetTeamArgs']]):
        pulumi.set(self, "team", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of ruleset. Currently only sets to `global`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Ruleset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team: Optional[pulumi.Input[pulumi.InputType['RulesetTeamArgs']]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        [Rulesets](https://support.pagerduty.com/docs/rulesets) allow you to route events to an endpoint and create collections of event rules, which define sets of actions to take based on event content.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_pagerduty as pagerduty

        foo_team = pagerduty.Team("fooTeam")
        foo_ruleset = pagerduty.Ruleset("fooRuleset", team=pagerduty.RulesetTeamArgs(
            id=foo_team.id,
        ))
        ```

        ## Import

        Rulesets can be imported using the `id`, e.g.

        ```sh
         $ pulumi import pagerduty:index/ruleset:Ruleset main 19acac92-027a-4ea0-b06c-bbf516519601
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the ruleset.
        :param pulumi.Input[pulumi.InputType['RulesetTeamArgs']] team: Reference to the team that owns the ruleset. If none is specified, only admins have access.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[RulesetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        [Rulesets](https://support.pagerduty.com/docs/rulesets) allow you to route events to an endpoint and create collections of event rules, which define sets of actions to take based on event content.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_pagerduty as pagerduty

        foo_team = pagerduty.Team("fooTeam")
        foo_ruleset = pagerduty.Ruleset("fooRuleset", team=pagerduty.RulesetTeamArgs(
            id=foo_team.id,
        ))
        ```

        ## Import

        Rulesets can be imported using the `id`, e.g.

        ```sh
         $ pulumi import pagerduty:index/ruleset:Ruleset main 19acac92-027a-4ea0-b06c-bbf516519601
        ```

        :param str resource_name: The name of the resource.
        :param RulesetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RulesetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 team: Optional[pulumi.Input[pulumi.InputType['RulesetTeamArgs']]] = None,
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
            __props__ = RulesetArgs.__new__(RulesetArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["team"] = team
            __props__.__dict__["routing_keys"] = None
            __props__.__dict__["type"] = None
        super(Ruleset, __self__).__init__(
            'pagerduty:index/ruleset:Ruleset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            routing_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            team: Optional[pulumi.Input[pulumi.InputType['RulesetTeamArgs']]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Ruleset':
        """
        Get an existing Ruleset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the ruleset.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] routing_keys: Routing keys routed to this ruleset.
        :param pulumi.Input[pulumi.InputType['RulesetTeamArgs']] team: Reference to the team that owns the ruleset. If none is specified, only admins have access.
        :param pulumi.Input[str] type: Type of ruleset. Currently only sets to `global`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RulesetState.__new__(_RulesetState)

        __props__.__dict__["name"] = name
        __props__.__dict__["routing_keys"] = routing_keys
        __props__.__dict__["team"] = team
        __props__.__dict__["type"] = type
        return Ruleset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the ruleset.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routingKeys")
    def routing_keys(self) -> pulumi.Output[Sequence[str]]:
        """
        Routing keys routed to this ruleset.
        """
        return pulumi.get(self, "routing_keys")

    @property
    @pulumi.getter
    def team(self) -> pulumi.Output[Optional['outputs.RulesetTeam']]:
        """
        Reference to the team that owns the ruleset. If none is specified, only admins have access.
        """
        return pulumi.get(self, "team")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of ruleset. Currently only sets to `global`.
        """
        return pulumi.get(self, "type")

