# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ImageCopyArgs', 'ImageCopy']

@pulumi.input_type
class ImageCopyArgs:
    def __init__(__self__, *,
                 source_image_id: pulumi.Input[str],
                 source_region_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        The set of arguments for constructing a ImageCopy resource.
        :param pulumi.Input[str] source_image_id: The source image ID.
        :param pulumi.Input[str] source_region_id: The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        :param pulumi.Input[str] description: The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        :param pulumi.Input[bool] encrypted: Indicates whether to encrypt the image.
        :param pulumi.Input[bool] force: Indicates whether to force delete the custom image, Default is `false`. 
               - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
               - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        :param pulumi.Input[str] image_name: The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        :param pulumi.Input[str] kms_key_id: Key ID used to encrypt the image.
        :param pulumi.Input[Mapping[str, Any]] tags: The tag value of an image. The value of N ranges from 1 to 20.
        """
        pulumi.set(__self__, "source_image_id", source_image_id)
        pulumi.set(__self__, "source_region_id", source_region_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if encrypted is not None:
            pulumi.set(__self__, "encrypted", encrypted)
        if force is not None:
            pulumi.set(__self__, "force", force)
        if image_name is not None:
            pulumi.set(__self__, "image_name", image_name)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name is not None:
            warnings.warn("""Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""", DeprecationWarning)
            pulumi.log.warn("""name is deprecated: Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""")
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> pulumi.Input[str]:
        """
        The source image ID.
        """
        return pulumi.get(self, "source_image_id")

    @source_image_id.setter
    def source_image_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_image_id", value)

    @property
    @pulumi.getter(name="sourceRegionId")
    def source_region_id(self) -> pulumi.Input[str]:
        """
        The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        """
        return pulumi.get(self, "source_region_id")

    @source_region_id.setter
    def source_region_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_region_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to encrypt the image.
        """
        return pulumi.get(self, "encrypted")

    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypted", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to force delete the custom image, Default is `false`. 
        - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
        - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[str]]:
        """
        The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        """
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_name", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        Key ID used to encrypt the image.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The tag value of an image. The value of N ranges from 1 to 20.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ImageCopyState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None,
                 source_region_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        """
        Input properties used for looking up and filtering ImageCopy resources.
        :param pulumi.Input[str] description: The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        :param pulumi.Input[bool] encrypted: Indicates whether to encrypt the image.
        :param pulumi.Input[bool] force: Indicates whether to force delete the custom image, Default is `false`. 
               - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
               - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        :param pulumi.Input[str] image_name: The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        :param pulumi.Input[str] kms_key_id: Key ID used to encrypt the image.
        :param pulumi.Input[str] source_image_id: The source image ID.
        :param pulumi.Input[str] source_region_id: The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        :param pulumi.Input[Mapping[str, Any]] tags: The tag value of an image. The value of N ranges from 1 to 20.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if encrypted is not None:
            pulumi.set(__self__, "encrypted", encrypted)
        if force is not None:
            pulumi.set(__self__, "force", force)
        if image_name is not None:
            pulumi.set(__self__, "image_name", image_name)
        if kms_key_id is not None:
            pulumi.set(__self__, "kms_key_id", kms_key_id)
        if name is not None:
            warnings.warn("""Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""", DeprecationWarning)
            pulumi.log.warn("""name is deprecated: Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""")
        if name is not None:
            pulumi.set(__self__, "name", name)
        if source_image_id is not None:
            pulumi.set(__self__, "source_image_id", source_image_id)
        if source_region_id is not None:
            pulumi.set(__self__, "source_region_id", source_region_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encrypted(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to encrypt the image.
        """
        return pulumi.get(self, "encrypted")

    @encrypted.setter
    def encrypted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "encrypted", value)

    @property
    @pulumi.getter
    def force(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether to force delete the custom image, Default is `false`. 
        - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
        - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        """
        return pulumi.get(self, "force")

    @force.setter
    def force(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force", value)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> Optional[pulumi.Input[str]]:
        """
        The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        """
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_name", value)

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[pulumi.Input[str]]:
        """
        Key ID used to encrypt the image.
        """
        return pulumi.get(self, "kms_key_id")

    @kms_key_id.setter
    def kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> Optional[pulumi.Input[str]]:
        """
        The source image ID.
        """
        return pulumi.get(self, "source_image_id")

    @source_image_id.setter
    def source_image_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_image_id", value)

    @property
    @pulumi.getter(name="sourceRegionId")
    def source_region_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        """
        return pulumi.get(self, "source_region_id")

    @source_region_id.setter
    def source_region_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_region_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The tag value of an image. The value of N ranges from 1 to 20.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)


class ImageCopy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None,
                 source_region_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Copies a custom image from one region to another. You can use copied images to perform operations in the target region, such as creating instances (RunInstances) and replacing system disks (ReplaceSystemDisk).

        > **NOTE:** You can only copy the custom image when it is in the Available state.

        > **NOTE:** You can only copy the image belonging to your Alibaba Cloud account. Images cannot be copied from one account to another.

        > **NOTE:** If the copying is not completed, you cannot call DeleteImage to delete the image but you can call CancelCopyImage to cancel the copying.

        > **NOTE:** Available in 1.66.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.ImageCopy("default",
            description="test-image",
            image_name="test-image",
            source_image_id="m-bp1gxyhdswlsn18tu***",
            source_region_id="cn-hangzhou",
            tags={
                "FinanceDept": "FinanceDeptJoshua",
            })
        ```
        ## Attributes Reference0

         The following attributes are exported:

        * `id` - ID of the image.

        ## Import

        image can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ecs/imageCopy:ImageCopy default m-uf66871ape***yg1q***
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        :param pulumi.Input[bool] encrypted: Indicates whether to encrypt the image.
        :param pulumi.Input[bool] force: Indicates whether to force delete the custom image, Default is `false`. 
               - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
               - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        :param pulumi.Input[str] image_name: The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        :param pulumi.Input[str] kms_key_id: Key ID used to encrypt the image.
        :param pulumi.Input[str] source_image_id: The source image ID.
        :param pulumi.Input[str] source_region_id: The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        :param pulumi.Input[Mapping[str, Any]] tags: The tag value of an image. The value of N ranges from 1 to 20.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImageCopyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Copies a custom image from one region to another. You can use copied images to perform operations in the target region, such as creating instances (RunInstances) and replacing system disks (ReplaceSystemDisk).

        > **NOTE:** You can only copy the custom image when it is in the Available state.

        > **NOTE:** You can only copy the image belonging to your Alibaba Cloud account. Images cannot be copied from one account to another.

        > **NOTE:** If the copying is not completed, you cannot call DeleteImage to delete the image but you can call CancelCopyImage to cancel the copying.

        > **NOTE:** Available in 1.66.0+.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.ecs.ImageCopy("default",
            description="test-image",
            image_name="test-image",
            source_image_id="m-bp1gxyhdswlsn18tu***",
            source_region_id="cn-hangzhou",
            tags={
                "FinanceDept": "FinanceDeptJoshua",
            })
        ```
        ## Attributes Reference0

         The following attributes are exported:

        * `id` - ID of the image.

        ## Import

        image can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:ecs/imageCopy:ImageCopy default m-uf66871ape***yg1q***
        ```

        :param str resource_name: The name of the resource.
        :param ImageCopyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImageCopyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encrypted: Optional[pulumi.Input[bool]] = None,
                 force: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 kms_key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source_image_id: Optional[pulumi.Input[str]] = None,
                 source_region_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
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
            __props__ = ImageCopyArgs.__new__(ImageCopyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["encrypted"] = encrypted
            __props__.__dict__["force"] = force
            __props__.__dict__["image_name"] = image_name
            __props__.__dict__["kms_key_id"] = kms_key_id
            if name is not None and not opts.urn:
                warnings.warn("""Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""", DeprecationWarning)
                pulumi.log.warn("""name is deprecated: Attribute 'name' has been deprecated from version 1.69.0. Use `image_name` instead.""")
            __props__.__dict__["name"] = name
            if source_image_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_image_id'")
            __props__.__dict__["source_image_id"] = source_image_id
            if source_region_id is None and not opts.urn:
                raise TypeError("Missing required property 'source_region_id'")
            __props__.__dict__["source_region_id"] = source_region_id
            __props__.__dict__["tags"] = tags
        super(ImageCopy, __self__).__init__(
            'alicloud:ecs/imageCopy:ImageCopy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            encrypted: Optional[pulumi.Input[bool]] = None,
            force: Optional[pulumi.Input[bool]] = None,
            image_name: Optional[pulumi.Input[str]] = None,
            kms_key_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            source_image_id: Optional[pulumi.Input[str]] = None,
            source_region_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'ImageCopy':
        """
        Get an existing ImageCopy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        :param pulumi.Input[bool] encrypted: Indicates whether to encrypt the image.
        :param pulumi.Input[bool] force: Indicates whether to force delete the custom image, Default is `false`. 
               - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
               - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        :param pulumi.Input[str] image_name: The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        :param pulumi.Input[str] kms_key_id: Key ID used to encrypt the image.
        :param pulumi.Input[str] source_image_id: The source image ID.
        :param pulumi.Input[str] source_region_id: The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        :param pulumi.Input[Mapping[str, Any]] tags: The tag value of an image. The value of N ranges from 1 to 20.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ImageCopyState.__new__(_ImageCopyState)

        __props__.__dict__["description"] = description
        __props__.__dict__["encrypted"] = encrypted
        __props__.__dict__["force"] = force
        __props__.__dict__["image_name"] = image_name
        __props__.__dict__["kms_key_id"] = kms_key_id
        __props__.__dict__["name"] = name
        __props__.__dict__["source_image_id"] = source_image_id
        __props__.__dict__["source_region_id"] = source_region_id
        __props__.__dict__["tags"] = tags
        return ImageCopy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the image. It must be 2 to 256 characters in length and must not start with http:// or https://. Default value: null.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encrypted(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether to encrypt the image.
        """
        return pulumi.get(self, "encrypted")

    @property
    @pulumi.getter
    def force(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicates whether to force delete the custom image, Default is `false`. 
        - true：Force deletes the custom image, regardless of whether the image is currently being used by other instances.
        - false：Verifies that the image is not currently in use by any other instances before deleting the image.
        """
        return pulumi.get(self, "force")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[str]:
        """
        The image name. It must be 2 to 128 characters in length, and must begin with a letter or Chinese character (beginning with http:// or https:// is not allowed). It can contain digits, colons (:), underscores (_), or hyphens (-). Default value: null.
        """
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> pulumi.Output[Optional[str]]:
        """
        Key ID used to encrypt the image.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sourceImageId")
    def source_image_id(self) -> pulumi.Output[str]:
        """
        The source image ID.
        """
        return pulumi.get(self, "source_image_id")

    @property
    @pulumi.getter(name="sourceRegionId")
    def source_region_id(self) -> pulumi.Output[str]:
        """
        The ID of the region to which the source custom image belongs. You can call [DescribeRegions](https://www.alibabacloud.com/help/doc-detail/25609.htm) to view the latest regions of Alibaba Cloud.
        """
        return pulumi.get(self, "source_region_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        The tag value of an image. The value of N ranges from 1 to 20.
        """
        return pulumi.get(self, "tags")

