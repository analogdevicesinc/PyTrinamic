'''
Created on 29.09.2020

@author: ED
'''
from abc import ABC

class linear_ramp_ap_feature(ABC):
 
    def __init__(self, parent):
        self._motorInterface = parent
        self._hasMotorHaltedVelocity = True
        self._hasTargetReachedVelocity = True
        self._hasTargetReachedDistance = True
            
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

    def disableTargetReachedVelocity(self):
        self._hasTargetReachedVelocity = False 
        
    def targetReachedVelocity(self):
        return (self._motorInterface.axisParameter(self._motorInterface.AP.TargetReachedVelocity) if (self._hasTargetReachedVelocity==True) else 500)
    
    def setTargetReachedVelocity(self, velocity):
        if self._hasTargetReachedVelocity:
            self._motorInterface.setAxisParameter(self._motorInterface.AP.TargetReachedVelocity, velocity)
 
    def disableTargetReachedDistance(self):
        self._hasTargetReachedDistance = False
        
    def targetReachedDistance(self):
        return (self._motorInterface.axisParameter(self._motorInterface.AP.TargetReachedDistance) if (self._hasTargetReachedDistance==True) else 5)

    def setTargetReachedDistance(self, distance):
        if self._hasTargetReachedDistance:
            self._motorInterface.setAxisParameter(self._motorInterface.AP.TargetReachedDistance, distance)

    def disableMotorHaltedVelocity(self):
        self._hasMotorHaltedVelocity = False 

    def motorHaltedVelocity(self):
        return (self._motorInterface.axisParameter(self._motorInterface.AP.MotorHaltedVelocity) if (self._hasMotorHaltedVelocity==True) else 50)

    def setMotorHaltedVelocity(self, velocity):
        if self._hasMotorHaltedVelocity:
            self._motorInterface.setAxisParameter(self._motorInterface.AP.MotorHaltedVelocity, velocity)
 
    def showConfiguration(self):
        print("LinearRamp configuration:")
        print("\tMax velocity: " + str(self.maxVelocity()))
        print("\tAcceleration: " + str(self.acceleration()))
        print("\tRamp enabled: " + ("disabled" if (self.rampEnabled()==0) else "enabled"))
        if self._hasMotorHaltedVelocity:
            print("\tMotor halted velocity:   " + str(self.motorHaltedVelocity()))
        if self._hasTargetReachedVelocity:
            print("\tTarget reached velocity: " + str(self.targetReachedVelocity()))
        if self._hasTargetReachedDistance:
            print("\tTarget reached distance: " + str(self.targetReachedDistance()))
