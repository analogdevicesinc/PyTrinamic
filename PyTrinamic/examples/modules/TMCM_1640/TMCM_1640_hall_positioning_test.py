'''
Created on 30.12.2018

@author: ED
'''

if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.modules.TMCM_1640 import TMCM_1640

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts(Serial=True)

" for usb connection "
#myInterface = serial_tmcl_interface('COM9')

" for RS485 connection "
myInterface = serial_tmcl_interface('COM16', '9600')

module = TMCM_1640(myInterface)

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
module.setCommutationMode(module.COMM_MODE_FOC_HALL)

" set position counter to zero"
module.setActualPosition(0) 

" move to zero position"
module.moveToPosition(0)

print("starting positioning")

module.moveToPosition(4000)

" wait for position reached "
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)

module.moveToPosition(0)

" wait for position reached "
while not module.positionReached():
    print("target position: " + str(module.targetPosition()) + " actual position: " + str(module.actualPosition()))
    time.sleep(0.2)

print("Ready.")
myInterface.close()