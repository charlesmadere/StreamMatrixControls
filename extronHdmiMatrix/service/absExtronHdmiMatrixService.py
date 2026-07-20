from abc import ABC, abstractmethod

from consoles.absConsoleConfiguration import AbsConsoleConfiguration


class AbsExtronHdmiMatrixService(ABC):

    @abstractmethod
    def applyConfiguration(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
    ):
        pass
