import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules import TMCM_1617
import time

PyTrinamic.show_info()
# connectionManager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
connectionManager = ConnectionManager("--interface kvaser_tmcl --module-id 1")

with connectionManager.connect() as myInterface: 
    module = TMCM_1617(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1617.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration 
    motor.DriveSetting.motor_type = motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.DriveSetting.pole_pairs = 4
    motor.DriveSetting.max_current = 2000
    motor.DriveSetting.commutation_mode = motor.ENUM.COMM_MODE_ABN_ENCODER
    motor.DriveSetting.target_reached_distance = 5
    motor.DriveSetting.target_reached_velocity = 500
    motor.DriveSetting.open_loop_current = 1000 
    print(motor.DriveSetting)

    # encoder configuration 
    motor.ABNEncoder.resolution = 4096
    motor.ABNEncoder.direction = 1
    motor.ABNEncoder.init_mode = motor.ENUM.ENCODER_INIT_MODE_0
    print(motor.ABNEncoder)

    # motion settings 
    motor.LinearRamp.max_velocity = 2000
    motor.LinearRamp.max_acceleration = 1000
    motor.LinearRamp.enabled = 1 
    print(motor.LinearRamp)

    motor.set_axis_parameter(motor.AP.PositionScaler, motor.ABNEncoder.resolution)

    # PI configuration 
    motor.PID.torque_p = 300 
    motor.PID.torque_i = 600
    motor.PID.velocity_p = 100
    motor.PID.velocity_i = 100
    motor.PID.position_p = 300
    print(motor.PID)

    time.sleep(1.0)

    # clear actual position 
    motor.actual_position = 0

    # set target position 
    motor.move_to(motor.ABNEncoder.resolution * 50)
    while not(motor.get_position_reached()):
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    # move back to zero position 
    motor.move_to(0)
    while not(motor.get_position_reached()):
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

print("\nReady.")
