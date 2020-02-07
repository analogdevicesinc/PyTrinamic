#!/usr/bin/env python3
'''
Created on 30.12.2018

@author: ED
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.modules.TMCM_0010_OPC import TMCM_0010_OPC

PyTrinamic.showInfo()

connectionManager = ConnectionManager()
myInterface = connectionManager.connect()
brakeChopper = TMCM_0010_OPC(myInterface)

" show config "
brakeChopper.showConfiguration()

myInterface.close()