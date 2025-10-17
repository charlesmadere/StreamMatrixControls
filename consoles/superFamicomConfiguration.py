from dataclasses import dataclass

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True)
class SuperFamicomConfiguration(AbsConsoleConfiguration):

    extronPreset: int = 3
    hdmiPort: int = 8

    def getExtronPreset(self) -> int:
        return self.extronPreset

    def getHdmiPort(self) -> int:
        return self.hdmiPort

    def getWhichConsole(self) -> WhichConsole:
        return WhichConsole.SUPER_FAMICOM

    def usesRetroTinkPassThrough(self) -> bool:
        return False
