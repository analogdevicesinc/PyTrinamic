# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2Motor(StallGuard2):

    class __GROUPING:

        def __init__(self, parent):
            self.parent = parent

        def setStallguard2Filter(self, filter):
            self.parent.setStallguard2Filter(filter)

        def setStallguard2Threshold(self, threshold):
            self.parent.setStallguard2Threshold(threshold)

        def setStopOnStallVelocity(self, velocity):
            self.parent.setStopOnStallVelocity(velocity)

        def getStallguard2Filter(self):
            return self.parent.getStallguard2Filter()

        def getStallguard2Threshold(self):
            return self.parent.getStallguard2Threshold()

        def getStopOnStallVelocity(self):
            return self.parent.getStopOnStallVelocity()

    def __init__(self):
        self.StallGuard2 = self.__GROUPING(self)

    def setAxisParameter(self, parameter, value):
        raise NotImplementedError()

    def axisParameter(self, parameter, signed=False):
        raise NotImplementedError()

    def setStallguard2Filter(self, filter):
        self.setAxisParameter(self.APs.SG2FilterEnable, filter)

    def setStallguard2Threshold(self, threshold):
        self.setAxisParameter(self.APs.SG2Threshold, threshold)

    def setStopOnStallVelocity(self, velocity):
        self.setAxisParameter(self.APs.SmartEnergyStallVelocity, velocity)

    def getStallguard2Filter(self):
        return self.axisParameter(self.APs.SG2FilterEnable)

    def getStallguard2Threshold(self):
        return self.axisParameter(self.APs.SG2Threshold)

    def getStopOnStallVelocity(self):
        return self.axisParameter(self.APs.SmartEnergyStallVelocity)
