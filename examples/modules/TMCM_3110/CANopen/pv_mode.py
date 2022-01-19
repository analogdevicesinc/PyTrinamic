'''
Move a motor back and forth in PV_Mode for with CANopen using the TMCM3110 module

Created on 08.06.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM3110.TMCM_3110 import TMCM_3110

DEFAULT_MOTOR = 0 # Axis: [0;2]

"""
    Choose the right bustype before starting the script.
    If no connection type is given the default connection type for this script is usb_tmcl.
    For further details look in our ConnectionManager and the connection interfaces.
"""

connectionManager = ConnectionManager(" --interface kvaser_CANopen", connection_type="CANopen")
network = connectionManager.connect()

node = network.addDs402Node(TMCM_3110.getEdsFile(), 1, TMCM_3110.MOTORS)
module = node

objMicrostepResoultion = []
objMaximumCurrent      = []
objSwitchParameters    = []
objModesOfOperation    = []
objActualPositions     = []
objTargetPositions     = []
objAccelerations       = []
objActualVelocities    = []
objDesiredVelocities   = []

for i in range(TMCM_3110.MOTORS):
    objMicrostepResoultion.append (module.sdo[0x2000 + i*0x0200])
    objMaximumCurrent.append      (module.sdo[0x2003 + i*0x0200])
    objSwitchParameters.append    (module.sdo[0x2005 + i*0x0200])
    objModesOfOperation.append    (module.sdo[0x6060 + i*0x0800])
    objActualPositions.append     (module.sdo[0x6064 + i*0x0800])
    objTargetPositions.append     (module.sdo[0x607A + i*0x0800])
    objAccelerations.append       (module.sdo[0x6083 + i*0x0800])
    objActualVelocities.append    (module.sdo[0x606C + i*0x0800])
    objDesiredVelocities.append   (module.sdo[0x60FF + i*0x0800])

# Setup Microstep_Resolution
objMicrostepResoultion[DEFAULT_MOTOR].raw = 7
# Setup Maximum_Current
objMaximumCurrent[DEFAULT_MOTOR].raw = 100

print("######################################")
if node.is_faulted(DEFAULT_MOTOR):
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

def velocityReached():
    return abs(objActualVelocities[DEFAULT_MOTOR].raw - objDesiredVelocities[DEFAULT_MOTOR].raw) < 10

startPV()

'''
Configuration Setup for using PV_Mode
'''
# Setup desired_Velocity
objDesiredVelocities[DEFAULT_MOTOR].raw = 2000

# Setup Acceleration
objAccelerations[DEFAULT_MOTOR].raw = 30

while not velocityReached():
    print("DesiredVelocity: " + str(objDesiredVelocities[DEFAULT_MOTOR].raw) + " ActualVelocity: " + str(objActualVelocities[DEFAULT_MOTOR].raw))
    time.sleep(0.1)

print()
print("Hold for three seconds DesiredVelocity")
print()
time.sleep(3)

objDesiredVelocities[DEFAULT_MOTOR].raw = 0
print("DesiredVelocity: %d" % objDesiredVelocities[DEFAULT_MOTOR].raw)

while not velocityReached():
    print("DesiredVelocity: " + str(objDesiredVelocities[DEFAULT_MOTOR].raw) + " ActualVelocity: " + str(objActualVelocities[DEFAULT_MOTOR].raw))
    time.sleep(0.1)

network.close()
print("disconnected.")

