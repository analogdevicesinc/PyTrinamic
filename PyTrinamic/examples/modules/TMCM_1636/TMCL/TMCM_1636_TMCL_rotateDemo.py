#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1636 module

Created on 13.07.2021

@author: JH
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1636.TMCM_1636 import TMCM_1636
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
myInterface = connectionManager.connect()
module = TMCM_1636(myInterface)
motor = module.MOTORS[0]

print("Preparing parameters")
" motor configuration for three phase bldc"
motor.DriveSetting.motor_type = motor.ENUMs.MOTOR_TYPE_THREE_PHASE_BLDC
motor.DriveSetting.pole_pairs = 4
motor.DriveSetting.max_current= 2000
motor.DriveSetting.commutation_mode = motor.ENUMs.COMM_MODE_OPENLOOP
motor.DriveSetting.position_sensor = motor.ENUMs.POS_SELECTION_SAME
motor.DriveSetting.velocity_sensor = motor.ENUMs.VEL_SELECTION_SAME
print(motor.DriveSetting.__str__())

"Set sensors to open loop mode"
motor.max_acceleration = 1000
motor.max_velocity = 1000

print("Rotating")
motor.rotate(1000)

time.sleep(5)

print("Stopping")
motor.stop()

print("ActualPostion = {}".format(motor.actual_position))

time.sleep(2)

print("Doubling moved distance")
motor.move_by(motor.actual_position, 1000000)
while not(motor.get_position_reached()):
    print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
    time.sleep(0.2)

print("Furthest point reached")
print("ActualPostion = {}".format(motor.actual_position))

time.sleep(2)

print("Moving back to 0")
motor.move_to(0)

# Wait until position 0 is reached
while not(motor.get_position_reached()):
    print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
    time.sleep(0.2)

print("Reached Position 0")

print()

myInterface.close()
