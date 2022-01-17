
import sys
import time
import runpy
import builtins

import pytest


sys.path.insert(0, '../../../..')
from PyTrinamic.connections.ConnectionManager import ConnectionManager  # noqa: E402
from PyTrinamic.modules import TMCM_1140  # noqa: E402


class MockTmclInterface:
    def __init__(self):
        self._position_reached_toggle = True

    def __enter__(self):
        return self

    def __exit__(self, exitType, value, traceback):
        del exitType, value, traceback

    def setAxisParameter(self, type, axis, value, module_id):
        pass

    def axisParameter(self, type, axis, module_id, signed):
        if type == TMCM_1140.Motor0.APs.PositionReachedFlag:
            self._position_reached_toggle ^= True
            if self._position_reached_toggle:
                return 1
            else:
                return 0
        else:
            return 0

    def moveTo(self, axis, position, module_id):
        pass

    def moveBy(self, axis, difference, module_id):
        pass

    def rotate(self, axis, velocity, module_id):
        pass

    def stop(self, axis, module_id):
        pass


@pytest.mark.parametrize('example_script_path', [
    f'../TMCM_1140/TMCL/CoolStep_demo.py',
    f'../TMCM_1140/TMCL/rotate_demo.py',
    f'../TMCM_1140/TMCL/StallGuard2_demo.py',
])
def test(monkeypatch, example_script_path):

    def mock_init(self, _):
        pass

    def mock_connect(self):
        return MockTmclInterface()

    def mock_sleep(_):
        pass

    def mock_input(_):
        pass

    monkeypatch.setattr(ConnectionManager, '__init__', mock_init)
    monkeypatch.setattr(ConnectionManager, 'connect', mock_connect)
    monkeypatch.setattr(time, 'sleep', mock_sleep)
    monkeypatch.setattr(builtins, 'input', mock_input)

    runpy.run_path(example_script_path)
