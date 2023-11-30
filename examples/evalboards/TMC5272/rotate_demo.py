"""
Move a motor back and forth using velocity and position mode of the TMC5272
"""
import time
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5272_eval

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    # Create TMC5272-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5272_eval(my_interface)
    print(eval_board)
    motor = eval_board.motors[0]
    mc = eval_board.ics[0]

    #eval_board.write_register_field(mc.FIELD.GCONF_M0_MULTISTEP_FILT, 1)
    #eval_board.write_register_field(mc.FIELD.M0_IHOLD_IRUN_IHOLD, 8)
    #eval_board.write_register_field(mc.FIELD.M0_IHOLD_IRUN_IRUN, 31)
    #eval_board.write_register_field(mc.FIELD.M0_CHOPCONF_INTPOL, 1)
    eval_board.write_register(0x00, 0x00020002)
    eval_board.write_register(0x04, 0x60223B18)
    eval_board.write_register(0x05, 0x00000004)
    eval_board.write_register(0x06, 0x0000FAFA)
    eval_board.write_register(0x07, 0x00000001)
    eval_board.write_register(0x08, 0x00000019)
    eval_board.write_register(0x09, 0xFFFF8056)
    eval_board.write_register(0x10, 0xFFFFFFFF)
    eval_board.write_register(0x12, 0x04011F0A)
    eval_board.write_register(0x13, 0x0000000A)
    eval_board.write_register(0x18, 0x00029617)
    eval_board.write_register(0x38, 0x10410153)
    eval_board.write_register(0x3C, 0xC40C001D)
    eval_board.write_register(0x20, 0x000003E8)
    eval_board.write_register(0x22, 0x000003E8)
    eval_board.write_register(0x24, 0x0000000A)
    eval_board.write_register(0x25, 0x0000000A)
    eval_board.write_register(0x2D, 0x10000000)
    eval_board.write_register(0x2F, 0x00108000)
    eval_board.write_register(0x38, 0x10410153)
    eval_board.write_register(0x3C, 0xC40C001D)
    eval_board.write_register(0x3F, 0x00000200)
    time.sleep(5)
    print("Rotating...")
    motor.rotate(25000)
    time.sleep(5)
    print("Stopping...")
    motor.stop()
    time.sleep(1)

    #print("Moving back to 0...")
    #motor.move_to(0, 200000)
#
    ## Wait until position 0 is reached
    #while motor.actual_position != 0:
    #    print("Actual position: " + str(motor.actual_position))
    #    time.sleep(0.2)
#
    #print("Reached position 0")

print("\nReady.")
