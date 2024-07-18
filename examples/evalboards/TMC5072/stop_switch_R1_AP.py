################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""
Automatically stops the motor during active (low active) right reference switch input using APs.
"""

import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5072_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create TMC5072-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5072_eval(my_interface)
    mc = eval_board.ics[0]
    motor0 = eval_board.motors[0]
    print(motor0)

    # Preparing parameter for motor 0...
    motor0.set_axis_parameter(motor0.AP.MaxVelocity, 100000)
    motor0.set_axis_parameter(motor0.AP.MaxAcceleration, 1000)

    # Invert the active polarity of the right reference switch input (low active) and
    # Enable the automatic motor stop during active right reference switch input
    motor0.set_axis_parameter(motor0.AP.SW_MODE, 0xA)

    print("The motor rotates until left reference switch becomes active")
    motor0.rotate(10*25600)

    while motor0.get_axis_parameter(motor0.AP.RightEndstop) != 1:
        pass
    print("Switch is active!")
    while motor0.actual_velocity != 0:
        pass
    print("Motor stopped!")
    # Stop the motor to make sure that it doesn't start rotating again when the switch becomes inactive
    motor0.stop()

print("\nReady.")
