from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC5160
from pytrinamic.features import MotorControlModule
from pytrinamic.helpers import TMC_helpers
from pytrinamic.tmcl import TMCLCommand


class TMC5160_shield(TMCLEval):
    """
    This class represents a TMC5160 Evaluation Shield.

    Communication is done over the TMCL commands writeMC and readMC,
    wrapped in writeRegister and readRegister respectively.
    In the wrapper function, an additional channel number can be assigned to
    distinguish between 3+ ICs. An implementation without TMCL may still use
    this class if these two functions are provided properly. See __init__ for
    details on the function requirements.
    """
    def __init__(self, connection, channel=0, module_id=1):
        """
        Parameters:
            connection:
                Type: class
                A class that provides the necessary functions for communicating
                with a TMC5160. The required functions are
                    connection.writeRegister(registerAddress, command, channel, value, moduleID)
                    connection.readRegister(registerAddress, command, channel, moduleID, signed)
                for writing/reading to register of the TMC5160.
            channel:
                Type: int
                IC index for the given module. It is used to distinguish between
                multiple ICs of the same type on a single module.
            module_id:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC5160. This ID is used as a
                parameter for the writeRegister and readRegister functions.
        """
        TMCLEval.__init__(self, connection, module_id)
        self.__channel = channel
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC5160()]

    # Use the motion controller functions for register access
    def write_register(self, register_address, value):
        return self._connection.write_register(register_address, TMCLCommand.WRITE_MC, self.__channel, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_register(register_address, TMCLCommand.READ_MC, self.__channel, self._module_id, signed)

    # Motion control functions

    def rotate(self, motor, value):
        self._connection.rotate(motor, value)

    def stop(self, motor):
        self._connection.stop(motor)

    def move_to(self, motor, position, velocity=None):
        if velocity and velocity != 0:
            # Set maximum positioning velocity
            self.motors[motor].set_axis_parameter(self.motors[motor].AP.MaxVelocity, velocity)
        self._connection.move_to(motor, position, self._module_id)

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
            RightEndstop                   = 10
            LeftEndstop                    = 11
            AutomaticRightStop             = 12
            AutomaticLeftStop              = 13
            SW_MODE                        = 14
            A1                             = 15
            V1                             = 16
            MaxDeceleration                = 17
            D1                             = 18
            StartVelocity                  = 19
            StopVelocity                   = 20
            RampWaitTime                   = 21
            THIGH                          = 23
            VDCMIN                         = 24
            HighSpeedChopperMode           = 27
            HighSpeedFullstepMode          = 28
            MeasuredSpeed                  = 29
            I_scale_analog                 = 33
            internal_Rsense                = 34
            MicrostepResolution            = 140
            ChopperBlankTime               = 162
            ConstantTOffMode               = 163
            DisableFastDecayComparator     = 164
            ChopperHysteresisEnd           = 165
            ChopperHysteresisStart         = 166
            TOff                           = 167
            SEIMIN                         = 168
            SECDS                          = 169
            smartEnergyHysteresis          = 170
            SECUS                          = 171
            smartEnergyHysteresisStart     = 172
            SG2FilterEnable                = 173
            SG2Threshold                   = 174
            smartEnergyActualCurrent       = 180
            smartEnergyStallVelocity       = 181
            smartEnergyThresholdSpeed      = 182
            RandomTOffMode                 = 184
            ChopperSynchronization         = 185
            PWMThresholdSpeed              = 186
            PWMGrad                        = 187
            PWMAmplitude                   = 188
            PWMFrequency                   = 191
            PWMAutoscale                   = 192
            FreewheelingMode               = 204
            LoadValue                      = 206
            EncoderPosition                = 209
            EncoderResolution              = 210
