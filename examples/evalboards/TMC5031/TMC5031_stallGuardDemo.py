###############################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""
Demonstrate usage of StallGuard2 homing with the TMC5031

This script uses two motors for a simple demonstration of Stallguard2-based
homing. One motor is rotated until a stall is detected. Once a stall has been
detected the other motor moves to the position where the first motor has
stalled. This process is repeated indefinitely. Optionally the direction of the
rotation can change after each stall to allow moving back and forth between two
objects the motor collides with when rotating.
"""

import time
import keyboard
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5031_eval


def stallGuardDemo_stall_test(my_motor, direction):
    ### Demo #######################################################################
    # Direction of the rotation represented as [-1, 1]
    # Multiply with the velocity constant to get the target velocity

    global DELAY
    global VELOCITY
    global CHANGE_DIR

    sg_stop_dic = {0:mc.FIELD.SG_STOP_M1, 1:mc.FIELD.SG_STOP_M2}
    event_step_sg_dic = {0:mc.FIELD.EVENT_STOP_SG_M1, 1:mc.FIELD.EVENT_STOP_SG_M2}
    #while True:
    eval_board.write_register_field(sg_stop_dic[my_motor], 0)
    print("\nMotor " + str(my_motor) + " speed up:")
    eval_board.rotate(my_motor, direction * VELOCITY)
    time.sleep(DELAY)  # wait for motor to start up
    # Enable Stall guard
    eval_board.write_register_field(sg_stop_dic[my_motor], 1)
    print("Motor " + str(my_motor) + " Rotating")

    print("Motor " + str(my_motor) + " waiting for a stall")
    # Wait until the leading motor is stalled
    while eval_board.read_register_field(event_step_sg_dic[my_motor]) == 0:
        time.sleep(0.1)

    # Stop motor once a stall has occured
    eval_board.stop(my_motor)

    print("Motor " + str(my_motor) + " stalled was detected. Motor was disabled.")

    time.sleep(DELAY)

    if CHANGE_DIR:
        # Flip the direction around
        return -direction



connection_manager = ConnectionManager()
my_interface = connection_manager.connect()

### Parameters #################################################################

# Motor selection (select different ones for each entry)
MOTOR_LEADING   = 0
MOTOR_FOLLOWING = 1

VELOCITY     = 100000
ACCELERATION = 1000
SG_VELOCITY  = 50000

SG_THRESHOLD = 6
#SG_THRESHOLD = 9

# Delay between Demo steps
DELAY        = 1
# En/Disable switching direction after each stall
CHANGE_DIR   = True
################################################################################

pytrinamic.show_info()

# Initialization

TMC5031 = TMC5031_eval(my_interface)
eval_board = TMC5031_eval(my_interface)
mc = eval_board.ics[0]

### Configuration
print("Configuring")

# Reset position references to 0
eval_board.write_register_field(mc.FIELD.XACTUAL_M1, 0)
eval_board.write_register_field(mc.FIELD.XACTUAL_M2, 0)
eval_board.write_register_field(mc.FIELD.XTARGET_M1, 0)
eval_board.write_register_field(mc.FIELD.XTARGET_M2, 0)

# Set run current
eval_board.write_register_field(mc.FIELD.IRUN_M1, 13)
eval_board.write_register_field(mc.FIELD.IRUN_M2, 13)

## Configure leading motor for stallguard homing
# Stall guard threshold
eval_board.write_register_field(mc.FIELD.SGT_M1, SG_THRESHOLD)
eval_board.write_register_field(mc.FIELD.SGT_M2, SG_THRESHOLD)
# Set stall guard minimum velocity
eval_board.write_register_field(mc.FIELD.VCOOLTHRS_M1, SG_VELOCITY)
eval_board.write_register_field(mc.FIELD.VCOOLTHRS_M2, SG_VELOCITY)
# disenable Stall guard (so that the motor is not stalling at the startup)
eval_board.write_register_field(mc.FIELD.SG_STOP_M1, 0)
eval_board.write_register_field(mc.FIELD.SG_STOP_M2, 0)

## Configure following motor for position ramping
eval_board.write_register(mc.REG.V1[MOTOR_LEADING], 0)
eval_board.write_register(mc.REG.A1[MOTOR_LEADING], 100)
eval_board.write_register(mc.REG.D1[MOTOR_LEADING], 100)
eval_board.write_register(mc.REG.VSTART[MOTOR_LEADING], 0)
eval_board.write_register(mc.REG.VSTOP[MOTOR_LEADING], 10)
eval_board.write_register(mc.REG.AMAX[MOTOR_LEADING], ACCELERATION)
eval_board.write_register(mc.REG.DMAX[MOTOR_LEADING], ACCELERATION)

eval_board.write_register(mc.REG.V1[MOTOR_FOLLOWING], 0)
eval_board.write_register(mc.REG.A1[MOTOR_FOLLOWING], 100)
eval_board.write_register(mc.REG.D1[MOTOR_FOLLOWING], 100)
eval_board.write_register(mc.REG.VSTART[MOTOR_FOLLOWING], 0)
eval_board.write_register(mc.REG.VSTOP[MOTOR_FOLLOWING], 10)
eval_board.write_register(mc.REG.AMAX[MOTOR_FOLLOWING], ACCELERATION)
eval_board.write_register(mc.REG.DMAX[MOTOR_FOLLOWING], ACCELERATION)

# Start the test. Alternating for each motor
direction_M1 = 1
direction_M2 = 1
while True:
    direction_M1 = stallGuardDemo_stall_test(MOTOR_LEADING, direction_M1)
    direction_M2 = stallGuardDemo_stall_test(MOTOR_FOLLOWING,  direction_M2)
    print("Press a key. Press 'q' for quiting:")
    if keyboard.read_key() == "q":
        break



print("\nStopping motors")
# Stop the motors
eval_board.stop(0)
eval_board.stop(1)

time.sleep(1)

# Clear any remaining stalls
eval_board.write_register_field(mc.FIELD.SG_STOP_M1, 0)
eval_board.write_register_field(mc.FIELD.SG_STOP_M2, 0)

my_interface.close()
