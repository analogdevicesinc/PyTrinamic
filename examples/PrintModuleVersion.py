#!/usr/bin/env python3
"""
Print the received version of an attached module.

This uses the generic connection manager commmandline to allow flexible
module connection selection.
"""

from PyTrinamic.connections.ConnectionManager import ConnectionManager

connectionManager = ConnectionManager()

myInterface = connectionManager.connect()
print(myInterface.getVersionString())
