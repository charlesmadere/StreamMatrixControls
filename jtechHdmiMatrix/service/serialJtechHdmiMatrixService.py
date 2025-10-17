import time
from typing import Final

import serial

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from jtechHdmiMatrix.configuration.serialJtechHdmiMatrixConfiguration import SerialJtechHdmiMatrixConfiguration
from jtechHdmiMatrix.service.absJtechHdmiMatrixService import AbsJtechHdmiMatrixService
from retroTink.retroTinkConfiguration import RetroTinkConfiguration


class SerialJtechHdmiMatrixService(AbsJtechHdmiMatrixService):

    def __init__(
        self,
        retroTinkConfiguration: RetroTinkConfiguration,
        configuration: SerialJtechHdmiMatrixConfiguration,
        sleepDuration: float = 0.25,
        readBytes: int = 64,
    ):
        self.__retroTinkConfiguration: Final[RetroTinkConfiguration] = retroTinkConfiguration
        self.__configuration: Final[SerialJtechHdmiMatrixConfiguration] = configuration
        self.__sleepDuration: Final[float] = sleepDuration
        self.__readBytes: Final[int] = readBytes

    def applyConfiguration(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
    ):
        try:
            with serial.Serial(
                self.__configuration.comPort,
                self.__configuration.baudRate,
                timeout = 1,
            ) as connection:
                for outputPortIndex in range(self.__configuration.portCount):
                    serialCommand = self.__buildSerialCommand(
                        consoleConfiguration = consoleConfiguration,
                        outputPortIndex = outputPortIndex,
                    )

                    connection.write(serialCommand)

                    # wait a moment for the HDMI Matrix to process
                    time.sleep(self.__sleepDuration)

                    # read some of the response bytes
                    responseBytes = connection.read(self.__readBytes)

                    # decode the response for readability and logging
                    response = responseBytes.decode(encoding = 'utf-8', errors = 'ignore')

                    print(f'JTech HDMI Matrix response ({outputPortIndex=}) ({consoleConfiguration=}): {response}')
        except Exception as e:
            print(f'JTech HDMI Matrix connection error ({self.__configuration=}) ({consoleConfiguration=}):', e)
            raise e

    def __buildSerialCommand(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
        outputPortIndex: int,
    ) -> bytes:
        inputPort: int

        if consoleConfiguration.usesRetroTinkPassThrough() and (outputPortIndex + 1) != self.__retroTinkConfiguration.hdmiPort:
            inputPort = self.__retroTinkConfiguration.hdmiPort
        else:
            inputPort = consoleConfiguration.getHdmiPort()

        # convert the HDMI port number to be 0 based (port 1 is actually port 0)
        inputPortIndex = inputPort - 1

        # convert the HDMI port number into the required string format
        outputPortIndexString = f'{outputPortIndex:02}'
        inputPortIndexString = f'{inputPortIndex:02}'

        # append carriage return
        return f'@T {outputPortIndexString} {inputPortIndexString} #'.encode('utf-8') + b'\r'
