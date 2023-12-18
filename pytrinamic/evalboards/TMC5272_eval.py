################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC5272
from pytrinamic.features import MotorControlModule


class TMC5272_eval(TMCLEval):
    """
    This class represents a TMC5272 Evaluation board.

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
                with a TMC5272. The required functions are
                    connection.writeDRV(registerAddress, value, moduleID)
                    connection.readDRV(registerAddress, moduleID, signed)
                for writing/reading to register of the TMC5272.
            module_id:
                Type: int, optional, default value: 1
                The TMCL module ID of the TMC5272. This ID is used as a
                parameter for the writeDRV and readDRV functions.
        """
        TMCLEval.__init__(self, connection, module_id)
        self.motors = [self._MotorTypeA(self, 0)]
        self.ics = [TMC5272()]

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
        if velocity and velocity != 0:
            self.motors[motor].set_axis_parameter(self.motors[motor].AP.MaxVelocity, velocity)
        self._connection.move_by(motor, distance, self._module_id)

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
            RightEndstop = 10
            LeftEndstop = 11
            AutomaticRightStop = 12
            AutomaticLeftStop = 13
            SW_MODE = 14
            MaxDeceleration = 15
            StartVelocity = 16
            A1 = 17
            V1 = 18
            D1 = 19
            StopVelocity = 20
            RampWaitTime = 21
            V2 = 22
            D2 = 23
            A2 = 24
            TVMax = 25
            THIGH = 26
            VDCMIN = 27
            HighSpeedChopperMode = 28
            HighSpeedFullstepMode = 29
            GlobalCurrentScalerA = 35
            GlobalCurrentScalerB = 36
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
            SG4FilterEnable = 173
            SG4Threshold = 174
            SG2FilterEnable = 175
            SG2Threshold = 176
            smartEnergyActualCurrent = 180
            smartEnergyStallVelocity = 181
            smartEnergyThresholdSpeed = 182
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
            Temperature = 214
            FSR_IREF = 215
            nSLEEP = 216
            MSLUT_0 = 220
            MSLUT_1 = 221
            MSLUT_2 = 222
            MSLUT_3 = 223
            MSLUT_4 = 224
            MSLUT_5 = 225
            MSLUT_6 = 226
            MSLUT_7 = 227
            MSLUT_START = 228
            MSLUT_SEL = 229
            START_SIN90 = 230
            OFFSET_SIN90 = 231
            SG4_IND_0 = 232
            SG4_IND_1 = 233
            SG4_IND_2 = 234
            SG4_IND_3 = 235
            TargetPosition = 0
            ActualPosition = 1
            TargetVelocity = 2
            ActualVelocity = 3
            MaxVelocity = 4
            MaxAcceleration = 5
            MaxCurrent = 6
            StandbyCurrent = 7
            PositionReachedFlag = 8
            RightEndstop = 10
            LeftEndstop = 11
            AutomaticRightStop = 12
            AutomaticLeftStop = 13
            SW_MODE = 14
            MaxDeceleration = 15
            StartVelocity = 16
            A1 = 17
            V1 = 18
            D1 = 19
            StopVelocity = 20
            RampWaitTime = 21
            V2 = 22
            D2 = 23
            A2 = 24
            TVMax = 25
            THIGH = 26
            VDCMIN = 27
            HighSpeedChopperMode = 28
            HighSpeedFullstepMode = 29
            GlobalCurrentScalerA = 35
            GlobalCurrentScalerB = 36
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
            SG4FilterEnable = 173
            SG4Threshold = 174
            SG2FilterEnable = 175
            SG2Threshold = 176
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
            Temperature = 214
            FSR_IREF = 215
            nSLEEP = 216
            MSLUT_0 = 220
            MSLUT_1 = 221
            MSLUT_2 = 222
            MSLUT_3 = 223
            MSLUT_4 = 224
            MSLUT_5 = 225
            MSLUT_6 = 226
            MSLUT_7 = 227
            MSLUT_START = 228
            MSLUT_SEL = 229
            START_SIN90 = 230
            OFFSET_SIN90 = 231
            SG4_IND_0 = 232
            SG4_IND_1 = 233
            SG4_IND_2 = 234
            SG4_IND_3 = 235
