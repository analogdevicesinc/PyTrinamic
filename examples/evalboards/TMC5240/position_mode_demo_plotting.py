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
from typing import Literal, List

from matplotlib import pyplot as plt

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5240_eval


number_of_ramp_points: Literal[4, 6, 8] = 4

# 16 MHz this is the clock frequency of the clock fed from the Landungsbruecke to TMC5240.
f_clk_hz = 16_000_000
# Scaling factors from the TMC5240 datasheet
velocity_scaling_factor = 2**24 / f_clk_hz
acceleration_scaling_factor = 2**41 / f_clk_hz**2


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
class RampConfig:
    a1: int
    a2: int
    amax: int
    v1: int
    v2: int
    vmax: int


@dataclass
class Sample:
    time_stamp: float
    value: int


@dataclass
class Record:
    vactual: Sample
    xactual: Sample


with ConnectionManager().connect() as my_interface:
    eval_board = TMC5240_eval(my_interface)
    tmc5240 = eval_board.ics[0]

    if number_of_ramp_points == 4:
        ramp_config = RampConfig(a1=51200, a2=0, amax=0, v1=51200, v2=51200, vmax=51200)
    elif number_of_ramp_points == 6:
        ramp_config = RampConfig(
            a1=51200, a2=25600, amax=0, v1=25600, v2=51200, vmax=51200
        )
    elif number_of_ramp_points == 8:
        ramp_config = RampConfig(
            a1=51200, a2=25600, amax=51200, v1=17600, v2=33600, vmax=51200
        )
    else:
        raise ValueError("Invalid number of ramp points")

    eval_board.write_register(
        tmc5240.REG.A1,
        acceleration_usteps_per_second_squared_to_internal(ramp_config.a1),
    )
    eval_board.write_register(
        tmc5240.REG.A2,
        acceleration_usteps_per_second_squared_to_internal(ramp_config.a2),
    )
    eval_board.write_register(
        tmc5240.REG.AMAX,
        acceleration_usteps_per_second_squared_to_internal(ramp_config.amax),
    )
    eval_board.write_register(
        tmc5240.REG.D1,
        acceleration_usteps_per_second_squared_to_internal(ramp_config.a1),
    )
    eval_board.write_register(
        tmc5240.REG.D2,
        acceleration_usteps_per_second_squared_to_internal(ramp_config.a2),
    )
    eval_board.write_register(
        tmc5240.REG.DMAX,
        acceleration_usteps_per_second_squared_to_internal(ramp_config.amax),
    )
    eval_board.write_register(
        tmc5240.REG.V1, velocity_usteps_per_second_to_internal(ramp_config.v1)
    )
    eval_board.write_register(
        tmc5240.REG.V2, velocity_usteps_per_second_to_internal(ramp_config.v2)
    )
    eval_board.write_register(
        tmc5240.REG.VMAX, velocity_usteps_per_second_to_internal(ramp_config.vmax)
    )

    # Set RAMPMODE to "Positioning mode".
    eval_board.write_register_field(tmc5240.FIELD.RAMPMODE, 0x0)

    # Clear the actual position to have a known starting point.
    eval_board.write_register(tmc5240.REG.XACTUAL, 0)

    # Start the position mode by specifying a target position of 2 * 51200 µsteps.
    # With a 200 steps/rev motor and 256 microsteps this is 2 revolutions.
    eval_board.write_register(tmc5240.REG.XTARGET, 2 * 51200)
    timeout_timer = TimeoutTimer(10)
    samples: List[Record] = []
    while (
        not eval_board.read_register_field(tmc5240.FIELD.POSITION_REACHED)
        and not timeout_timer.has_expired()
    ):
        samples.append(
            Record(
                vactual=Sample(
                    time.time(), eval_board.read_register(tmc5240.REG.VACTUAL)
                ),
                xactual=Sample(
                    time.time(), eval_board.read_register(tmc5240.REG.XACTUAL)
                ),
            )
        )

    # Plot the results
    fig, ax = plt.subplots()
    ax.plot(
        [sample.vactual.time_stamp - timeout_timer._start for sample in samples],
        [
            velocity_internal_to_usteps_per_second(sample.vactual.value)
            for sample in samples
        ],
        "b-",
        label="Velocity (µsteps/s)",
    )
    ax_sec = ax.twinx()
    ax_sec.plot(
        [sample.xactual.time_stamp - timeout_timer._start for sample in samples],
        [sample.xactual.value for sample in samples],
        "y-",
        label="Position (µsteps)",
    )
    ax.set_title(f"TMC5240 {number_of_ramp_points}-Point Ramp Profile")
    fig.legend()
    plt.show()
