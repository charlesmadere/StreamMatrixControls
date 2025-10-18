from consoles.absConsoleConfiguration import AbsConsoleConfiguration
from extronVgaMatrix.configuration.serialExtronVgaMatrixConfiguration import SerialExtronVgaMatrixConfiguration
from extronVgaMatrix.service.absExtronVgaMatrixService import AbsExtronVgaMatrixService
from extronVgaMatrix.service.serialExtronVgaMatrixService import SerialExtronVgaMatrixService
from jtechHdmiMatrix.configuration.serialJtechHdmiMatrixConfiguration import SerialJtechHdmiMatrixConfiguration
from jtechHdmiMatrix.service.absJtechHdmiMatrixService import AbsJtechHdmiMatrixService
from jtechHdmiMatrix.service.serialJtechHdmiMatrixService import SerialJtechHdmiMatrixService
from retroTink.retroTinkConfiguration import RetroTinkConfiguration


extronVgaMatrixConfiguration = SerialExtronVgaMatrixConfiguration()

extronVgaMatrixService: AbsExtronVgaMatrixService = SerialExtronVgaMatrixService(
    configuration = extronVgaMatrixConfiguration,
)

retroTinkConfiguration = RetroTinkConfiguration()

jtechHdmiMatrixConfiguration = SerialJtechHdmiMatrixConfiguration()

jtechHdmiMatrixService: AbsJtechHdmiMatrixService = SerialJtechHdmiMatrixService(
    configuration = jtechHdmiMatrixConfiguration,
    retroTinkConfiguration = retroTinkConfiguration,
)

def applyConfiguration(consoleConfiguration: AbsConsoleConfiguration):
    extronVgaMatrixService.applyConfiguration(consoleConfiguration)
    jtechHdmiMatrixService.applyConfiguration(consoleConfiguration)
    print(f'Finished applying console configuration ({consoleConfiguration=})')
