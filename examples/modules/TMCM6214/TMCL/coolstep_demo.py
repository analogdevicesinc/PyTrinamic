"""
Sets the CoolStep parameters such that the current increases/decreases if the SG value lies
below or above the SG_min or SG_max threshold values.
Works with Stepper motor type: MS17HD4P4150
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM6214
import time

pytrinamic.show_info()
connection_manager = ConnectionManager()

with connection_manager.connect() as my_interface:
    module = TMCM6214(my_interface)
    motor_0 = module.motors[0]

    print("Preparing parameters")
    # preparing drive settings
    motor_0.drive_settings.max_current = 64
    motor_0.drive_settings.standby_current = 8
    motor_0.drive_settings.microstep_resolution = motor_0.ENUM.MicrostepResolution256Microsteps

    # preparing Stallguard2 settings
    motor_0.stallguard2.set_threshold(2)
    motor_0.stallguard2.stop_velocity = 0
    motor_0.set_axis_parameter(motor_0.AP.SG2FilterEnable, 1)

    # preparing Coolstep settings
    motor_0.set_axis_parameter(motor_0.AP.SEIMIN, 0)
    motor_0.set_axis_parameter(motor_0.AP.SECDS, 1)
    motor_0.set_axis_parameter(motor_0.AP.SECUS, 1)
    motor_0.set_axis_parameter(motor_0.AP.SmartEnergyHysteresis, 0)
    motor_0.set_axis_parameter(motor_0.AP.SmartEnergyHysteresisStart, 7)
    motor_0.set_axis_parameter(motor_0.AP.SmartEnergyThresholdSpeed, 30)

    print("Rotating")
    motor_0.rotate(40000)
    
    while 1:
        print("Smart Energy Actual Current: {current}" .format(current=motor_0.get_axis_parameter(motor_0.AP.SmartEnergyActualCurrent) * 8))
        time.sleep(0.1)

    





