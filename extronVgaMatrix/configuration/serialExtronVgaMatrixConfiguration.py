from dataclasses import dataclass

from extronVgaMatrix.configuration.absExtronVgaMatrixConfiguration import AbsExtronVgaMatrixConfiguration


@dataclass(frozen = True, slots = True)
class SerialExtronVgaMatrixConfiguration(AbsExtronVgaMatrixConfiguration):
    comPort: str

    @property
    def baudRate(self) -> int:
        return 9600
