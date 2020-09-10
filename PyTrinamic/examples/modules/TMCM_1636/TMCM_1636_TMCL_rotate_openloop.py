#!/usr/bin/env python3
'''
Turn a motor without feedback in open loop mode

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
    Define all motor configurations for the the TMCM-1636.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" select open loop mode "
module.setAxisParameter(module.APs.CommutationMode, module.ENUMs.COMM_MODE_OPENLOOP);

print("Starting motor...")
module.setAxisParameter(module.APs.TargetVelocity, 1000);
time.sleep(3);

print("Stopping motor...")
module.setAxisParameter(module.APs.TargetVelocity, 0);
time.sleep(3);

" power of "
module.setAxisParameter(module.APs.CommutationMode, 0);

print("Done")
myInterface.close()
