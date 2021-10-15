#!/usr/bin/env python3
'''
Positioning a motor using abn and absolute encoders

Created on 28.11.2019

@author: SW, JH
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1636.TMCM_1636 import TMCM_1636
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
myInterface = connectionManager.connect()
module = TMCM_1636(myInterface)
motor = module.MOTORS[0]

"""
    Define motor configuration for the TMCM-1636.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

" config open loop torque"
motor.OpenLoop.torque = 1000
motor.OpenLoop.__str__()

" config abn encoder "
motor.ABNEncoder.resolution  = 4096
motor.ABNEncoder.direction = 1
motor.ABNEncoder.init_mode = motor.ENUMs.ENCODER_INIT_MODE_0
motor.ABNEncoder.__str__()

" config absolute encoder "
motor.AbsoluteEncoder.type = 1
motor.AbsoluteEncoder.init_mode = 0
motor.AbsoluteEncoder.direction = 1
motor.AbsoluteEncoder.offset = 0
motor.AbsoluteEncoder.__str__()

" config drive mode "
motor.CommutationSelection.mode = motor.ENUMs.COMM_MODE_ABN_ENCODER
motor.CommutationSelection.__str__()
motor.PID.position_sensor = motor.ENUMs.POS_SELECTION_ABS
time.sleep(1)

" motion settings "
motor.LinearRamp.max_velocity = 1000
motor.LinearRamp.max_acceleration = 250
motor.LinearRamp.__str__()

" clear actual position "
motor.LinearRamp.actual_position = 0

" move to new target position "
motor.move_to(1000000)

while not motor.get_position_reached():
    print("target position: " + str(motor.LinearRamp.target_position) + " actual position: " + str(motor.LinearRamp.actual_position))
    time.sleep(0.2)

motor.CommutationSelection.mode = motor.ENUMs.COMM_MODE_DISABLED
motor.PID.position_sensor = motor.ENUMs.POS_SELECTION_SAME

myInterface.close()
print("\nReady.")
