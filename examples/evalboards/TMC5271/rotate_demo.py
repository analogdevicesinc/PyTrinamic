################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""
Move a motor back and forth using velocity and position mode of the TMC5271
"""

import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5271_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    # Create TMC5271-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5271_eval(my_interface)
    motor = eval_board.motors[0]
    mc = eval_board.ics[0]

    # Set the current scaling selector
    eval_board.set_axis_parameter(motor.AP.CurrentScalingSelector, 0, 3)

    # Ramp parameters setting for Position Mode
    eval_board.write_register(mc.REG.VSTART, 40000)
    eval_board.write_register(mc.REG.VSTOP, 40001)
    eval_board.write_register(mc.REG.V1, 25000)
    eval_board.write_register(mc.REG.VMAX, 100000)
    eval_board.write_register(mc.REG.A1, 10000)
    eval_board.write_register(mc.REG.AMAX, 10000)
    eval_board.write_register(mc.REG.D1, 10)
    # Current settings
    eval_board.write_register_field(mc.FIELD.IRUN, 31)
    eval_board.write_register_field(mc.FIELD.IHOLD, 10)
    eval_board.write_register_field(mc.FIELD.FSR, 0)
    eval_board.write_register_field(mc.FIELD.FSR_IREF, 3)
    eval_board.write_register_field(mc.FIELD.GLOBALSCALER_A, 251)
    time.sleep(1)
    # Resetting the current position to 0
    eval_board.write_register(mc.REG.XACTUAL, 0)
    print("Actual Position", eval_board.read_register(mc.REG.XACTUAL, 0))

    print("Rotating...")
    motor.rotate(2*25600)
    time.sleep(5)
    print("Stopping...")
    motor.stop()
    time.sleep(1)

    print("Moving back to 0...")
    motor.move_to(0, 4*25600)

    # Wait until position 0 is reached
    while motor.actual_position != 0:
        print("Actual position: " + str(motor.actual_position))
        time.sleep(0.2)
    print("Reached position 0")

print("\nReady.")
