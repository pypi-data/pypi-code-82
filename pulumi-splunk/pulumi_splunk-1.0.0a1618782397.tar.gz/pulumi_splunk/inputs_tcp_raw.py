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

__all__ = ['InputsTcpRawArgs', 'InputsTcpRaw']

@pulumi.input_type
class InputsTcpRawArgs:
    def __init__(__self__, *,
                 acl: Optional[pulumi.Input['InputsTcpRawAclArgs']] = None,
                 connection_host: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 index: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 queue: Optional[pulumi.Input[str]] = None,
                 raw_tcp_done_timeout: Optional[pulumi.Input[int]] = None,
                 restrict_to_host: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 sourcetype: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InputsTcpRaw resource.
        :param pulumi.Input['InputsTcpRawAclArgs'] acl: The app/user context that is the namespace for the resource
        :param pulumi.Input[str] connection_host: Valid values: (ip | dns | none)
               Set the host for the remote server that is sending data.
               ip sets the host to the IP address of the remote server sending data.
               dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
               none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
               Default value is dns.
        :param pulumi.Input[bool] disabled: Indicates if input is disabled.
        :param pulumi.Input[str] host: Host from which the indexer gets data.
        :param pulumi.Input[str] index: Index to store generated events. Defaults to default.
        :param pulumi.Input[str] name: The input port which receives raw data.
        :param pulumi.Input[str] queue: Valid values: (parsingQueue | indexQueue)
               Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
               Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at "Monitor files and directories with inputs.conf"
               Set queue to indexQueue to send your data directly into the index.
        :param pulumi.Input[int] raw_tcp_done_timeout: Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
               If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.
        :param pulumi.Input[str] restrict_to_host: Allows for restricting this input to only accept data from the host specified here.
        :param pulumi.Input[str] source: Sets the source key/field for events from this input. Defaults to the input file path.
               Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'.
        :param pulumi.Input[str] sourcetype: Set the source type for events from this input.
               "sourcetype=" is automatically prepended to <string>.
               Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).
        """
        if acl is not None:
            pulumi.set(__self__, "acl", acl)
        if connection_host is not None:
            pulumi.set(__self__, "connection_host", connection_host)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if index is not None:
            pulumi.set(__self__, "index", index)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if queue is not None:
            pulumi.set(__self__, "queue", queue)
        if raw_tcp_done_timeout is not None:
            pulumi.set(__self__, "raw_tcp_done_timeout", raw_tcp_done_timeout)
        if restrict_to_host is not None:
            pulumi.set(__self__, "restrict_to_host", restrict_to_host)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if sourcetype is not None:
            pulumi.set(__self__, "sourcetype", sourcetype)

    @property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input['InputsTcpRawAclArgs']]:
        """
        The app/user context that is the namespace for the resource
        """
        return pulumi.get(self, "acl")

    @acl.setter
    def acl(self, value: Optional[pulumi.Input['InputsTcpRawAclArgs']]):
        pulumi.set(self, "acl", value)

    @property
    @pulumi.getter(name="connectionHost")
    def connection_host(self) -> Optional[pulumi.Input[str]]:
        """
        Valid values: (ip | dns | none)
        Set the host for the remote server that is sending data.
        ip sets the host to the IP address of the remote server sending data.
        dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
        none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
        Default value is dns.
        """
        return pulumi.get(self, "connection_host")

    @connection_host.setter
    def connection_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_host", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if input is disabled.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        Host from which the indexer gets data.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def index(self) -> Optional[pulumi.Input[str]]:
        """
        Index to store generated events. Defaults to default.
        """
        return pulumi.get(self, "index")

    @index.setter
    def index(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "index", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The input port which receives raw data.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def queue(self) -> Optional[pulumi.Input[str]]:
        """
        Valid values: (parsingQueue | indexQueue)
        Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
        Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at "Monitor files and directories with inputs.conf"
        Set queue to indexQueue to send your data directly into the index.
        """
        return pulumi.get(self, "queue")

    @queue.setter
    def queue(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue", value)

    @property
    @pulumi.getter(name="rawTcpDoneTimeout")
    def raw_tcp_done_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
        If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.
        """
        return pulumi.get(self, "raw_tcp_done_timeout")

    @raw_tcp_done_timeout.setter
    def raw_tcp_done_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "raw_tcp_done_timeout", value)

    @property
    @pulumi.getter(name="restrictToHost")
    def restrict_to_host(self) -> Optional[pulumi.Input[str]]:
        """
        Allows for restricting this input to only accept data from the host specified here.
        """
        return pulumi.get(self, "restrict_to_host")

    @restrict_to_host.setter
    def restrict_to_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restrict_to_host", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Sets the source key/field for events from this input. Defaults to the input file path.
        Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def sourcetype(self) -> Optional[pulumi.Input[str]]:
        """
        Set the source type for events from this input.
        "sourcetype=" is automatically prepended to <string>.
        Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).
        """
        return pulumi.get(self, "sourcetype")

    @sourcetype.setter
    def sourcetype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sourcetype", value)


@pulumi.input_type
class _InputsTcpRawState:
    def __init__(__self__, *,
                 acl: Optional[pulumi.Input['InputsTcpRawAclArgs']] = None,
                 connection_host: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 index: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 queue: Optional[pulumi.Input[str]] = None,
                 raw_tcp_done_timeout: Optional[pulumi.Input[int]] = None,
                 restrict_to_host: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 sourcetype: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InputsTcpRaw resources.
        :param pulumi.Input['InputsTcpRawAclArgs'] acl: The app/user context that is the namespace for the resource
        :param pulumi.Input[str] connection_host: Valid values: (ip | dns | none)
               Set the host for the remote server that is sending data.
               ip sets the host to the IP address of the remote server sending data.
               dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
               none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
               Default value is dns.
        :param pulumi.Input[bool] disabled: Indicates if input is disabled.
        :param pulumi.Input[str] host: Host from which the indexer gets data.
        :param pulumi.Input[str] index: Index to store generated events. Defaults to default.
        :param pulumi.Input[str] name: The input port which receives raw data.
        :param pulumi.Input[str] queue: Valid values: (parsingQueue | indexQueue)
               Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
               Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at "Monitor files and directories with inputs.conf"
               Set queue to indexQueue to send your data directly into the index.
        :param pulumi.Input[int] raw_tcp_done_timeout: Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
               If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.
        :param pulumi.Input[str] restrict_to_host: Allows for restricting this input to only accept data from the host specified here.
        :param pulumi.Input[str] source: Sets the source key/field for events from this input. Defaults to the input file path.
               Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'.
        :param pulumi.Input[str] sourcetype: Set the source type for events from this input.
               "sourcetype=" is automatically prepended to <string>.
               Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).
        """
        if acl is not None:
            pulumi.set(__self__, "acl", acl)
        if connection_host is not None:
            pulumi.set(__self__, "connection_host", connection_host)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if host is not None:
            pulumi.set(__self__, "host", host)
        if index is not None:
            pulumi.set(__self__, "index", index)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if queue is not None:
            pulumi.set(__self__, "queue", queue)
        if raw_tcp_done_timeout is not None:
            pulumi.set(__self__, "raw_tcp_done_timeout", raw_tcp_done_timeout)
        if restrict_to_host is not None:
            pulumi.set(__self__, "restrict_to_host", restrict_to_host)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if sourcetype is not None:
            pulumi.set(__self__, "sourcetype", sourcetype)

    @property
    @pulumi.getter
    def acl(self) -> Optional[pulumi.Input['InputsTcpRawAclArgs']]:
        """
        The app/user context that is the namespace for the resource
        """
        return pulumi.get(self, "acl")

    @acl.setter
    def acl(self, value: Optional[pulumi.Input['InputsTcpRawAclArgs']]):
        pulumi.set(self, "acl", value)

    @property
    @pulumi.getter(name="connectionHost")
    def connection_host(self) -> Optional[pulumi.Input[str]]:
        """
        Valid values: (ip | dns | none)
        Set the host for the remote server that is sending data.
        ip sets the host to the IP address of the remote server sending data.
        dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
        none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
        Default value is dns.
        """
        return pulumi.get(self, "connection_host")

    @connection_host.setter
    def connection_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_host", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if input is disabled.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[str]]:
        """
        Host from which the indexer gets data.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def index(self) -> Optional[pulumi.Input[str]]:
        """
        Index to store generated events. Defaults to default.
        """
        return pulumi.get(self, "index")

    @index.setter
    def index(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "index", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The input port which receives raw data.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def queue(self) -> Optional[pulumi.Input[str]]:
        """
        Valid values: (parsingQueue | indexQueue)
        Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
        Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at "Monitor files and directories with inputs.conf"
        Set queue to indexQueue to send your data directly into the index.
        """
        return pulumi.get(self, "queue")

    @queue.setter
    def queue(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue", value)

    @property
    @pulumi.getter(name="rawTcpDoneTimeout")
    def raw_tcp_done_timeout(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
        If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.
        """
        return pulumi.get(self, "raw_tcp_done_timeout")

    @raw_tcp_done_timeout.setter
    def raw_tcp_done_timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "raw_tcp_done_timeout", value)

    @property
    @pulumi.getter(name="restrictToHost")
    def restrict_to_host(self) -> Optional[pulumi.Input[str]]:
        """
        Allows for restricting this input to only accept data from the host specified here.
        """
        return pulumi.get(self, "restrict_to_host")

    @restrict_to_host.setter
    def restrict_to_host(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restrict_to_host", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Sets the source key/field for events from this input. Defaults to the input file path.
        Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def sourcetype(self) -> Optional[pulumi.Input[str]]:
        """
        Set the source type for events from this input.
        "sourcetype=" is automatically prepended to <string>.
        Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).
        """
        return pulumi.get(self, "sourcetype")

    @sourcetype.setter
    def sourcetype(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sourcetype", value)


class InputsTcpRaw(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl: Optional[pulumi.Input[pulumi.InputType['InputsTcpRawAclArgs']]] = None,
                 connection_host: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 index: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 queue: Optional[pulumi.Input[str]] = None,
                 raw_tcp_done_timeout: Optional[pulumi.Input[int]] = None,
                 restrict_to_host: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 sourcetype: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## # Resource: InputsTcpRaw

        Create or update raw TCP input information for managing raw tcp inputs from forwarders.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_splunk as splunk

        tcp_raw = splunk.InputsTcpRaw("tcpRaw",
            disabled=False,
            index="main",
            queue="indexQueue",
            source="new",
            sourcetype="new")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['InputsTcpRawAclArgs']] acl: The app/user context that is the namespace for the resource
        :param pulumi.Input[str] connection_host: Valid values: (ip | dns | none)
               Set the host for the remote server that is sending data.
               ip sets the host to the IP address of the remote server sending data.
               dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
               none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
               Default value is dns.
        :param pulumi.Input[bool] disabled: Indicates if input is disabled.
        :param pulumi.Input[str] host: Host from which the indexer gets data.
        :param pulumi.Input[str] index: Index to store generated events. Defaults to default.
        :param pulumi.Input[str] name: The input port which receives raw data.
        :param pulumi.Input[str] queue: Valid values: (parsingQueue | indexQueue)
               Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
               Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at "Monitor files and directories with inputs.conf"
               Set queue to indexQueue to send your data directly into the index.
        :param pulumi.Input[int] raw_tcp_done_timeout: Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
               If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.
        :param pulumi.Input[str] restrict_to_host: Allows for restricting this input to only accept data from the host specified here.
        :param pulumi.Input[str] source: Sets the source key/field for events from this input. Defaults to the input file path.
               Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'.
        :param pulumi.Input[str] sourcetype: Set the source type for events from this input.
               "sourcetype=" is automatically prepended to <string>.
               Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InputsTcpRawArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## # Resource: InputsTcpRaw

        Create or update raw TCP input information for managing raw tcp inputs from forwarders.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_splunk as splunk

        tcp_raw = splunk.InputsTcpRaw("tcpRaw",
            disabled=False,
            index="main",
            queue="indexQueue",
            source="new",
            sourcetype="new")
        ```

        :param str resource_name: The name of the resource.
        :param InputsTcpRawArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InputsTcpRawArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 acl: Optional[pulumi.Input[pulumi.InputType['InputsTcpRawAclArgs']]] = None,
                 connection_host: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 index: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 queue: Optional[pulumi.Input[str]] = None,
                 raw_tcp_done_timeout: Optional[pulumi.Input[int]] = None,
                 restrict_to_host: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 sourcetype: Optional[pulumi.Input[str]] = None,
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
            __props__ = InputsTcpRawArgs.__new__(InputsTcpRawArgs)

            __props__.__dict__["acl"] = acl
            __props__.__dict__["connection_host"] = connection_host
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["host"] = host
            __props__.__dict__["index"] = index
            __props__.__dict__["name"] = name
            __props__.__dict__["queue"] = queue
            __props__.__dict__["raw_tcp_done_timeout"] = raw_tcp_done_timeout
            __props__.__dict__["restrict_to_host"] = restrict_to_host
            __props__.__dict__["source"] = source
            __props__.__dict__["sourcetype"] = sourcetype
        super(InputsTcpRaw, __self__).__init__(
            'splunk:index/inputsTcpRaw:InputsTcpRaw',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            acl: Optional[pulumi.Input[pulumi.InputType['InputsTcpRawAclArgs']]] = None,
            connection_host: Optional[pulumi.Input[str]] = None,
            disabled: Optional[pulumi.Input[bool]] = None,
            host: Optional[pulumi.Input[str]] = None,
            index: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            queue: Optional[pulumi.Input[str]] = None,
            raw_tcp_done_timeout: Optional[pulumi.Input[int]] = None,
            restrict_to_host: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None,
            sourcetype: Optional[pulumi.Input[str]] = None) -> 'InputsTcpRaw':
        """
        Get an existing InputsTcpRaw resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['InputsTcpRawAclArgs']] acl: The app/user context that is the namespace for the resource
        :param pulumi.Input[str] connection_host: Valid values: (ip | dns | none)
               Set the host for the remote server that is sending data.
               ip sets the host to the IP address of the remote server sending data.
               dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
               none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
               Default value is dns.
        :param pulumi.Input[bool] disabled: Indicates if input is disabled.
        :param pulumi.Input[str] host: Host from which the indexer gets data.
        :param pulumi.Input[str] index: Index to store generated events. Defaults to default.
        :param pulumi.Input[str] name: The input port which receives raw data.
        :param pulumi.Input[str] queue: Valid values: (parsingQueue | indexQueue)
               Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
               Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at "Monitor files and directories with inputs.conf"
               Set queue to indexQueue to send your data directly into the index.
        :param pulumi.Input[int] raw_tcp_done_timeout: Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
               If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.
        :param pulumi.Input[str] restrict_to_host: Allows for restricting this input to only accept data from the host specified here.
        :param pulumi.Input[str] source: Sets the source key/field for events from this input. Defaults to the input file path.
               Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'.
        :param pulumi.Input[str] sourcetype: Set the source type for events from this input.
               "sourcetype=" is automatically prepended to <string>.
               Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InputsTcpRawState.__new__(_InputsTcpRawState)

        __props__.__dict__["acl"] = acl
        __props__.__dict__["connection_host"] = connection_host
        __props__.__dict__["disabled"] = disabled
        __props__.__dict__["host"] = host
        __props__.__dict__["index"] = index
        __props__.__dict__["name"] = name
        __props__.__dict__["queue"] = queue
        __props__.__dict__["raw_tcp_done_timeout"] = raw_tcp_done_timeout
        __props__.__dict__["restrict_to_host"] = restrict_to_host
        __props__.__dict__["source"] = source
        __props__.__dict__["sourcetype"] = sourcetype
        return InputsTcpRaw(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def acl(self) -> pulumi.Output['outputs.InputsTcpRawAcl']:
        """
        The app/user context that is the namespace for the resource
        """
        return pulumi.get(self, "acl")

    @property
    @pulumi.getter(name="connectionHost")
    def connection_host(self) -> pulumi.Output[str]:
        """
        Valid values: (ip | dns | none)
        Set the host for the remote server that is sending data.
        ip sets the host to the IP address of the remote server sending data.
        dns sets the host to the reverse DNS entry for the IP address of the remote server sending data.
        none leaves the host as specified in inputs.conf, which is typically the Splunk system hostname.
        Default value is dns.
        """
        return pulumi.get(self, "connection_host")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[bool]:
        """
        Indicates if input is disabled.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        Host from which the indexer gets data.
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def index(self) -> pulumi.Output[str]:
        """
        Index to store generated events. Defaults to default.
        """
        return pulumi.get(self, "index")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The input port which receives raw data.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def queue(self) -> pulumi.Output[str]:
        """
        Valid values: (parsingQueue | indexQueue)
        Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.
        Set queue to parsingQueue to apply props.conf and other parsing rules to your data. For more information about props.conf and rules for timestamping and linebreaking, refer to props.conf and the online documentation at "Monitor files and directories with inputs.conf"
        Set queue to indexQueue to send your data directly into the index.
        """
        return pulumi.get(self, "queue")

    @property
    @pulumi.getter(name="rawTcpDoneTimeout")
    def raw_tcp_done_timeout(self) -> pulumi.Output[int]:
        """
        Specifies in seconds the timeout value for adding a Done-key. Default value is 10 seconds.
        If a connection over the port specified by name remains idle after receiving data for specified number of seconds, it adds a Done-key. This implies the last event is completely received.
        """
        return pulumi.get(self, "raw_tcp_done_timeout")

    @property
    @pulumi.getter(name="restrictToHost")
    def restrict_to_host(self) -> pulumi.Output[str]:
        """
        Allows for restricting this input to only accept data from the host specified here.
        """
        return pulumi.get(self, "restrict_to_host")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        """
        Sets the source key/field for events from this input. Defaults to the input file path.
        Sets the source key initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def sourcetype(self) -> pulumi.Output[str]:
        """
        Set the source type for events from this input.
        "sourcetype=" is automatically prepended to <string>.
        Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).
        """
        return pulumi.get(self, "sourcetype")

