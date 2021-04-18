# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'address',
    'ca_file',
    'ca_path',
    'ca_pem',
    'cert_file',
    'cert_pem',
    'datacenter',
    'http_auth',
    'insecure_https',
    'key_file',
    'key_pem',
    'namespace',
    'scheme',
    'token',
]

__config__ = pulumi.Config('consul')

address = __config__.get('address')

ca_file = __config__.get('caFile')

ca_path = __config__.get('caPath')

ca_pem = __config__.get('caPem')

cert_file = __config__.get('certFile')

cert_pem = __config__.get('certPem')

datacenter = __config__.get('datacenter')

http_auth = __config__.get('httpAuth')

insecure_https = __config__.get('insecureHttps')

key_file = __config__.get('keyFile')

key_pem = __config__.get('keyPem')

namespace = __config__.get('namespace')

scheme = __config__.get('scheme')

token = __config__.get('token')

