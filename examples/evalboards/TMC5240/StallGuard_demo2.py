################################################################################
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
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


def stallguard2_init(motor, init_velocity):
    # Resetting SG2 threshold and stop on stall velocity to zero
    motor.set_axis_parameter(motor.AP.SG2Threshold, 0)
    motor.set_axis_parameter(motor.AP.smartEnergyStallVelocity, 0)
    motor.set_axis_parameter(motor.AP.CurrentScalingSelector, 3)

    print("Initial StallGuard2 values:")
    print("Filter:", motor.get_axis_parameter(motor.AP.SG2FilterEnable))
    print("Threshold:", motor.get_axis_parameter(motor.AP.SG2Threshold))
    print("stop_velocity:", motor.get_axis_parameter(motor.AP.smartEnergyStallVelocity))

    print("Rotating...")
    motor.rotate(init_velocity)
    sgthresh = 0
    sgt = 0
    load_samples = []
    while (sgt == 0) and (sgthresh < 64):
        load_samples = []
        motor.set_axis_parameter(motor.AP.SG2Threshold, sgthresh)
        time.sleep(0.2)
        sgthresh += 1
        for i in range(50):
            load_samples.append(motor.get_axis_parameter(motor.AP.LoadValue))
        if not any(load_samples):
            sgt = 0
        else:
            sgt = max(load_samples)
    while 1:
        load_samples = []
        for i in range(50):
            load_samples.append(motor.get_axis_parameter(motor.AP.LoadValue))
        if 0 in load_samples:
            motor.set_axis_parameter(motor.AP.MaxCurrent, motor.get_axis_parameter(motor.AP.MaxCurrent) - 1)
        else:
            break

    motor.set_axis_parameter(motor.AP.smartEnergyStallVelocity, motor.actual_velocity-1)

    print("Configured StallGuard2 parameters:")
    print("Filter:", motor.get_axis_parameter(motor.AP.SG2FilterEnable))
    print("Threshold:", motor.get_axis_parameter(motor.AP.SG2Threshold))
    print("stop_velocity:", motor.get_axis_parameter(motor.AP.smartEnergyStallVelocity))


def main():
    pytrinamic.show_info()

    with ConnectionManager().connect() as my_interface:
        print(my_interface)

        eval_board = TMC5240_eval(my_interface)
        motor = eval_board.motors[0]
        print("Preparing parameters")
        # preparing drive settings
        motor.set_axis_parameter(motor.AP.MaxCurrent, 17)
        motor.set_axis_parameter(motor.AP.StandbyCurrent, 6)
        motor.set_axis_parameter(motor.AP.MicrostepResolution, 8)  # 256 micro-steps
        print("Max_Velocity:", motor.get_axis_parameter(motor.AP.MaxVelocity))
        print("Max_Acceleration:", motor.get_axis_parameter(motor.AP.MaxAcceleration))

        time.sleep(1.0)

        # clear position counter
        motor.actual_position = 0
        motor.set_axis_parameter(motor.AP.MaxAcceleration, 500)

        # set up StallGuard2
        print("Configuring StallGuard2 parameters...")
        stallguard2_init(motor, init_velocity=10000)
        print("Apply load and try to stall the motor...")
        while not (motor.actual_velocity == 0):
            pass
        print("Motor stopped by StallGuard2!")


if __name__ == "__main__":
    main()

