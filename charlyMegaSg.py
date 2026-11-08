from typing import Final

from charlyApplyConfiguration import applyConfiguration
from consoles.consoleConfiguration import ConsoleConfiguration
from consoles.megaSgConfiguration import MegaSgConfiguration

consoleConfiguration: Final[ConsoleConfiguration] = MegaSgConfiguration()
applyConfiguration(consoleConfiguration)
