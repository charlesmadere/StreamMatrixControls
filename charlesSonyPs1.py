from typing import Final

from charlesApplyConfiguration import applyConfiguration
from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.sonyPs1Configuration import SonyPs1Configuration

consoleConfiguration: Final[ConsoleConfiguration] = SonyPs1Configuration()
applyConfiguration(consoleConfiguration)
