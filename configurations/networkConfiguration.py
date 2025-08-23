from abc import ABC, abstractmethod


class NetworkConfiguration(ABC):

    @abstractmethod
    def getIpAddress(self) -> str:
        pass
