# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'apikey',
    'enable_ddi',
    'endpoint',
    'ignore_ssl',
    'rate_limit_parallelism',
]

__config__ = pulumi.Config('ns1')

apikey = __config__.get('apikey')
"""
The ns1 API key, this is required
"""

enable_ddi = __config__.get('enableDdi')

endpoint = __config__.get('endpoint')

ignore_ssl = __config__.get('ignoreSsl')

rate_limit_parallelism = __config__.get('rateLimitParallelism')

