################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC2130 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC2130_eval

pytrinamic.show_info()

my_interface = ConnectionManager().connect()
print(my_interface)
eval_board = TMC2130_eval(my_interface)
drv = eval_board.ics[0]
print("Driver info: " + str(drv.get_info()))
print("Register dump for " + str(drv.get_name()) + ":")

print("GCONF:       0x{0:08X}".format(eval_board.read_register(drv.REG.GCONF)))
print("GSTAT:       0x{0:08X}".format(eval_board.read_register(drv.REG.GSTAT)))
print("IOIN:        0x{0:08X}".format(eval_board.read_register(drv.REG.IOIN)))
print("IHOLD_IRUN:  0x{0:08X}".format(eval_board.read_register(drv.REG.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(eval_board.read_register(drv.REG.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(eval_board.read_register(drv.REG.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(eval_board.read_register(drv.REG.TPWMTHRS)))
print("TCOOLTHRS:   0x{0:08X}".format(eval_board.read_register(drv.REG.TCOOLTHRS)))
print("THIGH:       0x{0:08X}".format(eval_board.read_register(drv.REG.THIGH)))
print("XDIRECT:     0x{0:08X}".format(eval_board.read_register(drv.REG.XDIRECT)))
print("VDCMIN:      0x{0:08X}".format(eval_board.read_register(drv.REG.VDCMIN)))
print("MSLUT__:     0x{0:08X}".format(eval_board.read_register(drv.REG.MSLUT__)))
print("MSLUTSEL:    0x{0:08X}".format(eval_board.read_register(drv.REG.MSLUTSEL)))
print("MSLUTSTART:  0x{0:08X}".format(eval_board.read_register(drv.REG.MSLUTSTART)))
print("MSCNT:       0x{0:08X}".format(eval_board.read_register(drv.REG.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(eval_board.read_register(drv.REG.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(eval_board.read_register(drv.REG.CHOPCONF)))
print("COOLCONF:    0x{0:08X}".format(eval_board.read_register(drv.REG.COOLCONF)))
print("DCCTRL:      0x{0:08X}".format(eval_board.read_register(drv.REG.DCCTRL)))
print("DRV_STATUS:  0x{0:08X}".format(eval_board.read_register(drv.REG.DRV_STATUS)))
print("PWM_CONF:    0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_CONF)))
print("PWM_SCALE:   0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_SCALE)))
print("ENCM_CTRL:   0x{0:08X}".format(eval_board.read_register(drv.REG.ENCM_CTRL)))
print("LOST_STEPS:  0x{0:08X}".format(eval_board.read_register(drv.REG.LOST_STEPS)))

my_interface.close()

print("\nReady.")
