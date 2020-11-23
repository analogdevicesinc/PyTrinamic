#!/usr/bin/env python3
'''
Dump all register values of the TMC2590 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 07.02.2020

@author: JM
'''
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC2590_eval import TMC2590_eval

PyTrinamic.showInfo()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC2590 = TMC2590_eval(myInterface)

print("DRVSTATUS___MSTEP:              0x{0:08X}".format(TMC2590.readRegister(TMC2590.registers.DRVSTATUS___MSTEP)))
print("DRVSTATUS___SG:                 0x{0:08X}".format(TMC2590.readRegister(TMC2590.registers.DRVSTATUS___SG)))
print("DRVSTATUS___SG_SE:              0x{0:08X}".format(TMC2590.readRegister(TMC2590.registers.DRVSTATUS___SG_SE)))
print("DRVCTRL:                        0x{0:08X}".format(TMC2590.readRegister(TMC2590.registers.DRVCTRL)))
print("CHOPCONF:                       0x{0:08X}".format(TMC2590.readRegister(TMC2590.registers.CHOPCONF)))
print("SMARTEN:                        0x{0:08X}".format(TMC2590.readRegister(TMC2590.registers.SMARTEN)))
print("SGCSCONF:                       0x{0:08X}".format(TMC2590.readRegister(TMC2590.registers.SGCSCONF)))
print("DRVCONF:                        0x{0:08X}".format(TMC2590.readRegister(TMC2590.registers.DRVCONF)))

myInterface.close()