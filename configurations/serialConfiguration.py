from abc import ABC, abstractmethod


class SerialConfiguration(ABC):

    @abstractmethod
    def getBaudRate(self) -> int:
        pass

    @abstractmethod
    def getComPort(self) -> str:
        pass
