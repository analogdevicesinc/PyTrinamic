'''
Created on 29.09.2020

@author: ED
'''

from abc import ABC
from PyTrinamic.helpers import TMC_helpers

class tmcl_motor_interface(ABC):

    def __init__(self, parent, axisID, motorType, axisParameter, constants):
        self._moduleInterface = parent
        self._axisId = axisID
        self._motorType = motorType
        self.AP = axisParameter
        self.ENUM = constants
        self.feature = {}

    def showMotorInfo(self, indent=""):
        print("%sMotor_%d:" % (indent, self._axisId))
        print("%s\tType: %s" % (indent, self.motorTypeToString(self._motorType)))
        print("%s\tFeatures:" % (indent))
        for key in self.feature:
            print("%s\t\t%s" % (indent, key))

    def motorTypeToString(self, motorType):
        switcher = {
            0: "DC",
            1: "BLDC",
            2: "DC_BLDC",
            3: "STEPPER",
            4: "DC_BLDC_STEPPER"
        }
        return switcher.get(motorType, "Unknown motor type >%d<!" % motorType)

    " single axis parameter access "
    def setAxisParameter(self, apType, value):
        self._moduleInterface.setAxisParameter(self._axisId, apType, value)

    def axisParameter(self, apType):
        return self._moduleInterface.axisParameter(self._axisId, apType)

    " motor poles "  
    def setMotorPoles(self, poles):
        self.setAxisParameter(self.AP.MotorPoles, poles)
        
    def motorPoles(self):
        return self.axisParameter(self.AP.MotorPoles)

    " max torque "
    def setMaxTorque(self, maxTorque):
        self.setAxisParameter(self.AP.MaxTorque, maxTorque)

    def maxTorque(self):
        return self.axisParameter(self.AP.MaxTorque)

    def statusFlags(self):
        return self.axisParameter(self.AP.StatusFlags)

    def showConfiguration(self):
        print("Motor configuration:")
        print("\tMotor poles: " + str(self.motorPoles()))
        print("\tMax torque:  " + str(self.maxTorque()) + " mA")

    " motion control functions "
    
    " torque mode"
    def setTargetTorque(self, torque):
        self.setAxisParameter(self.AP.TargetTorque, torque)
 
    def targetTorque(self):
        return TMC_helpers.toSigned32(self.axisParameter(self.AP.TargetTorque))
 
    def actualTorque(self):
        return TMC_helpers.toSigned32(self.axisParameter(self.AP.ActualTorque))
    
    " velocity mode "
    def rotate(self, velocity):
        self.setAxisParameter(self.AP.TargetVelocity, velocity)
        
    def setTargetVelocity(self, velocity):
        self.setAxisParameter(self.AP.TargetVelocity, velocity)
      
    def targetVelocity(self):
        return self.axisParameter(self.AP.TargetVelocity)  

    def actualVelocity(self):
        return TMC_helpers.toSigned32(self.axisParameter(self.AP.ActualVelocity))

    " position mode "
    def moveToPosition(self, position):
        self.setAxisParameter(self.AP.TargetPosition, position)

    def setTargetPosition(self, position):
        self.setAxisParameter(self.AP.TargetPosition, position)
 
    def targetPosition(self):
        return TMC_helpers.toSigned32(self.axisParameter(self.AP.TargetPosition))

    def setActualPosition(self, position):
        return self.setAxisParameter(self.AP.ActualPosition, position)
 
    def actualPosition(self):
        return TMC_helpers.toSigned32(self.axisParameter(self.AP.ActualPosition))

    def positionReachedFlag(self):
        return ((self.statusFlags() & self.ENUM.FLAG_POSITION_END) != 0)                    
