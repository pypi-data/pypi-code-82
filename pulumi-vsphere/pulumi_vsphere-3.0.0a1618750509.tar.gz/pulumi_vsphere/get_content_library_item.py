# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetContentLibraryItemResult',
    'AwaitableGetContentLibraryItemResult',
    'get_content_library_item',
]

@pulumi.output_type
class GetContentLibraryItemResult:
    """
    A collection of values returned by getContentLibraryItem.
    """
    def __init__(__self__, id=None, library_id=None, name=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if library_id and not isinstance(library_id, str):
            raise TypeError("Expected argument 'library_id' to be a str")
        pulumi.set(__self__, "library_id", library_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="libraryId")
    def library_id(self) -> str:
        return pulumi.get(self, "library_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The Content Library type. Can be ovf, iso, or vm-template.
        """
        return pulumi.get(self, "type")


class AwaitableGetContentLibraryItemResult(GetContentLibraryItemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContentLibraryItemResult(
            id=self.id,
            library_id=self.library_id,
            name=self.name,
            type=self.type)


def get_content_library_item(library_id: Optional[str] = None,
                             name: Optional[str] = None,
                             type: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContentLibraryItemResult:
    """
    The `ContentLibraryItem` data source can be used to discover the ID of a Content Library item.

    > **NOTE:** This resource requires vCenter and is not available on direct ESXi
    connections.


    :param str library_id: The ID of the Content Library the item exists in.
    :param str name: The name of the Content Library.
    :param str type: The Content Library type. Can be ovf, iso, or vm-template.
    """
    __args__ = dict()
    __args__['libraryId'] = library_id
    __args__['name'] = name
    __args__['type'] = type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('vsphere:index/getContentLibraryItem:getContentLibraryItem', __args__, opts=opts, typ=GetContentLibraryItemResult).value

    return AwaitableGetContentLibraryItemResult(
        id=__ret__.id,
        library_id=__ret__.library_id,
        name=__ret__.name,
        type=__ret__.type)
