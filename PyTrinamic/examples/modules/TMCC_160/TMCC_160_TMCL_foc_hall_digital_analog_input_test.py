#!/usr/bin/env python3
'''
Created on 04.02.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCC160.TMCC_160 import TMCC_160

PyTrinamic.showInfo()
connectionManager = ConnectionManager("--interface pcan_tmcl".split()) #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()

module = TMCC_160(myInterface)

"""
    Define all motor configurations for the the TMCC-160.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

" motor/module settings "
module.setMotorPoles(4)
module.setMaxTorque(2000)
module.showMotorConfiguration()

" hall configuration "
module.setHallInvert(0)
module.showHallConfiguration()

" encoder settings "
module.setOpenLoopTorque(1500)
module.setEncoderResolution(4096)
module.setEncoderDirection(0)
module.setEncoderInitMode(module.ENUMs.ENCODER_INIT_MODE_1)
module.showEncoderConfiguration()

" motion settings "
module.setMaxVelocity(4000)
module.setAcceleration(2000)
module.setRampEnabled(1)
module.setTargetReachedVelocity(1000)
module.setTargetReachedDistance(5)
module.showMotionConfiguration()

" current PID values "
module.setTorquePParameter(600)
module.setTorqueIParameter(600)

" velocity PID values "
module.setVelocityPParameter(800)
module.setVelocityIParameter(500)

" position PID values "
module.setPositionPParameter(300)
module.showPIConfiguration()

" set commutation mode to FOC based on hall sensor signals "
module.setCommutationMode(module.ENUMs.COMM_MODE_FOC_ENCODER)

" set position counter to zero"
module.setActualPosition(0)

" move to zero position"
module.moveToPosition(0)

module.rotate(500)

print()
print("Current direction: rotate forward")
print("Press 'input_0' to swap the direction (waiting for input_0)")

" wait for input_0 "
while (module.digitalInput(0) == 1):
#    print("actual position: " + str(module.actualPosition())) # Activated this line if you want constantly actualPosition updates
#    time.sleep(0.2)
    pass
module.rotate(-500)

print()
print("Current direction: rotate backwards")
print("Press 'input_1' to stop the digital_input_test (waiting for input_1)")

" wait for input_1 "
while (module.digitalInput(1) == 1):
#    print("actual position: " + str(module.actualPosition())) # Activated this line if you want constantly actualPosition updates
#    time.sleep(0.2)
    pass

module.rotate(0)
print()
print("Ready.")
myInterface.close()