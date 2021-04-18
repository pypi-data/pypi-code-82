# coding: utf-8

"""
    AssistedInstall

    Assisted installation  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Inventory(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'hostname': 'str',
        'bmc_address': 'str',
        'interfaces': 'list[Interface]',
        'disks': 'list[Disk]',
        'boot': 'Boot',
        'system_vendor': 'SystemVendor',
        'bmc_v6address': 'str',
        'memory': 'Memory',
        'cpu': 'Cpu',
        'timestamp': 'int',
        'gpus': 'list[Gpu]'
    }

    attribute_map = {
        'hostname': 'hostname',
        'bmc_address': 'bmc_address',
        'interfaces': 'interfaces',
        'disks': 'disks',
        'boot': 'boot',
        'system_vendor': 'system_vendor',
        'bmc_v6address': 'bmc_v6address',
        'memory': 'memory',
        'cpu': 'cpu',
        'timestamp': 'timestamp',
        'gpus': 'gpus'
    }

    def __init__(self, hostname=None, bmc_address=None, interfaces=None, disks=None, boot=None, system_vendor=None, bmc_v6address=None, memory=None, cpu=None, timestamp=None, gpus=None):  # noqa: E501
        """Inventory - a model defined in Swagger"""  # noqa: E501

        self._hostname = None
        self._bmc_address = None
        self._interfaces = None
        self._disks = None
        self._boot = None
        self._system_vendor = None
        self._bmc_v6address = None
        self._memory = None
        self._cpu = None
        self._timestamp = None
        self._gpus = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if bmc_address is not None:
            self.bmc_address = bmc_address
        if interfaces is not None:
            self.interfaces = interfaces
        if disks is not None:
            self.disks = disks
        if boot is not None:
            self.boot = boot
        if system_vendor is not None:
            self.system_vendor = system_vendor
        if bmc_v6address is not None:
            self.bmc_v6address = bmc_v6address
        if memory is not None:
            self.memory = memory
        if cpu is not None:
            self.cpu = cpu
        if timestamp is not None:
            self.timestamp = timestamp
        if gpus is not None:
            self.gpus = gpus

    @property
    def hostname(self):
        """Gets the hostname of this Inventory.  # noqa: E501


        :return: The hostname of this Inventory.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Inventory.


        :param hostname: The hostname of this Inventory.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def bmc_address(self):
        """Gets the bmc_address of this Inventory.  # noqa: E501


        :return: The bmc_address of this Inventory.  # noqa: E501
        :rtype: str
        """
        return self._bmc_address

    @bmc_address.setter
    def bmc_address(self, bmc_address):
        """Sets the bmc_address of this Inventory.


        :param bmc_address: The bmc_address of this Inventory.  # noqa: E501
        :type: str
        """

        self._bmc_address = bmc_address

    @property
    def interfaces(self):
        """Gets the interfaces of this Inventory.  # noqa: E501


        :return: The interfaces of this Inventory.  # noqa: E501
        :rtype: list[Interface]
        """
        return self._interfaces

    @interfaces.setter
    def interfaces(self, interfaces):
        """Sets the interfaces of this Inventory.


        :param interfaces: The interfaces of this Inventory.  # noqa: E501
        :type: list[Interface]
        """

        self._interfaces = interfaces

    @property
    def disks(self):
        """Gets the disks of this Inventory.  # noqa: E501


        :return: The disks of this Inventory.  # noqa: E501
        :rtype: list[Disk]
        """
        return self._disks

    @disks.setter
    def disks(self, disks):
        """Sets the disks of this Inventory.


        :param disks: The disks of this Inventory.  # noqa: E501
        :type: list[Disk]
        """

        self._disks = disks

    @property
    def boot(self):
        """Gets the boot of this Inventory.  # noqa: E501


        :return: The boot of this Inventory.  # noqa: E501
        :rtype: Boot
        """
        return self._boot

    @boot.setter
    def boot(self, boot):
        """Sets the boot of this Inventory.


        :param boot: The boot of this Inventory.  # noqa: E501
        :type: Boot
        """

        self._boot = boot

    @property
    def system_vendor(self):
        """Gets the system_vendor of this Inventory.  # noqa: E501


        :return: The system_vendor of this Inventory.  # noqa: E501
        :rtype: SystemVendor
        """
        return self._system_vendor

    @system_vendor.setter
    def system_vendor(self, system_vendor):
        """Sets the system_vendor of this Inventory.


        :param system_vendor: The system_vendor of this Inventory.  # noqa: E501
        :type: SystemVendor
        """

        self._system_vendor = system_vendor

    @property
    def bmc_v6address(self):
        """Gets the bmc_v6address of this Inventory.  # noqa: E501


        :return: The bmc_v6address of this Inventory.  # noqa: E501
        :rtype: str
        """
        return self._bmc_v6address

    @bmc_v6address.setter
    def bmc_v6address(self, bmc_v6address):
        """Sets the bmc_v6address of this Inventory.


        :param bmc_v6address: The bmc_v6address of this Inventory.  # noqa: E501
        :type: str
        """

        self._bmc_v6address = bmc_v6address

    @property
    def memory(self):
        """Gets the memory of this Inventory.  # noqa: E501


        :return: The memory of this Inventory.  # noqa: E501
        :rtype: Memory
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this Inventory.


        :param memory: The memory of this Inventory.  # noqa: E501
        :type: Memory
        """

        self._memory = memory

    @property
    def cpu(self):
        """Gets the cpu of this Inventory.  # noqa: E501


        :return: The cpu of this Inventory.  # noqa: E501
        :rtype: Cpu
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this Inventory.


        :param cpu: The cpu of this Inventory.  # noqa: E501
        :type: Cpu
        """

        self._cpu = cpu

    @property
    def timestamp(self):
        """Gets the timestamp of this Inventory.  # noqa: E501


        :return: The timestamp of this Inventory.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Inventory.


        :param timestamp: The timestamp of this Inventory.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def gpus(self):
        """Gets the gpus of this Inventory.  # noqa: E501


        :return: The gpus of this Inventory.  # noqa: E501
        :rtype: list[Gpu]
        """
        return self._gpus

    @gpus.setter
    def gpus(self, gpus):
        """Sets the gpus of this Inventory.


        :param gpus: The gpus of this Inventory.  # noqa: E501
        :type: list[Gpu]
        """

        self._gpus = gpus

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Inventory, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Inventory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
