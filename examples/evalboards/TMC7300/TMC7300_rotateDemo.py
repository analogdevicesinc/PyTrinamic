#!/usr/bin/env python3
'''
Move a DC motor back and forth using the TMC7300

Created on 30.03.2020

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC7300_eval import TMC7300_eval

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

PyTrinamic.show_info()

TMC7300 = TMC7300_eval(myInterface)
TMC7300.showChipInfo()

DEFAULT_MOTOR = 0

TMC7300.ICStandby(DEFAULT_MOTOR, 0)

PWM_DUTY_CYCLE = 30

print("Rotating")
TMC7300.setAxisParameter(TMC7300.APs.PWMDutyA, DEFAULT_MOTOR, 50)

time.sleep(2)

print("Stopping")
TMC7300.setAxisParameter(TMC7300.APs.PWMDutyA, DEFAULT_MOTOR, 0)

time.sleep(1)

print("Rotating")
TMC7300.setAxisParameter(TMC7300.APs.PWMDutyA, DEFAULT_MOTOR, -50)

time.sleep(2)

print("Stopping")
TMC7300.setAxisParameter(TMC7300.APs.PWMDutyA, DEFAULT_MOTOR, 0)

time.sleep(1)

myInterface.close()
