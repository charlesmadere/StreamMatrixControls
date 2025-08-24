from dataclasses import dataclass

from .absJtechHdmiMatrixConfiguration import AbsJtechHdmiMatrixConfiguration


@dataclass(frozen = True)
class NetworkJtechHdmiMatrixConfiguration(AbsJtechHdmiMatrixConfiguration):
    portCount: int = 8
    ipAddress: str = 'http://192.168.1.7'
