"""
Turn a motor using hall sensors
"""

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.referencedesigns import TMC4671_LEV_REF
import time

PyTrinamic.showInfo()

# please select your CAN adapter
# myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

with myInterface:
    module = TMC4671_LEV_REF(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMC4671-LEV-REF.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.DriveSetting.motor_type = motor.ENUMs.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.DriveSetting.pole_pairs = 4
    motor.DriveSetting.max_current = 2000
    motor.DriveSetting.commutation_mode = motor.ENUMs.COMM_MODE_DIGITAL_HALL
    motor.DriveSetting.target_reached_distance = 5
    motor.DriveSetting.target_reached_velocity = 500
    print(motor.DriveSetting)

    # hall sensor configuration
    motor.DigitalHall.direction = 0
    motor.DigitalHall.polarity = 1
    motor.DigitalHall.offset = 0
    motor.DigitalHall.interpolation = 1
    print(motor.DigitalHall)

    # motion settings
    motor.LinearRamp.max_velocity = 2000
    motor.LinearRamp.max_acceleration = 500
    motor.LinearRamp.enabled = 1
    print(motor.LinearRamp)

    print("Starting motor...")
    motor.rotate(1000)
    time.sleep(3)

    print("Changing motor direction...")
    motor.rotate(-1000)
    time.sleep(6)

    print("Stopping motor...")
    motor.rotate(0)
    time.sleep(3)

    # power of
    motor.DriveSetting.commutation_mode = motor.ENUMs.COMM_MODE_DISABLED

print("\nReady.")
