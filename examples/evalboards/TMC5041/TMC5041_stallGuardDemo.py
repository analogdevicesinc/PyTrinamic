################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

#!/usr/bin/env python3
'''
Demonstrate usage of StallGuard2 homing with the TMC5041

This script uses two motors for a simple demonstration of Stallguard2-based
homing. One motor is rotated until a stall is detected. Once a stall has been
detected the other motor moves to the position where the first motor has
stalled. This process is repeated indefinitely. Optionally the direction of the
rotation can change after each stall to allow moving back and forth between two
objects the motor collides with when rotating.

Created on 29.04.2019

@author: LH
'''

import time
import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.evalboards.TMC5041_eval import TMC5041_eval

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

TMC5041 = TMC5041_eval(my_interface)
TMC5041.showChipInfo()

### Configuration
print("Configuring")

# Reset position references to 0
TMC5041.writeRegisterField(TMC5041.fields.XACTUAL[0], 0)
TMC5041.writeRegisterField(TMC5041.fields.XACTUAL[1], 0)
TMC5041.writeRegisterField(TMC5041.fields.XTARGET[MOTOR_FOLLOWING], 0)

## Configure leading motor for stallguard homing
# Stall guard threshold
TMC5041.writeRegisterField(TMC5041.fields.SGT[MOTOR_LEADING], SG_THRESHOLD)
# Set stall guard minimum velocity
TMC5041.writeRegisterField(TMC5041.fields.VCOOLTHRS[MOTOR_LEADING], SG_VELOCITY)
# Enable Stall guard
TMC5041.writeRegisterField(TMC5041.fields.SG_STOP[MOTOR_LEADING], 1)

## Configure following motor for position ramping
TMC5041.writeRegister(TMC5041.registers.V1[MOTOR_FOLLOWING], 0)
TMC5041.writeRegister(TMC5041.registers.A1[MOTOR_FOLLOWING], 100)
TMC5041.writeRegister(TMC5041.registers.D1[MOTOR_FOLLOWING], 100)
TMC5041.writeRegister(TMC5041.registers.VSTART[MOTOR_FOLLOWING], 0)
TMC5041.writeRegister(TMC5041.registers.VSTOP[MOTOR_FOLLOWING], 10)
TMC5041.writeRegister(TMC5041.registers.AMAX[MOTOR_FOLLOWING], ACCELERATION)
TMC5041.writeRegister(TMC5041.registers.DMAX[MOTOR_FOLLOWING], ACCELERATION)

### Demo #######################################################################

# Direction of the rotation represented as [-1, 1]
# Multiply with the velocity constant to get the target velocity
direction = 1

try:
    while True:
        print("")
        print("Motor " + str(MOTOR_LEADING) + " Rotating")
        TMC5041.rotate(MOTOR_LEADING, direction * VELOCITY)

        print("Motor " + str(MOTOR_LEADING) + " waiting for a stall")
        # Wait until the leading motor is stalled
        while TMC5041.readRegisterField(TMC5041.fields.EVENT_STOP_SG[MOTOR_LEADING]) == 0:
            pass

        # Stop leading motor once a stall has occured
        TMC5041.stop(MOTOR_LEADING)

        print("Motor " + str(MOTOR_LEADING) + " stalled")

        time.sleep(DELAY)

        # Let the other motor follow
        print("Motor " + str(MOTOR_FOLLOWING) + " following")
        target = TMC5041.readRegisterField(TMC5041.fields.XACTUAL[MOTOR_LEADING])
        TMC5041.moveTo(MOTOR_FOLLOWING, target, VELOCITY)

        # Wait until the other motor reached the target
        while TMC5041.readRegisterField(TMC5041.fields.POSITION_REACHED[MOTOR_FOLLOWING]) == 0:
            pass

        print("Motor " + str(MOTOR_FOLLOWING) + " caught up")

        time.sleep(DELAY)

        if CHANGE_DIR:
            # Flip the direction around
            direction = -direction
except KeyboardInterrupt:
    print("")

print("Stopping motors")
# Stop the motors
TMC5041.stop(0)
TMC5041.stop(1)

# Wait until the motors are standing still
while TMC5041.readRegisterField(TMC5041.fields.VACTUAL[0]) != 0 and TMC5041.readRegisterField(TMC5041.fields.VACTUAL[1]) != 0:
    pass

# Clear any remaining stalls
TMC5041.readRegisterField(TMC5041.fields.EVENT_STOP_SG[MOTOR_LEADING])

my_interface.close()