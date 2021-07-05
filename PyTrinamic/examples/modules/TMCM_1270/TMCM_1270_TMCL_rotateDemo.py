#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1270 module

Created on 03.12.2019

@author: JM
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1270.TMCM_1270 import TMCM_1270
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager("--interface dummy_tmcl") #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()
module = TMCM_1270(myInterface)
motor = module.MOTORS[0]

print("Preparing parameters")
motor.max_acceleration = 9000

print("Rotating")
motor.rotate(40000)

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

myInterface.close()
