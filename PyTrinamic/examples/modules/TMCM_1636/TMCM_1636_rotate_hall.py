#!/usr/bin/env python3
'''
Turn a motor using hall sensors

Created on 28.11.2019

@author: SW
'''

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM_1636 import TMCM_1636
import time

PyTrinamic.showInfo()
connectionManager = ConnectionManager("--interface pcan_tmcl".split()) #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()

module = TMCM_1636(myInterface)

"""
    Define all motor configurations for the the TMCM-1633.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

#config hall
module.setAxisParameter(module.APs.HallSensorPolarity, 1);
module.setAxisParameter(module.APs.HallSensorDirection, 1);
module.setAxisParameter(module.APs.HallInterpolation, 1);
module.setAxisParameter(module.APs.HallSensorOffset, 22000);

#testdrive
module.setAxisParameter(module.APs.CommutationMode, module.ENUMs.COMM_MODE_HALL);
module.setAxisParameter(module.APs.TargetVelocity, 1000);
time.sleep(5);
module.setAxisParameter(module.APs.TargetVelocity, 0);
time.sleep(1);
module.setAxisParameter(module.APs.CommutationMode, 0);
print("Done")
myInterface.close()
