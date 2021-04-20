# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2Motor(StallGuard2):

    def setStallguard2Filter(self, filter):
        self.handler.setStallguard2Filter(self.axis, filter)

    def setStallguard2Threshold(self, threshold):
        self.handler.setStallguard2Threshold(self.axis, threshold)

    def setStopOnStallVelocity(self, velocity):
        self.handler.setStopOnStallVelocity(self.axis, velocity)

    def getStallguard2Filter(self):
        return self.handler.getStallguard2Filter(self.axis)

    def getStallguard2Threshold(self):
        return self.handler.getStallguard2Threshold(self.axis)

    def getStopOnStallVelocity(self):
        return self.handler.getStopOnStallVelocity(self.axis)
