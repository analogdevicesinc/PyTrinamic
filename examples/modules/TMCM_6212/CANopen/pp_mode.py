'''
Move a motor back and forth in PP_Mode for with CANopen using the TMCM6212 module

Created on 03.03.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM6212.TMCM_6212 import TMCM_6212

DEFAULT_MOTOR = 0 # Axis: [0;5]

""" 
    Choose the right bustype before starting the script.
    If no connection type is given the default connection type for this script is usb_tmcl.
    For further details look in our ConnectionManager and the connection interfaces.
"""

connectionManager = ConnectionManager(" --interface pcan_CANopen", connection_type="CANopen")
network = connectionManager.connect()

node = network.addDs402Node(TMCM_6212.getEdsFile(), 1, TMCM_6212.MOTORS)
module = node

objSwitchParameters    = []
objModesOfOperation    = []
objActualPositions     = []
objTargetPositions     = []
objAccelerations       = []

for i in range(TMCM_6212.MOTORS):
    objSwitchParameters.append (module.sdo[0x2005 + i*0x0200])
    objModesOfOperation.append (module.sdo[0x6060 + i*0x0800])
    objActualPositions.append  (module.sdo[0x6064 + i*0x0800])
    objTargetPositions.append  (module.sdo[0x607A + i*0x0800])
    objAccelerations.append    (module.sdo[0x6083 + i*0x0800])
    
print("state dump 0:")
for i in range(6):
    print(i, node.states[i])
print()
    
print("state dump 1:")
for i in range(6):
    print(i, node.states[i])
print()

print("######################################")
print(node.states[DEFAULT_MOTOR])
if node.is_faulted():
    print(node.states[DEFAULT_MOTOR])
    if not node.reset_from_fault(DEFAULT_MOTOR): # Reset node from fault and set it to Operation Enable state
        print("Failed to reset fault")
        exit(1)
    print(node.states[DEFAULT_MOTOR])

print("state dump 2:")
for i in range(6):
    print(i, node.states[i])
print()
    
node.states[DEFAULT_MOTOR] = 'SWITCH ON DISABLED'

print("state dump 3:")
for i in range(6):
    print(i, node.states[i])
print()
    

def startPP():

    objSwitchParameters[DEFAULT_MOTOR].raw = 3

    print("state dump 4:")
    for i in range(6):
        print(node.states[i])
    print()
    

    timeout = time.time() + 15
    node.states[DEFAULT_MOTOR] = 'READY TO SWITCH ON'
    while node.states[DEFAULT_MOTOR] != 'READY TO SWITCH ON':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print("state dump 5:")
    for i in range(6):
        print(node.states[i])
    print()
        

    print(node.states[DEFAULT_MOTOR])

    timeout = time.time() + 15
    node.states[DEFAULT_MOTOR] = 'SWITCHED ON'
    while node.states[DEFAULT_MOTOR] != 'SWITCHED ON':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print(node.states[DEFAULT_MOTOR])

    if objModesOfOperation[DEFAULT_MOTOR].raw != 1:
        objModesOfOperation[DEFAULT_MOTOR].raw = 1
        time.sleep(0.1)    
    print("MODE OF OPERATION SET TO: %d" % objModesOfOperation[DEFAULT_MOTOR].raw)

    timeout = time.time() + 15
    node.states[DEFAULT_MOTOR] = 'OPERATION ENABLED'
    while node.states[DEFAULT_MOTOR] != 'OPERATION ENABLED':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print(node.states[DEFAULT_MOTOR])

    return

def positionReached():
    return objActualPositions[DEFAULT_MOTOR].raw == objTargetPositions[DEFAULT_MOTOR].raw

startPP()

'''
Configuration Setup for using PP_Mode
'''
# Setup target_Position
objTargetPositions[DEFAULT_MOTOR].raw = 50000
# Setup Acceleration
objAccelerations[DEFAULT_MOTOR].raw = 20000

print()
print("Configure parameters")
time.sleep(0.2)
print()
print("Target position: %d" % objTargetPositions[DEFAULT_MOTOR].raw)
print("Accelaration: %d" % objAccelerations[DEFAULT_MOTOR].raw)
print()
print("Start PP_Mode...")
time.sleep(0.2)
print()

# Tell the PP mode that it has a new target position
node.controlwords[DEFAULT_MOTOR] = 0x000F
node.controlwords[DEFAULT_MOTOR] = 0x001F

while not positionReached():

    print("Target position: " + str(objTargetPositions[DEFAULT_MOTOR].raw) + " Actual position: " + str(objActualPositions[DEFAULT_MOTOR].raw))
    time.sleep(0.1)

# Set target_Position back to 0
objTargetPositions[DEFAULT_MOTOR].raw = 0
print("Target position: %d" % objTargetPositions[DEFAULT_MOTOR].raw)

# Tell the PP mode that it has a new target position
node.controlwords[DEFAULT_MOTOR] = 0x000F
node.controlwords[DEFAULT_MOTOR] = 0x001F

while not positionReached():
    print("Target position: " + str(objTargetPositions[DEFAULT_MOTOR].raw) + " Actual position: " + str(objActualPositions[DEFAULT_MOTOR].raw))
    time.sleep(0.1)

network.close()
print("disconnected.")
