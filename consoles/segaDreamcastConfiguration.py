from dataclasses import dataclass

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True)
class SegaDreamcastConfiguration(AbsConsoleConfiguration):

    @property
    def extronPreset(self) -> int:
        return 6

    @property
    def hdmiPort(self) -> int:
        return 8

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return False

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.SEGA_DREAMCAST
