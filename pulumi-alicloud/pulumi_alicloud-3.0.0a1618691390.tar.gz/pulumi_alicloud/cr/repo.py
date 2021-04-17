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

__all__ = ['RepoArgs', 'Repo']

@pulumi.input_type
class RepoArgs:
    def __init__(__self__, *,
                 namespace: pulumi.Input[str],
                 repo_type: pulumi.Input[str],
                 summary: pulumi.Input[str],
                 detail: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Repo resource.
        :param pulumi.Input[str] namespace: Name of container registry namespace where repository is located.
        :param pulumi.Input[str] repo_type: `PUBLIC` or `PRIVATE`, repo's visibility.
        :param pulumi.Input[str] summary: The repository general information. It can contain 1 to 80 characters.
        :param pulumi.Input[str] detail: The repository specific information. MarkDown format is supported, and the length limit is 2000.
        :param pulumi.Input[str] name: Name of container registry repository.
        """
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "repo_type", repo_type)
        pulumi.set(__self__, "summary", summary)
        if detail is not None:
            pulumi.set(__self__, "detail", detail)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        Name of container registry namespace where repository is located.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> pulumi.Input[str]:
        """
        `PUBLIC` or `PRIVATE`, repo's visibility.
        """
        return pulumi.get(self, "repo_type")

    @repo_type.setter
    def repo_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "repo_type", value)

    @property
    @pulumi.getter
    def summary(self) -> pulumi.Input[str]:
        """
        The repository general information. It can contain 1 to 80 characters.
        """
        return pulumi.get(self, "summary")

    @summary.setter
    def summary(self, value: pulumi.Input[str]):
        pulumi.set(self, "summary", value)

    @property
    @pulumi.getter
    def detail(self) -> Optional[pulumi.Input[str]]:
        """
        The repository specific information. MarkDown format is supported, and the length limit is 2000.
        """
        return pulumi.get(self, "detail")

    @detail.setter
    def detail(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "detail", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of container registry repository.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _RepoState:
    def __init__(__self__, *,
                 detail: Optional[pulumi.Input[str]] = None,
                 domain_list: Optional[pulumi.Input['RepoDomainListArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 repo_type: Optional[pulumi.Input[str]] = None,
                 summary: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Repo resources.
        :param pulumi.Input[str] detail: The repository specific information. MarkDown format is supported, and the length limit is 2000.
        :param pulumi.Input['RepoDomainListArgs'] domain_list: The repository domain list.
        :param pulumi.Input[str] name: Name of container registry repository.
        :param pulumi.Input[str] namespace: Name of container registry namespace where repository is located.
        :param pulumi.Input[str] repo_type: `PUBLIC` or `PRIVATE`, repo's visibility.
        :param pulumi.Input[str] summary: The repository general information. It can contain 1 to 80 characters.
        """
        if detail is not None:
            pulumi.set(__self__, "detail", detail)
        if domain_list is not None:
            pulumi.set(__self__, "domain_list", domain_list)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if repo_type is not None:
            pulumi.set(__self__, "repo_type", repo_type)
        if summary is not None:
            pulumi.set(__self__, "summary", summary)

    @property
    @pulumi.getter
    def detail(self) -> Optional[pulumi.Input[str]]:
        """
        The repository specific information. MarkDown format is supported, and the length limit is 2000.
        """
        return pulumi.get(self, "detail")

    @detail.setter
    def detail(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "detail", value)

    @property
    @pulumi.getter(name="domainList")
    def domain_list(self) -> Optional[pulumi.Input['RepoDomainListArgs']]:
        """
        The repository domain list.
        """
        return pulumi.get(self, "domain_list")

    @domain_list.setter
    def domain_list(self, value: Optional[pulumi.Input['RepoDomainListArgs']]):
        pulumi.set(self, "domain_list", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of container registry repository.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        Name of container registry namespace where repository is located.
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> Optional[pulumi.Input[str]]:
        """
        `PUBLIC` or `PRIVATE`, repo's visibility.
        """
        return pulumi.get(self, "repo_type")

    @repo_type.setter
    def repo_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_type", value)

    @property
    @pulumi.getter
    def summary(self) -> Optional[pulumi.Input[str]]:
        """
        The repository general information. It can contain 1 to 80 characters.
        """
        return pulumi.get(self, "summary")

    @summary.setter
    def summary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "summary", value)


class Repo(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detail: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 repo_type: Optional[pulumi.Input[str]] = None,
                 summary: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This resource will help you to manager Container Registry repositories.

        > **NOTE:** Available in v1.35.0+.

        > **NOTE:** You need to set your registry password in Container Registry console before use this resource.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        my_namespace = alicloud.cr.Namespace("my-namespace",
            auto_create=False,
            default_visibility="PUBLIC")
        my_repo = alicloud.cr.Repo("my-repo",
            namespace=my_namespace.name,
            summary="this is summary of my new repo",
            repo_type="PUBLIC",
            detail="this is a public repo")
        ```

        ## Import

        Container Registry repository can be imported using the `namespace/repository`, e.g.

        ```sh
         $ pulumi import alicloud:cr/repo:Repo default `my-namespace/my-repo`
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detail: The repository specific information. MarkDown format is supported, and the length limit is 2000.
        :param pulumi.Input[str] name: Name of container registry repository.
        :param pulumi.Input[str] namespace: Name of container registry namespace where repository is located.
        :param pulumi.Input[str] repo_type: `PUBLIC` or `PRIVATE`, repo's visibility.
        :param pulumi.Input[str] summary: The repository general information. It can contain 1 to 80 characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepoArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource will help you to manager Container Registry repositories.

        > **NOTE:** Available in v1.35.0+.

        > **NOTE:** You need to set your registry password in Container Registry console before use this resource.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        my_namespace = alicloud.cr.Namespace("my-namespace",
            auto_create=False,
            default_visibility="PUBLIC")
        my_repo = alicloud.cr.Repo("my-repo",
            namespace=my_namespace.name,
            summary="this is summary of my new repo",
            repo_type="PUBLIC",
            detail="this is a public repo")
        ```

        ## Import

        Container Registry repository can be imported using the `namespace/repository`, e.g.

        ```sh
         $ pulumi import alicloud:cr/repo:Repo default `my-namespace/my-repo`
        ```

        :param str resource_name: The name of the resource.
        :param RepoArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepoArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detail: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 repo_type: Optional[pulumi.Input[str]] = None,
                 summary: Optional[pulumi.Input[str]] = None,
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
            __props__ = RepoArgs.__new__(RepoArgs)

            __props__.__dict__["detail"] = detail
            __props__.__dict__["name"] = name
            if namespace is None and not opts.urn:
                raise TypeError("Missing required property 'namespace'")
            __props__.__dict__["namespace"] = namespace
            if repo_type is None and not opts.urn:
                raise TypeError("Missing required property 'repo_type'")
            __props__.__dict__["repo_type"] = repo_type
            if summary is None and not opts.urn:
                raise TypeError("Missing required property 'summary'")
            __props__.__dict__["summary"] = summary
            __props__.__dict__["domain_list"] = None
        super(Repo, __self__).__init__(
            'alicloud:cr/repo:Repo',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            detail: Optional[pulumi.Input[str]] = None,
            domain_list: Optional[pulumi.Input[pulumi.InputType['RepoDomainListArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            repo_type: Optional[pulumi.Input[str]] = None,
            summary: Optional[pulumi.Input[str]] = None) -> 'Repo':
        """
        Get an existing Repo resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detail: The repository specific information. MarkDown format is supported, and the length limit is 2000.
        :param pulumi.Input[pulumi.InputType['RepoDomainListArgs']] domain_list: The repository domain list.
        :param pulumi.Input[str] name: Name of container registry repository.
        :param pulumi.Input[str] namespace: Name of container registry namespace where repository is located.
        :param pulumi.Input[str] repo_type: `PUBLIC` or `PRIVATE`, repo's visibility.
        :param pulumi.Input[str] summary: The repository general information. It can contain 1 to 80 characters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RepoState.__new__(_RepoState)

        __props__.__dict__["detail"] = detail
        __props__.__dict__["domain_list"] = domain_list
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["repo_type"] = repo_type
        __props__.__dict__["summary"] = summary
        return Repo(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def detail(self) -> pulumi.Output[Optional[str]]:
        """
        The repository specific information. MarkDown format is supported, and the length limit is 2000.
        """
        return pulumi.get(self, "detail")

    @property
    @pulumi.getter(name="domainList")
    def domain_list(self) -> pulumi.Output['outputs.RepoDomainList']:
        """
        The repository domain list.
        """
        return pulumi.get(self, "domain_list")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of container registry repository.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[str]:
        """
        Name of container registry namespace where repository is located.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="repoType")
    def repo_type(self) -> pulumi.Output[str]:
        """
        `PUBLIC` or `PRIVATE`, repo's visibility.
        """
        return pulumi.get(self, "repo_type")

    @property
    @pulumi.getter
    def summary(self) -> pulumi.Output[str]:
        """
        The repository general information. It can contain 1 to 80 characters.
        """
        return pulumi.get(self, "summary")

