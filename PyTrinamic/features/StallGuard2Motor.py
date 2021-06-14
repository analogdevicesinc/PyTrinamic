# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2Motor(StallGuard2):

    def setAxisParameter(self, parameter, value):
        raise NotImplementedError()

    def axisParameter(self, parameter):
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
