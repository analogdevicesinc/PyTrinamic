################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Example on how to use TMC2262-EVAL.

Please note that the Landungsbruecke firmware presets some registers on startup!
To actually operate a motor with the TMC2262, some more configuration might be necessary.
"""

import time

from pytrinamic.connections import ConnectionManager

from pytrinamic.ic import TMC2262
from pytrinamic.evalboards import TMC2262_eval


with ConnectionManager().connect() as my_interface:
    tmc2262_eval = TMC2262_eval(my_interface)
    motor = tmc2262_eval.motors[0]

    # Reduce the current
    tmc2262_eval.write(TMC2262.REGMAP.IHOLD_IRUN.IHOLD, 10)
    tmc2262_eval.write(TMC2262.REGMAP.IHOLD_IRUN.IRUN, 64)

    # Set microstepping to 32 microsteps per full step -> reducing the steps per revolution to 6400 steps for a 200 steps/rev motor
    tmc2262_eval.write(TMC2262.REGMAP.CHOPCONF.MRES.choice.RES_32)

    # Let the Landungsbruecke generate some STEP pulses, that are fed into the STEP input of the TMC2262.
    # Set the STEP pulses acceleration and deceleration to 2,500 steps/s^2
    motor.set_axis_parameter(motor.AP.MaxAcceleration, 2500)

    # Now let the STEP pulses ramp up to the a target velocity of 6400 steps/s which is 1 round per second for a 200 steps/rev motor
    motor.set_target_velocity(6400)
    time.sleep(5)

    # Now stop the motor - ramp down to 0 steps/s
    motor.set_target_velocity(0)
    time.sleep(1)
