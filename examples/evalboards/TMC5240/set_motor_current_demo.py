################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""This demo shows how to set the motor current."""

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5240_eval


class RrefResistor:
    R_48K = 0
    R_24K = 1
    R_16K = 2
    R_12K = 3


with ConnectionManager().connect() as my_interface:
    eval_board = TMC5240_eval(my_interface)
    motor = eval_board.motors[0]
    tmc5240 = eval_board.ics[0]

    # Modify the reference resistor on the eval board via IREF_R2 and IREF_R3.
    # The value of 16 kΩ is the default setting.
    motor.set_axis_parameter(motor.AP.CurrentScalingSelector, RrefResistor.R_16K)

    # Motor run current: 16/32 * Imax
    eval_board.write_register_field(tmc5240.FIELD.IRUN, 16)
    # Motor standstill current: 10/32 * Imax
    eval_board.write_register_field(tmc5240.FIELD.IHOLD, 10)
