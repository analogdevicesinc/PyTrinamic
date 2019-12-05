'''
Created on 02.01.2019

@author: ED
'''

from PyTrinamic.ic.TMC4671.TMC4671 import TMC4671

class TMC4671_eval(TMC4671):

    def __init__(self, connection, moduleID=1):
        self.connection = connection
        
        TMC4671.__init__(self, connection=None, channel=0)

    def register(self):
        return self.tmc4671.register()

    def variants(self):
        return self.tmc4671.variants()

    def maskShift(self):
        return self.tmc4671.maskShift()

    def ic(self):
        return self.tmc4671

    " register access: use Landungsbrücke/Startrampe with MC channel"
    def writeRegister(self, registerAddress, value , channel=0):
        if channel != 0:
            raise ValueError
        return self.connection.writeMC(registerAddress, value)

    def readRegister(self, registerAddress, channel=0, signed=False):
        if channel != 0:
            raise ValueError
        return self.connection.readMC(registerAddress, signed=signed)

class _APs():
    MaxVelocity                    = 4
    Acceleration                   = 11
    EnableRamp                     = 12
    RampVelocity                   = 13
    TargetTorque                   = 171
    PID_FLUX_TARGET                = 172
    PID_VELOCITY_TARGET            = 173
    TargetPosition                 = 174
    ActualTorque                   = 176
    ActualVelocity                 = 178
    ActualPosition                 = 179
    TargetTorqueRaw                = 189
    PIDIN_TARGET_FLUX              = 191
    TargetVelocity                 = 192
    torqueMeasurementFactor        = 251
    StartEncoderInitialization     = 252
    EncoderInitState               = 253
    ActualEncoderWaitTime          = 254
