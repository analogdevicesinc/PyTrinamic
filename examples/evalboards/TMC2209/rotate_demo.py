import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards import TMC2209_eval

PyTrinamic.show_info()
myInterface = ConnectionManager().connect()
print(myInterface)

with myInterface:
    # Create TMC2209-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC2209_eval(myInterface)
    motor = eval_board.motors[0]

    print("Rotating...")
    motor.rotate(1*4000)
    time.sleep(2)

    print("Stopping...")
    motor.stop()
    time.sleep(1)

    print("Moving back to 0")
    motor.move_to(0, 2000)

    # Wait until position 0 is reached
    while motor.actual_position != 0:
        print("Actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Reached position 0")

print("\nReady.")
