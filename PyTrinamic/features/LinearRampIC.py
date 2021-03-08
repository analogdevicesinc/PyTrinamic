# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.LinearRamp import LinearRamp

class LinearRampIC(LinearRamp):

    def writeRegisterField(self, axis, field, value):
        raise NotImplementedError()

    def readRegisterField(self, axis, field, signed=False):
        raise NotImplementedError()

    def getTargetPosition(self, axis):
        return self.readRegisterField(axis, self.fields.XTARGET)

    def setTargetPosition(self, axis, position):
        self.writeRegisterField(axis, self.fields.XTARGET, position)

    def getActualPosition(self, axis):
        return self.readRegisterField(axis, self.fields.XACTUAL)

    def setActualPosition(self, axis, position):
        self.writeRegisterField(axis, self.fields.XACTUAL, position)

    def getTargetVelocity(self, axis):
        return self.readRegisterField(axis, self.fields.VMAX)

    def setTargetVelocity(self, axis, velocity):
        self.writeRegisterField(axis, self.fields.VMAX, velocity)

    def getActualVelocity(self, axis):
        return self.readRegisterField(axis, self.fields.VACTUAL)

    def getMaxVelocity(self, axis):
        return self.readRegisterField(axis, self.fields.VMAX)

    def setMaxVelocity(self, axis, velocity):
        self.writeRegisterField(axis, self.fields.VMAX, velocity)

    def getMaxAcceleration(self, axis):
        return self.readRegisterField(axis, self.fields.AMAX)

    def setMaxAcceleration(self, axis, acceleration):
        self.writeRegisterField(axis, self.fields.AMAX, acceleration)
