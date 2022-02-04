"""
Dump all register values of the TMC2100 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC2100_eval

pytrinamic.show_info()

myInterface = ConnectionManager().connect()
print(myInterface)

eval_board = TMC2100_eval(myInterface)
drv = eval_board.ics[0]
print("Driver info: " + str(drv.get_info()))
print("Register dump for " + str(drv.get_name()) + ":")

print("GCONF:       0x{0:08X}".format(eval_board.read_register(drv.REG.GCONF)))

myInterface.close()

print("\nReady.")
