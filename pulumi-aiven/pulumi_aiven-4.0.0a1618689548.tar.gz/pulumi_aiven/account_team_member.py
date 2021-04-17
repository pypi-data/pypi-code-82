# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AccountTeamMemberArgs', 'AccountTeamMember']

@pulumi.input_type
class AccountTeamMemberArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 team_id: pulumi.Input[str],
                 user_email: pulumi.Input[str],
                 accepted: Optional[pulumi.Input[bool]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 invited_by_user_email: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccountTeamMember resource.
        :param pulumi.Input[str] account_id: is a unique account id.
        :param pulumi.Input[str] team_id: is an account team id.
        :param pulumi.Input[str] user_email: is a user email address that first will be invited, and after accepting an invitation,
               he or she becomes a member of a team.
        :param pulumi.Input[bool] accepted: is a boolean flag that determines whether an invitation was accepted or not by the user. 
               `false` value means that the invitation was sent to the user but not yet accepted.
               `true` means that the user accepted the invitation and now a member of an account team.
        :param pulumi.Input[str] create_time: time of creation.
        :param pulumi.Input[str] invited_by_user_email: team invited by user email.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "team_id", team_id)
        pulumi.set(__self__, "user_email", user_email)
        if accepted is not None:
            pulumi.set(__self__, "accepted", accepted)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if invited_by_user_email is not None:
            pulumi.set(__self__, "invited_by_user_email", invited_by_user_email)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        is a unique account id.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Input[str]:
        """
        is an account team id.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> pulumi.Input[str]:
        """
        is a user email address that first will be invited, and after accepting an invitation,
        he or she becomes a member of a team.
        """
        return pulumi.get(self, "user_email")

    @user_email.setter
    def user_email(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_email", value)

    @property
    @pulumi.getter
    def accepted(self) -> Optional[pulumi.Input[bool]]:
        """
        is a boolean flag that determines whether an invitation was accepted or not by the user. 
        `false` value means that the invitation was sent to the user but not yet accepted.
        `true` means that the user accepted the invitation and now a member of an account team.
        """
        return pulumi.get(self, "accepted")

    @accepted.setter
    def accepted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "accepted", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        time of creation.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="invitedByUserEmail")
    def invited_by_user_email(self) -> Optional[pulumi.Input[str]]:
        """
        team invited by user email.
        """
        return pulumi.get(self, "invited_by_user_email")

    @invited_by_user_email.setter
    def invited_by_user_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "invited_by_user_email", value)


@pulumi.input_type
class _AccountTeamMemberState:
    def __init__(__self__, *,
                 accepted: Optional[pulumi.Input[bool]] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 invited_by_user_email: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 user_email: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccountTeamMember resources.
        :param pulumi.Input[bool] accepted: is a boolean flag that determines whether an invitation was accepted or not by the user. 
               `false` value means that the invitation was sent to the user but not yet accepted.
               `true` means that the user accepted the invitation and now a member of an account team.
        :param pulumi.Input[str] account_id: is a unique account id.
        :param pulumi.Input[str] create_time: time of creation.
        :param pulumi.Input[str] invited_by_user_email: team invited by user email.
        :param pulumi.Input[str] team_id: is an account team id.
        :param pulumi.Input[str] user_email: is a user email address that first will be invited, and after accepting an invitation,
               he or she becomes a member of a team.
        """
        if accepted is not None:
            pulumi.set(__self__, "accepted", accepted)
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if create_time is not None:
            pulumi.set(__self__, "create_time", create_time)
        if invited_by_user_email is not None:
            pulumi.set(__self__, "invited_by_user_email", invited_by_user_email)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)
        if user_email is not None:
            pulumi.set(__self__, "user_email", user_email)

    @property
    @pulumi.getter
    def accepted(self) -> Optional[pulumi.Input[bool]]:
        """
        is a boolean flag that determines whether an invitation was accepted or not by the user. 
        `false` value means that the invitation was sent to the user but not yet accepted.
        `true` means that the user accepted the invitation and now a member of an account team.
        """
        return pulumi.get(self, "accepted")

    @accepted.setter
    def accepted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "accepted", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        is a unique account id.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[str]]:
        """
        time of creation.
        """
        return pulumi.get(self, "create_time")

    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "create_time", value)

    @property
    @pulumi.getter(name="invitedByUserEmail")
    def invited_by_user_email(self) -> Optional[pulumi.Input[str]]:
        """
        team invited by user email.
        """
        return pulumi.get(self, "invited_by_user_email")

    @invited_by_user_email.setter
    def invited_by_user_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "invited_by_user_email", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        is an account team id.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> Optional[pulumi.Input[str]]:
        """
        is a user email address that first will be invited, and after accepting an invitation,
        he or she becomes a member of a team.
        """
        return pulumi.get(self, "user_email")

    @user_email.setter
    def user_email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_email", value)


class AccountTeamMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accepted: Optional[pulumi.Input[bool]] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 invited_by_user_email: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 user_email: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## # Account Team Member Resource

        The Account Team Member resource allows the creation and management of an Aiven Account Team Member.

        During the creation of `AccountTeamMember` resource, an email invitation will be sent\
        to a user using `user_email` address. If the user accepts an invitation, he or she will become
        a member of the account team. The deletion of `AccountTeamMember` will not only
        delete the invitation if one was sent but not yet accepted by the user, it will also
        eliminate an account team member if one has accepted an invitation previously.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] accepted: is a boolean flag that determines whether an invitation was accepted or not by the user. 
               `false` value means that the invitation was sent to the user but not yet accepted.
               `true` means that the user accepted the invitation and now a member of an account team.
        :param pulumi.Input[str] account_id: is a unique account id.
        :param pulumi.Input[str] create_time: time of creation.
        :param pulumi.Input[str] invited_by_user_email: team invited by user email.
        :param pulumi.Input[str] team_id: is an account team id.
        :param pulumi.Input[str] user_email: is a user email address that first will be invited, and after accepting an invitation,
               he or she becomes a member of a team.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountTeamMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Account Team Member Resource

        The Account Team Member resource allows the creation and management of an Aiven Account Team Member.

        During the creation of `AccountTeamMember` resource, an email invitation will be sent\
        to a user using `user_email` address. If the user accepts an invitation, he or she will become
        a member of the account team. The deletion of `AccountTeamMember` will not only
        delete the invitation if one was sent but not yet accepted by the user, it will also
        eliminate an account team member if one has accepted an invitation previously.

        :param str resource_name: The name of the resource.
        :param AccountTeamMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountTeamMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accepted: Optional[pulumi.Input[bool]] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 create_time: Optional[pulumi.Input[str]] = None,
                 invited_by_user_email: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 user_email: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccountTeamMemberArgs.__new__(AccountTeamMemberArgs)

            __props__.__dict__["accepted"] = accepted
            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["create_time"] = create_time
            __props__.__dict__["invited_by_user_email"] = invited_by_user_email
            if team_id is None and not opts.urn:
                raise TypeError("Missing required property 'team_id'")
            __props__.__dict__["team_id"] = team_id
            if user_email is None and not opts.urn:
                raise TypeError("Missing required property 'user_email'")
            __props__.__dict__["user_email"] = user_email
        super(AccountTeamMember, __self__).__init__(
            'aiven:index/accountTeamMember:AccountTeamMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accepted: Optional[pulumi.Input[bool]] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            create_time: Optional[pulumi.Input[str]] = None,
            invited_by_user_email: Optional[pulumi.Input[str]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            user_email: Optional[pulumi.Input[str]] = None) -> 'AccountTeamMember':
        """
        Get an existing AccountTeamMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] accepted: is a boolean flag that determines whether an invitation was accepted or not by the user. 
               `false` value means that the invitation was sent to the user but not yet accepted.
               `true` means that the user accepted the invitation and now a member of an account team.
        :param pulumi.Input[str] account_id: is a unique account id.
        :param pulumi.Input[str] create_time: time of creation.
        :param pulumi.Input[str] invited_by_user_email: team invited by user email.
        :param pulumi.Input[str] team_id: is an account team id.
        :param pulumi.Input[str] user_email: is a user email address that first will be invited, and after accepting an invitation,
               he or she becomes a member of a team.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountTeamMemberState.__new__(_AccountTeamMemberState)

        __props__.__dict__["accepted"] = accepted
        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["create_time"] = create_time
        __props__.__dict__["invited_by_user_email"] = invited_by_user_email
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["user_email"] = user_email
        return AccountTeamMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def accepted(self) -> pulumi.Output[bool]:
        """
        is a boolean flag that determines whether an invitation was accepted or not by the user. 
        `false` value means that the invitation was sent to the user but not yet accepted.
        `true` means that the user accepted the invitation and now a member of an account team.
        """
        return pulumi.get(self, "accepted")

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        is a unique account id.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[str]:
        """
        time of creation.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="invitedByUserEmail")
    def invited_by_user_email(self) -> pulumi.Output[str]:
        """
        team invited by user email.
        """
        return pulumi.get(self, "invited_by_user_email")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        is an account team id.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> pulumi.Output[str]:
        """
        is a user email address that first will be invited, and after accepting an invitation,
        he or she becomes a member of a team.
        """
        return pulumi.get(self, "user_email")

