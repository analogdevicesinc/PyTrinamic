#!/usr/bin/env python3
'''
Dump all register values of the TMC2208 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 17.10.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.evalboards.TMC2208_eval import TMC2208_eval

PyTrinamic.showInfo()

from PyTrinamic.connections.ConnectionManager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC2208 = TMC2208_eval(myInterface)

print("GCONF:       0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.GCONF)))
print("GSTAT:       0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.GSTAT)))
print("IFCNT:       0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.IFCNT)))
print("SLAVECONF:   0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.SLAVECONF)))
print("IHOLD_IRUN:  0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.TPWMTHRS)))
print("MSCNT:       0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.CHOPCONF)))
print("DRVSTATUS:   0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.DRVSTATUS)))
print("PWMCONF:     0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.PWMCONF)))
print("PWMSCALE:    0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.PWMSCALE)))
print("PWMAUTO:     0x{0:08X}".format(TMC2208.readRegister(TMC2208.registers.PWMAUTO)))

myInterface.close()
