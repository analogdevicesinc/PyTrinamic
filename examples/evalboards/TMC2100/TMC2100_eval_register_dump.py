#!/usr/bin/env python3
'''
Dump all register values of the TMC2100 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 15.10.2019

@author: JM
'''

import pytrinamic
from pytrinamic.evalboards.TMC2100_eval import TMC2100_eval

pytrinamic.show_info()

from pytrinamic.connections.ConnectionManager import ConnectionManager
connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
TMC2100 = TMC2100_eval(myInterface)

print("GCONF:       0x{0:08X}".format(TMC2100.readRegister(TMC2100.registers.GCONF)))

myInterface.close()