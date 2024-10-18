################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1290
import time

pytrinamic.show_info()

# We are using RS485
connection_manager = ConnectionManager("--interface serial_tmcl --data-rate 115200 --port interactive")

my_interface = connection_manager.connect()
module = TMCM1290(my_interface)
motor = module.motors[0]

print("Preparing parameters")
motor.max_acceleration = 20000

print("Rotating")
motor.rotate(50000)

time.sleep(5)

print("Stopping")
motor.stop()

print("ActualPostion = {}".format(motor.actual_position))

time.sleep(5)

print("Doubling moved distance")
motor.move_by(motor.actual_position, 50000)
while not(motor.get_position_reached()):
    pass

print("Furthest point reached")
print("ActualPostion = {}".format(motor.actual_position))

time.sleep(5)

print("Moving back to 0")
motor.move_to(0, 100000)

# Wait until position 0 is reached
while not(motor.get_position_reached()):
    pass

print("Reached Position 0")

print()

my_interface.close()
