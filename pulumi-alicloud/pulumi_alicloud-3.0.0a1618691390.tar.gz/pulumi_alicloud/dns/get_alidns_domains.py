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
    'GetAlidnsDomainsResult',
    'AwaitableGetAlidnsDomainsResult',
    'get_alidns_domains',
]

@pulumi.output_type
class GetAlidnsDomainsResult:
    """
    A collection of values returned by getAlidnsDomains.
    """
    def __init__(__self__, ali_domain=None, domain_name_regex=None, domains=None, enable_details=None, group_id=None, group_name_regex=None, id=None, ids=None, instance_id=None, key_word=None, lang=None, names=None, output_file=None, resource_group_id=None, search_mode=None, starmark=None, tags=None, version_code=None):
        if ali_domain and not isinstance(ali_domain, bool):
            raise TypeError("Expected argument 'ali_domain' to be a bool")
        pulumi.set(__self__, "ali_domain", ali_domain)
        if domain_name_regex and not isinstance(domain_name_regex, str):
            raise TypeError("Expected argument 'domain_name_regex' to be a str")
        pulumi.set(__self__, "domain_name_regex", domain_name_regex)
        if domains and not isinstance(domains, list):
            raise TypeError("Expected argument 'domains' to be a list")
        pulumi.set(__self__, "domains", domains)
        if enable_details and not isinstance(enable_details, bool):
            raise TypeError("Expected argument 'enable_details' to be a bool")
        pulumi.set(__self__, "enable_details", enable_details)
        if group_id and not isinstance(group_id, str):
            raise TypeError("Expected argument 'group_id' to be a str")
        pulumi.set(__self__, "group_id", group_id)
        if group_name_regex and not isinstance(group_name_regex, str):
            raise TypeError("Expected argument 'group_name_regex' to be a str")
        pulumi.set(__self__, "group_name_regex", group_name_regex)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if key_word and not isinstance(key_word, str):
            raise TypeError("Expected argument 'key_word' to be a str")
        pulumi.set(__self__, "key_word", key_word)
        if lang and not isinstance(lang, str):
            raise TypeError("Expected argument 'lang' to be a str")
        pulumi.set(__self__, "lang", lang)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if resource_group_id and not isinstance(resource_group_id, str):
            raise TypeError("Expected argument 'resource_group_id' to be a str")
        pulumi.set(__self__, "resource_group_id", resource_group_id)
        if search_mode and not isinstance(search_mode, str):
            raise TypeError("Expected argument 'search_mode' to be a str")
        pulumi.set(__self__, "search_mode", search_mode)
        if starmark and not isinstance(starmark, bool):
            raise TypeError("Expected argument 'starmark' to be a bool")
        pulumi.set(__self__, "starmark", starmark)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if version_code and not isinstance(version_code, str):
            raise TypeError("Expected argument 'version_code' to be a str")
        pulumi.set(__self__, "version_code", version_code)

    @property
    @pulumi.getter(name="aliDomain")
    def ali_domain(self) -> Optional[bool]:
        """
        Indicates whether the domain is an Alibaba Cloud domain.
        """
        return pulumi.get(self, "ali_domain")

    @property
    @pulumi.getter(name="domainNameRegex")
    def domain_name_regex(self) -> Optional[str]:
        return pulumi.get(self, "domain_name_regex")

    @property
    @pulumi.getter
    def domains(self) -> Sequence['outputs.GetAlidnsDomainsDomainResult']:
        """
        A list of domains. Each element contains the following attributes:
        """
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter(name="enableDetails")
    def enable_details(self) -> Optional[bool]:
        return pulumi.get(self, "enable_details")

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[str]:
        """
        Id of group that contains the domain.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter(name="groupNameRegex")
    def group_name_regex(self) -> Optional[str]:
        return pulumi.get(self, "group_name_regex")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of domain IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> Optional[str]:
        """
        Cloud analysis product ID of the domain.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter(name="keyWord")
    def key_word(self) -> Optional[str]:
        return pulumi.get(self, "key_word")

    @property
    @pulumi.getter
    def lang(self) -> Optional[str]:
        return pulumi.get(self, "lang")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of domain names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="resourceGroupId")
    def resource_group_id(self) -> Optional[str]:
        """
        The Id of resource group which the dns belongs.
        """
        return pulumi.get(self, "resource_group_id")

    @property
    @pulumi.getter(name="searchMode")
    def search_mode(self) -> Optional[str]:
        return pulumi.get(self, "search_mode")

    @property
    @pulumi.getter
    def starmark(self) -> Optional[bool]:
        return pulumi.get(self, "starmark")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="versionCode")
    def version_code(self) -> Optional[str]:
        """
        Cloud resolution version ID.
        """
        return pulumi.get(self, "version_code")


class AwaitableGetAlidnsDomainsResult(GetAlidnsDomainsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAlidnsDomainsResult(
            ali_domain=self.ali_domain,
            domain_name_regex=self.domain_name_regex,
            domains=self.domains,
            enable_details=self.enable_details,
            group_id=self.group_id,
            group_name_regex=self.group_name_regex,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            key_word=self.key_word,
            lang=self.lang,
            names=self.names,
            output_file=self.output_file,
            resource_group_id=self.resource_group_id,
            search_mode=self.search_mode,
            starmark=self.starmark,
            tags=self.tags,
            version_code=self.version_code)


def get_alidns_domains(ali_domain: Optional[bool] = None,
                       domain_name_regex: Optional[str] = None,
                       enable_details: Optional[bool] = None,
                       group_id: Optional[str] = None,
                       group_name_regex: Optional[str] = None,
                       ids: Optional[Sequence[str]] = None,
                       instance_id: Optional[str] = None,
                       key_word: Optional[str] = None,
                       lang: Optional[str] = None,
                       output_file: Optional[str] = None,
                       resource_group_id: Optional[str] = None,
                       search_mode: Optional[str] = None,
                       starmark: Optional[bool] = None,
                       tags: Optional[Mapping[str, Any]] = None,
                       version_code: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAlidnsDomainsResult:
    """
    This data source provides a list of Alidns Domains in an Alibaba Cloud account according to the specified filters.

    > **NOTE:**  Available in 1.95.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    domains_ds = alicloud.dns.get_alidns_domains(domain_name_regex="^hegu",
        output_file="domains.txt")
    pulumi.export("firstDomainId", domains_ds.domains[0].domain_id)
    ```


    :param bool ali_domain: Specifies whether the domain is from Alibaba Cloud or not.
    :param str domain_name_regex: A regex string to filter results by the domain name.
    :param str group_id: Domain group ID, if not filled, the default is all groups.
    :param str group_name_regex: A regex string to filter results by the group name.
    :param Sequence[str] ids: A list of domain IDs.
    :param str instance_id: Cloud analysis product ID.
    :param str key_word: The keywords are searched according to the `%KeyWord%` mode, which is not case sensitive.
    :param str lang: User language.
    :param str resource_group_id: The Id of resource group which the dns belongs.
    :param str search_mode: Search mode, `LIKE` fuzzy search, `EXACT` exact search.
    :param bool starmark: Whether to query the domain name star.
    :param Mapping[str, Any] tags: A mapping of tags to assign to the resource.
    :param str version_code: Cloud analysis version code.
    """
    __args__ = dict()
    __args__['aliDomain'] = ali_domain
    __args__['domainNameRegex'] = domain_name_regex
    __args__['enableDetails'] = enable_details
    __args__['groupId'] = group_id
    __args__['groupNameRegex'] = group_name_regex
    __args__['ids'] = ids
    __args__['instanceId'] = instance_id
    __args__['keyWord'] = key_word
    __args__['lang'] = lang
    __args__['outputFile'] = output_file
    __args__['resourceGroupId'] = resource_group_id
    __args__['searchMode'] = search_mode
    __args__['starmark'] = starmark
    __args__['tags'] = tags
    __args__['versionCode'] = version_code
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:dns/getAlidnsDomains:getAlidnsDomains', __args__, opts=opts, typ=GetAlidnsDomainsResult).value

    return AwaitableGetAlidnsDomainsResult(
        ali_domain=__ret__.ali_domain,
        domain_name_regex=__ret__.domain_name_regex,
        domains=__ret__.domains,
        enable_details=__ret__.enable_details,
        group_id=__ret__.group_id,
        group_name_regex=__ret__.group_name_regex,
        id=__ret__.id,
        ids=__ret__.ids,
        instance_id=__ret__.instance_id,
        key_word=__ret__.key_word,
        lang=__ret__.lang,
        names=__ret__.names,
        output_file=__ret__.output_file,
        resource_group_id=__ret__.resource_group_id,
        search_mode=__ret__.search_mode,
        starmark=__ret__.starmark,
        tags=__ret__.tags,
        version_code=__ret__.version_code)
