'''
Move a motor back and forth in PP_Mode for with CANopen using the TMCM1160 module

Created on 27.02.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1160.TMCM_1160 import TMCM_1160

"""
    Choose the right bustype before starting the script.
    If no connection type is given the default connection type for this script is usb_tmcl.
    For further details look in our ConnectionManager and the connection interfaces.
"""

connectionManager = ConnectionManager(" --interface pcan_CANopen", connection_type="CANopen")
network = connectionManager.connect()

node = network.addDs402Node(TMCM_1160.getEdsFile(), 1)
module = node

# This function initialized the ds402StateMachine
node.setup_402_state_machine()

objSwitchParameter    = module.sdo[0x2005]
objModeOfOperation    = module.sdo[0x6060]
objActualPosition     = module.sdo[0x6064]
objTargetPosition     = module.sdo[0x607A]
objAcceleration       = module.sdo[0x6083]

if node.is_faulted():
    node.reset_from_fault() # Reset node from fault and set it to Operation Enable state 

def startPP():

    print("Connecting to Node...")
    time.sleep(0.2)
    print()
    print("Node is booted up and ready to go!")
    time.sleep(0.2)
    print()
    print("Setup ds402_StateMachine: ")
    time.sleep(0.2)
    print()

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
        time.sleep(0.1)
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
    return objActualPosition.raw == objTargetPosition.raw

startPP()

'''
Configuration Setup for using PP_Mode
'''
# Setup target_Position
objTargetPosition.raw = 500000
# Setup Acceleration
objAcceleration.raw = 2000

print()
print("Configure parameters")
time.sleep(0.2)
print()
print("Target position: %d" % objTargetPosition.raw)
print("Accelaration: %d" % objAcceleration.raw)
print()
print("Start PP_Mode...")
time.sleep(0.2)
print()

# Tell the PP mode that it has a new target position
node.controlword = 0x000F
node.controlword = 0x001F

while not positionReached():

    print("Target position: " + str(objTargetPosition.raw) + " Actual position: " + str(objActualPosition.raw))
    time.sleep(0.1)

# Set target_Position back to 0
objTargetPosition.raw = 0
print("Target position: %d" % objTargetPosition.raw)

# Tell the PP mode that it has a new target position
node.controlword = 0x000F
node.controlword = 0x001F

while not positionReached():
    print("Target position: " + str(objTargetPosition.raw) + " Actual position: " + str(objActualPosition.raw))
    time.sleep(0.1)

network.close()
print("disconnected.")
