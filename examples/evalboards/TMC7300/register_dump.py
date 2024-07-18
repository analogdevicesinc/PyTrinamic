################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC7300 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC7300_eval

pytrinamic.show_info()

my_interface = ConnectionManager().connect()
print(my_interface)

eval_board = TMC7300_eval(my_interface)
drv = eval_board.ics[0]
print("Driver info: " + str(drv.get_info()))
print("Register dump for " + str(drv.get_name()) + ":")

print("GCONF:          0x{0:08X}".format(eval_board.read_register(drv.REG.GCONF)))
print("GSTAT:          0x{0:08X}".format(eval_board.read_register(drv.REG.GSTAT)))
print("IFCNT:          0x{0:08X}".format(eval_board.read_register(drv.REG.IFCNT)))
print("SLAVECONF:      0x{0:08X}".format(eval_board.read_register(drv.REG.SLAVECONF)))
print("IOIN:           0x{0:08X}".format(eval_board.read_register(drv.REG.IOIN)))
print("CURRENT_LIMIT:  0x{0:08X}".format(eval_board.read_register(drv.REG.CURRENT_LIMIT)))
print("PWM_AB:         0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_AB)))
print("CHOPCONF:       0x{0:08X}".format(eval_board.read_register(drv.REG.CHOPCONF)))
print("DRV_STATUS:     0x{0:08X}".format(eval_board.read_register(drv.REG.DRV_STATUS)))
print("PWMCONF:        0x{0:08X}".format(eval_board.read_register(drv.REG.PWMCONF)))

my_interface.close()

print("\nReady.")
