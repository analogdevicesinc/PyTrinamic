# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.LinearRamp import LinearRamp

class LinearRampModule(LinearRamp):

    def setAxisParameter(self, axis, parameter, value):
        raise NotImplementedError()

    def axisParameter(self, axis, parameter):
        raise NotImplementedError()

    def getTargetPosition(self, axis):
        return self.axisParameter(self.APs.TargetPosition, axis)

    def setTargetPosition(self, axis, position):
        self.setAxisParameter(self.APs.TargetPosition, axis, position)

    def getActualPosition(self, axis):
        return self.axisParameter(self.APs.ActualPosition, axis)

    def setActualPosition(self, axis, position):
        return self.setAxisParameter(self.APs.ActualPosition, axis, position)

    def getTargetVelocity(self, axis):
        return self.axisParameter(self.APs.TargetVelocity, axis)

    def setTargetVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, axis, velocity)

    def getActualVelocity(self, axis):
        return self.axisParameter(self.APs.ActualVelocity, axis)

    def getMaxVelocity(self, axis):
        return self.axisParameter(self.APs.MaxVelocity, axis)

    def setMaxVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.MaxVelocity, axis, velocity)

    def getMaxAcceleration(self, axis):
        return self.axisParameter(self.APs.MaxAcceleration, axis)

    def setMaxAcceleration(self, axis, acceleration):
        self.setAxisParameter(self.APs.MaxAcceleration, axis, acceleration)
