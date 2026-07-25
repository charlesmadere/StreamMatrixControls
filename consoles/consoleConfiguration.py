from abc import ABC, abstractmethod

from consoles.whichConsole import WhichConsole


class ConsoleConfiguration(ABC):

    @property
    @abstractmethod
    def extronHdmiPreset(self) -> int:
        pass

    @property
    @abstractmethod
    def extronVgaPreset(self) -> int:
        pass

    @property
    @abstractmethod
    def jtechHdmiPort(self) -> int:
        pass

    @property
    @abstractmethod
    def usesRetroTinkPassThrough(self) -> bool:
        pass

    @property
    @abstractmethod
    def whichConsole(self) -> WhichConsole:
        pass
