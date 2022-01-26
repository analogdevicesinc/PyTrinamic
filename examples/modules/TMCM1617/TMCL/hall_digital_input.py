import pytrinamic
from pytrinamic.connections.ConnectionManager import ConnectionManager
from pytrinamic.modules import TMCM1617
import time

pytrinamic.show_info()
# connectionManager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
connectionManager = ConnectionManager("--interface kvaser_tmcl --module-id 1")

with connectionManager.connect() as myInterface: 
    module = TMCM1617(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1617.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
    
    # drive configuration 
    motor.drive_settings.motor_type = motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.drive_settings.pole_pairs = 4
    motor.drive_settings.max_current = 2000
    motor.drive_settings.target_reached_distance = 5
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DIGITAL_HALL
    print(motor.drive_settings)

    # hall sensor configuration 
    motor.digital_hall.direction = 0
    motor.digital_hall.polarity = 1
    motor.digital_hall.offset = 0
    motor.digital_hall.interpolation = 1
    print(motor.digital_hall)

    # motion settings 
    motor.linear_ramp.max_velocity = 2000
    motor.linear_ramp.max_acceleration = 1000
    motor.linear_ramp.enabled = 1 
    print(motor.linear_ramp)

    motor.set_axis_parameter(motor.AP.PositionScaler, 6*motor.drive_settings.pole_pairs)
    # PI configuration 
    motor.pid.torque_p = 300 
    motor.pid.torque_i = 600
    motor.pid.velocity_p = 100
    motor.pid.velocity_i = 100
    motor.pid.position_p = 300
    print(motor.pid)

    # set position counter to zero
    motor.actual_position = 0

    print("\nRotate motor in clockwise direction...")
    motor.rotate(500)

    print("Press 'input_0' to swap the direction (waiting for input_0)")

    # wait for input_0 
    while module.get_digital_input(module.IO.GPI_0) == 1:
        print("actual position: %d   actual velocity: %d" % (motor.actual_position, motor.actual_velocity))
        time.sleep(0.2)

    print("\nRotate motor in counterclockwise direction...")
    motor.rotate(-500)

    print("Press 'input_1' to stop the motor (waiting for input_1)")

    # wait for input_1 
    while module.get_digital_input(module.IO.GPI_1) == 1:
        print("actual position: %d   actual velocity: %d" % (motor.actual_position, motor.actual_velocity))
        time.sleep(0.2)

    # stop motor 
    motor.rotate(0)

print("\nReady.")
