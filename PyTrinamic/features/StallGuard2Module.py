# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2Module(StallGuard2):

    def setAxisParameter(self, axis, parameter, value):
        raise NotImplementedError()

    def getAxisParameter(self, axis, parameter):
        raise NotImplementedError()

    def setStallguard2Filter(self, axis, filter):
        self.setAxisParameter(self.APs.SG2FilterEnable, axis, filter)

    def setStallguard2Threshold(self, axis, threshold):
        self.setAxisParameter(self.APs.SG2Threshold, axis, threshold)

    def setStopOnStallVelocity(self, axis, velocity):
        self.setAxisParameter(self.APs.SmartEnergyStallVelocity, axis, velocity)

    def getStallguard2Filter(self, axis):
        return self.getAxisParameter(self.APs.SG2FilterEnable, axis)

    def getStallguard2Threshold(self, axis):
        return self.getAxisParameter(self.APs.SG2Threshold, axis)

    def getStopOnStallVelocity(self, axis):
        return self.getAxisParameter(self.APs.SmartEnergyStallVelocity, axis)
