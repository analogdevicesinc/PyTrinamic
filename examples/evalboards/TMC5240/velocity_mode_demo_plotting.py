################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demonstrates the velocity mode of the TMC5240

It includes plotting of the actual velocity over time.

Note that the example requires matplotlib to be installed (using `pip install matplotlib`).
"""

import time
from dataclasses import dataclass

from matplotlib import pyplot as plt

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5240_eval


# 16 MHz this is the clock frequency of the clock from the Landungsbruecke to TMC5240-EVAL
f_clk_hz_hz = 16_000_000
# Scaling factors from the TMC5240 datasheet
velocity_scaling_factor = 2**24 / f_clk_hz_hz
acceleration_scaling_factor = 2**41 / f_clk_hz_hz**2


def velocity_usteps_per_second_to_internal(usteps_per_second_value):
    return int(usteps_per_second_value * velocity_scaling_factor)


def velocity_internal_to_usteps_per_second(internal_value):
    return internal_value / velocity_scaling_factor


def acceleration_usteps_per_second_squared_to_internal(usteps_per_second_squared_value):
    return int(usteps_per_second_squared_value * acceleration_scaling_factor)


def acceleration_internal_to_usteps_per_second_squared(internal_value):
    return internal_value / acceleration_scaling_factor


class TimeoutTimer:
    def __init__(self, timeout_in_seconds):
        self._start = time.time()
        self._timeout_in_seconds = timeout_in_seconds

    def has_expired(self):
        return time.time() - self._start > self._timeout_in_seconds


@dataclass
class Sample:
    timestamp: float
    velocity: int


with ConnectionManager().connect() as my_interface:
    eval_board = TMC5240_eval(my_interface)
    motor = eval_board.motors[0]
    mc = eval_board.ics[0]

    # Set current reference resistor to 12k via IREF_R2 and IREF_R3 on the eval board.
    motor.set_axis_parameter(motor.AP.CurrentScalingSelector, 0)

    # Set the acceleration to 51200 µsteps per second squared
    # This will result in a ramp time of 1 second to reach 51200 µsteps per second.
    eval_board.write_register(
        mc.REG.AMAX, acceleration_usteps_per_second_squared_to_internal(51200)
    )
    # Set RAMPMODE to "Velocity mode to positive VMAX".
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 0x1)

    # Start the velocity mode by specifying a target velocity of 51200 µsteps per second.
    eval_board.write_register(
        mc.REG.VMAX, velocity_usteps_per_second_to_internal(51200)
    )
    timeout_timer = TimeoutTimer(2)
    samples = []
    while not timeout_timer.has_expired():
        samples.append(Sample(time.time(), eval_board.read_register(mc.REG.VACTUAL)))

    # Stop the motor by setting VMAX to 0
    eval_board.write_register(mc.REG.VMAX, 0)
    timeout_timer = TimeoutTimer(1)
    while not timeout_timer.has_expired():
        samples.append(Sample(time.time(), eval_board.read_register(mc.REG.VACTUAL)))

    fig, ax = plt.subplots()
    ax.plot(
        [sample.timestamp - samples[0].timestamp for sample in samples],
        [velocity_internal_to_usteps_per_second(sample.velocity) for sample in samples],
    )
    plt.show()
