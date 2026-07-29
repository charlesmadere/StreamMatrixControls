from typing import Final

from consoles.consoleConfiguration import ConsoleConfiguration
from extronHdmiMatrix.configuration.networkExtronHdmiMatrixConfiguration import NetworkExtronHdmiMatrixConfiguration
from extronHdmiMatrix.service.absExtronHdmiMatrixService import AbsExtronHdmiMatrixService
from extronHdmiMatrix.service.networkExtronHdmiMatrixService import NetworkExtronHdmiMatrixService
from extronVgaMatrix.configuration.serialExtronVgaMatrixConfiguration import SerialExtronVgaMatrixConfiguration
from extronVgaMatrix.service.absExtronVgaMatrixService import AbsExtronVgaMatrixService
from extronVgaMatrix.service.serialExtronVgaMatrixService import SerialExtronVgaMatrixService
from retroTink.retroTinkConfiguration import RetroTinkConfiguration


extronVgaMatrixConfiguration = SerialExtronVgaMatrixConfiguration(
    comPort = 'COM5',
)

extronVgaMatrixService: Final[AbsExtronVgaMatrixService] = SerialExtronVgaMatrixService(
    configuration = extronVgaMatrixConfiguration,
)

retroTinkConfiguration = RetroTinkConfiguration()

extronHdmiMatrixConfiguration = NetworkExtronHdmiMatrixConfiguration()

extronHdmiMatrixService: Final[AbsExtronHdmiMatrixService] = NetworkExtronHdmiMatrixService(
    configuration = extronHdmiMatrixConfiguration,
)

def applyConfiguration(consoleConfiguration: ConsoleConfiguration):
    extronVgaMatrixService.applyConfiguration(consoleConfiguration)
    extronHdmiMatrixService.applyConfiguration(consoleConfiguration)
    print(f'Finished applying console configuration ({consoleConfiguration=})')
