################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1636
import time

pytrinamic.show_info()
# connection_manager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
connection_manager = ConnectionManager("--interface kvaser_tmcl --module-id 1")

with connection_manager.connect() as my_interface:
    module = TMCM1636(my_interface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1636.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.drive_settings.motor_type = motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.drive_settings.pole_pairs = 4
    motor.drive_settings.max_current = 2000
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DIGITAL_HALL
    print(motor.drive_settings)

    # hall sensor configuration
    motor.digital_hall.direction = 0
    motor.digital_hall.polarity = 1
    motor.digital_hall.offset = 0
    motor.digital_hall.interpolation = 1
    print(motor.digital_hall)

    # enable ref switch 
    motor.set_axis_parameter(motor.AP.ReferenceSwitchEnable, 3)
    motor.set_axis_parameter(motor.AP.ReferenceSwitchPolarity, 0)

    print("\nRotate motor in clockwise direction...")
    motor.rotate(500)

    print("Waiting for right ref switch...")
    while not motor.get_axis_parameter(motor.AP.RightStopSwitch):
        time.sleep(0.1)

    print("Triggered!")
    motor.rotate(-500)

    print("Waiting for left ref switch...")
    while not motor.get_axis_parameter(motor.AP.LeftStopSwitch):
        time.sleep(0.1)

    print("Triggered!")
    print("Stopping motor...")
    motor.rotate(0)

print("\nReady.")
