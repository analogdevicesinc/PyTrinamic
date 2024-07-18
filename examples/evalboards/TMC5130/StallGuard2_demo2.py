################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Sets the StallGuard2 threshold such that the stall guard value (i.e SG value) is zero
when the motor comes close to stall and also sets the stop on stall velocity to a value
one less than the actual velocity of the motor
"""

import time
import pytrinamic
import math
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5130_eval

M_RES = 5
micro_steps_per_mechanical_revolution = 53687   # unit [ppt] = [µsteps / t]
def rotation2step(x):  # | converting  rotation or rps or rps^2 in Microsteps
    return round(x * (micro_steps_per_mechanical_revolution / pow(2, M_RES)))

def stallguard2_init(mc, motor, eval_board, init_velocity):
    # Resetting SG2 threshold and stop on stall velocity to zero
    eval_board.write_register_field(mc.FIELD.SGT, 0)
    eval_board.write_register_field(mc.FIELD.SG_STOP, 0)
    eval_board.write_register(mc.REG.TCOOLTHRS, 0)

    print("Initial StallGuard2 values:")
    print("Filter:", eval_board.read_register_field(mc.FIELD.SFILT))
    print("Threshold:", eval_board.read_register_field(mc.FIELD.SGT))
    print("stop_velocity:", eval_board.read_register_field(mc.FIELD.TCOOLTHRS))
    print("Rotating...")

    microstep_resolution = eval_board.read_register_field(mc.FIELD.MRES)
    v_max = rotation2step( init_velocity)     # internal unit  <- rps
    eval_board.write_register_field(mc.FIELD.VMAX, v_max)                   # set max speed in the register
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 1)                   # activate velocity mode in positive direction
    sgthresh = 0
    sgt = 0

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
    eval_board.write_register_field(mc.FIELD.TCOOLTHRS, eval_board.read_register_field(mc.FIELD.VACTUAL)-1)

    print("Configured StallGuard2 parameters:")
    print("Filter:", eval_board.read_register_field(mc.FIELD.SFILT))
    print("Threshold:", eval_board.read_register_field(mc.FIELD.SGT))
    print("stop_velocity:", eval_board.read_register_field(mc.FIELD.TCOOLTHRS))

def main():
    pytrinamic.show_info()

    with ConnectionManager().connect() as my_interface:
        print(my_interface)

        eval_board = TMC5130_eval(my_interface)
        motor = eval_board.motors[0]
        mc = eval_board.ics[0]

        print("Preparing parameters")
        # preparing drive settings
        eval_board.write_register_field(mc.FIELD.IRUN, 17)
        eval_board.write_register_field(mc.FIELD.IHOLD, 6)
        eval_board.write_register_field(mc.FIELD.MRES, M_RES)  # 2^MRES = 2^5 = 32 micro-steps
        print("Max_Velocity:", eval_board.read_register(mc.REG.VMAX))
        print("Max_Acceleration:", eval_board.read_register(mc.REG.AMAX))
        time.sleep(1.0)

        # clear position counter
        eval_board.write_register_field(mc.FIELD.XACTUAL, 0)
        eval_board.write_register(mc.REG.AMAX, 500)

        # set up StallGuard2
        print("Configuring StallGuard2 parameters...")
        stallguard2_init(mc, motor, eval_board, init_velocity=3)    # velocity in [rps]
        print("Apply load and try to stall the motor...")

        while not (eval_board.read_register_field(mc.FIELD.VACTUAL) == 0):
            pass

        eval_board.write_register_field(mc.FIELD.SGT, 0)        # Turn the StallGuard2 off
        eval_board.write_register_field(mc.FIELD.SG_STOP, 0)
        eval_board.write_register(mc.REG.TCOOLTHRS, 0)
        eval_board.write_register_field(mc.FIELD.VMAX, 0)
        eval_board.write_register_field(mc.FIELD.RAMPMODE, 1)
        print("Motor stopped by StallGuard2!")

if __name__ == "__main__":
    main()
