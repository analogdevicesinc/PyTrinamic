################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Tests for the serial socket interface.

Requirements:

* A Landungsbruecke board connected to the PC.
* A (cloned) copy of the pyserial repository. 

Principal setup:

::                                           
    +---------------------+              +---------+                         
    | PC                  |              |         |                         
    |        +----------+ |              |         |                         
    |        |  Serial  | |   USB/Serial |         |                         
    |        |  Socket  ------------------         |                         
    |        |  Server  | |              |         |                         
    |        +-----|----+ |              |         |                         
    |              |      |              |         |                         
    |        +-----|----+ |              +---------+                         
    |        | Serial   | |            Landungsbruecke                                                     
    |        | Socket   | |                                                    
    |        | Client   | |                                                    
    |        +----------+ |                                                    
    +---------------------+       

Note, you probably need to modify the ``landungsbruecke_com_port`` variable to match the COM port of your Landungsbruecke board.
If the pyserial repository is not located in th same directory as the pytrinamic repository, the path to the ``tcp_serial_redirect.py`` script must be adjusted accordingly.
We make use of the `tcp_serial_redirect.py <https://pyserial.readthedocs.io/en/latest/examples.html#tcp-ip-serial-bridge>`_ script from the pyserial repository to create a socket server that redirects the serial communication to the Landungsbruecke board.
"""
import sys
import struct
import subprocess
from pathlib import Path

import pytest

from pytrinamic.connections import ConnectionManager
from pytrinamic.connections.socket_tmcl_interface import SocketTmclInterface
from pytrinamic.tmcl import TMCLCommand


this_file_dir = Path(__file__).parent

path_to_tcp_serial_redirect = this_file_dir / "../../pyserial/examples/tcp_serial_redirect.py"

landungsbruecke_com_port = "COM12"

tcp_ip_port_for_serial_socket_server = 7000

LANDUNGSBRUECKE_MODULE_NUMBER = 12


@pytest.fixture(scope="module")
def serial_socket_server():
    """Fixture to start the serial socket server (tcp_serial_redirect.py)."""
    process = subprocess.Popen(
        [sys.executable, path_to_tcp_serial_redirect, "-P", str(tcp_ip_port_for_serial_socket_server), landungsbruecke_com_port],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    yield None
    process.terminate()


def test_adapter_class_legacy(serial_socket_server):
    interface = SocketTmclInterface(ip_and_port=f"127.0.0.1:{tcp_ip_port_for_serial_socket_server}")
    get_fw_result = interface.send(TMCLCommand.GET_FIRMWARE_VERSION, 1, 0, 0)
    fw_version_minor, fw_version_major, module_number = struct.unpack("<BBH", get_fw_result.value.to_bytes(4, byteorder='little'))
    del fw_version_minor, fw_version_major
    assert module_number == LANDUNGSBRUECKE_MODULE_NUMBER
    interface.close()


def test_adapter_class_with(serial_socket_server):
    with SocketTmclInterface(ip_and_port=f"127.0.0.1:{tcp_ip_port_for_serial_socket_server}") as interface:
        get_fw_result = interface.send(TMCLCommand.GET_FIRMWARE_VERSION, 1, 0, 0)
        fw_version_minor, fw_version_major, module_number = struct.unpack("<BBH", get_fw_result.value.to_bytes(4, byteorder='little'))
        del fw_version_minor, fw_version_major
        assert module_number == LANDUNGSBRUECKE_MODULE_NUMBER


def test_connection_manager(serial_socket_server):
    cm = ConnectionManager(f"--interface socket_serial_tmcl --port 127.0.0.1:{tcp_ip_port_for_serial_socket_server}")
    with cm.connect() as interface:
        get_fw_result = interface.send(TMCLCommand.GET_FIRMWARE_VERSION, 1, 0, 0)
        fw_version_minor, fw_version_major, module_number = struct.unpack("<BBH", get_fw_result.value.to_bytes(4, byteorder='little'))
        del fw_version_minor, fw_version_major
        assert module_number == LANDUNGSBRUECKE_MODULE_NUMBER
