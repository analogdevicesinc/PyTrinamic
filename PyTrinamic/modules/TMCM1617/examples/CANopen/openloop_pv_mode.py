'''
Move a motor in PV mode with CANopen using the TMCM-1617 module

Created on 09.04.2020

@author: JM, ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1617.TMCM_1617 import TMCM_1617
import time

PyTrinamic.showInfo()

" choose the right bustype before starting the script "
#connectionManager = ConnectionManager(" --interface pcan_CANopen", connectionType = "CANopen")
connectionManager = ConnectionManager(" --interface kvaser_CANopen", connectionType = "CANopen")
network = connectionManager.connect()

node = network.addDs402Node(TMCM_1617.getEdsFile(), 1)
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

" profile specific area "
objModeOfOperation            = module.sdo[0x6060]
objAcceleration               = module.sdo[0x6083]
objActualVelocity             = module.sdo[0x606C]
objTargetVelocity             = module.sdo[0x60FF]

"""
    Define all motor configurations for the TMCM-1617.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""
objMotorPolePairs.raw   = 4
objMotorType.raw        = 3 # three phase BLDC
objOpenloopCurrent.raw  = 1000
objMaximumCurrent.raw   = 1500
objCommutationMode.raw  = 1 # open loop mode
objMotorType.raw        = 3 # three phase BLDC
objAcceleration.raw     = 200

print("MotorPolePairs:   %d" % objMotorPolePairs.raw)
print("CommutationMode:  %d" % objCommutationMode.raw)
print()

" reset node from fault and set it to Operation Enable state "
node.reset_from_fault() 

def startPV():
 
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

    if objModeOfOperation.raw != 3:
        objModeOfOperation.raw = 3
    print("MODE OF OPERATION SET TO: %d" % objModeOfOperation.raw)

    timeout = time.time() + 15
    node.state = 'OPERATION ENABLED'
    while node.state != 'OPERATION ENABLED':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print(node.state)

    return

def velocityReached():
    return abs(objActualVelocity.raw - objTargetVelocity.raw) < 10

startPV()

" set target velocity "
objTargetVelocity.raw = 1000

while not velocityReached():
    print("DesiredVelocity: " + str(objTargetVelocity.raw) + " ActualVelocity: " + str(objActualVelocity.raw))
    time.sleep(0.1)

print("\nHold desired velocity for three seconds\n")
time.sleep(3)

" stop motor "
objTargetVelocity.raw = 0

while not velocityReached():
    print("DesiredVelocity: " + str(objTargetVelocity.raw) + " ActualVelocity: " + str(objActualVelocity.raw))
    time.sleep(0.1)

network.close()
print("Ready.")
