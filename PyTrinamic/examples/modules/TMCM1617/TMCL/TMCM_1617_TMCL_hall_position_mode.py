#!/usr/bin/env python3
'''
Created on 12.04.2021

@author: JM, ED, JH 
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1617.TMCM_1617 import TMCM_1617
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
myInterface = connectionManager.connect()
module = TMCM_1617(myInterface)
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
motor.BLDCMotor.__str__()

" hall sensor configuration "
motor.DigitalHallWeasel.direction = 0
motor.DigitalHallWeasel.polarity = 1
motor.DigitalHallWeasel.offset = 0
motor.DigitalHallWeasel.interpolation = 1
motor.DigitalHallWeasel.__str__()

" motion settings "
motor.LinearRamp.max_velocity = 2000
motor.LinearRamp.max_acceleration = 1000
motor.LinearRamp.enabled = 1 
motor.LinearRamp.target_reached_distance = 5
motor.LinearRamp.target_reached_velocity = 500
motor.LinearRamp.__str__()

motor.set_axis_parameter(motor.APs.PositionScaler, 6*motor.BLDCMotor.pole_pairs)
" PI configuration "
motor.PID.torque_p = 300 
motor.PID.torque_i = 600
motor.PID.velocity_p = 100
motor.PID.velocity_i = 100
motor.PID.position_p = 300
motor.PID.__str__()

" set commutation mode to FOC based on hall sensor signals "
motor.CommutationSelection.mode = motor.ENUMs.COMM_MODE_DIGITAL_HALL
motor.CommutationSelection.__str__()

" set position counter to zero"
motor.actual_position = 0

" move to zero position"
motor.move_to(0)

print("starting positioning")
motor.move_to(4000)

" wait for position reached "
while not(motor.get_position_reached()):
    print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
    time.sleep(0.2)

" move back to zero"
motor.move_to(0)

" wait for position reached "
while not(motor.get_position_reached()):
    print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
    time.sleep(0.2)

myInterface.close()
print("\nReady.")
