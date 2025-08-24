import time
from typing import Final

import serial

from .absExtronVgaMatrixService import AbsExtronVgaMatrixService
from ..configuration.serialExtronVgaMatrixConfiguration import SerialExtronVgaMatrixConfiguration
from ...consoles.consoleConfiguration import ConsoleConfiguration


class SerialExtronVgaMatrixService(AbsExtronVgaMatrixService):

    def __init__(
        self,
        configuration: SerialExtronVgaMatrixConfiguration,
        sleepDuration: float = 0.25,
        readBytes: int = 100,
    ):
        self.__configuration: Final[SerialExtronVgaMatrixConfiguration] = configuration
        self.__sleepDuration: Final[float] = sleepDuration
        self.__readBytes: Final[int] = readBytes

    def applyConfiguration(
        self,
        consoleConfiguration: ConsoleConfiguration,
    ):
        command = self.__buildCommand(
            consoleConfiguration = consoleConfiguration,
        )

        try:
            with serial.Serial(
                self.__configuration.comPort,
                self.__configuration.baudRate,
                timeout = 1,
            ) as connection:
                connection.write(command)

                # wait a moment for the VGA Matrix to process
                time.sleep(self.__sleepDuration)

                # read up to 100 bytes
                responseBytes = connection.read(self.__readBytes)

                # decode the response for readability and logging
                response = responseBytes.decode(encoding = 'utf-8', errors = 'ignore')

                print(f'Extron VGA Matrix response ({consoleConfiguration=}): {response}')
        except Exception as e:
            print(f'Extron VGA Matrix connection error ({self.__configuration=}) ({consoleConfiguration=}):', e)
            raise e

    def __buildCommand(
        self,
        consoleConfiguration: ConsoleConfiguration,
    ) -> bytes:
        # append carriage return
        return f'{consoleConfiguration.extronPreset}.'.encode('utf-8') + b'\r'
