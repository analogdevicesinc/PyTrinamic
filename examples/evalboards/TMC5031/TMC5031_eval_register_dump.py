#!/usr/bin/env python3
'''
Dump all register values of the TMC5031 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 29.01.2020

@author: JM
'''

import pytrinamic2
from pytrinamic2.connections.connection_manager import ConnectionManager
from pytrinamic2.evalboards.TMC5031_eval import TMC5031_eval

pytrinamic2.show_info()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC5031 = TMC5031_eval(myInterface)

print("GCONF:          0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.GCONF)))
print("GSTAT:          0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.GSTAT)))
print("SLAVECONF:      0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.SLAVECONF)))
print("INPUT:          0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.INPUT)))
print("X_COMPARE:      0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.X_COMPARE)))

print("RAMPMODE_M1:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.RAMPMODE[0])))
print("XACTUAL_M1:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.XACTUAL[0])))
print("VACTUAL_M1:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VACTUAL[0])))
print("VSTART_M1:      0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VSTART[0])))
print("A1:             0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.A1[0])))
print("V1:             0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.V1[0])))
print("AMAX_M1:        0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.AMAX[0])))
print("VMAX_M1:        0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VMAX[0])))
print("DMAX_M1:        0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.DMAX[0])))
print("D1_M1:          0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.D1[0])))
print("VSTOP_M1:       0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VSTOP[0])))
print("TZEROWAIT_M1:   0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.TZEROWAIT[0])))
print("XTARGET_M1:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.XTARGET[0])))
print("IHOLD_IRUN_M1:  0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.IHOLD_IRUN[0])))
print("VCOOLTHRS_M1:   0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VCOOLTHRS[0])))
print("VHIGH_M1:       0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VHIGH[0])))
print("SW_MODE_M1:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.SWMODE[0])))
print("RAMP_STAT_M1:   0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.RAMPSTAT[0])))
print("XLATCH_M1:      0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.XLATCH[0])))
print("RAMPMODE_M2:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.RAMPMODE[1])))
print("XACTUAL_M2:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.XACTUAL[1])))
print("VACTUAL_M2:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VACTUAL[1])))
print("VSTART_M2:      0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VSTART[1])))
print("A1_M2:          0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.A1[1])))
print("V1_M2:          0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.V1[1])))
print("AMAX_M2:        0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.AMAX[1])))
print("VMAX_M2:        0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VMAX[1])))
print("DMAX_M2:        0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.DMAX[1])))
print("D1_M2:          0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.D1[1])))
print("VSTOP_M2:       0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VSTOP[1])))
print("TZEROWAIT_M2:   0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.TZEROWAIT[1])))
print("XTARGET_M2:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.XTARGET[1])))
print("IHOLD_IRUN_M2:  0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.IHOLD_IRUN[1])))
print("VCOOLTHRS_M2:   0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VCOOLTHRS[1])))
print("VHIGH_M2:       0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.VHIGH[1])))
print("SW_MODE_M2:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.SW_MODE_M2[1])))
print("RAMP_STAT_M2:   0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.RAMP_STAT_M2[1])))
print("XLATCH_M2:      0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.XLATCH[1])))

print("MSLUT___M1:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSLUT___M1)))
print("MSLUT___M2:     0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSLUT___M2)))

print("MSLUTSEL_M1:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSLUTSEL_M1)))
print("MSLUTSTART_M1:  0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSLUTSTART_M1)))
print("MSCNT_M1:       0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSCNT_M1[0])))
print("MSCURACT_M1:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSCURACT_M1[0])))
print("CHOPCONF_M1:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.CHOPCONF_M1[0])))
print("COOLCONF_M1:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.COOLCONF_M1[0])))
print("DRV_STATUS_M1:  0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.DRV_STATUS_M1[0])))

print("MSLUTSEL_M2:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSLUTSEL_M2)))
print("MSLUTSTART_M2:  0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSLUTSTART_M2)))
print("MSCNT_M2:       0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSCNT_M2[1])))
print("MSCURACT_M2:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.MSCURACT_M2[1])))
print("CHOPCONF_M2:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.CHOPCONF_M2[1])))
print("COOLCONF_M2:    0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.COOLCONF_M2[1])))
print("DRV_STATUS_M2:  0x{0:08X}".format(TMC5031.readRegister(TMC5031.registers.DRV_STATUS_M2[1])))

myInterface.close()