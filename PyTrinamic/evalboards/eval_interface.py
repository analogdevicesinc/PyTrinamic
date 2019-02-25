'''
Created on 22.02.2019

@author: ed
'''
import abc

class eval_interface(abc.ABC):
   
    @abc.abstractmethod
    def register(self):
        pass

    @abc.abstractmethod
    def variants(self):
        pass

    @abc.abstractmethod
    def maskShift(self):
        pass
    
    @abc.abstractmethod
    def ic(self):
        pass
    
    @abc.abstractmethod
    def writeRegister(self, registerAddress, value):
        pass
    
    @abc.abstractmethod
    def readRegister(self, registerAddress):
        pass
    
    @abc.abstractmethod
    def writeRegisterField(self, registerAddress, value, mask, shift):
        pass
     
    @abc.abstractmethod
    def readRegisterField(self, registerAddress, mask, shift):
        pass

