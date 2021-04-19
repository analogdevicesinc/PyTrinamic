'''
Created on 25.06.2019

@author: ED
'''
from PyTrinamic.helpers import TMC_helpers
from PyTrinamic.modules.tmcl_module import tmcl_module

class TMCM_1633(tmcl_module):

    class APs():
        TargetPosition                 = 0
        ActualPosition                 = 1
        TargetVelocity                 = 2
        ActualVelocity                 = 3
        MaxVelocity                    = 4
        MaxTorque                      = 6
        TargetReachedVelocity          = 7
        MotorHaltedVelocity            = 9
        TargetReachedDistance          = 10
        Acceleration                   = 11
        RampVelocity                   = 13
        ReinitBldcRegulation           = 31
        PIDRegulationLoopDelay         = 133
        CurrentRegulationLoopDelay     = 134
        EnableRamp                     = 146
        ActualTorque                   = 150
        SupplyVoltage                  = 151
        DriverTemperature              = 152
        TargetTorque                   = 155
        StatusFlags                    = 156
        CommutationMode                = 159
        ClearOnNull                    = 161
        ClearOnce                      = 163
        EncoderOffset                  = 165
        TorqueP                        = 172
        TorqueI                        = 173
        StartCurrent                   = 177
        MainLoopsPerSecond             = 180
        PwmLoopsPerSecond              = 181
        TorqueLoopsPerSecond           = 182
        VelocityLoopsPerSecond         = 183
        DebugValue0                    = 190
        DebugValue1                    = 191
        DebugValue2                    = 192
        DebugValue3                    = 193
        DebugValue4                    = 194
        DebugValue5                    = 195
        DebugValue6                    = 196
        DebugValue7                    = 197
        DebugValue8                    = 198
        DebugValue9                    = 199
        CurrentPIDError                = 200
        CurrentPIDErrorSum             = 201
        ActualHallAngle                = 210
        ActualEncoderAngle             = 211
        ActualControlledAngle          = 212
        PositionPIDError               = 226
        VelocityPIDError               = 228
        VelocityPIDErrorSum            = 229
        PositionP                      = 230
        VelocityP                      = 234
        VelocityI                      = 235
        InitVelocity                   = 241
        InitSineDelay                  = 244
        EncoderInitMode                = 249
        EncoderSteps                   = 250
        EncoderDirection               = 251
        HallInterpolation              = 252
        MotorPoles                     = 253
        HallSensorInvert               = 254
        DriverEnabled                  = 255

    class ENUMs():
        COMM_MODE_FOC_HALL              = 6
        COMM_MODE_FOC_ENCODER           = 7
        COMM_MODE_FOC_CONTROLLED        = 8

        ENCODER_INIT_MODE_0             = 0
        ENCODER_INIT_MODE_1             = 1
        ENCODER_INIT_MODE_2             = 2

        FLAG_POSITION_END               = 0x00004000

    class GPs():
        serialBaudRate                 = 65
        serialAddress                  = 66
        CANBitRate                     = 69
        CANsendID                      = 70
        CANreceiveID                   = 71
        telegramPauseTime              = 75
        serialHostAddress              = 76
        autoStartMode                  = 77
        applicationStatus              = 128
        programCounter                 = 130
        tickTimer                      = 132

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)

        self.motor = 0

    @staticmethod
    def getEdsFile():
        return __file__.replace("TMCM_1633.py", "TMCM_1633_Hw1.00_Fw2.10.eds")

    def showChipInfo(self):
        print("The TMCM-1633 is a highly integrated single axis BLDC servo controller module with several interface options. Voltage supply: 14,5 - 48V");

    " standard functions "
    def moveToPosition(self, axis, position):
        self.setAxisParameter(self.APs.TargetPosition, position)

    def targetPosition(self, axis):
        return self.axisParameter(self.APs.TargetPosition)

    def actualPosition(self, axis):
        return TMC_helpers.toSigned32(self.axisParameter(self.APs.ActualPosition))

    def setActualPosition(self, axis, position):
        return self.setAxisParameter(self.APs.ActualPosition, position)

    def rotate(self, axis, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, velocity)

    def actualVelocity(self, axis):
        return TMC_helpers.toSigned32(self.axisParameter(self.APs.ActualVelocity))

    def setTargetTorque(self, axis, torque):
        self.setAxisParameter(self.APs.TargetTorque, torque)

    def targetTorque(self, axis):
        return self.axisParameter(self.APs.TargetTorque)

    def actualTorque(self, axis):
        return self.axisParameter(self.APs.ActualTorque)

    " helpful functions "

    def maxVelocity(self, axis):
        return self.axisParameter(self.APs.MaxVelocity, axis)

    def setMaxVelocity(self, axis, maxVelocity):
        self.setAxisParameter(self.APs.MaxVelocity, axis, maxVelocity)

    def maxTorque(self, axis):
        return self.axisParameter(self.APs.MaxTorque, axis)

    def setMaxTorque(self, axis, maxTorque):
        self.setAxisParameter(self.APs.MaxTorque, axis, maxTorque)

    def openLoopTorque(self, axis):
        return self.axisParameter(self.APs.StartCurrent, axis)

    def setOpenLoopTorque(self, axis, torque):
        self.setAxisParameter(self.APs.StartCurrent, axis, torque)

    def acceleration(self, axis):
        return self.axisParameter(self.APs.Acceleration, axis)

    def setAcceleration(self, axis, acceleration):
        self.setAxisParameter(self.APs.Acceleration, axis, acceleration)

    def targetReachedVelocity(self, axis):
        return self.axisParameter(self.APs.TargetReachedVelocity, axis)

    def setTargetReachedVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.TargetReachedVelocity, axis, velocity)

    def targetReachedDistance(self, axis):
        return self.axisParameter(self.APs.TargetReachedDistance, axis)

    def setTargetReachedDistance(self, axis, distance):
        self.setAxisParameter(self.APs.TargetReachedDistance, axis, distance)

    def motorHaltedVelocity(self, axis):
        return self.axisParameter(self.APs.MotorHaltedVelocity, axis)

    def setMotorHaltedVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.MotorHaltedVelocity, axis, velocity)

    def positionReached(self, axis):
        return ((self.statusFlags() & self.ENUMs.FLAG_POSITION_END) != 0)

    def rampEnabled(self, axis):
        return self.axisParameter(self.APs.EnableRamp, axis)

    def setRampEnabled(self, axis, enable):
        self.setAxisParameter(self.APs.EnableRamp, axis, enable)

    def torquePParameter(self, axis):
        return self.axisParameter(self.APs.TorqueP, axis)

    def setTorquePParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.TorqueP, axis, pValue)

    def torqueIParameter(self, axis):
        return self.axisParameter(self.APs.TorqueI, axis)

    def setTorqueIParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.TorqueI, axis, pValue)

    def velocityPParameter(self, axis):
        return self.axisParameter(self.APs.VelocityP, axis)

    def setVelocityPParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.VelocityP, axis, pValue)

    def velocityIParameter(self, axis):
        return self.axisParameter(self.APs.VelocityI, axis)

    def setVelocityIParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.VelocityI, axis, pValue)

    def positionPParameter(self, axis):
        return self.axisParameter(self.APs.PositionP, axis)

    def setPositionPParameter(self, axis, pValue):
        self.setAxisParameter(self.APs.PositionP, axis, pValue)

    def motorPoles(self, axis):
        return self.axisParameter(self.APs.MotorPoles, axis)

    def setMotorPoles(self, axis, poles):
        self.setAxisParameter(self.APs.MotorPoles, axis, poles)

    def hallInvert(self, axis):
        return self.axisParameter(self.APs.HallSensorInvert, axis)

    def setHallInvert(self, axis, invert):
        self.setAxisParameter(self.APs.HallSensorInvert, axis, invert)

    def encoderInitMode(self, axis):
        return self.axisParameter(self.APs.EncoderInitMode, axis)

    def setEncoderInitMode(self, axis, mode):
        self.setAxisParameter(self.APs.EncoderInitMode, axis, mode)

    def encoderResolution(self, axis):
        return self.axisParameter(self.APs.EncoderSteps, axis)

    def setEncoderResolution(self, axis, steps):
        self.setAxisParameter(self.APs.EncoderSteps, axis, steps)

    def encoderDirection(self, axis):
        return self.axisParameter(self.APs.EncoderDirection, axis)

    def setEncoderDirection(self, axis, direction):
        self.setAxisParameter(self.APs.EncoderDirection, axis, direction)

    def commutationMode(self, axis):
        return self.axisParameter(self.APs.CommutationMode, axis)

    def setCommutationMode(self, axis, mode):
        self.setAxisParameter(self.APs.CommutationMode, axis, mode)

    def statusFlags(self, axis):
        return self.axisParameter(self.APs.StatusFlags, axis)

    # Differs semantically from default
    def setDigitalOutput(self, x):
        return self.connection.setDigitalOutput(x, 1)

    # Differs semantically from default
    def clearDigitalOutput(self, x):
        return self.connection.setDigitalOutput(x, 0)

    def showMotorConfiguration(self):
        print("Motor configuration:")
        print("\tMotor poles: " + str(self.motorPoles()))
        print("\tMax torque:  " + str(self.maxTorque()) + " mA")

    def showHallConfiguration(self):
        print("Hall configuration:")
        print("\tHall invert: " + str(self.hallInvert()))

    def showEncoderConfiguration(self):
        print("Encoder configuration:")
        print("\tOpen loop torque:   " + str(self.openLoopTorque()) + " mA")
        print("\tEncoder resolution: " + str(self.encoderResolution()))
        print("\tEncoder direction:  " + str(self.encoderDirection()))
        print("\tEncoder init mode:  " + str(self.encoderInitMode()))

    def showMotionConfiguration(self):
        print("Motion configuration:")
        print("\tMax velocity: " + str(self.maxVelocity()))
        print("\tAcceleration: " + str(self.acceleration()))
        print("\tRamp enabled: " + ("disabled" if (self.rampEnabled()==0) else "enabled"))
        print("\tMotor halted velocity:   " + str(self.motorHaltedVelocity()))
        print("\tTarget reached velocity: " + str(self.targetReachedVelocity()))
        print("\tTarget reached distance: " + str(self.targetReachedDistance()))

    def showPIConfiguration(self):
        print("PI configuration:")
        print("\tTorque   P: " + str(self.torquePParameter()) + " I: " + str(self.torqueIParameter()))
        print("\tVelocity P: " + str(self.velocityPParameter()) + " I: " + str(self.velocityIParameter()))
        print("\tPosition P: " + str(self.positionPParameter()))
