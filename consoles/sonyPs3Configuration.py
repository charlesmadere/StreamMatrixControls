from dataclasses import dataclass

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True, slots = True)
class SonyPs3Configuration(AbsConsoleConfiguration):

    @property
    def extronHdmiPreset(self) -> int:
        raise NotImplementedError()

    @property
    def extronVgaPreset(self) -> int:
        return 7

    @property
    def jtechHdmiPort(self) -> int:
        return 8

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return False

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.SONY_PS3
