# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['RepositoryPullRequestArgs', 'RepositoryPullRequest']

@pulumi.input_type
class RepositoryPullRequestArgs:
    def __init__(__self__, *,
                 base_ref: pulumi.Input[str],
                 base_repository: pulumi.Input[str],
                 head_ref: pulumi.Input[str],
                 title: pulumi.Input[str],
                 body: Optional[pulumi.Input[str]] = None,
                 maintainer_can_modify: Optional[pulumi.Input[bool]] = None,
                 owner: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RepositoryPullRequest resource.
        :param pulumi.Input[str] base_ref: Name of the branch serving as the base of the Pull Request.
        :param pulumi.Input[str] base_repository: Name of the base repository to retrieve the Pull Requests from.
        :param pulumi.Input[str] head_ref: Name of the branch serving as the head of the Pull Request.
        :param pulumi.Input[str] title: The title of the Pull Request.
        :param pulumi.Input[str] body: Body of the Pull Request.
        :param pulumi.Input[bool] maintainer_can_modify: Controls whether the base repository maintainers can modify the Pull Request. Default: false.
        :param pulumi.Input[str] owner: Owner of the repository. If not provided, the provider's default owner is used.
        """
        pulumi.set(__self__, "base_ref", base_ref)
        pulumi.set(__self__, "base_repository", base_repository)
        pulumi.set(__self__, "head_ref", head_ref)
        pulumi.set(__self__, "title", title)
        if body is not None:
            pulumi.set(__self__, "body", body)
        if maintainer_can_modify is not None:
            pulumi.set(__self__, "maintainer_can_modify", maintainer_can_modify)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)

    @property
    @pulumi.getter(name="baseRef")
    def base_ref(self) -> pulumi.Input[str]:
        """
        Name of the branch serving as the base of the Pull Request.
        """
        return pulumi.get(self, "base_ref")

    @base_ref.setter
    def base_ref(self, value: pulumi.Input[str]):
        pulumi.set(self, "base_ref", value)

    @property
    @pulumi.getter(name="baseRepository")
    def base_repository(self) -> pulumi.Input[str]:
        """
        Name of the base repository to retrieve the Pull Requests from.
        """
        return pulumi.get(self, "base_repository")

    @base_repository.setter
    def base_repository(self, value: pulumi.Input[str]):
        pulumi.set(self, "base_repository", value)

    @property
    @pulumi.getter(name="headRef")
    def head_ref(self) -> pulumi.Input[str]:
        """
        Name of the branch serving as the head of the Pull Request.
        """
        return pulumi.get(self, "head_ref")

    @head_ref.setter
    def head_ref(self, value: pulumi.Input[str]):
        pulumi.set(self, "head_ref", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The title of the Pull Request.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        Body of the Pull Request.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="maintainerCanModify")
    def maintainer_can_modify(self) -> Optional[pulumi.Input[bool]]:
        """
        Controls whether the base repository maintainers can modify the Pull Request. Default: false.
        """
        return pulumi.get(self, "maintainer_can_modify")

    @maintainer_can_modify.setter
    def maintainer_can_modify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "maintainer_can_modify", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        Owner of the repository. If not provided, the provider's default owner is used.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)


@pulumi.input_type
class _RepositoryPullRequestState:
    def __init__(__self__, *,
                 base_ref: Optional[pulumi.Input[str]] = None,
                 base_repository: Optional[pulumi.Input[str]] = None,
                 base_sha: Optional[pulumi.Input[str]] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 draft: Optional[pulumi.Input[bool]] = None,
                 head_ref: Optional[pulumi.Input[str]] = None,
                 head_sha: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 maintainer_can_modify: Optional[pulumi.Input[bool]] = None,
                 number: Optional[pulumi.Input[int]] = None,
                 opened_at: Optional[pulumi.Input[int]] = None,
                 opened_by: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering RepositoryPullRequest resources.
        :param pulumi.Input[str] base_ref: Name of the branch serving as the base of the Pull Request.
        :param pulumi.Input[str] base_repository: Name of the base repository to retrieve the Pull Requests from.
        :param pulumi.Input[str] base_sha: Head commit SHA of the Pull Request base.
        :param pulumi.Input[str] body: Body of the Pull Request.
        :param pulumi.Input[bool] draft: Indicates Whether this Pull Request is a draft.
        :param pulumi.Input[str] head_ref: Name of the branch serving as the head of the Pull Request.
        :param pulumi.Input[str] head_sha: Head commit SHA of the Pull Request head.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of label names set on the Pull Request.
        :param pulumi.Input[bool] maintainer_can_modify: Controls whether the base repository maintainers can modify the Pull Request. Default: false.
        :param pulumi.Input[int] number: The number of the Pull Request within the repository.
        :param pulumi.Input[int] opened_at: Unix timestamp indicating the Pull Request creation time.
        :param pulumi.Input[str] opened_by: GitHub login of the user who opened the Pull Request.
        :param pulumi.Input[str] owner: Owner of the repository. If not provided, the provider's default owner is used.
        :param pulumi.Input[str] state: the current Pull Request state - can be "open", "closed" or "merged".
        :param pulumi.Input[str] title: The title of the Pull Request.
        :param pulumi.Input[int] updated_at: The timestamp of the last Pull Request update.
        """
        if base_ref is not None:
            pulumi.set(__self__, "base_ref", base_ref)
        if base_repository is not None:
            pulumi.set(__self__, "base_repository", base_repository)
        if base_sha is not None:
            pulumi.set(__self__, "base_sha", base_sha)
        if body is not None:
            pulumi.set(__self__, "body", body)
        if draft is not None:
            pulumi.set(__self__, "draft", draft)
        if head_ref is not None:
            pulumi.set(__self__, "head_ref", head_ref)
        if head_sha is not None:
            pulumi.set(__self__, "head_sha", head_sha)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if maintainer_can_modify is not None:
            pulumi.set(__self__, "maintainer_can_modify", maintainer_can_modify)
        if number is not None:
            pulumi.set(__self__, "number", number)
        if opened_at is not None:
            pulumi.set(__self__, "opened_at", opened_at)
        if opened_by is not None:
            pulumi.set(__self__, "opened_by", opened_by)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="baseRef")
    def base_ref(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the branch serving as the base of the Pull Request.
        """
        return pulumi.get(self, "base_ref")

    @base_ref.setter
    def base_ref(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_ref", value)

    @property
    @pulumi.getter(name="baseRepository")
    def base_repository(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the base repository to retrieve the Pull Requests from.
        """
        return pulumi.get(self, "base_repository")

    @base_repository.setter
    def base_repository(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_repository", value)

    @property
    @pulumi.getter(name="baseSha")
    def base_sha(self) -> Optional[pulumi.Input[str]]:
        """
        Head commit SHA of the Pull Request base.
        """
        return pulumi.get(self, "base_sha")

    @base_sha.setter
    def base_sha(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_sha", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        Body of the Pull Request.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter
    def draft(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates Whether this Pull Request is a draft.
        """
        return pulumi.get(self, "draft")

    @draft.setter
    def draft(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "draft", value)

    @property
    @pulumi.getter(name="headRef")
    def head_ref(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the branch serving as the head of the Pull Request.
        """
        return pulumi.get(self, "head_ref")

    @head_ref.setter
    def head_ref(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "head_ref", value)

    @property
    @pulumi.getter(name="headSha")
    def head_sha(self) -> Optional[pulumi.Input[str]]:
        """
        Head commit SHA of the Pull Request head.
        """
        return pulumi.get(self, "head_sha")

    @head_sha.setter
    def head_sha(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "head_sha", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of label names set on the Pull Request.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="maintainerCanModify")
    def maintainer_can_modify(self) -> Optional[pulumi.Input[bool]]:
        """
        Controls whether the base repository maintainers can modify the Pull Request. Default: false.
        """
        return pulumi.get(self, "maintainer_can_modify")

    @maintainer_can_modify.setter
    def maintainer_can_modify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "maintainer_can_modify", value)

    @property
    @pulumi.getter
    def number(self) -> Optional[pulumi.Input[int]]:
        """
        The number of the Pull Request within the repository.
        """
        return pulumi.get(self, "number")

    @number.setter
    def number(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "number", value)

    @property
    @pulumi.getter(name="openedAt")
    def opened_at(self) -> Optional[pulumi.Input[int]]:
        """
        Unix timestamp indicating the Pull Request creation time.
        """
        return pulumi.get(self, "opened_at")

    @opened_at.setter
    def opened_at(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "opened_at", value)

    @property
    @pulumi.getter(name="openedBy")
    def opened_by(self) -> Optional[pulumi.Input[str]]:
        """
        GitHub login of the user who opened the Pull Request.
        """
        return pulumi.get(self, "opened_by")

    @opened_by.setter
    def opened_by(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "opened_by", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        Owner of the repository. If not provided, the provider's default owner is used.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        the current Pull Request state - can be "open", "closed" or "merged".
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the Pull Request.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[int]]:
        """
        The timestamp of the last Pull Request update.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "updated_at", value)


class RepositoryPullRequest(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_ref: Optional[pulumi.Input[str]] = None,
                 base_repository: Optional[pulumi.Input[str]] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 head_ref: Optional[pulumi.Input[str]] = None,
                 maintainer_can_modify: Optional[pulumi.Input[bool]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resource allows you to create and manage PullRequests for repositories within your GitHub organization or personal account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example = github.RepositoryPullRequest("example",
            base_ref="main",
            base_repository="example-repository",
            body="This will change everything",
            head_ref="feature-branch",
            title="My newest feature")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_ref: Name of the branch serving as the base of the Pull Request.
        :param pulumi.Input[str] base_repository: Name of the base repository to retrieve the Pull Requests from.
        :param pulumi.Input[str] body: Body of the Pull Request.
        :param pulumi.Input[str] head_ref: Name of the branch serving as the head of the Pull Request.
        :param pulumi.Input[bool] maintainer_can_modify: Controls whether the base repository maintainers can modify the Pull Request. Default: false.
        :param pulumi.Input[str] owner: Owner of the repository. If not provided, the provider's default owner is used.
        :param pulumi.Input[str] title: The title of the Pull Request.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepositoryPullRequestArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to create and manage PullRequests for repositories within your GitHub organization or personal account.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_github as github

        example = github.RepositoryPullRequest("example",
            base_ref="main",
            base_repository="example-repository",
            body="This will change everything",
            head_ref="feature-branch",
            title="My newest feature")
        ```

        :param str resource_name: The name of the resource.
        :param RepositoryPullRequestArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryPullRequestArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 base_ref: Optional[pulumi.Input[str]] = None,
                 base_repository: Optional[pulumi.Input[str]] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 head_ref: Optional[pulumi.Input[str]] = None,
                 maintainer_can_modify: Optional[pulumi.Input[bool]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
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
            __props__ = RepositoryPullRequestArgs.__new__(RepositoryPullRequestArgs)

            if base_ref is None and not opts.urn:
                raise TypeError("Missing required property 'base_ref'")
            __props__.__dict__["base_ref"] = base_ref
            if base_repository is None and not opts.urn:
                raise TypeError("Missing required property 'base_repository'")
            __props__.__dict__["base_repository"] = base_repository
            __props__.__dict__["body"] = body
            if head_ref is None and not opts.urn:
                raise TypeError("Missing required property 'head_ref'")
            __props__.__dict__["head_ref"] = head_ref
            __props__.__dict__["maintainer_can_modify"] = maintainer_can_modify
            __props__.__dict__["owner"] = owner
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            __props__.__dict__["base_sha"] = None
            __props__.__dict__["draft"] = None
            __props__.__dict__["head_sha"] = None
            __props__.__dict__["labels"] = None
            __props__.__dict__["number"] = None
            __props__.__dict__["opened_at"] = None
            __props__.__dict__["opened_by"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["updated_at"] = None
        super(RepositoryPullRequest, __self__).__init__(
            'github:index/repositoryPullRequest:RepositoryPullRequest',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            base_ref: Optional[pulumi.Input[str]] = None,
            base_repository: Optional[pulumi.Input[str]] = None,
            base_sha: Optional[pulumi.Input[str]] = None,
            body: Optional[pulumi.Input[str]] = None,
            draft: Optional[pulumi.Input[bool]] = None,
            head_ref: Optional[pulumi.Input[str]] = None,
            head_sha: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            maintainer_can_modify: Optional[pulumi.Input[bool]] = None,
            number: Optional[pulumi.Input[int]] = None,
            opened_at: Optional[pulumi.Input[int]] = None,
            opened_by: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            title: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[int]] = None) -> 'RepositoryPullRequest':
        """
        Get an existing RepositoryPullRequest resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] base_ref: Name of the branch serving as the base of the Pull Request.
        :param pulumi.Input[str] base_repository: Name of the base repository to retrieve the Pull Requests from.
        :param pulumi.Input[str] base_sha: Head commit SHA of the Pull Request base.
        :param pulumi.Input[str] body: Body of the Pull Request.
        :param pulumi.Input[bool] draft: Indicates Whether this Pull Request is a draft.
        :param pulumi.Input[str] head_ref: Name of the branch serving as the head of the Pull Request.
        :param pulumi.Input[str] head_sha: Head commit SHA of the Pull Request head.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of label names set on the Pull Request.
        :param pulumi.Input[bool] maintainer_can_modify: Controls whether the base repository maintainers can modify the Pull Request. Default: false.
        :param pulumi.Input[int] number: The number of the Pull Request within the repository.
        :param pulumi.Input[int] opened_at: Unix timestamp indicating the Pull Request creation time.
        :param pulumi.Input[str] opened_by: GitHub login of the user who opened the Pull Request.
        :param pulumi.Input[str] owner: Owner of the repository. If not provided, the provider's default owner is used.
        :param pulumi.Input[str] state: the current Pull Request state - can be "open", "closed" or "merged".
        :param pulumi.Input[str] title: The title of the Pull Request.
        :param pulumi.Input[int] updated_at: The timestamp of the last Pull Request update.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RepositoryPullRequestState.__new__(_RepositoryPullRequestState)

        __props__.__dict__["base_ref"] = base_ref
        __props__.__dict__["base_repository"] = base_repository
        __props__.__dict__["base_sha"] = base_sha
        __props__.__dict__["body"] = body
        __props__.__dict__["draft"] = draft
        __props__.__dict__["head_ref"] = head_ref
        __props__.__dict__["head_sha"] = head_sha
        __props__.__dict__["labels"] = labels
        __props__.__dict__["maintainer_can_modify"] = maintainer_can_modify
        __props__.__dict__["number"] = number
        __props__.__dict__["opened_at"] = opened_at
        __props__.__dict__["opened_by"] = opened_by
        __props__.__dict__["owner"] = owner
        __props__.__dict__["state"] = state
        __props__.__dict__["title"] = title
        __props__.__dict__["updated_at"] = updated_at
        return RepositoryPullRequest(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="baseRef")
    def base_ref(self) -> pulumi.Output[str]:
        """
        Name of the branch serving as the base of the Pull Request.
        """
        return pulumi.get(self, "base_ref")

    @property
    @pulumi.getter(name="baseRepository")
    def base_repository(self) -> pulumi.Output[str]:
        """
        Name of the base repository to retrieve the Pull Requests from.
        """
        return pulumi.get(self, "base_repository")

    @property
    @pulumi.getter(name="baseSha")
    def base_sha(self) -> pulumi.Output[str]:
        """
        Head commit SHA of the Pull Request base.
        """
        return pulumi.get(self, "base_sha")

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[Optional[str]]:
        """
        Body of the Pull Request.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def draft(self) -> pulumi.Output[bool]:
        """
        Indicates Whether this Pull Request is a draft.
        """
        return pulumi.get(self, "draft")

    @property
    @pulumi.getter(name="headRef")
    def head_ref(self) -> pulumi.Output[str]:
        """
        Name of the branch serving as the head of the Pull Request.
        """
        return pulumi.get(self, "head_ref")

    @property
    @pulumi.getter(name="headSha")
    def head_sha(self) -> pulumi.Output[str]:
        """
        Head commit SHA of the Pull Request head.
        """
        return pulumi.get(self, "head_sha")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Sequence[str]]:
        """
        List of label names set on the Pull Request.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="maintainerCanModify")
    def maintainer_can_modify(self) -> pulumi.Output[Optional[bool]]:
        """
        Controls whether the base repository maintainers can modify the Pull Request. Default: false.
        """
        return pulumi.get(self, "maintainer_can_modify")

    @property
    @pulumi.getter
    def number(self) -> pulumi.Output[int]:
        """
        The number of the Pull Request within the repository.
        """
        return pulumi.get(self, "number")

    @property
    @pulumi.getter(name="openedAt")
    def opened_at(self) -> pulumi.Output[int]:
        """
        Unix timestamp indicating the Pull Request creation time.
        """
        return pulumi.get(self, "opened_at")

    @property
    @pulumi.getter(name="openedBy")
    def opened_by(self) -> pulumi.Output[str]:
        """
        GitHub login of the user who opened the Pull Request.
        """
        return pulumi.get(self, "opened_by")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[Optional[str]]:
        """
        Owner of the repository. If not provided, the provider's default owner is used.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        the current Pull Request state - can be "open", "closed" or "merged".
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The title of the Pull Request.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[int]:
        """
        The timestamp of the last Pull Request update.
        """
        return pulumi.get(self, "updated_at")

