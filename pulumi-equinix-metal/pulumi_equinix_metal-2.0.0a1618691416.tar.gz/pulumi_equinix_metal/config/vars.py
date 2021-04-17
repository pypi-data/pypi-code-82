# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'auth_token',
    'max_retries',
    'max_retry_wait_seconds',
]

__config__ = pulumi.Config('equinix-metal')

auth_token = __config__.get('authToken')
"""
The API auth key for API operations.
"""

max_retries = __config__.get('maxRetries')

max_retry_wait_seconds = __config__.get('maxRetryWaitSeconds')

