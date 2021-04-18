# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['VirtualDiskArgs', 'VirtualDisk']

@pulumi.input_type
class VirtualDiskArgs:
    def __init__(__self__, *,
                 datastore: pulumi.Input[str],
                 size: pulumi.Input[int],
                 vmdk_path: pulumi.Input[str],
                 adapter_type: Optional[pulumi.Input[str]] = None,
                 create_directories: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a VirtualDisk resource.
        :param pulumi.Input[str] datastore: The name of the datastore in which to create the
               disk.
        :param pulumi.Input[int] size: Size of the disk (in GB).
        :param pulumi.Input[str] vmdk_path: The path, including filename, of the virtual disk to
               be created.  This needs to end in `.vmdk`.
        :param pulumi.Input[str] adapter_type: The adapter type for this virtual disk. Can be
               one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        :param pulumi.Input[bool] create_directories: Tells the resource to create any
               directories that are a part of the `vmdk_path` parameter if they are missing.
               Default: `false`.
        :param pulumi.Input[str] datacenter: The name of the datacenter in which to create the
               disk. Can be omitted when when ESXi or if there is only one datacenter in
               your infrastructure.
        :param pulumi.Input[str] type: The type of disk to create. Can be one of
               `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
               information on what each kind of disk provisioning policy means, click
               [here][docs-vmware-vm-disk-provisioning].
        """
        pulumi.set(__self__, "datastore", datastore)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "vmdk_path", vmdk_path)
        if adapter_type is not None:
            warnings.warn("""this attribute has no effect on controller types - please use scsi_type in vsphere_virtual_machine instead""", DeprecationWarning)
            pulumi.log.warn("""adapter_type is deprecated: this attribute has no effect on controller types - please use scsi_type in vsphere_virtual_machine instead""")
        if adapter_type is not None:
            pulumi.set(__self__, "adapter_type", adapter_type)
        if create_directories is not None:
            pulumi.set(__self__, "create_directories", create_directories)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def datastore(self) -> pulumi.Input[str]:
        """
        The name of the datastore in which to create the
        disk.
        """
        return pulumi.get(self, "datastore")

    @datastore.setter
    def datastore(self, value: pulumi.Input[str]):
        pulumi.set(self, "datastore", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        """
        Size of the disk (in GB).
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="vmdkPath")
    def vmdk_path(self) -> pulumi.Input[str]:
        """
        The path, including filename, of the virtual disk to
        be created.  This needs to end in `.vmdk`.
        """
        return pulumi.get(self, "vmdk_path")

    @vmdk_path.setter
    def vmdk_path(self, value: pulumi.Input[str]):
        pulumi.set(self, "vmdk_path", value)

    @property
    @pulumi.getter(name="adapterType")
    def adapter_type(self) -> Optional[pulumi.Input[str]]:
        """
        The adapter type for this virtual disk. Can be
        one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        """
        return pulumi.get(self, "adapter_type")

    @adapter_type.setter
    def adapter_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "adapter_type", value)

    @property
    @pulumi.getter(name="createDirectories")
    def create_directories(self) -> Optional[pulumi.Input[bool]]:
        """
        Tells the resource to create any
        directories that are a part of the `vmdk_path` parameter if they are missing.
        Default: `false`.
        """
        return pulumi.get(self, "create_directories")

    @create_directories.setter
    def create_directories(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "create_directories", value)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the datacenter in which to create the
        disk. Can be omitted when when ESXi or if there is only one datacenter in
        your infrastructure.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of disk to create. Can be one of
        `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
        information on what each kind of disk provisioning policy means, click
        [here][docs-vmware-vm-disk-provisioning].
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _VirtualDiskState:
    def __init__(__self__, *,
                 adapter_type: Optional[pulumi.Input[str]] = None,
                 create_directories: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 datastore: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vmdk_path: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering VirtualDisk resources.
        :param pulumi.Input[str] adapter_type: The adapter type for this virtual disk. Can be
               one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        :param pulumi.Input[bool] create_directories: Tells the resource to create any
               directories that are a part of the `vmdk_path` parameter if they are missing.
               Default: `false`.
        :param pulumi.Input[str] datacenter: The name of the datacenter in which to create the
               disk. Can be omitted when when ESXi or if there is only one datacenter in
               your infrastructure.
        :param pulumi.Input[str] datastore: The name of the datastore in which to create the
               disk.
        :param pulumi.Input[int] size: Size of the disk (in GB).
        :param pulumi.Input[str] type: The type of disk to create. Can be one of
               `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
               information on what each kind of disk provisioning policy means, click
               [here][docs-vmware-vm-disk-provisioning].
        :param pulumi.Input[str] vmdk_path: The path, including filename, of the virtual disk to
               be created.  This needs to end in `.vmdk`.
        """
        if adapter_type is not None:
            warnings.warn("""this attribute has no effect on controller types - please use scsi_type in vsphere_virtual_machine instead""", DeprecationWarning)
            pulumi.log.warn("""adapter_type is deprecated: this attribute has no effect on controller types - please use scsi_type in vsphere_virtual_machine instead""")
        if adapter_type is not None:
            pulumi.set(__self__, "adapter_type", adapter_type)
        if create_directories is not None:
            pulumi.set(__self__, "create_directories", create_directories)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if datastore is not None:
            pulumi.set(__self__, "datastore", datastore)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if vmdk_path is not None:
            pulumi.set(__self__, "vmdk_path", vmdk_path)

    @property
    @pulumi.getter(name="adapterType")
    def adapter_type(self) -> Optional[pulumi.Input[str]]:
        """
        The adapter type for this virtual disk. Can be
        one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        """
        return pulumi.get(self, "adapter_type")

    @adapter_type.setter
    def adapter_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "adapter_type", value)

    @property
    @pulumi.getter(name="createDirectories")
    def create_directories(self) -> Optional[pulumi.Input[bool]]:
        """
        Tells the resource to create any
        directories that are a part of the `vmdk_path` parameter if they are missing.
        Default: `false`.
        """
        return pulumi.get(self, "create_directories")

    @create_directories.setter
    def create_directories(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "create_directories", value)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the datacenter in which to create the
        disk. Can be omitted when when ESXi or if there is only one datacenter in
        your infrastructure.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter
    def datastore(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the datastore in which to create the
        disk.
        """
        return pulumi.get(self, "datastore")

    @datastore.setter
    def datastore(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datastore", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        Size of the disk (in GB).
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of disk to create. Can be one of
        `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
        information on what each kind of disk provisioning policy means, click
        [here][docs-vmware-vm-disk-provisioning].
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="vmdkPath")
    def vmdk_path(self) -> Optional[pulumi.Input[str]]:
        """
        The path, including filename, of the virtual disk to
        be created.  This needs to end in `.vmdk`.
        """
        return pulumi.get(self, "vmdk_path")

    @vmdk_path.setter
    def vmdk_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vmdk_path", value)


class VirtualDisk(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adapter_type: Optional[pulumi.Input[str]] = None,
                 create_directories: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 datastore: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vmdk_path: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The `VirtualDisk` resource can be used to create virtual disks outside
        of any given `VirtualMachine`
        resource. These disks can be attached to a virtual machine by creating a disk
        block with the `attach` parameter.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        my_disk = vsphere.VirtualDisk("myDisk",
            datacenter="Datacenter",
            datastore="local",
            size=2,
            type="thin",
            vmdk_path="myDisk.vmdk")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] adapter_type: The adapter type for this virtual disk. Can be
               one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        :param pulumi.Input[bool] create_directories: Tells the resource to create any
               directories that are a part of the `vmdk_path` parameter if they are missing.
               Default: `false`.
        :param pulumi.Input[str] datacenter: The name of the datacenter in which to create the
               disk. Can be omitted when when ESXi or if there is only one datacenter in
               your infrastructure.
        :param pulumi.Input[str] datastore: The name of the datastore in which to create the
               disk.
        :param pulumi.Input[int] size: Size of the disk (in GB).
        :param pulumi.Input[str] type: The type of disk to create. Can be one of
               `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
               information on what each kind of disk provisioning policy means, click
               [here][docs-vmware-vm-disk-provisioning].
        :param pulumi.Input[str] vmdk_path: The path, including filename, of the virtual disk to
               be created.  This needs to end in `.vmdk`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualDiskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `VirtualDisk` resource can be used to create virtual disks outside
        of any given `VirtualMachine`
        resource. These disks can be attached to a virtual machine by creating a disk
        block with the `attach` parameter.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vsphere as vsphere

        my_disk = vsphere.VirtualDisk("myDisk",
            datacenter="Datacenter",
            datastore="local",
            size=2,
            type="thin",
            vmdk_path="myDisk.vmdk")
        ```

        :param str resource_name: The name of the resource.
        :param VirtualDiskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualDiskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 adapter_type: Optional[pulumi.Input[str]] = None,
                 create_directories: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 datastore: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vmdk_path: Optional[pulumi.Input[str]] = None,
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
            __props__ = VirtualDiskArgs.__new__(VirtualDiskArgs)

            if adapter_type is not None and not opts.urn:
                warnings.warn("""this attribute has no effect on controller types - please use scsi_type in vsphere_virtual_machine instead""", DeprecationWarning)
                pulumi.log.warn("""adapter_type is deprecated: this attribute has no effect on controller types - please use scsi_type in vsphere_virtual_machine instead""")
            __props__.__dict__["adapter_type"] = adapter_type
            __props__.__dict__["create_directories"] = create_directories
            __props__.__dict__["datacenter"] = datacenter
            if datastore is None and not opts.urn:
                raise TypeError("Missing required property 'datastore'")
            __props__.__dict__["datastore"] = datastore
            if size is None and not opts.urn:
                raise TypeError("Missing required property 'size'")
            __props__.__dict__["size"] = size
            __props__.__dict__["type"] = type
            if vmdk_path is None and not opts.urn:
                raise TypeError("Missing required property 'vmdk_path'")
            __props__.__dict__["vmdk_path"] = vmdk_path
        super(VirtualDisk, __self__).__init__(
            'vsphere:index/virtualDisk:VirtualDisk',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            adapter_type: Optional[pulumi.Input[str]] = None,
            create_directories: Optional[pulumi.Input[bool]] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            datastore: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            vmdk_path: Optional[pulumi.Input[str]] = None) -> 'VirtualDisk':
        """
        Get an existing VirtualDisk resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] adapter_type: The adapter type for this virtual disk. Can be
               one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        :param pulumi.Input[bool] create_directories: Tells the resource to create any
               directories that are a part of the `vmdk_path` parameter if they are missing.
               Default: `false`.
        :param pulumi.Input[str] datacenter: The name of the datacenter in which to create the
               disk. Can be omitted when when ESXi or if there is only one datacenter in
               your infrastructure.
        :param pulumi.Input[str] datastore: The name of the datastore in which to create the
               disk.
        :param pulumi.Input[int] size: Size of the disk (in GB).
        :param pulumi.Input[str] type: The type of disk to create. Can be one of
               `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
               information on what each kind of disk provisioning policy means, click
               [here][docs-vmware-vm-disk-provisioning].
        :param pulumi.Input[str] vmdk_path: The path, including filename, of the virtual disk to
               be created.  This needs to end in `.vmdk`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _VirtualDiskState.__new__(_VirtualDiskState)

        __props__.__dict__["adapter_type"] = adapter_type
        __props__.__dict__["create_directories"] = create_directories
        __props__.__dict__["datacenter"] = datacenter
        __props__.__dict__["datastore"] = datastore
        __props__.__dict__["size"] = size
        __props__.__dict__["type"] = type
        __props__.__dict__["vmdk_path"] = vmdk_path
        return VirtualDisk(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adapterType")
    def adapter_type(self) -> pulumi.Output[Optional[str]]:
        """
        The adapter type for this virtual disk. Can be
        one of `ide`, `lsiLogic`, or `busLogic`.  Default: `lsiLogic`.
        """
        return pulumi.get(self, "adapter_type")

    @property
    @pulumi.getter(name="createDirectories")
    def create_directories(self) -> pulumi.Output[Optional[bool]]:
        """
        Tells the resource to create any
        directories that are a part of the `vmdk_path` parameter if they are missing.
        Default: `false`.
        """
        return pulumi.get(self, "create_directories")

    @property
    @pulumi.getter
    def datacenter(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the datacenter in which to create the
        disk. Can be omitted when when ESXi or if there is only one datacenter in
        your infrastructure.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter
    def datastore(self) -> pulumi.Output[str]:
        """
        The name of the datastore in which to create the
        disk.
        """
        return pulumi.get(self, "datastore")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        Size of the disk (in GB).
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of disk to create. Can be one of
        `eagerZeroedThick`, `lazy`, or `thin`. Default: `eagerZeroedThick`. For
        information on what each kind of disk provisioning policy means, click
        [here][docs-vmware-vm-disk-provisioning].
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmdkPath")
    def vmdk_path(self) -> pulumi.Output[str]:
        """
        The path, including filename, of the virtual disk to
        be created.  This needs to end in `.vmdk`.
        """
        return pulumi.get(self, "vmdk_path")

