from dataclasses import dataclass

from .absConsoleConfiguration import AbsConsoleConfiguration
from .whichConsole import WhichConsole


@dataclass(frozen = True)
class GameCubeConfiguration(AbsConsoleConfiguration):

    extronPreset: int = 6
    hdmiPort: int = 4

    def getExtronPreset(self) -> int:
        return self.extronPreset

    def getHdmiPort(self) -> int:
        return self.hdmiPort

    def getWhichConsole(self) -> WhichConsole:
        return WhichConsole.GAME_CUBE

    def usesRetroTinkPassThrough(self) -> bool:
        return False
