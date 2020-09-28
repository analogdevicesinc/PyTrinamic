#!/usr/bin/env python3
'''
Created on 31.01.2020

@author: JM, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1633.TMCM_1633 import TMCM_1633

PyTrinamic.showInfo()

" please select your CAN adapter "
#connectionManager = ConnectionManager("--interface pcan_tmcl")
connectionManager = ConnectionManager("--interface kvaser_tmcl")
myInterface = connectionManager.connect()

module = TMCM_1633(myInterface)

"""
    Define motor configuration for the TMCM-1633.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
module.setMotorPoles(8)
module.setMaxTorque(2000)
module.showMotorConfiguration()

" hall configuration "
module.setHallInvert(0)
module.showHallConfiguration()

" motion settings "
module.setMaxVelocity(1000)
module.setAcceleration(2000)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(5)
module.showMotionConfiguration()

" PI configuration "
module.setTorquePParameter(600)
module.setTorqueIParameter(600)
module.setVelocityPParameter(800)
module.setVelocityIParameter(500)
module.setPositionPParameter(300)
module.showPIConfiguration()

" set commutation mode to FOC based on hall sensor signals "
module.setCommutationMode(module.ENUMs.COMM_MODE_FOC_HALL)

module.rotate(500)
print("\nCurrent direction: rotate forward")
print("Press 'input_0' to swap the direction (waiting for input_0)")

" wait for input_0 "
while (module.digitalInput(0) == 1):
#     print("actual position: " + str(module.actualPosition()))
#     time.sleep(0.2)
    pass

module.rotate(-500)
print("\nCurrent direction: rotate backwards")
print("Press 'input_1' to stop the motor (waiting for input_1)")

" wait for input_1 "
while (module.digitalInput(1) == 1):
#     print("actual position: " + str(module.actualPosition()))
#     time.sleep(0.2)
    pass

" stop motor"
module.rotate(0)

myInterface.close()
print("Ready.")