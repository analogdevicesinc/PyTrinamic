#!/usr/bin/env python3
'''
Dump all register values of the TMC5130 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 09.01.2019

@author: LK
'''

import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.evalboards.TMC5130_eval import TMC5130_eval

pytrinamic.show_info()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
eval = TMC5130_eval(myInterface)
ic = eval.IC

print("GCONF:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.GCONF)))
print("GSTAT:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.GSTAT)))
print("IFCNT:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.IFCNT)))
print("SLAVECONF:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.SLAVECONF)))
print("INP_OUT:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.INP_OUT)))
print("X_COMPARE:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.X_COMPARE)))
print("IHOLD_IRUN:  0x{0:08X}".format(ic.read_register(ic.REGISTERS.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(ic.read_register(ic.REGISTERS.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.TPWMTHRS)))
print("TCOOLTHRS:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.TCOOLTHRS)))
print("THIGH:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.THIGH)))
print("RAMPMODE:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.RAMPMODE)))
print("XACTUAL:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.XACTUAL)))
print("VACTUAL:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.VACTUAL)))
print("VSTART:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.VSTART)))
print("A1:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.A1)))
print("V1:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.V1)))
print("AMAX:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.AMAX)))
print("VMAX:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.VMAX)))
print("DMAX:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.DMAX)))
print("D1:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.D1)))
print("VSTOP:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.VSTOP)))
print("TZEROWAIT:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.TZEROWAIT)))
print("XTARGET:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.XTARGET)))
print("VDCMIN:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.VDCMIN)))
print("SWMODE:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.SWMODE)))
print("RAMPSTAT:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.RAMPSTAT)))
print("XLATCH:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.XLATCH)))
print("ENCMODE:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.ENCMODE)))
print("XENC:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.XENC)))
print("ENC_CONST:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.ENC_CONST)))
print("ENC_STATUS:  0x{0:08X}".format(ic.read_register(ic.REGISTERS.ENC_STATUS)))
print("ENC_LATCH:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.ENC_LATCH)))
print("MSLUT0:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT0)))
print("MSLUT1:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT1)))
print("MSLUT2:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT2)))
print("MSLUT3:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT3)))
print("MSLUT4:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT4)))
print("MSLUT5:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT5)))
print("MSLUT6:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT6)))
print("MSLUT7:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT7)))
print("MSLUTSEL:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUTSEL)))
print("MSLUTSTART:  0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUTSTART)))
print("MSCNT:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.CHOPCONF)))
print("COOLCONF:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.COOLCONF)))
print("DCCTRL:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.DCCTRL)))
print("DRVSTATUS:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.DRVSTATUS)))
print("PWMCONF:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.PWMCONF)))
print("PWMSTATUS:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.PWMSTATUS)))
print("ENCM_CTRL:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.ENCM_CTRL)))
print("LOST_STEPS:  0x{0:08X}".format(ic.read_register(ic.REGISTERS.LOST_STEPS)))

myInterface.close()
