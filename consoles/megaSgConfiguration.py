from dataclasses import dataclass

from .absConsoleConfiguration import AbsConsoleConfiguration
from .whichConsole import WhichConsole


@dataclass(frozen = True)
class MegaSgConfiguration(AbsConsoleConfiguration):

    extronPreset: int = 2
    hdmiPort: int = 1

    def getExtronPreset(self) -> int:
        return self.extronPreset

    def getHdmiPort(self) -> int:
        return self.hdmiPort

    def getWhichConsole(self) -> WhichConsole:
        return WhichConsole.MEGA_SG

    def usesRetroTinkPassThrough(self) -> bool:
        return False
