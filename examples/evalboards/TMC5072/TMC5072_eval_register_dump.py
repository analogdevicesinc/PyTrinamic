#!/usr/bin/env python3
'''
Dump all register values of the TMC5072 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 20.09.2019

@author: JM
'''
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC5072_eval import TMC5072_eval

PyTrinamic.show_info()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
eval = TMC5072_eval(myInterface)
ic = eval.IC

print("GCONF:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.GCONF)))
print("GSTAT:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.GSTAT)))
print("SLAVECONF:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.SLAVECONF)))
print("INPUT:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.INPUT___OUTPUT)))
print("X_COMPARE:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.X_COMPARE)))

print("PWMCONF_M1:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.PWMCONF_M1)))
print("PWM_STATUS_M1:  0x{0:08X}".format(ic.read_register(ic.REGISTERS.PWM_STATUS_M1)))
print("PWMCONF_M2:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.PWMCONF_M2)))
print("PWM_STATUS_M2:  0x{0:08X}".format(ic.read_register(ic.REGISTERS.PWM_STATUS_M2)))

print("RAMPMODE_M1:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.RAMPMODE_M1)))
print("XACTUAL_M1:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.XACTUAL_M1)))
print("VACTUAL_M1:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.VACTUAL_M1)))
print("VSTART_M1:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.VSTART_M1)))
print("A1_M1:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.A1_M1)))
print("V1_M1:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.V1_M1)))
print("AMAX_M1:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.AMAX_M1)))
print("VMAX_M1:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.VMAX_M1)))
print("DMAX_M1:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.DMAX_M1)))
print("D1_M1:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.D1_M1)))
print("VSTOP_M1:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.VSTOP_M1)))
print("TZEROWAIT_M1:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.TZEROWAIT_M1)))
print("XTARGET_M1:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.XTARGET_M1)))
print("IHOLD_IRUN_M1:  0x{0:08X}".format(ic.read_register(ic.REGISTERS.IHOLD_IRUN_M1)))
print("VCOOLTHRS_M1:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.VCOOLTHRS_M1)))
print("VHIGH_M1:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.VHIGH_M1)))
print("RAMPMODE_M2:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.RAMPMODE_M2)))
print("XACTUAL_M2:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.XACTUAL_M2)))
print("VACTUAL_M2:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.VACTUAL_M2)))
print("VSTART_M2:      0x{0:08X}".format(ic.read_register(ic.REGISTERS.VSTART_M2)))
print("A1_M2:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.A1_M2)))
print("V1_M2:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.V1_M2)))
print("AMAX_M2:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.AMAX_M2)))
print("VMAX_M2:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.VMAX_M2)))
print("DMAX_M2:        0x{0:08X}".format(ic.read_register(ic.REGISTERS.DMAX_M2)))
print("D1_M2:          0x{0:08X}".format(ic.read_register(ic.REGISTERS.D1_M2)))
print("VSTOP_M2:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.VSTOP_M2)))
print("TZEROWAIT_M2:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.TZEROWAIT_M2)))
print("XTARGET_M2:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.XTARGET_M2)))
print("IHOLD_IRUN_M2:  0x{0:08X}".format(ic.read_register(ic.REGISTERS.IHOLD_IRUN_M2)))
print("VCOOLTHRS_M2:   0x{0:08X}".format(ic.read_register(ic.REGISTERS.VCOOLTHRS_M2)))
print("VHIGH_M2:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.VHIGH_M2)))

print("MSLUT0:         0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT_0)))
print("MSLUT1:         0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT_1)))
print("MSLUT2:         0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT_2)))
print("MSLUT3:         0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT_3)))
print("MSLUT4:         0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT_4)))
print("MSLUT5:         0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT_5)))
print("MSLUT6:         0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT_6)))
print("MSLUT7:         0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUT_7)))
print("MSLUTSEL:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUTSEL)))
print("MSLUTSTART:     0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSLUTSTART)))

print("MSCNT_M1:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSCNT_M1)))
print("MSCURACT_M1:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSCURACT_M1)))
print("CHOPCONF_M1:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.CHOPCONF_M1)))
print("COOLCONF_M1:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.COOLCONF_M1)))
print("MSCNT_M2:       0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSCNT_M2)))
print("MSCURACT_M2:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.MSCURACT_M2)))
print("CHOPCONF_M2:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.CHOPCONF_M2)))
print("COOLCONF_M2:    0x{0:08X}".format(ic.read_register(ic.REGISTERS.COOLCONF_M2)))

myInterface.close()
