from dataclasses import dataclass

from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.whichConsole import WhichConsole


@dataclass(frozen = True, slots = True)
class MegaSgConfiguration(ConsoleConfiguration):

    @property
    def extronHdmiPreset(self) -> int:
        return 1

    @property
    def extronVgaPreset(self) -> int:
        return 2

    @property
    def jtechHdmiPort(self) -> int:
        return 8

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        return False

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.MEGA_SG
