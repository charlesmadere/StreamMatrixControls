from dataclasses import dataclass

from .absExtronVgaMatrixConfiguration import AbsExtronVgaMatrixConfiguration


@dataclass(frozen = True)
class SerialExtronVgaMatrixConfiguration(AbsExtronVgaMatrixConfiguration):
    baudRate: int
    comPort: str
