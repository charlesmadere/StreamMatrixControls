from dataclasses import dataclass

from extronHdmiMatrix.configuration.absExtronHdmiMatrixConfiguration import AbsExtronHdmiMatrixConfiguration


@dataclass(frozen = True, slots = True)
class NetworkExtronHdmiMatrixConfiguration(AbsExtronHdmiMatrixConfiguration):
    port: int = 23
    ipAddress: str = '192.168.1.249'
