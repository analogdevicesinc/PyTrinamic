#!/usr/bin/env python3
'''
Move a two motors back and forth using the TMCM3312 module

Created on 15.07.2021

@author: JH
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM3312.TMCM_3312 import TMCM_3312
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager("--interface usb_tmcl") #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()
module = TMCM_3312(myInterface)
motor_0 = module.MOTORS[0]
motor_1 = module.MOTORS[1]
motor_2 = module.MOTORS[2]

print("Preparing parameters")
motor_0.max_acceleration = 20000
motor_1.max_acceleration = 20000

print("Rotating in same direction")
motor_0.rotate(50000)
motor_1.rotate(50000)

time.sleep(5)

print("Stopping")
motor_0.stop()
motor_1.stop()

time.sleep(3)

print("Rotating in opposite direction")
motor_0.rotate(50000)
motor_1.rotate(-50000)

time.sleep(7)

print("Stopping")
motor_0.stop()
motor_1.stop()

time.sleep(3)

print("ActualPostion Axis 0= {}".format(motor_0.actual_position))
print("ActualPostion Axis 1= {}".format(motor_1.actual_position))

print("Doubling moved distance")
motor_0.move_by(motor_0.actual_position, 50000)
motor_1.move_by(motor_1.actual_position, 50000)

while not(motor_0.get_position_reached()) and not(motor_1.get_position_reached()) :
    pass

print("Furthest point reached")
print("ActualPostion Axis 0= {}".format(motor_0.actual_position))
print("ActualPostion Axis 1= {}".format(motor_1.actual_position))

time.sleep(3)

print("Moving back to 0")
motor_0.move_to(0, 100000)
motor_1.move_to(0, 100000)

# Wait until position 0 is reached
while not(motor_0.get_position_reached()) and not(motor_1.get_position_reached()) :
    pass

print("Reached Position 0")

print()

myInterface.close()
