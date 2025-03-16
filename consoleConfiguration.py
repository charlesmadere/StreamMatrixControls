from enum import Enum, auto


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
