from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.whichConsole import WhichConsole
from imytApplyConfiguration import applyConfiguration


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

consoleConfiguration: ConsoleConfiguration = NtMiniNoirConfiguration()
applyConfiguration(consoleConfiguration)
