#!/usr/bin/env python3
'''
Dump all register values of the TMC2225 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 17.10.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.evalboards.TMC2225_eval import TMC2225_eval

PyTrinamic.showInfo()

from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]
TMC2225 = TMC2225_eval(myInterface)

print("GCONF:       0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.GCONF)))
print("GSTAT:       0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.GSTAT)))
print("IFCNT:       0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.IFCNT)))
print("SLAVECONF:   0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.SLAVECONF)))
print("IHOLD_IRUN:  0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.TPWMTHRS)))
print("MSCNT:       0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.CHOPCONF)))
print("DRVSTATUS:   0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.DRVSTATUS)))
print("PWMCONF:     0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.PWMCONF)))
print("PWMSTATUS:   0x{0:08X}".format(TMC2225.readRegister(TMC2225.registers.PWMSTATUS)))

myInterface.close()
