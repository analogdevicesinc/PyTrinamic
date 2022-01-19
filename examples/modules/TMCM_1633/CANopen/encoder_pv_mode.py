'''
Move a motor back and forth in PV_Mode for with CANopen using the TMCM1633 module

Created on 07.05.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1633.TMCM_1633 import TMCM_1633

"""
    Choose the right bustype before starting the script
"""

connectionManager = ConnectionManager(" --interface pcan_CANopen", connection_type="CANopen")
network = connectionManager.connect()

node = network.addDs402Node(TMCM_1633.getEdsFile(), 1)
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

#Limit Switches
objSwitchParameter            = module.sdo[0x2005]

#Motor Settings
objMotorPoles                 = module.sdo[0x2010][1]

#Limits
objMaxTorque                  = module.sdo[0x2020][1]
objMaxVelocity                = module.sdo[0x2020][2]
objMaxAcceleration            = module.sdo[0x2020][3]

#Torque Mode Settings
objActualCurrent              = module.sdo[0x2030][1]
objTargetCurrent              = module.sdo[0x2030][2]
objRampTargetCurrent          = module.sdo[0x2030][3]
objTorque_P_Parameter         = module.sdo[0x2030][4]
objTorque_I_Parameter         = module.sdo[0x2030][5]
objPI_Torque_Error            = module.sdo[0x2030][6]
objPI_Torque_Error_Sum        = module.sdo[0x2030][7]
objPI_Flux_Error              = module.sdo[0x2030][8]
objPI_Flux_Error_Sum          = module.sdo[0x2030][9]

#Velocity Mode Settings
objActualVelocity             = module.sdo[0x2040][1]
objTargetVelocity             = module.sdo[0x2040][2]
objRampTargetVelocity         = module.sdo[0x2040][3]
objMotorHaltedVelocity        = module.sdo[0x2040][4]
objVelocity_P_Parameter       = module.sdo[0x2040][5]
objVelocity_I_Parameter       = module.sdo[0x2040][6]
objPI_Velocity_Error          = module.sdo[0x2040][7]
objPI_Velocity_Error_Sum      = module.sdo[0x2040][8]

#Position Mode Settings
objActualPosition             = module.sdo[0x2050][1]
objTargetPosition             = module.sdo[0x2050][2]
objRampTargetPosition         = module.sdo[0x2050][3]
objPosition_P_Parameter       = module.sdo[0x2050][4]
objPI_Position_Error          = module.sdo[0x2050][5]
objTargetReachedVelocity      = module.sdo[0x2050][6]
objTargetReachedDistance      = module.sdo[0x2050][7]

#Commutation Mode
objCommutation_Mode           = module.sdo[0x2055]

#Velocity Ramp Mode
objVelocity_Ramp_Mode         = module.sdo[0x2056]

#Open Loop Settings
objActualAngle                = module.sdo[0x2060][1]
objOpenLoopCurrent            = module.sdo[0x2060][2]

#Hall Sensor Settings
objHall_ActualAngle           = module.sdo[0x2070][1]
objHall_Inversion             = module.sdo[0x2070][2]
objHall_Interpolation         = module.sdo[0x2070][3]

#ABN Encoder Settings
objENC_ActualAngle            = module.sdo[0x2080][1]
objStepsPerRotation           = module.sdo[0x2080][2]
objENC_Offset                 = module.sdo[0x2080][3]
objDirection                  = module.sdo[0x2080][4]
objENC_InitMode               = module.sdo[0x2080][5]
objENC_InitDelay              = module.sdo[0x2080][6]
objENC_InitVelocity           = module.sdo[0x2080][7]

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
    Define all motor configurations for the the TMCM-1633.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not working.
"""

objMotorPoles.raw         = 8
objCommutation_Mode.raw   = 7
objStepsPerRotation.raw   = 16384
objDirection.raw          = 1
objMaxTorque.raw          = 4000

print("MotorPoles:            %d" % objMotorPoles.raw)

print("CommutationMode:       %d" % objCommutation_Mode.raw)
print("ENC_ActualAngle:       %d" % objENC_ActualAngle.raw)
print("StepsPerRotation:      %d" % objStepsPerRotation.raw)
print("ENC_Direction:         %d" % objDirection.raw)

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

startPV()

'''
Configuration Setup for using PV_Mode
'''
# Setup desired_Velocity
objDesiredVelocity.raw = 10000
# Setup Acceleration
objAcceleration.raw = 1000

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

print()
time.sleep(3)

objDesiredVelocity.raw = -10000
print("DesiredVelocity: %d" % objDesiredVelocity.raw)

# Tell the PV mode that it has a new DesiredVelocity
node.controlword = 0x000F
node.controlword = 0x001F

time.sleep(3)

objDesiredVelocity.raw = 0

network.close()
print("disconnected.")
