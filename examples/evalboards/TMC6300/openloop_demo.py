################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Move a motor back and forth using velocity mode of the TMC6300
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC6300_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    eval_board = TMC6300_eval(my_interface)
    motor = eval_board.motors[0]

    # configure
    motor.set_standby_current(0)
    motor.set_commutation_mode(0)

    print("Rotating...")
    motor.set_target_pwm(6000)
    time.sleep(3)

    print("Stopping...")
    motor.set_target_pwm(0)
    time.sleep(2)

    print("Rotating back...")
    motor.set_target_pwm(-6000)
    time.sleep(3)

    print("Stopping...")
    motor.set_target_pwm(0)
    time.sleep(1)

print("\nReady.")
