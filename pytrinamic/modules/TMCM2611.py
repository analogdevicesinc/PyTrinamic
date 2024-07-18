################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# features
from ..features import (
    ABNEncoderModule,
    DigitalHallModule,
    DriveSettingModule,
    LinearRampModule,
    MotorControlModule,
    PIDModule,
)
from . import TMCLModule


class TMCM2611(TMCLModule):
    """
    The TMCM-2611-AGV is a dual axis servo drive module for three phase BLDC motors
        * Supply Voltage: 24-48V
    """

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.name = "TMCM-2611-AGV"
        self.desc = self.__doc__
        self.motors = [self._MotorTypeA(self, 0), self._MotorTypeA(self, 1)]

    def rotate(self, axis, velocity):
        self.connection.rotate(axis, velocity, self.module_id)

    def stop(self, axis):
        self.connection.stop(axis, self.module_id)

    def move_to(self, axis, position, velocity=None):
        if velocity:
            self.motors[axis].linear_ramp.max_velocity = velocity
        self.connection.move_to(axis, position, self.module_id)

    def move_by(self, axis, difference, velocity=None):
        if velocity:
            self.motors[axis].linear_ramp.max_velocity = velocity
        self.connection.move_by(axis, difference, self.module_id)

    def store_axis_parameter(self, ap_type, axis):
        """
        Store an axis parameter setting in non-volatile memory of the module.
        """
        self.connection.store_axis_parameter(ap_type, axis, self.module_id, self.ap_index_bit_width)

    class _MotorTypeA(MotorControlModule):
        def __init__(self, module, axis):
            MotorControlModule.__init__(self, module, axis, self.AP)
            self.drive_settings = DriveSettingModule(module, axis, self.AP)
            self.linear_ramp = LinearRampModule(module, axis, self.AP)
            self.abn_encoder = ABNEncoderModule(module, axis, self.AP)
            self.digital_hall = DigitalHallModule(module, axis, self.AP)
            self.pid = PIDModule(module, axis, self.AP)

        def get_position_reached(self):
            return self.get_axis_parameter(self.AP.PositionReachedFlag)

        class AP:
            # Basic motor parameters
            MotorPolePairs = 0
            MaxCurrent = 1
            OpenLoopCurrent = 2
            MotorDirection = 3
            CommutationMode = 4
            ActualOpenLoopAngle = 5
            MotorType = 9

            # Current ADC parameters
            AdcOffsetI0 = 10
            AdcOffsetI1 = 11
            AdcI0Raw = 12
            AdcI1Raw = 13
            CurrentPhaseU = 14
            CurrentPhaseV = 15
            CurrentPhaseW = 16

            # PID Settings
            TorqueP = 20
            TorqueI = 21
            VelocityP = 22
            VelocityI = 23
            PositionP = 24
            VelocityPScaler = 25
            VelocityIScaler = 26
            PositionPScaler = 27

            # Torque mode parameters
            TargetTorque = 30
            TorqueOffset = 31
            ActualTorque = 32
            TargetFlux = 33
            ActualFlux = 34

            # Ramper parameters
            MaxVelocity = 40
            MaxAcceleration = 41
            TargetVelocity = 42
            RampVelocity = 44
            ActualVelocity = 45
            TargetPosition = 46
            RampPosition = 47
            ActualPosition = 48
            PositionReachedFlag = 49

            # Advanced motor control configuration
            EnableRamp = 50
            VelocityFilter = 51
            MotorHaltedVelocity = 53
            PositionReachedDistance = 54
            PositionReachedVelocity = 55
            PositionScaler = 56
            UseFeedForwardVel = 57
            VelocityMeterCounterLimit = 58

            # Hall sensor parameters
            HallSensorPolarity = 60
            HallSensorDirection = 61
            HallSensorInterpolation = 62
            HallSensorOffset = 63
            ActualHallAngle = 64

            # ABN Encoder parameters
            EncoderSteps = 70
            EncoderDirection = 71
            EncoderInitMode = 72
            EncoderInitDelay = 73
            EncoderInitVelocity = 74
            EncoderInitState = 75
            EncoderOffset = 76
            ActualEncoderAngle = 79

            # Brake control parameters
            BrakeRelease = 80
            BrakeReleaseDuty = 81
            BrakeReleaseDuration = 82
            BrakeHoldDuty = 83
            BrakeState = 84

            # Status APs
            StatusFlags = 90
            SupplyVoltage = 91
            DriverTemperature = 92
            HallSensorInputs = 93
            EncoderInputs = 94
            EncoderRawValue = 95

            # PI internal parameters
            TorquePIDErrorSum = 100
            FluxPIDErrorSum = 101
            VelocityPIDErrorSum = 102

            # IIt
            ThermalWindingTimeConstant1 = 110
            IItlimit1 = 111
            IItSum1 = 112
            ThermalWindingTimeConstant2 = 113
            IItlimit2 = 114
            IItSum2 = 115

            # Diagnostic/Debug parameters
            MainLoopsPerSecond = 230
            TorqueLoopsPerSecond = 231
            VelocityLoopsPerSecond = 232
            DebugValue0 = 240
            DebugValue1 = 241
            DebugValue2 = 242
            DebugValue3 = 243
            DebugValue4 = 244
            DebugValue5 = 245
            DebugValue6 = 246
            DebugValue7 = 247
            DebugValue8 = 248
            DebugValue9 = 249

            # Disable driver
            EnableDriver = 255

        class ENUM:
            # Commutation modes
            COMM_MODE_DISABLED = 0
            COMM_MODE_OPENLOOP = 1
            COMM_MODE_DIGITAL_HALL = 2
            COMM_MODE_ABN_ENCODER = 3

            # Encoder init methods
            ENC_INIT_ESTIMATE_OFFSET = 0
            ENC_INIT_USE_HALL = 1

            # Encoder init states
            ENC_INIT_STATE_SLEEP = 0
            ENC_INIT_STATE_START = 1
            ENC_INIT_STATE_WAIT = 2
            ENC_INIT_STATE_ESTIMATE_OFFSET = 3

            # Brake states
            BRAKE_FAULTY = 0
            BRAKE_READY = 1
            BRAKE_APPLY_MAX_PWM = 2
            BRAKE_APPLY_HOLD_PWM = 3

    class GP:
        SerialBaudRate = 65
        SerialAddress = 66
        SerialHeartbeat = 68
        CANBitRate = 69
        CANsendID = 70
        CANreceiveID = 71
        TelegramPauseTime = 75
        SerialHostAddress = 76
        CANHeartbeat = 82
