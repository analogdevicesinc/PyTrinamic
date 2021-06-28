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
Module_1270 = TMCM_1270(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
Module_1270.MOTORS[0].max_acceleration = 9000

print("Rotating")
Module_1270.MOTORS[0].target_velocity = 40000

time.sleep(5)

print("Stopping")
Module_1270.MOTORS[0].target_velocity = 0 #replaced stop

print("ActualPostion") 
print(Module_1270.MOTORS[0].actual_position)
time.sleep(5)

print("Doubling moved distance")
Module_1270.MOTORS[0].move_by(Module_1270.MOTORS[0].actual_position, 50000)
Module_1270.MOTORS[0].actual_position
while not(Module_1270.MOTORS[0].get_position_reached()):
    pass

print("Furthest point reached")
print(Module_1270.MOTORS[0].actual_position)

time.sleep(5)

print("Moving back to 0")
Module_1270.MOTORS[0].move_to(0, 100000)

# Wait until position 0 is reached
while not(Module_1270.MOTORS[0].get_position_reached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
