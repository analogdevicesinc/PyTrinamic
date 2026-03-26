################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

from pytrinamic.connections.tmcl_interface import TmclInterface
from pytrinamic.evalboards import TMC6460_eval


class MockTmclInterface(TmclInterface):
    def __init__(self):
        super().__init__()

    def read_register(self, register_address, command, channel, module_id=None, signed=False):
        return 0

    def write_register(self, register_address, command, channel, value, module_id=None):
        pass


def test_tmc6460_eval_read_write(mocker):
    """This is more like a demo for now."""

    mock_tmcl_interface = MockTmclInterface()
    read_reg_fn_spy = mocker.spy(mock_tmcl_interface, "read_register")
    write_reg_fn_spy = mocker.spy(mock_tmcl_interface, "write_register")
    tmc6460_eval = TMC6460_eval(mock_tmcl_interface)
    map = tmc6460_eval.ics[0].REGMAP

    # Check register read
    tmc6460_eval.read(map.CHIP.REVISION)
    read_reg_fn_spy.assert_called_once()
    read_reg_fn_spy.reset_mock()

    # Check register write
    tmc6460_eval.write(map.FOC.PID_POSITION_LIMIT_LOW, 4000)
    write_reg_fn_spy.assert_called_once()
    write_reg_fn_spy.reset_mock()

    # Check field read
    tmc6460_eval.read(map.MCC_CONFIG.MOTOR_MOTION.MOTOR_TYPE)
    read_reg_fn_spy.assert_called_once()
    read_reg_fn_spy.reset_mock()

    # Check field write
    tmc6460_eval.write(map.MCC_CONFIG.MOTOR_MOTION.N_POLE_PAIRS, 4)
    write_reg_fn_spy.assert_called_once()
    write_reg_fn_spy.reset_mock()

    # Check choice write
    tmc6460_eval.write(map.MCC_CONFIG.PWM.CHOP.choice.CENTERED)
    write_reg_fn_spy.assert_called_once()
    write_reg_fn_spy.reset_mock()