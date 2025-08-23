from dataclasses import dataclass

from .whichConsole import WhichConsole


@dataclass(frozen = True)
class ConsoleConfiguration:
    usesRetroTinkPassThrough: bool
    extronPreset: int
    hdmiPort: int
    whichConsole: WhichConsole
