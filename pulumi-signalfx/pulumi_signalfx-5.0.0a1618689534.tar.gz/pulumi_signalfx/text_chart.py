# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['TextChartArgs', 'TextChart']

@pulumi.input_type
class TextChartArgs:
    def __init__(__self__, *,
                 markdown: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TextChart resource.
        :param pulumi.Input[str] markdown: Markdown text to display.
        :param pulumi.Input[str] description: Description of the text note.
        :param pulumi.Input[str] name: Name of the text note.
        """
        pulumi.set(__self__, "markdown", markdown)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def markdown(self) -> pulumi.Input[str]:
        """
        Markdown text to display.
        """
        return pulumi.get(self, "markdown")

    @markdown.setter
    def markdown(self, value: pulumi.Input[str]):
        pulumi.set(self, "markdown", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the text note.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the text note.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TextChartState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 markdown: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TextChart resources.
        :param pulumi.Input[str] description: Description of the text note.
        :param pulumi.Input[str] markdown: Markdown text to display.
        :param pulumi.Input[str] name: Name of the text note.
        :param pulumi.Input[str] url: The URL of the chart.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if markdown is not None:
            pulumi.set(__self__, "markdown", markdown)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the text note.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def markdown(self) -> Optional[pulumi.Input[str]]:
        """
        Markdown text to display.
        """
        return pulumi.get(self, "markdown")

    @markdown.setter
    def markdown(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "markdown", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the text note.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the chart.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class TextChart(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 markdown: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        This special type of chart doesn’t display any metric data. Rather, it lets you place a text note on the dashboard.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_signalfx as signalfx

        mynote0 = signalfx.TextChart("mynote0",
            description="Lorem ipsum dolor sit amet, laudem tibique iracundia at mea. Nam posse dolores ex, nec cu adhuc putent honestatis",
            markdown=\"\"\"    1. First ordered list item
            2. Another item
              * Unordered sub-list.
            1. Actual numbers don't matter, just that it's a number
              1. Ordered sub-list
            4. And another item.

               You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

               To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
               Note that this line is separate, but within the same paragraph.⋅⋅
               (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

            * Unordered list can use asterisks
            - Or minuses
            + Or pluses

        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the text note.
        :param pulumi.Input[str] markdown: Markdown text to display.
        :param pulumi.Input[str] name: Name of the text note.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TextChartArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This special type of chart doesn’t display any metric data. Rather, it lets you place a text note on the dashboard.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_signalfx as signalfx

        mynote0 = signalfx.TextChart("mynote0",
            description="Lorem ipsum dolor sit amet, laudem tibique iracundia at mea. Nam posse dolores ex, nec cu adhuc putent honestatis",
            markdown=\"\"\"    1. First ordered list item
            2. Another item
              * Unordered sub-list.
            1. Actual numbers don't matter, just that it's a number
              1. Ordered sub-list
            4. And another item.

               You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we'll use three here to also align the raw Markdown).

               To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅
               Note that this line is separate, but within the same paragraph.⋅⋅
               (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)

            * Unordered list can use asterisks
            - Or minuses
            + Or pluses

        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param TextChartArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TextChartArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 markdown: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
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
            __props__ = TextChartArgs.__new__(TextChartArgs)

            __props__.__dict__["description"] = description
            if markdown is None and not opts.urn:
                raise TypeError("Missing required property 'markdown'")
            __props__.__dict__["markdown"] = markdown
            __props__.__dict__["name"] = name
            __props__.__dict__["url"] = None
        super(TextChart, __self__).__init__(
            'signalfx:index/textChart:TextChart',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            markdown: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'TextChart':
        """
        Get an existing TextChart resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the text note.
        :param pulumi.Input[str] markdown: Markdown text to display.
        :param pulumi.Input[str] name: Name of the text note.
        :param pulumi.Input[str] url: The URL of the chart.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TextChartState.__new__(_TextChartState)

        __props__.__dict__["description"] = description
        __props__.__dict__["markdown"] = markdown
        __props__.__dict__["name"] = name
        __props__.__dict__["url"] = url
        return TextChart(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the text note.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def markdown(self) -> pulumi.Output[str]:
        """
        Markdown text to display.
        """
        return pulumi.get(self, "markdown")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the text note.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The URL of the chart.
        """
        return pulumi.get(self, "url")

