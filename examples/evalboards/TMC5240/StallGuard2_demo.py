################################################################################
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demonstrates the StallGuard2 feature of the TMC5240.

Sets the StallGuard2 threshold such that the stall guard value (i.e SG value) is zero
when the motor comes close to stall and also sets the stop on stall velocity to a value
one less than the actual velocity of the motor.
"""

import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards.TMC5240_eval import TMC5240_eval


def stallguard2_init(mc, eval_board, init_velocity):
    """Auto configure the StallGuard2 parameters such that the motor stops when it stalls.

    :param mc: The TMC5240 IC instance
    :param eval_board: The TMC5240 evaluation board instance
    :param init_velocity: The initial velocity to start the motor with given in µsteps per second

    The real world init_velocity is a bit off due to the internal velocity scaling of the TMC5240.
    """
    # Resetting SG2 threshold and stop on stall velocity to zero
    eval_board.write_register_field(mc.FIELD.SGT, 0)
    eval_board.write_register_field(mc.FIELD.SG_STOP, 0)
    eval_board.write_register(mc.REG.TCOOLTHRS, 0)

    print("Initial StallGuard2 values:")
    print("  Filter:", eval_board.read_register_field(mc.FIELD.SFILT))
    print("  Threshold:", eval_board.read_register_field(mc.FIELD.SGT))
    print("  Stop Velocity:", eval_board.read_register_field(mc.FIELD.TCOOLTHRS))

    print("Rotating...")
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 0x1)
    eval_board.write_register(mc.REG.VMAX, init_velocity)
    sgthresh = 0
    sgt = 0
    while (sgt == 0) and (sgthresh < 64):
        load_samples = []
        eval_board.write_register_field(mc.FIELD.SGT, sgthresh)
        time.sleep(0.2)
        sgthresh += 1
        for _ in range(50):
            load_samples.append(eval_board.read_register_field(mc.FIELD.SG_RESULT))
        if not any(load_samples):
            sgt = 0
        else:
            sgt = max(load_samples)
    while True:
        load_samples = []
        for _ in range(50):
            load_samples.append(eval_board.read_register_field(mc.FIELD.SG_RESULT))
        if 0 in load_samples:
            eval_board.write_register_field(
                mc.FIELD.IRUN, eval_board.read_register_field(mc.FIELD.IRUN) - 1
            )
        else:
            break

    eval_board.write_register_field(mc.FIELD.SG_STOP, 1)
    eval_board.write_register_field(
        mc.FIELD.TCOOLTHRS, eval_board.read_register(mc.REG.VACTUAL) - 1
    )

    print("Configured StallGuard2 parameters:")
    print("  Filter:", eval_board.read_register_field(mc.FIELD.SFILT))
    print("  Threshold:", eval_board.read_register_field(mc.FIELD.SGT))
    print("  Stop Velocity:", eval_board.read_register_field(mc.FIELD.TCOOLTHRS))


def main():
    with ConnectionManager().connect() as my_interface:
        eval_board = TMC5240_eval(my_interface)
        motor = eval_board.motors[0]
        mc = eval_board.ics[0]

        print("Preparing parameters")
        # Set current reference resistor to 12k
        motor.set_axis_parameter(motor.AP.CurrentScalingSelector, 3)
        # Change the current settings
        eval_board.write_register_field(mc.FIELD.IRUN, 17)
        eval_board.write_register_field(mc.FIELD.IHOLD, 6)
        # 256 micro-steps resolution
        eval_board.write_register_field(mc.FIELD.MRES, 5)
        # Set the acceleration to ~51200 µsteps per second squared
        eval_board.write_register(mc.REG.AMAX, 400)

        # Set up StallGuard2
        print("Configuring StallGuard2 parameters...")
        stallguard2_init(mc, eval_board, init_velocity=5000)
        print("Apply load and try to stall the motor...")
        while not (eval_board.read_register(mc.REG.VACTUAL) == 0):
            pass
        print("Motor stopped by StallGuard2!")


if __name__ == "__main__":
    main()
