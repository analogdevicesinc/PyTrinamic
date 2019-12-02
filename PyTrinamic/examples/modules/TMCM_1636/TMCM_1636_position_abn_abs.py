#!/usr/bin/env python3
'''
Positioning a motor using abn and absolute encoders

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

#config abn encoder
module.setAxisParameter(module.AP_EncoderSteps, 4096);
module.setAxisParameter(module.AP_EncoderDirection, 0);
module.setAxisParameter(module.AP_EncoderInitMode, 0);

#config absolute encoder
module.setAxisParameter(module.AP_AbsoluteEncoderType, 1);
module.setAxisParameter(module.AP_AbsoluteEncoderInit, 0);
module.setAxisParameter(module.AP_AbsoluteEncoderDirection, 1);

#cofig drive mode
module.setAxisParameter(module.AP_CommutationMode, module.COMM_MODE_ABN);
module.setAxisParameter(module.AP_CommutationModePosition, module.POS_MODE_ABS);
time.sleep(1);

#testdrive
module.setAxisParameter(module.AP_ActualPosition, 0);
module.setAxisParameter(module.AP_MaxVelocity, 1000);
module.setAxisParameter(module.AP_Acceleration, 250);
module.setAxisParameter(module.AP_TargetPosition, 10000000);

while not module.axisParameter(module.AP_PositionReachedFlag) :
    time.sleep(0.1);

module.setAxisParameter(module.AP_CommutationMode, 0);
module.setAxisParameter(module.AP_CommutationModePosition, 0);
print("Done")
myInterface.close()
