from dataclasses import dataclass

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True)
class Nintendo64Configuration(AbsConsoleConfiguration):

    extronPreset: int = 5
    hdmiPort: int = 3

    def getExtronPreset(self) -> int:
        return self.extronPreset

    def getHdmiPort(self) -> int:
        return self.hdmiPort

    def getWhichConsole(self) -> WhichConsole:
        return WhichConsole.NINTENDO_64

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return False
