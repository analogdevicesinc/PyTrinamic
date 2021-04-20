# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2IC(StallGuard2):

    def writeRegisterField(self, field, value, axis=0):
        raise NotImplementedError()

    def readRegisterField(self, field, signed=False, axis=0):
        raise NotImplementedError()

    def setStallguard2Filter(self, axis, filter):
        self.writeRegisterField(self.fields.SFILT, filter, axis=axis)

    def setStallguard2Threshold(self, axis, threshold):
        self.writeRegisterField(self.fields.SGT, filter, axis=axis)

    def setStopOnStallVelocity(self, axis, velocity):
        self.writeRegisterField(self.fields.TCOOLTHRS, velocity, axis=axis)

    def getStallguard2Filter(self, axis):
        return self.readRegisterField(self.fields.SFILT, axis=axis)

    def getStallguard2Threshold(self, axis):
        return self.readRegisterField(self.fields.SGT, axis=axis)

    def getStopOnStallVelocity(self, axis):
        return self.readRegisterField(self.fields.TCOOLTHRS, axis=axis)
