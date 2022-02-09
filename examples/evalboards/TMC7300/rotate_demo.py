"""
Move a DC motor back and forth using the TMC7300
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC7300_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create TMC7300-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC7300_eval(my_interface)
    motor = eval_board.motors[0]

    motor.set_standby_current(0)

    print("Rotating...")
    motor.set_axis_parameter(motor.AP.PWMDutyA, 50)
    time.sleep(2)

    print("Stopping...")
    motor.set_axis_parameter(motor.AP.PWMDutyA, 0)
    time.sleep(1)

    print("Rotating...")
    motor.set_axis_parameter(motor.AP.PWMDutyA, -50)
    time.sleep(2)

    print("Stopping...")
    motor.set_axis_parameter(motor.AP.PWMDutyA, 0)
    time.sleep(1)

print("\nReady.")
