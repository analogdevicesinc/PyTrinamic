from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC2209
from pytrinamic.features import MotorControlModule
from pytrinamic.helpers import TMC_helpers


class TMC2209_eval(TMCLEval):
    """
    This class represents a TMC2209 Evaluation board.

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
                with a TMC2209. The required functions are
                    connection.writeDRV(registerAddress, value, moduleID)
                    connection.readDRV(registerAddress, moduleID, signed)
                for writing/reading to register of the TMC2209.
            module_id:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC2209. This ID is used as a
                parameter for the writeDRV and readDRV functions.
        """
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC2209()]

    # Use the driver controller functions for register access

    def write_register(self, register_address, value):
        return self._connection.write_drv(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_drv(register_address, self._module_id, signed)

    # Motion control functions

    def rotate(self, motor, value):
        self._connection.rotate(motor, value)

    def stop(self, motor):
        self._connection.stop(motor)

    def move_to(self, motor, position, velocity=None):
        if velocity and velocity != 0:
            self.motors[motor].set_axis_parameter(self.motors[motor].AP.MaxVelocity, velocity)
        self._connection.move_to(motor, position, self._module_id)

    def move_by(self, motor, distance, velocity=None):
        if velocity:
            self.motors[motor].set_axis_parameter(self.motors[motor].AP.MaxVelocity, velocity)
        self._connection.move_by(motor, distance, self._module_id)

    class _MotorTypeA(MotorControlModule):
        def __init__(self, eval_board, axis):
            MotorControlModule.__init__(self, eval_board, axis, self.AP)

        class AP:
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxAcceleration                = 5
            MaxCurrent                     = 6
            StandbyCurrent                 = 7
            PositionReachedFlag            = 8
            THIGH                          = 23
            internal_Rsense                = 28
            MeasuredSpeed                  = 29
            StepDirSource                  = 50
            StepDirFrequency               = 51
            MicrostepResolution            = 140
            ChopperBlankTime               = 162
            ChopperHysteresisEnd           = 165
            ChopperHysteresisStart         = 166
            TOff                           = 167
            SEIMIN                         = 168
            SECDS                          = 169
            smartEnergyHysteresis          = 170
            SECUS                          = 171
            smartEnergyHysteresisStart     = 172
            SG2Threshold                   = 174
            VSense                         = 179
            smartEnergyActualCurrent       = 180
            smartEnergyStallVelocity       = 181
            smartEnergyThresholdSpeed      = 182
            PWMThresholdSpeed              = 186
            PWMGrad                        = 187
            PWMFrequency                   = 191
            PWMAutoscale                   = 192
            FreewheelingMode               = 204
            LoadValue                      = 206
