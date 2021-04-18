# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'allow_reauth',
    'application_credential_id',
    'application_credential_name',
    'application_credential_secret',
    'auth_url',
    'cacert_file',
    'cert',
    'cloud',
    'default_domain',
    'delayed_auth',
    'disable_no_cache_header',
    'domain_id',
    'domain_name',
    'endpoint_overrides',
    'endpoint_type',
    'insecure',
    'key',
    'max_retries',
    'password',
    'project_domain_id',
    'project_domain_name',
    'region',
    'swauth',
    'tenant_id',
    'tenant_name',
    'token',
    'use_octavia',
    'user_domain_id',
    'user_domain_name',
    'user_id',
    'user_name',
]

__config__ = pulumi.Config('openstack')

allow_reauth = __config__.get('allowReauth') or _utilities.get_env_bool('OS_ALLOW_REAUTH')
"""
If set to `false`, OpenStack authorization won't be perfomed automatically, if the initial auth token get expired.
Defaults to `true`
"""

application_credential_id = __config__.get('applicationCredentialId')
"""
Application Credential ID to login with.
"""

application_credential_name = __config__.get('applicationCredentialName')
"""
Application Credential name to login with.
"""

application_credential_secret = __config__.get('applicationCredentialSecret')
"""
Application Credential secret to login with.
"""

auth_url = __config__.get('authUrl')
"""
The Identity authentication URL.
"""

cacert_file = __config__.get('cacertFile')
"""
A Custom CA certificate.
"""

cert = __config__.get('cert')
"""
A client certificate to authenticate with.
"""

cloud = __config__.get('cloud') or _utilities.get_env('OS_CLOUD')
"""
An entry in a `clouds.yaml` file to use.
"""

default_domain = __config__.get('defaultDomain')
"""
The name of the Domain ID to scope to if no other domain is specified. Defaults to `default` (Identity v3).
"""

delayed_auth = __config__.get('delayedAuth') or _utilities.get_env_bool('OS_DELAYED_AUTH')
"""
If set to `false`, OpenStack authorization will be perfomed, every time the service provider client is called. Defaults
to `true`.
"""

disable_no_cache_header = __config__.get('disableNoCacheHeader')
"""
If set to `true`, the HTTP `Cache-Control: no-cache` header will not be added by default to all API requests.
"""

domain_id = __config__.get('domainId')
"""
The ID of the Domain to scope to (Identity v3).
"""

domain_name = __config__.get('domainName')
"""
The name of the Domain to scope to (Identity v3).
"""

endpoint_overrides = __config__.get('endpointOverrides')
"""
A map of services with an endpoint to override what was from the Keystone catalog
"""

endpoint_type = __config__.get('endpointType') or _utilities.get_env('OS_ENDPOINT_TYPE')

insecure = __config__.get('insecure') or _utilities.get_env_bool('OS_INSECURE')
"""
Trust self-signed certificates.
"""

key = __config__.get('key')
"""
A client private key to authenticate with.
"""

max_retries = __config__.get('maxRetries')
"""
How many times HTTP connection should be retried until giving up.
"""

password = __config__.get('password')
"""
Password to login with.
"""

project_domain_id = __config__.get('projectDomainId')
"""
The ID of the domain where the proejct resides (Identity v3).
"""

project_domain_name = __config__.get('projectDomainName')
"""
The name of the domain where the project resides (Identity v3).
"""

region = __config__.get('region') or _utilities.get_env('OS_REGION_NAME')
"""
The OpenStack region to connect to.
"""

swauth = __config__.get('swauth') or _utilities.get_env_bool('OS_SWAUTH')
"""
Use Swift's authentication system instead of Keystone. Only used for interaction with Swift.
"""

tenant_id = __config__.get('tenantId')
"""
The ID of the Tenant (Identity v2) or Project (Identity v3) to login with.
"""

tenant_name = __config__.get('tenantName')
"""
The name of the Tenant (Identity v2) or Project (Identity v3) to login with.
"""

token = __config__.get('token')
"""
Authentication token to use as an alternative to username/password.
"""

use_octavia = __config__.get('useOctavia') or _utilities.get_env_bool('OS_USE_OCTAVIA')
"""
If set to `true`, API requests will go the Load Balancer service (Octavia) instead of the Networking service (Neutron).
"""

user_domain_id = __config__.get('userDomainId')
"""
The ID of the domain where the user resides (Identity v3).
"""

user_domain_name = __config__.get('userDomainName')
"""
The name of the domain where the user resides (Identity v3).
"""

user_id = __config__.get('userId')
"""
Username to login with.
"""

user_name = __config__.get('userName')
"""
Username to login with.
"""

