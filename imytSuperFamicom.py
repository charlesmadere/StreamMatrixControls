from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.whichConsole import WhichConsole
from imytApplyConfiguration import applyConfiguration


class SuperFamicomConfiguration(ConsoleConfiguration):

    @property
    def extronHdmiPreset(self) -> int:
        return 3

    @property
    def extronVgaPreset(self) -> int:
        return 3

    @property
    def jtechHdmiPort(self) -> int:
        raise NotImplementedError()

    @property
    def usesRetroTinkPassThrough(self) -> bool:
        raise NotImplementedError()

    @property
    def whichConsole(self) -> WhichConsole:
        return WhichConsole.SUPER_FAMICOM

consoleConfiguration: ConsoleConfiguration = SuperFamicomConfiguration()
applyConfiguration(consoleConfiguration)
