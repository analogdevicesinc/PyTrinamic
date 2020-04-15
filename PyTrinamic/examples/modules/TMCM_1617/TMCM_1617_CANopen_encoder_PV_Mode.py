'''
Move a motor back and forth in PV_Mode for with CANopen using the TMCM1617 module

Created on 09.04.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1617.TMCM_1617 import TMCM_1617

"""
    Choose the right bustype before starting the script
"""

connectionManager = ConnectionManager(" --interface pcan_CANopen", connectionType = "CANopen")
network = connectionManager.connect()

node = network.addDs402Node(TMCM_1617.getEdsFile(), 1)
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

objOpenloopCurrent            = module.sdo[0x2004]

#Limit Switches
objSwitchParameter            = module.sdo[0x2005]

#Torque Mode Settings
objTorque_P                   = module.sdo[0x2041][1]
objTorque_I                   = module.sdo[0x2041][2]
objPID_Torque_Error           = module.sdo[0x2041][3]
objPID_Torque_Error_Sum       = module.sdo[0x2041][4]
objPID_Flux_Error             = module.sdo[0x2041][5]
objPID_Flux_Error_Sum         = module.sdo[0x2041][6]
objPHI_E                      = module.sdo[0x2041][7]

#Velocity Mode Settings
objP_Parameter                = module.sdo[0x2042][1]
objI_Parameter                = module.sdo[0x2042][2]
objPI_Velocity_Error          = module.sdo[0x2042][3]
objPI_Velocity_Error_Sum      = module.sdo[0x2042][4]

#Position Mode Settings
objP_Parameter                = module.sdo[0x2043][1]
objPID_Position_Error         = module.sdo[0x2043][2]

#Motor Type
objMotorType                  = module.sdo[0x2050]

#Commutation Mode
objCommutationMode            = module.sdo[0x2055]

#Motor Pole Pairs
objMotorPolePairs             = module.sdo[0x2056]

#Hall Sensor Settings
objHallPolarity               = module.sdo[0x2070][1]
objHallDirection              = module.sdo[0x2070][2]
objHallInterpolation          = module.sdo[0x2070][3]
objHallPHI_E_offset           = module.sdo[0x2070][4]

#ABN Encoder Settings
objEncoderDirection           = module.sdo[0x2080][1]
objEncoderSteps               = module.sdo[0x2080][2]
objEncoderInitMode            = module.sdo[0x2080][3]

#Motor Status Flags
objDeviceState                = module.sdo[0x2101]
objOpenloopAngle              = module.sdo[0x2102]
objEncoderCommutationAngle    = module.sdo[0x2103]
objHallCommutationAngle       = module.sdo[0x2104]


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

"""
    Define all motor configurations for the the TMCM-1617.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

objMotorPolePairs.raw          = 4
objCommutationMode.raw         = 3
objOpenloopCurrent.raw         = 500
objEncoderSteps.raw            = 16384
objEncoderDirection.raw        = 1

print("##############################")
print("MotorPoles:                %d" % objMotorPolePairs.raw)
print("Commutation Mode:          %d" % objCommutationMode.raw)
print("Encoder Steps:             %d" % objEncoderSteps.raw)
print("Encoder Direction:         %d" % objEncoderDirection.raw)
print("Encoder InitMode:          %d" % objEncoderInitMode.raw)
print("##############################")
print("startPV-Mode...")
time.sleep(2)

if node.is_faulted():
    print("Resetting fault")
    node.reset_from_fault() # Reset node from fault and set it to Operation Enable state 

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
    return objActualVelocity.raw == objDesiredVelocity.raw

startPV()

'''
Configuration Setup for using PV_Mode
'''
# Setup desired_Velocity
objDesiredVelocity.raw = 1000
# Setup Acceleration
objAcceleration.raw = 200

print()
print("Configure parameters")
time.sleep(0.2)
print()
print("DesiredVelocity: %d" % objDesiredVelocity.raw)
print("Accelaration: %d" % objAcceleration.raw)
print()
print("Start PV_Mode...")
time.sleep(0.2)
print()

# Tell the PV mode that it has a new DesiredVelocity
node.controlword = 0x000F
node.controlword = 0x001F

while not velocityReached():
    print("DesiredVelocity: " + str(objDesiredVelocity.raw) + " ActualVelocity: " + str(objActualVelocity.raw))
    time.sleep(0.1)
    
print()
print("Hold for five seconds DesiredVelocity")
time.sleep(5)

objDesiredVelocity.raw = 0
print("DesiredVelocity: %d" % objDesiredVelocity.raw)

# Tell the PV mode that it has a new DesiredVelocity
node.controlword = 0x000F
node.controlword = 0x001F

while not velocityReached():
    print("DesiredVelocity: " + str(objDesiredVelocity.raw) + " ActualVelocity: " + str(objActualVelocity.raw))
    time.sleep(0.1)

network.close()
print("disconnected.")
