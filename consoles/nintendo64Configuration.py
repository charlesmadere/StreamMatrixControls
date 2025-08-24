from dataclasses import dataclass

from .absConsoleConfiguration import AbsConsoleConfiguration
from .whichConsole import WhichConsole


@dataclass(frozen = True)
class Nintendo64Configuration(AbsConsoleConfiguration):

    extronPreset: int = 5
    hdmiPort: int = 4

    def getExtronPreset(self) -> int:
        return self.extronPreset

    def getHdmiPort(self) -> int:
        return self.hdmiPort

    def getWhichConsole(self) -> WhichConsole:
        return WhichConsole.NINTENDO_64

    def usesRetroTinkPassThrough(self) -> bool:
        return False
