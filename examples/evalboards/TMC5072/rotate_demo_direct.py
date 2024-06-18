################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Move a motor back and forth using velocity and position mode of the TMC5072
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5072_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create TMC5062-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5072_eval(my_interface)
    mc = eval_board.ics[0]
    ic = eval_board.ics[0]
    motor0 = ic.motors[0]
    print(motor0)
    motor1 = ic.motors[1]
    print(motor1)

    print("Preparing parameter for motor 0...")

    motor0.write_axis_field(ic.FIELD.A1, 1000)
    motor0.write_axis_field(ic.FIELD.V1, 50000)
    motor0.write_axis_field(ic.FIELD.D1, 500)
    motor0.write_axis_field(ic.FIELD.DMAX, 500)
    motor0.write_axis_field(ic.FIELD.VSTART, 0)
    motor0.write_axis_field(ic.FIELD.VSTOP, 10)
    motor0.write_axis_field(ic.FIELD.AMAX, 1000)

    motor1.write_axis_field(ic.FIELD.A1, 1000)
    motor1.write_axis_field(ic.FIELD.V1, 50000)
    motor1.write_axis_field(ic.FIELD.D1, 500)
    motor1.write_axis_field(ic.FIELD.DMAX, 500)
    motor1.write_axis_field(ic.FIELD.VSTART, 0)
    motor1.write_axis_field(ic.FIELD.VSTOP, 10)
    motor1.write_axis_field(ic.FIELD.AMAX, 1000)

    # Clear actual positions
    motor0.actual_position = 0
    motor1.actual_position = 0

    print(f"M0: target position: {motor0.target_position}  actual position: {motor0.actual_position}")
    print(f"M1: target position: {motor1.target_position}  actual position: {motor1.actual_position}")

    print("Rotating motor 0...")
    motor0.rotate(10*25600)

    startTime = time.time()
    while (time.time() - startTime) <= 3.0:
        print(f"Target velocity: {motor0.target_velocity}  actual velocity: {motor0.actual_velocity}")
        time.sleep(0.3)

    print("Stopping motor 0...")
    motor0.stop()
    time.sleep(1)

    print("Rotating motor 1...")
    motor1.rotate(10*25600)

    startTime = time.time()
    while (time.time() - startTime) <= 3.0:
        print(f"Target velocity: {motor1.target_velocity}  actual velocity: {motor1.actual_velocity}")
        time.sleep(0.3)

    print("Stopping motor 1...")
    motor1.stop()
    time.sleep(1)

    print("\nMoving to new positions with move_to...")
    motor0.move_to(50000, 100000)
    motor1.move_to(80000, 80000)

    # Wait until position 0 is reached by both motors
    while (motor0.actual_position != motor0.target_position) or (motor1.actual_position != motor1.target_position):
        print(f"M0: target position: {motor0.target_position}  actual position: {motor0.actual_position}")
        print(f"M1: target position: {motor1.target_position}  actual position: {motor1.actual_position}")
        time.sleep(0.3)

    print("Reached target positions")

    for i in range(3):
        print("\nMoving to new positions with move_by...")
        motor0.move_by(100000)
        motor1.move_by(200000)

        # waiting for position reached
        while (motor0.actual_position != motor0.target_position) or (motor1.actual_position != motor1.target_position):
            print(f"M0: target position: {motor0.target_position}  actual position: {motor0.actual_position}")
            print(f"M1: target position: {motor1.target_position}  actual position: {motor1.actual_position}")
            time.sleep(0.3)

        # new position reached
        print("\nTarget positions reached:")
        print(f"M0: target position: {motor0.target_position}  actual position: {motor0.actual_position}")
        print(f"M1: target position: {motor1.target_position}  actual position: {motor1.actual_position}")
        time.sleep(2)

print("\nReady.")
