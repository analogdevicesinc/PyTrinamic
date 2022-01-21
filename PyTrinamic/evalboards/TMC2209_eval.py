from PyTrinamic.evalboards.tmcl_eval import TMCLEval
from PyTrinamic.ic.TMC2209.TMC2209 import TMC2209
from PyTrinamic.features import MotorControlModule
from PyTrinamic.helpers import TMC_helpers


class TMC2209_eval(TMCLEval, TMC2209):
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
                for writing/reading to registers of the TMC2209.
            module_id:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC2209. This ID is used as a
                parameter for the writeDRV and readDRV functions.
        """
        TMCLEval.__init__(self, connection, module_id)
        TMC2209.__init__(self)
        self.motors = [self.Motor0(self, 0)]

    # Use the driver controller channel for register access

    def write_register(self, register_address, value):
        return self._connection.writeDRV(register_address, value)

    def read_register(self, register_address, signed=False):
        return self._connection.readDRV(register_address, signed)

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

    # Motion control functions

    def rotate(self, axis, value):
        self._connection.rotate(axis, value)

    def stop(self, axis):
        self._connection.stop(axis)

    def move_to(self, axis, position, velocity=None):
        if velocity and velocity != 0:
            self.motors[0].set_axis_parameter(self.motors[0].AP.MaxVelocity, velocity)
        self._connection.moveTo(axis, position, self._module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.motors[0].set_axis_parameter(self.motors[0].AP.MaxVelocity, velocity)
        self._connection.moveBy(axis, difference, self._module_id)

    class Motor0(MotorControlModule):
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
