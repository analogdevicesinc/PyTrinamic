#!/usr/bin/env python3
'''
Dump all register values of the TMC2130 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 14.10.2019

@author: JM
'''

import pytrinamic
from pytrinamic.evalboards.TMC2130_eval import TMC2130_eval

pytrinamic.show_info()

from pytrinamic.connections.ConnectionManager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC2130 = TMC2130_eval(myInterface)

print("GCONF:       0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.GCONF)))
print("GSTAT:       0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.GSTAT)))
print("IFCNT:       0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.IFCNT)))
print("SLAVECONF:   0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.SLAVECONF)))
print("INP_OUT:     0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.INP_OUT)))
print("X_COMPARE:   0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.X_COMPARE)))
print("IHOLD_IRUN:  0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.TPWMTHRS)))
print("TCOOLTHRS:   0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.TCOOLTHRS)))
print("THIGH:       0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.THIGH)))
print("TZEROWAIT:   0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.TZEROWAIT)))
print("XTARGET:     0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.XTARGET)))
print("VDCMIN:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.VDCMIN)))
print("SWMODE:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.SWMODE)))
print("RAMPSTAT:    0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.RAMPSTAT)))
print("XLATCH:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.XLATCH)))
print("ENCMODE:     0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.ENCMODE)))
print("XENC:        0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.XENC)))
print("ENC_CONST:   0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.ENC_CONST)))
print("ENC_STATUS:  0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.ENC_STATUS)))
print("ENC_LATCH:   0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.ENC_LATCH)))
print("MSLUT0:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUT0)))
print("MSLUT1:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUT1)))
print("MSLUT2:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUT2)))
print("MSLUT3:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUT3)))
print("MSLUT4:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUT4)))
print("MSLUT5:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUT5)))
print("MSLUT6:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUT6)))
print("MSLUT7:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUT7)))
print("MSLUTSEL:    0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUTSEL)))
print("MSLUTSTART:  0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSLUTSTART)))
print("MSCNT:       0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.CHOPCONF)))
print("COOLCONF:    0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.COOLCONF)))
print("DCCTRL:      0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.DCCTRL)))
print("DRVSTATUS:   0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.DRVSTATUS)))
print("PWMCONF:     0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.PWMCONF)))
print("PWMSTATUS:   0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.PWMSTATUS)))
print("ENCM_CTRL:   0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.ENCM_CTRL)))
print("LOST_STEPS:  0x{0:08X}".format(TMC2130.readRegister(TMC2130.registers.LOST_STEPS)))

myInterface.close()
