#!/usr/bin/env python3
'''
Print the received version of an attached module.

This uses the generic connection manager commmandline to allow flexible
module connection selection.

Created on 07.06.2019

@author: LH
'''

import sys
from PyTrinamic.connections.ConnectionManager import ConnectionManager

connectionManager = ConnectionManager(sys.argv, debug=False)

myInterface = connectionManager.connect()
print(myInterface.getVersionString())
