# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.LinearRamp import LinearRamp

class LinearRampMotor(LinearRamp):

    class __GROUPING:

        def __init__(self, parent):
            self.parent = parent

        def getTargetPosition(self):
            return self.parent.getTargetPosition()

        def setTargetPosition(self, position):
            self.parent.setTargetPosition(position)

        def getActualPosition(self):
            return self.parent.getActualPosition()

        def setActualPosition(self, position):
            self.parent.setActualPosition(position)

        def getTargetVelocity(self):
            return self.parent.getTargetVelocity()

        def setTargetVelocity(self, velocity):
            self.parent.setTargetVelocity(velocity)

        def getActualVelocity(self):
            return self.parent.getActualVelocity()

        def getMaxVelocity(self):
            return self.parent.getMaxVelocity()

        def setMaxVelocity(self, velocity):
            self.parent.setMaxVelocity(velocity)

        def getMaxAcceleration(self):
            return self.parent.getMaxAcceleration()

        def setMaxAcceleration(self, acceleration):
            self.parent.setMaxAcceleration(acceleration)

    def __init__(self):
        self.LinearRamp = self.__GROUPING(self)

    def setAxisParameter(self, parameter, value):
        raise NotImplementedError()

    def axisParameter(self, parameter, signed=False):
        raise NotImplementedError()

    def getTargetPosition(self):
        return self.axisParameter(self.APs.TargetPosition)

    def setTargetPosition(self, position):
        self.setAxisParameter(self.APs.TargetPosition, position)

    def getActualPosition(self):
        return self.axisParameter(self.APs.ActualPosition)

    def setActualPosition(self, position):
        self.setAxisParameter(self.APs.ActualPosition, position)

    def getTargetVelocity(self):
        return self.axisParameter(self.APs.TargetVelocity)

    def setTargetVelocity(self, velocity):
        self.setAxisParameter(self.APs.TargetVelocity, velocity)

    def getActualVelocity(self):
        return self.axisParameter(self.APs.ActualVelocity)

    def getMaxVelocity(self):
        return self.axisParameter(self.APs.MaxVelocity)

    def setMaxVelocity(self, velocity):
        self.setAxisParameter(self.APs.MaxVelocity, velocity)

    def getMaxAcceleration(self):
        return self.axisParameter(self.APs.MaxAcceleration)

    def setMaxAcceleration(self, acceleration):
        self.setAxisParameter(self.APs.MaxAcceleration, acceleration)
