import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1276
import time

pytrinamic.show_info()

# This example is using PCAN, if you want to use another connection please change the next line.
connectionManager = ConnectionManager("--interface pcan_tmcl")

with connectionManager.connect() as myInterface:
    module = TMCM1276(myInterface)
    motor = module.motors[0]

    print("Preparing parameters")
    # preparing linear ramp settings
    motor.max_acceleration = 20000

    while 1:
        if motor.get_axis_parameter(motor.AP.RightEndstop):
            motor.stop()
            time.sleep(5)
            print("Rotating in opposite direction")
            motor.rotate(-50000)
            time.sleep(5)
            motor.stop()
            break
        else:
            print("Rotating")
            motor.rotate(50000)
            time.sleep(5)

