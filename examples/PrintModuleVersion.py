"""
Print the received version of an attached module.

This uses the generic connection manager commandline to allow flexible
module connection selection.
"""

from PyTrinamic.connections.ConnectionManager import ConnectionManager

myInterface = ConnectionManager().connect()

with myInterface:
    print(myInterface.get_version_string())
