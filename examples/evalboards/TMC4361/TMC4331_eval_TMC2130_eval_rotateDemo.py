################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4361_eval, TMC2130_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create an TMC4361-Eval class which communicates over the Landungsbruecke via TMCL
    eval_mc = TMC4361_eval(my_interface)
    motor = eval_mc.motors[0]
    mc = eval_mc.ics[0]
    print("Motion controller: " + str(mc.get_info()))

    # Create an TMC2130-Eval class which communicates over the Landungsbruecke via TMCL
    eval_drv = TMC2130_eval(my_interface)
    drv = eval_drv.ics[0]
    print("Driver: " + str(drv.get_info()))

    # configure TMC2130 pwm for use with TMC4361 (disable singleline)"
    # eval_drv.write_register(drv.REG.DRVCTRL, 0x00)
    # eval_drv.write_register(drv.REG.CHOPCONF, 0x0C)
    # eval_drv.write_register(drv.REG.SMARTEN, 0x0D)
    # eval_drv.write_register(drv.REG.SGCSCONF, 0x0E)
    # eval_drv.write_register(drv.REG.DRVCONF, 0x0F)

    motor.set_axis_parameter(motor.AP.MaxVelocity, 1000)
    motor.set_axis_parameter(motor.AP.MaxAcceleration, 10000)

    print("Rotating...")
    motor.rotate(30 * 25600)
    time.sleep(10)

    print("Stopping...")
    motor.stop()
    time.sleep(1)

    print("Moving back to 0...")
    motor.move_to(0, 30 * 25600)

    # Wait until position 0 is reached
    while motor.actual_position != 0:
        print("Actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Reached position 0")


print("\nReady.")
