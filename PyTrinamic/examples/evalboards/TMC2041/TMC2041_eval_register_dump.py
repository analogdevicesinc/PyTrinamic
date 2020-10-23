#!/usr/bin/env python3
'''
Dump all register values of the TMC2041 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 24.10.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.evalboards.TMC2041_eval import TMC2041_eval

PyTrinamic.showInfo()

from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]
TMC2041 = TMC2041_eval(myInterface)

print("GCONF:         0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.GCONF)))
print("GSTAT:         0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.GSTAT)))
print("IFCNT:         0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.IFCNT)))
print("TEST_SEL:      0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.TEST_SEL)))
print("INPUT:         0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.INPUT)))
print("IHOLD_IRUN_M1: 0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.IHOLD_IRUN_M1)))
print("MSCNT_M1:      0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.MSCNT_M1)))
print("MSCURACT_M1:      0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.MSCURACT_M1)))
print("CHOPCONF_M1:      0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.CHOPCONF_M1)))
print("COOLCONF_M1:      0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.COOLCONF_M1)))
print("DRV_STATUS_M1:      0x{0:08X}".format(TMC2041.readRegister(TMC2041.registers.DRV_STATUS_M1)))

myInterface.close()
