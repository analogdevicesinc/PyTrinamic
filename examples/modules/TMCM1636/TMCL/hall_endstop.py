import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.modules import TMCM1636
import time

pytrinamic.show_info()
# connectionManager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
connectionManager = ConnectionManager("--interface kvaser_tmcl --module-id 1")

with connectionManager.connect() as myInterface: 
    module = TMCM1636(myInterface)
    motor = module.motors[0]

    # Define motor configuration for the TMCM-1636.
    #
    # The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    # If you use a different motor be sure you have the right configuration setup otherwise the script may not work.

    # drive configuration
    motor.drive_settings.motor_type = motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC
    motor.drive_settings.pole_pairs = 4
    motor.drive_settings.max_current = 2000
    motor.drive_settings.commutation_mode = motor.ENUM.COMM_MODE_DIGITAL_HALL
    print(motor.drive_settings)

    # hall sensor configuration
    motor.digital_hall.direction = 0
    motor.digital_hall.polarity = 1
    motor.digital_hall.offset = 0
    motor.digital_hall.interpolation = 1
    print(motor.digital_hall)

    # enable ref switch 
    motor.set_axis_parameter(motor.AP.ReferenceSwitchEnable, 3)
    motor.set_axis_parameter(motor.AP.ReferenceSwitchPolarity, 0)

    print("\nRotate motor in clockwise direction...")
    motor.rotate(500)

    print("Waiting for right ref switch...")
    while not motor.get_axis_parameter(motor.AP.RightStopSwitch):
        time.sleep(0.1)

    print("Triggered!")
    motor.rotate(-500)

    print("Waiting for left ref switch...")
    while not motor.get_axis_parameter(motor.AP.LeftStopSwitch):
        time.sleep(0.1)

    print("Triggered!")
    print("Stopping motor...")
    motor.rotate(0)

print("\nReady.")
