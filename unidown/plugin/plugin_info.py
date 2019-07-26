from __future__ import annotations

from packaging.version import InvalidVersion, Version

from unidown.plugin.protobuf.plugin_info_pb2 import PluginInfoProto


class PluginInfo:
    """
    .. warning:

        Parameters may change in the future.

    Information about the module. Those information will be saved into the save files as well.

    :param name: the name of the plugin
    :param version: version, PEP440 conform
    :param host: host url of the main data
    :raises ValueError: name is empty
    :raises ValueError: host is empty
    :raises ~packaging.version.InvalidVersion: version is not PEP440 conform

    :ivar name: name
    :vartype name: str
    :ivar host: host url of the main data
    :vartype host: str
    :ivar version: plugin version
    :vartype version: ~packaging.version.Version
    """

    def __init__(self, name: str, version: str, host: str):
        if name is None or name == "":
            raise ValueError("Plugin name cannot be empty.")
        elif host is None or host == "":
            raise ValueError("Plugin host cannot be empty.")
        self.name = name
        self.host = host

        try:
            self.version = Version(version)
        except InvalidVersion:
            raise InvalidVersion(f"Plugin version is not PEP440 conform: {version}")

    @classmethod
    def from_protobuf(cls, proto: PluginInfoProto) -> PluginInfo:
        """
        Constructor from protobuf.

        :param proto: protobuf structure
        :return: the PluginInfo
        :raises ValueError: name of PluginInfo does not exist or is empty inside the protobuf
        :raises ValueError: version of PluginInfo does not exist or is empty inside the protobuf
        :raises ValueError: host of PluginInfo does not exist or is empty inside the protobuf
        """
        if proto.name == "":
            raise ValueError("name of PluginInfo does not exist or is empty inside the protobuf.")
        elif proto.version == "":
            raise ValueError("version of PluginInfo does not exist or is empty inside the protobuf.")
        elif proto.host == "":
            raise ValueError("host of PluginInfo does not exist or is empty inside the protobuf.")
        return cls(proto.name, proto.version, proto.host)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.name == other.name and self.host == other.host and self.version == other.version

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return self.name + " - " + str(self.version) + " : " + self.host

    def to_protobuf(self) -> PluginInfoProto:
        """
        Create protobuf item.

        :return: protobuf structure
        """
        proto = PluginInfoProto()
        proto.name = self.name
        proto.version = str(self.version)
        proto.host = self.host
        return proto
