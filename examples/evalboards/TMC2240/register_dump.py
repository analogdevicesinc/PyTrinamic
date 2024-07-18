################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC2240 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC2240_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    eval_board = TMC2240_eval(my_interface)
    mc = eval_board.ics[0]


    print("GCONF:           0x{0:08X}".format(eval_board.read_register(mc.REG.GCONF)))
    print("GSTAT:           0x{0:08X}".format(eval_board.read_register(mc.REG.GSTAT)))
    print("IFCNT:           0x{0:08X}".format(eval_board.read_register(mc.REG.IFCNT)))
    print("SLAVECONF:       0x{0:08X}".format(eval_board.read_register(mc.REG.SLAVECONF)))
    print("IOIN:            0x{0:08X}".format(eval_board.read_register(mc.REG.IOIN)))
    print("DRV_CONF:        0x{0:08X}".format(eval_board.read_register(mc.REG.DRV_CONF)))
    print("GLOBAL_SCALE     0x{0:08X}".format(eval_board.read_register(mc.REG.GLOBAL_SCALER)))
    print("IHOLD_IRUN:      0x{0:08X}".format(eval_board.read_register(mc.REG.IHOLD_IRUN)))
    print("TPOWERDOWN:      0x{0:08X}".format(eval_board.read_register(mc.REG.TPOWERDOWN)))
    print("TSTEP:           0x{0:08X}".format(eval_board.read_register(mc.REG.TSTEP)))
    print("TPWMTHRS:        0x{0:08X}".format(eval_board.read_register(mc.REG.TPWMTHRS)))
    print("TCOOLTHRS:       0x{0:08X}".format(eval_board.read_register(mc.REG.TCOOLTHRS)))
    print("THIGH:           0x{0:08X}".format(eval_board.read_register(mc.REG.THIGH)))
    print("DIRECT_MODE:     0x{0:08X}".format(eval_board.read_register(mc.REG.DIRECT_MODE)))
    print("ENCMODE:         0x{0:08X}".format(eval_board.read_register(mc.REG.ENCMODE)))
    print("X_ENC:           0x{0:08X}".format(eval_board.read_register(mc.REG.X_ENC)))
    print("ENC_CONST:       0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_CONST)))
    print("ENC_STATUS:      0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_STATUS)))
    print("ENC_LATCH:       0x{0:08X}".format(eval_board.read_register(mc.REG.ENC_LATCH)))
    print("ADC_VSUPPLY_AIN: 0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_VSUPPLY_AIN)))
    print("ADC_TEMP:        0x{0:08X}".format(eval_board.read_register(mc.REG.ADC_TEMP)))
    print("OTW_OV_VTH:      0x{0:08X}".format(eval_board.read_register(mc.REG.OTW_OV_VTH)))
    print("MSLUT_0:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_0)))
    print("MSLUT_1:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_1)))
    print("MSLUT_2:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_2)))
    print("MSLUT_3:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_3)))
    print("MSLUT_4:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_4)))
    print("MSLUT_5:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_5)))
    print("MSLUT_6:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_6)))
    print("MSLUT_7:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_7)))
    print("MSLUTSEL:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSEL)))
    print("MSLUTSTART:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSTART)))
    print("MSCNT:           0x{0:08X}".format(eval_board.read_register(mc.REG.MSCNT)))
    print("MSCURACT:        0x{0:08X}".format(eval_board.read_register(mc.REG.MSCURACT)))
    print("CHOPCONF:        0x{0:08X}".format(eval_board.read_register(mc.REG.CHOPCONF)))
    print("COOLCONF:        0x{0:08X}".format(eval_board.read_register(mc.REG.COOLCONF)))
    print("DCCTRL:          0x{0:08X}".format(eval_board.read_register(mc.REG.DCCTRL)))
    print("DRV_STATUS:      0x{0:08X}".format(eval_board.read_register(mc.REG.DRV_STATUS)))
    print("PWMCONF:         0x{0:08X}".format(eval_board.read_register(mc.REG.PWMCONF)))
    print("PWM_SCALE:       0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_SCALE)))
    print("PWM_AUTO:        0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_AUTO)))
    print("SG4_THRS:        0x{0:08X}".format(eval_board.read_register(mc.REG.SG4_THRS)))
    print("SG4_RESULT:      0x{0:08X}".format(eval_board.read_register(mc.REG.SG4_RESULT)))
    print("SG4_IND:         0x{0:08X}".format(eval_board.read_register(mc.REG.SG4_IND)))


print("\nReady.")
