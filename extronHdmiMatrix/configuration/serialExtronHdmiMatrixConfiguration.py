from dataclasses import dataclass

from extronHdmiMatrix.configuration.absExtronHdmiMatrixConfiguration import AbsExtronHdmiMatrixConfiguration


@dataclass(frozen = True, slots = True)
class SerialExtronHdmiMatrixConfiguration(AbsExtronHdmiMatrixConfiguration):
    baudRate: int = 9600
    comPort: str = 'COM9'
