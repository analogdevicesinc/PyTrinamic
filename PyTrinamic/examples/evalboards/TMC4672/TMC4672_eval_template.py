#!/usr/bin/env python3
'''
Created on 21.03.2019

@author: ed
'''
if __name__ == '__main__':
    pass

import time
import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.connections.uart_ic_interface import uart_ic_interface
from PyTrinamic.evalboards.TMC4672_eval import TMC4672_eval
from PyTrinamic.ic.TMC4672.TMC4672 import TMC4672

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts(Serial=True)

" use evalboard via landungsbrücke or directly via UART"
USE_LANDUNGSBRUECKE = True #False

if USE_LANDUNGSBRUECKE:
    myInterface = serial_tmcl_interface('COM5')
    tmc4672 = TMC4672_eval(myInterface).ic()
else:
    myInterface = uart_ic_interface(PyTrinamic.firstAvailableComPort())
    tmc4672 = TMC4672(myInterface)

" get register set "
tmc4672_reg = tmc4672.register()

" read ChipInfo "
tmc4672.showChipInfo()

" add your python code here "
"..."
time.sleep(1) 

" close interface"
myInterface.close()