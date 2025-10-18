import time
from typing import Final

import serial
from serial import SerialBase

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from jtechHdmiMatrix.configuration.serialJtechHdmiMatrixConfiguration import SerialJtechHdmiMatrixConfiguration
from jtechHdmiMatrix.service.absJtechHdmiMatrixService import AbsJtechHdmiMatrixService
from retroTink.retroTinkConfiguration import RetroTinkConfiguration


class SerialJtechHdmiMatrixService(AbsJtechHdmiMatrixService):

    def __init__(
        self,
        retroTinkConfiguration: RetroTinkConfiguration,
        configuration: SerialJtechHdmiMatrixConfiguration,
        sleepDurationSeconds: float = 0.25,
        timeoutDurationSeconds: float = 1.0,
        readBytes: int = 64,
    ):
        self.__retroTinkConfiguration: Final[RetroTinkConfiguration] = retroTinkConfiguration
        self.__configuration: Final[SerialJtechHdmiMatrixConfiguration] = configuration
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
            print(f'JTech HDMI Matrix connection error ({self.__configuration=}) ({consoleConfiguration=}):', e)
            raise e

    def __applyConfiguration(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
        serialConnection: SerialBase,
    ):
        serialCommand = f'@T {4:02}'

        for outputPortIndex in range(self.__configuration.portCount):
            inputPortIndex: int

            if consoleConfiguration.usesRetroTinkPassThrough and (outputPortIndex + 1 != self.__retroTinkConfiguration.outputHdmiPort):
                inputPortIndex = self.__retroTinkConfiguration.inputHdmiPort
            else:
                inputPortIndex = consoleConfiguration.hdmiPort

            # convert the HDMI port number to be 0 based (port 1 is actually port 0)
            inputPortIndex = inputPortIndex - 1

            serialCommand += f' {inputPortIndex:02}'

        serialCommand += ' #'
        serialConnection.write(serialCommand.encode('utf-8') + b'\r')

        # wait a moment for the HDMI Matrix to process
        time.sleep(self.__sleepDurationSeconds)

        # read some of the response bytes
        responseBytes = serialConnection.read(self.__readBytes)

        # decode the response for readability and logging
        response = responseBytes.decode(encoding = 'utf-8', errors = 'ignore')

        print(f'JTech HDMI Matrix response ({consoleConfiguration=}) ({serialCommand=}) ({response=})')
