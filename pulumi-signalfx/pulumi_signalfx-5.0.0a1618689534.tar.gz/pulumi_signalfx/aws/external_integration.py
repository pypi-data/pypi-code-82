# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ExternalIntegrationArgs', 'ExternalIntegration']

@pulumi.input_type
class ExternalIntegrationArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ExternalIntegration resource.
        :param pulumi.Input[str] name: The name of this integration
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of this integration
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ExternalIntegrationState:
    def __init__(__self__, *,
                 external_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 signalfx_aws_account: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ExternalIntegration resources.
        :param pulumi.Input[str] external_id: The external ID to use with your IAM role and with `aws.Integration`.
        :param pulumi.Input[str] name: The name of this integration
        :param pulumi.Input[str] signalfx_aws_account: The AWS Account ARN to use with your policies/roles, provided by SignalFx.
        """
        if external_id is not None:
            pulumi.set(__self__, "external_id", external_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if signalfx_aws_account is not None:
            pulumi.set(__self__, "signalfx_aws_account", signalfx_aws_account)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> Optional[pulumi.Input[str]]:
        """
        The external ID to use with your IAM role and with `aws.Integration`.
        """
        return pulumi.get(self, "external_id")

    @external_id.setter
    def external_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "external_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of this integration
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="signalfxAwsAccount")
    def signalfx_aws_account(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS Account ARN to use with your policies/roles, provided by SignalFx.
        """
        return pulumi.get(self, "signalfx_aws_account")

    @signalfx_aws_account.setter
    def signalfx_aws_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signalfx_aws_account", value)


class ExternalIntegration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        SignalFx AWS CloudWatch integrations using Role ARNs. For help with this integration see [Connect to AWS CloudWatch](https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#connect-to-aws).

        > **NOTE** When managing integrations you'll need to use an admin token to authenticate the SignalFx provider.

        > **WARNING** This resource implements a part of a workflow. You must use it with `aws.Integration`. Check with SignalFx support for your realm's AWS account id.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_signalfx as signalfx

        aws_myteam_extern = signalfx.aws.ExternalIntegration("awsMyteamExtern")
        signalfx_assume_policy = pulumi.Output.all(aws_myteam_extern.signalfx_aws_account, aws_myteam_extern.external_id).apply(lambda signalfx_aws_account, external_id: aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["sts:AssumeRole"],
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                type="AWS",
                identifiers=[signalfx_aws_account],
            )],
            conditions=[aws.iam.GetPolicyDocumentStatementConditionArgs(
                test="StringEquals",
                variable="sts:ExternalId",
                values=[external_id],
            )],
        )]))
        aws_sfx_role = aws.iam.Role("awsSfxRole",
            description="signalfx integration to read out data and send it to signalfxs aws account",
            assume_role_policy=signalfx_assume_policy.json)
        aws_read_permissions = aws.iam.Policy("awsReadPermissions",
            description="farts",
            policy=\"\"\"{
        	"Version": "2012-10-17",
        	"Statement": [
        		{
        			"Action": [
        				"dynamodb:ListTables",
        		    "dynamodb:DescribeTable",
        		    "dynamodb:ListTagsOfResource",
        		    "ec2:DescribeInstances",
        		    "ec2:DescribeInstanceStatus",
        		    "ec2:DescribeVolumes",
        		    "ec2:DescribeReservedInstances",
        		    "ec2:DescribeReservedInstancesModifications",
        		    "ec2:DescribeTags",
        		    "organizations:DescribeOrganization",
        		    "cloudwatch:ListMetrics",
        		    "cloudwatch:GetMetricData",
        		    "cloudwatch:GetMetricStatistics",
        		    "cloudwatch:DescribeAlarms",
        		    "sqs:ListQueues",
        		    "sqs:GetQueueAttributes",
        		    "sqs:ListQueueTags",
        		    "elasticmapreduce:ListClusters",
        		    "elasticmapreduce:DescribeCluster",
        		    "kinesis:ListShards",
        		    "kinesis:ListStreams",
        		    "kinesis:DescribeStream",
        		    "kinesis:ListTagsForStream",
        		    "rds:DescribeDBInstances",
        		    "rds:ListTagsForResource",
        		    "elasticloadbalancing:DescribeLoadBalancers",
        		    "elasticloadbalancing:DescribeTags",
        		    "elasticache:describeCacheClusters",
        		    "redshift:DescribeClusters",
        		    "lambda:GetAlias",
        		    "lambda:ListFunctions",
        		    "lambda:ListTags",
        		    "autoscaling:DescribeAutoScalingGroups",
        		    "s3:ListAllMyBuckets",
        		    "s3:ListBucket",
        		    "s3:GetBucketLocation",
        		    "s3:GetBucketTagging",
        		    "ecs:ListServices",
        		    "ecs:ListTasks",
        		    "ecs:DescribeTasks",
        		    "ecs:DescribeServices",
        		    "ecs:ListClusters",
        		    "ecs:DescribeClusters",
        		    "ecs:ListTaskDefinitions",
        		    "ecs:ListTagsForResource",
        		    "apigateway:GET",
        		    "cloudfront:ListDistributions",
        		    "cloudfront:ListTagsForResource",
        		    "tag:GetResources",
        		    "es:ListDomainNames",
        		    "es:DescribeElasticsearchDomain"
        			],
        			"Effect": "Allow",
        			"Resource": "*"
        		}
        	]
        }
        \"\"\")
        sfx_read_attach = aws.iam.RolePolicyAttachment("sfx-read-attach",
            role=aws_sfx_role.name,
            policy_arn=aws_read_permissions.arn)
        aws_myteam = signalfx.aws.Integration("awsMyteam",
            enabled=True,
            integration_id=aws_myteam_extern.id,
            external_id=aws_myteam_extern.external_id,
            role_arn=aws_sfx_role.arn,
            regions=["us-east-1"],
            poll_rate=300,
            import_cloud_watch=True,
            enable_aws_usage=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of this integration
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ExternalIntegrationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        SignalFx AWS CloudWatch integrations using Role ARNs. For help with this integration see [Connect to AWS CloudWatch](https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#connect-to-aws).

        > **NOTE** When managing integrations you'll need to use an admin token to authenticate the SignalFx provider.

        > **WARNING** This resource implements a part of a workflow. You must use it with `aws.Integration`. Check with SignalFx support for your realm's AWS account id.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_signalfx as signalfx

        aws_myteam_extern = signalfx.aws.ExternalIntegration("awsMyteamExtern")
        signalfx_assume_policy = pulumi.Output.all(aws_myteam_extern.signalfx_aws_account, aws_myteam_extern.external_id).apply(lambda signalfx_aws_account, external_id: aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            actions=["sts:AssumeRole"],
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                type="AWS",
                identifiers=[signalfx_aws_account],
            )],
            conditions=[aws.iam.GetPolicyDocumentStatementConditionArgs(
                test="StringEquals",
                variable="sts:ExternalId",
                values=[external_id],
            )],
        )]))
        aws_sfx_role = aws.iam.Role("awsSfxRole",
            description="signalfx integration to read out data and send it to signalfxs aws account",
            assume_role_policy=signalfx_assume_policy.json)
        aws_read_permissions = aws.iam.Policy("awsReadPermissions",
            description="farts",
            policy=\"\"\"{
        	"Version": "2012-10-17",
        	"Statement": [
        		{
        			"Action": [
        				"dynamodb:ListTables",
        		    "dynamodb:DescribeTable",
        		    "dynamodb:ListTagsOfResource",
        		    "ec2:DescribeInstances",
        		    "ec2:DescribeInstanceStatus",
        		    "ec2:DescribeVolumes",
        		    "ec2:DescribeReservedInstances",
        		    "ec2:DescribeReservedInstancesModifications",
        		    "ec2:DescribeTags",
        		    "organizations:DescribeOrganization",
        		    "cloudwatch:ListMetrics",
        		    "cloudwatch:GetMetricData",
        		    "cloudwatch:GetMetricStatistics",
        		    "cloudwatch:DescribeAlarms",
        		    "sqs:ListQueues",
        		    "sqs:GetQueueAttributes",
        		    "sqs:ListQueueTags",
        		    "elasticmapreduce:ListClusters",
        		    "elasticmapreduce:DescribeCluster",
        		    "kinesis:ListShards",
        		    "kinesis:ListStreams",
        		    "kinesis:DescribeStream",
        		    "kinesis:ListTagsForStream",
        		    "rds:DescribeDBInstances",
        		    "rds:ListTagsForResource",
        		    "elasticloadbalancing:DescribeLoadBalancers",
        		    "elasticloadbalancing:DescribeTags",
        		    "elasticache:describeCacheClusters",
        		    "redshift:DescribeClusters",
        		    "lambda:GetAlias",
        		    "lambda:ListFunctions",
        		    "lambda:ListTags",
        		    "autoscaling:DescribeAutoScalingGroups",
        		    "s3:ListAllMyBuckets",
        		    "s3:ListBucket",
        		    "s3:GetBucketLocation",
        		    "s3:GetBucketTagging",
        		    "ecs:ListServices",
        		    "ecs:ListTasks",
        		    "ecs:DescribeTasks",
        		    "ecs:DescribeServices",
        		    "ecs:ListClusters",
        		    "ecs:DescribeClusters",
        		    "ecs:ListTaskDefinitions",
        		    "ecs:ListTagsForResource",
        		    "apigateway:GET",
        		    "cloudfront:ListDistributions",
        		    "cloudfront:ListTagsForResource",
        		    "tag:GetResources",
        		    "es:ListDomainNames",
        		    "es:DescribeElasticsearchDomain"
        			],
        			"Effect": "Allow",
        			"Resource": "*"
        		}
        	]
        }
        \"\"\")
        sfx_read_attach = aws.iam.RolePolicyAttachment("sfx-read-attach",
            role=aws_sfx_role.name,
            policy_arn=aws_read_permissions.arn)
        aws_myteam = signalfx.aws.Integration("awsMyteam",
            enabled=True,
            integration_id=aws_myteam_extern.id,
            external_id=aws_myteam_extern.external_id,
            role_arn=aws_sfx_role.arn,
            regions=["us-east-1"],
            poll_rate=300,
            import_cloud_watch=True,
            enable_aws_usage=True)
        ```

        :param str resource_name: The name of the resource.
        :param ExternalIntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ExternalIntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
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
            __props__ = ExternalIntegrationArgs.__new__(ExternalIntegrationArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["external_id"] = None
            __props__.__dict__["signalfx_aws_account"] = None
        super(ExternalIntegration, __self__).__init__(
            'signalfx:aws/externalIntegration:ExternalIntegration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            external_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            signalfx_aws_account: Optional[pulumi.Input[str]] = None) -> 'ExternalIntegration':
        """
        Get an existing ExternalIntegration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] external_id: The external ID to use with your IAM role and with `aws.Integration`.
        :param pulumi.Input[str] name: The name of this integration
        :param pulumi.Input[str] signalfx_aws_account: The AWS Account ARN to use with your policies/roles, provided by SignalFx.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ExternalIntegrationState.__new__(_ExternalIntegrationState)

        __props__.__dict__["external_id"] = external_id
        __props__.__dict__["name"] = name
        __props__.__dict__["signalfx_aws_account"] = signalfx_aws_account
        return ExternalIntegration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="externalId")
    def external_id(self) -> pulumi.Output[str]:
        """
        The external ID to use with your IAM role and with `aws.Integration`.
        """
        return pulumi.get(self, "external_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of this integration
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="signalfxAwsAccount")
    def signalfx_aws_account(self) -> pulumi.Output[str]:
        """
        The AWS Account ARN to use with your policies/roles, provided by SignalFx.
        """
        return pulumi.get(self, "signalfx_aws_account")

