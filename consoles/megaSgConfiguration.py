from dataclasses import dataclass

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True)
class MegaSgConfiguration(AbsConsoleConfiguration):

    extronPreset: int = 2
    hdmiPort: int = 8

    def getExtronPreset(self) -> int:
        return self.extronPreset

    def getHdmiPort(self) -> int:
        return self.hdmiPort

    def getWhichConsole(self) -> WhichConsole:
        return WhichConsole.MEGA_SG

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return False
