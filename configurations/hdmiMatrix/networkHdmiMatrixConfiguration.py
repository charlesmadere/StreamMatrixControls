from dataclasses import dataclass

from .absHdmiMatrixConfiguration import AbsHdmiMatrixConfiguration
from ..networkConfiguration import NetworkConfiguration


@dataclass(frozen = True)
class NetworkHdmiMatrixConfiguration(
    AbsHdmiMatrixConfiguration,
    NetworkConfiguration,
):

    ipAddress: str

    def getIpAddress(self) -> str:
        return self.ipAddress
