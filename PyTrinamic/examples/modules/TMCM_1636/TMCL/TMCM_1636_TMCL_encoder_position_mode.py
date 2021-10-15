#!/usr/bin/env python3
'''
Created on 12.04.2021

@author: JM, ED, JH
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
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
motor.BLDCMotor.type = motor.ENUMs.MOTOR_TYPE_THREE_PHASE_BLDC
motor.BLDCMotor.pole_pairs = 4
motor.BLDCMotor.max_torque = 2000
print(motor.BLDCMotor.__str__())

" encoder configuration "
motor.OpenLoop.open_loop_torque = 1000 
motor.ABNEncoder.resolution = 4096
motor.ABNEncoder.direction = 1
motor.ABNEncoder.init_mode =motor.ENUMs.ENCODER_INIT_MODE_0
print(motor.ABNEncoder.__str__())

" motion settings "
motor.LinearRamp.max_velocity = 2000
motor.LinearRamp.max_acceleration = 1000
motor.LinearRamp.enabled = 1 
motor.LinearRamp.target_reached_distance = 5
motor.LinearRamp.target_reached_velocity = 500
print(motor.LinearRamp.__str__())

motor.set_axis_parameter(motor.APs.PositionScaler, motor.ABNEncoder.resolution)
" PI configuration "
motor.PID.torque_p = 300 
motor.PID.torque_i = 600
motor.PID.velocity_p = 100
motor.PID.velocity_i = 100
motor.PID.position_p = 300
print(motor.PID.__str__())

" set commutation mode to FOC based on hall sensor signals "
motor.CommutationSelection.mode = motor.ENUMs.COMM_MODE_ABN_ENCODER
print(motor.CommutationSelection.__str__())

time.sleep(1.0)

" clear actual position "
motor.actual_position = 0

" set target position "
motor.move_to(motor.ABNEncoder.resolution * 50)
while not(motor.get_position_reached()):
    print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
    time.sleep(0.2)

" move back to zero position "
motor.move_to(0)
while not(motor.get_position_reached()):
    print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
    time.sleep(0.2)

myInterface.close()
print("\nReady.")
