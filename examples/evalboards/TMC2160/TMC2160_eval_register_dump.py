#!/usr/bin/env python3
'''
Dump all register values of the TMC2160 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 23.10.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.evalboards.TMC2160_eval import TMC2160_eval

PyTrinamic.showInfo()

from PyTrinamic.connections.ConnectionManager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC2160 = TMC2160_eval(myInterface)

print("GCONF:         0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.GCONF)))
print("GSTAT:         0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.GSTAT)))
print("INP_OUT:       0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.INP_OUT)))
print("X_COMPARE:     0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.X_COMPARE)))
print("OTP_PROG:      0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.OTP_PROG)))
print("OTP_READ:      0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.OTP_READ)))
print("FACTORY_CONF:  0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.FACTORY_CONF)))
print("SHORT_CONF:    0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.SHORT_CONF)))
print("DRV_CONF:      0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.DRV_CONF)))
print("GLOBAL_SCALER: 0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.GLOBAL_SCALER)))
print("OFFSET_READ:   0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.OFFSET_READ)))
print("IHOLD_IRUN:    0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.IHOLD_IRUN)))
print("TPOWERDOWN:    0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.TPOWERDOWN)))
print("TSTEP:         0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.TSTEP)))
print("TPWMTHRS:      0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.TPWMTHRS)))
print("TCOOLTHRS:     0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.TCOOLTHRS)))
print("THIGH:         0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.THIGH)))
print("XDIRECT:       0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.XDIRECT)))
print("VDCMIN:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.VDCMIN)))
print("MSLUT0:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUT0)))
print("MSLUT1:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUT1)))
print("MSLUT2:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUT2)))
print("MSLUT3:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUT3)))
print("MSLUT4:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUT4)))
print("MSLUT5:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUT5)))
print("MSLUT6:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUT6)))
print("MSLUT7:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUT7)))
print("MSLUTSEL:      0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUTSEL)))
print("MSLUTSTART:    0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSLUTSTART)))
print("MSCNT:         0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSCNT)))
print("MSCURACT:      0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.MSCURACT)))
print("CHOPCONF:      0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.CHOPCONF)))
print("COOLCONF:      0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.COOLCONF)))
print("DCCTRL:        0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.DCCTRL)))
print("DRVSTATUS:     0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.DRVSTATUS)))
print("PWMCONF:       0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.PWMCONF)))
print("PWM_SCALE:     0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.PWM_SCALE)))
print("PWM_AUTO:      0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.PWM_AUTO)))
print("LOST_STEPS:    0x{0:08X}".format(TMC2160.readRegister(TMC2160.registers.LOST_STEPS)))

myInterface.close()
