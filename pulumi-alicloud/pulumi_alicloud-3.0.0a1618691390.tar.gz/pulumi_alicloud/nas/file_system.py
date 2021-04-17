# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['FileSystemArgs', 'FileSystem']

@pulumi.input_type
class FileSystemArgs:
    def __init__(__self__, *,
                 protocol_type: pulumi.Input[str],
                 storage_type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a FileSystem resource.
        :param pulumi.Input[str] protocol_type: The Protocol Type of a File System. Valid values: `NFS` and `SMB`.
        :param pulumi.Input[str] storage_type: The Storage Type of a File System. Valid values: `Capacity` and `Performance`.
        :param pulumi.Input[str] description: The File System description.
        """
        pulumi.set(__self__, "protocol_type", protocol_type)
        pulumi.set(__self__, "storage_type", storage_type)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> pulumi.Input[str]:
        """
        The Protocol Type of a File System. Valid values: `NFS` and `SMB`.
        """
        return pulumi.get(self, "protocol_type")

    @protocol_type.setter
    def protocol_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol_type", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Input[str]:
        """
        The Storage Type of a File System. Valid values: `Capacity` and `Performance`.
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The File System description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class _FileSystemState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 protocol_type: Optional[pulumi.Input[str]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FileSystem resources.
        :param pulumi.Input[str] description: The File System description.
        :param pulumi.Input[str] protocol_type: The Protocol Type of a File System. Valid values: `NFS` and `SMB`.
        :param pulumi.Input[str] storage_type: The Storage Type of a File System. Valid values: `Capacity` and `Performance`.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if protocol_type is not None:
            pulumi.set(__self__, "protocol_type", protocol_type)
        if storage_type is not None:
            pulumi.set(__self__, "storage_type", storage_type)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The File System description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> Optional[pulumi.Input[str]]:
        """
        The Protocol Type of a File System. Valid values: `NFS` and `SMB`.
        """
        return pulumi.get(self, "protocol_type")

    @protocol_type.setter
    def protocol_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol_type", value)

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[pulumi.Input[str]]:
        """
        The Storage Type of a File System. Valid values: `Capacity` and `Performance`.
        """
        return pulumi.get(self, "storage_type")

    @storage_type.setter
    def storage_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_type", value)


class FileSystem(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 protocol_type: Optional[pulumi.Input[str]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Nas File System resource.

        After activating NAS, you can create a file system and purchase a storage package for it in the NAS console. The NAS console also enables you to view the file system details and remove unnecessary file systems.

        For information about NAS file system and how to use it, see [Manage file systems](https://www.alibabacloud.com/help/doc-detail/27530.htm)

        > **NOTE:** Available in v1.33.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        foo = alicloud.nas.FileSystem("foo",
            description="tf-testAccNasConfig",
            protocol_type="NFS",
            storage_type="Performance")
        ```

        ## Import

        Nas File System can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:nas/fileSystem:FileSystem foo 1337849c59
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The File System description.
        :param pulumi.Input[str] protocol_type: The Protocol Type of a File System. Valid values: `NFS` and `SMB`.
        :param pulumi.Input[str] storage_type: The Storage Type of a File System. Valid values: `Capacity` and `Performance`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FileSystemArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Nas File System resource.

        After activating NAS, you can create a file system and purchase a storage package for it in the NAS console. The NAS console also enables you to view the file system details and remove unnecessary file systems.

        For information about NAS file system and how to use it, see [Manage file systems](https://www.alibabacloud.com/help/doc-detail/27530.htm)

        > **NOTE:** Available in v1.33.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        foo = alicloud.nas.FileSystem("foo",
            description="tf-testAccNasConfig",
            protocol_type="NFS",
            storage_type="Performance")
        ```

        ## Import

        Nas File System can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:nas/fileSystem:FileSystem foo 1337849c59
        ```

        :param str resource_name: The name of the resource.
        :param FileSystemArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FileSystemArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 protocol_type: Optional[pulumi.Input[str]] = None,
                 storage_type: Optional[pulumi.Input[str]] = None,
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
            __props__ = FileSystemArgs.__new__(FileSystemArgs)

            __props__.__dict__["description"] = description
            if protocol_type is None and not opts.urn:
                raise TypeError("Missing required property 'protocol_type'")
            __props__.__dict__["protocol_type"] = protocol_type
            if storage_type is None and not opts.urn:
                raise TypeError("Missing required property 'storage_type'")
            __props__.__dict__["storage_type"] = storage_type
        super(FileSystem, __self__).__init__(
            'alicloud:nas/fileSystem:FileSystem',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            protocol_type: Optional[pulumi.Input[str]] = None,
            storage_type: Optional[pulumi.Input[str]] = None) -> 'FileSystem':
        """
        Get an existing FileSystem resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The File System description.
        :param pulumi.Input[str] protocol_type: The Protocol Type of a File System. Valid values: `NFS` and `SMB`.
        :param pulumi.Input[str] storage_type: The Storage Type of a File System. Valid values: `Capacity` and `Performance`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FileSystemState.__new__(_FileSystemState)

        __props__.__dict__["description"] = description
        __props__.__dict__["protocol_type"] = protocol_type
        __props__.__dict__["storage_type"] = storage_type
        return FileSystem(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The File System description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="protocolType")
    def protocol_type(self) -> pulumi.Output[str]:
        """
        The Protocol Type of a File System. Valid values: `NFS` and `SMB`.
        """
        return pulumi.get(self, "protocol_type")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> pulumi.Output[str]:
        """
        The Storage Type of a File System. Valid values: `Capacity` and `Performance`.
        """
        return pulumi.get(self, "storage_type")

