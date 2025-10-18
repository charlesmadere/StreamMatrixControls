from dataclasses import dataclass


@dataclass(frozen = True)
class RetroTinkConfiguration:
    inputHdmiPort: int = 8
    outputHdmiPort: int = 6
