#!/usr/bin/env python3
'''
Dump all register values of the TMC2224 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 07.02.2020

@author: JM
'''

import pytrinamic2
from pytrinamic2.evalboards.TMC2224_eval import TMC2224_eval

pytrinamic2.show_info()

from pytrinamic2.connections.connection_manager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC2224 = TMC2224_eval(myInterface)

print("GCONF:       0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.GCONF)))
print("GSTAT:       0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.GSTAT)))
print("IFCNT:       0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.IFCNT)))
print("SLAVECONF:   0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.SLAVECONF)))
print("IHOLD_IRUN:  0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.TPWMTHRS)))
print("MSCNT:       0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.CHOPCONF)))
print("DRVSTATUS:   0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.DRVSTATUS)))
print("PWMCONF:     0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.PWMCONF)))
print("PWMSCALE:    0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.PWMSCALE)))
print("PWMAUTO:     0x{0:08X}".format(TMC2224.readRegister(TMC2224.registers.PWMAUTO)))

myInterface.close()
