################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Test the dot Register/Field/Choice syntax and metadata in context of the TMC4671."""

import pytest

from pytrinamic.connections.tmcl_interface import TmclInterface
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import Access


PID_VELOCITY_LIMIT_REGISTER_ADDRESS = 0x60
HALL_MODE_REGISTER_ADDRESS = 0x33
CHIP_INFO_ADDRESS_ADDRESS = 0x01


class MockTmclInterface(TmclInterface):
    """This interface/connection is given to the Eval instead of a real connection.
    
    The `read_mc()` and `write_mc()` functions are mocked, and called instead of the real functions.
    """
    def __init__(self):
        super().__init__()

    def read_mc(self, register_address, module_id=None, signed=False):
        return 0

    def write_mc(self, register_address, value, module_id=None):
        pass


def test_tmc4671_eval_read_write(mocker):
    """Test dot syntax read/write of registers, fields."""
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

    # Check Choice write
    tmc4671_eval.write(register.CHIPINFO_ADDR.CHIP_INFO_ADDRESS.choice["SI_TYPE"])
    write_mc_fn_spy.assert_called_once_with(register_address=CHIP_INFO_ADDRESS_ADDRESS, value=0, module_id=1)
    write_mc_fn_spy.reset_mock()
    tmc4671_eval.write(register.CHIPINFO_ADDR.CHIP_INFO_ADDRESS.choice["SI_VERSION"])
    write_mc_fn_spy.assert_called_once_with(register_address=CHIP_INFO_ADDRESS_ADDRESS, value=1, module_id=1)
    write_mc_fn_spy.reset_mock()


def test_field_get():
    
    tmc4671_eval = TMC4671_eval(None)
    register = tmc4671_eval.ics[0].register

    register_value = 0x00000000
    register_value = register.MOTOR_TYPE_N_POLE_PAIRS.MOTOR_TYPE.set(register_value, 0x03)
    register_value = register.MOTOR_TYPE_N_POLE_PAIRS.N_POLE_PAIRS.set(register_value, 0xA5A5)
    assert register_value == 0x0003A5A5

    register_value = 0xFFFFFFFF
    register_value = register.MOTOR_TYPE_N_POLE_PAIRS.MOTOR_TYPE.set(register_value, 0x03)
    register_value = register.MOTOR_TYPE_N_POLE_PAIRS.N_POLE_PAIRS.set(register_value, 0xA5A5)
    assert register_value == 0xFF03A5A5


def test_field_set():
    
    tmc4671_eval = TMC4671_eval(None)
    register = tmc4671_eval.ics[0].register

    register_value = 0x00000000
    assert register.MOTOR_TYPE_N_POLE_PAIRS.MOTOR_TYPE.get(register_value) == 0x00
    assert register.MOTOR_TYPE_N_POLE_PAIRS.N_POLE_PAIRS.get(register_value) == 0x0000

    register_value = 0x0003FEDC
    assert register.MOTOR_TYPE_N_POLE_PAIRS.MOTOR_TYPE.get(register_value) == 0x03
    assert register.MOTOR_TYPE_N_POLE_PAIRS.N_POLE_PAIRS.get(register_value) == 0xFEDC



def test_tmc4671_out_of_bounds_exception():
    
    mock_tmcl_interface = MockTmclInterface()
    tmc4671_eval = TMC4671_eval(mock_tmcl_interface)
    register = tmc4671_eval.ics[0].register
        
    # HALL_MODE.polarity is a bool, so 2 should not be allowed.
    with pytest.raises(ValueError):
        tmc4671_eval.write(register.HALL_MODE.polarity, 2)

    # With omit_bounds_check=True, the write should not raise an exception.
    tmc4671_eval.write(register.HALL_MODE.polarity, 2, omit_bounds_check=True)

    # PID_VELOCITY_LIMIT is unsigned, so -1 should not be allowed.
    with pytest.raises(ValueError):
        tmc4671_eval.write(register.PID_VELOCITY_LIMIT, -1)

    # With omit_bounds_check=True, the write should not raise an exception.
    tmc4671_eval.write(register.PID_VELOCITY_LIMIT, -1, omit_bounds_check=True)


def test_tmc4671_access_exception():
    mock_tmcl_interface = MockTmclInterface()
    tmc4671_eval = TMC4671_eval(mock_tmcl_interface)
    register = tmc4671_eval.ics[0].register

    # CHIPINFO_DATA is read only so writing to it should raise a PermissionError.
    with pytest.raises(PermissionError):
        tmc4671_eval.write(register.CHIPINFO_DATA, 0)

    # With omit_permission_checks=True, the write should not raise an exception.
    tmc4671_eval.write(register.CHIPINFO_DATA, 0, omit_permission_checks=True)


def test_tmc4671_field():
    """Test field metadata and helper functions."""

    mock_tmcl_interface = MockTmclInterface()
    tmc4671_eval = TMC4671_eval(mock_tmcl_interface)
    register = tmc4671_eval.ics[0].register

    # Check is signed
    assert not register.PID_VELOCITY_LIMIT.signed
    assert register.PID_VELOCITY_TARGET.signed  # TODO: Fix the generated code to have the correct signedness!

    # Check is is_in_bounds - for unsigned fields
    # Because ADC_I0_OFFSET is unsigned -1 should not be in bounds.
    assert not register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.is_in_bounds(-1)
    # Check lower bound
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.is_in_bounds(0)
    # Check upper bound
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.is_in_bounds(0xFFFF)
    # Check out of bounds
    assert not register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.is_in_bounds(0x10000)

    # Check is is_in_bounds - for signed fields
    # Check lower bound
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_SCALE.is_in_bounds(-0x8000)  # TODO: Fix the generated code to have the correct signedness!
    # Check upper bound
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_SCALE.is_in_bounds(0x7FFF)
    # Check out of bounds - lower bound
    assert not register.ADC_I0_SCALE_OFFSET.ADC_I0_SCALE.is_in_bounds(-0x8001)
    # Check out of bounds - upper bound
    assert not register.ADC_I0_SCALE_OFFSET.ADC_I0_SCALE.is_in_bounds(0x8000)  # TODO: Fix the generated code to have the correct signedness!

    # Check access
    assert register.ADC_IWY_IUX.ADC_IUX.access == Access.R
    assert register.ADC_IWY_IUX.ADC_IUX.access.name == "R"
    assert not register.ADC_IWY_IUX.ADC_IUX.access.is_writable()
    # .. also check a field that is writable
    assert register.ADC_I0_SCALE_OFFSET.ADC_I0_OFFSET.access.is_writable()
    

def test_tmc4671_register():
    mock_tmcl_interface = MockTmclInterface()
    tmc4671_eval = TMC4671_eval(mock_tmcl_interface)
    register = tmc4671_eval.ics[0].register

    assert register.PID_VELOCITY_LIMIT.is_in_bounds(0)
    assert register.PID_VELOCITY_LIMIT.is_in_bounds(0xFFFFFFFF)
    assert not register.PID_VELOCITY_LIMIT.is_in_bounds(-1)
    assert not register.PID_VELOCITY_LIMIT.is_in_bounds(0x100000000)

    # Check is access
    assert register.ADC_I0_SCALE_OFFSET.access == Access.RW
    assert register.ADC_I0_SCALE_OFFSET.access.name == "RW"
    assert register.ADC_I0_SCALE_OFFSET.access.is_writable()

    # Check names
    assert register.ABN_DECODER_COUNT.name == "ABN_DECODER_COUNT"

    # Check the fields() function that gets you a list of all fields of a register.
    fields_of_mode_ramp_mode_motion = register.MODE_RAMP_MODE_MOTION.fields()
    assert len(fields_of_mode_ramp_mode_motion) == 5
    assert fields_of_mode_ramp_mode_motion[0] == register.MODE_RAMP_MODE_MOTION.MODE_MOTION
    assert fields_of_mode_ramp_mode_motion[1] == register.MODE_RAMP_MODE_MOTION.MODE_RAMP
    assert fields_of_mode_ramp_mode_motion[2] == register.MODE_RAMP_MODE_MOTION.MODE_FF
    assert fields_of_mode_ramp_mode_motion[3] == register.MODE_RAMP_MODE_MOTION.MODE_PID_SMPL
    assert fields_of_mode_ramp_mode_motion[4] == register.MODE_RAMP_MODE_MOTION.MODE_PID_TYPE


def test_tmc4671_register_group():
    mock_tmcl_interface = MockTmclInterface()
    tmc4671_eval = TMC4671_eval(mock_tmcl_interface)
    register = tmc4671_eval.ics[0].register

    # Check the find register function of the TMC4671 register group.
    assert register.find("ABN_DECODER_COUNT") == register.ABN_DECODER_COUNT

    # Check the list of registers function for the TMC4671 register group.
    list_of_registers = register.registers()
    assert list_of_registers[0] == register.CHIPINFO_DATA
    assert list_of_registers[-1] == register.STATUS_MASK
