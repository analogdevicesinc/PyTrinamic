# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.LinearRamp import LinearRamp

class LinearRampIC(LinearRamp):

    def writeRegisterField(self, field, value, axis=0):
        raise NotImplementedError()

    def readRegisterField(self, field, signed=False, axis=0):
        raise NotImplementedError()

    def getTargetPosition(self, axis):
        return self.readRegisterField(self.fields.XTARGET, axis=axis)

    def setTargetPosition(self, axis, position):
        self.writeRegisterField(self.fields.XTARGET, position, axis=axis)

    def getActualPosition(self, axis):
        return self.readRegisterField(self.fields.XACTUAL, axis=axis)

    def setActualPosition(self, axis, position):
        self.writeRegisterField(self.fields.XACTUAL, position, axis=axis)

    def getTargetVelocity(self, axis):
        return self.readRegisterField(self.fields.VMAX, axis=axis)

    def setTargetVelocity(self, axis, velocity):
        self.writeRegisterField(self.fields.VMAX, velocity, axis=axis)

    def getActualVelocity(self, axis):
        return self.readRegisterField(self.fields.VACTUAL, axis=axis)

    def getMaxVelocity(self, axis):
        return self.readRegisterField(self.fields.VMAX, axis=axis)

    def setMaxVelocity(self, axis, velocity):
        self.writeRegisterField(self.fields.VMAX, velocity, axis=axis)

    def getMaxAcceleration(self, axis):
        return self.readRegisterField(self.fields.AMAX, axis=axis)

    def setMaxAcceleration(self, axis, acceleration):
        self.writeRegisterField(self.fields.AMAX, acceleration, axis=axis)
