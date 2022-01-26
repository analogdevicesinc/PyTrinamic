'''
Created on 06.02.2020

@author: JM
'''

from pytrinamic.ic.TMC4330.TMC4330 import TMC4330

class TMC4330_eval(TMC4330):

    def __init__(self, connection, moduleID=1):
        self.__connection = connection
        self._MODULE_ID   = moduleID
        self.APs          = _APs
        
        TMC4330.__init__(self, connection, channel=0)

    def register(self):
        return self.TMC4330.register()

    def variants(self):
        return self.TMC4330.variants()

    def maskShift(self):
        return self.TMC4330.maskShift()

    def ic(self):
        return self.TMC4330

    " register access: use Landungsbrücke/Startrampe with MC channel"
    def writeRegister(self, registerAddress, value , channel=0):
        if channel != 0:
            raise ValueError
        return self.__connection.write_mc(registerAddress, value)

    def readRegister(self, registerAddress, channel=0, signed=False):
        if channel != 0:
            raise ValueError
        return self.__connection.read_mc(registerAddress, signed=signed)

    # Axis parameter access
    def getAxisParameter(self, apType, axis):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        return self.__connection.get_axis_parameter(apType, axis)

    def setAxisParameter(self, apType, axis, value):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        self.__connection.set_axis_parameter(apType, axis, value)

    # Motion Control functions
    def rotate(self, motor, value):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        self.__connection.rotate(motor, value)

    def stop(self, motor):
        self.__connection.stop(motor)

    def moveTo(self, motor, position, velocity=None):
        if velocity and velocity != 0:
            # Set maximum positioning velocity
            self.setAxisParameter(self.APs.MaxVelocity, motor, velocity)

        self.__connection.move(0, motor, position)

class _APs():
    TargetPosition                 = 0
    ActualPosition                 = 1
    TargetVelocity                 = 2
    ActualVelocity                 = 3
    MaxVelocity                    = 4
    MaxAcceleration                = 5
    PositionReachedFlag            = 8
    RampType                       = 14
    StartVelocity                  = 15
    AStart                         = 16
    MaxDeceleration                = 17
    VBreak                         = 18
    DFinal                         = 19
    StopVelocity                   = 20
    DSTOP                          = 21
    BOW1                           = 22
    BOW2                           = 23
    BOW3                           = 24
    BOW4                           = 25
    VirtualStopLeft                = 26
    VirtualStopRight               = 27
    CLGammaVMin                    = 108
    CLGammaVMax                    = 109
    CLMaxGamma                     = 110
    CLBeta                         = 111
    CLOffset                       = 112
    CLCorrectionVelocityP          = 115
    CLCorrectionVelocityI          = 116
    CLCorrectionVelIClip           = 116
    CL_CorrectionVelDVClock        = 116
    CL_Correction_VelDVClip        = 119
    CLCorrectionPositionP          = 124
    CLMaxCorrectionTolerance       = 125
    CLStartUp                      = 126
    CLFlag                         = 129
    MeasuredEncoderSpeed           = 132
    CLInitFlag                     = 133
    EncoderDeviation               = 134
    EncVelDelay                    = 136
    EncVelFilter                   = 137
    FilterUpdateTime               = 138
    EncoderPosition                = 209
    MaxEncoderDeviation            = 212
    PowerDownDelay                 = 214
