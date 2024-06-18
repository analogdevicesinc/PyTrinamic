################################################################################
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Sets the StallGuard2 threshold such that the stall guard value (i.e SG value) is zero
when the motor comes close to stall and also sets the stop on stall velocity to a value
one less than the actual velocity of the motor
"""

import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards.TMC5240_eval import TMC5240_eval


def stallguard2_init(mc, motor, eval_board, init_velocity):
    # Resetting SG2 threshold and stop on stall velocity to zero
    eval_board.write_register_field(mc.FIELD.SGT, 0)
    eval_board.write_register_field(mc.FIELD.SG_STOP, 0)
    eval_board.write_register(mc.REG.TCOOLTHRS, 0)

    # Setting current reference resistor as 12k
    motor.set_axis_parameter(motor.AP.CurrentScalingSelector, 3)

    print("Initial StallGuard2 values:")
    print("Filter:", eval_board.read_register_field(mc.FIELD.SFILT))
    print("Threshold:", eval_board.read_register_field(mc.FIELD.SGT))
    print("stop_velocity:", eval_board.read_register_field(mc.FIELD.TCOOLTHRS))

    print("Rotating...")
    motor.rotate(init_velocity)
    sgthresh = 0
    sgt = 0
    load_samples = []
    while (sgt == 0) and (sgthresh < 64):
        load_samples = []
        eval_board.write_register_field(mc.FIELD.SGT, sgthresh)
        time.sleep(0.2)
        sgthresh += 1
        for i in range(50):
            load_samples.append(eval_board.read_register_field(mc.FIELD.SG_RESULT))
        if not any(load_samples):
            sgt = 0
        else:
            sgt = max(load_samples)
    while 1:
        load_samples = []
        for i in range(50):
            load_samples.append(eval_board.read_register_field(mc.FIELD.SG_RESULT))
        if 0 in load_samples:
            eval_board.write_register_field(mc.FIELD.IRUN, eval_board.read_register_field(mc.FIELD.IRUN)-1)
        else:
            break

    eval_board.write_register_field(mc.FIELD.SG_STOP, 1)
    eval_board.write_register_field(mc.FIELD.TCOOLTHRS, motor.actual_velocity-1)

    print("Configured StallGuard2 parameters:")
    print("Filter:", eval_board.read_register_field(mc.FIELD.SFILT))
    print("Threshold:", eval_board.read_register_field(mc.FIELD.SGT))
    print("stop_velocity:", eval_board.read_register_field(mc.FIELD.TCOOLTHRS))


def main():
    pytrinamic.show_info()

    with ConnectionManager().connect() as my_interface:
        print(my_interface)

        eval_board = TMC5240_eval(my_interface)
        motor = eval_board.motors[0]
        mc = eval_board.ics[0]

        print("Preparing parameters")
        # preparing drive settings
        eval_board.write_register_field(mc.FIELD.IRUN, 17)
        eval_board.write_register_field(mc.FIELD.IHOLD, 6)
        eval_board.write_register_field(mc.FIELD.MRES, 5)  # 256 micro-steps
        print("Max_Velocity:", eval_board.read_register(mc.REG.VMAX))
        print("Max_Acceleration:", eval_board.read_register(mc.REG.AMAX))

        time.sleep(1.0)

        # clear position counter
        motor.actual_position = 0
        eval_board.write_register(mc.REG.AMAX, 500)

        # set up StallGuard2
        print("Configuring StallGuard2 parameters...")
        stallguard2_init(mc, motor, eval_board, init_velocity=5000)
        print("Apply load and try to stall the motor...")
        while not (motor.actual_velocity == 0):
            pass
        print("Motor stopped by StallGuard2!")


if __name__ == "__main__":
    main()
