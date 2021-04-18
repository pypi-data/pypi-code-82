# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'InstanceBlockDeviceArgs',
    'InstanceNetworkArgs',
    'InstancePersonalityArgs',
    'InstanceSchedulerHintArgs',
    'InstanceVendorOptionsArgs',
    'SecGroupRuleArgs',
    'VolumeAttachVendorOptionsArgs',
    'GetInstanceV2NetworkArgs',
]

@pulumi.input_type
class InstanceBlockDeviceArgs:
    def __init__(__self__, *,
                 source_type: pulumi.Input[str],
                 boot_index: Optional[pulumi.Input[int]] = None,
                 delete_on_termination: Optional[pulumi.Input[bool]] = None,
                 destination_type: Optional[pulumi.Input[str]] = None,
                 device_type: Optional[pulumi.Input[str]] = None,
                 disk_bus: Optional[pulumi.Input[str]] = None,
                 guest_format: Optional[pulumi.Input[str]] = None,
                 uuid: Optional[pulumi.Input[str]] = None,
                 volume_size: Optional[pulumi.Input[int]] = None,
                 volume_type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] source_type: The source type of the device. Must be one of
               "blank", "image", "volume", or "snapshot". Changing this creates a new
               server.
        :param pulumi.Input[int] boot_index: The boot index of the volume. It defaults to 0.
               Changing this creates a new server.
        :param pulumi.Input[bool] delete_on_termination: Delete the volume / block device upon
               termination of the instance. Defaults to false. Changing this creates a
               new server.
        :param pulumi.Input[str] destination_type: The type that gets created. Possible values
               are "volume" and "local". Changing this creates a new server.
        :param pulumi.Input[str] device_type: The low-level device type that will be used. Most
               common thing is to leave this empty. Changing this creates a new server.
        :param pulumi.Input[str] disk_bus: The low-level disk bus that will be used. Most common
               thing is to leave this empty. Changing this creates a new server.
        :param pulumi.Input[str] guest_format: Specifies the guest server disk file system format,
               such as `ext2`, `ext3`, `ext4`, `xfs` or `swap`. Swap block device mappings
               have the following restrictions: source_type must be blank and destination_type
               must be local and only one swap disk per server and the size of the swap disk
               must be less than or equal to the swap size of the flavor. Changing this
               creates a new server.
        :param pulumi.Input[str] uuid: The UUID of
               the image, volume, or snapshot. Changing this creates a new server.
        :param pulumi.Input[int] volume_size: The size of the volume to create (in gigabytes). Required
               in the following combinations: source=image and destination=volume,
               source=blank and destination=local, and source=blank and destination=volume.
               Changing this creates a new server.
        :param pulumi.Input[str] volume_type: The volume type that will be used, for example SSD
               or HDD storage. The available options depend on how your specific OpenStack
               cloud is configured and what classes of storage are provided. Changing this
               creates a new server.
        """
        pulumi.set(__self__, "source_type", source_type)
        if boot_index is not None:
            pulumi.set(__self__, "boot_index", boot_index)
        if delete_on_termination is not None:
            pulumi.set(__self__, "delete_on_termination", delete_on_termination)
        if destination_type is not None:
            pulumi.set(__self__, "destination_type", destination_type)
        if device_type is not None:
            pulumi.set(__self__, "device_type", device_type)
        if disk_bus is not None:
            pulumi.set(__self__, "disk_bus", disk_bus)
        if guest_format is not None:
            pulumi.set(__self__, "guest_format", guest_format)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)
        if volume_size is not None:
            pulumi.set(__self__, "volume_size", volume_size)
        if volume_type is not None:
            pulumi.set(__self__, "volume_type", volume_type)

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> pulumi.Input[str]:
        """
        The source type of the device. Must be one of
        "blank", "image", "volume", or "snapshot". Changing this creates a new
        server.
        """
        return pulumi.get(self, "source_type")

    @source_type.setter
    def source_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_type", value)

    @property
    @pulumi.getter(name="bootIndex")
    def boot_index(self) -> Optional[pulumi.Input[int]]:
        """
        The boot index of the volume. It defaults to 0.
        Changing this creates a new server.
        """
        return pulumi.get(self, "boot_index")

    @boot_index.setter
    def boot_index(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "boot_index", value)

    @property
    @pulumi.getter(name="deleteOnTermination")
    def delete_on_termination(self) -> Optional[pulumi.Input[bool]]:
        """
        Delete the volume / block device upon
        termination of the instance. Defaults to false. Changing this creates a
        new server.
        """
        return pulumi.get(self, "delete_on_termination")

    @delete_on_termination.setter
    def delete_on_termination(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_on_termination", value)

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type that gets created. Possible values
        are "volume" and "local". Changing this creates a new server.
        """
        return pulumi.get(self, "destination_type")

    @destination_type.setter
    def destination_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_type", value)

    @property
    @pulumi.getter(name="deviceType")
    def device_type(self) -> Optional[pulumi.Input[str]]:
        """
        The low-level device type that will be used. Most
        common thing is to leave this empty. Changing this creates a new server.
        """
        return pulumi.get(self, "device_type")

    @device_type.setter
    def device_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "device_type", value)

    @property
    @pulumi.getter(name="diskBus")
    def disk_bus(self) -> Optional[pulumi.Input[str]]:
        """
        The low-level disk bus that will be used. Most common
        thing is to leave this empty. Changing this creates a new server.
        """
        return pulumi.get(self, "disk_bus")

    @disk_bus.setter
    def disk_bus(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disk_bus", value)

    @property
    @pulumi.getter(name="guestFormat")
    def guest_format(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the guest server disk file system format,
        such as `ext2`, `ext3`, `ext4`, `xfs` or `swap`. Swap block device mappings
        have the following restrictions: source_type must be blank and destination_type
        must be local and only one swap disk per server and the size of the swap disk
        must be less than or equal to the swap size of the flavor. Changing this
        creates a new server.
        """
        return pulumi.get(self, "guest_format")

    @guest_format.setter
    def guest_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "guest_format", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of
        the image, volume, or snapshot. Changing this creates a new server.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)

    @property
    @pulumi.getter(name="volumeSize")
    def volume_size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the volume to create (in gigabytes). Required
        in the following combinations: source=image and destination=volume,
        source=blank and destination=local, and source=blank and destination=volume.
        Changing this creates a new server.
        """
        return pulumi.get(self, "volume_size")

    @volume_size.setter
    def volume_size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "volume_size", value)

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[pulumi.Input[str]]:
        """
        The volume type that will be used, for example SSD
        or HDD storage. The available options depend on how your specific OpenStack
        cloud is configured and what classes of storage are provided. Changing this
        creates a new server.
        """
        return pulumi.get(self, "volume_type")

    @volume_type.setter
    def volume_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_type", value)


@pulumi.input_type
class InstanceNetworkArgs:
    def __init__(__self__, *,
                 access_network: Optional[pulumi.Input[bool]] = None,
                 fixed_ip_v4: Optional[pulumi.Input[str]] = None,
                 fixed_ip_v6: Optional[pulumi.Input[str]] = None,
                 floating_ip: Optional[pulumi.Input[str]] = None,
                 mac: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 uuid: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] access_network: Specifies if this network should be used for
               provisioning access. Accepts true or false. Defaults to false.
        :param pulumi.Input[str] fixed_ip_v4: Specifies a fixed IPv4 address to be used on this
               network. Changing this creates a new server.
        :param pulumi.Input[str] name: The human-readable
               name of the network. Changing this creates a new server.
        :param pulumi.Input[str] port: The port UUID of a
               network to attach to the server. Changing this creates a new server.
        :param pulumi.Input[str] uuid: The UUID of
               the image, volume, or snapshot. Changing this creates a new server.
        """
        if access_network is not None:
            pulumi.set(__self__, "access_network", access_network)
        if fixed_ip_v4 is not None:
            pulumi.set(__self__, "fixed_ip_v4", fixed_ip_v4)
        if fixed_ip_v6 is not None:
            pulumi.set(__self__, "fixed_ip_v6", fixed_ip_v6)
        if floating_ip is not None:
            pulumi.set(__self__, "floating_ip", floating_ip)
        if mac is not None:
            pulumi.set(__self__, "mac", mac)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="accessNetwork")
    def access_network(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies if this network should be used for
        provisioning access. Accepts true or false. Defaults to false.
        """
        return pulumi.get(self, "access_network")

    @access_network.setter
    def access_network(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "access_network", value)

    @property
    @pulumi.getter(name="fixedIpV4")
    def fixed_ip_v4(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies a fixed IPv4 address to be used on this
        network. Changing this creates a new server.
        """
        return pulumi.get(self, "fixed_ip_v4")

    @fixed_ip_v4.setter
    def fixed_ip_v4(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fixed_ip_v4", value)

    @property
    @pulumi.getter(name="fixedIpV6")
    def fixed_ip_v6(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "fixed_ip_v6")

    @fixed_ip_v6.setter
    def fixed_ip_v6(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fixed_ip_v6", value)

    @property
    @pulumi.getter(name="floatingIp")
    def floating_ip(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "floating_ip")

    @floating_ip.setter
    def floating_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "floating_ip", value)

    @property
    @pulumi.getter
    def mac(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The human-readable
        name of the network. Changing this creates a new server.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        The port UUID of a
        network to attach to the server. Changing this creates a new server.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of
        the image, volume, or snapshot. Changing this creates a new server.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)


@pulumi.input_type
class InstancePersonalityArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 file: pulumi.Input[str]):
        """
        :param pulumi.Input[str] content: The contents of the file. Limited to 255 bytes.
        :param pulumi.Input[str] file: The absolute path of the destination file.
        """
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "file", file)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        The contents of the file. Limited to 255 bytes.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def file(self) -> pulumi.Input[str]:
        """
        The absolute path of the destination file.
        """
        return pulumi.get(self, "file")

    @file.setter
    def file(self, value: pulumi.Input[str]):
        pulumi.set(self, "file", value)


@pulumi.input_type
class InstanceSchedulerHintArgs:
    def __init__(__self__, *,
                 additional_properties: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 build_near_host_ip: Optional[pulumi.Input[str]] = None,
                 different_cells: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 different_hosts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 group: Optional[pulumi.Input[str]] = None,
                 queries: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 same_hosts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 target_cell: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[Mapping[str, Any]] additional_properties: Arbitrary key/value pairs of additional
               properties to pass to the scheduler.
        :param pulumi.Input[str] build_near_host_ip: An IP Address in CIDR form. The instance
               will be placed on a compute node that is in the same subnet.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] different_cells: The names of cells where not to build the instance.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] different_hosts: A list of instance UUIDs. The instance will
               be scheduled on a different host than all other instances.
        :param pulumi.Input[str] group: A UUID of a Server Group. The instance will be placed
               into that group.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] queries: A conditional query that a compute node must pass in
               order to host an instance. The query must use the `JsonFilter` syntax
               which is described
               [here](https://docs.openstack.org/nova/latest/admin/configuration/schedulers.html#jsonfilter).
               At this time, only simple queries are supported. Compound queries using
               `and`, `or`, or `not` are not supported. An example of a simple query is:
        :param pulumi.Input[Sequence[pulumi.Input[str]]] same_hosts: A list of instance UUIDs. The instance will be
               scheduled on the same host of those specified.
        :param pulumi.Input[str] target_cell: The name of a cell to host the instance.
        """
        if additional_properties is not None:
            pulumi.set(__self__, "additional_properties", additional_properties)
        if build_near_host_ip is not None:
            pulumi.set(__self__, "build_near_host_ip", build_near_host_ip)
        if different_cells is not None:
            pulumi.set(__self__, "different_cells", different_cells)
        if different_hosts is not None:
            pulumi.set(__self__, "different_hosts", different_hosts)
        if group is not None:
            pulumi.set(__self__, "group", group)
        if queries is not None:
            pulumi.set(__self__, "queries", queries)
        if same_hosts is not None:
            pulumi.set(__self__, "same_hosts", same_hosts)
        if target_cell is not None:
            pulumi.set(__self__, "target_cell", target_cell)

    @property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Arbitrary key/value pairs of additional
        properties to pass to the scheduler.
        """
        return pulumi.get(self, "additional_properties")

    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "additional_properties", value)

    @property
    @pulumi.getter(name="buildNearHostIp")
    def build_near_host_ip(self) -> Optional[pulumi.Input[str]]:
        """
        An IP Address in CIDR form. The instance
        will be placed on a compute node that is in the same subnet.
        """
        return pulumi.get(self, "build_near_host_ip")

    @build_near_host_ip.setter
    def build_near_host_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "build_near_host_ip", value)

    @property
    @pulumi.getter(name="differentCells")
    def different_cells(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The names of cells where not to build the instance.
        """
        return pulumi.get(self, "different_cells")

    @different_cells.setter
    def different_cells(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "different_cells", value)

    @property
    @pulumi.getter(name="differentHosts")
    def different_hosts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of instance UUIDs. The instance will
        be scheduled on a different host than all other instances.
        """
        return pulumi.get(self, "different_hosts")

    @different_hosts.setter
    def different_hosts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "different_hosts", value)

    @property
    @pulumi.getter
    def group(self) -> Optional[pulumi.Input[str]]:
        """
        A UUID of a Server Group. The instance will be placed
        into that group.
        """
        return pulumi.get(self, "group")

    @group.setter
    def group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group", value)

    @property
    @pulumi.getter
    def queries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A conditional query that a compute node must pass in
        order to host an instance. The query must use the `JsonFilter` syntax
        which is described
        [here](https://docs.openstack.org/nova/latest/admin/configuration/schedulers.html#jsonfilter).
        At this time, only simple queries are supported. Compound queries using
        `and`, `or`, or `not` are not supported. An example of a simple query is:
        """
        return pulumi.get(self, "queries")

    @queries.setter
    def queries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "queries", value)

    @property
    @pulumi.getter(name="sameHosts")
    def same_hosts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of instance UUIDs. The instance will be
        scheduled on the same host of those specified.
        """
        return pulumi.get(self, "same_hosts")

    @same_hosts.setter
    def same_hosts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "same_hosts", value)

    @property
    @pulumi.getter(name="targetCell")
    def target_cell(self) -> Optional[pulumi.Input[str]]:
        """
        The name of a cell to host the instance.
        """
        return pulumi.get(self, "target_cell")

    @target_cell.setter
    def target_cell(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_cell", value)


@pulumi.input_type
class InstanceVendorOptionsArgs:
    def __init__(__self__, *,
                 detach_ports_before_destroy: Optional[pulumi.Input[bool]] = None,
                 ignore_resize_confirmation: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] detach_ports_before_destroy: Whether to try to detach all attached
               ports to the vm before destroying it to make sure the port state is correct
               after the vm destruction. This is helpful when the port is not deleted.
        :param pulumi.Input[bool] ignore_resize_confirmation: Boolean to control whether
               to ignore manual confirmation of the instance resizing. This can be helpful
               to work with some OpenStack clouds which automatically confirm resizing of
               instances after some timeout.
        """
        if detach_ports_before_destroy is not None:
            pulumi.set(__self__, "detach_ports_before_destroy", detach_ports_before_destroy)
        if ignore_resize_confirmation is not None:
            pulumi.set(__self__, "ignore_resize_confirmation", ignore_resize_confirmation)

    @property
    @pulumi.getter(name="detachPortsBeforeDestroy")
    def detach_ports_before_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to try to detach all attached
        ports to the vm before destroying it to make sure the port state is correct
        after the vm destruction. This is helpful when the port is not deleted.
        """
        return pulumi.get(self, "detach_ports_before_destroy")

    @detach_ports_before_destroy.setter
    def detach_ports_before_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "detach_ports_before_destroy", value)

    @property
    @pulumi.getter(name="ignoreResizeConfirmation")
    def ignore_resize_confirmation(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean to control whether
        to ignore manual confirmation of the instance resizing. This can be helpful
        to work with some OpenStack clouds which automatically confirm resizing of
        instances after some timeout.
        """
        return pulumi.get(self, "ignore_resize_confirmation")

    @ignore_resize_confirmation.setter
    def ignore_resize_confirmation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_resize_confirmation", value)


@pulumi.input_type
class SecGroupRuleArgs:
    def __init__(__self__, *,
                 from_port: pulumi.Input[int],
                 ip_protocol: pulumi.Input[str],
                 to_port: pulumi.Input[int],
                 cidr: Optional[pulumi.Input[str]] = None,
                 from_group_id: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 self: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[int] from_port: An integer representing the lower bound of the port
               range to open. Changing this creates a new security group rule.
        :param pulumi.Input[str] ip_protocol: The protocol type that will be allowed. Changing
               this creates a new security group rule.
        :param pulumi.Input[int] to_port: An integer representing the upper bound of the port
               range to open. Changing this creates a new security group rule.
        :param pulumi.Input[str] cidr: Required if `from_group_id` or `self` is empty. The IP range
               that will be the source of network traffic to the security group. Use 0.0.0.0/0
               to allow all IP addresses. Changing this creates a new security group rule. Cannot
               be combined with `from_group_id` or `self`.
        :param pulumi.Input[str] from_group_id: Required if `cidr` or `self` is empty. The ID of a
               group from which to forward traffic to the parent group. Changing this creates a
               new security group rule. Cannot be combined with `cidr` or `self`.
        :param pulumi.Input[bool] self: Required if `cidr` and `from_group_id` is empty. If true,
               the security group itself will be added as a source to this ingress rule. Cannot
               be combined with `cidr` or `from_group_id`.
        """
        pulumi.set(__self__, "from_port", from_port)
        pulumi.set(__self__, "ip_protocol", ip_protocol)
        pulumi.set(__self__, "to_port", to_port)
        if cidr is not None:
            pulumi.set(__self__, "cidr", cidr)
        if from_group_id is not None:
            pulumi.set(__self__, "from_group_id", from_group_id)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if self is not None:
            pulumi.set(__self__, "self", self)

    @property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[int]:
        """
        An integer representing the lower bound of the port
        range to open. Changing this creates a new security group rule.
        """
        return pulumi.get(self, "from_port")

    @from_port.setter
    def from_port(self, value: pulumi.Input[int]):
        pulumi.set(self, "from_port", value)

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Input[str]:
        """
        The protocol type that will be allowed. Changing
        this creates a new security group rule.
        """
        return pulumi.get(self, "ip_protocol")

    @ip_protocol.setter
    def ip_protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_protocol", value)

    @property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[int]:
        """
        An integer representing the upper bound of the port
        range to open. Changing this creates a new security group rule.
        """
        return pulumi.get(self, "to_port")

    @to_port.setter
    def to_port(self, value: pulumi.Input[int]):
        pulumi.set(self, "to_port", value)

    @property
    @pulumi.getter
    def cidr(self) -> Optional[pulumi.Input[str]]:
        """
        Required if `from_group_id` or `self` is empty. The IP range
        that will be the source of network traffic to the security group. Use 0.0.0.0/0
        to allow all IP addresses. Changing this creates a new security group rule. Cannot
        be combined with `from_group_id` or `self`.
        """
        return pulumi.get(self, "cidr")

    @cidr.setter
    def cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr", value)

    @property
    @pulumi.getter(name="fromGroupId")
    def from_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Required if `cidr` or `self` is empty. The ID of a
        group from which to forward traffic to the parent group. Changing this creates a
        new security group rule. Cannot be combined with `cidr` or `self`.
        """
        return pulumi.get(self, "from_group_id")

    @from_group_id.setter
    def from_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "from_group_id", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def self(self) -> Optional[pulumi.Input[bool]]:
        """
        Required if `cidr` and `from_group_id` is empty. If true,
        the security group itself will be added as a source to this ingress rule. Cannot
        be combined with `cidr` or `from_group_id`.
        """
        return pulumi.get(self, "self")

    @self.setter
    def self(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "self", value)


@pulumi.input_type
class VolumeAttachVendorOptionsArgs:
    def __init__(__self__, *,
                 ignore_volume_confirmation: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] ignore_volume_confirmation: Boolean to control whether
               to ignore volume status confirmation of the attached volume. This can be helpful
               to work with some OpenStack clouds which don't have the Block Storage V3 API available.
        """
        if ignore_volume_confirmation is not None:
            pulumi.set(__self__, "ignore_volume_confirmation", ignore_volume_confirmation)

    @property
    @pulumi.getter(name="ignoreVolumeConfirmation")
    def ignore_volume_confirmation(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean to control whether
        to ignore volume status confirmation of the attached volume. This can be helpful
        to work with some OpenStack clouds which don't have the Block Storage V3 API available.
        """
        return pulumi.get(self, "ignore_volume_confirmation")

    @ignore_volume_confirmation.setter
    def ignore_volume_confirmation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ignore_volume_confirmation", value)


@pulumi.input_type
class GetInstanceV2NetworkArgs:
    def __init__(__self__, *,
                 fixed_ip_v4: str,
                 fixed_ip_v6: str,
                 mac: str,
                 name: str,
                 port: str,
                 uuid: str):
        """
        :param str fixed_ip_v4: The IPv4 address assigned to this network port.
        :param str fixed_ip_v6: The IPv6 address assigned to this network port.
        :param str mac: The MAC address assigned to this network interface.
        :param str name: The name of the network
        :param str port: The port UUID for this network
        :param str uuid: The UUID of the network
        """
        pulumi.set(__self__, "fixed_ip_v4", fixed_ip_v4)
        pulumi.set(__self__, "fixed_ip_v6", fixed_ip_v6)
        pulumi.set(__self__, "mac", mac)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="fixedIpV4")
    def fixed_ip_v4(self) -> str:
        """
        The IPv4 address assigned to this network port.
        """
        return pulumi.get(self, "fixed_ip_v4")

    @fixed_ip_v4.setter
    def fixed_ip_v4(self, value: str):
        pulumi.set(self, "fixed_ip_v4", value)

    @property
    @pulumi.getter(name="fixedIpV6")
    def fixed_ip_v6(self) -> str:
        """
        The IPv6 address assigned to this network port.
        """
        return pulumi.get(self, "fixed_ip_v6")

    @fixed_ip_v6.setter
    def fixed_ip_v6(self, value: str):
        pulumi.set(self, "fixed_ip_v6", value)

    @property
    @pulumi.getter
    def mac(self) -> str:
        """
        The MAC address assigned to this network interface.
        """
        return pulumi.get(self, "mac")

    @mac.setter
    def mac(self, value: str):
        pulumi.set(self, "mac", value)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the network
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> str:
        """
        The port UUID for this network
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: str):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        The UUID of the network
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: str):
        pulumi.set(self, "uuid", value)


