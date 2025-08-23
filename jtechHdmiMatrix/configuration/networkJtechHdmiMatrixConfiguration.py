from dataclasses import dataclass

from .absJtechHdmiMatrixConfiguration import AbsJtechHdmiMatrixConfiguration


@dataclass(frozen = True)
class NetworkJtechHdmiMatrixConfiguration(AbsJtechHdmiMatrixConfiguration):
    portCount: int
    ipAddress: str
