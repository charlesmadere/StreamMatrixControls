import socket
import time
from typing import Final

import serial

from consoles.consoleConfiguration import ConsoleConfiguration
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
        consoleConfiguration: ConsoleConfiguration,
    ):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketConnection:
                socketConnection.connect(('192.168.1.249', 23))
                self.__applyConfiguration(
                    consoleConfiguration = consoleConfiguration,
                    socketConnection = socketConnection,
                )
        except Exception as e:
            print(f'Extron HDMI Matrix connection error ({self.__configuration=}) ({consoleConfiguration=}):', e)
            raise e

    def __applyConfiguration(
        self,
        consoleConfiguration: ConsoleConfiguration,
        socketConnection: socket.socket,
    ):
        # 1. Appended \r to act as an "Enter" key for the command parser
        ipCommand = f'{consoleConfiguration.extronHdmiPreset}.\r'

        # 2. Use sendall() for TCP sockets instead of write()
        socketConnection.sendall(ipCommand.encode('ascii'))

        # 3. Use recv() to read the response buffer.
        # This will block until the matrix replies or the socket times out.
        responseBytes = socketConnection.recv(1024)

        # 4. Decode and strip whitespace/newlines for logging
        response = responseBytes.decode(encoding = 'ascii', errors = 'ignore').strip()

        print(f'Extron HDMI Matrix response ({consoleConfiguration=}) ({ipCommand=}) ({response=})')
