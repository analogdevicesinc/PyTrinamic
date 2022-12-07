import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM6214
import time

pytrinamic.show_info()

# This example uses PCAN, if you want to use another connection please change this line.
connectionManager = ConnectionManager("--interface pcan_tmcl")
myInterface = connectionManager.connect()
module = TMCM6214(myInterface)
motor = module.motors[0]

print("Preparing parameters")
motor.max_acceleration = 20000

print("Rotating")
motor.rotate(50000)

time.sleep(5)

print("Stopping")
motor.stop()

print("ActualPostion = {}".format(motor.actual_position))

time.sleep(5)

print("Doubling moved distance")
motor.move_by(motor.actual_position, 50000)
while not(motor.get_position_reached()):
    pass

print("Furthest point reached")
print("ActualPostion = {}".format(motor.actual_position))

time.sleep(5)

print("Moving back to 0")
motor.move_to(0, 100000)

# Wait until position 0 is reached
while not(motor.get_position_reached()):
    pass

print("Reached Position 0")

print()

myInterface.close()
