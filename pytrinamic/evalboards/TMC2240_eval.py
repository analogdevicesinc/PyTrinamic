from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC2240
from pytrinamic.features import MotorControlModule
from pytrinamic.helpers import TMC_helpers


class TMC2240_eval(TMCLEval):
    """
    This class represents a TMC2240 Evaluation board.

    Communication is done over the TMCL commands writeMC and readMC. An
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
                with a TMC2240. The required functions are
                    connection.writeMC(registerAddress, value, moduleID)
                    connection.readMC(registerAddress, moduleID, signed)
                for writing/reading to registers of the TMC2240.
            module_id:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC2240. This ID is used as a
                parameter for the writeMC and readMC functions.
        """
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC2240()]

    # Use the motion controller functions for register access

    def write_register(self, register_address, value):
        return self._connection.read_drv(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_drv(register_address, self._module_id, signed)

    def write_register_field(self, field, value):
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

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
            TargetPosition = 0
            ActualPosition = 1
            TargetVelocity = 2
            ActualVelocity = 3
            MaxVelocity = 4
            MaxAcceleration = 5
            MaxCurrent = 6
            StandbyCurrent = 7
            PositionReachedFlag = 8
            THIGH = 26
            HighSpeedChopperMode = 28
            HighSpeedFullstepMode = 29
            MeasuredSpeed = 30
            internal_Rsense = 34
            GlobalCurrentScaler = 35
            MicrostepResolution = 140
            ChopperBlankTime = 162
            ConstantTOffMode = 163
            DisableFastDecayComparator = 164
            ChopperHysteresisEnd = 165
            ChopperHysteresisStart = 166
            TOff = 167
            SEIMIN = 168
            SECDS = 169
            smartEnergyHysteresis = 170
            SECUS = 171
            smartEnergyHysteresisStart = 172
            SG2FilterEnable = 173
            SG2Threshold = 174
            smartEnergyActualCurrent = 180
            smartEnergyStallVelocity = 181
            smartEnergyThresholdSpeed = 182
            SG4FilterEnable = 183
            SGAngleOffset = 184
            ChopperSynchronization = 185
            PWMThresholdSpeed = 186
            PWMGrad = 187
            PWMAmplitude = 188
            PWMFrequency = 191
            PWMAutoscale = 192
            PWMScaleSum = 193
            MSCNT = 194
            MEAS_SD_EN = 195
            DIS_REG_STST = 196
            FreewheelingMode = 204
            LoadValue = 206
            EncoderPosition = 209
            EncoderResolution = 210
            CurrentScalingSelector = 211
            CurrentRange = 212
            ADCTemperature = 213
            ADCIN = 214
            ADCSupply = 215
            ADCOvervoltageLimit = 216
            ADCOvertemperatureWarningLimit = 217
            Temperature = 218
            AIN = 219
            VSupply = 220
            OvervoltageLimit = 221
            OvertemperatureWarningLimit = 222
            nSLEEP = 223
