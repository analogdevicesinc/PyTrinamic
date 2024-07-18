################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC5160 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5160_eval

pytrinamic.show_info()

my_interface = ConnectionManager().connect()
print(my_interface)

eval_board = TMC5160_eval(my_interface)
mc = eval_board.ics[0]

print("GCONF:         0x{0:08X}".format(eval_board.read_register(mc.REG.GCONF)))
print("GSTAT:         0x{0:08X}".format(eval_board.read_register(mc.REG.GSTAT)))
print("SLAVECONF:     0x{0:08X}".format(eval_board.read_register(mc.REG.SLAVECONF)))
print("IOIN / OUTPUT: 0x{0:08X}".format(eval_board.read_register(mc.REG.IOIN_OUTPUT)))
print("X_COMPARE:     0x{0:08X}".format(eval_board.read_register(mc.REG.X_COMPARE)))
print("OTP_PROG:      0x{0:08X}".format(eval_board.read_register(mc.REG.OTP_PROG)))
print("OTP_READ:      0x{0:08X}".format(eval_board.read_register(mc.REG.OTP_READ)))
print("FACTORY_CONF:  0x{0:08X}".format(eval_board.read_register(mc.REG.FACTORY_CONF)))
print("SHORT_CONF:    0x{0:08X}".format(eval_board.read_register(mc.REG.SHORT_CONF)))
print("DRV_CONF:      0x{0:08X}".format(eval_board.read_register(mc.REG.DRV_CONF)))
print("GLOBAL_SCALER: 0x{0:08X}".format(eval_board.read_register(mc.REG.GLOBAL_SCALER)))
print("OFFSET_READ:   0x{0:08X}".format(eval_board.read_register(mc.REG.OFFSET_READ)))
print("IHOLD_IRUN:    0x{0:08X}".format(eval_board.read_register(mc.REG.IHOLD_IRUN)))
print("TPOWERDOWN:    0x{0:08X}".format(eval_board.read_register(mc.REG.TPOWERDOWN)))
print("TSTEP:         0x{0:08X}".format(eval_board.read_register(mc.REG.TSTEP)))
print("TPWMTHRS:      0x{0:08X}".format(eval_board.read_register(mc.REG.TPWMTHRS)))
print("TCOOLTHRS:     0x{0:08X}".format(eval_board.read_register(mc.REG.TCOOLTHRS)))
print("THIGH:         0x{0:08X}".format(eval_board.read_register(mc.REG.THIGH)))
print("RAMPMODE:      0x{0:08X}".format(eval_board.read_register(mc.REG.RAMPMODE)))
print("XACTUAL:       0x{0:08X}".format(eval_board.read_register(mc.REG.XACTUAL)))
print("VACTUAL:       0x{0:08X}".format(eval_board.read_register(mc.REG.VACTUAL)))
print("VSTART:        0x{0:08X}".format(eval_board.read_register(mc.REG.VSTART)))
print("A1:            0x{0:08X}".format(eval_board.read_register(mc.REG.A1)))
print("V1:            0x{0:08X}".format(eval_board.read_register(mc.REG.V1)))
print("AMAX:          0x{0:08X}".format(eval_board.read_register(mc.REG.AMAX)))
print("VMAX:          0x{0:08X}".format(eval_board.read_register(mc.REG.VMAX)))
print("DMAX:          0x{0:08X}".format(eval_board.read_register(mc.REG.DMAX)))
print("D1:            0x{0:08X}".format(eval_board.read_register(mc.REG.D1)))
print("VSTOP:         0x{0:08X}".format(eval_board.read_register(mc.REG.VSTOP)))
print("TZEROWAIT:     0x{0:08X}".format(eval_board.read_register(mc.REG.TZEROWAIT)))
print("XTARGET:       0x{0:08X}".format(eval_board.read_register(mc.REG.XTARGET)))
print("VDCMIN:        0x{0:08X}".format(eval_board.read_register(mc.REG.VDCMIN)))
print("SW_MODE:       0x{0:08X}".format(eval_board.read_register(mc.REG.SW_MODE)))
print("RAMP_STAT:     0x{0:08X}".format(eval_board.read_register(mc.REG.RAMP_STAT)))
print("XLATCH:        0x{0:08X}".format(eval_board.read_register(mc.REG.XLATCH)))
print("ENCMODE:       0x{0:08X}".format(eval_board.read_register(mc.REG.ENCMODE)))
print("X_ENC:         0x{0:08X}".format(eval_board.read_register(mc.REG.X_ENC)))
print("ENC_CONST:     0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_CONST)))
print("ENC_STATUS:    0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_STATUS)))
print("ENC_LATCH:     0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_LATCH)))
print("ENC_DEVIATION: 0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_DEVIATION)))
print("MSLUT0:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT0)))
print("MSLUT1:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT1)))
print("MSLUT2:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT2)))
print("MSLUT3:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT3)))
print("MSLUT4:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT4)))
print("MSLUT5:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT5)))
print("MSLUT6:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT6)))
print("MSLUT7:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT7)))
print("MSLUTSEL:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSEL)))
print("MSLUTSTART:    0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSTART)))
print("MSCNT:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSCNT)))
print("MSCURACT:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSCURACT)))
print("CHOPCONF:      0x{0:08X}".format(eval_board.read_register(mc.REG.CHOPCONF)))
print("COOLCONF:      0x{0:08X}".format(eval_board.read_register(mc.REG.COOLCONF)))
print("DCCTRL:        0x{0:08X}".format(eval_board.read_register(mc.REG.DCCTRL)))
print("DRV_STATUS:    0x{0:08X}".format(eval_board.read_register(mc.REG.DRV_STATUS)))
print("PWM_CONF:      0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_CONF)))
print("PWM_SCALE:     0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_SCALE)))
print("PWM_AUTO:      0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_AUTO)))
print("LOST_STEPS:    0x{0:08X}".format(eval_board.read_register(mc.REG.LOST_STEPS)))

my_interface.close()

print("\nReady.")
