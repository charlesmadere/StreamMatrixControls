from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from extronVgaMatrix.configuration.serialExtronVgaMatrixConfiguration import SerialExtronVgaMatrixConfiguration
from extronVgaMatrix.service.absExtronVgaMatrixService import AbsExtronVgaMatrixService
from extronVgaMatrix.service.serialExtronVgaMatrixService import SerialExtronVgaMatrixService
from jtechHdmiMatrix.configuration.networkJtechHdmiMatrixConfiguration import NetworkJtechHdmiMatrixConfiguration
from jtechHdmiMatrix.service.absJtechHdmiMatrixService import AbsJtechHdmiMatrixService
from jtechHdmiMatrix.service.networkJtechHdmiMatrixService import NetworkJtechHdmiMatrixService
from retroTink.retroTinkConfiguration import RetroTinkConfiguration


extronVgaMatrixConfiguration = SerialExtronVgaMatrixConfiguration()

extronVgaMatrixService: AbsExtronVgaMatrixService = SerialExtronVgaMatrixService(
    configuration = extronVgaMatrixConfiguration,
)

retroTinkConfiguration = RetroTinkConfiguration()

jtechHdmiMatrixConfiguration = NetworkJtechHdmiMatrixConfiguration()

jtechHdmiMatrixService: AbsJtechHdmiMatrixService = NetworkJtechHdmiMatrixService(
    configuration = jtechHdmiMatrixConfiguration,
    retroTinkConfiguration = retroTinkConfiguration,
)

def applyConfiguration(consoleConfiguration: AbsConsoleConfiguration):
    extronVgaMatrixService.applyConfiguration(consoleConfiguration)
    jtechHdmiMatrixService.applyConfiguration(consoleConfiguration)
    print(f'Finished applying console configuration ({consoleConfiguration=})')
