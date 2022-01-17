'''
Move a motor in PP mode with CANopen using the TMCM-1617 module

Created on 09.04.2020

@author: JM, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1617.TMCM_1617 import TMCM_1617
import time

PyTrinamic.show_info()

" choose the right bustype before starting the script "
#connectionManager = ConnectionManager(" --interface pcan_CANopen", connectionType = "CANopen")
connectionManager = ConnectionManager(" --interface kvaser_CANopen", connectionType = "CANopen")
network = connectionManager.connect()

node = network.addDs402Node("TMCM_1617_Hw1.2_Fw1.06.eds", 1)
module = node

" this function initializes the DS402 state machine "
node.setup_402_state_machine()

" communication area "
objManufacturerDeviceName      = module.sdo[0x1008]
objManufacturerHardwareVersion = module.sdo[0x1009]

print("\nModule name:      %s" % objManufacturerDeviceName.raw)
print("Hardware version: %s" % objManufacturerHardwareVersion.raw)

" manufacturer specific area "
objMaximumCurrent             = module.sdo[0x2003]
objOpenloopCurrent            = module.sdo[0x2004]
objSwitchParameter            = module.sdo[0x2005]
objMotorType                  = module.sdo[0x2050]
objCommutationMode            = module.sdo[0x2055]
objMotorPolePairs             = module.sdo[0x2056]

" hall sensor settings "
# objHallPolarity               = module.sdo[0x2070][1]
# objHallDirection              = module.sdo[0x2070][2]
# objHallInterpolation          = module.sdo[0x2070][3]
# objHallPHI_E_offset           = module.sdo[0x2070][4]

" ABN encoder settings "
objEncoderDirection           = module.sdo[0x2080][1]
objEncoderSteps               = module.sdo[0x2080][2]
objEncoderInitMode            = module.sdo[0x2080][3]

" profile specific area "
objModeOfOperation          = module.sdo[0x6060]
objActualPosition           = module.sdo[0x6064]
objTargetPosition           = module.sdo[0x607A]
objAcceleration             = module.sdo[0x6083]

"""
    Define motor configuration for the TMCM-1617.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""
objMotorPolePairs.raw    = 4
objMotorType.raw         = 3 # three phase BLDC
objMaximumCurrent.raw    = 1500
objOpenloopCurrent.raw  = 1500

# objHallDirection.raw     = 0
# objHallPolarity.raw      = 1
# objHallPHI_E_offset.raw  = 0
# objHallInterpolation.raw = 1

objEncoderSteps.raw      = 4096
objEncoderDirection.raw  = 0
objEncoderInitMode.raw   = 0 # 2 # use hall sensor for initialization 

objAcceleration.raw      = 1000
objCommutationMode.raw   = 3 # ABN encoder

print("MotorPoles:               %d" % objMotorPolePairs.raw)
print("CommutationMode:          %d" % objCommutationMode.raw)
# print("HallDirection:            %d" % objHallDirection.raw)
# print("HallPolarity:             %d" % objHallPolarity.raw)
# print("HallPHI_E_offset:         %d" % objHallPHI_E_offset.raw)
# print("HallInterpolation:        %d" % objHallPHI_E_offset.raw)
print("Encoder_StepsPerRotation: %d" % objEncoderSteps.raw)
print("Encoder_Direction:        %d" % objEncoderDirection.raw)
print("Encoder_InitMode:         %d" % objEncoderInitMode.raw)
print()

" reset node from fault and set it to Operation Enable state "
node.reset_from_fault() 

def startPP():

    print("Node state before switcHParameter write:" + node.state)
    objSwitchParameter.raw = 3

    timeout = time.time() + 15
    node.state = 'READY TO SWITCH ON'
    while node.state != 'READY TO SWITCH ON':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print(node.state)

    timeout = time.time() + 15
    node.state = 'SWITCHED ON'
    while node.state != 'SWITCHED ON':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print(node.state)

    if objModeOfOperation.raw != 1:
        objModeOfOperation.raw = 1
    print("MODE OF OPERATION SET TO: %d" % objModeOfOperation.raw)

    timeout = time.time() + 15
    node.state = 'OPERATION ENABLED'
    while node.state != 'OPERATION ENABLED':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print(node.state)

    return

def positionReached():
    return abs(objTargetPosition.raw - objActualPosition.raw) < 100

startPP()

time.sleep(1) # encoder init time

" set target position "
objTargetPosition.raw = objEncoderSteps.raw * 50 # 50 rotations
print("Target position: %d" % objTargetPosition.raw)

" tell the PP mode that it has a new target position "
node.controlword = 0x000F
node.controlword = 0x001F

while not positionReached():
    print("Target position: " + str(objTargetPosition.raw) + " Actual position: " + str(objActualPosition.raw))
    time.sleep(0.1)

" set new target position (back to 0) "
objTargetPosition.raw = 0
print("Target position: %d" % objTargetPosition.raw)

" tell the PP mode that it has a new target position "
node.controlword = 0x000F
node.controlword = 0x001F

while not positionReached():
    print("Target position: " + str(objTargetPosition.raw) + " Actual position: " + str(objActualPosition.raw))
    time.sleep(0.1)

network.close()
print("Ready.")
