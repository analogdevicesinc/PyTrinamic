################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Move both motors back and forth using velocity and position mode of the TMC5272
"""

import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5272_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    # Create TMC5272-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5272_eval(my_interface)
    mc = eval_board.ics[0]
    motor1 = eval_board.motors[0]
    motor2 = eval_board.motors[1]

    # Set the current scaling selector
    eval_board.set_axis_parameter(motor1.AP.CurrentScalingSelector, 0, 3)

    # Motor 1

    # Ramp parameters setting for Position Mode
    eval_board.write_register(mc.REG.M0_VSTART, 40000)
    eval_board.write_register(mc.REG.M0_VSTOP, 40001)
    eval_board.write_register(mc.REG.M0_V1, 25000)
    eval_board.write_register(mc.REG.M0_VMAX, 100000)
    eval_board.write_register(mc.REG.M0_A1, 10000)
    eval_board.write_register(mc.REG.M0_AMAX, 10000)
    eval_board.write_register(mc.REG.M0_D1, 10)
    # Current settings
    eval_board.write_register_field(mc.FIELD.M0_IHOLD_IRUN_IRUN, 31)
    eval_board.write_register_field(mc.FIELD.M0_IHOLD_IRUN_IHOLD, 10)
    eval_board.write_register_field(mc.FIELD.M0_FSR, 3)
    eval_board.write_register_field(mc.FIELD.M0_FSR_IREF, 3)
    eval_board.write_register_field(mc.FIELD.GLOBAL_SCALER_GLOBALSCALER_M0_A, 251)
    time.sleep(1)
    # Resetting the current position to 0
    eval_board.write_register(mc.REG.M0_XACTUAL, 0)
    print("Actual Position Motor 1:", eval_board.read_register(mc.REG.M0_XACTUAL, 0))

    # Motor 2

    # Ramp parameters setting for Position Mode
    eval_board.write_register(mc.REG.M1_VSTART, 40000)
    eval_board.write_register(mc.REG.M1_VSTOP, 40001)
    eval_board.write_register(mc.REG.M1_V1, 25000)
    eval_board.write_register(mc.REG.M1_VMAX, 100000)
    eval_board.write_register(mc.REG.M1_A1, 10000)
    eval_board.write_register(mc.REG.M1_AMAX, 10000)
    eval_board.write_register(mc.REG.M1_D1, 10)
    # Current settings
    eval_board.write_register_field(mc.FIELD.M1_IHOLD_IRUN_IRUN, 31)
    eval_board.write_register_field(mc.FIELD.M1_IHOLD_IRUN_IHOLD, 10)
    eval_board.write_register_field(mc.FIELD.M1_FSR, 3)
    eval_board.write_register_field(mc.FIELD.M1_FSR_IREF, 3)
    eval_board.write_register_field(mc.FIELD.GLOBAL_SCALER_GLOBALSCALER_M1_A, 251)
    time.sleep(1)
    # Resetting the current position to 0
    eval_board.write_register(mc.REG.M1_XACTUAL, 0)
    print("Actual Position Motor 2:", eval_board.read_register(mc.REG.M1_XACTUAL, 0))

    print("Rotating...")
    motor1.rotate(2*25600)
    motor2.rotate(2 * 25600)
    time.sleep(5)
    print("Stopping...")
    motor1.stop()
    motor2.stop()
    time.sleep(1)

    print("Moving back to 0...")
    motor1.move_to(0, 4*25600)
    motor2.move_to(0, 4*25600)

    # Wait until position 0 is reached
    while (motor1.actual_position and motor2.actual_position) != 0:
        print("Actual position Motor 1: " + str(motor1.actual_position))
        print("Actual position Motor 2: " + str(motor2.actual_position))
        time.sleep(0.2)

    print("Reached position 0")

print("\nReady.")
