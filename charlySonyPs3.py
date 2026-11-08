from typing import Final

from charlyApplyConfiguration import applyConfiguration
from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.sonyPs3Configuration import SonyPs3Configuration

consoleConfiguration: Final[ConsoleConfiguration] = SonyPs3Configuration()
applyConfiguration(consoleConfiguration)
