import serial
import sys
import time
from typing import Any


# the Extron MVX 84 VGA uses a baud rate of 9600
BAUD_RATE = 9600

# Replace "COM3" with the appropriate COM port
COM_PORT = "COM4"

def sendCommand(command: str):
    """Send a command to the Extron MVX 84 VGA A."""
    try:
        with serial.Serial(COM_PORT, BAUD_RATE, timeout = 1) as ser:
            ser.write(command.encode('utf-8') + b'\r') # Append carriage return
            time.sleep(0.2) # Wait for the device to process
            response = ser.read(100) # Read up to 100 bytes
            print("Response:", response.decode('utf-8', errors = 'ignore'))
    except serial.SerialException as e:
        print("Serial connection error:", e)

if __name__ == "__main__":
    arguments: list[str] | Any | None = sys.argv
    presetNumber: int

    if isinstance(arguments, list) and len(arguments) >= 2:
        presetNumberArgument: str | Any | None = arguments[1]

        try:
            presetNumber = int(presetNumberArgument)
        except Exception as e:
            raise RuntimeError(f"Preset number parse error ({presetNumberArgument=}) ({arguments=}): {e}")

        if presetNumber < 0 or presetNumber > 8:
            raise RuntimeError(f"Preset number is out of bounds ({presetNumber=}) ({presetNumberArgument=}) ({arguments=})")
    else:
        raise RuntimeError(f"No preset number argument specified ({arguments=})")

    fullCommand = f"{presetNumber}."
    sendCommand(fullCommand)
