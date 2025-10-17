from abc import ABC, abstractmethod

from consoles.whichConsole import WhichConsole


class AbsConsoleConfiguration(ABC):

    @abstractmethod
    def getExtronPreset(self) -> int:
        pass

    @abstractmethod
    def getHdmiPort(self) -> int:
        pass

    @abstractmethod
    def getWhichConsole(self) -> WhichConsole:
        pass

    @property
    @abstractmethod
    def usesRetroTinkPassThrough(self) -> bool:
        pass
