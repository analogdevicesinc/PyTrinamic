#!/usr/bin/env python3
'''
Dump all register values of the shield IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are
used for communicating with the IC.

Created on 18.03.2020

@author: LK
'''

import PyTrinamic
from PyTrinamic.evalboards.TMC5160_shield import TMC5160_shield
from PyTrinamic.modules.TMC_EvalShield import TMC_EvalShield

PyTrinamic.showInfo()

from PyTrinamic.connections.ConnectionManagerPC import ConnectionManagerPC
myInterface = ConnectionManagerPC(interfaces=["usb_tmcl"]).connect()[0]

shields = TMC_EvalShield(myInterface, TMC5160_shield).shields

for shield in shields:
    print(shield)
    for name, register in shield.registers.__dict__.items():
        if((not name.startswith("__")) and (not name.endswith("__"))):
            print("{0}: 0x{1:08X}".format(name, shield.readRegister(register)))

myInterface.close()
