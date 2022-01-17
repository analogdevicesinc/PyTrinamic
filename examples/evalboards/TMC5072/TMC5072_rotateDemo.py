#!/usr/bin/env python3
'''
Move a motor back and forth using velocity and position mode of the TMC5072

Created on 20.09.2019

@author: JM
'''

import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards.TMC5072_eval import TMC5072_eval

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
PyTrinamic.show_info()
eval = TMC5072_eval(myInterface)
ic = eval.IC

print("Preparing parameters")
ic.MOTORS[0].write_axis_field(ic.FIELDS.A1, 1000)
# ic.write_axis_field(0, ic.FIELDS.A1, 1000)
ic.MOTORS[0].write_axis_field(ic.FIELDS.V1, 50000)
# ic.write_axis_field(0, ic.FIELDS.V1, 50000)
ic.MOTORS[0].write_axis_field(ic.FIELDS.D1, 500)
# ic.write_axis_field(0, ic.FIELDS.D1, 500)
ic.MOTORS[0].write_axis_field(ic.FIELDS.DMAX, 500)
# ic.write_axis_field(0, ic.FIELDS.DMAX, 500)
ic.MOTORS[0].write_axis_field(ic.FIELDS.VSTART, 0)
# ic.write_axis_field(0, ic.FIELDS.VSTART, 0)
ic.MOTORS[0].write_axis_field(ic.FIELDS.VSTOP, 10)
# ic.write_axis_field(0, ic.FIELDS.VSTOP, 10)
ic.MOTORS[0].write_axis_field(ic.FIELDS.AMAX, 1000)
# ic.write_axis_field(0, ic.FIELDS.AMAX, 1000)
ic.MOTORS[1].write_axis_field(ic.FIELDS.A1, 1000)
# ic.write_axis_field(0, ic.FIELDS.A1, 1000)
ic.MOTORS[1].write_axis_field(ic.FIELDS.V1, 50000)
# ic.write_axis_field(0, ic.FIELDS.V1, 50000)
ic.MOTORS[1].write_axis_field(ic.FIELDS.D1, 500)
# ic.write_axis_field(0, ic.FIELDS.D1, 500)
ic.MOTORS[1].write_axis_field(ic.FIELDS.DMAX, 500)
# ic.write_axis_field(0, ic.FIELDS.DMAX, 500)
ic.MOTORS[1].write_axis_field(ic.FIELDS.VSTART, 0)
# ic.write_axis_field(0, ic.FIELDS.VSTART, 0)
ic.MOTORS[1].write_axis_field(ic.FIELDS.VSTOP, 10)
# ic.write_axis_field(0, ic.FIELDS.VSTOP, 10)
ic.MOTORS[1].write_axis_field(ic.FIELDS.AMAX, 1000)
# ic.write_axis_field(0, ic.FIELDS.AMAX, 1000)

print("Rotating motor 1")
ic.MOTORS[0].rotate(10*25600)

time.sleep(5)

print("Stopping motor 1")
ic.MOTORS[0].stop()

time.sleep(1)

print("Rotating motor 2")
ic.MOTORS[1].rotate(10*25600)

time.sleep(5)

print("Stopping motor 2")
ic.MOTORS[1].stop()

time.sleep(1)

print("Moving back to 0")
ic.MOTORS[0].move_to(0, 100000)

# Wait until position 0 is reached
while eval.MOTORS[0].actual_position != 0:
    pass

print("Reached Position 0")

myInterface.close()
