# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetRepositoriesResult',
    'AwaitableGetRepositoriesResult',
    'get_repositories',
]

@pulumi.output_type
class GetRepositoriesResult:
    """
    A collection of values returned by getRepositories.
    """
    def __init__(__self__, full_names=None, id=None, names=None, query=None, sort=None):
        if full_names and not isinstance(full_names, list):
            raise TypeError("Expected argument 'full_names' to be a list")
        pulumi.set(__self__, "full_names", full_names)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if query and not isinstance(query, str):
            raise TypeError("Expected argument 'query' to be a str")
        pulumi.set(__self__, "query", query)
        if sort and not isinstance(sort, str):
            raise TypeError("Expected argument 'sort' to be a str")
        pulumi.set(__self__, "sort", sort)

    @property
    @pulumi.getter(name="fullNames")
    def full_names(self) -> Sequence[str]:
        return pulumi.get(self, "full_names")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        return pulumi.get(self, "names")

    @property
    @pulumi.getter
    def query(self) -> str:
        return pulumi.get(self, "query")

    @property
    @pulumi.getter
    def sort(self) -> Optional[str]:
        return pulumi.get(self, "sort")


class AwaitableGetRepositoriesResult(GetRepositoriesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRepositoriesResult(
            full_names=self.full_names,
            id=self.id,
            names=self.names,
            query=self.query,
            sort=self.sort)


def get_repositories(query: Optional[str] = None,
                     sort: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRepositoriesResult:
    """
    > **Note:** The data source will return a maximum of `1000` repositories
    	[as documented in official API docs](https://developer.github.com/v3/search/#about-the-search-api).

    Use this data source to retrieve a list of GitHub repositories using a search query.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_github as github

    example = github.get_repositories(query="org:hashicorp language:Go")
    ```


    :param str query: Search query. See [documentation for the search syntax](https://help.github.com/articles/understanding-the-search-syntax/).
    :param str sort: Sorts the repositories returned by the specified attribute. Valid values include `stars`, `fork`, and `updated`. Defaults to `updated`.
    """
    __args__ = dict()
    __args__['query'] = query
    __args__['sort'] = sort
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('github:index/getRepositories:getRepositories', __args__, opts=opts, typ=GetRepositoriesResult).value

    return AwaitableGetRepositoriesResult(
        full_names=__ret__.full_names,
        id=__ret__.id,
        names=__ret__.names,
        query=__ret__.query,
        sort=__ret__.sort)
