import re
import sys
from typing import Any

from applyConfiguration import applyConfiguration
from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from consoles.gameCubeConfiguration import GameCubeConfiguration
from consoles.megaSgConfiguration import MegaSgConfiguration
from consoles.nintendo64Configuration import Nintendo64Configuration
from consoles.ntMiniNoirConfiguration import NtMiniNoirConfiguration
from consoles.sonyPs1Configuration import SonyPs1Configuration
from consoles.sonyPs3Configuration import SonyPs3Configuration
from consoles.superFamicomConfiguration import SuperFamicomConfiguration


def determineConsoleConfiguration(consoleArgument: str) -> AbsConsoleConfiguration | None:
    if re.fullmatch(r'^\s*game(?:\s+|_|-)?cube\s*$', consoleArgument, re.IGNORECASE):
        return GameCubeConfiguration()

    elif re.fullmatch(r'^\s*mega(?:\s+|_|-)?sg\s*$', consoleArgument, re.IGNORECASE):
        return MegaSgConfiguration()

    elif re.fullmatch(r'^\s*nintendo(?:\s+|_|-)?64\s*$', consoleArgument, re.IGNORECASE):
        return Nintendo64Configuration()

    elif re.fullmatch(r'^\s*nt(?:\s+|_|-)?mini(?:(?:\s+|_|-)noir)?\s*$', consoleArgument, re.IGNORECASE):
        return NtMiniNoirConfiguration()

    elif re.fullmatch(r'^\s*(?:sony(?:\s+|_|-)?)?ps1\s*$', consoleArgument, re.IGNORECASE):
        return SonyPs1Configuration()

    elif re.fullmatch(r'^\s*(?:sony(?:\s+|_|-)?)?ps3\s*$', consoleArgument, re.IGNORECASE):
        return SonyPs3Configuration()

    elif re.fullmatch(r'^\s*super(?:\s+|_|-)?famicom\s*$', consoleArgument, re.IGNORECASE):
        return SuperFamicomConfiguration()

    else:
        return None

if __name__ == "__main__":
    arguments: list[str] | Any | None = sys.argv

    if not isinstance(arguments, list) or len(arguments) < 2:
        raise RuntimeError(f'Console configuration argument is not set ({arguments=})')

    consoleArgument: str | Any | None = ' '.join(arguments[1:]).strip()

    if not isinstance(consoleArgument, str) or len(consoleArgument) == 0 or consoleArgument.isspace():
        raise RuntimeError(f'Console configuration argument is malformed ({consoleArgument=}) ({arguments=})')

    consoleConfiguration = determineConsoleConfiguration(consoleArgument)

    if consoleConfiguration is None:
        raise RuntimeError(f'Console configuration argument doesn\'t match any console ({consoleArgument=}) ({arguments=})')

    applyConfiguration(consoleConfiguration)
    print(f'Finished applying console configuration ({consoleConfiguration=})')
