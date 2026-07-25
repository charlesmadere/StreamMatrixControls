from dataclasses import dataclass

from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True, slots = True)
class SonyPs1Configuration(ConsoleConfiguration):

    @property
    def extronHdmiPreset(self) -> int:
        raise NotImplementedError()

    @property
    def extronVgaPreset(self) -> int:
        return 4

    @property
    def jtechHdmiPort(self) -> int:
        return 2

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return False

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.SONY_PS1
