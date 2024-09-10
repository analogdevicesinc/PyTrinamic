################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.connections.tmcl_interface import TmclInterface
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import Access


PID_VELOCITY_LIMIT_REGISTER_ADDRESS = 0x60
HALL_MODE_REGISTER_ADDRESS = 0x33


class MockTmclInterface(TmclInterface):
    def __init__(self):
        super().__init__()

    def read_mc(self, register_address, module_id=None, signed=False):
        return 0

    def write_mc(self, register_address, value, module_id=None):
        pass


def test_tmc4671_eval_read_write(mocker):
    mock_tmcl_interface = MockTmclInterface()
    read_mc_fn_spy = mocker.spy(mock_tmcl_interface, "read_mc")
    write_mc_fn_spy = mocker.spy(mock_tmcl_interface, "write_mc")
    tmc4671_eval = TMC4671_eval(mock_tmcl_interface)
    register = tmc4671_eval.ics[0].register

    # Check register read
    tmc4671_eval.read(register.PID_VELOCITY_LIMIT)
    read_mc_fn_spy.assert_called_once_with(register_address=PID_VELOCITY_LIMIT_REGISTER_ADDRESS, module_id=1, signed=False)
    read_mc_fn_spy.reset_mock()

    # Check register write
    tmc4671_eval.write(register.PID_VELOCITY_LIMIT, 42)
    write_mc_fn_spy.assert_called_once_with(register_address=PID_VELOCITY_LIMIT_REGISTER_ADDRESS, value=42, module_id=1)
    write_mc_fn_spy.reset_mock()

    # Check field read
    tmc4671_eval.read(register.HALL_MODE.polarity)
    read_mc_fn_spy.assert_called_once_with(register_address=HALL_MODE_REGISTER_ADDRESS, module_id=1, signed=False)
    read_mc_fn_spy.reset_mock()

    # Check field write
    tmc4671_eval.write(register.HALL_MODE.polarity, 1)
    read_mc_fn_spy.assert_called_once_with(register_address=HALL_MODE_REGISTER_ADDRESS, module_id=1, signed=False)
    read_mc_fn_spy.reset_mock()
    write_mc_fn_spy.assert_called_once_with(register_address=HALL_MODE_REGISTER_ADDRESS, value=1, module_id=1)
    write_mc_fn_spy.reset_mock()


def test_tmc4671_field():
    mock_tmcl_interface = MockTmclInterface()
    tmc4671_eval = TMC4671_eval(mock_tmcl_interface)
    register = tmc4671_eval.ics[0].register

    # Check is signed
    ####################################################################################################

    assert not register.PID_VELOCITY_LIMIT.signed
    assert register.PID_VELOCITY_TARGET.signed  # TODO: Fix the generated code to have the correct signedness!

    # Check is is_in_bounds
    ####################################################################################################

    # Because ADC_I0_OFFSET is unsigned -1 should not be in bounds.
    assert not register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.is_in_bounds(-1)
    # Check lower bound
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.is_in_bounds(0)
    # Check upper bound
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.is_in_bounds(0xFFFF)
    # Check out of bounds
    assert not register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.is_in_bounds(0x10000)

    # Check lower bound
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_SCALE.is_in_bounds(-0x8000)  # TODO: Fix the generated code to have the correct signedness!
    # Check upper bound
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_SCALE.is_in_bounds(0x7FFF)
    # Check out of bounds - lower bound
    assert not register.ADC_I0_SCALE_OFFSET.ADC_I0_SCALE.is_in_bounds(-0x8001)
    # Check out of bounds - upper bound
    assert not register.ADC_I0_SCALE_OFFSET.ADC_I0_SCALE.is_in_bounds(0x8000)  # TODO: Fix the generated code to have the correct signedness!

    # Check access
    ####################################################################################################
    
    assert register.ADC_IWY_IUX.ADC_IUX.access == Access.R
    assert register.ADC_IWY_IUX.ADC_IUX.access.name == "R"
    assert not register.ADC_IWY_IUX.ADC_IUX.access.is_writable()
    # .. also check a field that is writable
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.access.is_writable()
    

def test_tmc4671_register():
    mock_tmcl_interface = MockTmclInterface()
    tmc4671_eval = TMC4671_eval(mock_tmcl_interface)
    register = tmc4671_eval.ics[0].register

    # Check is access
    ####################################################################################################
    # For a register
    assert register.ADC_I0_SCALE_OFFSET.access == Access.RW
    assert register.ADC_I0_SCALE_OFFSET.access.name == "RW"
    assert register.ADC_I0_SCALE_OFFSET.access.is_writable()

    # Check names
    ####################################################################################################
    assert register.ABN_DECODER_COUNT.name == "ABN_DECODER_COUNT"

    # Check fields
    ####################################################################################################
    fields_of_mode_ramp_mode_motion = register.MODE_RAMP_MODE_MOTION.fields()
    assert fields_of_mode_ramp_mode_motion[0] == register.MODE_RAMP_MODE_MOTION.MODE_MOTION
    assert fields_of_mode_ramp_mode_motion[1] == register.MODE_RAMP_MODE_MOTION.MODE_RAMP
    assert fields_of_mode_ramp_mode_motion[2] == register.MODE_RAMP_MODE_MOTION.MODE_FF
    assert fields_of_mode_ramp_mode_motion[3] == register.MODE_RAMP_MODE_MOTION.MODE_PID_SMPL
    assert fields_of_mode_ramp_mode_motion[4] == register.MODE_RAMP_MODE_MOTION.MODE_PID_TYPE


def test_tmc4671_register_group():
    mock_tmcl_interface = MockTmclInterface()
    tmc4671_eval = TMC4671_eval(mock_tmcl_interface)
    register = tmc4671_eval.ics[0].register

    # Check find_register
    assert register.find("ABN_DECODER_COUNT") == register.ABN_DECODER_COUNT

    list_of_registers = register.registers()
    assert list_of_registers[0] == register.CHIPINFO_DATA
    assert list_of_registers[-1] == register.STATUS_MASK