# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DashboardJsonArgs', 'DashboardJson']

@pulumi.input_type
class DashboardJsonArgs:
    def __init__(__self__, *,
                 dashboard_json: pulumi.Input[str]):
        """
        The set of arguments for constructing a DashboardJson resource.
        :param pulumi.Input[str] dashboard_json: See [Wavefront API Documentation](https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance) 
               for instructions on how to get to your API documentation for more details.
        """
        pulumi.set(__self__, "dashboard_json", dashboard_json)

    @property
    @pulumi.getter(name="dashboardJson")
    def dashboard_json(self) -> pulumi.Input[str]:
        """
        See [Wavefront API Documentation](https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance) 
        for instructions on how to get to your API documentation for more details.
        """
        return pulumi.get(self, "dashboard_json")

    @dashboard_json.setter
    def dashboard_json(self, value: pulumi.Input[str]):
        pulumi.set(self, "dashboard_json", value)


@pulumi.input_type
class _DashboardJsonState:
    def __init__(__self__, *,
                 dashboard_json: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DashboardJson resources.
        :param pulumi.Input[str] dashboard_json: See [Wavefront API Documentation](https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance) 
               for instructions on how to get to your API documentation for more details.
        """
        if dashboard_json is not None:
            pulumi.set(__self__, "dashboard_json", dashboard_json)

    @property
    @pulumi.getter(name="dashboardJson")
    def dashboard_json(self) -> Optional[pulumi.Input[str]]:
        """
        See [Wavefront API Documentation](https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance) 
        for instructions on how to get to your API documentation for more details.
        """
        return pulumi.get(self, "dashboard_json")

    @dashboard_json.setter
    def dashboard_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_json", value)


class DashboardJson(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_json: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Wavefront Dashboard JSON resource.  This allows dashboards to be created, updated, and deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_wavefront as wavefront

        test_dashboard_json = wavefront.DashboardJson("testDashboardJson", dashboard_json=\"\"\"{
          "name": "Terraform Test Dashboard Json",
          "description": "a",
          "eventFilterType": "BYCHART",
          "eventQuery": "",
          "defaultTimeWindow": "",
          "url": "tftestimport",
          "displayDescription": false,
          "displaySectionTableOfContents": true,
          "displayQueryParameters": false,
          "sections": [
            {
              "name": "section 1",
              "rows": [
                {
                  "charts": [
                    {
                      "name": "chart 1",
                      "sources": [
                        {
                          "name": "source 1",
                          "query": "ts()",
                          "scatterPlotSource": "Y",
                          "querybuilderEnabled": false,
                          "sourceDescription": ""
                        }
                      ],
                      "units": "someunit",
                      "base": 0,
                      "noDefaultEvents": false,
                      "interpolatePoints": false,
                      "includeObsoleteMetrics": false,
                      "description": "This is chart 1, showing something",
                      "chartSettings": {
                        "type": "markdown-widget",
                        "max": 100,
                        "expectedDataSpacing": 120,
                        "windowing": "full",
                        "windowSize": 10,
                        "autoColumnTags": false,
                        "columnTags": "deprecated",
                        "tagMode": "all",
                        "numTags": 2,
                        "customTags": [
                          "tag1",
                          "tag2"
                        ],
                        "groupBySource": true,
                        "y1Max": 100,
                        "y1Units": "units",
                        "y0ScaleSIBy1024": true,
                        "y1ScaleSIBy1024": true,
                        "y0UnitAutoscaling": true,
                        "y1UnitAutoscaling": true,
                        "fixedLegendEnabled": true,
                        "fixedLegendUseRawStats": true,
                        "fixedLegendPosition": "RIGHT",
                        "fixedLegendDisplayStats": [
                          "stat1",
                          "stat2"
                        ],
                        "fixedLegendFilterSort": "TOP",
                        "fixedLegendFilterLimit": 1,
                        "fixedLegendFilterField": "CURRENT",
                        "plainMarkdownContent": "markdown content"
                      },
                      "summarization": "MEAN"
                    }
                  ],
                  "heightFactor": 50
                }
              ]
            }
          ],
          "parameterDetails": {
            "param": {
              "hideFromView": false,
              "description": null,
              "allowAll": null,
              "tagKey": null,
              "queryValue": null,
              "dynamicFieldType": null,
              "reverseDynSort": null,
              "parameterType": "SIMPLE",
              "label": "test",
              "defaultValue": "Label",
              "valuesToReadableStrings": {
                "Label": "test"
              },
              "selectedLabel": "Label",
              "value": "test"
            }
          },
          "tags" :{
            "customerTags":  ["terraform"]
          }
        }

        \"\"\")
        ```

        ## Import

        Dashboard JSON can be imported using the `id`, e.g.

        ```sh
         $ pulumi import wavefront:index/dashboardJson:DashboardJson dashboard_json tftestimport
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_json: See [Wavefront API Documentation](https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance) 
               for instructions on how to get to your API documentation for more details.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DashboardJsonArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Wavefront Dashboard JSON resource.  This allows dashboards to be created, updated, and deleted.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_wavefront as wavefront

        test_dashboard_json = wavefront.DashboardJson("testDashboardJson", dashboard_json=\"\"\"{
          "name": "Terraform Test Dashboard Json",
          "description": "a",
          "eventFilterType": "BYCHART",
          "eventQuery": "",
          "defaultTimeWindow": "",
          "url": "tftestimport",
          "displayDescription": false,
          "displaySectionTableOfContents": true,
          "displayQueryParameters": false,
          "sections": [
            {
              "name": "section 1",
              "rows": [
                {
                  "charts": [
                    {
                      "name": "chart 1",
                      "sources": [
                        {
                          "name": "source 1",
                          "query": "ts()",
                          "scatterPlotSource": "Y",
                          "querybuilderEnabled": false,
                          "sourceDescription": ""
                        }
                      ],
                      "units": "someunit",
                      "base": 0,
                      "noDefaultEvents": false,
                      "interpolatePoints": false,
                      "includeObsoleteMetrics": false,
                      "description": "This is chart 1, showing something",
                      "chartSettings": {
                        "type": "markdown-widget",
                        "max": 100,
                        "expectedDataSpacing": 120,
                        "windowing": "full",
                        "windowSize": 10,
                        "autoColumnTags": false,
                        "columnTags": "deprecated",
                        "tagMode": "all",
                        "numTags": 2,
                        "customTags": [
                          "tag1",
                          "tag2"
                        ],
                        "groupBySource": true,
                        "y1Max": 100,
                        "y1Units": "units",
                        "y0ScaleSIBy1024": true,
                        "y1ScaleSIBy1024": true,
                        "y0UnitAutoscaling": true,
                        "y1UnitAutoscaling": true,
                        "fixedLegendEnabled": true,
                        "fixedLegendUseRawStats": true,
                        "fixedLegendPosition": "RIGHT",
                        "fixedLegendDisplayStats": [
                          "stat1",
                          "stat2"
                        ],
                        "fixedLegendFilterSort": "TOP",
                        "fixedLegendFilterLimit": 1,
                        "fixedLegendFilterField": "CURRENT",
                        "plainMarkdownContent": "markdown content"
                      },
                      "summarization": "MEAN"
                    }
                  ],
                  "heightFactor": 50
                }
              ]
            }
          ],
          "parameterDetails": {
            "param": {
              "hideFromView": false,
              "description": null,
              "allowAll": null,
              "tagKey": null,
              "queryValue": null,
              "dynamicFieldType": null,
              "reverseDynSort": null,
              "parameterType": "SIMPLE",
              "label": "test",
              "defaultValue": "Label",
              "valuesToReadableStrings": {
                "Label": "test"
              },
              "selectedLabel": "Label",
              "value": "test"
            }
          },
          "tags" :{
            "customerTags":  ["terraform"]
          }
        }

        \"\"\")
        ```

        ## Import

        Dashboard JSON can be imported using the `id`, e.g.

        ```sh
         $ pulumi import wavefront:index/dashboardJson:DashboardJson dashboard_json tftestimport
        ```

        :param str resource_name: The name of the resource.
        :param DashboardJsonArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DashboardJsonArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_json: Optional[pulumi.Input[str]] = None,
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
            __props__ = DashboardJsonArgs.__new__(DashboardJsonArgs)

            if dashboard_json is None and not opts.urn:
                raise TypeError("Missing required property 'dashboard_json'")
            __props__.__dict__["dashboard_json"] = dashboard_json
        super(DashboardJson, __self__).__init__(
            'wavefront:index/dashboardJson:DashboardJson',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dashboard_json: Optional[pulumi.Input[str]] = None) -> 'DashboardJson':
        """
        Get an existing DashboardJson resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_json: See [Wavefront API Documentation](https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance) 
               for instructions on how to get to your API documentation for more details.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DashboardJsonState.__new__(_DashboardJsonState)

        __props__.__dict__["dashboard_json"] = dashboard_json
        return DashboardJson(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dashboardJson")
    def dashboard_json(self) -> pulumi.Output[str]:
        """
        See [Wavefront API Documentation](https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance) 
        for instructions on how to get to your API documentation for more details.
        """
        return pulumi.get(self, "dashboard_json")

