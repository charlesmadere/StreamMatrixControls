from dataclasses import dataclass
from typing import Final

from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.whichConsole import WhichConsole
from imytApplyConfiguration import applyConfiguration


@dataclass(frozen = True, slots = True)
class NtMiniNoirConfiguration(ConsoleConfiguration):

    @property
    def extronHdmiPreset(self) -> int:
        return 1

    @property
    def extronVgaPreset(self) -> int:
        return 1

    @property
    def jtechHdmiPort(self) -> int:
        raise NotImplementedError()

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        raise NotImplementedError()

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.NT_MINI_NOIR

consoleConfiguration: Final[ConsoleConfiguration] = NtMiniNoirConfiguration()
applyConfiguration(consoleConfiguration)
