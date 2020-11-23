'''
Move a motor back and forth in PV_Mode for with CANopen using the TMCM6212 module

Created on 03.03.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM6212.TMCM_6212 import TMCM_6212

DEFAULT_MOTOR = 1 # Axis: [0;5]

"""
    Choose the right bustype before starting the script.
    If no connection type is given the default connection type for this script is usb_tmcl.
    For further details look in our ConnectionManager and the connection interfaces.
"""

connectionManager = ConnectionManager("--interface pcan_CANopen", connectionType="CANopen")
network = connectionManager.connect()

node = network.addDs402Node(TMCM_6212.getEdsFile(), 1, TMCM_6212.MOTORS)
module = node


objSwitchParameters  = []
objModesOfOperation  = []
objActualPositions   = []
objTargetPositions   = []
objAccelerations     = []
objActualVelocities  = []
objDesiredVelocities = []

for i in range(TMCM_6212.MOTORS):
    objSwitchParameters.append (module.sdo[0x2005 + i*0x0200])
    objModesOfOperation.append (module.sdo[0x6060 + i*0x0800])
    objActualPositions.append  (module.sdo[0x6064 + i*0x0800])
    objTargetPositions.append  (module.sdo[0x607A + i*0x0800])
    objAccelerations.append    (module.sdo[0x6083 + i*0x0800])
    objActualVelocities.append (module.sdo[0x606C + i*0x0800])
    objDesiredVelocities.append(module.sdo[0x60FF + i*0x0800])

print("######################################")
print(node.states[DEFAULT_MOTOR])
if node.is_faulted(DEFAULT_MOTOR):
    print(node.states[DEFAULT_MOTOR])
    print(node.states[DEFAULT_MOTOR])
    print(node.states[DEFAULT_MOTOR])
    print(node.states[DEFAULT_MOTOR])
    print(node.states[DEFAULT_MOTOR])
    print(node.states[DEFAULT_MOTOR])
    print(node.states[DEFAULT_MOTOR])
    print(node.states[DEFAULT_MOTOR])
    print(node.states[DEFAULT_MOTOR])
    print("Resetting fault")
    node.reset_from_fault(DEFAULT_MOTOR) # Reset node from fault and set it to Operation Enable state
    print(node.states[DEFAULT_MOTOR])

node.states[DEFAULT_MOTOR] = 'SWITCH ON DISABLED'

def startPV():

    objSwitchParameters[DEFAULT_MOTOR].raw = 3

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

    if objModesOfOperation[DEFAULT_MOTOR].raw != 3:
        objModesOfOperation[DEFAULT_MOTOR].raw = 3
    print("MODE OF OPERATION SET TO: %d" % objModesOfOperation[DEFAULT_MOTOR].raw)

    timeout = time.time() + 15
    node.state = 'OPERATION ENABLED'
    while node.state != 'OPERATION ENABLED':
        if time.time() > timeout:
            raise Exception('Timeout when trying to change state')
        time.sleep(0.001)

    print(node.state)

    return

# Note: DVR stands for Desired Velocity Reached
def DVR():
    return objActualVelocities[DEFAULT_MOTOR].raw == objDesiredVelocities[DEFAULT_MOTOR].raw

startPV()

'''
Configuration Setup for using PV_Mode
'''
# Setup desired_Velocity
objDesiredVelocities[DEFAULT_MOTOR].raw = 250000
# Setup Acceleration
objAccelerations[DEFAULT_MOTOR].raw = 40000

print()
print("Configure parameters")
time.sleep(0.2)
print()
print("DesiredVelocity: %d" % objDesiredVelocities[DEFAULT_MOTOR].raw)
print("Accelaration: %d" % objAccelerations[DEFAULT_MOTOR].raw)
print()
print("Start PV_Mode...")
time.sleep(0.2)
print()

# Tell the PV mode that it has a new DesiredVelocity
node.controlword = 0x000F
node.controlword = 0x001F

#node.controlwords[DEFAULT_MOTOR] = 0x000F
#node.controlwords[DEFAULT_MOTOR] = 0x001F

while not DVR():
    print("DesiredVelocity: " + str(objDesiredVelocities[DEFAULT_MOTOR].raw) + " ActualVelocity: " + str(objActualVelocities[DEFAULT_MOTOR].raw))
    time.sleep(0.1)
    if DVR():
        print()
        print("Hold for two seconds DesiredVelocity")
        time.sleep(2)

# Set desired_Velocity back to 0
objDesiredVelocities[DEFAULT_MOTOR].raw = 0
print("DesiredVelocity: %d" % objDesiredVelocities[DEFAULT_MOTOR].raw)

# Tell the PV mode that it has a new DesiredVelocity
node.controlword = 0x000F
node.controlword = 0x001F

#node.controlwords[DEFAULT_MOTOR] = 0x000F
#node.controlwords[DEFAULT_MOTOR] = 0x001F

while not DVR():
    print("DesiredVelocity: " + str(objDesiredVelocities[DEFAULT_MOTOR].raw) + " ActualVelocity: " + str(objActualVelocities[DEFAULT_MOTOR].raw))
    time.sleep(0.1)

network.close()
print("disconnected.")
