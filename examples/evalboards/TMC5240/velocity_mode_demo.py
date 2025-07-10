################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5240_eval


with ConnectionManager().connect() as my_interface:

    eval_board = TMC5240_eval(my_interface)
    motor = eval_board.motors[0]
    mc = eval_board.ics[0]

    eval_board.write_register(mc.REG.AMAX, 200) # Set the acceleration
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 0x1) # Set RAMPMODE to "Velocity mode to positive VMAX"

    eval_board.write_register(mc.REG.VMAX, 51200) # Start the velocity mode by specifying a target velocity of 51200 steps per second.
    time.sleep(2) # Keep the motor running for 2 seconds
    eval_board.write_register(mc.REG.VMAX, 0) # Stop the motor
    time.sleep(1) # Let the motor stop
