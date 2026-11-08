from typing import Final

from charlyApplyConfiguration import applyConfiguration
from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.switch2Configuration import Switch2Configuration

consoleConfiguration: Final[ConsoleConfiguration] = Switch2Configuration()
applyConfiguration(consoleConfiguration)
