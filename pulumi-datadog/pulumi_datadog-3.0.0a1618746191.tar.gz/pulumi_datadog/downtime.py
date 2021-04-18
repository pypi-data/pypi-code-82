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

__all__ = ['DowntimeArgs', 'Downtime']

@pulumi.input_type
class DowntimeArgs:
    def __init__(__self__, *,
                 scopes: pulumi.Input[Sequence[pulumi.Input[str]]],
                 active: Optional[pulumi.Input[bool]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 end: Optional[pulumi.Input[int]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 monitor_id: Optional[pulumi.Input[int]] = None,
                 monitor_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 recurrence: Optional[pulumi.Input['DowntimeRecurrenceArgs']] = None,
                 start: Optional[pulumi.Input[int]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Downtime resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: specify the group scope to which this downtime applies. For everything use '*'
        :param pulumi.Input[bool] active: When true indicates this downtime is being actively applied
        :param pulumi.Input[bool] disabled: When true indicates this downtime is not being applied
        :param pulumi.Input[int] end: Optionally specify an end date when this downtime should expire
        :param pulumi.Input[str] end_date: String representing date and time to end the downtime in RFC3339 format.
        :param pulumi.Input[str] message: An optional message to provide when creating the downtime, can include notification handles
        :param pulumi.Input[int] monitor_id: When specified, this downtime will only apply to this monitor
        :param pulumi.Input[Sequence[pulumi.Input[str]]] monitor_tags: A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies
        :param pulumi.Input['DowntimeRecurrenceArgs'] recurrence: Optional recurring schedule for this downtime
        :param pulumi.Input[int] start: Specify when this downtime should start
        :param pulumi.Input[str] start_date: String representing date and time to start the downtime in RFC3339 format.
        :param pulumi.Input[str] timezone: The timezone for the downtime, default UTC
        """
        pulumi.set(__self__, "scopes", scopes)
        if active is not None:
            pulumi.set(__self__, "active", active)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if end is not None:
            pulumi.set(__self__, "end", end)
        if end_date is not None:
            pulumi.set(__self__, "end_date", end_date)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if monitor_id is not None:
            pulumi.set(__self__, "monitor_id", monitor_id)
        if monitor_tags is not None:
            pulumi.set(__self__, "monitor_tags", monitor_tags)
        if recurrence is not None:
            pulumi.set(__self__, "recurrence", recurrence)
        if start is not None:
            pulumi.set(__self__, "start", start)
        if start_date is not None:
            pulumi.set(__self__, "start_date", start_date)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        specify the group scope to which this downtime applies. For everything use '*'
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        When true indicates this downtime is being actively applied
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        When true indicates this downtime is not being applied
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[int]]:
        """
        Optionally specify an end date when this downtime should expire
        """
        return pulumi.get(self, "end")

    @end.setter
    def end(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "end", value)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[str]]:
        """
        String representing date and time to end the downtime in RFC3339 format.
        """
        return pulumi.get(self, "end_date")

    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_date", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        An optional message to provide when creating the downtime, can include notification handles
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter(name="monitorId")
    def monitor_id(self) -> Optional[pulumi.Input[int]]:
        """
        When specified, this downtime will only apply to this monitor
        """
        return pulumi.get(self, "monitor_id")

    @monitor_id.setter
    def monitor_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "monitor_id", value)

    @property
    @pulumi.getter(name="monitorTags")
    def monitor_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies
        """
        return pulumi.get(self, "monitor_tags")

    @monitor_tags.setter
    def monitor_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "monitor_tags", value)

    @property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input['DowntimeRecurrenceArgs']]:
        """
        Optional recurring schedule for this downtime
        """
        return pulumi.get(self, "recurrence")

    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input['DowntimeRecurrenceArgs']]):
        pulumi.set(self, "recurrence", value)

    @property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[int]]:
        """
        Specify when this downtime should start
        """
        return pulumi.get(self, "start")

    @start.setter
    def start(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "start", value)

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[str]]:
        """
        String representing date and time to start the downtime in RFC3339 format.
        """
        return pulumi.get(self, "start_date")

    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_date", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        """
        The timezone for the downtime, default UTC
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)


@pulumi.input_type
class _DowntimeState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 end: Optional[pulumi.Input[int]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 monitor_id: Optional[pulumi.Input[int]] = None,
                 monitor_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 recurrence: Optional[pulumi.Input['DowntimeRecurrenceArgs']] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 start: Optional[pulumi.Input[int]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Downtime resources.
        :param pulumi.Input[bool] active: When true indicates this downtime is being actively applied
        :param pulumi.Input[bool] disabled: When true indicates this downtime is not being applied
        :param pulumi.Input[int] end: Optionally specify an end date when this downtime should expire
        :param pulumi.Input[str] end_date: String representing date and time to end the downtime in RFC3339 format.
        :param pulumi.Input[str] message: An optional message to provide when creating the downtime, can include notification handles
        :param pulumi.Input[int] monitor_id: When specified, this downtime will only apply to this monitor
        :param pulumi.Input[Sequence[pulumi.Input[str]]] monitor_tags: A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies
        :param pulumi.Input['DowntimeRecurrenceArgs'] recurrence: Optional recurring schedule for this downtime
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: specify the group scope to which this downtime applies. For everything use '*'
        :param pulumi.Input[int] start: Specify when this downtime should start
        :param pulumi.Input[str] start_date: String representing date and time to start the downtime in RFC3339 format.
        :param pulumi.Input[str] timezone: The timezone for the downtime, default UTC
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if end is not None:
            pulumi.set(__self__, "end", end)
        if end_date is not None:
            pulumi.set(__self__, "end_date", end_date)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if monitor_id is not None:
            pulumi.set(__self__, "monitor_id", monitor_id)
        if monitor_tags is not None:
            pulumi.set(__self__, "monitor_tags", monitor_tags)
        if recurrence is not None:
            pulumi.set(__self__, "recurrence", recurrence)
        if scopes is not None:
            pulumi.set(__self__, "scopes", scopes)
        if start is not None:
            pulumi.set(__self__, "start", start)
        if start_date is not None:
            pulumi.set(__self__, "start_date", start_date)
        if timezone is not None:
            pulumi.set(__self__, "timezone", timezone)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        """
        When true indicates this downtime is being actively applied
        """
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        When true indicates this downtime is not being applied
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter
    def end(self) -> Optional[pulumi.Input[int]]:
        """
        Optionally specify an end date when this downtime should expire
        """
        return pulumi.get(self, "end")

    @end.setter
    def end(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "end", value)

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[pulumi.Input[str]]:
        """
        String representing date and time to end the downtime in RFC3339 format.
        """
        return pulumi.get(self, "end_date")

    @end_date.setter
    def end_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_date", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        An optional message to provide when creating the downtime, can include notification handles
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter(name="monitorId")
    def monitor_id(self) -> Optional[pulumi.Input[int]]:
        """
        When specified, this downtime will only apply to this monitor
        """
        return pulumi.get(self, "monitor_id")

    @monitor_id.setter
    def monitor_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "monitor_id", value)

    @property
    @pulumi.getter(name="monitorTags")
    def monitor_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies
        """
        return pulumi.get(self, "monitor_tags")

    @monitor_tags.setter
    def monitor_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "monitor_tags", value)

    @property
    @pulumi.getter
    def recurrence(self) -> Optional[pulumi.Input['DowntimeRecurrenceArgs']]:
        """
        Optional recurring schedule for this downtime
        """
        return pulumi.get(self, "recurrence")

    @recurrence.setter
    def recurrence(self, value: Optional[pulumi.Input['DowntimeRecurrenceArgs']]):
        pulumi.set(self, "recurrence", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        specify the group scope to which this downtime applies. For everything use '*'
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def start(self) -> Optional[pulumi.Input[int]]:
        """
        Specify when this downtime should start
        """
        return pulumi.get(self, "start")

    @start.setter
    def start(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "start", value)

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> Optional[pulumi.Input[str]]:
        """
        String representing date and time to start the downtime in RFC3339 format.
        """
        return pulumi.get(self, "start_date")

    @start_date.setter
    def start_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_date", value)

    @property
    @pulumi.getter
    def timezone(self) -> Optional[pulumi.Input[str]]:
        """
        The timezone for the downtime, default UTC
        """
        return pulumi.get(self, "timezone")

    @timezone.setter
    def timezone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "timezone", value)


class Downtime(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 end: Optional[pulumi.Input[int]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 monitor_id: Optional[pulumi.Input[int]] = None,
                 monitor_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 recurrence: Optional[pulumi.Input[pulumi.InputType['DowntimeRecurrenceArgs']]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 start: Optional[pulumi.Input[int]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Datadog downtime resource. This can be used to create and manage Datadog downtimes.

        ## Example: downtime for a specific monitor

        ```python
        import pulumi
        import pulumi_datadog as datadog

        # Create a new daily 1700-0900 Datadog downtime for a specific monitor id
        foo = datadog.Downtime("foo",
            end=1483365600,
            monitor_id=12345,
            recurrence=datadog.DowntimeRecurrenceArgs(
                period=1,
                type="days",
            ),
            scopes=["*"],
            start=1483308000)
        ```

        ## Example: downtime for all monitors

        ```python
        import pulumi
        import pulumi_datadog as datadog

        # Create a new daily 1700-0900 Datadog downtime for all monitors
        foo = datadog.Downtime("foo",
            end=1483365600,
            recurrence=datadog.DowntimeRecurrenceArgs(
                period=1,
                type="days",
            ),
            scopes=["*"],
            start=1483308000)
        ```

        ## Import

        Downtimes can be imported using their numeric ID, e.g.

        ```sh
         $ pulumi import datadog:index/downtime:Downtime bytes_received_localhost 2081
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: When true indicates this downtime is being actively applied
        :param pulumi.Input[bool] disabled: When true indicates this downtime is not being applied
        :param pulumi.Input[int] end: Optionally specify an end date when this downtime should expire
        :param pulumi.Input[str] end_date: String representing date and time to end the downtime in RFC3339 format.
        :param pulumi.Input[str] message: An optional message to provide when creating the downtime, can include notification handles
        :param pulumi.Input[int] monitor_id: When specified, this downtime will only apply to this monitor
        :param pulumi.Input[Sequence[pulumi.Input[str]]] monitor_tags: A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies
        :param pulumi.Input[pulumi.InputType['DowntimeRecurrenceArgs']] recurrence: Optional recurring schedule for this downtime
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: specify the group scope to which this downtime applies. For everything use '*'
        :param pulumi.Input[int] start: Specify when this downtime should start
        :param pulumi.Input[str] start_date: String representing date and time to start the downtime in RFC3339 format.
        :param pulumi.Input[str] timezone: The timezone for the downtime, default UTC
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DowntimeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Datadog downtime resource. This can be used to create and manage Datadog downtimes.

        ## Example: downtime for a specific monitor

        ```python
        import pulumi
        import pulumi_datadog as datadog

        # Create a new daily 1700-0900 Datadog downtime for a specific monitor id
        foo = datadog.Downtime("foo",
            end=1483365600,
            monitor_id=12345,
            recurrence=datadog.DowntimeRecurrenceArgs(
                period=1,
                type="days",
            ),
            scopes=["*"],
            start=1483308000)
        ```

        ## Example: downtime for all monitors

        ```python
        import pulumi
        import pulumi_datadog as datadog

        # Create a new daily 1700-0900 Datadog downtime for all monitors
        foo = datadog.Downtime("foo",
            end=1483365600,
            recurrence=datadog.DowntimeRecurrenceArgs(
                period=1,
                type="days",
            ),
            scopes=["*"],
            start=1483308000)
        ```

        ## Import

        Downtimes can be imported using their numeric ID, e.g.

        ```sh
         $ pulumi import datadog:index/downtime:Downtime bytes_received_localhost 2081
        ```

        :param str resource_name: The name of the resource.
        :param DowntimeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DowntimeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 end: Optional[pulumi.Input[int]] = None,
                 end_date: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 monitor_id: Optional[pulumi.Input[int]] = None,
                 monitor_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 recurrence: Optional[pulumi.Input[pulumi.InputType['DowntimeRecurrenceArgs']]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 start: Optional[pulumi.Input[int]] = None,
                 start_date: Optional[pulumi.Input[str]] = None,
                 timezone: Optional[pulumi.Input[str]] = None,
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
            __props__ = DowntimeArgs.__new__(DowntimeArgs)

            __props__.__dict__["active"] = active
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["end"] = end
            __props__.__dict__["end_date"] = end_date
            __props__.__dict__["message"] = message
            __props__.__dict__["monitor_id"] = monitor_id
            __props__.__dict__["monitor_tags"] = monitor_tags
            __props__.__dict__["recurrence"] = recurrence
            if scopes is None and not opts.urn:
                raise TypeError("Missing required property 'scopes'")
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["start"] = start
            __props__.__dict__["start_date"] = start_date
            __props__.__dict__["timezone"] = timezone
        super(Downtime, __self__).__init__(
            'datadog:index/downtime:Downtime',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            disabled: Optional[pulumi.Input[bool]] = None,
            end: Optional[pulumi.Input[int]] = None,
            end_date: Optional[pulumi.Input[str]] = None,
            message: Optional[pulumi.Input[str]] = None,
            monitor_id: Optional[pulumi.Input[int]] = None,
            monitor_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            recurrence: Optional[pulumi.Input[pulumi.InputType['DowntimeRecurrenceArgs']]] = None,
            scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            start: Optional[pulumi.Input[int]] = None,
            start_date: Optional[pulumi.Input[str]] = None,
            timezone: Optional[pulumi.Input[str]] = None) -> 'Downtime':
        """
        Get an existing Downtime resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] active: When true indicates this downtime is being actively applied
        :param pulumi.Input[bool] disabled: When true indicates this downtime is not being applied
        :param pulumi.Input[int] end: Optionally specify an end date when this downtime should expire
        :param pulumi.Input[str] end_date: String representing date and time to end the downtime in RFC3339 format.
        :param pulumi.Input[str] message: An optional message to provide when creating the downtime, can include notification handles
        :param pulumi.Input[int] monitor_id: When specified, this downtime will only apply to this monitor
        :param pulumi.Input[Sequence[pulumi.Input[str]]] monitor_tags: A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies
        :param pulumi.Input[pulumi.InputType['DowntimeRecurrenceArgs']] recurrence: Optional recurring schedule for this downtime
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: specify the group scope to which this downtime applies. For everything use '*'
        :param pulumi.Input[int] start: Specify when this downtime should start
        :param pulumi.Input[str] start_date: String representing date and time to start the downtime in RFC3339 format.
        :param pulumi.Input[str] timezone: The timezone for the downtime, default UTC
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DowntimeState.__new__(_DowntimeState)

        __props__.__dict__["active"] = active
        __props__.__dict__["disabled"] = disabled
        __props__.__dict__["end"] = end
        __props__.__dict__["end_date"] = end_date
        __props__.__dict__["message"] = message
        __props__.__dict__["monitor_id"] = monitor_id
        __props__.__dict__["monitor_tags"] = monitor_tags
        __props__.__dict__["recurrence"] = recurrence
        __props__.__dict__["scopes"] = scopes
        __props__.__dict__["start"] = start
        __props__.__dict__["start_date"] = start_date
        __props__.__dict__["timezone"] = timezone
        return Downtime(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[Optional[bool]]:
        """
        When true indicates this downtime is being actively applied
        """
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[Optional[bool]]:
        """
        When true indicates this downtime is not being applied
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter
    def end(self) -> pulumi.Output[Optional[int]]:
        """
        Optionally specify an end date when this downtime should expire
        """
        return pulumi.get(self, "end")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> pulumi.Output[Optional[str]]:
        """
        String representing date and time to end the downtime in RFC3339 format.
        """
        return pulumi.get(self, "end_date")

    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[Optional[str]]:
        """
        An optional message to provide when creating the downtime, can include notification handles
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter(name="monitorId")
    def monitor_id(self) -> pulumi.Output[Optional[int]]:
        """
        When specified, this downtime will only apply to this monitor
        """
        return pulumi.get(self, "monitor_id")

    @property
    @pulumi.getter(name="monitorTags")
    def monitor_tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies
        """
        return pulumi.get(self, "monitor_tags")

    @property
    @pulumi.getter
    def recurrence(self) -> pulumi.Output[Optional['outputs.DowntimeRecurrence']]:
        """
        Optional recurring schedule for this downtime
        """
        return pulumi.get(self, "recurrence")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        specify the group scope to which this downtime applies. For everything use '*'
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def start(self) -> pulumi.Output[Optional[int]]:
        """
        Specify when this downtime should start
        """
        return pulumi.get(self, "start")

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> pulumi.Output[Optional[str]]:
        """
        String representing date and time to start the downtime in RFC3339 format.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter
    def timezone(self) -> pulumi.Output[Optional[str]]:
        """
        The timezone for the downtime, default UTC
        """
        return pulumi.get(self, "timezone")

