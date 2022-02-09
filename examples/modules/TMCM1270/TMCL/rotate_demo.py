import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.modules.TMCM1270 import TMCM1270
import time

pytrinamic.show_info()

connectionManager = ConnectionManager("--interface pcan_tmcl") #This setting is configurated for PCAN , if you want to use another Connection please change this line
myInterface = connectionManager.connect()
module = TMCM1270(myInterface)
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
