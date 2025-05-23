################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
import pathlib
import runpy
import builtins

import pytest

from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.modules import TMCM1140


this_files_directory = pathlib.Path(__file__).parent


class MockTmclInterface:
    def __init__(self):
        self._position_reached_toggle = True

    def __enter__(self):
        return self

    def __exit__(self, exitType, value, traceback):
        del exitType, value, traceback

    def set_axis_parameter(self, type, axis, value, module_id, ap_index_bit_width):
        pass

    def get_axis_parameter(self, type, axis, module_id, signed, ap_index_bit_width):
        if type == TMCM1140._MotorTypeA.AP.PositionReachedFlag:
            self._position_reached_toggle ^= True
            if self._position_reached_toggle:
                return 1
            else:
                return 0
        else:
            return 0

    def move_to(self, axis, position, module_id):
        pass

    def move_by(self, axis, delta, module_id):
        pass

    def rotate(self, axis, velocity, module_id):
        pass

    def stop(self, axis, module_id):
        pass


@pytest.mark.parametrize("example_script_path", [
    this_files_directory / "../TMCM1140/TMCL/CoolStep_demo.py",
    this_files_directory / "../TMCM1140/TMCL/rotate_demo.py",
    this_files_directory / "../TMCM1140/TMCL/StallGuard2_demo.py",
])
def test(monkeypatch, example_script_path):

    def mock_init(self, _=None):
        pass

    def mock_connect(self):
        return MockTmclInterface()

    def mock_sleep(_):
        pass

    def mock_input(_):
        pass

    monkeypatch.setattr(ConnectionManager, "__init__", mock_init)
    monkeypatch.setattr(ConnectionManager, "connect", mock_connect)
    monkeypatch.setattr(time, "sleep", mock_sleep)
    monkeypatch.setattr(builtins, "input", mock_input)

    runpy.run_path(example_script_path)
