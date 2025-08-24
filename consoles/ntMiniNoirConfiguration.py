from dataclasses import dataclass

from .absConsoleConfiguration import AbsConsoleConfiguration
from .whichConsole import WhichConsole


@dataclass(frozen = True)
class NtMiniNoirConfiguration(AbsConsoleConfiguration):

    extronPreset: int = 1
    hdmiPort: int = 1

    def getExtronPreset(self) -> int:
        return self.extronPreset

    def getHdmiPort(self) -> int:
        return self.hdmiPort

    def getWhichConsole(self) -> WhichConsole:
        return WhichConsole.NT_MINI_NOIR

    def usesRetroTinkPassThrough(self) -> bool:
        return True
