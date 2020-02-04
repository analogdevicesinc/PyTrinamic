#!/usr/bin/env python3
'''
Turn a motor without feedback

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
module.setAxisParameter(module.APs.CommutationMode, module.ENUMs.COMM_MODE_OPENLOOP);
module.setAxisParameter(module.APs.TargetVelocity, 1000);
time.sleep(5);
module.setAxisParameter(module.APs.TargetVelocity, 0);
time.sleep(5);
module.setAxisParameter(module.APs.CommutationMode, 0);
print("Done")
myInterface.close()
