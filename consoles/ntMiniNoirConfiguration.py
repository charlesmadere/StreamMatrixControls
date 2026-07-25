from dataclasses import dataclass

from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True, slots = True)
class NtMiniNoirConfiguration(ConsoleConfiguration):

    @property
    def extronHdmiPreset(self) -> int:
        return 2

    @property
    def extronVgaPreset(self) -> int:
        return 1

    @property
    def jtechHdmiPort(self) -> int:
        return 1

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return True

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.NT_MINI_NOIR
