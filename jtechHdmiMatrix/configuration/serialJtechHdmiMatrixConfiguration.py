from dataclasses import dataclass

from .absJtechHdmiMatrixConfiguration import AbsJtechHdmiMatrixConfiguration


@dataclass(frozen = True)
class SerialJtechHdmiMatrixConfiguration(AbsJtechHdmiMatrixConfiguration):
    baudRate: int
    portCount: int
    comPort: str
