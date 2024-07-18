################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC2660 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC2660_eval

pytrinamic.show_info()

my_interface = ConnectionManager().connect()
print(my_interface)

eval_board = TMC2660_eval(my_interface)
drv = eval_board.ics[0]
print("Driver info: " + str(drv.get_info()))
print("Register dump for " + str(drv.get_name()) + ":")

print("DRVSTATUS_MSTEP:       0x{0:08X}".format(eval_board.read_register(drv.REG.DRVSTATUS_MSTEP)))
print("DRVSTATUS_SG:          0x{0:08X}".format(eval_board.read_register(drv.REG.DRVSTATUS_SG)))
print("DRVSTATUS_SG_SE:       0x{0:08X}".format(eval_board.read_register(drv.REG.DRVSTATUS_SG_SE)))
print("DRVCTRL:               0x{0:08X}".format(eval_board.read_register(drv.REG.DRVCTRL)))
print("CHOPCONF:              0x{0:08X}".format(eval_board.read_register(drv.REG.CHOPCONF)))
print("SMARTEN:               0x{0:08X}".format(eval_board.read_register(drv.REG.SMARTEN)))
print("SGCSCONF:              0x{0:08X}".format(eval_board.read_register(drv.REG.SGCSCONF)))
print("DRVCONF:               0x{0:08X}".format(eval_board.read_register(drv.REG.DRVCONF)))

my_interface.close()

print("\nReady.")
