from typing import Final

from .absJtechHdmiMatrixService import AbsJtechHdmiMatrixService
from ..configuration.serialJtechHdmiMatrixConfiguration import SerialJtechHdmiMatrixConfiguration
from ...consoles.absConsoleConfiguration import AbsConsoleConfiguration
from ...retroTink.retroTinkConfiguration import RetroTinkConfiguration


class SerialJtechHdmiMatrixService(AbsJtechHdmiMatrixService):

    def __init__(
        self,
        retroTinkConfiguration: RetroTinkConfiguration,
        configuration: SerialJtechHdmiMatrixConfiguration,
        sleepDuration: float = 0.25,
        readBytes: int = 100,
    ):
        self.__retroTinkConfiguration: Final[RetroTinkConfiguration] = retroTinkConfiguration
        self.__configuration: Final[SerialJtechHdmiMatrixConfiguration] = configuration
        self.__sleepDuration: Final[float] = sleepDuration
        self.__readBytes: Final[int] = readBytes

    def applyConfiguration(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
    ):
        # TODO
        pass
