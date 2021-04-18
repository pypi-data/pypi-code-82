# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SecurityServiceArgs', 'SecurityService']

@pulumi.input_type
class SecurityServiceArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 dns_ip: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ou: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityService resource.
        :param pulumi.Input[str] type: The security service type - can either be active\_directory,
               kerberos or ldap.  Changing this updates the existing security service.
        :param pulumi.Input[str] description: The human-readable description for the security service.
               Changing this updates the description of the existing security service.
        :param pulumi.Input[str] dns_ip: The security service DNS IP address that is used inside the
               tenant network.
        :param pulumi.Input[str] domain: The security service domain.
        :param pulumi.Input[str] name: The name of the security service. Changing this updates the name
               of the existing security service.
        :param pulumi.Input[str] ou: The security service ou. An organizational unit can be added to
               specify where the share ends up. New in Manila microversion 2.44.
        :param pulumi.Input[str] password: The user password, if you specify a user.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a security service. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               security service.
        :param pulumi.Input[str] server: The security service host name or IP address.
        :param pulumi.Input[str] user: The security service user or group name that is used by the
               tenant.
        """
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dns_ip is not None:
            pulumi.set(__self__, "dns_ip", dns_ip)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ou is not None:
            pulumi.set(__self__, "ou", ou)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if server is not None:
            pulumi.set(__self__, "server", server)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The security service type - can either be active\_directory,
        kerberos or ldap.  Changing this updates the existing security service.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The human-readable description for the security service.
        Changing this updates the description of the existing security service.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dnsIp")
    def dns_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The security service DNS IP address that is used inside the
        tenant network.
        """
        return pulumi.get(self, "dns_ip")

    @dns_ip.setter
    def dns_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_ip", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The security service domain.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the security service. Changing this updates the name
        of the existing security service.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def ou(self) -> Optional[pulumi.Input[str]]:
        """
        The security service ou. An organizational unit can be added to
        specify where the share ends up. New in Manila microversion 2.44.
        """
        return pulumi.get(self, "ou")

    @ou.setter
    def ou(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ou", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The user password, if you specify a user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Shared File System client.
        A Shared File System client is needed to create a security service. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        security service.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[str]]:
        """
        The security service host name or IP address.
        """
        return pulumi.get(self, "server")

    @server.setter
    def server(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        The security service user or group name that is used by the
        tenant.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


@pulumi.input_type
class _SecurityServiceState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_ip: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ou: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecurityService resources.
        :param pulumi.Input[str] description: The human-readable description for the security service.
               Changing this updates the description of the existing security service.
        :param pulumi.Input[str] dns_ip: The security service DNS IP address that is used inside the
               tenant network.
        :param pulumi.Input[str] domain: The security service domain.
        :param pulumi.Input[str] name: The name of the security service. Changing this updates the name
               of the existing security service.
        :param pulumi.Input[str] ou: The security service ou. An organizational unit can be added to
               specify where the share ends up. New in Manila microversion 2.44.
        :param pulumi.Input[str] password: The user password, if you specify a user.
        :param pulumi.Input[str] project_id: The owner of the Security Service.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a security service. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               security service.
        :param pulumi.Input[str] server: The security service host name or IP address.
        :param pulumi.Input[str] type: The security service type - can either be active\_directory,
               kerberos or ldap.  Changing this updates the existing security service.
        :param pulumi.Input[str] user: The security service user or group name that is used by the
               tenant.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if dns_ip is not None:
            pulumi.set(__self__, "dns_ip", dns_ip)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if ou is not None:
            pulumi.set(__self__, "ou", ou)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if server is not None:
            pulumi.set(__self__, "server", server)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The human-readable description for the security service.
        Changing this updates the description of the existing security service.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="dnsIp")
    def dns_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The security service DNS IP address that is used inside the
        tenant network.
        """
        return pulumi.get(self, "dns_ip")

    @dns_ip.setter
    def dns_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_ip", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        """
        The security service domain.
        """
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the security service. Changing this updates the name
        of the existing security service.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def ou(self) -> Optional[pulumi.Input[str]]:
        """
        The security service ou. An organizational unit can be added to
        specify where the share ends up. New in Manila microversion 2.44.
        """
        return pulumi.get(self, "ou")

    @ou.setter
    def ou(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ou", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The user password, if you specify a user.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The owner of the Security Service.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[str]]:
        """
        The region in which to obtain the V2 Shared File System client.
        A Shared File System client is needed to create a security service. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        security service.
        """
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter
    def server(self) -> Optional[pulumi.Input[str]]:
        """
        The security service host name or IP address.
        """
        return pulumi.get(self, "server")

    @server.setter
    def server(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The security service type - can either be active\_directory,
        kerberos or ldap.  Changing this updates the existing security service.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def user(self) -> Optional[pulumi.Input[str]]:
        """
        The security service user or group name that is used by the
        tenant.
        """
        return pulumi.get(self, "user")

    @user.setter
    def user(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user", value)


class SecurityService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_ip: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ou: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Use this resource to configure a security service.

        > **Note:** All arguments including the security service password will be
        stored in the raw state as plain-text. [Read more about sensitive data in
        state](https://www.terraform.io/docs/state/sensitive-data.html).

        A security service stores configuration information for clients for
        authentication and authorization (AuthN/AuthZ). For example, a share server
        will be the client for an existing service such as LDAP, Kerberos, or
        Microsoft Active Directory.

        Minimum supported Manila microversion is 2.7.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        securityservice1 = openstack.sharedfilesystem.SecurityService("securityservice1",
            description="created by terraform",
            dns_ip="192.168.199.10",
            domain="example.com",
            ou="CN=Computers,DC=example,DC=com",
            password="s8cret",
            server="192.168.199.10",
            type="active_directory",
            user="joinDomainUser")
        ```

        ## Import

        This resource can be imported by specifying the ID of the security service

        ```sh
         $ pulumi import openstack:sharedfilesystem/securityService:SecurityService securityservice_1 <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description for the security service.
               Changing this updates the description of the existing security service.
        :param pulumi.Input[str] dns_ip: The security service DNS IP address that is used inside the
               tenant network.
        :param pulumi.Input[str] domain: The security service domain.
        :param pulumi.Input[str] name: The name of the security service. Changing this updates the name
               of the existing security service.
        :param pulumi.Input[str] ou: The security service ou. An organizational unit can be added to
               specify where the share ends up. New in Manila microversion 2.44.
        :param pulumi.Input[str] password: The user password, if you specify a user.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a security service. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               security service.
        :param pulumi.Input[str] server: The security service host name or IP address.
        :param pulumi.Input[str] type: The security service type - can either be active\_directory,
               kerberos or ldap.  Changing this updates the existing security service.
        :param pulumi.Input[str] user: The security service user or group name that is used by the
               tenant.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use this resource to configure a security service.

        > **Note:** All arguments including the security service password will be
        stored in the raw state as plain-text. [Read more about sensitive data in
        state](https://www.terraform.io/docs/state/sensitive-data.html).

        A security service stores configuration information for clients for
        authentication and authorization (AuthN/AuthZ). For example, a share server
        will be the client for an existing service such as LDAP, Kerberos, or
        Microsoft Active Directory.

        Minimum supported Manila microversion is 2.7.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        securityservice1 = openstack.sharedfilesystem.SecurityService("securityservice1",
            description="created by terraform",
            dns_ip="192.168.199.10",
            domain="example.com",
            ou="CN=Computers,DC=example,DC=com",
            password="s8cret",
            server="192.168.199.10",
            type="active_directory",
            user="joinDomainUser")
        ```

        ## Import

        This resource can be imported by specifying the ID of the security service

        ```sh
         $ pulumi import openstack:sharedfilesystem/securityService:SecurityService securityservice_1 <id>
        ```

        :param str resource_name: The name of the resource.
        :param SecurityServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_ip: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 ou: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 server: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 user: Optional[pulumi.Input[str]] = None,
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
            __props__ = SecurityServiceArgs.__new__(SecurityServiceArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["dns_ip"] = dns_ip
            __props__.__dict__["domain"] = domain
            __props__.__dict__["name"] = name
            __props__.__dict__["ou"] = ou
            __props__.__dict__["password"] = password
            __props__.__dict__["region"] = region
            __props__.__dict__["server"] = server
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["user"] = user
            __props__.__dict__["project_id"] = None
        super(SecurityService, __self__).__init__(
            'openstack:sharedfilesystem/securityService:SecurityService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            dns_ip: Optional[pulumi.Input[str]] = None,
            domain: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            ou: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            server: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            user: Optional[pulumi.Input[str]] = None) -> 'SecurityService':
        """
        Get an existing SecurityService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description for the security service.
               Changing this updates the description of the existing security service.
        :param pulumi.Input[str] dns_ip: The security service DNS IP address that is used inside the
               tenant network.
        :param pulumi.Input[str] domain: The security service domain.
        :param pulumi.Input[str] name: The name of the security service. Changing this updates the name
               of the existing security service.
        :param pulumi.Input[str] ou: The security service ou. An organizational unit can be added to
               specify where the share ends up. New in Manila microversion 2.44.
        :param pulumi.Input[str] password: The user password, if you specify a user.
        :param pulumi.Input[str] project_id: The owner of the Security Service.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a security service. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               security service.
        :param pulumi.Input[str] server: The security service host name or IP address.
        :param pulumi.Input[str] type: The security service type - can either be active\_directory,
               kerberos or ldap.  Changing this updates the existing security service.
        :param pulumi.Input[str] user: The security service user or group name that is used by the
               tenant.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecurityServiceState.__new__(_SecurityServiceState)

        __props__.__dict__["description"] = description
        __props__.__dict__["dns_ip"] = dns_ip
        __props__.__dict__["domain"] = domain
        __props__.__dict__["name"] = name
        __props__.__dict__["ou"] = ou
        __props__.__dict__["password"] = password
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["region"] = region
        __props__.__dict__["server"] = server
        __props__.__dict__["type"] = type
        __props__.__dict__["user"] = user
        return SecurityService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The human-readable description for the security service.
        Changing this updates the description of the existing security service.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsIp")
    def dns_ip(self) -> pulumi.Output[Optional[str]]:
        """
        The security service DNS IP address that is used inside the
        tenant network.
        """
        return pulumi.get(self, "dns_ip")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        """
        The security service domain.
        """
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the security service. Changing this updates the name
        of the existing security service.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ou(self) -> pulumi.Output[Optional[str]]:
        """
        The security service ou. An organizational unit can be added to
        specify where the share ends up. New in Manila microversion 2.44.
        """
        return pulumi.get(self, "ou")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The user password, if you specify a user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The owner of the Security Service.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Shared File System client.
        A Shared File System client is needed to create a security service. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        security service.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def server(self) -> pulumi.Output[Optional[str]]:
        """
        The security service host name or IP address.
        """
        return pulumi.get(self, "server")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The security service type - can either be active\_directory,
        kerberos or ldap.  Changing this updates the existing security service.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def user(self) -> pulumi.Output[Optional[str]]:
        """
        The security service user or group name that is used by the
        tenant.
        """
        return pulumi.get(self, "user")

