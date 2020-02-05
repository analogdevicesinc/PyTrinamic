#!/usr/bin/env python3
'''
Created on 04.02.2020

@author: JM
'''

if __name__ == '__main__':
    pass

#import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM_1617 import TMCM_1617

PyTrinamic.showInfo()
connectionManager = ConnectionManager("--interface pcan_tmcl".split()) #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()

module = TMCM_1617(myInterface)

" motor configuration "
module.setMotorPoles(4)
module.setMaxTorque(2000)
module.setMotorType(3)
module.showMotorConfiguration()

" hall configuration "
#module.setHallInvert(0)
module.showHallConfiguration()

" motion settings "
module.setMaxVelocity(400)
module.setAcceleration(200)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(5)
module.setPositionScalerM(2048)
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