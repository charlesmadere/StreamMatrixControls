import random
import time
from datetime import datetime, timezone
from typing import Any, Final

import requests

from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from jtechHdmiMatrix.configuration.networkJtechHdmiMatrixConfiguration import NetworkJtechHdmiMatrixConfiguration
from jtechHdmiMatrix.service.absJtechHdmiMatrixService import AbsJtechHdmiMatrixService
from retroTink.retroTinkConfiguration import RetroTinkConfiguration


class NetworkJtechHdmiMatrixService(AbsJtechHdmiMatrixService):

    def __init__(
        self,
        configuration: NetworkJtechHdmiMatrixConfiguration,
        retroTinkConfiguration: RetroTinkConfiguration,
        sleepDuration: float = 0.25,
        timeZone: timezone = timezone.utc,
    ):
        self.__configuration: Final[NetworkJtechHdmiMatrixConfiguration] = configuration
        self.__retroTinkConfiguration: Final[RetroTinkConfiguration] = retroTinkConfiguration
        self.__sleepDuration: Final[float] = sleepDuration
        self.__timeZone: Final[timezone] = timeZone

    def applyConfiguration(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
    ):
        try:
            for portIndex in range(self.__configuration.portCount):
                actualPortIndex = portIndex + 1

                url = self.__buildUrl(
                    consoleConfiguration = consoleConfiguration,
                    portIndex = actualPortIndex,
                )

                cookies = self.__buildCookies()

                response = requests.get(
                    url = url,
                    cookies = cookies,
                )

                print(f'JTech HDMI Matrix response ({consoleConfiguration=}) ({actualPortIndex=}) ({response=})')

                # wait a moment for the HDMI Matrix to process
                time.sleep(self.__sleepDuration)
        except Exception as e:
            print(f'JTech HDMI Matrix connection error ({self.__configuration=}) ({consoleConfiguration=}):', e)
            raise e

    def __buildCookies(self) -> dict[str, Any]:
        now = datetime.now(self.__timeZone)

        return {
            'State': f'1,{now.hour}:{now.minute}:{now.second}',
        }

    def __buildUrl(
        self,
        consoleConfiguration: AbsConsoleConfiguration,
        portIndex: int,
    ) -> str:
        randomNumber = random.random()
        hdmiPort: int

        if consoleConfiguration.usesRetroTinkPassThrough and portIndex != self.__retroTinkConfiguration.outputHdmiPort:
            hdmiPort = self.__retroTinkConfiguration.inputHdmiPort
        else:
            hdmiPort = consoleConfiguration.hdmiPort

        return f'{self.__configuration.ipAddress}/@PORT{portIndex}={hdmiPort}.{randomNumber}'
