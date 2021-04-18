# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MfaPolicyArgs', 'MfaPolicy']

@pulumi.input_type
class MfaPolicyArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 duo: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_u2f: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_webauthn: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 google_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 groups_includeds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 hotp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 okta_call: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_email: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_password: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_push: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_question: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_sms: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rsa_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 symantec_vip: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 yubikey_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a MfaPolicy resource.
        :param pulumi.Input[str] description: Policy Description
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups_includeds: List of Group IDs to Include
        :param pulumi.Input[str] name: Policy Name
        :param pulumi.Input[int] priority: Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
               priority is provided. API defaults it to the last (lowest) if not there.
        :param pulumi.Input[str] status: Policy Status: ACTIVE or INACTIVE.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if duo is not None:
            pulumi.set(__self__, "duo", duo)
        if fido_u2f is not None:
            pulumi.set(__self__, "fido_u2f", fido_u2f)
        if fido_webauthn is not None:
            pulumi.set(__self__, "fido_webauthn", fido_webauthn)
        if google_otp is not None:
            pulumi.set(__self__, "google_otp", google_otp)
        if groups_includeds is not None:
            pulumi.set(__self__, "groups_includeds", groups_includeds)
        if hotp is not None:
            pulumi.set(__self__, "hotp", hotp)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if okta_call is not None:
            pulumi.set(__self__, "okta_call", okta_call)
        if okta_email is not None:
            pulumi.set(__self__, "okta_email", okta_email)
        if okta_otp is not None:
            pulumi.set(__self__, "okta_otp", okta_otp)
        if okta_password is not None:
            pulumi.set(__self__, "okta_password", okta_password)
        if okta_push is not None:
            pulumi.set(__self__, "okta_push", okta_push)
        if okta_question is not None:
            pulumi.set(__self__, "okta_question", okta_question)
        if okta_sms is not None:
            pulumi.set(__self__, "okta_sms", okta_sms)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if rsa_token is not None:
            pulumi.set(__self__, "rsa_token", rsa_token)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if symantec_vip is not None:
            pulumi.set(__self__, "symantec_vip", symantec_vip)
        if yubikey_token is not None:
            pulumi.set(__self__, "yubikey_token", yubikey_token)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Policy Description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def duo(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "duo")

    @duo.setter
    def duo(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "duo", value)

    @property
    @pulumi.getter(name="fidoU2f")
    def fido_u2f(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "fido_u2f")

    @fido_u2f.setter
    def fido_u2f(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "fido_u2f", value)

    @property
    @pulumi.getter(name="fidoWebauthn")
    def fido_webauthn(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "fido_webauthn")

    @fido_webauthn.setter
    def fido_webauthn(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "fido_webauthn", value)

    @property
    @pulumi.getter(name="googleOtp")
    def google_otp(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "google_otp")

    @google_otp.setter
    def google_otp(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "google_otp", value)

    @property
    @pulumi.getter(name="groupsIncludeds")
    def groups_includeds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Group IDs to Include
        """
        return pulumi.get(self, "groups_includeds")

    @groups_includeds.setter
    def groups_includeds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "groups_includeds", value)

    @property
    @pulumi.getter
    def hotp(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "hotp")

    @hotp.setter
    def hotp(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "hotp", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Policy Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="oktaCall")
    def okta_call(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_call")

    @okta_call.setter
    def okta_call(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_call", value)

    @property
    @pulumi.getter(name="oktaEmail")
    def okta_email(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_email")

    @okta_email.setter
    def okta_email(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_email", value)

    @property
    @pulumi.getter(name="oktaOtp")
    def okta_otp(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_otp")

    @okta_otp.setter
    def okta_otp(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_otp", value)

    @property
    @pulumi.getter(name="oktaPassword")
    def okta_password(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_password")

    @okta_password.setter
    def okta_password(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_password", value)

    @property
    @pulumi.getter(name="oktaPush")
    def okta_push(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_push")

    @okta_push.setter
    def okta_push(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_push", value)

    @property
    @pulumi.getter(name="oktaQuestion")
    def okta_question(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_question")

    @okta_question.setter
    def okta_question(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_question", value)

    @property
    @pulumi.getter(name="oktaSms")
    def okta_sms(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_sms")

    @okta_sms.setter
    def okta_sms(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_sms", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
        priority is provided. API defaults it to the last (lowest) if not there.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="rsaToken")
    def rsa_token(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "rsa_token")

    @rsa_token.setter
    def rsa_token(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "rsa_token", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Policy Status: ACTIVE or INACTIVE.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="symantecVip")
    def symantec_vip(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "symantec_vip")

    @symantec_vip.setter
    def symantec_vip(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "symantec_vip", value)

    @property
    @pulumi.getter(name="yubikeyToken")
    def yubikey_token(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "yubikey_token")

    @yubikey_token.setter
    def yubikey_token(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "yubikey_token", value)


@pulumi.input_type
class _MfaPolicyState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 duo: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_u2f: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_webauthn: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 google_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 groups_includeds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 hotp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 okta_call: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_email: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_password: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_push: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_question: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_sms: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rsa_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 symantec_vip: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 yubikey_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering MfaPolicy resources.
        :param pulumi.Input[str] description: Policy Description
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups_includeds: List of Group IDs to Include
        :param pulumi.Input[str] name: Policy Name
        :param pulumi.Input[int] priority: Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
               priority is provided. API defaults it to the last (lowest) if not there.
        :param pulumi.Input[str] status: Policy Status: ACTIVE or INACTIVE.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if duo is not None:
            pulumi.set(__self__, "duo", duo)
        if fido_u2f is not None:
            pulumi.set(__self__, "fido_u2f", fido_u2f)
        if fido_webauthn is not None:
            pulumi.set(__self__, "fido_webauthn", fido_webauthn)
        if google_otp is not None:
            pulumi.set(__self__, "google_otp", google_otp)
        if groups_includeds is not None:
            pulumi.set(__self__, "groups_includeds", groups_includeds)
        if hotp is not None:
            pulumi.set(__self__, "hotp", hotp)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if okta_call is not None:
            pulumi.set(__self__, "okta_call", okta_call)
        if okta_email is not None:
            pulumi.set(__self__, "okta_email", okta_email)
        if okta_otp is not None:
            pulumi.set(__self__, "okta_otp", okta_otp)
        if okta_password is not None:
            pulumi.set(__self__, "okta_password", okta_password)
        if okta_push is not None:
            pulumi.set(__self__, "okta_push", okta_push)
        if okta_question is not None:
            pulumi.set(__self__, "okta_question", okta_question)
        if okta_sms is not None:
            pulumi.set(__self__, "okta_sms", okta_sms)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if rsa_token is not None:
            pulumi.set(__self__, "rsa_token", rsa_token)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if symantec_vip is not None:
            pulumi.set(__self__, "symantec_vip", symantec_vip)
        if yubikey_token is not None:
            pulumi.set(__self__, "yubikey_token", yubikey_token)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Policy Description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def duo(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "duo")

    @duo.setter
    def duo(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "duo", value)

    @property
    @pulumi.getter(name="fidoU2f")
    def fido_u2f(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "fido_u2f")

    @fido_u2f.setter
    def fido_u2f(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "fido_u2f", value)

    @property
    @pulumi.getter(name="fidoWebauthn")
    def fido_webauthn(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "fido_webauthn")

    @fido_webauthn.setter
    def fido_webauthn(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "fido_webauthn", value)

    @property
    @pulumi.getter(name="googleOtp")
    def google_otp(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "google_otp")

    @google_otp.setter
    def google_otp(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "google_otp", value)

    @property
    @pulumi.getter(name="groupsIncludeds")
    def groups_includeds(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of Group IDs to Include
        """
        return pulumi.get(self, "groups_includeds")

    @groups_includeds.setter
    def groups_includeds(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "groups_includeds", value)

    @property
    @pulumi.getter
    def hotp(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "hotp")

    @hotp.setter
    def hotp(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "hotp", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Policy Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="oktaCall")
    def okta_call(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_call")

    @okta_call.setter
    def okta_call(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_call", value)

    @property
    @pulumi.getter(name="oktaEmail")
    def okta_email(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_email")

    @okta_email.setter
    def okta_email(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_email", value)

    @property
    @pulumi.getter(name="oktaOtp")
    def okta_otp(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_otp")

    @okta_otp.setter
    def okta_otp(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_otp", value)

    @property
    @pulumi.getter(name="oktaPassword")
    def okta_password(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_password")

    @okta_password.setter
    def okta_password(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_password", value)

    @property
    @pulumi.getter(name="oktaPush")
    def okta_push(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_push")

    @okta_push.setter
    def okta_push(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_push", value)

    @property
    @pulumi.getter(name="oktaQuestion")
    def okta_question(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_question")

    @okta_question.setter
    def okta_question(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_question", value)

    @property
    @pulumi.getter(name="oktaSms")
    def okta_sms(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "okta_sms")

    @okta_sms.setter
    def okta_sms(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "okta_sms", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
        priority is provided. API defaults it to the last (lowest) if not there.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="rsaToken")
    def rsa_token(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "rsa_token")

    @rsa_token.setter
    def rsa_token(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "rsa_token", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Policy Status: ACTIVE or INACTIVE.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="symantecVip")
    def symantec_vip(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "symantec_vip")

    @symantec_vip.setter
    def symantec_vip(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "symantec_vip", value)

    @property
    @pulumi.getter(name="yubikeyToken")
    def yubikey_token(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        return pulumi.get(self, "yubikey_token")

    @yubikey_token.setter
    def yubikey_token(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "yubikey_token", value)


class MfaPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 duo: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_u2f: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_webauthn: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 google_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 groups_includeds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 hotp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 okta_call: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_email: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_password: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_push: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_question: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_sms: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rsa_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 symantec_vip: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 yubikey_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a MfaPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Policy Description
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups_includeds: List of Group IDs to Include
        :param pulumi.Input[str] name: Policy Name
        :param pulumi.Input[int] priority: Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
               priority is provided. API defaults it to the last (lowest) if not there.
        :param pulumi.Input[str] status: Policy Status: ACTIVE or INACTIVE.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[MfaPolicyArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a MfaPolicy resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param MfaPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MfaPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 duo: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_u2f: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fido_webauthn: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 google_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 groups_includeds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 hotp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 okta_call: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_email: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_password: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_push: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_question: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 okta_sms: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 rsa_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 symantec_vip: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 yubikey_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
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
            __props__ = MfaPolicyArgs.__new__(MfaPolicyArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["duo"] = duo
            __props__.__dict__["fido_u2f"] = fido_u2f
            __props__.__dict__["fido_webauthn"] = fido_webauthn
            __props__.__dict__["google_otp"] = google_otp
            __props__.__dict__["groups_includeds"] = groups_includeds
            __props__.__dict__["hotp"] = hotp
            __props__.__dict__["name"] = name
            __props__.__dict__["okta_call"] = okta_call
            __props__.__dict__["okta_email"] = okta_email
            __props__.__dict__["okta_otp"] = okta_otp
            __props__.__dict__["okta_password"] = okta_password
            __props__.__dict__["okta_push"] = okta_push
            __props__.__dict__["okta_question"] = okta_question
            __props__.__dict__["okta_sms"] = okta_sms
            __props__.__dict__["priority"] = priority
            __props__.__dict__["rsa_token"] = rsa_token
            __props__.__dict__["status"] = status
            __props__.__dict__["symantec_vip"] = symantec_vip
            __props__.__dict__["yubikey_token"] = yubikey_token
        super(MfaPolicy, __self__).__init__(
            'okta:deprecated/mfaPolicy:MfaPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            duo: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            fido_u2f: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            fido_webauthn: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            google_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            groups_includeds: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            hotp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            okta_call: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_email: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_otp: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_password: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_push: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_question: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            okta_sms: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            rsa_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            symantec_vip: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            yubikey_token: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'MfaPolicy':
        """
        Get an existing MfaPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Policy Description
        :param pulumi.Input[Sequence[pulumi.Input[str]]] groups_includeds: List of Group IDs to Include
        :param pulumi.Input[str] name: Policy Name
        :param pulumi.Input[int] priority: Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
               priority is provided. API defaults it to the last (lowest) if not there.
        :param pulumi.Input[str] status: Policy Status: ACTIVE or INACTIVE.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MfaPolicyState.__new__(_MfaPolicyState)

        __props__.__dict__["description"] = description
        __props__.__dict__["duo"] = duo
        __props__.__dict__["fido_u2f"] = fido_u2f
        __props__.__dict__["fido_webauthn"] = fido_webauthn
        __props__.__dict__["google_otp"] = google_otp
        __props__.__dict__["groups_includeds"] = groups_includeds
        __props__.__dict__["hotp"] = hotp
        __props__.__dict__["name"] = name
        __props__.__dict__["okta_call"] = okta_call
        __props__.__dict__["okta_email"] = okta_email
        __props__.__dict__["okta_otp"] = okta_otp
        __props__.__dict__["okta_password"] = okta_password
        __props__.__dict__["okta_push"] = okta_push
        __props__.__dict__["okta_question"] = okta_question
        __props__.__dict__["okta_sms"] = okta_sms
        __props__.__dict__["priority"] = priority
        __props__.__dict__["rsa_token"] = rsa_token
        __props__.__dict__["status"] = status
        __props__.__dict__["symantec_vip"] = symantec_vip
        __props__.__dict__["yubikey_token"] = yubikey_token
        return MfaPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Policy Description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duo(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "duo")

    @property
    @pulumi.getter(name="fidoU2f")
    def fido_u2f(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "fido_u2f")

    @property
    @pulumi.getter(name="fidoWebauthn")
    def fido_webauthn(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "fido_webauthn")

    @property
    @pulumi.getter(name="googleOtp")
    def google_otp(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "google_otp")

    @property
    @pulumi.getter(name="groupsIncludeds")
    def groups_includeds(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of Group IDs to Include
        """
        return pulumi.get(self, "groups_includeds")

    @property
    @pulumi.getter
    def hotp(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "hotp")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Policy Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oktaCall")
    def okta_call(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "okta_call")

    @property
    @pulumi.getter(name="oktaEmail")
    def okta_email(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "okta_email")

    @property
    @pulumi.getter(name="oktaOtp")
    def okta_otp(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "okta_otp")

    @property
    @pulumi.getter(name="oktaPassword")
    def okta_password(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "okta_password")

    @property
    @pulumi.getter(name="oktaPush")
    def okta_push(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "okta_push")

    @property
    @pulumi.getter(name="oktaQuestion")
    def okta_question(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "okta_question")

    @property
    @pulumi.getter(name="oktaSms")
    def okta_sms(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "okta_sms")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Policy Priority, this attribute can be set to a valid priority. To avoid endless diff situation we error if an invalid
        priority is provided. API defaults it to the last (lowest) if not there.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="rsaToken")
    def rsa_token(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "rsa_token")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Policy Status: ACTIVE or INACTIVE.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="symantecVip")
    def symantec_vip(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "symantec_vip")

    @property
    @pulumi.getter(name="yubikeyToken")
    def yubikey_token(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        return pulumi.get(self, "yubikey_token")

