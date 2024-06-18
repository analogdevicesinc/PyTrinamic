################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1021
import time

pytrinamic.show_info()

with ConnectionManager("--interface serial_tmcl --port COM8 --data-rate 9600").connect() as my_interface:
    print(my_interface)
    module = TMCM1021(my_interface)
    motor = module.motors[0]

    # The configuration is based on our PD28-x-1021-TMCL
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not working.

    print("Preparing parameters...")

    # preparing drive settings
    motor.drive_settings.max_current = 128
    motor.drive_settings.standby_current = 0
    motor.drive_settings.boost_current = 0
    motor.drive_settings.microstep_resolution = motor.ENUM.MicrostepResolution256Microsteps
    print(motor.drive_settings)

    # preparing linear ramp settings
    motor.linear_ramp.max_acceleration = 51200
    motor.linear_ramp.max_velocity = 102400
    print(motor.linear_ramp)

    time.sleep(1.0)

    # clear position counter
    motor.actual_position = 0

    # start rotating motor for 1.5 sek
    print("Rotating...")
    motor.rotate(102400)
    
    # set up StahlGuard2
    print("Initial StallGuard2 values:")
    print(motor.stallguard2)

    motor.stallguard2.calibrate_zero()
    print("StallGuard2 after calibration:")
    print(motor.stallguard2)

    print("Try to stop motor...")

    while not(motor.actual_velocity == 0):
        print("Actual load value: " + str(motor.stallguard2.get_load_value()))
        time.sleep(0.2)
    
    time.sleep(3)
    print("Start rotating again")
    motor.rotate(102400)

    print("Initial CoolStep values:")
    print(motor.coolstep)
    motor.coolstep.calibrate()

    print("CoolStep after calibration:")
    print(motor.coolstep)

    time.sleep(10)

    # stop rotating motor
    print("Stopping...")
    motor.stop()

print("\nReady.")
