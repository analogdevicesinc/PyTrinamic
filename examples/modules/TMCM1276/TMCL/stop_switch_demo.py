################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1276
import time

pytrinamic.show_info()

# This example is using PCAN, if you want to use another connection please change the next line.
connection_manager = ConnectionManager("--interface pcan_tmcl")

with connection_manager.connect() as my_interface:
    module = TMCM1276(my_interface)
    motor = module.motors[0]

    print("Preparing parameters")
    # preparing linear ramp settings
    motor.max_acceleration = 20000

    while 1:
        if motor.get_axis_parameter(motor.AP.RightEndstop):
            motor.stop()
            time.sleep(5)
            print("Rotating in opposite direction")
            motor.rotate(-50000)
            time.sleep(5)
            motor.stop()
            break
        else:
            print("Rotating")
            motor.rotate(50000)
            time.sleep(5)

