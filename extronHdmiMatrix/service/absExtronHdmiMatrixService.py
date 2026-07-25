from abc import ABC, abstractmethod

from consoles.consoleConfiguration import ConsoleConfiguration


class AbsExtronHdmiMatrixService(ABC):

    @abstractmethod
    def applyConfiguration(
        self,
        consoleConfiguration: ConsoleConfiguration,
    ):
        pass
