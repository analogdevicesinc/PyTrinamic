'''
Created on 29.09.2020

@author: ED
'''

from abc import ABC

class linear_ramp_ap_feature(ABC):
 
    def __init__(self, parent):
        self._motorInterface = parent
            
    def maxVelocity(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.MaxVelocity)
# 
    def setMaxVelocity(self, maxVelocity):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.MaxVelocity, maxVelocity)

    def acceleration(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.Acceleration)

    def setAcceleration(self, acceleration):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.Acceleration, acceleration)

    def rampEnabled(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.EnableRamp)
 
    def setRampEnabled(self, enable):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.EnableRamp, enable)

    def targetReachedVelocity(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.TargetReachedVelocity)
 
    def setTargetReachedVelocity(self, velocity):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.TargetReachedVelocity, velocity)
 
    def targetReachedDistance(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.TargetReachedDistance)

    def setTargetReachedDistance(self, distance):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.TargetReachedDistance, distance)
 
    def motorHaltedVelocity(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.MotorHaltedVelocity)

    def setMotorHaltedVelocity(self, velocity):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.MotorHaltedVelocity, velocity)

    def showConfiguration(self):
        print("LinearRamp configuration:")
        print("\tMax velocity: " + str(self.maxVelocity()))
        print("\tAcceleration: " + str(self.acceleration()))
        print("\tRamp enabled: " + ("disabled" if (self.rampEnabled()==0) else "enabled"))
        print("\tMotor halted velocity:   " + str(self.motorHaltedVelocity()))
        print("\tTarget reached velocity: " + str(self.targetReachedVelocity()))
        print("\tTarget reached distance: " + str(self.targetReachedDistance()))
