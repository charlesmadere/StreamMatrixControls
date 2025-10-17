from dataclasses import dataclass

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True)
class SonyPs3Configuration(AbsConsoleConfiguration):

    extronPreset: int = 7
    hdmiPort: int = 1

    def getExtronPreset(self) -> int:
        return self.extronPreset

    def getHdmiPort(self) -> int:
        return self.hdmiPort

    def getWhichConsole(self) -> WhichConsole:
        return WhichConsole.SONY_PS3

    def usesRetroTinkPassThrough(self) -> bool:
        return False
