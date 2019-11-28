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
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()

module = TMCM_1636(myInterface)

#config hall
module.setAxisParameter(module.AP_HallSensorPolarity, 1);
module.setAxisParameter(module.AP_HallSensorDirection, 1);
module.setAxisParameter(module.AP_HallInterpolation, 1);
module.setAxisParameter(module.AP_HallSensorOffset, 22000);

#testdrive
module.setAxisParameter(module.AP_CommutationMode, module.COMM_MODE_HALL);
module.setAxisParameter(module.AP_TargetVelocity, 1000);
time.sleep(5);
module.setAxisParameter(module.AP_TargetVelocity, 0);
time.sleep(1);
module.setAxisParameter(module.AP_CommutationMode, 0);
print("Done")
myInterface.close()
