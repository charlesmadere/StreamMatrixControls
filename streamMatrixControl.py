import random
import re
import sys
import time
from datetime import datetime, timezone
from typing import Any

import requests
import serial

from consoleConfiguration import ConsoleConfiguration

HDMI_MATRIX_ADDRESS = "http://192.168.1.7"

# the Extron MVX 84 VGA uses a baud rate of 9600
BAUD_RATE = 9600

# the Extron MVX 84 VGA is currently using COM4 on my system
COM_PORT = "COM3"

# small amount of buffer time to allow external devices to process
SLEEP_DURATION = 0.2

def determineConsoleConfiguration(consoleArgument: str) -> ConsoleConfiguration | None:
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
        return None

def setHdmiMatrixConfiguration(configuration: ConsoleConfiguration):
    ports: list[int] = [ 6, 7, 8 ]

    try:
        for port in ports:
            randomNumber = random.random()
            hdmiMatrixUrl = f'{HDMI_MATRIX_ADDRESS}/@PORT{port}={configuration.hdmiPort}.{randomNumber}'
            now = datetime.now(timezone.utc)

            cookies: dict[str, Any] = {
                'State': f'1,{now.hour}:{now.minute}:{now.second}'
            }

            response = requests.get(
                url = hdmiMatrixUrl,
                cookies = cookies
            )

            print(f"HDMI Matrix response (port {port}): {response}")
            time.sleep(SLEEP_DURATION) # Wait for the device to process
    except Exception as e:
        print(f"HDMI Matrix connection error ({HDMI_MATRIX_ADDRESS=}) ({configuration=}):", e)
        raise e

def setVgaMatrixConfiguration(configuration: ConsoleConfiguration):
    extronCommand = f'{configuration.extronPreset}.'

    try:
        with serial.Serial(COM_PORT, BAUD_RATE, timeout = 1) as ser:
            ser.write(extronCommand.encode("utf-8") + b'\r') # Append carriage return
            time.sleep(SLEEP_DURATION) # Wait for the device to process
            response = ser.read(100) # Read up to 100 bytes
            print("Extron response:", response.decode('utf-8', errors = 'ignore'))
    except serial.SerialException as e:
        print(f"Extron connection error ({COM_PORT=}) ({BAUD_RATE=}) ({configuration=}) ({extronCommand=}):", e)
        raise e

def applyConsoleConfiguration(configuration: ConsoleConfiguration) -> bool:
    print(f'Applying console configuration ({configuration=})')

    try:
        setHdmiMatrixConfiguration(configuration)
        setVgaMatrixConfiguration(configuration)
    except Exception as e:
        print(f"Encountered error during console configuration ({configuration=}):", e)
        return False

    print(f'Finished applying console configuration ({configuration=})')
    return True

if __name__ == "__main__":
    arguments: list[str] | Any | None = sys.argv

    if not isinstance(arguments, list) or len(arguments) < 2:
        raise RuntimeError(f"Console configuration argument is not set ({arguments=})")

    consoleArgument: str | Any | None = ' '.join(arguments[1:]).strip()

    if not isinstance(consoleArgument, str) or len(consoleArgument) == 0 or consoleArgument.isspace():
        raise RuntimeError(f"Console configuration argument is malformed ({consoleArgument=}) ({arguments=})")

    consoleConfiguration = determineConsoleConfiguration(consoleArgument)

    if consoleConfiguration is None:
        raise RuntimeError(f'Console configuration argument doesn\'t match any console ({consoleArgument=}) ({arguments=})')

    applyConsoleConfiguration(consoleConfiguration)
