'''
Created on 30.12.2018

@author: ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.modules.TMCM_0010_OPC import TMCM_0010_OPC

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts(Serial=True)

myInterface = serial_tmcl_interface('COM15')
brakeChopper = TMCM_0010_OPC(myInterface)

" show config "
brakeChopper.showConfiguration()

myInterface.close()