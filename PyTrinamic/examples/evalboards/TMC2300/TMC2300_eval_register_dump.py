#!/usr/bin/env python3
'''
Dump all register values of the TMC2300 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 27.03.2020

@author: JM
'''

import PyTrinamic
from PyTrinamic.evalboards.TMC2300_eval import TMC2300_eval

PyTrinamic.showInfo()

from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]
TMC2300 = TMC2300_eval(myInterface)

print("DRVSTATUS_MSTEP:       0x{0:08X}".format(TMC2300.readRegister(TMC2300.registers.DRVSTATUS_MSTEP)))
print("DRVSTATUS_SG:          0x{0:08X}".format(TMC2300.readRegister(TMC2300.registers.DRVSTATUS_SG)))
print("DRVSTATUS_SG_SE:       0x{0:08X}".format(TMC2300.readRegister(TMC2300.registers.DRVSTATUS_SG_SE)))
print("DRVCTRL:               0x{0:08X}".format(TMC2300.readRegister(TMC2300.registers.DRVCTRL)))
print("CHOPCONF:              0x{0:08X}".format(TMC2300.readRegister(TMC2300.registers.CHOPCONF)))
print("SMARTEN:               0x{0:08X}".format(TMC2300.readRegister(TMC2300.registers.SMARTEN)))
print("SGCSCONF:              0x{0:08X}".format(TMC2300.readRegister(TMC2300.registers.SGCSCONF)))
print("DRVCONF:               0x{0:08X}".format(TMC2300.readRegister(TMC2300.registers.DRVCONF)))

myInterface.close()
