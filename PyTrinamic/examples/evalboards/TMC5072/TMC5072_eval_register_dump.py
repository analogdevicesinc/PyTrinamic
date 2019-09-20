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

PyTrinamic.showInfo()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC5072 = TMC5072_eval(myInterface)

print("GCONF:          0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.GCONF)))
print("GSTAT:          0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.GSTAT)))
print("SLAVECONF:      0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.SLAVECONF)))
print("INPUT:          0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.INPUT)))
print("X_COMPARE:      0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.X_COMPARE)))

print("PWMCONF_M1:     0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.PWMCONF[0])))
print("PWM_STATUS_M1:  0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.PWM_STATUS[0])))
print("PWMCONF_M2:     0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.PWMCONF[1])))
print("PWM_STATUS_M2:  0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.PWM_STATUS[1])))

print("RAMPMODE_M1:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.RAMPMODE[0])))
print("XACTUAL_M1:     0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.XACTUAL[0])))
print("VACTUAL_M1:     0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VACTUAL[0])))
print("VSTART_M1:      0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VSTART[0])))
print("A1_M1:          0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.A1[0])))
print("V1_M1:          0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.V1[0])))
print("AMAX_M1:        0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.AMAX[0])))
print("VMAX_M1:        0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VMAX[0])))
print("DMAX_M1:        0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.DMAX[0])))
print("D1_M1:          0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.D1[0])))
print("VSTOP_M1:       0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VSTOP[0])))
print("TZEROWAIT_M1:   0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.TZEROWAIT[0])))
print("XTARGET_M1:     0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.XTARGET[0])))
print("IHOLD_IRUN_M1:  0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.IHOLD_IRUN[0])))
print("VCOOLTHRS_M1:   0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VCOOLTHRS[0])))
print("VHIGH_M1:       0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VHIGH[0])))
print("SWMODE_M1:      0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.SWMODE[0])))
print("RAMPSTAT_M1:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.RAMPSTAT[0])))
print("XLATCH_M1:      0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.XLATCH[0])))
print("RAMPMODE_M2:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.RAMPMODE[1])))
print("XACTUAL_M2:     0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.XACTUAL[1])))
print("VACTUAL_M2:     0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VACTUAL[1])))
print("VSTART_M2:      0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VSTART[1])))
print("A1_M2:          0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.A1[1])))
print("V1_M2:          0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.V1[1])))
print("AMAX_M2:        0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.AMAX[1])))
print("VMAX_M2:        0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VMAX[1])))
print("DMAX_M2:        0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.DMAX[1])))
print("D1_M2:          0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.D1[1])))
print("VSTOP_M2:       0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VSTOP[1])))
print("TZEROWAIT_M2:   0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.TZEROWAIT[1])))
print("XTARGET_M2:     0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.XTARGET[1])))
print("IHOLD_IRUN_M2:  0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.IHOLD_IRUN[1])))
print("VCOOLTHRS_M2:   0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VCOOLTHRS[1])))
print("VHIGH_M2:       0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.VHIGH[1])))
print("SWMODE_M2:      0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.SWMODE[1])))
print("RAMPSTAT_M2:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.RAMPSTAT[1])))
print("XLATCH_M2:      0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.XLATCH[1])))

print("MSLUT0:         0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUT0)))
print("MSLUT1:         0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUT1)))
print("MSLUT2:         0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUT2)))
print("MSLUT3:         0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUT3)))
print("MSLUT4:         0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUT4)))
print("MSLUT5:         0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUT5)))
print("MSLUT6:         0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUT6)))
print("MSLUT7:         0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUT7)))
print("MSLUTSEL:       0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUTSEL)))
print("MSLUTSTART:     0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSLUTSTART)))

print("MSCNT_M1:       0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSCNT[0])))
print("MSCURACT_M1:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSCURACT[0])))
print("CHOPCONF_M1:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.CHOPCONF[0])))
print("COOLCONF_M1:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.COOLCONF[0])))
print("DRVSTATUS_M1:   0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.DRVSTATUS[0])))
print("MSCNT_M2:       0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSCNT[1])))
print("MSCURACT_M2:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.MSCURACT[1])))
print("CHOPCONF_M2:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.CHOPCONF[1])))
print("COOLCONF_M2:    0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.COOLCONF[1])))
print("DRVSTATUS_M2:   0x{0:08X}".format(TMC5072.readRegister(TMC5072.registers.DRVSTATUS[1])))

myInterface.close()