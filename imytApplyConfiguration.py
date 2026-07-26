from typing import Final

from consoles.consoleConfiguration import ConsoleConfiguration
from extronHdmiMatrix.configuration.serialExtronHdmiMatrixConfiguration import SerialExtronHdmiMatrixConfiguration
from extronHdmiMatrix.service.absExtronHdmiMatrixService import AbsExtronHdmiMatrixService
from extronHdmiMatrix.service.serialExtronHdmiMatrixService import SerialExtronHdmiMatrixService
from extronVgaMatrix.configuration.serialExtronVgaMatrixConfiguration import SerialExtronVgaMatrixConfiguration
from extronVgaMatrix.service.absExtronVgaMatrixService import AbsExtronVgaMatrixService
from extronVgaMatrix.service.serialExtronVgaMatrixService import SerialExtronVgaMatrixService
from retroTink.retroTinkConfiguration import RetroTinkConfiguration


extronVgaMatrixConfiguration = SerialExtronVgaMatrixConfiguration()

extronVgaMatrixService: Final[AbsExtronVgaMatrixService] = SerialExtronVgaMatrixService(
    configuration = extronVgaMatrixConfiguration,
)

retroTinkConfiguration = RetroTinkConfiguration()

extronHdmiMatrixConfiguration = SerialExtronHdmiMatrixConfiguration()

extronHdmiMatrixService: Final[AbsExtronHdmiMatrixService] = SerialExtronHdmiMatrixService(
    configuration = extronHdmiMatrixConfiguration,
)

def applyConfiguration(consoleConfiguration: ConsoleConfiguration):
    extronVgaMatrixService.applyConfiguration(consoleConfiguration)
    extronHdmiMatrixService.applyConfiguration(consoleConfiguration)
    print(f'Finished applying console configuration ({consoleConfiguration=})')
