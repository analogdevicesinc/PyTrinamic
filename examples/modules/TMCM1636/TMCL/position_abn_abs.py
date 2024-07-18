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
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not working. 

    # config abn encoder 
    motor.abn_encoder.resolution = 4096
    motor.abn_encoder.direction = 1
    motor.abn_encoder.init_mode = motor.ENUM.ENCODER_INIT_MODE_0
    print(motor.abn_encoder)
    
    # config absolute encoder 
    motor.absolute_encoder.type = 1
    motor.absolute_encoder.init_mode = 0
    motor.absolute_encoder.direction = 1
    motor.absolute_encoder.offset = 0
    print(motor.absolute_encoder)

    # config drive mode 
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_ABN_ENCODER
    motor.drive_settings.position_sensor = motor.ENUM.POS_SELECTION_ABS
    motor.drive_settings.open_loop_current = 1000
    print(motor.drive_settings)
    time.sleep(1)

    # motion settings 
    motor.linear_ramp.max_velocity = 1000
    motor.linear_ramp.max_acceleration = 250
    print(motor.linear_ramp)

    # clear actual position 
    motor.linear_ramp.actual_position = 0

    # move to new target position 
    motor.move_to(1000000)

    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: "
              + str(motor.actual_position))
        time.sleep(0.2)

    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DISABLED
    motor.drive_settings.position_sensor = motor.ENUM.POS_SELECTION_SAME

print("\nReady.")
