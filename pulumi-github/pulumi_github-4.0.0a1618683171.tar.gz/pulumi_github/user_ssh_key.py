# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UserSshKeyArgs', 'UserSshKey']

@pulumi.input_type
class UserSshKeyArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 title: pulumi.Input[str]):
        """
        The set of arguments for constructing a UserSshKey resource.
        :param pulumi.Input[str] key: The public SSH key to add to your GitHub account.
        :param pulumi.Input[str] title: A descriptive name for the new key. e.g. `Personal MacBook Air`
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The public SSH key to add to your GitHub account.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        A descriptive name for the new key. e.g. `Personal MacBook Air`
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)


@pulumi.input_type
class _UserSshKeyState:
    def __init__(__self__, *,
                 etag: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UserSshKey resources.
        :param pulumi.Input[str] key: The public SSH key to add to your GitHub account.
        :param pulumi.Input[str] title: A descriptive name for the new key. e.g. `Personal MacBook Air`
        :param pulumi.Input[str] url: The URL of the SSH key
        """
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The public SSH key to add to your GitHub account.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        A descriptive name for the new key. e.g. `Personal MacBook Air`
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the SSH key
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class UserSshKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a GitHub user's SSH key resource.

        This resource allows you to add/remove SSH keys from your user account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example = github.UserSshKey("example",
            title="example title",
            key=(lambda path: open(path).read())("~/.ssh/id_rsa.pub"))
        ```

        ## Import

        SSH keys can be imported using their ID e.g.

        ```sh
         $ pulumi import github:index/userSshKey:UserSshKey example 1234567
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The public SSH key to add to your GitHub account.
        :param pulumi.Input[str] title: A descriptive name for the new key. e.g. `Personal MacBook Air`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserSshKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a GitHub user's SSH key resource.

        This resource allows you to add/remove SSH keys from your user account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example = github.UserSshKey("example",
            title="example title",
            key=(lambda path: open(path).read())("~/.ssh/id_rsa.pub"))
        ```

        ## Import

        SSH keys can be imported using their ID e.g.

        ```sh
         $ pulumi import github:index/userSshKey:UserSshKey example 1234567
        ```

        :param str resource_name: The name of the resource.
        :param UserSshKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserSshKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
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
            __props__ = UserSshKeyArgs.__new__(UserSshKeyArgs)

            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["etag"] = None
            __props__.__dict__["url"] = None
        super(UserSshKey, __self__).__init__(
            'github:index/userSshKey:UserSshKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            etag: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'UserSshKey':
        """
        Get an existing UserSshKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The public SSH key to add to your GitHub account.
        :param pulumi.Input[str] title: A descriptive name for the new key. e.g. `Personal MacBook Air`
        :param pulumi.Input[str] url: The URL of the SSH key
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserSshKeyState.__new__(_UserSshKeyState)

        __props__.__dict__["etag"] = etag
        __props__.__dict__["key"] = key
        __props__.__dict__["title"] = title
        __props__.__dict__["url"] = url
        return UserSshKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The public SSH key to add to your GitHub account.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        A descriptive name for the new key. e.g. `Personal MacBook Air`
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL of the SSH key
        """
        return pulumi.get(self, "url")

