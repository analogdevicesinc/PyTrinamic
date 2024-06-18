################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC5130 mc.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the mc.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5130_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    eval_board = TMC5130_eval(my_interface)
    mc = eval_board.ics[0]
    print("Motion controller info: " + str(mc.get_info()))
    print("Register dump for " + str(mc.get_name()) + ":")

    print("GCONF:       0x{0:08X}".format(eval_board.read_register(mc.REG.GCONF)))
    print("GSTAT:       0x{0:08X}".format(eval_board.read_register(mc.REG.GSTAT)))
    print("IFCNT:       0x{0:08X}".format(eval_board.read_register(mc.REG.IFCNT)))
    print("SLAVECONF:   0x{0:08X}".format(eval_board.read_register(mc.REG.SLAVECONF)))
    print("IOIN_OUTPUT: 0x{0:08X}".format(eval_board.read_register(mc.REG.IOIN_OUTPUT)))
    print("X_COMPARE:   0x{0:08X}".format(eval_board.read_register(mc.REG.X_COMPARE)))
    print("IHOLD_IRUN:  0x{0:08X}".format(eval_board.read_register(mc.REG.IHOLD_IRUN)))
    print("TPOWERDOWN:  0x{0:08X}".format(eval_board.read_register(mc.REG.TPOWERDOWN)))
    print("TSTEP:       0x{0:08X}".format(eval_board.read_register(mc.REG.TSTEP)))
    print("TPWMTHRS:    0x{0:08X}".format(eval_board.read_register(mc.REG.TPWMTHRS)))
    print("TCOOLTHRS:   0x{0:08X}".format(eval_board.read_register(mc.REG.TCOOLTHRS)))
    print("THIGH:       0x{0:08X}".format(eval_board.read_register(mc.REG.THIGH)))
    print("RAMPMODE:    0x{0:08X}".format(eval_board.read_register(mc.REG.RAMPMODE)))
    print("XACTUAL:     0x{0:08X}".format(eval_board.read_register(mc.REG.XACTUAL)))
    print("VACTUAL:     0x{0:08X}".format(eval_board.read_register(mc.REG.VACTUAL)))
    print("VSTART:      0x{0:08X}".format(eval_board.read_register(mc.REG.VSTART)))
    print("A1:          0x{0:08X}".format(eval_board.read_register(mc.REG.A1)))
    print("V1:          0x{0:08X}".format(eval_board.read_register(mc.REG.V1)))
    print("AMAX:        0x{0:08X}".format(eval_board.read_register(mc.REG.AMAX)))
    print("VMAX:        0x{0:08X}".format(eval_board.read_register(mc.REG.VMAX)))
    print("DMAX:        0x{0:08X}".format(eval_board.read_register(mc.REG.DMAX)))
    print("D1:          0x{0:08X}".format(eval_board.read_register(mc.REG.D1)))
    print("VSTOP:       0x{0:08X}".format(eval_board.read_register(mc.REG.VSTOP)))
    print("TZEROWAIT:   0x{0:08X}".format(eval_board.read_register(mc.REG.TZEROWAIT)))
    print("XTARGET:     0x{0:08X}".format(eval_board.read_register(mc.REG.XTARGET)))
    print("VDCMIN:      0x{0:08X}".format(eval_board.read_register(mc.REG.VDCMIN)))
    print("SW_MODE:     0x{0:08X}".format(eval_board.read_register(mc.REG.SW_MODE)))
    print("RAMP_STAT:   0x{0:08X}".format(eval_board.read_register(mc.REG.RAMP_STAT)))
    print("XLATCH:      0x{0:08X}".format(eval_board.read_register(mc.REG.XLATCH)))
    print("ENCMODE:     0x{0:08X}".format(eval_board.read_register(mc.REG.ENCMODE)))
    print("X_ENC:       0x{0:08X}".format(eval_board.read_register(mc.REG.X_ENC)))
    print("ENC_CONST:   0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_CONST)))
    print("ENC_STATUS:  0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_STATUS)))
    print("ENC_LATCH:   0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_LATCH)))
    print("MSLUT_0:     0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_0)))
    print("MSLUT_1:     0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_1)))
    print("MSLUT_2:     0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_2)))
    print("MSLUT_3:     0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_3)))
    print("MSLUT_4:     0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_4)))
    print("MSLUT_5:     0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_5)))
    print("MSLUT_6:     0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_6)))
    print("MSLUT_7:     0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_7)))
    print("MSLUTSEL:    0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSEL)))
    print("MSLUTSTART:  0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSTART)))
    print("MSCNT:       0x{0:08X}".format(eval_board.read_register(mc.REG.MSCNT)))
    print("MSCURACT:    0x{0:08X}".format(eval_board.read_register(mc.REG.MSCURACT)))
    print("CHOPCONF:    0x{0:08X}".format(eval_board.read_register(mc.REG.CHOPCONF)))
    print("COOLCONF:    0x{0:08X}".format(eval_board.read_register(mc.REG.COOLCONF)))
    print("DCCTRL:      0x{0:08X}".format(eval_board.read_register(mc.REG.DCCTRL)))
    print("DRV_STATUS:  0x{0:08X}".format(eval_board.read_register(mc.REG.DRV_STATUS)))
    print("PWMCONF:     0x{0:08X}".format(eval_board.read_register(mc.REG.PWMCONF)))
    print("PWM_SCALE:   0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_SCALE)))
    print("ENCM_CTRL:   0x{0:08X}".format(eval_board.read_register(mc.REG.ENCM_CTRL)))
    print("LOST_STEPS:  0x{0:08X}".format(eval_board.read_register(mc.REG.LOST_STEPS)))

print("\nReady.")
