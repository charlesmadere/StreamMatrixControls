from dataclasses import dataclass

from jtechHdmiMatrix.configuration.absJtechHdmiMatrixConfiguration import AbsJtechHdmiMatrixConfiguration


@dataclass(frozen = True)
class SerialJtechHdmiMatrixConfiguration(AbsJtechHdmiMatrixConfiguration):
    baudRate: int = 115200
    portCount: int = 8
    comPort: str = 'COM10'
