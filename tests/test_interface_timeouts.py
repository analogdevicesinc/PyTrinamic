"""Test for the ConnectionManager timeout parameter.

A (virtual) comport and a Kvaser CAN-Adapter are needed to run these tests.
Note, you may need change the comport number.
"""

import time

import pytest

from pytrinamic.connections import ConnectionManager


@pytest.mark.parametrize('add_argument,expected_timeout', [
    ('', 5),
    (' --timeout 7', 7),
    (' --timeout 200', 200),
    (' --timeout 33.3', 33.3),
])
def test_serial_tmcl(add_argument, expected_timeout):
    """Check if the timeout is forwarded to the serial interface."""

    cm = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200" + add_argument)

    with cm.connect() as myinterface:
        assert myinterface._serial.timeout == expected_timeout


@pytest.mark.parametrize('add_argument,expected_timeout', [
    ('', 5),
    (' --timeout 7', 7),
    (' --timeout 200', 200),
    (' --timeout 33.3', 33.3),
])
def test_kvaser_tmcl(add_argument, expected_timeout):
    """Check if the timeout is forwarded to the Kvaser interface."""

    cm = ConnectionManager("--interface kvaser_tmcl" + add_argument)

    with cm.connect() as myinterface:
        assert myinterface._timeout_s == expected_timeout


@pytest.mark.parametrize('con_man_call,expected_exception', [
    ('--interface serial_tmcl --port COM4 --data-rate 115200', RuntimeError),
    ('--interface kvaser_tmcl', ConnectionError),
])
def test_actual_timeout(con_man_call, expected_exception):
    """We just call the receive-function without sending anything and check if a timeout will be raised."""

    cm = ConnectionManager(f"{con_man_call} --timeout 1.5")

    with pytest.raises(expected_exception) as exec_info:
        with cm.connect() as myinterface:
            start_time = time.perf_counter()
            myinterface._recv(0, 0)
    stop_time = time.perf_counter()
    duration = stop_time - start_time
    assert 1.5 < duration < 1.7


@pytest.mark.parametrize('timeout_argument', [
    'string',
    '0',
    '0x1F'
])
def test_invalid_timeout(timeout_argument):
    """Test some invalid arguments for the timeout value."""
    with pytest.raises(SystemExit) as exec_info:
        ConnectionManager(f"--interface serial_tmcl --port COM4 --data-rate 115200 --timeout {timeout_argument}")
