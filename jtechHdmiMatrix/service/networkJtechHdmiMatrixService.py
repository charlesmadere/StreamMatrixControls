import random
import time
from datetime import datetime, timezone
from typing import Any, Final

import requests

from .absJtechHdmiMatrixService import AbsJtechHdmiMatrixService
from ..configuration.networkJtechHdmiMatrixConfiguration import NetworkJtechHdmiMatrixConfiguration
from ...consoles.consoleConfiguration import ConsoleConfiguration
from ...retroTink.retroTinkConfiguration import RetroTinkConfiguration


class NetworkJtechHdmiMatrixService(AbsJtechHdmiMatrixService):

    def __init__(
        self,
        configuration: NetworkJtechHdmiMatrixConfiguration,
        retroTinkConfiguration: RetroTinkConfiguration,
        sleepDuration: float = 0.2,
        timeZone: timezone = timezone.utc,
    ):
        self.__configuration: Final[NetworkJtechHdmiMatrixConfiguration] = configuration
        self.__retroTinkConfiguration: Final[RetroTinkConfiguration] = retroTinkConfiguration
        self.__sleepDuration: Final[float] = sleepDuration
        self.__timeZone: Final[timezone] = timeZone

    def applyConfiguration(
        self,
        consoleConfiguration: ConsoleConfiguration,
    ):
        if consoleConfiguration.hdmiPort > self.__configuration.portCount:
            return

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

                print(f'JTech HDMI Matrix response ({actualPortIndex=}) ({consoleConfiguration=}): {response}')

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
        consoleConfiguration: ConsoleConfiguration,
        portIndex: int,
    ) -> str:
        randomNumber = random.random()
        hdmiPort: int

        if consoleConfiguration.usesRetroTinkPassThrough and portIndex != self.__retroTinkConfiguration.hdmiPort:
            hdmiPort = self.__retroTinkConfiguration.hdmiPort
        else:
            hdmiPort = consoleConfiguration.hdmiPort

        return f'{self.__configuration.ipAddress}/@PORT{portIndex}={hdmiPort}.{randomNumber}'
