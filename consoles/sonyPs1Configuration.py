from dataclasses import dataclass

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True)
class SonyPs1Configuration(AbsConsoleConfiguration):

    @property
    def extronPreset(self) -> int:
        return 4

    @property
    def hdmiPort(self) -> int:
        return 2

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return False

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.SONY_PS1
