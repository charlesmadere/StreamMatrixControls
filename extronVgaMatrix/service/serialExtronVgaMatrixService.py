import time
from typing import Final

import serial

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from extronVgaMatrix.configuration.serialExtronVgaMatrixConfiguration import SerialExtronVgaMatrixConfiguration
from extronVgaMatrix.service.absExtronVgaMatrixService import AbsExtronVgaMatrixService


class SerialExtronVgaMatrixService(AbsExtronVgaMatrixService):

    def __init__(
        self,
        configuration: SerialExtronVgaMatrixConfiguration,
        sleepDurationSeconds: float = 0.25,
        timeoutDurationSeconds: float = 1.0,
        readBytes: int = 100,
    ):
        self.__configuration: Final[SerialExtronVgaMatrixConfiguration] = configuration
        self.__sleepDurationSeconds: Final[float] = sleepDurationSeconds
        self.__timeoutDurationSeconds: Final[float] = timeoutDurationSeconds
        self.__readBytes: Final[int] = readBytes

    def applyConfiguration(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
    ):
        command = self.__buildCommand(
            consoleConfiguration = consoleConfiguration,
        )

        try:
            with serial.Serial(
                port = self.__configuration.comPort,
                baudrate = self.__configuration.baudRate,
                timeout = self.__timeoutDurationSeconds,
            ) as connection:
                connection.write(command)

                # wait a moment for the VGA Matrix to process
                time.sleep(self.__sleepDurationSeconds)

                # read some of the response bytes
                responseBytes = connection.read(self.__readBytes)

                # decode the response for readability and logging
                response = responseBytes.decode(encoding = 'utf-8', errors = 'ignore')

                print(f'Extron VGA Matrix response ({consoleConfiguration=}) ({command=}) ({response=})')
        except Exception as e:
            print(f'Extron VGA Matrix connection error ({self.__configuration=}) ({consoleConfiguration=}):', e)
            raise e

    def __buildCommand(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
    ) -> bytes:
        # append carriage return
        return f'{consoleConfiguration.extronPreset}.'.encode('utf-8') + b'\r'
