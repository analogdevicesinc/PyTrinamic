#!/usr/bin/env python3
'''
Dump all register values of the TMC5130 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 09.01.2019

@author: LK
'''

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval
from PyTrinamic.cli import select_com_port_by_name

PyTrinamic.showInfo()

myInterface = serial_tmcl_interface(PyTrinamic.getComPort(name=select_com_port_by_name(USB=True), return_default=False, USB=True))
TMC5130 = TMC5130_eval(myInterface)

print("GCONF:       0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.GCONF)))
print("GSTAT:       0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.GSTAT)))
print("IFCNT:       0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.IFCNT)))
print("SLAVECONF:   0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.SLAVECONF)))
print("INP_OUT:     0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.INP_OUT)))
print("X_COMPARE:   0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.X_COMPARE)))
print("IHOLD_IRUN:  0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.TPWMTHRS)))
print("TCOOLTHRS:   0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.TCOOLTHRS)))
print("THIGH:       0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.THIGH)))
print("RAMPMODE:    0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.RAMPMODE)))
print("XACTUAL:     0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.XACTUAL)))
print("VACTUAL:     0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.VACTUAL)))
print("VSTART:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.VSTART)))
print("A1:          0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.A1)))
print("V1:          0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.V1)))
print("AMAX:        0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.AMAX)))
print("VMAX:        0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.VMAX)))
print("DMAX:        0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.DMAX)))
print("D1:          0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.D1)))
print("VSTOP:       0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.VSTOP)))
print("TZEROWAIT:   0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.TZEROWAIT)))
print("XTARGET:     0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.XTARGET)))
print("VDCMIN:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.VDCMIN)))
print("SWMODE:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.SWMODE)))
print("RAMPSTAT:    0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.RAMPSTAT)))
print("XLATCH:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.XLATCH)))
print("ENCMODE:     0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.ENCMODE)))
print("XENC:        0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.XENC)))
print("ENC_CONST:   0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.ENC_CONST)))
print("ENC_STATUS:  0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.ENC_STATUS)))
print("ENC_LATCH:   0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.ENC_LATCH)))
print("MSLUT0:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUT0)))
print("MSLUT1:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUT1)))
print("MSLUT2:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUT2)))
print("MSLUT3:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUT3)))
print("MSLUT4:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUT4)))
print("MSLUT5:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUT5)))
print("MSLUT6:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUT6)))
print("MSLUT7:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUT7)))
print("MSLUTSEL:    0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUTSEL)))
print("MSLUTSTART:  0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSLUTSTART)))
print("MSCNT:       0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.CHOPCONF)))
print("COOLCONF:    0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.COOLCONF)))
print("DCCTRL:      0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.DCCTRL)))
print("DRVSTATUS:   0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.DRVSTATUS)))
print("PWMCONF:     0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.PWMCONF)))
print("PWMSTATUS:   0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.PWMSTATUS)))
print("ENCM_CTRL:   0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.ENCM_CTRL)))
print("LOST_STEPS:  0x{0:08X}".format(TMC5130.readRegister(TMC5130.registers.LOST_STEPS)))

myInterface.close()
