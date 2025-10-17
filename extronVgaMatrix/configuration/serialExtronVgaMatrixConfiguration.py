from dataclasses import dataclass

from extronVgaMatrix.configuration.absExtronVgaMatrixConfiguration import AbsExtronVgaMatrixConfiguration


@dataclass(frozen = True)
class SerialExtronVgaMatrixConfiguration(AbsExtronVgaMatrixConfiguration):
    baudRate: int = 9600
    comPort: str = 'COM9'
