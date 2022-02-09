
import sys
import time
import runpy

import pytest

sys.path.insert(0, '../../../..')
from pytrinamic.connections.connection_manager import ConnectionManager  # noqa: E402
from pytrinamic.modules import TMCM1636  # noqa: E402


class MockTmclInterface:
    def __init__(self):
        self._position_reached_toggle = True
        self._digital_input_toggle = True

    def __enter__(self):
        return self

    def __exit__(self, exitType, value, traceback):
        del exitType, value, traceback

    def set_axis_parameter(self, type, axis, value, module_id):
        pass

    def get_axis_parameter(self, type, axis, module_id, signed):
        if type == TMCM1636._MotorTypeA.AP.PositionReachedFlag:
            self._position_reached_toggle ^= True
            if self._position_reached_toggle:
                return 1
            else:
                return 0
        elif type == TMCM1636._MotorTypeA.AP.RightStopSwitch or type == TMCM1636._MotorTypeA.AP.LeftStopSwitch:
            self._position_reached_toggle ^= True
            if self._digital_input_toggle:
                return 1
            else:
                return 0
        else:
            return 0

    def move_to(self, axis, position, module_id):
        pass

    def move_by(self, axis, difference, module_id):
        pass

    def rotate(self, axis, velocity, module_id):
        pass

    def stop(self, axis, module_id):
        pass

    def get_digital_input(self, x, module_id):
        self._digital_input_toggle ^= True
        if self._digital_input_toggle:
            return 1
        else:
            return 0


@pytest.mark.parametrize('example_script_path', [
    f'../TMCM1636/TMCL/encoder_position_mode.py',
    f'../TMCM1636/TMCL/hall_digital_input.py',
    f'../TMCM1636/TMCL/hall_endstop.py',
    f'../TMCM1636/TMCL/hall_position_mode.py',
    f'../TMCM1636/TMCL/position_abn_abs.py',
])
def test(monkeypatch, example_script_path):

    def mock_init(self, _=None):
        pass

    def mock_connect(self):
        return MockTmclInterface()

    def mock_sleep(_):
        pass

    monkeypatch.setattr(ConnectionManager, '__init__', mock_init)
    monkeypatch.setattr(ConnectionManager, 'connect', mock_connect)
    monkeypatch.setattr(time, 'sleep', mock_sleep)

    runpy.run_path(example_script_path)
