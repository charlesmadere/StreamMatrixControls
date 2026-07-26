from typing import Final

from consoles.consoleConfiguration import ConsoleConfiguration
from extronVgaMatrix.configuration.serialExtronVgaMatrixConfiguration import SerialExtronVgaMatrixConfiguration
from extronVgaMatrix.service.absExtronVgaMatrixService import AbsExtronVgaMatrixService
from extronVgaMatrix.service.serialExtronVgaMatrixService import SerialExtronVgaMatrixService
from jtechHdmiMatrix.configuration.serialJtechHdmiMatrixConfiguration import SerialJtechHdmiMatrixConfiguration
from jtechHdmiMatrix.service.absJtechHdmiMatrixService import AbsJtechHdmiMatrixService
from jtechHdmiMatrix.service.serialJtechHdmiMatrixService import SerialJtechHdmiMatrixService
from retroTink.retroTinkConfiguration import RetroTinkConfiguration


extronVgaMatrixConfiguration = SerialExtronVgaMatrixConfiguration(
    comPort = 'COM9',
)

extronVgaMatrixService: Final[AbsExtronVgaMatrixService] = SerialExtronVgaMatrixService(
    configuration = extronVgaMatrixConfiguration,
)

retroTinkConfiguration = RetroTinkConfiguration()

jtechHdmiMatrixConfiguration = SerialJtechHdmiMatrixConfiguration()

jtechHdmiMatrixService: Final[AbsJtechHdmiMatrixService] = SerialJtechHdmiMatrixService(
    configuration = jtechHdmiMatrixConfiguration,
    retroTinkConfiguration = retroTinkConfiguration,
)

def applyConfiguration(consoleConfiguration: ConsoleConfiguration):
    extronVgaMatrixService.applyConfiguration(consoleConfiguration)
    jtechHdmiMatrixService.applyConfiguration(consoleConfiguration)
    print(f'Finished applying console configuration ({consoleConfiguration=})')
