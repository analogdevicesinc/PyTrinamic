################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
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
    # Ramp_Parameters_Setting for Position Mode
    eval_board.set_axis_parameter(motor.AP.StartVelocity, 0, 40000)
    eval_board.set_axis_parameter(motor.AP.StopVelocity, 0, 40001)
    eval_board.set_axis_parameter(motor.AP.V1, 0, 25000)
    eval_board.set_axis_parameter(motor.AP.MaxVelocity, 0, 100000)
    eval_board.set_axis_parameter(motor.AP.A1, 0, 10000)
    eval_board.set_axis_parameter(motor.AP.MaxAcceleration, 0, 10000)
    eval_board.set_axis_parameter(motor.AP.D1, 0, 10)
    # Current_Settings
    eval_board.set_axis_parameter(motor.AP.MaxCurrent, 0, 31)
    eval_board.set_axis_parameter(motor.AP.StandbyCurrent, 0, 10)
    eval_board.set_axis_parameter(motor.AP.FSR_IREF, 0, 3)
    eval_board.set_axis_parameter(motor.AP.CurrentScalingSelector, 0, 3)
    eval_board.set_axis_parameter(motor.AP.GlobalCurrentScalerA, 0, 251)
    time.sleep(1)

    # Resetting the current position to 0
    eval_board.set_axis_parameter(motor.AP.ActualPosition, 0, 0)
    print(eval_board.get_axis_parameter(motor.AP.ActualPosition, 0))

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
