# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetClientResult',
    'AwaitableGetClientResult',
    'get_client',
]

@pulumi.output_type
class GetClientResult:
    """
    A collection of values returned by getClient.
    """
    def __init__(__self__, assertion_consumer_post_url=None, assertion_consumer_redirect_url=None, authentication_flow_binding_overrides=None, base_url=None, client_id=None, client_signature_required=None, description=None, enabled=None, encrypt_assertions=None, encryption_certificate=None, force_name_id_format=None, force_post_binding=None, front_channel_logout=None, full_scope_allowed=None, id=None, idp_initiated_sso_relay_state=None, idp_initiated_sso_url_name=None, include_authn_statement=None, logout_service_post_binding_url=None, logout_service_redirect_binding_url=None, master_saml_processing_url=None, name=None, name_id_format=None, realm_id=None, root_url=None, sign_assertions=None, sign_documents=None, signature_algorithm=None, signing_certificate=None, signing_private_key=None, valid_redirect_uris=None):
        if assertion_consumer_post_url and not isinstance(assertion_consumer_post_url, str):
            raise TypeError("Expected argument 'assertion_consumer_post_url' to be a str")
        pulumi.set(__self__, "assertion_consumer_post_url", assertion_consumer_post_url)
        if assertion_consumer_redirect_url and not isinstance(assertion_consumer_redirect_url, str):
            raise TypeError("Expected argument 'assertion_consumer_redirect_url' to be a str")
        pulumi.set(__self__, "assertion_consumer_redirect_url", assertion_consumer_redirect_url)
        if authentication_flow_binding_overrides and not isinstance(authentication_flow_binding_overrides, list):
            raise TypeError("Expected argument 'authentication_flow_binding_overrides' to be a list")
        pulumi.set(__self__, "authentication_flow_binding_overrides", authentication_flow_binding_overrides)
        if base_url and not isinstance(base_url, str):
            raise TypeError("Expected argument 'base_url' to be a str")
        pulumi.set(__self__, "base_url", base_url)
        if client_id and not isinstance(client_id, str):
            raise TypeError("Expected argument 'client_id' to be a str")
        pulumi.set(__self__, "client_id", client_id)
        if client_signature_required and not isinstance(client_signature_required, bool):
            raise TypeError("Expected argument 'client_signature_required' to be a bool")
        pulumi.set(__self__, "client_signature_required", client_signature_required)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if encrypt_assertions and not isinstance(encrypt_assertions, bool):
            raise TypeError("Expected argument 'encrypt_assertions' to be a bool")
        pulumi.set(__self__, "encrypt_assertions", encrypt_assertions)
        if encryption_certificate and not isinstance(encryption_certificate, str):
            raise TypeError("Expected argument 'encryption_certificate' to be a str")
        pulumi.set(__self__, "encryption_certificate", encryption_certificate)
        if force_name_id_format and not isinstance(force_name_id_format, bool):
            raise TypeError("Expected argument 'force_name_id_format' to be a bool")
        pulumi.set(__self__, "force_name_id_format", force_name_id_format)
        if force_post_binding and not isinstance(force_post_binding, bool):
            raise TypeError("Expected argument 'force_post_binding' to be a bool")
        pulumi.set(__self__, "force_post_binding", force_post_binding)
        if front_channel_logout and not isinstance(front_channel_logout, bool):
            raise TypeError("Expected argument 'front_channel_logout' to be a bool")
        pulumi.set(__self__, "front_channel_logout", front_channel_logout)
        if full_scope_allowed and not isinstance(full_scope_allowed, bool):
            raise TypeError("Expected argument 'full_scope_allowed' to be a bool")
        pulumi.set(__self__, "full_scope_allowed", full_scope_allowed)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if idp_initiated_sso_relay_state and not isinstance(idp_initiated_sso_relay_state, str):
            raise TypeError("Expected argument 'idp_initiated_sso_relay_state' to be a str")
        pulumi.set(__self__, "idp_initiated_sso_relay_state", idp_initiated_sso_relay_state)
        if idp_initiated_sso_url_name and not isinstance(idp_initiated_sso_url_name, str):
            raise TypeError("Expected argument 'idp_initiated_sso_url_name' to be a str")
        pulumi.set(__self__, "idp_initiated_sso_url_name", idp_initiated_sso_url_name)
        if include_authn_statement and not isinstance(include_authn_statement, bool):
            raise TypeError("Expected argument 'include_authn_statement' to be a bool")
        pulumi.set(__self__, "include_authn_statement", include_authn_statement)
        if logout_service_post_binding_url and not isinstance(logout_service_post_binding_url, str):
            raise TypeError("Expected argument 'logout_service_post_binding_url' to be a str")
        pulumi.set(__self__, "logout_service_post_binding_url", logout_service_post_binding_url)
        if logout_service_redirect_binding_url and not isinstance(logout_service_redirect_binding_url, str):
            raise TypeError("Expected argument 'logout_service_redirect_binding_url' to be a str")
        pulumi.set(__self__, "logout_service_redirect_binding_url", logout_service_redirect_binding_url)
        if master_saml_processing_url and not isinstance(master_saml_processing_url, str):
            raise TypeError("Expected argument 'master_saml_processing_url' to be a str")
        pulumi.set(__self__, "master_saml_processing_url", master_saml_processing_url)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if name_id_format and not isinstance(name_id_format, str):
            raise TypeError("Expected argument 'name_id_format' to be a str")
        pulumi.set(__self__, "name_id_format", name_id_format)
        if realm_id and not isinstance(realm_id, str):
            raise TypeError("Expected argument 'realm_id' to be a str")
        pulumi.set(__self__, "realm_id", realm_id)
        if root_url and not isinstance(root_url, str):
            raise TypeError("Expected argument 'root_url' to be a str")
        pulumi.set(__self__, "root_url", root_url)
        if sign_assertions and not isinstance(sign_assertions, bool):
            raise TypeError("Expected argument 'sign_assertions' to be a bool")
        pulumi.set(__self__, "sign_assertions", sign_assertions)
        if sign_documents and not isinstance(sign_documents, bool):
            raise TypeError("Expected argument 'sign_documents' to be a bool")
        pulumi.set(__self__, "sign_documents", sign_documents)
        if signature_algorithm and not isinstance(signature_algorithm, str):
            raise TypeError("Expected argument 'signature_algorithm' to be a str")
        pulumi.set(__self__, "signature_algorithm", signature_algorithm)
        if signing_certificate and not isinstance(signing_certificate, str):
            raise TypeError("Expected argument 'signing_certificate' to be a str")
        pulumi.set(__self__, "signing_certificate", signing_certificate)
        if signing_private_key and not isinstance(signing_private_key, str):
            raise TypeError("Expected argument 'signing_private_key' to be a str")
        pulumi.set(__self__, "signing_private_key", signing_private_key)
        if valid_redirect_uris and not isinstance(valid_redirect_uris, list):
            raise TypeError("Expected argument 'valid_redirect_uris' to be a list")
        pulumi.set(__self__, "valid_redirect_uris", valid_redirect_uris)

    @property
    @pulumi.getter(name="assertionConsumerPostUrl")
    def assertion_consumer_post_url(self) -> str:
        return pulumi.get(self, "assertion_consumer_post_url")

    @property
    @pulumi.getter(name="assertionConsumerRedirectUrl")
    def assertion_consumer_redirect_url(self) -> str:
        return pulumi.get(self, "assertion_consumer_redirect_url")

    @property
    @pulumi.getter(name="authenticationFlowBindingOverrides")
    def authentication_flow_binding_overrides(self) -> Sequence['outputs.GetClientAuthenticationFlowBindingOverrideResult']:
        return pulumi.get(self, "authentication_flow_binding_overrides")

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> str:
        return pulumi.get(self, "base_url")

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="clientSignatureRequired")
    def client_signature_required(self) -> bool:
        return pulumi.get(self, "client_signature_required")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="encryptAssertions")
    def encrypt_assertions(self) -> bool:
        return pulumi.get(self, "encrypt_assertions")

    @property
    @pulumi.getter(name="encryptionCertificate")
    def encryption_certificate(self) -> str:
        return pulumi.get(self, "encryption_certificate")

    @property
    @pulumi.getter(name="forceNameIdFormat")
    def force_name_id_format(self) -> bool:
        return pulumi.get(self, "force_name_id_format")

    @property
    @pulumi.getter(name="forcePostBinding")
    def force_post_binding(self) -> bool:
        return pulumi.get(self, "force_post_binding")

    @property
    @pulumi.getter(name="frontChannelLogout")
    def front_channel_logout(self) -> bool:
        return pulumi.get(self, "front_channel_logout")

    @property
    @pulumi.getter(name="fullScopeAllowed")
    def full_scope_allowed(self) -> bool:
        return pulumi.get(self, "full_scope_allowed")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="idpInitiatedSsoRelayState")
    def idp_initiated_sso_relay_state(self) -> str:
        return pulumi.get(self, "idp_initiated_sso_relay_state")

    @property
    @pulumi.getter(name="idpInitiatedSsoUrlName")
    def idp_initiated_sso_url_name(self) -> str:
        return pulumi.get(self, "idp_initiated_sso_url_name")

    @property
    @pulumi.getter(name="includeAuthnStatement")
    def include_authn_statement(self) -> bool:
        return pulumi.get(self, "include_authn_statement")

    @property
    @pulumi.getter(name="logoutServicePostBindingUrl")
    def logout_service_post_binding_url(self) -> str:
        return pulumi.get(self, "logout_service_post_binding_url")

    @property
    @pulumi.getter(name="logoutServiceRedirectBindingUrl")
    def logout_service_redirect_binding_url(self) -> str:
        return pulumi.get(self, "logout_service_redirect_binding_url")

    @property
    @pulumi.getter(name="masterSamlProcessingUrl")
    def master_saml_processing_url(self) -> str:
        return pulumi.get(self, "master_saml_processing_url")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameIdFormat")
    def name_id_format(self) -> str:
        return pulumi.get(self, "name_id_format")

    @property
    @pulumi.getter(name="realmId")
    def realm_id(self) -> str:
        return pulumi.get(self, "realm_id")

    @property
    @pulumi.getter(name="rootUrl")
    def root_url(self) -> str:
        return pulumi.get(self, "root_url")

    @property
    @pulumi.getter(name="signAssertions")
    def sign_assertions(self) -> bool:
        return pulumi.get(self, "sign_assertions")

    @property
    @pulumi.getter(name="signDocuments")
    def sign_documents(self) -> bool:
        return pulumi.get(self, "sign_documents")

    @property
    @pulumi.getter(name="signatureAlgorithm")
    def signature_algorithm(self) -> str:
        return pulumi.get(self, "signature_algorithm")

    @property
    @pulumi.getter(name="signingCertificate")
    def signing_certificate(self) -> str:
        return pulumi.get(self, "signing_certificate")

    @property
    @pulumi.getter(name="signingPrivateKey")
    def signing_private_key(self) -> str:
        return pulumi.get(self, "signing_private_key")

    @property
    @pulumi.getter(name="validRedirectUris")
    def valid_redirect_uris(self) -> Sequence[str]:
        return pulumi.get(self, "valid_redirect_uris")


class AwaitableGetClientResult(GetClientResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientResult(
            assertion_consumer_post_url=self.assertion_consumer_post_url,
            assertion_consumer_redirect_url=self.assertion_consumer_redirect_url,
            authentication_flow_binding_overrides=self.authentication_flow_binding_overrides,
            base_url=self.base_url,
            client_id=self.client_id,
            client_signature_required=self.client_signature_required,
            description=self.description,
            enabled=self.enabled,
            encrypt_assertions=self.encrypt_assertions,
            encryption_certificate=self.encryption_certificate,
            force_name_id_format=self.force_name_id_format,
            force_post_binding=self.force_post_binding,
            front_channel_logout=self.front_channel_logout,
            full_scope_allowed=self.full_scope_allowed,
            id=self.id,
            idp_initiated_sso_relay_state=self.idp_initiated_sso_relay_state,
            idp_initiated_sso_url_name=self.idp_initiated_sso_url_name,
            include_authn_statement=self.include_authn_statement,
            logout_service_post_binding_url=self.logout_service_post_binding_url,
            logout_service_redirect_binding_url=self.logout_service_redirect_binding_url,
            master_saml_processing_url=self.master_saml_processing_url,
            name=self.name,
            name_id_format=self.name_id_format,
            realm_id=self.realm_id,
            root_url=self.root_url,
            sign_assertions=self.sign_assertions,
            sign_documents=self.sign_documents,
            signature_algorithm=self.signature_algorithm,
            signing_certificate=self.signing_certificate,
            signing_private_key=self.signing_private_key,
            valid_redirect_uris=self.valid_redirect_uris)


def get_client(client_id: Optional[str] = None,
               realm_id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientResult:
    """
    This data source can be used to fetch properties of a Keycloak client that uses the SAML protocol.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_keycloak as keycloak

    realm_management = keycloak.saml.get_client(realm_id="my-realm",
        client_id="realm-management")
    admin = keycloak.get_role(realm_id="my-realm",
        client_id=realm_management.id,
        name="realm-admin")
    ```


    :param str client_id: The client id (not its unique ID).
    :param str realm_id: The realm id.
    """
    __args__ = dict()
    __args__['clientId'] = client_id
    __args__['realmId'] = realm_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('keycloak:saml/getClient:getClient', __args__, opts=opts, typ=GetClientResult).value

    return AwaitableGetClientResult(
        assertion_consumer_post_url=__ret__.assertion_consumer_post_url,
        assertion_consumer_redirect_url=__ret__.assertion_consumer_redirect_url,
        authentication_flow_binding_overrides=__ret__.authentication_flow_binding_overrides,
        base_url=__ret__.base_url,
        client_id=__ret__.client_id,
        client_signature_required=__ret__.client_signature_required,
        description=__ret__.description,
        enabled=__ret__.enabled,
        encrypt_assertions=__ret__.encrypt_assertions,
        encryption_certificate=__ret__.encryption_certificate,
        force_name_id_format=__ret__.force_name_id_format,
        force_post_binding=__ret__.force_post_binding,
        front_channel_logout=__ret__.front_channel_logout,
        full_scope_allowed=__ret__.full_scope_allowed,
        id=__ret__.id,
        idp_initiated_sso_relay_state=__ret__.idp_initiated_sso_relay_state,
        idp_initiated_sso_url_name=__ret__.idp_initiated_sso_url_name,
        include_authn_statement=__ret__.include_authn_statement,
        logout_service_post_binding_url=__ret__.logout_service_post_binding_url,
        logout_service_redirect_binding_url=__ret__.logout_service_redirect_binding_url,
        master_saml_processing_url=__ret__.master_saml_processing_url,
        name=__ret__.name,
        name_id_format=__ret__.name_id_format,
        realm_id=__ret__.realm_id,
        root_url=__ret__.root_url,
        sign_assertions=__ret__.sign_assertions,
        sign_documents=__ret__.sign_documents,
        signature_algorithm=__ret__.signature_algorithm,
        signing_certificate=__ret__.signing_certificate,
        signing_private_key=__ret__.signing_private_key,
        valid_redirect_uris=__ret__.valid_redirect_uris)
