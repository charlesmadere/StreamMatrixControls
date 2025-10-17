from abc import ABC, abstractmethod

from consoles.absConsoleConfiguration import AbsConsoleConfiguration


class AbsJtechHdmiMatrixService(ABC):

    @abstractmethod
    def applyConfiguration(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
    ):
        pass
