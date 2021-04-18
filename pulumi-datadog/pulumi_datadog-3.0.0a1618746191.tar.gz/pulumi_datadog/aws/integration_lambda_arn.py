# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IntegrationLambdaArnArgs', 'IntegrationLambdaArn']

@pulumi.input_type
class IntegrationLambdaArnArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 lambda_arn: pulumi.Input[str]):
        """
        The set of arguments for constructing a IntegrationLambdaArn resource.
        :param pulumi.Input[str] account_id: Your AWS Account ID without dashes.
        :param pulumi.Input[str] lambda_arn: The ARN of the Datadog forwarder Lambda.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "lambda_arn", lambda_arn)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        Your AWS Account ID without dashes.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the Datadog forwarder Lambda.
        """
        return pulumi.get(self, "lambda_arn")

    @lambda_arn.setter
    def lambda_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "lambda_arn", value)


@pulumi.input_type
class _IntegrationLambdaArnState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 lambda_arn: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering IntegrationLambdaArn resources.
        :param pulumi.Input[str] account_id: Your AWS Account ID without dashes.
        :param pulumi.Input[str] lambda_arn: The ARN of the Datadog forwarder Lambda.
        """
        if account_id is not None:
            pulumi.set(__self__, "account_id", account_id)
        if lambda_arn is not None:
            pulumi.set(__self__, "lambda_arn", lambda_arn)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        Your AWS Account ID without dashes.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the Datadog forwarder Lambda.
        """
        return pulumi.get(self, "lambda_arn")

    @lambda_arn.setter
    def lambda_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "lambda_arn", value)


class IntegrationLambdaArn(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 lambda_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Datadog - Amazon Web Services integration Lambda ARN resource. This can be used to create and manage the log collection Lambdas for an account.

        Update operations are currently not supported with datadog API so any change forces a new resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datadog as datadog

        main_collector = datadog.aws.IntegrationLambdaArn("mainCollector",
            account_id="1234567890",
            lambda_arn="arn:aws:lambda:us-east-1:1234567890:function:datadog-forwarder-Forwarder")
        ```

        ## Import

        Amazon Web Services Lambda ARN integrations can be imported using their `account_id` and `lambda_arn` separated with a space (` `).

        ```sh
         $ pulumi import datadog:aws/integrationLambdaArn:IntegrationLambdaArn test "1234567890 arn:aws:lambda:us-east-1:1234567890:function:datadog-forwarder-Forwarder"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Your AWS Account ID without dashes.
        :param pulumi.Input[str] lambda_arn: The ARN of the Datadog forwarder Lambda.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationLambdaArnArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Datadog - Amazon Web Services integration Lambda ARN resource. This can be used to create and manage the log collection Lambdas for an account.

        Update operations are currently not supported with datadog API so any change forces a new resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_datadog as datadog

        main_collector = datadog.aws.IntegrationLambdaArn("mainCollector",
            account_id="1234567890",
            lambda_arn="arn:aws:lambda:us-east-1:1234567890:function:datadog-forwarder-Forwarder")
        ```

        ## Import

        Amazon Web Services Lambda ARN integrations can be imported using their `account_id` and `lambda_arn` separated with a space (` `).

        ```sh
         $ pulumi import datadog:aws/integrationLambdaArn:IntegrationLambdaArn test "1234567890 arn:aws:lambda:us-east-1:1234567890:function:datadog-forwarder-Forwarder"
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationLambdaArnArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationLambdaArnArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 lambda_arn: Optional[pulumi.Input[str]] = None,
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
            __props__ = IntegrationLambdaArnArgs.__new__(IntegrationLambdaArnArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            if lambda_arn is None and not opts.urn:
                raise TypeError("Missing required property 'lambda_arn'")
            __props__.__dict__["lambda_arn"] = lambda_arn
        super(IntegrationLambdaArn, __self__).__init__(
            'datadog:aws/integrationLambdaArn:IntegrationLambdaArn',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            lambda_arn: Optional[pulumi.Input[str]] = None) -> 'IntegrationLambdaArn':
        """
        Get an existing IntegrationLambdaArn resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: Your AWS Account ID without dashes.
        :param pulumi.Input[str] lambda_arn: The ARN of the Datadog forwarder Lambda.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationLambdaArnState.__new__(_IntegrationLambdaArnState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["lambda_arn"] = lambda_arn
        return IntegrationLambdaArn(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        Your AWS Account ID without dashes.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="lambdaArn")
    def lambda_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Datadog forwarder Lambda.
        """
        return pulumi.get(self, "lambda_arn")

