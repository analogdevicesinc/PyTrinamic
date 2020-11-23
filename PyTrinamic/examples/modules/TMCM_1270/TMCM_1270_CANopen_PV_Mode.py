'''
Move a motor back and forth in PV_Mode for with CANopen using the TMCM1270 module

Created on 12.02.2020

@author: JM
'''

if __name__ == '__main__':
    pass

import time
from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
from PyTrinamic.modules.TMCM1270.TMCM_1270 import TMCM_1270

"""
    Choose the right bustype before starting the script.
    If no connection type is given the default connection type for this script is usb_tmcl.
    For further details look in our ConnectionManager and the connection interfaces.
"""

network = ConnectionManagerPC(interfaces=["pcan_CANopen"]).connect()[0]

node = network.addDs402Node(TMCM_1270.getEdsFile(), 1)
module = node

#This function initialized the ds402StateMachine
node.setup_402_state_machine()

objSwitchParameter   = module.sdo[0x2005]
objModeOfOperation   = module.sdo[0x6060]
objActualPosition    = module.sdo[0x6064]
objTargetPosition    = module.sdo[0x607A]
objAcceleration      = module.sdo[0x6083]
objActualVelocity    = module.sdo[0x606C]
objDesiredVelocity   = module.sdo[0x60FF]

if node.is_faulted():
    node.reset_from_fault() # Reset node from fault and set it to Operation Enable state

def startPV():

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

# Note: DVR stands for Desired Velocity Reached
def DVR():
    return objActualVelocity.raw == objDesiredVelocity.raw

startPV()

'''
Configuration Setup for using PV_Mode
'''
# Setup desired_Velocity
objDesiredVelocity.raw = 250000
# Setup Acceleration
objAcceleration.raw = 15000

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

while not DVR():
    print("DesiredVelocity: " + str(objDesiredVelocity.raw) + " ActualVelocity: " + str(objActualVelocity.raw))
    time.sleep(0.1)
    if DVR():
        print()
        print("Hold for five seconds DesiredVelocity")
        time.sleep(5)

# Set desired_Velocity back to 0
objDesiredVelocity.raw = 0
print("DesiredVelocity: %d" % objDesiredVelocity.raw)

# Tell the PV mode that it has a new DesiredVelocity
node.controlword = 0x000F
node.controlword = 0x001F

while not DVR():
    print("DesiredVelocity: " + str(objDesiredVelocity.raw) + " ActualVelocity: " + str(objActualVelocity.raw))
    time.sleep(0.1)

network.close()
print("disconnected.")
