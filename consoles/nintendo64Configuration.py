from dataclasses import dataclass

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True)
class Nintendo64Configuration(AbsConsoleConfiguration):

    @property
    def extronPreset(self) -> int:
        return 5

    @property
    def hdmiPort(self) -> int:
        return 3

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return False

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.NINTENDO_64
