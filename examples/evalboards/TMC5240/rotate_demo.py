################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards.TMC5240_eval import TMC5240_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    eval_board = TMC5240_eval(my_interface)
    motor = eval_board.motors[0]
    motor.set_axis_parameter(motor.AP.MaxAcceleration,51200)

    print("Rotating...")
    motor.rotate(51200)
    time.sleep(2)

    print("Stopping...")
    motor.stop()
    time.sleep(1)

print("\nReady.")

