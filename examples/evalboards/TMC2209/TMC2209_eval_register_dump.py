#!/usr/bin/env python3
'''
Dump all register values of the TMC2209 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 18.10.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.evalboards.TMC2209_eval import TMC2209_eval

PyTrinamic.show_info()

from PyTrinamic.connections.ConnectionManager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC2209 = TMC2209_eval(myInterface)

print("GCONF:       0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.GCONF)))
print("GSTAT:       0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.GSTAT)))
print("IFCNT:       0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.IFCNT)))
print("SLAVECONF:   0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.SLAVECONF)))
print("IHOLD_IRUN:  0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.TPWMTHRS)))
print("TCOOLTHRS:   0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.TCOOLTHRS)))
print("VACTUAL:     0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.VACTUAL)))
print("SGTHRS:      0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.SGTHRS)))
print("SG_RESULT:   0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.SG_RESULT)))
print("COOLCONF:    0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.COOLCONF)))
print("MSCNT:       0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.CHOPCONF)))
print("DRVSTATUS:   0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.DRVSTATUS)))
print("PWMCONF:     0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.PWMCONF)))
print("PWMSCALE:    0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.PWMSCALE)))
print("PWMAUTO:     0x{0:08X}".format(TMC2209.readRegister(TMC2209.registers.PWMAUTO)))

myInterface.close()
