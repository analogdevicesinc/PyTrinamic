'''
Created on 29.04.2019

@author: LH
'''

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.evalboards.TMC5041_eval import TMC5041_eval
import time

### Parameters #################################################################

# Motor selection (select different ones for each entry)
MOTOR_LEADING   = 0
MOTOR_FOLLOWING = 1

VELOCITY     = 100000
ACCELERATION = 1000
SG_VELOCITY  = 50000

SG_THRESHOLD = 6
#SG_THRESHOLD = 9

# Delay between Demo steps
DELAY        = 1
# En/Disable switching direction after each stall
CHANGE_DIR   = True
################################################################################

PyTrinamic.showInfo()

# Initialization

myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))
TMC5041 = TMC5041_eval(myInterface)

### Configuration
print("Configuring")

# Reset position references to 0
TMC5041.writeRegisterField(TMC5041.fields.XACTUAL[0], 0)
TMC5041.writeRegisterField(TMC5041.fields.XACTUAL[1], 0)
TMC5041.writeRegisterField(TMC5041.fields.XTARGET[MOTOR_FOLLOWING], 0)

## Configure leading motor for stallguard homing
# Stall guard threshold
TMC5041.writeRegisterField(TMC5041.fields.SGT[MOTOR_LEADING], SG_THRESHOLD)
# Set stall guard minimum velocity
TMC5041.writeRegisterField(TMC5041.fields.VCOOLTHRS[MOTOR_LEADING], SG_VELOCITY)
# Enable Stall guard
TMC5041.writeRegisterField(TMC5041.fields.SG_STOP[MOTOR_LEADING], 1);

## Configure following motor for position ramping
TMC5041.writeRegister(TMC5041.registers.V1[MOTOR_FOLLOWING], 0)
TMC5041.writeRegister(TMC5041.registers.A1[MOTOR_FOLLOWING], 100)
TMC5041.writeRegister(TMC5041.registers.D1[MOTOR_FOLLOWING], 100)
TMC5041.writeRegister(TMC5041.registers.VSTART[MOTOR_FOLLOWING], 0)
TMC5041.writeRegister(TMC5041.registers.VSTOP[MOTOR_FOLLOWING], 10)
TMC5041.writeRegister(TMC5041.registers.AMAX[MOTOR_FOLLOWING], ACCELERATION)
TMC5041.writeRegister(TMC5041.registers.DMAX[MOTOR_FOLLOWING], ACCELERATION)

### Demo #######################################################################

# Direction of the rotation represented as [-1, 1]
# Multiply with the velocity constant to get the target velocity
direction = 1

while True:
    print("")
    print("Motor " + str(MOTOR_LEADING) + " Rotating")
    TMC5041.rotate(MOTOR_LEADING, direction * VELOCITY)
    
    
    print("Motor " + str(MOTOR_LEADING) + " waiting for a stall")
    # Wait until the leading motor is stalled
    while TMC5041.readRegisterField(TMC5041.fields.EVENT_STOP_SG[MOTOR_LEADING]) == 0:
        pass
                
    # Stop leading motor once a stall has occured
    TMC5041.stop(MOTOR_LEADING)

    print("Motor " + str(MOTOR_LEADING) + " stalled")
    
    time.sleep(DELAY)
    
    # Let the other motor follow
    print("Motor " + str(MOTOR_FOLLOWING) + " following")
    target = TMC5041.readRegisterField(TMC5041.fields.XACTUAL[MOTOR_LEADING])
    TMC5041.moveTo(MOTOR_FOLLOWING, target, VELOCITY);
    
    # Wait until the other motor reached the target
    while TMC5041.readRegisterField(TMC5041.fields.POSITION_REACHED[MOTOR_FOLLOWING]) == 0:
        pass
    
    print("Motor " + str(MOTOR_FOLLOWING) + " caught up")
    
    time.sleep(DELAY)
    
    if CHANGE_DIR:
        # Flip the direction around
        direction = -direction    
    
myInterface.close()