import pytrinamic
from pytrinamic.connections.ConnectionManager import ConnectionManager
from pytrinamic.modules import TMCM1670
import time

pytrinamic.show_info()

# please select your CAN adapter
# myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()

with myInterface:
    module = TMCM1670(myInterface)
    print(module)
    motor = module.motors[0]

    # drive configuration
    motor.drive_settings.poles = 8
    motor.drive_settings.max_current = 2000
    motor.drive_settings.target_reached_velocity = 500
    motor.drive_settings.target_reached_distance = 10
    motor.drive_settings.motor_halted_velocity = 5
    motor.drive_settings.open_loop_current = 1000
    print(motor.drive_settings)

    # encoder configuration
    print(motor.absolute_encoder)

    # motion settings
    motor.linear_ramp.max_velocity = 6000
    motor.linear_ramp.max_acceleration = 2000
    motor.linear_ramp.enabled = 1
    print(motor.linear_ramp)

    # PI configuration
    motor.pid.torque_p = 500
    motor.pid.torque_i = 500
    motor.pid.velocity_p = 1000
    motor.pid.velocity_i = 1000
    motor.pid.position_p = 300
    print(motor.pid)

    time.sleep(1.0)

    # use out_0 output for enable input (directly shortened)
    module.set_digital_output(module.DO.OUT_0)

    # clear actual position
    motor.actual_position = 0

    # move to first position
    motor.move_to(100000)

    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    time.sleep(1.0)

    # move to second position
    motor.move_to(200000)
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)
 
    time.sleep(1.0)

    # move back to start position
    motor.move_to(0)
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)

print("\nReady.")
