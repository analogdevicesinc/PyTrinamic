################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC2209 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC2209_eval

pytrinamic.show_info()

my_interface = ConnectionManager().connect()
print(my_interface)

eval_board = TMC2209_eval(my_interface)
drv = eval_board.ics[0]
print("Driver info: " + str(drv.get_info()))
print("Register dump for " + str(drv.get_name()) + ":")

print("GCONF:       0x{0:08X}".format(eval_board.read_register(drv.REG.GCONF)))
print("GSTAT:       0x{0:08X}".format(eval_board.read_register(drv.REG.GSTAT)))
print("IFCNT:       0x{0:08X}".format(eval_board.read_register(drv.REG.IFCNT)))
print("SLAVECONF:   0x{0:08X}".format(eval_board.read_register(drv.REG.SLAVECONF)))
print("IHOLD_IRUN:  0x{0:08X}".format(eval_board.read_register(drv.REG.IHOLD_IRUN)))
print("TPOWERDOWN:  0x{0:08X}".format(eval_board.read_register(drv.REG.TPOWERDOWN)))
print("TSTEP:       0x{0:08X}".format(eval_board.read_register(drv.REG.TSTEP)))
print("TPWMTHRS:    0x{0:08X}".format(eval_board.read_register(drv.REG.TPWMTHRS)))
print("TCOOLTHRS:   0x{0:08X}".format(eval_board.read_register(drv.REG.TCOOLTHRS)))
print("VACTUAL:     0x{0:08X}".format(eval_board.read_register(drv.REG.VACTUAL)))
print("SGTHRS:      0x{0:08X}".format(eval_board.read_register(drv.REG.SGTHRS)))
print("SG_RESULT:   0x{0:08X}".format(eval_board.read_register(drv.REG.SG_RESULT)))
print("COOLCONF:    0x{0:08X}".format(eval_board.read_register(drv.REG.COOLCONF)))
print("MSCNT:       0x{0:08X}".format(eval_board.read_register(drv.REG.MSCNT)))
print("MSCURACT:    0x{0:08X}".format(eval_board.read_register(drv.REG.MSCURACT)))
print("CHOPCONF:    0x{0:08X}".format(eval_board.read_register(drv.REG.CHOPCONF)))
print("DRV_STATUS:  0x{0:08X}".format(eval_board.read_register(drv.REG.DRV_STATUS)))
print("PWMCONF:     0x{0:08X}".format(eval_board.read_register(drv.REG.PWMCONF)))
print("PWMSCALE:    0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_SCALE)))
print("PWMAUTO:     0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_AUTO)))

my_interface.close()

print("\nReady.")
