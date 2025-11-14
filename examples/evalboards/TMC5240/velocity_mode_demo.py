################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demonstrates the velocity mode of the TMC5240"""

import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5240_eval


with ConnectionManager().connect() as my_interface:
    eval_board = TMC5240_eval(my_interface)
    tmc5240 = eval_board.ics[0]

    # Set the acceleration to ~51200 µsteps per second squared.
    eval_board.write_register(tmc5240.REG.AMAX, 400)
    # Set RAMPMODE to "Velocity mode to positive VMAX".
    eval_board.write_register_field(tmc5240.FIELD.RAMPMODE, 0x1)

    # Start the velocity mode by specifying a target velocity of ~51200 steps per second.
    eval_board.write_register(tmc5240.REG.VMAX, 51200)
    time.sleep(2)  # Keep the motor running for 2 seconds.

    # Stop the motor by setting VMAX to 0.
    eval_board.write_register(tmc5240.REG.VMAX, 0)
    time.sleep(1)  # Wait for the motor to stop.
