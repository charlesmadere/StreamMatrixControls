from typing import Final

from charlyApplyConfiguration import applyConfiguration
from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.tabletConfiguration import TabletConfiguration

consoleConfiguration: Final[ConsoleConfiguration] = TabletConfiguration()
applyConfiguration(consoleConfiguration)
