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
connectionManager = ConnectionManager("--interface pcan_tmcl".split()) #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()

module = TMCM_1636(myInterface)

"""
    Define all motor configurations for the the TMCM-1633.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

#config abn encoder
module.setAxisParameter(module.APs.EncoderSteps, 4096);
module.setAxisParameter(module.APs.EncoderDirection, 0);
module.setAxisParameter(module.APs.EncoderInitMode, 0);

#config absolute encoder
module.setAxisParameter(module.APs.AbsoluteEncoderType, 1);
module.setAxisParameter(module.APs.AbsoluteEncoderInit, 0);
module.setAxisParameter(module.APs.AbsoluteEncoderDirection, 1);

#cofig drive mode
module.setAxisParameter(module.APs.CommutationMode, module.ENUMs.COMM_MODE_ABN);
module.setAxisParameter(module.APs.CommutationModePosition, module.ENUMs.POS_MODE_ABS);
time.sleep(1);

#testdrive
module.setAxisParameter(module.APs.ActualPosition, 0);
module.setAxisParameter(module.APs.MaxVelocity, 1000);
module.setAxisParameter(module.APs.Acceleration, 250);
module.setAxisParameter(module.APs.TargetPosition, 10000000);

while not module.axisParameter(module.APs.PositionReachedFlag) :
    time.sleep(0.1);

module.setAxisParameter(module.APs.CommutationMode, 0);
module.setAxisParameter(module.APs.CommutationModePosition, 0);
print("Done")
myInterface.close()
