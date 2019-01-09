'''
Created on 30.12.2018

@author: ED
'''

import struct
from serial import Serial
from PyTrinamic.TMCL import TMCL, TMCL_Command, TMCL_Request, TMCL_Reply
from PyTrinamic.helpers import TMC_helpers

class serial_tmcl_interface(object):

    def __init__(self, comPort):
        self.debugEnabled = False
        self.moduleAddress = 1
        self.serial = Serial(comPort, 115200)
        print("Open port: " + self.serial.portstr)
        
    def close( self ):
        print("Close port: " + self.serial.portstr)
        self.serial.close()
        return 0;
    
    def enableDebug(self, enable):
        self.debugEnabled = enable

    def send ( self, address, command, commandType, motorbank, value ):
        """
        Send a message to the specified module. This is a blocking function that
        will not return until a reply has been received from the module. 
        """
       
        "prepare TMCL request"
        request = TMCL_Request(address, command, commandType, motorbank, value)
        
        if self.debugEnabled:
            request.dump()
        
        "send request, wait, and handle reply"
        self.serial.write(request.toBuffer())
        reply = TMCL_Reply(struct.unpack(TMCL.PACKAGE_STRUCTURE, self.serial.read(TMCL.PACKAGE_LENGTH)))
        
        if self.debugEnabled:
            reply.dump()

        return reply

    " axis parameter access "
    def getAxisParameter(self, commandType, axis):
        return self.send(self.moduleAddress, TMCL_Command.GAP, commandType, axis, 0)
    
    def setAxisParameter(self, commandType, axis, value):
        return self.send(self.moduleAddress, TMCL_Command.SAP, commandType, axis, value)

    def storeAxisParameter(self, commandType, axis):
        return self.send(self.moduleAddress, TMCL_Command.STAP, commandType, axis, 0)

    def setAndStoreAxisParameter(self, commandType, axis, value):
        self.send(self.moduleAddress, TMCL_Command.SAP, commandType, axis, value)
        self.send(self.moduleAddress, TMCL_Command.STAP, commandType, axis, 0)
        
    " motion controller register access "
    def writeMC(self, registerAddress, value, mask=0xFFFFFFFF, shift=0):
        return self.send(self.moduleAddress, TMCL_Command.WRITE_MC, registerAddress, 0, TMC_helpers.field_set(self.readMC(registerAddress), mask, shift, value))
    
    def readMC(self, registerAddress, mask=0xFFFFFFFF, shift=0):
        return TMC_helpers.field_get(self.send(self.moduleAddress, TMCL_Command.READ_MC, registerAddress, 0, 0), mask, shift)

    " driver register access "
    def writeDRV(self, registerAddress, value):
        return self.send(self.moduleAddress, TMCL_Command.WRITE_DRV, registerAddress, 0, value)
    
    def readDRVC(self, registerAddress):
        return self.send(self.moduleAddress, TMCL_Command.READ_DRV, registerAddress, 0, 0)
