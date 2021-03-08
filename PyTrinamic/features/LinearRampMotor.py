# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.LinearRamp import LinearRamp

class LinearRampMotor(LinearRamp):

    def getTargetPosition(self):
        return self.handler.getTargetPosition(self.axis)

    def setTargetPosition(self, position):
        self.handler.setTargetPosition(self.axis, position)

    def getActualPosition(self):
        return self.handler.getTargetPosition(self.axis)

    def setActualPosition(self, position):
        self.handler.setActualPosition(self.axis, position)

    def getTargetVelocity(self):
        return self.handler.getTargetPosition(self.axis)

    def setTargetVelocity(self, velocity):
        self.handler.setTargetVelocity(self.axis, velocity)

    def getActualVelocity(self):
        return self.handler.getTargetPosition(self.axis)

    def getMaxVelocity(self):
        return self.handler.getTargetPosition(self.axis)

    def setMaxVelocity(self, velocity):
        self.handler.setMaxVelocity(self.axis, velocity)

    def getMaxAcceleration(self):
        return self.handler.getTargetPosition(self.axis)

    def setMaxAcceleration(self, acceleration):
        self.handler.setMaxAcceleration(self.axis, acceleration)
