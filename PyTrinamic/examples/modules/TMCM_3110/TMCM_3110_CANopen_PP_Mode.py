'''
Move a motor back and forth in PP_Mode for with CANopen using the TMCM3110 module

Created on 08.06.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.modules.TMCM3110.TMCM_3110 import TMCM_3110

DEFAULT_MOTOR = 0 # Axis: [0;2]

"""
    Choose the right bustype before starting the script.
    If no connection type is given the default connection type for this script is usb_tmcl.
    For further details look in our ConnectionManager and the connection interfaces.
"""

network = ConnectionManagerPC(interfaces=["kvaser_CANopen"]).connect()[0]

node = network.addDs402Node(TMCM_3110.getEdsFile(), 1, TMCM_3110.MOTORS)
module = node

objMicrostepResolution = []
objMaximumCurrent      = []
objSwitchParameters    = []
objModesOfOperation    = []
objActualPositions     = []
objTargetPositions     = []
objAccelerations       = []

for i in range(TMCM_3110.MOTORS):
    objMicrostepResolution.append (module.sdo[0x2000 + i*0x0200])
    objMaximumCurrent.append      (module.sdo[0x2003 + i*0x0200])
    objSwitchParameters.append    (module.sdo[0x2005 + i*0x0200])
    objModesOfOperation.append    (module.sdo[0x6060 + i*0x0800])
    objActualPositions.append     (module.sdo[0x6064 + i*0x0800])
    objTargetPositions.append     (module.sdo[0x607A + i*0x0800])
    objAccelerations.append       (module.sdo[0x6083 + i*0x0800])

# Setup Microstep_Resolution
objMicrostepResolution[DEFAULT_MOTOR].raw = 7
# Setup Maximum_Current
objMaximumCurrent[DEFAULT_MOTOR].raw = 100

#for i in range(3):
#    print(i, node.states[i])
#print()

#print("state dump 1:")
#for i in range(2):
#    print(i, node.states[i])
#print()

print("######################################")
print(node.states[DEFAULT_MOTOR])
if node.is_faulted():
    print(node.states[DEFAULT_MOTOR])
    if not node.reset_from_fault(DEFAULT_MOTOR): # Reset node from fault and set it to Operation Enable state
        print("Failed to reset fault")
        exit(1)
    print(node.states[DEFAULT_MOTOR])

#print("state dump 2:")
#for i in range(3):
#    print(i, node.states[i])
#print()

node.states[DEFAULT_MOTOR] = 'SWITCH ON DISABLED'

#print("state dump 3:")
#for i in range(3):
#    print(i, node.states[i])
#print()

def startPP():

    objSwitchParameters[DEFAULT_MOTOR].raw = 3

#    print("state dump 4:")
#    for i in range(3):
#        print(node.states[i])
#    print()

    timeout = time.time() + 15
    node.states[DEFAULT_MOTOR] = 'READY TO SWITCH ON'
    while node.states[DEFAULT_MOTOR] != 'READY TO SWITCH ON':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

#    print("state dump 5:")
#    for i in range(3):
#        print(node.states[i])
#    print()

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
objTargetPositions[DEFAULT_MOTOR].raw = 150000
# Setup Acceleration
objAccelerations[DEFAULT_MOTOR].raw = 100

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
