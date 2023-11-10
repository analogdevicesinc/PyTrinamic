################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

"""Test for the ConnectionManager timeout parameter.

A (virtual) comport and a Kvaser CAN-Adapter are needed to run these tests.
Note, you may need change the comport number.
"""

import time

import pytest

from pytrinamic.connections import ConnectionManager
from pytrinamic.connections import KvaserTmclInterface
from pytrinamic.connections import SerialTmclInterface
from pytrinamic.connections import UartIcInterface


@pytest.mark.parametrize('interface,con_man_parameters', [
    ('serial_tmcl', ' --port COM4 --data-rate 115200'),
    ('uart_ic', ' --port COM4'),
    ('kvaser_tmcl', '')
])
@pytest.mark.parametrize('add_argument,expected_timeout', [
    ('', 5),
    (' --timeout 7', 7),
    (' --timeout 200', 200),
    (' --timeout 33.3', 33.3),
    (' --timeout 0.0', None),
    (' --timeout 0', None),
    (' --timeout -0', None),
])
def test_valid_input_cm(interface, con_man_parameters, add_argument, expected_timeout):
    """Check if the timeout is forwarded to the serial interface."""

    cm = ConnectionManager(f"--interface {interface}{con_man_parameters}" + add_argument)

    with cm.connect() as myinterface:
        if interface == 'serial_tmcl':
            assert myinterface._serial.timeout == expected_timeout
        elif interface == 'uart_ic':
            assert myinterface.serial.timeout == expected_timeout
        elif interface == 'kvaser_tmcl':
            assert myinterface._timeout_s == expected_timeout
        else:
            pytest.fail('Unexpected interface!')


@pytest.mark.parametrize('interface_class', [
    'kvaser_tmcl',
    'serial_tmcl',
    'uart_ic',
])
@pytest.mark.parametrize('timeout_input,expected_timeout', [
    ('', 5),
    (None, None),
    (0, None),
    (7, 7),
    (33.3, 33.3),
])
def test_valid_input_direct(interface_class, timeout_input, expected_timeout):
    """Test like the test_valid_input_cm() but without the connection manager."""
    if interface_class == 'kvaser_tmcl':
        if timeout_input == '':
            myinterface = KvaserTmclInterface()
        else:
            myinterface = KvaserTmclInterface(timeout_s=timeout_input)
        assert myinterface._timeout_s == expected_timeout
    elif interface_class == 'serial_tmcl':
        if timeout_input == '':
            myinterface = SerialTmclInterface('COM4')
        else:
            myinterface = SerialTmclInterface('COM4', timeout_s=timeout_input)
        assert myinterface._serial.timeout == expected_timeout
    elif interface_class == 'uart_ic':
        if timeout_input == '':
            myinterface = UartIcInterface('COM4')
        else:
            myinterface = UartIcInterface('COM4', timeout_s=timeout_input)
        assert myinterface.serial.timeout == expected_timeout


@pytest.mark.parametrize('con_man_call,expected_exception', [
    ('--interface serial_tmcl --port COM4 --data-rate 115200', RuntimeError),
    ('--interface kvaser_tmcl', ConnectionError),
])
def test_actual_timeout(con_man_call, expected_exception):
    """We just call the receive-function without sending anything and check if a timeout will be raised."""

    cm = ConnectionManager(f"{con_man_call} --timeout 1.5")

    with pytest.raises(expected_exception):
        with cm.connect() as myinterface:
            start_time = time.perf_counter()
            myinterface._recv(0, 0)
    stop_time = time.perf_counter()
    duration = stop_time - start_time
    assert 1.5 < duration < 1.7


@pytest.mark.parametrize('timeout_argument', [
    'string',
    '0x1F',
    '-0.1',
    '-100',
])
def test_invalid_timeout(timeout_argument):
    """Test some invalid arguments for the timeout value."""
    with pytest.raises(SystemExit) as exec_info:
        ConnectionManager(f"--interface serial_tmcl --port COM4 --data-rate 115200 --timeout {timeout_argument}")
