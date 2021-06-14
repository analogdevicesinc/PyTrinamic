# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.Feature import Feature

class LinearRamp(Feature):

    def getTargetPosition(self, axis):
        raise NotImplementedError()

    def setTargetPosition(self, axis, position):
        raise NotImplementedError()

    def getActualPosition(self, axis):
        raise NotImplementedError()

    def setActualPosition(self, axis, position):
        raise NotImplementedError()

    def getTargetVelocity(self, axis):
        raise NotImplementedError()

    def setTargetVelocity(self, axis, velocity):
        raise NotImplementedError()

    def getActualVelocity(self, axis):
        raise NotImplementedError()

    def getMaxVelocity(self, axis):
        raise NotImplementedError()

    def setMaxVelocity(self, axis, velocity):
        raise NotImplementedError()

    def getMaxAcceleration(self, axis):
        raise NotImplementedError()

    def setMaxAcceleration(self, axis, acceleration):
        raise NotImplementedError()

    def showMotionConfiguration(self, axis):
        print("Motion configuration:")
        print("\tMax velocity: " + str(self.getMaxVelocity(axis)))
        print("\tAcceleration: " + str(self.getMaxAcceleration(axis)))
