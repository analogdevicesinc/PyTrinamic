import pytrinamic
from pytrinamic.connections.ConnectionManager import ConnectionManager
from pytrinamic.modules import TMCM1640
import time

pytrinamic.show_info()
myInterface = ConnectionManager().connect()
print(myInterface)

with myInterface:
    module = TMCM1640(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1640.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.drive_settings.poles = 8
    motor.drive_settings.max_current = 2000
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_FOC_HALL
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.target_reached_distance = 5
    motor.drive_settings.motor_halted_velocity = 5
    print(motor.drive_settings)

    # hall sensor configuration
    motor.digital_hall.polarity = 0
    motor.digital_hall.interpolation = 0
    print(motor.digital_hall)

    # motion settings
    motor.linear_ramp.max_velocity = 1000
    motor.linear_ramp.max_acceleration = 2000
    motor.linear_ramp.enabled = 1
    print(motor.linear_ramp)

    # PI configuration
    motor.pid.torque_p = 600
    motor.pid.torque_i = 600
    motor.pid.velocity_p = 800
    motor.pid.velocity_i = 500
    motor.pid.position_p = 300
    print(motor.pid)

    time.sleep(1.0)

    # clear actual position
    motor.actual_position = 0

    print("move to first position")
    motor.move_to(motor.drive_settings.poles * 3 * 50)

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
