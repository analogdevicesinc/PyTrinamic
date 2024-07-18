################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Move a motor back and forth using velocity and position mode of the TMC5062
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5062_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create TMC5062-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5062_eval(my_interface)
    mc = eval_board.ics[0]
    motor0 = eval_board.motors[0]
    print(motor0)
    motor1 = eval_board.motors[1]
    print(motor1)

    for i in range(2):
        print("Preparing parameter for motor" + str(i) + "...")
        eval_board.write_register(mc.REG.A1[i], 1000)
        eval_board.write_register(mc.REG.V1[i], 50000)
        eval_board.write_register(mc.REG.D1[i], 500)
        eval_board.write_register(mc.REG.DMAX[i], 500)
        eval_board.write_register(mc.REG.VSTART[i], 0)
        eval_board.write_register(mc.REG.VSTOP[i], 10)
        eval_board.write_register(mc.REG.AMAX[i], 1000)

    # Clear actual positions
    motor0.actual_position = 0
    motor1.actual_position = 0

    print("Rotating...")
    motor0.rotate(2 * 25600)
    motor1.rotate(-4 * 25600)
    time.sleep(5)

    print("Stopping...")
    motor0.stop()
    motor1.stop()
    time.sleep(1)

    print("Moving back to 0...")
    motor0.move_to(0, 100000)
    motor1.move_to(0, 100000)

    # Wait until position 0 is reached by both motors
    while (motor0.actual_position != 0) or (motor1.actual_position != 0):
        print("Actual position motor0: " + str(motor0.actual_position) + "   "
              + "actual position motor1: " + str(motor1.actual_position))
        time.sleep(0.2)

    print("Reached position 0")

print("\nReady.")
