# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AccountArgs', 'Account']

@pulumi.input_type
class AccountArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 account_name_prefix: Optional[pulumi.Input[str]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 payer_account_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Account resource.
        :param pulumi.Input[str] display_name: Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (_), dots (.) And dashes (-).
        :param pulumi.Input[str] account_name_prefix: The name prefix of account.
        :param pulumi.Input[str] folder_id: The ID of the parent folder.
        :param pulumi.Input[str] payer_account_id: Settlement account ID. If the value is empty, the current account will be used for settlement.
        """
        pulumi.set(__self__, "display_name", display_name)
        if account_name_prefix is not None:
            pulumi.set(__self__, "account_name_prefix", account_name_prefix)
        if folder_id is not None:
            pulumi.set(__self__, "folder_id", folder_id)
        if payer_account_id is not None:
            pulumi.set(__self__, "payer_account_id", payer_account_id)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (_), dots (.) And dashes (-).
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="accountNamePrefix")
    def account_name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The name prefix of account.
        """
        return pulumi.get(self, "account_name_prefix")

    @account_name_prefix.setter
    def account_name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name_prefix", value)

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the parent folder.
        """
        return pulumi.get(self, "folder_id")

    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_id", value)

    @property
    @pulumi.getter(name="payerAccountId")
    def payer_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Settlement account ID. If the value is empty, the current account will be used for settlement.
        """
        return pulumi.get(self, "payer_account_id")

    @payer_account_id.setter
    def payer_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payer_account_id", value)


@pulumi.input_type
class _AccountState:
    def __init__(__self__, *,
                 account_name_prefix: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 join_method: Optional[pulumi.Input[str]] = None,
                 join_time: Optional[pulumi.Input[str]] = None,
                 modify_time: Optional[pulumi.Input[str]] = None,
                 payer_account_id: Optional[pulumi.Input[str]] = None,
                 resource_directory_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Account resources.
        :param pulumi.Input[str] account_name_prefix: The name prefix of account.
        :param pulumi.Input[str] display_name: Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (_), dots (.) And dashes (-).
        :param pulumi.Input[str] folder_id: The ID of the parent folder.
        :param pulumi.Input[str] join_method: Ways for members to join the resource directory. Valid values: `invited`, `created`.
        :param pulumi.Input[str] join_time: The time when the member joined the resource directory.
        :param pulumi.Input[str] modify_time: The modification time of the invitation.
        :param pulumi.Input[str] payer_account_id: Settlement account ID. If the value is empty, the current account will be used for settlement.
        :param pulumi.Input[str] resource_directory_id: Resource directory ID.
        :param pulumi.Input[str] status: Member joining status. Valid values: `CreateSuccess`,`CreateVerifying`,`CreateFailed`,`CreateExpired`,`CreateCancelled`,`PromoteVerifying`,`PromoteFailed`,`PromoteExpired`,`PromoteCancelled`,`PromoteSuccess`,`InviteSuccess`,`Removed`.
        :param pulumi.Input[str] type: Member type. The value of `ResourceAccount` indicates the resource account.
        """
        if account_name_prefix is not None:
            pulumi.set(__self__, "account_name_prefix", account_name_prefix)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if folder_id is not None:
            pulumi.set(__self__, "folder_id", folder_id)
        if join_method is not None:
            pulumi.set(__self__, "join_method", join_method)
        if join_time is not None:
            pulumi.set(__self__, "join_time", join_time)
        if modify_time is not None:
            pulumi.set(__self__, "modify_time", modify_time)
        if payer_account_id is not None:
            pulumi.set(__self__, "payer_account_id", payer_account_id)
        if resource_directory_id is not None:
            pulumi.set(__self__, "resource_directory_id", resource_directory_id)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accountNamePrefix")
    def account_name_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The name prefix of account.
        """
        return pulumi.get(self, "account_name_prefix")

    @account_name_prefix.setter
    def account_name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_name_prefix", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (_), dots (.) And dashes (-).
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the parent folder.
        """
        return pulumi.get(self, "folder_id")

    @folder_id.setter
    def folder_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "folder_id", value)

    @property
    @pulumi.getter(name="joinMethod")
    def join_method(self) -> Optional[pulumi.Input[str]]:
        """
        Ways for members to join the resource directory. Valid values: `invited`, `created`.
        """
        return pulumi.get(self, "join_method")

    @join_method.setter
    def join_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "join_method", value)

    @property
    @pulumi.getter(name="joinTime")
    def join_time(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the member joined the resource directory.
        """
        return pulumi.get(self, "join_time")

    @join_time.setter
    def join_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "join_time", value)

    @property
    @pulumi.getter(name="modifyTime")
    def modify_time(self) -> Optional[pulumi.Input[str]]:
        """
        The modification time of the invitation.
        """
        return pulumi.get(self, "modify_time")

    @modify_time.setter
    def modify_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modify_time", value)

    @property
    @pulumi.getter(name="payerAccountId")
    def payer_account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Settlement account ID. If the value is empty, the current account will be used for settlement.
        """
        return pulumi.get(self, "payer_account_id")

    @payer_account_id.setter
    def payer_account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payer_account_id", value)

    @property
    @pulumi.getter(name="resourceDirectoryId")
    def resource_directory_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource directory ID.
        """
        return pulumi.get(self, "resource_directory_id")

    @resource_directory_id.setter
    def resource_directory_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_directory_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Member joining status. Valid values: `CreateSuccess`,`CreateVerifying`,`CreateFailed`,`CreateExpired`,`CreateCancelled`,`PromoteVerifying`,`PromoteFailed`,`PromoteExpired`,`PromoteCancelled`,`PromoteSuccess`,`InviteSuccess`,`Removed`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Member type. The value of `ResourceAccount` indicates the resource account.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Account(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name_prefix: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 payer_account_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Resource Manager Account resource. Member accounts are containers for resources in a resource directory. These accounts isolate resources and serve as organizational units in the resource directory. You can create member accounts in a folder and then manage them in a unified manner.
        For information about Resource Manager Account and how to use it, see [What is Resource Manager Account](https://www.alibabacloud.com/help/en/doc-detail/111231.htm).

        > **NOTE:** Available in v1.83.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Add a Resource Manager Account.
        f1 = alicloud.resourcemanager.Folder("f1", folder_name="test1")
        example = alicloud.resourcemanager.Account("example",
            display_name="RDAccount",
            folder_id=f1.id)
        ```

        ## Import

        Resource Manager Account can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/account:Account example 13148890145*****
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name_prefix: The name prefix of account.
        :param pulumi.Input[str] display_name: Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (_), dots (.) And dashes (-).
        :param pulumi.Input[str] folder_id: The ID of the parent folder.
        :param pulumi.Input[str] payer_account_id: Settlement account ID. If the value is empty, the current account will be used for settlement.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Resource Manager Account resource. Member accounts are containers for resources in a resource directory. These accounts isolate resources and serve as organizational units in the resource directory. You can create member accounts in a folder and then manage them in a unified manner.
        For information about Resource Manager Account and how to use it, see [What is Resource Manager Account](https://www.alibabacloud.com/help/en/doc-detail/111231.htm).

        > **NOTE:** Available in v1.83.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        # Add a Resource Manager Account.
        f1 = alicloud.resourcemanager.Folder("f1", folder_name="test1")
        example = alicloud.resourcemanager.Account("example",
            display_name="RDAccount",
            folder_id=f1.id)
        ```

        ## Import

        Resource Manager Account can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:resourcemanager/account:Account example 13148890145*****
        ```

        :param str resource_name: The name of the resource.
        :param AccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name_prefix: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 folder_id: Optional[pulumi.Input[str]] = None,
                 payer_account_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = AccountArgs.__new__(AccountArgs)

            __props__.__dict__["account_name_prefix"] = account_name_prefix
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["folder_id"] = folder_id
            __props__.__dict__["payer_account_id"] = payer_account_id
            __props__.__dict__["join_method"] = None
            __props__.__dict__["join_time"] = None
            __props__.__dict__["modify_time"] = None
            __props__.__dict__["resource_directory_id"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        super(Account, __self__).__init__(
            'alicloud:resourcemanager/account:Account',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_name_prefix: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            folder_id: Optional[pulumi.Input[str]] = None,
            join_method: Optional[pulumi.Input[str]] = None,
            join_time: Optional[pulumi.Input[str]] = None,
            modify_time: Optional[pulumi.Input[str]] = None,
            payer_account_id: Optional[pulumi.Input[str]] = None,
            resource_directory_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'Account':
        """
        Get an existing Account resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name_prefix: The name prefix of account.
        :param pulumi.Input[str] display_name: Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (_), dots (.) And dashes (-).
        :param pulumi.Input[str] folder_id: The ID of the parent folder.
        :param pulumi.Input[str] join_method: Ways for members to join the resource directory. Valid values: `invited`, `created`.
        :param pulumi.Input[str] join_time: The time when the member joined the resource directory.
        :param pulumi.Input[str] modify_time: The modification time of the invitation.
        :param pulumi.Input[str] payer_account_id: Settlement account ID. If the value is empty, the current account will be used for settlement.
        :param pulumi.Input[str] resource_directory_id: Resource directory ID.
        :param pulumi.Input[str] status: Member joining status. Valid values: `CreateSuccess`,`CreateVerifying`,`CreateFailed`,`CreateExpired`,`CreateCancelled`,`PromoteVerifying`,`PromoteFailed`,`PromoteExpired`,`PromoteCancelled`,`PromoteSuccess`,`InviteSuccess`,`Removed`.
        :param pulumi.Input[str] type: Member type. The value of `ResourceAccount` indicates the resource account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountState.__new__(_AccountState)

        __props__.__dict__["account_name_prefix"] = account_name_prefix
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["folder_id"] = folder_id
        __props__.__dict__["join_method"] = join_method
        __props__.__dict__["join_time"] = join_time
        __props__.__dict__["modify_time"] = modify_time
        __props__.__dict__["payer_account_id"] = payer_account_id
        __props__.__dict__["resource_directory_id"] = resource_directory_id
        __props__.__dict__["status"] = status
        __props__.__dict__["type"] = type
        return Account(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountNamePrefix")
    def account_name_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        The name prefix of account.
        """
        return pulumi.get(self, "account_name_prefix")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Member name. The length is 2 ~ 50 characters or Chinese characters, which can include Chinese characters, English letters, numbers, underscores (_), dots (.) And dashes (-).
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="folderId")
    def folder_id(self) -> pulumi.Output[str]:
        """
        The ID of the parent folder.
        """
        return pulumi.get(self, "folder_id")

    @property
    @pulumi.getter(name="joinMethod")
    def join_method(self) -> pulumi.Output[str]:
        """
        Ways for members to join the resource directory. Valid values: `invited`, `created`.
        """
        return pulumi.get(self, "join_method")

    @property
    @pulumi.getter(name="joinTime")
    def join_time(self) -> pulumi.Output[str]:
        """
        The time when the member joined the resource directory.
        """
        return pulumi.get(self, "join_time")

    @property
    @pulumi.getter(name="modifyTime")
    def modify_time(self) -> pulumi.Output[str]:
        """
        The modification time of the invitation.
        """
        return pulumi.get(self, "modify_time")

    @property
    @pulumi.getter(name="payerAccountId")
    def payer_account_id(self) -> pulumi.Output[Optional[str]]:
        """
        Settlement account ID. If the value is empty, the current account will be used for settlement.
        """
        return pulumi.get(self, "payer_account_id")

    @property
    @pulumi.getter(name="resourceDirectoryId")
    def resource_directory_id(self) -> pulumi.Output[str]:
        """
        Resource directory ID.
        """
        return pulumi.get(self, "resource_directory_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Member joining status. Valid values: `CreateSuccess`,`CreateVerifying`,`CreateFailed`,`CreateExpired`,`CreateCancelled`,`PromoteVerifying`,`PromoteFailed`,`PromoteExpired`,`PromoteCancelled`,`PromoteSuccess`,`InviteSuccess`,`Removed`.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Member type. The value of `ResourceAccount` indicates the resource account.
        """
        return pulumi.get(self, "type")

