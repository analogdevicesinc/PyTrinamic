#!/usr/bin/env python3
'''
Positioning a motor using abn and absolute encoders

Created on 28.11.2019

@author: SW
'''

if __name__ == '__main__':
    pass

import PyTrinamic, time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1636.TMCM_1636 import TMCM_1636

PyTrinamic.showInfo()

#myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

module = TMCM_1636(myInterface)
module.showModuleInfo()
motor = module.motor(0)

"""
    Define motor configuration for the TMCM-1636.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

" config abn encoder "
motor.openLoop.setOpenLoopTorque(1000)
motor.abnEncoder.setResolution(4096)
motor.abnEncoder.setDirection(1)
motor.abnEncoder.setInitMode(motor.ENUM.ENCODER_INIT_MODE_0)
motor.showConfiguration()

" config absolute encoder "
motor.setAxisParameter(motor.AP.AbsoluteEncoderType, 1)
motor.setAxisParameter(motor.AP.AbsoluteEncoderInit, 0)
motor.setAxisParameter(motor.AP.AbsoluteEncoderDirection, 1)

" config drive mode "
motor.setAxisParameter(motor.AP.CommutationMode, motor.ENUM.COMM_MODE_ABN_ENCODER)
motor.setAxisParameter(motor.AP.PositionSensorSelection, motor.ENUM.POS_SELECTION_ABS)
time.sleep(1)

" motion settings "
motor.linearRamp.setMaxVelocity(1000)
motor.linearRamp.setAcceleration(250)
motor.linearRamp.showConfiguration()

" clear actual position "
motor.setActualPosition(0)

" move to new target position "
motor.moveToPosition(1000000)

while not motor.positionReachedFlag():
    print("target position: " + str(motor.targetPosition()) + " actual position: " + str(motor.actualPosition()))
    time.sleep(0.2)

motor.setAxisParameter(motor.AP.CommutationMode, motor.ENUM.COMM_MODE_DISABLED)
motor.setAxisParameter(motor.AP.PositionSensorSelection, motor.ENUM.POS_SELECTION_SAME)

myInterface.close()
print("\nReady.")
