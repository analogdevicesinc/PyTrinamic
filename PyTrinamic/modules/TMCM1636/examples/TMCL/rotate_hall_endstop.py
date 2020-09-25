#!/usr/bin/env python3
'''
Turn a motor using hall sensors

Created on 28.11.2019

@author: SW, ED
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1636.TMCM_1636 import TMCM_1636
import time

PyTrinamic.showInfo()

" please select your CAN adapter "
#connectionManager = ConnectionManager("--interface pcan_tmcl")
connectionManager = ConnectionManager("--interface kvaser_tmcl")

myInterface = connectionManager.connect()

module = TMCM_1636(myInterface)

"""
    Define all motor configurations for the TMCM-1636.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" hall sensor config "
module.setAxisParameter(module.APs.HallSensorPolarity, 1);
module.setAxisParameter(module.APs.HallSensorDirection, 0);
module.setAxisParameter(module.APs.HallSensorOffset, 0);
module.setAxisParameter(module.APs.HallInterpolation, 1);

" enable ref switch "
module.setAxisParameter(module.APs.ReferenceSwitchEnable, 3);

" select Hall sensor mode "
module.setAxisParameter(module.APs.CommutationMode, module.ENUMs.COMM_MODE_HALL);

print("Starting motor...")
module.setAxisParameter(module.APs.TargetVelocity, 1000);

print("Waiting for right ref switch...")
while not module.axisParameter(module.APs.RightStopSwitch) :
    time.sleep(0.1);

print("Triggered!")
module.setAxisParameter(module.APs.TargetVelocity, -1000);

print("Waiting for left ref switch...")
while not module.axisParameter(module.APs.LeftStopSwitch) :
    time.sleep(0.1);

print("Triggered!")
print("Stopping motor...")
module.setAxisParameter(module.APs.CommutationMode, 0);

print("Done")
myInterface.close()
