################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC2160 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC2160_eval

pytrinamic.show_info()

my_interface = ConnectionManager().connect()
print(my_interface)
eval_board = TMC2160_eval(my_interface)
drv = eval_board.ics[0]
print("Driver info: " + str(drv.get_info()))
print("Register dump for " + str(drv.get_name()) + ":")

print("GCONF:         0x{0:08X}".format(eval_board.read_register(drv.REG.GCONF)))
print("GSTAT:         0x{0:08X}".format(eval_board.read_register(drv.REG.GSTAT)))
print("IOIN_OUTPUT:   0x{0:08X}".format(eval_board.read_register(drv.REG.IOIN_OUTPUT)))
print("X_COMPARE:     0x{0:08X}".format(eval_board.read_register(drv.REG.X_COMPARE)))
print("FACTORY_CONF:  0x{0:08X}".format(eval_board.read_register(drv.REG.FACTORY_CONF)))
print("SHORT_CONF:    0x{0:08X}".format(eval_board.read_register(drv.REG.SHORT_CONF)))
print("DRV_CONF:      0x{0:08X}".format(eval_board.read_register(drv.REG.DRV_CONF)))
print("GLOBAL_SCALER: 0x{0:08X}".format(eval_board.read_register(drv.REG.GLOBAL_SCALER)))
print("OFFSET_READ:   0x{0:08X}".format(eval_board.read_register(drv.REG.OFFSET_READ)))
print("IHOLD_IRUN:    0x{0:08X}".format(eval_board.read_register(drv.REG.IHOLD_IRUN)))
print("TPOWERDOWN:    0x{0:08X}".format(eval_board.read_register(drv.REG.TPOWERDOWN)))
print("TSTEP:         0x{0:08X}".format(eval_board.read_register(drv.REG.TSTEP)))
print("TPWMTHRS:      0x{0:08X}".format(eval_board.read_register(drv.REG.TPWMTHRS)))
print("TCOOLTHRS:     0x{0:08X}".format(eval_board.read_register(drv.REG.TCOOLTHRS)))
print("THIGH:         0x{0:08X}".format(eval_board.read_register(drv.REG.THIGH)))
print("XDIRECT:       0x{0:08X}".format(eval_board.read_register(drv.REG.XDIRECT)))
print("VDCMIN:        0x{0:08X}".format(eval_board.read_register(drv.REG.VDCMIN)))
print("MSLUTSEL:      0x{0:08X}".format(eval_board.read_register(drv.REG.MSLUTSEL)))
print("MSLUTSTART:    0x{0:08X}".format(eval_board.read_register(drv.REG.MSLUTSTART)))
print("MSCNT:         0x{0:08X}".format(eval_board.read_register(drv.REG.MSCNT)))
print("MSCURACT:      0x{0:08X}".format(eval_board.read_register(drv.REG.MSCURACT)))
print("CHOPCONF:      0x{0:08X}".format(eval_board.read_register(drv.REG.CHOPCONF)))
print("COOLCONF:      0x{0:08X}".format(eval_board.read_register(drv.REG.COOLCONF)))
print("DCCTRL:        0x{0:08X}".format(eval_board.read_register(drv.REG.DCCTRL)))
print("DRV_STATUS:    0x{0:08X}".format(eval_board.read_register(drv.REG.DRV_STATUS)))
print("PWM_CONF:      0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_CONF)))
print("PWM_SCALE:     0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_SCALE)))
print("PWM_AUTO:      0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_AUTO)))
print("LOST_STEPS:    0x{0:08X}".format(eval_board.read_register(drv.REG.LOST_STEPS)))

my_interface.close()

print("\nReady.")
