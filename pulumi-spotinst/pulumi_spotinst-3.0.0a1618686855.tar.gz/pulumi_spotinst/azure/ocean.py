# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['OceanArgs', 'Ocean']

@pulumi.input_type
class OceanArgs:
    def __init__(__self__, *,
                 acd_identifier: pulumi.Input[str],
                 aks_name: pulumi.Input[str],
                 aks_resource_group_name: pulumi.Input[str],
                 ssh_public_key: pulumi.Input[str],
                 controller_cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Ocean resource.
        :param pulumi.Input[str] acd_identifier: The AKS identifier.
        :param pulumi.Input[str] aks_name: The AKS cluster name.
        :param pulumi.Input[str] aks_resource_group_name: Name of the Resource Group for AKS cluster.
        :param pulumi.Input[str] ssh_public_key: SSH public key for admin access to Linux VMs.
        :param pulumi.Input[str] controller_cluster_id: The Ocean controller cluster.
        :param pulumi.Input[str] name: The Ocean cluster name.
        :param pulumi.Input[str] user_name: Username for admin access to VMs.
        """
        pulumi.set(__self__, "acd_identifier", acd_identifier)
        pulumi.set(__self__, "aks_name", aks_name)
        pulumi.set(__self__, "aks_resource_group_name", aks_resource_group_name)
        pulumi.set(__self__, "ssh_public_key", ssh_public_key)
        if controller_cluster_id is not None:
            pulumi.set(__self__, "controller_cluster_id", controller_cluster_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="acdIdentifier")
    def acd_identifier(self) -> pulumi.Input[str]:
        """
        The AKS identifier.
        """
        return pulumi.get(self, "acd_identifier")

    @acd_identifier.setter
    def acd_identifier(self, value: pulumi.Input[str]):
        pulumi.set(self, "acd_identifier", value)

    @property
    @pulumi.getter(name="aksName")
    def aks_name(self) -> pulumi.Input[str]:
        """
        The AKS cluster name.
        """
        return pulumi.get(self, "aks_name")

    @aks_name.setter
    def aks_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "aks_name", value)

    @property
    @pulumi.getter(name="aksResourceGroupName")
    def aks_resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource Group for AKS cluster.
        """
        return pulumi.get(self, "aks_resource_group_name")

    @aks_resource_group_name.setter
    def aks_resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "aks_resource_group_name", value)

    @property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> pulumi.Input[str]:
        """
        SSH public key for admin access to Linux VMs.
        """
        return pulumi.get(self, "ssh_public_key")

    @ssh_public_key.setter
    def ssh_public_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "ssh_public_key", value)

    @property
    @pulumi.getter(name="controllerClusterId")
    def controller_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Ocean controller cluster.
        """
        return pulumi.get(self, "controller_cluster_id")

    @controller_cluster_id.setter
    def controller_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "controller_cluster_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The Ocean cluster name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        Username for admin access to VMs.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


@pulumi.input_type
class _OceanState:
    def __init__(__self__, *,
                 acd_identifier: Optional[pulumi.Input[str]] = None,
                 aks_name: Optional[pulumi.Input[str]] = None,
                 aks_resource_group_name: Optional[pulumi.Input[str]] = None,
                 controller_cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Ocean resources.
        :param pulumi.Input[str] acd_identifier: The AKS identifier.
        :param pulumi.Input[str] aks_name: The AKS cluster name.
        :param pulumi.Input[str] aks_resource_group_name: Name of the Resource Group for AKS cluster.
        :param pulumi.Input[str] controller_cluster_id: The Ocean controller cluster.
        :param pulumi.Input[str] name: The Ocean cluster name.
        :param pulumi.Input[str] ssh_public_key: SSH public key for admin access to Linux VMs.
        :param pulumi.Input[str] user_name: Username for admin access to VMs.
        """
        if acd_identifier is not None:
            pulumi.set(__self__, "acd_identifier", acd_identifier)
        if aks_name is not None:
            pulumi.set(__self__, "aks_name", aks_name)
        if aks_resource_group_name is not None:
            pulumi.set(__self__, "aks_resource_group_name", aks_resource_group_name)
        if controller_cluster_id is not None:
            pulumi.set(__self__, "controller_cluster_id", controller_cluster_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ssh_public_key is not None:
            pulumi.set(__self__, "ssh_public_key", ssh_public_key)
        if user_name is not None:
            pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="acdIdentifier")
    def acd_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The AKS identifier.
        """
        return pulumi.get(self, "acd_identifier")

    @acd_identifier.setter
    def acd_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "acd_identifier", value)

    @property
    @pulumi.getter(name="aksName")
    def aks_name(self) -> Optional[pulumi.Input[str]]:
        """
        The AKS cluster name.
        """
        return pulumi.get(self, "aks_name")

    @aks_name.setter
    def aks_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aks_name", value)

    @property
    @pulumi.getter(name="aksResourceGroupName")
    def aks_resource_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Resource Group for AKS cluster.
        """
        return pulumi.get(self, "aks_resource_group_name")

    @aks_resource_group_name.setter
    def aks_resource_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "aks_resource_group_name", value)

    @property
    @pulumi.getter(name="controllerClusterId")
    def controller_cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The Ocean controller cluster.
        """
        return pulumi.get(self, "controller_cluster_id")

    @controller_cluster_id.setter
    def controller_cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "controller_cluster_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The Ocean cluster name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> Optional[pulumi.Input[str]]:
        """
        SSH public key for admin access to Linux VMs.
        """
        return pulumi.get(self, "ssh_public_key")

    @ssh_public_key.setter
    def ssh_public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssh_public_key", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        Username for admin access to VMs.
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


class Ocean(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acd_identifier: Optional[pulumi.Input[str]] = None,
                 aks_name: Optional[pulumi.Input[str]] = None,
                 aks_resource_group_name: Optional[pulumi.Input[str]] = None,
                 controller_cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a Spotinst Ocean AKS resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_spotinst as spotinst

        example = spotinst.azure.Ocean("example",
            acd_identifier="acd-12345",
            aks_name="AKSName",
            aks_resource_group_name="ResourceGroupName",
            controller_cluster_id="controller-cluster-id",
            ssh_public_key="ssh-rsa [... redacted ...] generated-by-azure",
            user_name="some-name")
        ```

        ```python
        import pulumi

        pulumi.export("oceanId", spotinst_ocean_aks_["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acd_identifier: The AKS identifier.
        :param pulumi.Input[str] aks_name: The AKS cluster name.
        :param pulumi.Input[str] aks_resource_group_name: Name of the Resource Group for AKS cluster.
        :param pulumi.Input[str] controller_cluster_id: The Ocean controller cluster.
        :param pulumi.Input[str] name: The Ocean cluster name.
        :param pulumi.Input[str] ssh_public_key: SSH public key for admin access to Linux VMs.
        :param pulumi.Input[str] user_name: Username for admin access to VMs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OceanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages a Spotinst Ocean AKS resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_spotinst as spotinst

        example = spotinst.azure.Ocean("example",
            acd_identifier="acd-12345",
            aks_name="AKSName",
            aks_resource_group_name="ResourceGroupName",
            controller_cluster_id="controller-cluster-id",
            ssh_public_key="ssh-rsa [... redacted ...] generated-by-azure",
            user_name="some-name")
        ```

        ```python
        import pulumi

        pulumi.export("oceanId", spotinst_ocean_aks_["example"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param OceanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OceanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acd_identifier: Optional[pulumi.Input[str]] = None,
                 aks_name: Optional[pulumi.Input[str]] = None,
                 aks_resource_group_name: Optional[pulumi.Input[str]] = None,
                 controller_cluster_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[str]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = OceanArgs.__new__(OceanArgs)

            if acd_identifier is None and not opts.urn:
                raise TypeError("Missing required property 'acd_identifier'")
            __props__.__dict__["acd_identifier"] = acd_identifier
            if aks_name is None and not opts.urn:
                raise TypeError("Missing required property 'aks_name'")
            __props__.__dict__["aks_name"] = aks_name
            if aks_resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'aks_resource_group_name'")
            __props__.__dict__["aks_resource_group_name"] = aks_resource_group_name
            __props__.__dict__["controller_cluster_id"] = controller_cluster_id
            __props__.__dict__["name"] = name
            if ssh_public_key is None and not opts.urn:
                raise TypeError("Missing required property 'ssh_public_key'")
            __props__.__dict__["ssh_public_key"] = ssh_public_key
            __props__.__dict__["user_name"] = user_name
        super(Ocean, __self__).__init__(
            'spotinst:azure/ocean:Ocean',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acd_identifier: Optional[pulumi.Input[str]] = None,
            aks_name: Optional[pulumi.Input[str]] = None,
            aks_resource_group_name: Optional[pulumi.Input[str]] = None,
            controller_cluster_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ssh_public_key: Optional[pulumi.Input[str]] = None,
            user_name: Optional[pulumi.Input[str]] = None) -> 'Ocean':
        """
        Get an existing Ocean resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] acd_identifier: The AKS identifier.
        :param pulumi.Input[str] aks_name: The AKS cluster name.
        :param pulumi.Input[str] aks_resource_group_name: Name of the Resource Group for AKS cluster.
        :param pulumi.Input[str] controller_cluster_id: The Ocean controller cluster.
        :param pulumi.Input[str] name: The Ocean cluster name.
        :param pulumi.Input[str] ssh_public_key: SSH public key for admin access to Linux VMs.
        :param pulumi.Input[str] user_name: Username for admin access to VMs.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OceanState.__new__(_OceanState)

        __props__.__dict__["acd_identifier"] = acd_identifier
        __props__.__dict__["aks_name"] = aks_name
        __props__.__dict__["aks_resource_group_name"] = aks_resource_group_name
        __props__.__dict__["controller_cluster_id"] = controller_cluster_id
        __props__.__dict__["name"] = name
        __props__.__dict__["ssh_public_key"] = ssh_public_key
        __props__.__dict__["user_name"] = user_name
        return Ocean(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acdIdentifier")
    def acd_identifier(self) -> pulumi.Output[str]:
        """
        The AKS identifier.
        """
        return pulumi.get(self, "acd_identifier")

    @property
    @pulumi.getter(name="aksName")
    def aks_name(self) -> pulumi.Output[str]:
        """
        The AKS cluster name.
        """
        return pulumi.get(self, "aks_name")

    @property
    @pulumi.getter(name="aksResourceGroupName")
    def aks_resource_group_name(self) -> pulumi.Output[str]:
        """
        Name of the Resource Group for AKS cluster.
        """
        return pulumi.get(self, "aks_resource_group_name")

    @property
    @pulumi.getter(name="controllerClusterId")
    def controller_cluster_id(self) -> pulumi.Output[str]:
        """
        The Ocean controller cluster.
        """
        return pulumi.get(self, "controller_cluster_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The Ocean cluster name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> pulumi.Output[str]:
        """
        SSH public key for admin access to Linux VMs.
        """
        return pulumi.get(self, "ssh_public_key")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        Username for admin access to VMs.
        """
        return pulumi.get(self, "user_name")

