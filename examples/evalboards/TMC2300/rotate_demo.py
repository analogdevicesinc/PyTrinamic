"""
Move a motor back and forth using velocity and position mode of the TMC2300.
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC2300_eval

pytrinamic.show_info()
myInterface = ConnectionManager().connect()
print(myInterface)

with myInterface:
    # Create TMC2300-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC2300_eval(myInterface)
    motor = eval_board.motors[0]

    motor.set_ic_standby(0)
    motor.set_microstep_resolution(256)

    print("Rotating...")
    motor.rotate(10*25600)
    time.sleep(2)

    print("Stopping...")
    motor.stop()
    time.sleep(1)

    print("Moving back to 0...")
    motor.move_to(0, 10*25600)
 
    # Wait until position 0 is reached
    while motor.actual_position != 0:
        print("Actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Reached position 0")

print("\nReady.")
