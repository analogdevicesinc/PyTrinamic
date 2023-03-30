from ..modules import TMCLModule

# features
from ..features import MotorControlModule, DriveSettingModule, LinearRampModule
from ..features import StallGuard2Module, CoolStepModule


class TMCM1230(TMCM1231):
    """
    The TMCM-1230 is a  single axis controller/driver module for 2-phase bipolar stepper motors.
    """
    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.name = "TMCM-1230"
        self.desc = self.__doc__
        self.motors = [self._MotorTypeA(self, 0)]
