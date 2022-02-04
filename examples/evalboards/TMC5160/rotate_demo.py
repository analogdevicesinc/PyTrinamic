"""
Move a motor back and forth using velocity and position mode of the TMC5160
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5160_eval

pytrinamic.show_info()
myInterface = ConnectionManager().connect()
print(myInterface)

with myInterface:
    # Create TMC5160-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5160_eval(myInterface)
    mc = eval_board.ics[0]
    motor = eval_board.motors[0]

    print("Preparing parameter...")
    eval_board.write_register(mc.REG.A1, 1000)
    eval_board.write_register(mc.REG.V1, 50000)
    eval_board.write_register(mc.REG.D1, 500)
    eval_board.write_register(mc.REG.DMAX, 500)
    eval_board.write_register(mc.REG.VSTART, 0)
    eval_board.write_register(mc.REG.VSTOP, 10)
    eval_board.write_register(mc.REG.AMAX, 1000)

    # Clear actual positions
    motor.actual_position = 0

    print("Rotating...")
    motor.rotate(7*25600)
    time.sleep(5)

    print("Stopping...")
    motor.stop()
    time.sleep(1)

    print("Moving back to 0...")
    motor.move_to(0, 100000)

    # Wait until position 0 is reached
    while motor.actual_position != 0:
        print("Actual position: " + str(motor.actual_position))
        time.sleep(0.2)

    print("Reached position 0")

print("\nReady.")
