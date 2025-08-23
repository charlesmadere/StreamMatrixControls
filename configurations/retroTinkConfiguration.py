from dataclasses import dataclass


@dataclass(frozen = True)
class RetroTinkConfiguration:
    hdmiPort: int = 1
