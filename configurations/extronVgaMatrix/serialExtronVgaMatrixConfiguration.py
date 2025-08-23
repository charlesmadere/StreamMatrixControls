from dataclasses import dataclass

from .absExtronVgaMatrixConfiguration import AbsExtronVgaMatrixConfiguration
from ..serialConfiguration import SerialConfiguration


@dataclass(frozen = True)
class SerialExtronVgaMatrixConfiguration(
    AbsExtronVgaMatrixConfiguration,
    SerialConfiguration,
):

    baudRate: int
    comPort: str

    def getBaudRate(self) -> int:
        return self.baudRate

    def getComPort(self) -> str:
        return self.comPort
