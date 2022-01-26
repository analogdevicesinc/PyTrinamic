#!/usr/bin/env python3
'''
Dump all register values of the TMC5160 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 24.10.2019

@author: JM
'''

import pytrinamic
from pytrinamic.evalboards.TMC5160_eval import TMC5160_eval

pytrinamic.show_info()

from pytrinamic.connections.connection_manager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC5160 = TMC5160_eval(myInterface)

print("GCONF:         0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.GCONF)))
print("GSTAT:         0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.GSTAT)))
print("SLAVECONF:     0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.SLAVECONF)))
print("IOIN / OUTPUT: 0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.INP_OUT)))
print("X_COMPARE:     0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.X_COMPARE)))
print("OTP_PROG:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.OTP_PROG)))
print("OTP_READ:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.OTP_READ)))
print("FACTORY_CONF:  0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.FACTORY_CONF)))
print("SHORT_CONF:    0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.SHORT_CONF)))
print("DRV_CONF:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.DRV_CONF)))
print("GLOBAL_SCALER: 0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.GLOBAL_SCALER)))
print("OFFSET_READ:   0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.OFFSET_READ)))
print("IHOLD_IRUN:    0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.IHOLD_IRUN)))
print("TPOWERDOWN:    0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.TPOWERDOWN)))
print("TSTEP:         0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.TSTEP)))
print("TPWMTHRS:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.TPWMTHRS)))
print("TCOOLTHRS:     0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.TCOOLTHRS)))
print("THIGH:         0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.THIGH)))
print("RAMPMODE:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.RAMPMODE)))
print("XACTUAL:       0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.XACTUAL)))
print("VACTUAL:       0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.VACTUAL)))
print("VSTART:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.VSTART)))
print("A1:            0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.A1)))
print("V1:            0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.V1)))
print("AMAX:          0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.AMAX)))
print("VMAX:          0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.VMAX)))
print("DMAX:          0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.DMAX)))
print("D1:            0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.D1)))
print("VSTOP:         0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.VSTOP)))
print("TZEROWAIT:     0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.TZEROWAIT)))
print("XTARGET:       0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.XTARGET)))
print("VDCMIN:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.VDCMIN)))
print("SWMODE:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.SWMODE)))
print("RAMPSTAT:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.RAMPSTAT)))
print("XLATCH:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.XLATCH)))
print("ENCMODE:       0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.ENCMODE)))
print("XENC:          0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.XENC)))
print("ENC_CONST:     0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.ENC_CONST)))
print("ENC_STATUS:    0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.ENC_STATUS)))
print("ENC_LATCH:     0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.ENC_LATCH)))
print("ENC_DEVIATION: 0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.ENC_DEVIATION)))
print("MSLUT0:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUT0)))
print("MSLUT1:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUT1)))
print("MSLUT2:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUT2)))
print("MSLUT3:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUT3)))
print("MSLUT4:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUT4)))
print("MSLUT5:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUT5)))
print("MSLUT6:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUT6)))
print("MSLUT7:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUT7)))
print("MSLUTSEL:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUTSEL)))
print("MSLUTSTART:    0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSLUTSTART)))
print("MSCNT:         0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSCNT)))
print("MSCURACT:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.MSCURACT)))
print("CHOPCONF:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.CHOPCONF)))
print("COOLCONF:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.COOLCONF)))
print("DCCTRL:        0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.DCCTRL)))
print("DRVSTATUS:     0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.DRVSTATUS)))
print("PWMCONF:       0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.PWMCONF)))
print("PWM_SCALE:     0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.PWM_SCALE)))
print("PWM_AUTO:      0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.PWM_AUTO)))
print("LOST_STEPS:    0x{0:08X}".format(TMC5160.readRegister(TMC5160.registers.LOST_STEPS)))

myInterface.close()