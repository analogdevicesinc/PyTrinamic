from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC7300
from pytrinamic.features import MotorControlModule
from pytrinamic.helpers import TMC_helpers


class TMC7300_eval(TMCLEval):
    """
    This class represents a TMC7300 Evaluation board.

    Communication is done over the TMCL commands writeDRV and readDRV. An
    implementation without TMCL may still use this class if these two functions
    are provided properly. See __init__ for details on the function
    requirements.
    """
    
    def __init__(self, connection, module_id=1):
        """
        Parameters:
            connection:
                Type: class
                A class that provides the necessary functions for communicating
                with a TMC7300. The required functions are
                    connection.writeDRV(registerAddress, value, moduleID)
                    connection.readDRV(registerAddress, moduleID, signed)
                for writing/reading to register of the TMC7300.
            module_id:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC7300. This ID is used as a
                parameter for the writeDRV and readDRV functions.
        """
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC7300(connection)]

    # Use the driver controller channel for register access

    def write_register(self, register_address, value):
        return self._connection.write_drv(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_drv(register_address, self._module_id, signed)

    # Motion control functions

    def rotate(self, motor, value):
        self._connection.rotate(motor, value)
    
    def stop(self, motor):
        self._connection.stop(motor)

    class _MotorTypeA(MotorControlModule):
        def __init__(self, eval_board, axis):
            MotorControlModule.__init__(self, eval_board, axis, self.AP)

        def set_standby_current(self, value):
            self.set_axis_parameter(self.AP.ICStandby, value)

        class AP:
            PWMDutyA                       = 0
            PWMDutyB                       = 1
            MaxCurrent                     = 6
            ICStandby                      = 7
            PWMTwoMotors                   = 8
            ChopperBlankTime               = 162
            PWMFrequency                   = 191
            PWMAutoscale                   = 192
            FreewheelingMode               = 204
