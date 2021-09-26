'''
Created on 30.09.2020

@author: ED
'''

from abc import ABC

class pid_ap_feature(ABC):
 
    def __init__(self, parent):
        self._motorInterface = parent
        
    " torque/flux controller "
    def torquePParameter(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.TorqueP)

    def setTorquePParameter(self, pValue):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.TorqueP, pValue)

    def torqueIParameter(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.TorqueI)
 
    def setTorqueIParameter(self, iValue):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.TorqueI, iValue)

    def setTorquePIParameter(self, pValue, iValue):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.TorqueP, pValue)
        self._motorInterface.setAxisParameter(self._motorInterface.AP.TorqueI, iValue)
        
    " velocity controller "
    def velocityPParameter(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.VelocityP)
 
    def setVelocityPParameter(self, pValue):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.VelocityP, pValue)

    def velocityIParameter(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.VelocityI)

    def setVelocityIParameter(self, iValue):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.VelocityI, iValue)

    def setVelocityPIParameter(self, pValue, iValue):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.VelocityP, pValue)
        self._motorInterface.setAxisParameter(self._motorInterface.AP.VelocityI, iValue)

    " position controller "
    def positionPParameter(self):
        return self._motorInterface.axisParameter(self._motorInterface.AP.PositionP)

    def setPositionPParameter(self, pValue):
        self._motorInterface.setAxisParameter(self._motorInterface.AP.PositionP, pValue)

    def showConfiguration(self):
        print("PI configuration:")
        print("\tTorque   P: " + str(self.torquePParameter()) + " I: " + str(self.torqueIParameter()))
        print("\tVelocity P: " + str(self.velocityPParameter()) + " I: " + str(self.velocityIParameter()))
        print("\tPosition P: " + str(self.positionPParameter()))
