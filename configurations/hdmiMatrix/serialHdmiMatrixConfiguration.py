from dataclasses import dataclass

from .absHdmiMatrixConfiguration import AbsHdmiMatrixConfiguration
from ..serialConfiguration import SerialConfiguration


@dataclass(frozen = True)
class SerialHdmiMatrixConfiguration(
    AbsHdmiMatrixConfiguration,
    SerialConfiguration,
):

    baudRate: int
    comPort: str

    def getBaudRate(self) -> int:
        return self.baudRate

    def getComPort(self) -> str:
        return self.comPort
