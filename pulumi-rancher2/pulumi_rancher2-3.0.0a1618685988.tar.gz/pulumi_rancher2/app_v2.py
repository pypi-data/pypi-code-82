# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AppV2Args', 'AppV2']

@pulumi.input_type
class AppV2Args:
    def __init__(__self__, *,
                 chart_name: pulumi.Input[str],
                 cluster_id: pulumi.Input[str],
                 namespace: pulumi.Input[str],
                 repo_name: pulumi.Input[str],
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 chart_version: Optional[pulumi.Input[str]] = None,
                 cleanup_on_fail: Optional[pulumi.Input[bool]] = None,
                 disable_hooks: Optional[pulumi.Input[bool]] = None,
                 disable_open_api_validation: Optional[pulumi.Input[bool]] = None,
                 force_upgrade: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[str]] = None,
                 wait: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a AppV2 resource.
        :param pulumi.Input[str] chart_name: The app v2 chart name (string)
        :param pulumi.Input[str] cluster_id: The cluster id of the app (string)
        :param pulumi.Input[str] namespace: The namespace of the app v2 (string)
        :param pulumi.Input[str] repo_name: Repo name (string)
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for the app v2 (map)
        :param pulumi.Input[str] chart_version: The app v2 chart version (string)
        :param pulumi.Input[bool] cleanup_on_fail: Cleanup app v2 on failed chart upgrade. Default: `false` (bool)
        :param pulumi.Input[bool] disable_hooks: Disable app v2 chart hooks. Default: `false` (bool)
        :param pulumi.Input[bool] disable_open_api_validation: Disable app V2 Open API Validation. Default: `false` (bool)
        :param pulumi.Input[bool] force_upgrade: Force app V2 chart upgrade. Default: `false` (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for the app v2 (map)
        :param pulumi.Input[str] name: The name of the app v2 (string)
        :param pulumi.Input[str] project_id: Deploy the app v2 within project ID (string)
        :param pulumi.Input[str] values: The app v2 values yaml. Yaml format is required (string)
        :param pulumi.Input[bool] wait: Wait until app is deployed. Default: `true` (bool)
        """
        pulumi.set(__self__, "chart_name", chart_name)
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "namespace", namespace)
        pulumi.set(__self__, "repo_name", repo_name)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if chart_version is not None:
            pulumi.set(__self__, "chart_version", chart_version)
        if cleanup_on_fail is not None:
            pulumi.set(__self__, "cleanup_on_fail", cleanup_on_fail)
        if disable_hooks is not None:
            pulumi.set(__self__, "disable_hooks", disable_hooks)
        if disable_open_api_validation is not None:
            pulumi.set(__self__, "disable_open_api_validation", disable_open_api_validation)
        if force_upgrade is not None:
            pulumi.set(__self__, "force_upgrade", force_upgrade)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if values is not None:
            pulumi.set(__self__, "values", values)
        if wait is not None:
            pulumi.set(__self__, "wait", wait)

    @property
    @pulumi.getter(name="chartName")
    def chart_name(self) -> pulumi.Input[str]:
        """
        The app v2 chart name (string)
        """
        return pulumi.get(self, "chart_name")

    @chart_name.setter
    def chart_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "chart_name", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The cluster id of the app (string)
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Input[str]:
        """
        The namespace of the app v2 (string)
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> pulumi.Input[str]:
        """
        Repo name (string)
        """
        return pulumi.get(self, "repo_name")

    @repo_name.setter
    def repo_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "repo_name", value)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Annotations for the app v2 (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="chartVersion")
    def chart_version(self) -> Optional[pulumi.Input[str]]:
        """
        The app v2 chart version (string)
        """
        return pulumi.get(self, "chart_version")

    @chart_version.setter
    def chart_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "chart_version", value)

    @property
    @pulumi.getter(name="cleanupOnFail")
    def cleanup_on_fail(self) -> Optional[pulumi.Input[bool]]:
        """
        Cleanup app v2 on failed chart upgrade. Default: `false` (bool)
        """
        return pulumi.get(self, "cleanup_on_fail")

    @cleanup_on_fail.setter
    def cleanup_on_fail(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cleanup_on_fail", value)

    @property
    @pulumi.getter(name="disableHooks")
    def disable_hooks(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable app v2 chart hooks. Default: `false` (bool)
        """
        return pulumi.get(self, "disable_hooks")

    @disable_hooks.setter
    def disable_hooks(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_hooks", value)

    @property
    @pulumi.getter(name="disableOpenApiValidation")
    def disable_open_api_validation(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable app V2 Open API Validation. Default: `false` (bool)
        """
        return pulumi.get(self, "disable_open_api_validation")

    @disable_open_api_validation.setter
    def disable_open_api_validation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_open_api_validation", value)

    @property
    @pulumi.getter(name="forceUpgrade")
    def force_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        Force app V2 chart upgrade. Default: `false` (bool)
        """
        return pulumi.get(self, "force_upgrade")

    @force_upgrade.setter
    def force_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_upgrade", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Labels for the app v2 (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the app v2 (string)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Deploy the app v2 within project ID (string)
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[str]]:
        """
        The app v2 values yaml. Yaml format is required (string)
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def wait(self) -> Optional[pulumi.Input[bool]]:
        """
        Wait until app is deployed. Default: `true` (bool)
        """
        return pulumi.get(self, "wait")

    @wait.setter
    def wait(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "wait", value)


@pulumi.input_type
class _AppV2State:
    def __init__(__self__, *,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 chart_name: Optional[pulumi.Input[str]] = None,
                 chart_version: Optional[pulumi.Input[str]] = None,
                 cleanup_on_fail: Optional[pulumi.Input[bool]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 disable_hooks: Optional[pulumi.Input[bool]] = None,
                 disable_open_api_validation: Optional[pulumi.Input[bool]] = None,
                 force_upgrade: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 repo_name: Optional[pulumi.Input[str]] = None,
                 system_default_registry: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[str]] = None,
                 wait: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering AppV2 resources.
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for the app v2 (map)
        :param pulumi.Input[str] chart_name: The app v2 chart name (string)
        :param pulumi.Input[str] chart_version: The app v2 chart version (string)
        :param pulumi.Input[bool] cleanup_on_fail: Cleanup app v2 on failed chart upgrade. Default: `false` (bool)
        :param pulumi.Input[str] cluster_id: The cluster id of the app (string)
        :param pulumi.Input[str] cluster_name: (Computed) The cluster name of the app (string)
        :param pulumi.Input[bool] disable_hooks: Disable app v2 chart hooks. Default: `false` (bool)
        :param pulumi.Input[bool] disable_open_api_validation: Disable app V2 Open API Validation. Default: `false` (bool)
        :param pulumi.Input[bool] force_upgrade: Force app V2 chart upgrade. Default: `false` (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for the app v2 (map)
        :param pulumi.Input[str] name: The name of the app v2 (string)
        :param pulumi.Input[str] namespace: The namespace of the app v2 (string)
        :param pulumi.Input[str] project_id: Deploy the app v2 within project ID (string)
        :param pulumi.Input[str] repo_name: Repo name (string)
        :param pulumi.Input[str] system_default_registry: (Computed) The system default registry of the app (string)
        :param pulumi.Input[str] values: The app v2 values yaml. Yaml format is required (string)
        :param pulumi.Input[bool] wait: Wait until app is deployed. Default: `true` (bool)
        """
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if chart_name is not None:
            pulumi.set(__self__, "chart_name", chart_name)
        if chart_version is not None:
            pulumi.set(__self__, "chart_version", chart_version)
        if cleanup_on_fail is not None:
            pulumi.set(__self__, "cleanup_on_fail", cleanup_on_fail)
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if cluster_name is not None:
            pulumi.set(__self__, "cluster_name", cluster_name)
        if disable_hooks is not None:
            pulumi.set(__self__, "disable_hooks", disable_hooks)
        if disable_open_api_validation is not None:
            pulumi.set(__self__, "disable_open_api_validation", disable_open_api_validation)
        if force_upgrade is not None:
            pulumi.set(__self__, "force_upgrade", force_upgrade)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace is not None:
            pulumi.set(__self__, "namespace", namespace)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if repo_name is not None:
            pulumi.set(__self__, "repo_name", repo_name)
        if system_default_registry is not None:
            pulumi.set(__self__, "system_default_registry", system_default_registry)
        if values is not None:
            pulumi.set(__self__, "values", values)
        if wait is not None:
            pulumi.set(__self__, "wait", wait)

    @property
    @pulumi.getter
    def annotations(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Annotations for the app v2 (map)
        """
        return pulumi.get(self, "annotations")

    @annotations.setter
    def annotations(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "annotations", value)

    @property
    @pulumi.getter(name="chartName")
    def chart_name(self) -> Optional[pulumi.Input[str]]:
        """
        The app v2 chart name (string)
        """
        return pulumi.get(self, "chart_name")

    @chart_name.setter
    def chart_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "chart_name", value)

    @property
    @pulumi.getter(name="chartVersion")
    def chart_version(self) -> Optional[pulumi.Input[str]]:
        """
        The app v2 chart version (string)
        """
        return pulumi.get(self, "chart_version")

    @chart_version.setter
    def chart_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "chart_version", value)

    @property
    @pulumi.getter(name="cleanupOnFail")
    def cleanup_on_fail(self) -> Optional[pulumi.Input[bool]]:
        """
        Cleanup app v2 on failed chart upgrade. Default: `false` (bool)
        """
        return pulumi.get(self, "cleanup_on_fail")

    @cleanup_on_fail.setter
    def cleanup_on_fail(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "cleanup_on_fail", value)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The cluster id of the app (string)
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) The cluster name of the app (string)
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="disableHooks")
    def disable_hooks(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable app v2 chart hooks. Default: `false` (bool)
        """
        return pulumi.get(self, "disable_hooks")

    @disable_hooks.setter
    def disable_hooks(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_hooks", value)

    @property
    @pulumi.getter(name="disableOpenApiValidation")
    def disable_open_api_validation(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable app V2 Open API Validation. Default: `false` (bool)
        """
        return pulumi.get(self, "disable_open_api_validation")

    @disable_open_api_validation.setter
    def disable_open_api_validation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_open_api_validation", value)

    @property
    @pulumi.getter(name="forceUpgrade")
    def force_upgrade(self) -> Optional[pulumi.Input[bool]]:
        """
        Force app V2 chart upgrade. Default: `false` (bool)
        """
        return pulumi.get(self, "force_upgrade")

    @force_upgrade.setter
    def force_upgrade(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_upgrade", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Labels for the app v2 (map)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the app v2 (string)
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The namespace of the app v2 (string)
        """
        return pulumi.get(self, "namespace")

    @namespace.setter
    def namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        Deploy the app v2 within project ID (string)
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> Optional[pulumi.Input[str]]:
        """
        Repo name (string)
        """
        return pulumi.get(self, "repo_name")

    @repo_name.setter
    def repo_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_name", value)

    @property
    @pulumi.getter(name="systemDefaultRegistry")
    def system_default_registry(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) The system default registry of the app (string)
        """
        return pulumi.get(self, "system_default_registry")

    @system_default_registry.setter
    def system_default_registry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "system_default_registry", value)

    @property
    @pulumi.getter
    def values(self) -> Optional[pulumi.Input[str]]:
        """
        The app v2 values yaml. Yaml format is required (string)
        """
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "values", value)

    @property
    @pulumi.getter
    def wait(self) -> Optional[pulumi.Input[bool]]:
        """
        Wait until app is deployed. Default: `true` (bool)
        """
        return pulumi.get(self, "wait")

    @wait.setter
    def wait(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "wait", value)


class AppV2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 chart_name: Optional[pulumi.Input[str]] = None,
                 chart_version: Optional[pulumi.Input[str]] = None,
                 cleanup_on_fail: Optional[pulumi.Input[bool]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 disable_hooks: Optional[pulumi.Input[bool]] = None,
                 disable_open_api_validation: Optional[pulumi.Input[bool]] = None,
                 force_upgrade: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 repo_name: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[str]] = None,
                 wait: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Rancher App v2 resource. This can be used to manage helm charts for Rancher v2 environments and retrieve their information. App v2 resource is available at Rancher v2.5.x and above.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_rancher2 as rancher2

        # Create a new Rancher2 App V2 using
        foo = rancher2.AppV2("foo",
            cluster_id="<CLUSTER_ID>",
            namespace="cattle-monitoring-system",
            repo_name="rancher-charts",
            chart_name="rancher-monitoring",
            chart_version="9.4.200",
            values=(lambda path: open(path).read())("values.yaml"))
        ```

        ## Import

        V2 apps can be imported using the Rancher cluster ID and App V2 name.

        ```sh
         $ pulumi import rancher2:index/appV2:AppV2 foo &lt;CLUSTER_ID&gt;.&lt;APP_V2_NAME&gt;
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for the app v2 (map)
        :param pulumi.Input[str] chart_name: The app v2 chart name (string)
        :param pulumi.Input[str] chart_version: The app v2 chart version (string)
        :param pulumi.Input[bool] cleanup_on_fail: Cleanup app v2 on failed chart upgrade. Default: `false` (bool)
        :param pulumi.Input[str] cluster_id: The cluster id of the app (string)
        :param pulumi.Input[bool] disable_hooks: Disable app v2 chart hooks. Default: `false` (bool)
        :param pulumi.Input[bool] disable_open_api_validation: Disable app V2 Open API Validation. Default: `false` (bool)
        :param pulumi.Input[bool] force_upgrade: Force app V2 chart upgrade. Default: `false` (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for the app v2 (map)
        :param pulumi.Input[str] name: The name of the app v2 (string)
        :param pulumi.Input[str] namespace: The namespace of the app v2 (string)
        :param pulumi.Input[str] project_id: Deploy the app v2 within project ID (string)
        :param pulumi.Input[str] repo_name: Repo name (string)
        :param pulumi.Input[str] values: The app v2 values yaml. Yaml format is required (string)
        :param pulumi.Input[bool] wait: Wait until app is deployed. Default: `true` (bool)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AppV2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Rancher App v2 resource. This can be used to manage helm charts for Rancher v2 environments and retrieve their information. App v2 resource is available at Rancher v2.5.x and above.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_rancher2 as rancher2

        # Create a new Rancher2 App V2 using
        foo = rancher2.AppV2("foo",
            cluster_id="<CLUSTER_ID>",
            namespace="cattle-monitoring-system",
            repo_name="rancher-charts",
            chart_name="rancher-monitoring",
            chart_version="9.4.200",
            values=(lambda path: open(path).read())("values.yaml"))
        ```

        ## Import

        V2 apps can be imported using the Rancher cluster ID and App V2 name.

        ```sh
         $ pulumi import rancher2:index/appV2:AppV2 foo &lt;CLUSTER_ID&gt;.&lt;APP_V2_NAME&gt;
        ```

        :param str resource_name: The name of the resource.
        :param AppV2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AppV2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 chart_name: Optional[pulumi.Input[str]] = None,
                 chart_version: Optional[pulumi.Input[str]] = None,
                 cleanup_on_fail: Optional[pulumi.Input[bool]] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 disable_hooks: Optional[pulumi.Input[bool]] = None,
                 disable_open_api_validation: Optional[pulumi.Input[bool]] = None,
                 force_upgrade: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 repo_name: Optional[pulumi.Input[str]] = None,
                 values: Optional[pulumi.Input[str]] = None,
                 wait: Optional[pulumi.Input[bool]] = None,
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
            __props__ = AppV2Args.__new__(AppV2Args)

            __props__.__dict__["annotations"] = annotations
            if chart_name is None and not opts.urn:
                raise TypeError("Missing required property 'chart_name'")
            __props__.__dict__["chart_name"] = chart_name
            __props__.__dict__["chart_version"] = chart_version
            __props__.__dict__["cleanup_on_fail"] = cleanup_on_fail
            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            __props__.__dict__["disable_hooks"] = disable_hooks
            __props__.__dict__["disable_open_api_validation"] = disable_open_api_validation
            __props__.__dict__["force_upgrade"] = force_upgrade
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            if namespace is None and not opts.urn:
                raise TypeError("Missing required property 'namespace'")
            __props__.__dict__["namespace"] = namespace
            __props__.__dict__["project_id"] = project_id
            if repo_name is None and not opts.urn:
                raise TypeError("Missing required property 'repo_name'")
            __props__.__dict__["repo_name"] = repo_name
            __props__.__dict__["values"] = values
            __props__.__dict__["wait"] = wait
            __props__.__dict__["cluster_name"] = None
            __props__.__dict__["system_default_registry"] = None
        super(AppV2, __self__).__init__(
            'rancher2:index/appV2:AppV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            annotations: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            chart_name: Optional[pulumi.Input[str]] = None,
            chart_version: Optional[pulumi.Input[str]] = None,
            cleanup_on_fail: Optional[pulumi.Input[bool]] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            disable_hooks: Optional[pulumi.Input[bool]] = None,
            disable_open_api_validation: Optional[pulumi.Input[bool]] = None,
            force_upgrade: Optional[pulumi.Input[bool]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            repo_name: Optional[pulumi.Input[str]] = None,
            system_default_registry: Optional[pulumi.Input[str]] = None,
            values: Optional[pulumi.Input[str]] = None,
            wait: Optional[pulumi.Input[bool]] = None) -> 'AppV2':
        """
        Get an existing AppV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] annotations: Annotations for the app v2 (map)
        :param pulumi.Input[str] chart_name: The app v2 chart name (string)
        :param pulumi.Input[str] chart_version: The app v2 chart version (string)
        :param pulumi.Input[bool] cleanup_on_fail: Cleanup app v2 on failed chart upgrade. Default: `false` (bool)
        :param pulumi.Input[str] cluster_id: The cluster id of the app (string)
        :param pulumi.Input[str] cluster_name: (Computed) The cluster name of the app (string)
        :param pulumi.Input[bool] disable_hooks: Disable app v2 chart hooks. Default: `false` (bool)
        :param pulumi.Input[bool] disable_open_api_validation: Disable app V2 Open API Validation. Default: `false` (bool)
        :param pulumi.Input[bool] force_upgrade: Force app V2 chart upgrade. Default: `false` (bool)
        :param pulumi.Input[Mapping[str, Any]] labels: Labels for the app v2 (map)
        :param pulumi.Input[str] name: The name of the app v2 (string)
        :param pulumi.Input[str] namespace: The namespace of the app v2 (string)
        :param pulumi.Input[str] project_id: Deploy the app v2 within project ID (string)
        :param pulumi.Input[str] repo_name: Repo name (string)
        :param pulumi.Input[str] system_default_registry: (Computed) The system default registry of the app (string)
        :param pulumi.Input[str] values: The app v2 values yaml. Yaml format is required (string)
        :param pulumi.Input[bool] wait: Wait until app is deployed. Default: `true` (bool)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AppV2State.__new__(_AppV2State)

        __props__.__dict__["annotations"] = annotations
        __props__.__dict__["chart_name"] = chart_name
        __props__.__dict__["chart_version"] = chart_version
        __props__.__dict__["cleanup_on_fail"] = cleanup_on_fail
        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["cluster_name"] = cluster_name
        __props__.__dict__["disable_hooks"] = disable_hooks
        __props__.__dict__["disable_open_api_validation"] = disable_open_api_validation
        __props__.__dict__["force_upgrade"] = force_upgrade
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace"] = namespace
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["repo_name"] = repo_name
        __props__.__dict__["system_default_registry"] = system_default_registry
        __props__.__dict__["values"] = values
        __props__.__dict__["wait"] = wait
        return AppV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def annotations(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Annotations for the app v2 (map)
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter(name="chartName")
    def chart_name(self) -> pulumi.Output[str]:
        """
        The app v2 chart name (string)
        """
        return pulumi.get(self, "chart_name")

    @property
    @pulumi.getter(name="chartVersion")
    def chart_version(self) -> pulumi.Output[str]:
        """
        The app v2 chart version (string)
        """
        return pulumi.get(self, "chart_version")

    @property
    @pulumi.getter(name="cleanupOnFail")
    def cleanup_on_fail(self) -> pulumi.Output[Optional[bool]]:
        """
        Cleanup app v2 on failed chart upgrade. Default: `false` (bool)
        """
        return pulumi.get(self, "cleanup_on_fail")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The cluster id of the app (string)
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        """
        (Computed) The cluster name of the app (string)
        """
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="disableHooks")
    def disable_hooks(self) -> pulumi.Output[Optional[bool]]:
        """
        Disable app v2 chart hooks. Default: `false` (bool)
        """
        return pulumi.get(self, "disable_hooks")

    @property
    @pulumi.getter(name="disableOpenApiValidation")
    def disable_open_api_validation(self) -> pulumi.Output[Optional[bool]]:
        """
        Disable app V2 Open API Validation. Default: `false` (bool)
        """
        return pulumi.get(self, "disable_open_api_validation")

    @property
    @pulumi.getter(name="forceUpgrade")
    def force_upgrade(self) -> pulumi.Output[Optional[bool]]:
        """
        Force app V2 chart upgrade. Default: `false` (bool)
        """
        return pulumi.get(self, "force_upgrade")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        Labels for the app v2 (map)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the app v2 (string)
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> pulumi.Output[str]:
        """
        The namespace of the app v2 (string)
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[Optional[str]]:
        """
        Deploy the app v2 within project ID (string)
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="repoName")
    def repo_name(self) -> pulumi.Output[str]:
        """
        Repo name (string)
        """
        return pulumi.get(self, "repo_name")

    @property
    @pulumi.getter(name="systemDefaultRegistry")
    def system_default_registry(self) -> pulumi.Output[str]:
        """
        (Computed) The system default registry of the app (string)
        """
        return pulumi.get(self, "system_default_registry")

    @property
    @pulumi.getter
    def values(self) -> pulumi.Output[Optional[str]]:
        """
        The app v2 values yaml. Yaml format is required (string)
        """
        return pulumi.get(self, "values")

    @property
    @pulumi.getter
    def wait(self) -> pulumi.Output[Optional[bool]]:
        """
        Wait until app is deployed. Default: `true` (bool)
        """
        return pulumi.get(self, "wait")

