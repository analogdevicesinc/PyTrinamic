# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.Feature import Feature

class StallGuard2(Feature):

    def setStallguard2Filter(self, axis, filter):
        raise NotImplementedError()

    def setStallguard2Threshold(self, axis, threshold):
        raise NotImplementedError()

    def setStopOnStallVelocity(self, axis, velocity):
        raise NotImplementedError()

    def getStallguard2Filter(self, axis):
        raise NotImplementedError()

    def getStallguard2Threshold(self, axis):
        raise NotImplementedError()

    def getStopOnStallVelocity(self, axis):
        raise NotImplementedError()
