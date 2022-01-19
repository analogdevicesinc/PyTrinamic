import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules import TMCM_1240
import time

PyTrinamic.show_info()
myInterface = ConnectionManager().connect()
print(myInterface)

with myInterface:
    module = TMCM_1240(myInterface)
    motor = module.motors[0]

    # drive configuration
    motor.drive_settings.max_current = 50
    print(motor.drive_settings)

    # motion settings
    motor.linear_ramp.max_velocity = 20000
    motor.linear_ramp.max_acceleration = 40000
    print(motor.linear_ramp)

    time.sleep(1.0)

    # set move_by relative to the actual position
    motor.set_axis_parameter(motor.AP.RelativePositioningOption, 1)

    # clear position counter
    motor.actual_position = 0

    print("Rotating...")
    motor.rotate(20000)
    time.sleep(5)

    print("Stopping...")
    motor.stop()
    time.sleep(1)

    print("Double moved distance.")
    motor.move_by(motor.actual_position, 10000)

    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + "   actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Furthest point reached.")
    time.sleep(3)

    print("Moving back to 0...")
    motor.move_to(0, 20000)

    # wait until position 0 is reached
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + "   actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Reached position 0.")

    myInterface.close()

print("\nReady.")
