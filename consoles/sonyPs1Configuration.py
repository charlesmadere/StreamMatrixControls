from dataclasses import dataclass

from .absConsoleConfiguration import AbsConsoleConfiguration
from .whichConsole import WhichConsole


@dataclass(frozen = True)
class SonyPs1Configuration(AbsConsoleConfiguration):

    extronPreset: int = 4
    hdmiPort: int = 3

    def getExtronPreset(self) -> int:
        return self.extronPreset

    def getHdmiPort(self) -> int:
        return self.hdmiPort

    def getWhichConsole(self) -> WhichConsole:
        return WhichConsole.SONY_PS1

    def usesRetroTinkPassThrough(self) -> bool:
        return False
