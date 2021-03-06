# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2IC(StallGuard2):

    def writeRegisterField(self, axis, field, value):
        raise NotImplementedError()

    def readRegisterField(self, axis, field, signed=False):
        raise NotImplementedError()

    def setStallguard2Filter(self, axis, filter):
        self.writeRegisterField(axis, self.fields.SFILT, filter)

    def setStallguard2Threshold(self, axis, threshold):
        self.writeRegisterField(axis, self.fields.SGT, filter)

    def setStopOnStallVelocity(self, axis, velocity):
        self.writeRegisterField(axis, self.fields.TCOOLTHRS, velocity)

    def getStallguard2Filter(self, axis):
        return self.readRegisterField(axis, self.fields.SFILT)

    def getStallguard2Threshold(self, axis):
        return self.readRegisterField(axis, self.fields.SGT)

    def getStopOnStallVelocity(self, axis):
        return self.readRegisterField(axis, self.fields.TCOOLTHRS)
