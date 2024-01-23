################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
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
    motor1 = eval_board.motors[0]
    motor2 = eval_board.motors[1]

    # Motor 1

    # Ramp_Parameters_Setting for Position Mode
    eval_board.set_axis_parameter(motor1.AP.StartVelocity, 0, 40000)
    eval_board.set_axis_parameter(motor1.AP.StopVelocity, 0, 40001)
    eval_board.set_axis_parameter(motor1.AP.V1, 0, 25000)
    eval_board.set_axis_parameter(motor1.AP.MaxVelocity, 0, 100000)
    eval_board.set_axis_parameter(motor1.AP.A1, 0, 10000)
    eval_board.set_axis_parameter(motor1.AP.MaxAcceleration, 0, 10000)
    eval_board.set_axis_parameter(motor1.AP.D1, 0, 10)
    # Current_Settings1
    eval_board.set_axis_parameter(motor1.AP.MaxCurrent, 0, 31)
    eval_board.set_axis_parameter(motor1.AP.StandbyCurrent, 0, 10)
    eval_board.set_axis_parameter(motor1.AP.FSR_IREF, 0, 3)
    eval_board.set_axis_parameter(motor1.AP.CurrentScalingSelector, 0, 3)
    eval_board.set_axis_parameter(motor1.AP.GlobalCurrentScalerA, 0, 251)
    time.sleep(1)
    # Resetting the current position to 0
    eval_board.set_axis_parameter(motor1.AP.ActualPosition, 0, 0)
    print("Actual Position Motor 1:", eval_board.get_axis_parameter(motor1.AP.ActualPosition, 0))

    # Motor 2

    # Ramp_Parameters_Setting for Position Mode
    eval_board.set_axis_parameter(motor2.AP.StartVelocity, 1, 40000)
    eval_board.set_axis_parameter(motor2.AP.StopVelocity, 1, 40001)
    eval_board.set_axis_parameter(motor2.AP.V1, 1, 25000)
    eval_board.set_axis_parameter(motor2.AP.MaxVelocity, 0, 100000)
    eval_board.set_axis_parameter(motor2.AP.A1, 1, 10000)
    eval_board.set_axis_parameter(motor2.AP.MaxAcceleration, 1, 10000)
    eval_board.set_axis_parameter(motor2.AP.D1, 1, 10)
    # Current_Settings1
    eval_board.set_axis_parameter(motor2.AP.MaxCurrent, 1, 31)
    eval_board.set_axis_parameter(motor2.AP.StandbyCurrent, 1, 10)
    eval_board.set_axis_parameter(motor2.AP.FSR_IREF, 1, 1)
    eval_board.set_axis_parameter(motor2.AP.CurrentScalingSelector, 1, 0)
    eval_board.set_axis_parameter(motor2.AP.GlobalCurrentScalerA, 1, 251)
    time.sleep(1)
    # Resetting the current position to 0
    eval_board.set_axis_parameter(motor2.AP.ActualPosition, 0, 0)
    print("Actual Position Motor 2:", eval_board.get_axis_parameter(motor2.AP.ActualPosition, 0))

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
