from pytrinamic.modules import TMCLModule

# features
from pytrinamic.features.stallguard2_module import StallGuard2Module
from pytrinamic.features.coolstep_module import CoolStepModule
from pytrinamic.features.DriveSettingModule import DriveSettingModule
from pytrinamic.features.linear_ramp_module import LinearRampModule
from pytrinamic.features.motor_control_module import MotorControlModule


class TMCM6110(TMCLModule):
    """
    The TMCM-6110 is a six axis stepper motor controller/driver module for sensorless load dependent current control.
    """

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.name = "TMCM-6110"
        self.desc = self.__doc__
        self.motors = [self._MotorTypeA(self, 0), self._MotorTypeA(self, 1), self._MotorTypeA(self, 2),
                       self._MotorTypeA(self, 3), self._MotorTypeA(self, 4), self._MotorTypeA(self, 5)]

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

    class _MotorTypeA(MotorControlModule, StallGuard2Module, CoolStepModule):

        def __init__(self, module, axis):
            MotorControlModule.__init__(self, module, axis, self.AP)
            self.drive_settings = DriveSettingModule(module, axis, self.AP)
            self.linear_ramp = LinearRampModule(module, axis, self.AP)

            # ToDo: rework both modules!
            StallGuard2Module.__init__(self)
            CoolStepModule.__init__(self)

        def get_position_reached(self):
            return self.get_axis_parameter(self.AP.PositionReachedFlag)

        class AP:
            TargetPosition              = 0    #    The desired target position in position mode.
            ActualPosition              = 1    #    The actual position of the motor. Stop the motor before overwriting it. Should normally only be overwritten for reference position setting.
            TargetVelocity              = 2    #    The desired speed in velocity mode. Not valid in position mode.
            ActualVelocity              = 3    #    The actual speed of the motor.
            MaxVelocity                 = 4    #    The maximum speed used for positioning ramps.
            MaxAcceleration             = 5    #    Maximum acceleration in positioning ramps. Acceleration and deceleration value in velocity mode.
            MaxCurrent                  = 6    #    Motor current used when motor is running. The maximum value is 255 which means 100% of the maximum current of the module.
            StandbyCurrent              = 7    #    The current used when the motor is not running. The maximum value is 255 which means 100% of the maximum current of the module. This value should be as low as possible so that the motor can cool down when it is not moving. Please see also parameter 214.
            PositionReachedFlag         = 8    #    This flag is always set when target position and actual position are equal.
            ReferenceSwitchStatus       = 9    #    State of the home switch.
            RightEndstop                = 10    #    Logic state of the right switch.
            LeftEndstop                 = 11    #    Logic state of the left switch.
            RightLimitSwitchDisable     = 12    #    Enables automatic motor stop during active right reference switch input.
            LeftLimitSwitchDisable      = 13    #    Enables automatic motor stop during active left reference switch input.
            MinimumSpeed                = 130    #    Should always be set 1 to ensure exact reaching of the target position.
            ActualAcceleration          = 135    #    The current acceleration (read only).
            RampType                    = 138    #    Automatically set when using ROR, ROL, MST and MVP.
            MicrostepResolution         = 140    #    Microstep resolutions per full step:
            ReferenceSwitchTolerance    = 141    #    ref. switch tolerance
            SoftStopFlag                = 149    #    If cleared, the motor will stop immediately (disregarding motor limits), when the reference or limit switch is hit.
            EndSwitchPowerDown          = 150    #    Use standby current when stopped at end switch.
            RampDivisor                 = 153    #    The exponent of the scaling factor for the ramp generator - should be de/incremented carefully (in steps of one).
            PulseDivisor                = 154    #    The exponent of the scaling factor for the pulse (step) generator ? should be de/incremented carefully (in steps of one).
            Intpol                      = 160    #    Step interpolation is supported with a 16 microstep setting only. In this setting, each step impulse at the input causes the execution of 16 times 1/256 microsteps. This way, a smooth motor movement like in 256 microstep resolution is achieved.
            DoubleEdgeSteps             = 161    #    Every edge of the cycle releases a step/microstep. It does not make sense to activate this parameter for internal use. Double step enable can be used with Step/Dir interface.
            ChopperBlankTime            = 162    #    Selects the comparator blank time. This time needs to safely cover the switching event and the duration of the ringing on the sense resistor. Normally leave at the default value.
            ConstantTOffMode            = 163    #    Selection of the chopper mode.
            DisableFastDecayComparator  = 164    #    See parameter 163. For "classic const. off time", setting this parameter to "1" will disable current comparator usage for termination of fast decay cycle.
            ChopperHysteresisEnd        = 165    #    See parameter 163. For "spread cycle" chopper mode this parameter will set / return the hysteresis end setting (hysteresis end value after a number of decrements). For "classic const. off time" chopper mode this parameter will set / return the fast decay time.
            ChopperHysteresisStart      = 166    #    See parameter 163. For "spread cycle" chopper mode this parameter will set / return the Hysteresis start setting (please note that this value is an offset to the hysteresis end value). For "classic const. off time" chopper mode this parameter will set / return the sine wave offset.
            Toff                        = 167    #    The off time setting controls the minimum chopper frequency. An off time within the range of 5us to 20us will fit. Off time setting for constant t Off chopper: NCLK = 12 + 32 tOFF (Minimum is 64 clocks) Setting this parameter to zero completely disables all driver transistors and the motor can freewheel.
            SEIMIN                      = 168    #    Sets the lower motor current limit for coolStep operation by scaling the maximum current (see axis parameter 6) value.
            SECDS                       = 169    #    Sets the number of stallGuard2 readings above the upper threshold necessary for each current decrement of the motor current. Number of stallGuard2 measurements per decrement: Scaling: 0. . . 3: 32, 8, 2, 1. 0: slow decrement, 3: fast decrement
            SmartEnergyHysteresis       = 170    #    Sets the distance between the lower and the upper threshold for stallGuard2 reading. Above the upper threshold the motor current becomes decreased. Hysteresis: ([AP172] + 1) * 32. Upper stallGuard threshold: ([AP172] + [AP170] + 1) * 32
            SECUS                       = 171    #    Sets the current increment step. The current becomes incremented for each measured stallGuard2 value below the lower threshold see smartEnergy hysteresis start). Current increment step size: Scaling: 0. . . 3: 1, 2, 4, 8. 0: slow increment, 3: fast increment / fast reaction to rising load
            SmartEnergyHysteresisStart  = 172    #    The lower threshold for the stallGuard2 value (see smart Energy current up step).
            SG2FilterEnable             = 173    #    Enables the stallGuard2 filter for more precision of the movement. If set, reduces the measurement frequency to one measurement per four fullsteps. In most cases it is expedient to set the filtered mode before using coolStep. Use the standard mode for step loss detection.
            SG2Threshold                = 174    #    This signed value controls stallGuard2 threshold level for stall output and sets the optimum measurement range for readout. A lower value gives a higher sensitivity. Zero is the starting value. A higher value makes stallGuard2 less sensitive and requires more torque to indicate a stall.
            SlopeControlHighSide        = 175    #    Determines the slope of the motor driver outputs. Set to 2 or 3 for this module or rather use the default value. 0: lowest slope. 3: fastest slope.
            SlopeControlLowSide         = 176    #    Determines the slope of the motor driver outputs. Set to 2 or 3 for this module or rather use the default value. 0: lowest slope. 3: fastest slope.
            ShortToGroundProtection     = 177    #    Disable short to ground protection.
            ShortDetectionTime          = 178    #    Use default value!
            VSense                      = 179    #    Sense resistor voltage:
            SmartEnergyActualCurrent    = 180    #    This status value provides the actual motor current setting as controlled by coolStep. The value goes up to the CS value and down to the portion of CS as specified by SEIMIN. Actual motor current scaling factor: 0. . . 31: 1/32, 2/32, . . . 32/32
            SmartEnergyStallVelocity    = 181    #    Velocity from which stop on stall feature is active
            SmartEnergyThresholdSpeed   = 182    #    Above this speed coolStep becomes enabled.
            SmartEnergySlowRunCurrent   = 183    #    Sets the motor current which is used below the threshold speed.
            RandomTOffMode              = 184    #    Enable / disable random TOff mode.
            ReferenceSearchMode         = 193    #    Selects the reference search mode. Add 128 to a mode value for inverting the home switch (can be used with mode 5\ldots 8). Add 64 to a mode for driving the right instead of the left reference switch (can be used with modes 1-4).
            ReferenceSearchSpeed        = 194    #    This value specifies the speed for roughly searching the reference switch.
            ReferenceSwitchSpeed        = 195    #    This parameter specifies the speed for searching the switching point. It should be slower than parameter 194.
            ReferenceSwitchDistance     = 196    #    This parameter provides the distance between the end switches after executing the RFS command (with reference search mode 2 or 3).
            LastReferenceSwitchPosition = 197    #    This parameter contains the last position value before the position counter is set to zero during reference search.
            BoostCurrent                = 200    #    Current used for acceleration and deceleration phases. If set to 0 the same current as set by axis parameter 6 will be used.
            FreewheelingDelay           = 204    #    Time after which the power to the motor will be cut when its velocity has reached zero. 0: never.
            LoadValue                   = 206    #    Actual current control scaling for monitoring smart energy current scaling or automatic current scaling.
            ExtendedErrorFlags          = 207    #    A combination of the following values: 1 - stallGuard error, 2 - deviation error. These error flags are cleared automatically when this parameter has been read out or when a motion command has been executed.
            DrvStatusFlags              = 208    #    TMC5130 flags of register DRVSTATUS.
            GroupIndex                  = 213    #   All modules with the same group index will do the same when an ROL, ROR, MVP, MST or RFS is used on one of these motors. Setting it to 0 will turn off this feature.
            PowerDownDelay              = 214    #    Standstill period before the current will be ramped down to standby current. The standard value is 200 (which means 2000ms).
    
        class ENUM:
            microstep_resolution_fullstep = 0
            microstep_resolution_halfstep = 1
            microstep_resolution_4_microsteps = 2
            microstep_resolution_8_microsteps = 3
            microstep_resolution_16_microsteps = 4
            microstep_resolution_32_microsteps = 5
            microstep_resolution_64_microsteps = 6
            microstep_resolution_128_microsteps = 7
            microstep_resolution_256_microsteps = 8

    class GP:
        SerialBaudRate      = 65
        SerialAddress       = 66
        CANBitRate          = 69
        CANsendID           = 70
        CANreceiveID        = 71
        TelegramPauseTime   = 75
        SerialHostAddress   = 76
        AutoStartMode       = 77
        ApplicationStatus   = 128
        ProgramCounter      = 130
        TickTimer           = 132

    class IO:
        OUT0   = 0
        OUT1   = 1