#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1240 module

Created on 21.09.2020

@author: AA
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1240.TMCM_1240 import TMCM_1240
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
Module_1240 = TMCM_1240(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
Module_1240.setMaxAcceleration(10000)
Module_1240.setMaxCurrent(128)

print("Rotating")
Module_1240.rotate(20000)

time.sleep(5);

print("Stopping")
Module_1240.stop()

time.sleep(1);

print("Rotating back")
Module_1240.rotate(-20000)

time.sleep(5)

print("Stopping")
Module_1240.stop()

print()

myInterface.close()
