#!/usr/bin/env python3
'''
Dump all register values of the TMC5161 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 30.01.2020

@author: JM
'''

import PyTrinamic
from PyTrinamic.evalboards.TMC5161_eval import TMC5161_eval

PyTrinamic.showInfo()

from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]
TMC5161 = TMC5161_eval(myInterface)

print("GCONF:         0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.GCONF)))
print("GSTAT:         0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.GSTAT)))
print("SLAVECONF:     0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.SLAVECONF)))
print("IOIN / OUTPUT: 0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.INP_OUT)))
print("X_COMPARE:     0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.X_COMPARE)))
print("OTP_PROG:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.OTP_PROG)))
print("OTP_READ:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.OTP_READ)))
print("FACTORY_CONF:  0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.FACTORY_CONF)))
print("SHORT_CONF:    0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.SHORT_CONF)))
print("DRV_CONF:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.DRV_CONF)))
print("GLOBAL_SCALER: 0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.GLOBAL_SCALER)))
print("OFFSET_READ:   0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.OFFSET_READ)))
print("IHOLD_IRUN:    0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.IHOLD_IRUN)))
print("TPOWERDOWN:    0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.TPOWERDOWN)))
print("TSTEP:         0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.TSTEP)))
print("TPWMTHRS:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.TPWMTHRS)))
print("TCOOLTHRS:     0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.TCOOLTHRS)))
print("THIGH:         0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.THIGH)))
print("RAMPMODE:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.RAMPMODE)))
print("XACTUAL:       0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.XACTUAL)))
print("VACTUAL:       0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.VACTUAL)))
print("VSTART:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.VSTART)))
print("A1:            0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.A1)))
print("V1:            0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.V1)))
print("AMAX:          0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.AMAX)))
print("VMAX:          0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.VMAX)))
print("DMAX:          0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.DMAX)))
print("D1:            0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.D1)))
print("VSTOP:         0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.VSTOP)))
print("TZEROWAIT:     0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.TZEROWAIT)))
print("XTARGET:       0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.XTARGET)))
print("VDCMIN:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.VDCMIN)))
print("SWMODE:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.SWMODE)))
print("RAMPSTAT:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.RAMPSTAT)))
print("XLATCH:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.XLATCH)))
print("ENCMODE:       0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.ENCMODE)))
print("XENC:          0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.XENC)))
print("ENC_CONST:     0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.ENC_CONST)))
print("ENC_STATUS:    0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.ENC_STATUS)))
print("ENC_LATCH:     0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.ENC_LATCH)))
print("ENC_DEVIATION: 0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.ENC_DEVIATION)))
print("MSLUT0:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUT0)))
print("MSLUT1:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUT1)))
print("MSLUT2:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUT2)))
print("MSLUT3:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUT3)))
print("MSLUT4:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUT4)))
print("MSLUT5:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUT5)))
print("MSLUT6:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUT6)))
print("MSLUT7:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUT7)))
print("MSLUTSEL:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUTSEL)))
print("MSLUTSTART:    0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSLUTSTART)))
print("MSCNT:         0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSCNT)))
print("MSCURACT:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.MSCURACT)))
print("CHOPCONF:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.CHOPCONF)))
print("COOLCONF:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.COOLCONF)))
print("DCCTRL:        0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.DCCTRL)))
print("DRVSTATUS:     0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.DRVSTATUS)))
print("PWMCONF:       0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.PWMCONF)))
print("PWM_SCALE:     0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.PWM_SCALE)))
print("PWM_AUTO:      0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.PWM_AUTO)))
print("LOST_STEPS:    0x{0:08X}".format(TMC5161.readRegister(TMC5161.registers.LOST_STEPS)))

myInterface.close()
