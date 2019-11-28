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
module.setAxisParameter(module.AP_HallSensorDirection, 0);
module.setAxisParameter(module.AP_HallInterpolation, 1);
module.setAxisParameter(module.AP_HallSensorOffset, 22000);

#enable ref switch
module.setAxisParameter(module.AP_ReferenceSwitchEnable, 1);


#testdrive
module.setAxisParameter(module.AP_CommutationMode, module.COMM_MODE_HALL);
module.setAxisParameter(module.AP_TargetVelocity, 1000);

print("Wait for right ref switch")
while not module.axisParameter(module.AP_RightStopSwitch) :
    time.sleep(0.1);

print("Triggered!")
time.sleep(3);
module.setAxisParameter(module.AP_TargetVelocity, -1000);

print("Wait for left ref switch")
while not module.axisParameter(module.AP_LeftStopSwitch) :
    time.sleep(0.1);


print("Triggered!")
module.setAxisParameter(module.AP_CommutationMode, 0);
print("Done")
myInterface.close()
