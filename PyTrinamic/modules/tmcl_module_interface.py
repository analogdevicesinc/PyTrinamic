'''
Created on 29.09.2020

@author: ED
'''

from abc import ABC, abstractmethod

class tmcl_module_interface(ABC):
    
    def __init__(self, connection, moduleID):
        self.connection = connection
        self.moduleID = moduleID
        self._motors = []

    @abstractmethod
    def moduleName(self):
        pass
    
    @abstractmethod
    def moduleDescription(self):
        pass
    
    def motorCount(self):
        return len(self._motors)
    
    def motor(self, motorID):
        return self._motors[motorID]

    def showModuleInfo(self):
        print("%s:" % self.moduleName())
        print("\tModuleID: %d" % self.moduleID)
        for m in self._motors:
            m.showMotorInfo("\t")
        pass
        
    " multi axis parameter access "
    def setAxisParameter(self, axis, apType, value):
        self.connection.setAxisParameterRaw(self.moduleID, axis, apType, value)

    def axisParameter(self, axis, apType):
        return self.connection.axisParameterRaw(self.moduleID, axis, apType)
   
    " global parameter access "
    def setGlobalParameter(self, bank, gpType, value):
        self.connection.setGlobalParameterRaw(self.moduleID, bank, gpType, value)

    def globalParameter(self, bank, gpType):
        return self.connection.globalParameterRaw(self.moduleID, bank, gpType)

    " read inputs " 
    def analogInput(self, x):
        return self.connection.analogInputRaw(self.moduleID, x)

    def digitalInput(self, x):
        return self.connection.digitalInputRaw(self.moduleID, x)

    def digitalOutput(self, x):
        return self.connection.digitalOutputRaw(self.moduleID, x)

    " write outputs "
    def setDigitalOutput(self, x):
        return self.connection.setDigitalOutputRaw(self.moduleID, x, 1)

    def clearDigitalOutput(self, x):
        return self.connection.setDigitalOutputRaw(self.moduleID, x, 0)
