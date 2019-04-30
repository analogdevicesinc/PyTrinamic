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
myInterface = serial_tmcl_interface('COM9')

" for RS485 connection "
#myInterface = serial_tmcl_interface('COM16', '9600')

module = TMCM_1640(myInterface)

" motor configuration "
module.setMotorPoles(8)
module.setMaxTorque(2000)
module.showMotorConfiguration()

" hall configuration "
module.setHallInvert(0)
module.showHallConfiguration()

" encoder configuration "
module.setOpenLoopTorque(1500)
module.setEncoderResolution(4000)
module.setEncoderDirection(0)
module.setEncoderInitMode(module.ENCODER_INIT_MODE_1)
module.showEncoderConfiguration()

" motion settings "
module.setMaxVelocity(2048)
module.setAcceleration(10000)
module.setRampEnabled(1)
module.setTargetReachedVelocity(500)
module.setTargetReachedDistance(5)
module.showMotionConfiguration()

" PI configuration "
module.setTorquePParameter(600)
module.setTorqueIParameter(600)
module.setVelocityPParameter(800)
module.setVelocityIParameter(600)
module.setPositionPParameter(300)
module.showPIConfiguration()
 
" set commutation mode to FOC based on hall sensor signals "
module.setCommutationMode(module.COMM_MODE_FOC_ENCODER)
 
" read adc value and compute new target velocity "
while True:
    adcValue = module.analogInput(0)
    targetVelocity = (adcValue - 1024) * 2
    module.rotate(targetVelocity)
    print("adc value: " + str(adcValue) + " target velocity: " + str(targetVelocity) + " actual velocity: " + str(module.actualVelocity()))
    time.sleep(0.2)

print("Ready.")
myInterface.close()