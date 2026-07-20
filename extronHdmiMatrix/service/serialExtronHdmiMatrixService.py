import time
from typing import Final

import serial

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from extronHdmiMatrix.configuration.serialExtronHdmiMatrixConfiguration import SerialExtronHdmiMatrixConfiguration
from extronHdmiMatrix.service.absExtronHdmiMatrixService import AbsExtronHdmiMatrixService


class SerialExtronHdmiMatrixService(AbsExtronHdmiMatrixService):

    def __init__(
        self,
        configuration: SerialExtronHdmiMatrixConfiguration,
        sleepDurationSeconds: float = 0.25,
        timeoutDurationSeconds: float = 1.0,
        readBytes: int = 100,
    ):
        self.__configuration: Final[SerialExtronHdmiMatrixConfiguration] = configuration
        self.__sleepDurationSeconds: Final[float] = sleepDurationSeconds
        self.__timeoutDurationSeconds: Final[float] = timeoutDurationSeconds
        self.__readBytes: Final[int] = readBytes

    def applyConfiguration(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
    ):
        try:
            with serial.Serial(
                port = self.__configuration.comPort,
                baudrate = self.__configuration.baudRate,
                timeout = self.__timeoutDurationSeconds,
            ) as serialConnection:
                self.__applyConfiguration(
                    consoleConfiguration = consoleConfiguration,
                    serialConnection = serialConnection,
                )
        except Exception as e:
            print(f'Extron HDMI Matrix connection error ({self.__configuration=}) ({consoleConfiguration=}):', e)
            raise e

    def __applyConfiguration(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
        serialConnection: serial.Serial,
    ):
        serialCommand = f'{consoleConfiguration.extronHdmiPreset}.'
        serialConnection.write(serialCommand.encode('utf-8') + b'\r')

        # wait a moment for the HDMI Matrix to process
        time.sleep(self.__sleepDurationSeconds)

        # read some of the response bytes
        responseBytes = serialConnection.read(self.__readBytes)

        # decode the response for readability and logging
        response = responseBytes.decode(encoding = 'utf-8', errors = 'ignore')

        print(f'Extron HDMI Matrix response ({consoleConfiguration=}) ({serialCommand=}) ({response=})')
