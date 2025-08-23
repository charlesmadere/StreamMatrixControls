from typing import Final

from .absExtronVgaMatrixService import AbsExtronVgaMatrixService
from ..configuration.serialExtronVgaMatrixConfiguration import SerialExtronVgaMatrixConfiguration
from ...consoles.consoleConfiguration import ConsoleConfiguration


class SerialExtronVgaMatrixService(AbsExtronVgaMatrixService):

    def __init__(
        self,
        configuration: SerialExtronVgaMatrixConfiguration,
    ):
        self.__configuration: Final[SerialExtronVgaMatrixConfiguration] = configuration

    def applyConfiguration(
        self,
        consoleConfiguration: ConsoleConfiguration,
    ):
        # TODO
        pass
