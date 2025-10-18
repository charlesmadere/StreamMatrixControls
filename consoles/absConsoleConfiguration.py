from abc import ABC, abstractmethod

from consoles.whichConsole import WhichConsole


class AbsConsoleConfiguration(ABC):

    @property
    @abstractmethod
    def extronPreset(self) -> int:
        pass

    @property
    @abstractmethod
    def hdmiPort(self) -> int:
        pass

    @property
    @abstractmethod
    def usesRetroTinkPassThrough(self) -> bool:
        pass

    @property
    @abstractmethod
    def whichConsole(self) -> WhichConsole:
        pass
