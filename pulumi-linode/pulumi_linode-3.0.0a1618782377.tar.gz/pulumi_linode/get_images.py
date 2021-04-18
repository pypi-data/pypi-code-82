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

__all__ = [
    'GetImagesResult',
    'AwaitableGetImagesResult',
    'get_images',
]

@pulumi.output_type
class GetImagesResult:
    """
    A collection of values returned by getImages.
    """
    def __init__(__self__, filters=None, id=None, images=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if images and not isinstance(images, list):
            raise TypeError("Expected argument 'images' to be a list")
        pulumi.set(__self__, "images", images)

    @property
    @pulumi.getter
    def filters(self) -> Optional[Sequence['outputs.GetImagesFilterResult']]:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def images(self) -> Sequence['outputs.GetImagesImageResult']:
        return pulumi.get(self, "images")


class AwaitableGetImagesResult(GetImagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImagesResult(
            filters=self.filters,
            id=self.id,
            images=self.images)


def get_images(filters: Optional[Sequence[pulumi.InputType['GetImagesFilterArgs']]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImagesResult:
    """
    Provides information about Linode images that match a set of filters.

    ## Attributes

    Each Linode image will be stored in the `images` attribute and will export the following attributes:

    * `id` - The unique ID of this Image.  The ID of private images begin with `private/` followed by the numeric identifier of the private image, for example `private/12345`.

    * `label` - A short description of the Image.

    * `created` - When this Image was created.

    * `created_by` - The name of the User who created this Image, or "linode" for official Images.

    * `deprecated` - Whether or not this Image is deprecated. Will only be true for deprecated public Images.

    * `description` - A detailed description of this Image.

    * `is_public` - True if the Image is public.

    * `size` - The minimum size this Image needs to deploy. Size is in MB. example: 2500

    * `type` - How the Image was created. Manual Images can be created at any time. "Automatic" Images are created automatically from a deleted Linode.

    * `vendor` - The upstream distribution vendor. `None` for private Images.

    ## Filterable Fields

    * `deprecated`

    * `is_public`

    * `label`

    * `size`

    * `vendor`
    """
    __args__ = dict()
    __args__['filters'] = filters
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('linode:index/getImages:getImages', __args__, opts=opts, typ=GetImagesResult).value

    return AwaitableGetImagesResult(
        filters=__ret__.filters,
        id=__ret__.id,
        images=__ret__.images)
