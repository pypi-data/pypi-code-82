# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetAccountTeamMemberResult',
    'AwaitableGetAccountTeamMemberResult',
    'get_account_team_member',
]

@pulumi.output_type
class GetAccountTeamMemberResult:
    """
    A collection of values returned by getAccountTeamMember.
    """
    def __init__(__self__, accepted=None, account_id=None, create_time=None, id=None, invited_by_user_email=None, team_id=None, user_email=None):
        if accepted and not isinstance(accepted, bool):
            raise TypeError("Expected argument 'accepted' to be a bool")
        pulumi.set(__self__, "accepted", accepted)
        if account_id and not isinstance(account_id, str):
            raise TypeError("Expected argument 'account_id' to be a str")
        pulumi.set(__self__, "account_id", account_id)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if invited_by_user_email and not isinstance(invited_by_user_email, str):
            raise TypeError("Expected argument 'invited_by_user_email' to be a str")
        pulumi.set(__self__, "invited_by_user_email", invited_by_user_email)
        if team_id and not isinstance(team_id, str):
            raise TypeError("Expected argument 'team_id' to be a str")
        pulumi.set(__self__, "team_id", team_id)
        if user_email and not isinstance(user_email, str):
            raise TypeError("Expected argument 'user_email' to be a str")
        pulumi.set(__self__, "user_email", user_email)

    @property
    @pulumi.getter
    def accepted(self) -> bool:
        """
        is a boolean flag that determines whether an invitation was accepted or not by the user. 
        `false` value means that the invitation was sent to the user but not yet accepted.
        `true` means that the user accepted the invitation and is now a member of an account team.
        """
        return pulumi.get(self, "accepted")

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        time of creation.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="invitedByUserEmail")
    def invited_by_user_email(self) -> str:
        """
        team invited by user email.
        """
        return pulumi.get(self, "invited_by_user_email")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> str:
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter(name="userEmail")
    def user_email(self) -> str:
        return pulumi.get(self, "user_email")


class AwaitableGetAccountTeamMemberResult(GetAccountTeamMemberResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAccountTeamMemberResult(
            accepted=self.accepted,
            account_id=self.account_id,
            create_time=self.create_time,
            id=self.id,
            invited_by_user_email=self.invited_by_user_email,
            team_id=self.team_id,
            user_email=self.user_email)


def get_account_team_member(accepted: Optional[bool] = None,
                            account_id: Optional[str] = None,
                            create_time: Optional[str] = None,
                            invited_by_user_email: Optional[str] = None,
                            team_id: Optional[str] = None,
                            user_email: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAccountTeamMemberResult:
    """
    ## # Account Team Member Data Source

    The Account Team Member data source provides information about the existing Aiven Account Team Member.


    :param bool accepted: is a boolean flag that determines whether an invitation was accepted or not by the user. 
           `false` value means that the invitation was sent to the user but not yet accepted.
           `true` means that the user accepted the invitation and is now a member of an account team.
    :param str account_id: is a unique account id.
    :param str create_time: time of creation.
    :param str invited_by_user_email: team invited by user email.
    :param str team_id: is an account team id.
    :param str user_email: is a user email address that first will be invited, and after accepting an invitation,
           he or she becomes a member of a team.
    """
    __args__ = dict()
    __args__['accepted'] = accepted
    __args__['accountId'] = account_id
    __args__['createTime'] = create_time
    __args__['invitedByUserEmail'] = invited_by_user_email
    __args__['teamId'] = team_id
    __args__['userEmail'] = user_email
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aiven:index/getAccountTeamMember:getAccountTeamMember', __args__, opts=opts, typ=GetAccountTeamMemberResult).value

    return AwaitableGetAccountTeamMemberResult(
        accepted=__ret__.accepted,
        account_id=__ret__.account_id,
        create_time=__ret__.create_time,
        id=__ret__.id,
        invited_by_user_email=__ret__.invited_by_user_email,
        team_id=__ret__.team_id,
        user_email=__ret__.user_email)
