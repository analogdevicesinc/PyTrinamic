#!/usr/bin/env python3
'''
Move a motor back and forth using the TMCM1260 module

Created on 07.07.2020

@author: JM
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1260.TMCM_1260 import TMCM_1260
import time

PyTrinamic.showInfo()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
Module_1260 = TMCM_1260(myInterface)

DEFAULT_MOTOR = 0

print("Preparing parameters")
Module_1260.setMaxAcceleration(10000)
Module_1260.setMaxCurrent(128)

print("Rotating")
Module_1260.rotate(20000)

time.sleep(5);

print("Stopping")
Module_1260.stop()

time.sleep(1);

print("Rotating back")
Module_1260.rotate(-20000)

time.sleep(5)

print("Stopping")
Module_1260.stop()

print()

myInterface.close()
