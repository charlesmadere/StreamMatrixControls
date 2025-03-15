import random
import re
import requests
import sys
import time
from datetime import datetime, timezone
from enum import Enum, auto
from typing import Any

import serial

HDMI_MATRIX_IP = "192.168.1.7"

# the Extron MVX 84 VGA uses a baud rate of 9600
BAUD_RATE = 9600

# the Extron MVX 84 VGA is currently using COM4 on my system
COM_PORT = "COM4"

class ConsoleConfiguration(Enum):
    GAME_CUBE = auto()
    MEGA_SG = auto()
    NINTENDO_64 = auto()
    NT_MINI_NOIR = auto()
    SONY_PS1 = auto()
    SONY_PS3 = auto()
    SUPER_FAMICOM = auto()

    @property
    def extronPreset(self) -> int:
        match self:
            case ConsoleConfiguration.GAME_CUBE: return 6
            case ConsoleConfiguration.MEGA_SG: return 2
            case ConsoleConfiguration.NINTENDO_64: return 5
            case ConsoleConfiguration.NT_MINI_NOIR: return 1
            case ConsoleConfiguration.SONY_PS1: return 4
            case ConsoleConfiguration.SONY_PS3: return 7
            case ConsoleConfiguration.SUPER_FAMICOM: return 3
            case _: raise ValueError(f'Unknown ConsoleConfiguration value: \"{self}\"')

    @property
    def hdmiPort(self) -> int:
        match self:
            case ConsoleConfiguration.GAME_CUBE: return 5
            case ConsoleConfiguration.MEGA_SG: return 1
            case ConsoleConfiguration.NINTENDO_64: return 4
            case ConsoleConfiguration.NT_MINI_NOIR: return 2
            case ConsoleConfiguration.SONY_PS1: return 3
            case ConsoleConfiguration.SONY_PS3: return 1
            case ConsoleConfiguration.SUPER_FAMICOM: return 1
            case _: raise ValueError(f'Unknown ConsoleConfiguration value: \"{self}\"')

def determineConsoleConfiguration(consoleArgument: str) -> ConsoleConfiguration:
    if re.fullmatch(r'^\s*game(?:\s+|_|-)?cube\s*$', consoleArgument, re.IGNORECASE):
        return ConsoleConfiguration.GAME_CUBE

    elif re.fullmatch(r'^\s*mega(?:\s+|_|-)?sg\s*$', consoleArgument, re.IGNORECASE):
        return ConsoleConfiguration.MEGA_SG

    elif re.fullmatch(r'^\s*nintendo(?:\s+|_|-)?64\s*$', consoleArgument, re.IGNORECASE):
        return ConsoleConfiguration.NINTENDO_64

    elif re.fullmatch(r'^\s*nt(?:\s+|_|-)?mini(?:(?:\s+|_|-)noir)?\s*$', consoleArgument, re.IGNORECASE):
        return ConsoleConfiguration.NT_MINI_NOIR

    elif re.fullmatch(r'^\s*(?:sony(?:\s+|_|-)?)?ps1\s*$', consoleArgument, re.IGNORECASE):
        return ConsoleConfiguration.SONY_PS1

    elif re.fullmatch(r'^\s*(?:sony(?:\s+|_|-)?)?ps3\s*$', consoleArgument, re.IGNORECASE):
        return ConsoleConfiguration.SONY_PS3

    elif re.fullmatch(r'^\s*super(?:\s+|_|-)?famicom\s*$', consoleArgument, re.IGNORECASE):
        return ConsoleConfiguration.SUPER_FAMICOM

    else:
        raise ValueError(f'The given consoleArgument value has no matching ConsoleConfiguration: \"{consoleArgument}\"')

def setHdmiMatrixConfiguration(configuration: ConsoleConfiguration):
    ports: list[int] = [ 6, 7, 8 ]

    try:
        for port in ports:
            randomNumber = random.random()
            hdmiMatrixUrl = f'http://{HDMI_MATRIX_IP}/@PORT{port}={configuration.hdmiPort}.{randomNumber}'
            now = datetime.now(timezone.utc)

            cookies: dict[str, Any] = {
                'State': f'1,{now.hour}:{now.minute}:{now.second}'
            }

            response = requests.get(
                url = hdmiMatrixUrl,
                cookies = cookies
            )

            print(f"HDMI Matrix response (port {port}): {response}")
    except Exception as e:
        print(f"HDMI Matrix connection error ({HDMI_MATRIX_IP=}) ({configuration=}):", e)

def setVgaMatrixConfiguration(configuration: ConsoleConfiguration):
    extronCommand = f'{configuration.extronPreset}.'

    try:
        with serial.Serial(COM_PORT, BAUD_RATE, timeout = 1) as ser:
            ser.write(extronCommand.encode("utf-8") + b'\r') # Append carriage return
            time.sleep(0.2) # Wait for the device to process
            response = ser.read(100) # Read up to 100 bytes
            print("Extron response:", response.decode('utf-8', errors = 'ignore'))
    except serial.SerialException as e:
        print(f"Extron connection error ({COM_PORT=}) ({BAUD_RATE=}) ({configuration=}) ({extronCommand=}):", e)

if __name__ == "__main__":
    arguments: list[str] | Any | None = sys.argv

    if not isinstance(arguments, list) or len(arguments) < 2:
        raise RuntimeError(f"Console configuration argument is not set ({arguments=})")

    consoleArgument: str | Any | None = arguments[1]

    if not isinstance(consoleArgument, str) or len(consoleArgument) == 0 or consoleArgument.isspace():
        raise RuntimeError(f"Console configuration argument is malformed ({consoleArgument=}) ({arguments=})")

    consoleConfiguration = determineConsoleConfiguration(consoleArgument)
    setHdmiMatrixConfiguration(consoleConfiguration)
    setVgaMatrixConfiguration(consoleConfiguration)
