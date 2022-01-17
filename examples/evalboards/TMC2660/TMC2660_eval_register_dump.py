#!/usr/bin/env python3
'''
Dump all register values of the TMC2660 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 07.11.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.evalboards.TMC2660_eval import TMC2660_eval

PyTrinamic.show_info()

from PyTrinamic.connections.ConnectionManager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC2660 = TMC2660_eval(myInterface)

print("DRVSTATUS_MSTEP:       0x{0:08X}".format(TMC2660.readRegister(TMC2660.registers.DRVSTATUS_MSTEP)))
print("DRVSTATUS_SG:          0x{0:08X}".format(TMC2660.readRegister(TMC2660.registers.DRVSTATUS_SG)))
print("DRVSTATUS_SG_SE:       0x{0:08X}".format(TMC2660.readRegister(TMC2660.registers.DRVSTATUS_SG_SE)))
print("DRVCTRL:               0x{0:08X}".format(TMC2660.readRegister(TMC2660.registers.DRVCTRL)))
print("CHOPCONF:              0x{0:08X}".format(TMC2660.readRegister(TMC2660.registers.CHOPCONF)))
print("SMARTEN:               0x{0:08X}".format(TMC2660.readRegister(TMC2660.registers.SMARTEN)))
print("SGCSCONF:              0x{0:08X}".format(TMC2660.readRegister(TMC2660.registers.SGCSCONF)))
print("DRVCONF:               0x{0:08X}".format(TMC2660.readRegister(TMC2660.registers.DRVCONF)))

myInterface.close()
