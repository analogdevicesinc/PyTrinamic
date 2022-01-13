import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM1670.TMCM_1670 import TMCM_1670
import time

PyTrinamic.showInfo()

# please select your CAN adapter
# myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect() 

with myInterface:
    module = TMCM_1670(myInterface, 1)
    motor = module.motors[0]

    # drive configuration
    motor.DriveSetting.poles = 8
    motor.DriveSetting.max_current = 2000
    motor.DriveSetting.target_reached_velocity = 500
    motor.DriveSetting.target_reached_distance = 10
    motor.DriveSetting.motor_halted_velocity = 5
    motor.DriveSetting.open_loop_current = 1000
    print(motor.DriveSetting)

    # encoder configuration
    print(motor.AbsoluteEncoder)

    # motion settings
    motor.LinearRamp.max_velocity = 4000
    motor.LinearRamp.max_acceleration = 4000
    motor.LinearRamp.enabled = 1
    print(motor.LinearRamp)

    # PI configuration
    motor.PID.torque_p = 1000
    motor.PID.torque_i = 1000
    motor.PID.velocity_p = 2000
    motor.PID.velocity_i = 1000
    motor.PID.position_p = 300
    print(motor.PID)

    time.sleep(1.0)

    # use out_0 output for enable input (directly shortened)
    module.set_digital_output(module.DOs.OUT_0)

    # sync actual position with encoder N-Channel
    motor.actual_position = 0
    motor.rotate(200)
    time.sleep(0.5)
    motor.set_axis_parameter(motor.APs.ClearOnce, 1)
    motor.set_axis_parameter(motor.APs.ClearOnNull, 1)
    time.sleep(0.5)
 
    # move to zero position which is now located at the N-Channel
    motor.move_to(0)
    while not motor.get_position_reached():
        print("target position: " + str(motor.target_position) + " actual position: " + str(motor.actual_position))
        time.sleep(0.2)
 
print("\nReady.")
