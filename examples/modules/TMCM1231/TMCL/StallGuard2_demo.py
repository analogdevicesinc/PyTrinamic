import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1231
import time
import numpy as np

def stallguard2_init(init_velocity):
    motor.stallguard2.set_threshold(0)
    motor.stallguard2.stop_velocity = 0
    print("Rotating...")
    motor.rotate(init_velocity)
    sgthresh = 0
    sgt = 0
    array = []
    while (sgt == 0) and (sgthresh < 64):
        array = []
        motor.stallguard2.set_threshold(sgthresh)
        time.sleep(0.2)
        sgthresh += 1
        for i in range(50):
            array.append(motor.stallguard2.get_load_value())
        print(sgthresh)
        print(array)
        if not np.any(array):
            sgt = 0
        else:
            sgt = np.max(array)
    motor.stallguard2.set_threshold(sgthresh - 1)
    while 1:
        array = []
        for i in range(50):
            array.append(motor.stallguard2.get_load_value())
        print(array)
        if 0 in array:
            motor.drive_settings.max_current = motor.drive_settings.max_current - 1
        else:
            break

    motor.stallguard2.stop_velocity = motor.get_actual_velocity() - 1


pytrinamic.show_info()

# This example is using PCAN, if you want to use another connection please change the next line.
connectionManager = ConnectionManager("--interface pcan_tmcl")
with connectionManager.connect() as myInterface:
    module = TMCM1231(myInterface)
    motor = module.motors[0]


    print("Preparing parameters")
    # preparing drive settings
    motor.drive_settings.max_current = 20
    motor.drive_settings.standby_current = 8
    motor.drive_settings.boost_current = 0
    motor.drive_settings.microstep_resolution = motor.ENUM.microstep_resolution_256_microsteps
    print(motor.drive_settings)

    print(motor.linear_ramp)

    time.sleep(1.0)

    # clear position counter
    motor.actual_position = 0

    # set up StallGuard2
    print("Initial StallGuard2 values:")
    print(motor.stallguard2)
    stallguard2_init(10000)
