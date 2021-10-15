'''
Created on 04.05.2020
@author: JM, ED, JH 
'''

from PyTrinamic.features.DigitalHallWeaselModule import DigitalHallWeaselModule
from PyTrinamic.modules.tmcl_module import tmcl_module
from PyTrinamic.features.LinearRampModule import LinearRampModule
from PyTrinamic.features.ABNEncoderModule import ABNEncoderModule
from PyTrinamic.features.AbsoluteEncoderModule import AbsoluteEncoderModule
from PyTrinamic.features.DigitalHallWeaselModule import DigitalHallWeaselModule
from PyTrinamic.features.CommutationSelectionModule import CommutationSelectionModule
from PyTrinamic.features.OpenLoopModule import OpenLoopModule
from PyTrinamic.features.PIDModule import PIDModule
from PyTrinamic.features.MotorControlModule import MotorControlModule
from PyTrinamic.features.BLDCMotorModule import BLDCMotorModule

class TMCM_1636(tmcl_module):

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.MOTORS = [self.MOTOR_0(self, 0)]

    @staticmethod
    def getEdsFile():
        return __file__.replace("TMCM_1636.py", "TMCM-1636-CANopen_Hw1.1_Fw1.12.eds")

    def showChipInfo(self):
        print("The TMCM-1636 is a single axis servo drive platform for 3-phase BLDC motors and DC motors. Voltage supply: 8 - 28V");

    def rotate(self, axis, velocity):
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        if velocity:
            self.max_velocity = velocity
        self.connection.moveTo(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.max_velocity = velocity
        self.connection.moveBy(axis, difference, self.module_id)

    class MOTOR_0(tmcl_module.Motor, LinearRampModule, ABNEncoderModule,AbsoluteEncoderModule,DigitalHallWeaselModule,CommutationSelectionModule,PIDModule,MotorControlModule, OpenLoopModule, BLDCMotorModule):

        def __init__(self, module, axis):
            tmcl_module.Motor.__init__(self, module, axis)
            LinearRampModule.__init__(self)
            ABNEncoderModule.__init__(self)
            AbsoluteEncoderModule.__init__(self)
            DigitalHallWeaselModule.__init__(self)
            CommutationSelectionModule.__init__(self)
            OpenLoopModule.__init__(self)
            PIDModule.__init__(self)
            BLDCMotorModule.__init__(self)

        def get_position_reached(self):
            return self.get_axis_parameter(self.APs.PositionReachedFlag)

        class APs():
            AdcPhaseA                       = 0
            AdcPhaseB                       = 1
            CurrentPhaseA                   = 2
            CurrentPhaseB                   = 3
            CurrentPhaseC                   = 4
            AdcOffsetPhaseA                 = 5
            AdcOffsetPhaseB                 = 6
            MotorPolePairs                  = 10
            MaxCurrent                      = 11
            OpenLoopCurrent                 = 12
            MotorDirection                  = 13
            MotorType                       = 14
            CommutationMode                 = 15
            ActualOpenLoopAngle             = 16
            ActualEncoderAngle              = 17
            ActualHallAngle                 = 18
            ActualAbsoluteEncoderAngle      = 19
            PositionSensorSelection         = 25
            VelocitySensorSelection         = 26
            TargetTorque                    = 30
            ActualTorque                    = 31
            TargetFlux                      = 32
            ActualFlux                      = 33
            TargetVelocity                  = 40
            RampVelocity                    = 41
            ActualVelocity                  = 42
            MaxVelocity                     = 43
            MaxAcceleration                 = 44 #renamed from Acceleration
            EnableRamp                      = 45
            TargetPosition                  = 50
            RampPosition                    = 51
            ActualPosition                  = 52
            TargetReachedDistance           = 53
            TargetReachedVelocity           = 54
            PositionReachedFlag             = 55
            PositionScaler                  = 56
            TorqueP                         = 70
            TorqueI                         = 71
            VelocityP                       = 72
            VelocityI                       = 73
            PositionP                       = 74
            CurrentPiErrorSum               = 75
            FluxPiErrorSum                  = 76
            VelocityPiErrorSum              = 77
            TorquePiError                   = 78
            FluxPiError                     = 79
            VelocityPiError                 = 80
            PositionPiError                 = 81
            HallSensorPolarity              = 90
            HallSensorDirection             = 91
            HallSensorInterpolation         = 92
            HallSensorOffset                = 93
            HallSensorInputs                = 94
            EncoderSteps                    = 100
            EncoderDirection                = 101
            EncoderInitMode                 = 102
            EncoderInitState                = 103
            EncoderInitDelay                = 104
            EncoderInitVelocity             = 105
            EncoderOffset                   = 106
            ClearOnNull                     = 107
            ClearOnce                       = 108
            EncoderInputs                   = 109
            PWMFrequency                    = 110
            BrakeEnabled                    = 120
            BrakeDutyCycle0                 = 121
            BrakeDutyCycle1                 = 122
            BrakePhase0Duration             = 123
            EnableBrakeOutput               = 124
            InvertBrakeOutput               = 125
            BrakeChopperEnabled             = 140
            BrakeChopperVoltage             = 141
            BrakeChopperHysteresis          = 142
            BrakeChopperActive              = 144
            StatusFlags                     = 156
            AbsoluteEncoderType             = 160
            AbsoluteEncoderInit             = 161
            AbsoluteEncoderDirection        = 162
            AbsoluteEncoderOffset           = 163
            AbsoluteEncoderDataLength       = 165
            AbsoluteEncoderPositionStart    = 166
            AbsoluteEncoderPositionLength   = 167
            ReferenceSwitchEnable           = 209
            ReferenceSwitchPolarity         = 210
            RightStopSwitch                 = 211
            LeftStopSwitch                  = 212
            HomeStopSwitch                  = 213
            SupplyVoltage                   = 220
            DriverTemperature               = 221
            MainLoopsPerSecond              = 230
            TorqueLoopsPerSecond            = 231
            VelocityLoopsPerSecond          = 232
            DebugValue0                     = 240
            DebugValue1                     = 241
            DebugValue2                     = 242
            DebugValue3                     = 243
            DebugValue4                     = 244
            DebugValue5                     = 245
            DebugValue6                     = 246
            DebugValue7                     = 247
            DebugValue8                     = 248
            DebugValue9                     = 249
            DriverEnabled                   = 255

        class ENUMs():
            COMM_MODE_DISABLED              = 0
            COMM_MODE_OPENLOOP              = 1
            COMM_MODE_DIGITAL_HALL          = 2
            COMM_MODE_ABN_ENCODER           = 3
            COMM_MODE_ABS_ENCODER           = 4

            ENCODER_INIT_MODE_0             = 0
            ENCODER_INIT_MODE_1             = 1
            ENCODER_INIT_MODE_2             = 2

            POS_SELECTION_SAME              = 0
            POS_SELECTION_ABN               = 1
            POS_SELECTION_ABS               = 2

            VEL_SELECTION_SAME              = 0
            VEL_SELECTION_ABN               = 1
            VEL_SELECTION_ABS               = 2

            FLAG_POSITION_END               = 0x00004000

            MOTOR_TYPE_NO_MOTOR             = 0
            MOTOR_TYPE_SINGLE_PHASE_DC      = 1
            MOTOR_TYPE_THREE_PHASE_BLDC     = 3

    class GPs():
        serialBaudRate      = 65
        serialAddress       = 66
        CANBitRate          = 69
        CANsendID           = 70
        CANreceiveID        = 71
        telegramPauseTime   = 75
        serialHostAddress   = 76
        autoStartMode       = 77
        applicationStatus   = 128
        programCounter      = 130
        tickTimer           = 132

    class IOs():
        GPI_0   = 0
        GPI_1   = 1
        GPI_2   = 2
        GPI_3   = 3