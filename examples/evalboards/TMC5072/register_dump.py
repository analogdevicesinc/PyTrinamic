################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC5072 mc.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the mc.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5072_eval

pytrinamic.show_info()

my_interface = ConnectionManager().connect()
print(my_interface)

eval_board = TMC5072_eval(my_interface)
mc = eval_board.ics[0]
print("Motion controller info: " + str(mc.get_info()))
print("Register dump for " + str(mc.get_name()) + ":")

print("GCONF:          0x{0:08X}".format(eval_board.read_register(mc.REG.GCONF)))
print("GSTAT:          0x{0:08X}".format(eval_board.read_register(mc.REG.GSTAT)))
print("SLAVECONF:      0x{0:08X}".format(eval_board.read_register(mc.REG.SLAVECONF)))
print("INPUT:          0x{0:08X}".format(eval_board.read_register(mc.REG.INPUT___OUTPUT)))
print("X_COMPARE:      0x{0:08X}".format(eval_board.read_register(mc.REG.X_COMPARE)))

print("PWMCONF_M1:     0x{0:08X}".format(eval_board.read_register(mc.REG.PWMCONF_M1)))
print("PWM_STATUS_M1:  0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_STATUS_M1)))
print("PWMCONF_M2:     0x{0:08X}".format(eval_board.read_register(mc.REG.PWMCONF_M2)))
print("PWM_STATUS_M2:  0x{0:08X}".format(eval_board.read_register(mc.REG.PWM_STATUS_M2)))

print("RAMPMODE_M1:    0x{0:08X}".format(eval_board.read_register(mc.REG.RAMPMODE_M1)))
print("XACTUAL_M1:     0x{0:08X}".format(eval_board.read_register(mc.REG.XACTUAL_M1)))
print("VACTUAL_M1:     0x{0:08X}".format(eval_board.read_register(mc.REG.VACTUAL_M1)))
print("VSTART_M1:      0x{0:08X}".format(eval_board.read_register(mc.REG.VSTART_M1)))
print("A1_M1:          0x{0:08X}".format(eval_board.read_register(mc.REG.A1_M1)))
print("V1_M1:          0x{0:08X}".format(eval_board.read_register(mc.REG.V1_M1)))
print("AMAX_M1:        0x{0:08X}".format(eval_board.read_register(mc.REG.AMAX_M1)))
print("VMAX_M1:        0x{0:08X}".format(eval_board.read_register(mc.REG.VMAX_M1)))
print("DMAX_M1:        0x{0:08X}".format(eval_board.read_register(mc.REG.DMAX_M1)))
print("D1_M1:          0x{0:08X}".format(eval_board.read_register(mc.REG.D1_M1)))
print("VSTOP_M1:       0x{0:08X}".format(eval_board.read_register(mc.REG.VSTOP_M1)))
print("TZEROWAIT_M1:   0x{0:08X}".format(eval_board.read_register(mc.REG.TZEROWAIT_M1)))
print("XTARGET_M1:     0x{0:08X}".format(eval_board.read_register(mc.REG.XTARGET_M1)))
print("IHOLD_IRUN_M1:  0x{0:08X}".format(eval_board.read_register(mc.REG.IHOLD_IRUN_M1)))
print("VCOOLTHRS_M1:   0x{0:08X}".format(eval_board.read_register(mc.REG.VCOOLTHRS_M1)))
print("VHIGH_M1:       0x{0:08X}".format(eval_board.read_register(mc.REG.VHIGH_M1)))

print("RAMPMODE_M2:    0x{0:08X}".format(eval_board.read_register(mc.REG.RAMPMODE_M2)))
print("XACTUAL_M2:     0x{0:08X}".format(eval_board.read_register(mc.REG.XACTUAL_M2)))
print("VACTUAL_M2:     0x{0:08X}".format(eval_board.read_register(mc.REG.VACTUAL_M2)))
print("VSTART_M2:      0x{0:08X}".format(eval_board.read_register(mc.REG.VSTART_M2)))
print("A1_M2:          0x{0:08X}".format(eval_board.read_register(mc.REG.A1_M2)))
print("V1_M2:          0x{0:08X}".format(eval_board.read_register(mc.REG.V1_M2)))
print("AMAX_M2:        0x{0:08X}".format(eval_board.read_register(mc.REG.AMAX_M2)))
print("VMAX_M2:        0x{0:08X}".format(eval_board.read_register(mc.REG.VMAX_M2)))
print("DMAX_M2:        0x{0:08X}".format(eval_board.read_register(mc.REG.DMAX_M2)))
print("D1_M2:          0x{0:08X}".format(eval_board.read_register(mc.REG.D1_M2)))
print("VSTOP_M2:       0x{0:08X}".format(eval_board.read_register(mc.REG.VSTOP_M2)))
print("TZEROWAIT_M2:   0x{0:08X}".format(eval_board.read_register(mc.REG.TZEROWAIT_M2)))
print("XTARGET_M2:     0x{0:08X}".format(eval_board.read_register(mc.REG.XTARGET_M2)))
print("IHOLD_IRUN_M2:  0x{0:08X}".format(eval_board.read_register(mc.REG.IHOLD_IRUN_M2)))
print("VCOOLTHRS_M2:   0x{0:08X}".format(eval_board.read_register(mc.REG.VCOOLTHRS_M2)))
print("VHIGH_M2:       0x{0:08X}".format(eval_board.read_register(mc.REG.VHIGH_M2)))

print("MSLUT0:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_0)))
print("MSLUT1:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_1)))
print("MSLUT2:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_2)))
print("MSLUT3:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_3)))
print("MSLUT4:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_4)))
print("MSLUT5:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_5)))
print("MSLUT6:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_6)))
print("MSLUT7:         0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT_7)))
print("MSLUTSEL:       0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSEL)))
print("MSLUTSTART:     0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSTART)))

print("MSCNT_M1:       0x{0:08X}".format(eval_board.read_register(mc.REG.MSCNT_M1)))
print("MSCURACT_M1:    0x{0:08X}".format(eval_board.read_register(mc.REG.MSCURACT_M1)))
print("CHOPCONF_M1:    0x{0:08X}".format(eval_board.read_register(mc.REG.CHOPCONF_M1)))
print("COOLCONF_M1:    0x{0:08X}".format(eval_board.read_register(mc.REG.COOLCONF_M1)))

print("MSCNT_M2:       0x{0:08X}".format(eval_board.read_register(mc.REG.MSCNT_M2)))
print("MSCURACT_M2:    0x{0:08X}".format(eval_board.read_register(mc.REG.MSCURACT_M2)))
print("CHOPCONF_M2:    0x{0:08X}".format(eval_board.read_register(mc.REG.CHOPCONF_M2)))
print("COOLCONF_M2:    0x{0:08X}".format(eval_board.read_register(mc.REG.COOLCONF_M2)))

my_interface.close()

print("\nReady.")
