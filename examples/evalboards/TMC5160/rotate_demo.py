################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Move a motor back and forth using velocity and position mode of the TMC5160

Line 31, we set a lower run/standby current for the motor. Using NEMA17, this should result in a coil current around 800mA.
If the motor is stalling due to too low current, set motorCurrent higher.
If a lower value still is needed, set GLOBAL_SCALER register to 128 to half motor current.
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5160_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create TMC5160-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5160_eval(my_interface)
    mc = eval_board.ics[0]
    motor = eval_board.motors[0]

    print("Preparing parameters...")
    eval_board.write_register(mc.REG.A1, 1000)
    eval_board.write_register(mc.REG.V1, 50000)
    eval_board.write_register(mc.REG.D1, 500)
    eval_board.write_register(mc.REG.DMAX, 500)
    eval_board.write_register(mc.REG.VSTART, 0)
    eval_board.write_register(mc.REG.VSTOP, 10)
    eval_board.write_register(mc.REG.AMAX, 1000)

    # Set lower run/standby current
    motorCurrent = 2
    motor.set_axis_parameter(motor.AP.MaxCurrent, motorCurrent)
    motor.set_axis_parameter(motor.AP.StandbyCurrent, motorCurrent)

    # Clear actual positions
    motor.actual_position = 0

    print("Rotating...")
    motor.rotate(7 * 25600)
    time.sleep(5)

    print("Stopping...")
    motor.stop()
    time.sleep(1)

    print("Moving back to 0...")
    motor.move_to(0, 7 * 25600)

    # Wait until position 0 is reached
    while motor.actual_position != 0:
        print("Actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Reached position 0")

print("\nReady.")
