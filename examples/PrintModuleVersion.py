"""
Print the received version of an attached module.

This uses the generic connection manager commandline to allow flexible
module connection selection.
"""
from pytrinamic.connections import ConnectionManager

with ConnectionManager().connect() as my_interface:
    print(my_interface)
    print(my_interface.get_version_string())
