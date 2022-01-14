import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules import TMCC_160
import time

PyTrinamic.showInfo()

# please select your CAN adapter
# myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

with myInterface:
    module = TMCC_160(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMCC160-EVAL.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.DriveSetting.poles = 8
    motor.DriveSetting.max_current = 2000
    motor.DriveSetting.target_reached_velocity = 500
    motor.DriveSetting.target_reached_distance = 5
    motor.DriveSetting.open_loop_current = 1000

    # encoder configuration
    motor.ABNEncoder.resolution = 4096
    # motor.ABNEncoder.resolution = 16384
    motor.ABNEncoder.direction = 0
    motor.ABNEncoder.init_mode = motor.ENUMs.ENCODER_INIT_MODE_0
    print(motor.ABNEncoder)

    # motion settings
    motor.LinearRamp.max_velocity = 1000
    motor.LinearRamp.max_acceleration = 2000
    motor.LinearRamp.enabled = 1
    print(motor.LinearRamp)

    # PI configuration
    motor.PID.torque_p = 600
    motor.PID.torque_i = 600
    motor.PID.velocity_p = 800
    motor.PID.velocity_i = 500
    motor.PID.position_p = 300
    print(motor.PID)

    time.sleep(1.0)

    # set commutation mode to FOC based on encoder feedback
    motor.DriveSetting.commutation_mode = motor.ENUMs.COMM_MODE_FOC_ENCODER
    print(motor.DriveSetting)

    # clear actual position
    motor.actual_position = 0

    print("move to first position")
    motor.move_to(motor.ABNEncoder.resolution * 50)

    # wait for position reached
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("move back to zero")
    motor.move_to(0)

    # wait for position reached
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

print("\nReady.")
