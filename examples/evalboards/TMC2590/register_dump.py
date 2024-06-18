################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC2590 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC2590_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create TMC2590-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC2590_eval(my_interface)
    drv = eval_board.ics[0]
    print("Driver info: " + str(drv.get_info()))
    print("Register dump for " + str(drv.get_name()) + ":")

    print("DRVSTATUS___MSTEP:  0x{0:08X}".format(eval_board.read_register(drv.REG.DRVSTATUS___MSTEP)))
    print("DRVSTATUS___SG:     0x{0:08X}".format(eval_board.read_register(drv.REG.DRVSTATUS___SG)))
    print("DRVSTATUS___SG_SE:  0x{0:08X}".format(eval_board.read_register(drv.REG.DRVSTATUS___SG_SE)))
    print("DRVCTRL:            0x{0:08X}".format(eval_board.read_register(drv.REG.DRVCTRL)))
    print("CHOPCONF:           0x{0:08X}".format(eval_board.read_register(drv.REG.CHOPCONF)))
    print("SMARTEN:            0x{0:08X}".format(eval_board.read_register(drv.REG.SMARTEN)))
    print("SGCSCONF:           0x{0:08X}".format(eval_board.read_register(drv.REG.SGCSCONF)))
    print("DRVCONF:            0x{0:08X}".format(eval_board.read_register(drv.REG.DRVCONF)))

print("\nReady.")
