# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'api_endpoint',
    'spaces_access_id',
    'spaces_endpoint',
    'spaces_secret_key',
    'token',
]

__config__ = pulumi.Config('digitalocean')

api_endpoint = __config__.get('apiEndpoint') or (_utilities.get_env('DIGITALOCEAN_API_URL') or 'https://api.digitalocean.com')
"""
The URL to use for the DigitalOcean API.
"""

spaces_access_id = __config__.get('spacesAccessId')
"""
The access key ID for Spaces API operations.
"""

spaces_endpoint = __config__.get('spacesEndpoint') or _utilities.get_env('SPACES_ENDPOINT_URL')
"""
The URL to use for the DigitalOcean Spaces API.
"""

spaces_secret_key = __config__.get('spacesSecretKey')
"""
The secret access key for Spaces API operations.
"""

token = __config__.get('token')
"""
The token key for API operations.
"""

