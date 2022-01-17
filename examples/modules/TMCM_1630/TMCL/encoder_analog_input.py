import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules import TMCM_1630
import time

PyTrinamic.show_info()

# please select a CAN or USB interface

# CAN
# myInterface = ConnectionManager("--interface pcan_tmcl").connect()
# myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

# USB
myInterface = ConnectionManager().connect()

with myInterface:
    module = TMCM_1630(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1630.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.DriveSetting.poles = 8
    motor.DriveSetting.max_current = 2000
    motor.DriveSetting.target_reached_velocity = 500
    motor.DriveSetting.target_reached_distance = 5

    # hall sensor configuration
    motor.DigitalHall.polarity = 0
    motor.DigitalHall.interpolation = 0
    print(motor.DigitalHall)

    # encoder configuration
    motor.ABNEncoder.resolution = 4096
    motor.ABNEncoder.direction = 1
    motor.ABNEncoder.init_mode = motor.ENUM.ENCODER_INIT_MODE_1
    print(motor.ABNEncoder)

    # motion settings
    motor.LinearRamp.max_velocity = 2048
    motor.LinearRamp.max_acceleration = 10000
    motor.LinearRamp.enabled = 1
    print(motor.LinearRamp)

    # PI configuration
    motor.PID.torque_p = 600
    motor.PID.torque_i = 600
    motor.PID.velocity_p = 800
    motor.PID.velocity_i = 600
    motor.PID.position_p = 300
    print(motor.PID)

    time.sleep(1.0)

    # set commutation mode to FOC based on encoder feedback
    motor.DriveSetting.commutation_mode = motor.ENUM.COMM_MODE_FOC_ENCODER
    print(motor.DriveSetting)

    # read adc value and compute new target velocity
    while True:
        adcValue = module.get_analog_input(0)
        targetVelocity = (adcValue - 1024) * 2
        motor.rotate(targetVelocity)
        print("adc value: " + str(adcValue) + " target velocity: " + str(targetVelocity)
              + " actual velocity: " + str(motor.actual_velocity))
        time.sleep(0.2)
