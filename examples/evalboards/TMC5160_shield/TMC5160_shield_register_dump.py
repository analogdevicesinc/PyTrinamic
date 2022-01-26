#!/usr/bin/env python3
'''
Dump all register values of the shield IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 18.03.2020

@author: LK
'''

import pytrinamic
from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.modules.tmc_eval_shield import TmcEvalShield
from pytrinamic.evalboards.TMC5160_shield import TMC5160_shield

pytrinamic.show_info()
myInterface = ConnectionManager().connect()
shields = TmcEvalShield(myInterface, TMC5160_shield).shields

for shield in shields:
    print(shield)
    for name, register in shield.registers.__dict__.items():
        if(not name.startswith("__")) and (not name.endswith("__")):
            print("{0}: 0x{1:08X}".format(name, shield.read_register(register)))

myInterface.close()
