import time
from typing import Final

import serial

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
                for portIndex in range(self.__configuration.portCount):
                    actualPortIndex = portIndex + 1

                    serialCommand = self.__buildSerialCommand(
                        consoleConfiguration = consoleConfiguration,
                        portIndex = actualPortIndex,
                    )

                    connection.write(serialCommand)

                    # wait a moment for the HDMI Matrix to process
                    time.sleep(self.__sleepDuration)

                    # read up to 100 bytes
                    responseBytes = connection.read(self.__readBytes)

                    # decode the response for readability and logging
                    response = responseBytes.decode(encoding = 'utf-8', errors = 'ignore')

                    print(f'JTech HDMI Matrix response ({actualPortIndex=}) ({consoleConfiguration=}): {response}')
        except Exception as e:
            print(f'JTech HDMI Matrix connection error ({self.__configuration=}) ({consoleConfiguration=}):', e)
            raise e

    def __buildSerialCommand(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
        portIndex: int,
    ) -> bytes:
        hdmiPort: int

        if consoleConfiguration.usesRetroTinkPassThrough() and portIndex != self.__retroTinkConfiguration.hdmiPort:
            hdmiPort = self.__retroTinkConfiguration.hdmiPort
        else:
            hdmiPort = consoleConfiguration.getHdmiPort()

        # correct the HDMI port numbers to be 0 based (port 1 is actually port 0)
        portIndex -= 1
        hdmiPort -= 1

        # convert the HDMI port number into the required string format
        portIndexString = f'{portIndex::02}'
        hdmiPortString = f'{hdmiPort:02}'

        # append carriage return
        return f'@T {portIndexString} {hdmiPortString} #'.encode('utf-8') + b'\r'
