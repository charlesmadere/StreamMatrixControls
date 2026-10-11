from dataclasses import dataclass
from typing import Final

from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.whichConsole import WhichConsole
from imytApplyConfiguration import applyConfiguration


@dataclass(frozen = True, slots = True)
class MegaSgConfiguration(ConsoleConfiguration):

    @property
    def extronHdmiPreset(self) -> int:
        return 2

    @property
    def extronVgaPreset(self) -> int:
        return 2

    @property
    def jtechHdmiPort(self) -> int:
        raise NotImplementedError()

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        raise NotImplementedError()

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.MEGA_SG

consoleConfiguration: Final[ConsoleConfiguration] = MegaSgConfiguration()
applyConfiguration(consoleConfiguration)
