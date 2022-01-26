'''
Created on 03.12.2019

@author: JM
'''

from pytrinamic.modules.tmcl_module import TMCLModule
from pytrinamic.features.linear_ramp_module import LinearRampModule
from pytrinamic.features.stallguard2_module import StallGuard2Module
from pytrinamic.features.CurrentModule import CurrentModule
from pytrinamic.features.motor_control_module import MotorControlModule


class TMCM1270(TMCLModule):
    "TMCM-1270 module implementation"

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.MOTORS = [self.MOTOR_0(self, 0)]

    @staticmethod
    def getEdsFile():
        "Returns EDS file with parameters"
        return __file__.replace("TMCM1270.py", "TMCM_1270_V3.22.eds")

    def showChipInfo(self):
        print("The TMCM-1270 is a smart stepper motor driver module. The module is controlled via a CAN bus interface. Voltage supply: 6 - 24V")

    def rotate(self, axis, velocity):
        """
        Rotates the motor on the given axis with the given velocity.

        Parameters:
        axis: Axis index.
        velocity: Target velocity to rotate the motor with. Units are module specific.

        Returns: None
        """
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        """
        Stops the motor on the given axis.

        Parameters:
        axis: Axis index.

        Returns: None
        """
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        """
        Moves the motor on the given axis to the given target position.

        Parameters:
        axis: Axis index.
        position: Target position to move the motor to. Units are module specific.
        velocity: Maximum position velocity to position the motor. Units are module specific.
        If no velocity is given, the previously configured maximum positioning velocity (AP 4)
        will be used.

        Returns: None
        """
        if velocity:
            self.max_velocity = velocity
        self.connection.move_to(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        """
        Moves the motor on the given axis by the given position difference.

        Parameters:
        axis: Axis index.
        difference: Position difference to move the motor by. Units are module specific.
        velocity: Maximum position velocity to position the motor. Units are module specific.
        If no velocity is given, the previously configured maximum positioning velocity (AP 4)
        will be used.

        Returns: None
        """
        if velocity:
            self.max_velocity = velocity
        self.connection.move_by(axis, difference, self.module_id)

    class MOTOR_0(TMCLModule.Motor, LinearRampModule, StallGuard2Module, CurrentModule, MotorControlModule):
        "Motor class for the motor on axis 0."

        def __init__(self, module, axis):
            TMCLModule.Motor.__init__(self, module, axis)
            LinearRampModule.__init__(self)
            StallGuard2Module.__init__(self)
            CurrentModule.__init__(self)

        def get_position_reached(self):
            """
            Indicates whether a positioning task has been completed.

            Returns:
            1, if target position has been reached.
            0, if target position has not been reached.
            """
            return self.get_axis_parameter(self.AP.PositionReachedFlag)

        class AP:
            # Axis parameter map for this axis.
            TargetPosition                 = 0
            ActualPosition                 = 1
            TargetVelocity                 = 2
            ActualVelocity                 = 3
            MaxVelocity                    = 4
            MaxAcceleration                = 5
            RunCurrent                     = 6
            StandbyCurrent                 = 7
            PositionReachedFlag            = 8
            HomeSwitch                     = 9
            RightEndstop                   = 10
            LeftEndstop                    = 11
            AutomaticRightStop             = 12
            AutomaticLeftStop              = 13
            swapSwitchInputs               = 14
            A1                             = 15
            V1                             = 16
            MaxDeceleration                = 17
            D1                             = 18
            StartVelocity                  = 19
            StopVelocity                   = 20
            RampWaitTime                   = 21
            THIGH                          = 22
            VDCMIN                         = 23
            RightSwitchPolarity            = 24
            LeftSwitchPolarity             = 25
            Softstop                       = 26
            HighSpeedChopperMode           = 27
            HighSpeedFullstepMode          = 28
            MeasuredSpeed                  = 29
            PowerDownRamp                  = 31
            RelativePositioningOptionCode  = 127
            MicrostepResolution            = 140
            ChopperBlankTime               = 162
            ConstantTOffMode               = 163
            DisableFastDecayComparator     = 164
            ChopperHysteresisEnd           = 165
            ChopperHysteresisStart         = 166
            TOff                           = 167
            SEIMIN                         = 168
            SECDS                          = 169
            SmartEnergyHysteresis          = 170
            SECUS                          = 171
            SmartEnergyHysteresisStart     = 172
            SG2FilterEnable                = 173
            SG2Threshold                   = 174
            ShortToGroundProtection        = 177
            VSense                         = 179
            SmartEnergyActualCurrent       = 180
            SmartEnergyStallVelocity       = 181
            SmartEnergyThresholdSpeed      = 182
            RandomTOffMode                 = 184
            ChopperSynchronization         = 185
            PWMThresholdSpeed              = 186
            PWMGrad                        = 187
            PWMAmplitude                   = 188
            PWMScale                       = 189
            PWMMode                        = 190
            PWMFrequency                   = 191
            PWMAutoscale                   = 192
            ReferenceSearchMode            = 193
            ReferenceSearchSpeed           = 194
            RefSwitchSpeed                 = 195
            RightLimitSwitchPosition       = 196
            LastReferencePosition          = 197
            EncoderMode                    = 201
            MotorFullStepResolution        = 202
            PWMSymmetric                   = 203
            FreewheelingMode               = 204
            LoadValue                      = 206
            ErrorFlags                     = 207
            StatusFlags                    = 208
            EncoderPosition                = 209
            EncoderResolution              = 210
            EncoderDeviationMax            = 212
            PowerDownDelay                 = 214
            UnitMode                       = 255

    class ENUM():
        "Constant enums for parameters of this module."
        pass

    class GP():
        "Global parameter map for this module."
        CANBitrate                    = 69
        CANSendId                     = 70
        CANReceiveId                  = 71
        CANSecondaryId                = 72
        AutoStartMode                 = 77
        ProtectionMode                = 81
        EepromCoordinateStore         = 84
        ZeroUserVariables             = 85
        ApplicationStatus             = 128
        ProgramCounter                = 130
        LastTmclError                 = 131
        TickTimer                     = 132
        RandomNumber                  = 133
