'''
Move a motor back and forth in HM_Mode for with CANopen using the TMCM1636 module

Created on 15.05.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1636.TMCM_1636 import TMCM_1636

"""
    Choose the right bustype before starting the script
"""

connectionManager = ConnectionManager(" --interface kvaser_CANopen", connectionType = "CANopen")
network = connectionManager.connect()

node = network.addDs402Node(TMCM_1636.getEdsFile(), 1)
module = node

#This function initialized the ds402StateMachine
node.setup_402_state_machine()

#####################
#Communication area
objManufacturerDeviceName      = module.sdo[0x1008]
objManufacturerHardwareVersion = module.sdo[0x1009]

print()
print("Module name: %s"        % objManufacturerDeviceName.raw)
print("Hardware version: %s"   % objManufacturerHardwareVersion.raw)

######################
#Manufacturer specific area

#Current
objMaximumCurrent             = module.sdo[0x2003]

#Limit Switches
objSwitchParameter            = module.sdo[0x2005]

#Position Mode Settings
objP_Parameter                = module.sdo[0x2043][1]
objPID_Position_Error         = module.sdo[0x2043][2]
objAlwaysUseEncoder           = module.sdo[0x2043][3]

#Commutation Mode
objCommutationMode            = module.sdo[0x2055]

#Motor Pole Pairs
objMotorPolePairs             = module.sdo[0x2056]

#ABN Encoder Settings
objEncoderDirection           = module.sdo[0x2080][1]
objEncoderSteps               = module.sdo[0x2080][2]
objEncoderInitMode            = module.sdo[0x2080][3]

#Digital Inputs
objDeviceDigitalInputs        = module.sdo[0x2702]

######################
#Profile specific area

objControlWord              = module.sdo[0x6040]
objStatusWord               = module.sdo[0x6041]
objModeOfOperation          = module.sdo[0x6060]
objActualPosition           = module.sdo[0x6064]
objTargetTorque             = module.sdo[0x6071]
objTargetPosition           = module.sdo[0x607A]
objAcceleration             = module.sdo[0x6083]
objActualVelocity           = module.sdo[0x606C]
objDesiredVelocity          = module.sdo[0x60FF]
objVelocityActualValue      = module.sdo[0x606C]
objHomingMethod             = module.sdo[0x6098]
objHomingSpeedFast          = module.sdo[0x6099][1]
objHomingSpeedsSlow         = module.sdo[0x6099][2]
objHomingAcceleration       = module.sdo[0x609A]

"""
    Define all motor configurations for the TMCM-1636.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""



objMotorPolePairs.raw              = 4
objMaximumCurrent.raw              = 1500
objCommutationMode.raw             = 3
objEncoderSteps.raw                = 16384
objEncoderDirection.raw            = 1

print("MotorPoles:               %d" % objMotorPolePairs.raw)
print("CommutationMode:          %d" % objCommutationMode.raw)
print("Encoder_StepsPerRotation: %d" % objEncoderSteps.raw)
print("Encoder_Direction:        %d" % objEncoderDirection.raw)
print()

'''
Configuration Setup for using HM_Mode
'''

# Setup Homing Method
objHomingMethod.raw = 17 #(Homing on negative Limit Switch)
# Setup Homing Speed
objHomingSpeedFast.raw = 1000
objHomingSpeedsSlow.raw = 500
# Setup Homing Acceleration
objHomingAcceleration.raw = 500

if node.is_faulted():
    print("Resetting fault")
    node.reset_from_fault() # Reset node from fault and set it to Operation Enable state

def startHM():

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

    if objModeOfOperation.raw != 6:
        objModeOfOperation.raw = 6
    print("MODE OF OPERATION SET TO: %d" % objModeOfOperation.raw)

    timeout = time.time() + 15
    node.state = 'OPERATION ENABLED'
    while node.state != 'OPERATION ENABLED':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print(node.state)

    return

def HM_RUN():
    return (objStatusWord.raw & (1 << 10)) != 0

startHM()

while not HM_RUN():
    print("Homing...")
    time.sleep(0.4)

network.close()
print("disconnected.")
