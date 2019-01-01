'''
Created on 30.12.2018

@author: ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.SerialInterface import SerialInterface
from PyTrinamic.modules.TMCM_010_OPC import TMCM_0010_OPC

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts()

myInterface = SerialInterface('COM5')
brakeChopper = TMCM_0010_OPC(myInterface)

" show config "
brakeChopper.showConfiguration()

myInterface.close()