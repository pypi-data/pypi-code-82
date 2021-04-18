# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetGroupResult',
    'AwaitableGetGroupResult',
    'get_group',
]

warnings.warn("""azuredevops.identities.getGroup has been deprecated in favor of azuredevops.getGroup""", DeprecationWarning)

@pulumi.output_type
class GetGroupResult:
    """
    A collection of values returned by getGroup.
    """
    def __init__(__self__, descriptor=None, id=None, name=None, origin=None, origin_id=None, project_id=None):
        if descriptor and not isinstance(descriptor, str):
            raise TypeError("Expected argument 'descriptor' to be a str")
        pulumi.set(__self__, "descriptor", descriptor)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if origin and not isinstance(origin, str):
            raise TypeError("Expected argument 'origin' to be a str")
        pulumi.set(__self__, "origin", origin)
        if origin_id and not isinstance(origin_id, str):
            raise TypeError("Expected argument 'origin_id' to be a str")
        pulumi.set(__self__, "origin_id", origin_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter
    def descriptor(self) -> str:
        """
        The Descriptor is the primary way to reference the graph subject. This field will uniquely identify the same graph subject across both Accounts and Organizations.
        """
        return pulumi.get(self, "descriptor")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def origin(self) -> str:
        """
        The type of source provider for the origin identifier (ex:AD, AAD, MSA)
        """
        return pulumi.get(self, "origin")

    @property
    @pulumi.getter(name="originId")
    def origin_id(self) -> str:
        """
        The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.
        """
        return pulumi.get(self, "origin_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[str]:
        return pulumi.get(self, "project_id")


class AwaitableGetGroupResult(GetGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupResult(
            descriptor=self.descriptor,
            id=self.id,
            name=self.name,
            origin=self.origin,
            origin_id=self.origin_id,
            project_id=self.project_id)


def get_group(name: Optional[str] = None,
              project_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupResult:
    """
    Use this data source to access information about an existing Group within Azure DevOps

    ## Example Usage

    ```python
    import pulumi
    import pulumi_azuredevops as azuredevops

    project = azuredevops.get_project(name="contoso-project")
    test = azuredevops.get_group(project_id=project.id,
        name="Test Group")
    pulumi.export("groupId", test.id)
    pulumi.export("groupDescriptor", test.descriptor)
    test_collection_group = azuredevops.get_group(name="Project Collection Administrators")
    pulumi.export("collectionGroupId", test_collection_group.id)
    pulumi.export("collectionGroupDescriptor", test_collection_group.descriptor)
    ```
    ## Relevant Links

    - [Azure DevOps Service REST API 5.1 - Groups - Get](https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/groups/get?view=azure-devops-rest-5.1)


    :param str name: The Group Name.
    :param str project_id: The Project ID. If no project ID is specified the project collection groups will be searched.
    """
    pulumi.log.warn("""get_group is deprecated: azuredevops.identities.getGroup has been deprecated in favor of azuredevops.getGroup""")
    __args__ = dict()
    __args__['name'] = name
    __args__['projectId'] = project_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('azuredevops:Identities/getGroup:getGroup', __args__, opts=opts, typ=GetGroupResult).value

    return AwaitableGetGroupResult(
        descriptor=__ret__.descriptor,
        id=__ret__.id,
        name=__ret__.name,
        origin=__ret__.origin,
        origin_id=__ret__.origin_id,
        project_id=__ret__.project_id)
