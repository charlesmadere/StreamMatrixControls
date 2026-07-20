from dataclasses import dataclass

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True, slots = True)
class NtMiniNoirConfiguration(AbsConsoleConfiguration):

    @property
    def extronVgaPreset(self) -> int:
        return 1

    @property
    def hdmiPort(self) -> int:
        return 1

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return True

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.NT_MINI_NOIR
