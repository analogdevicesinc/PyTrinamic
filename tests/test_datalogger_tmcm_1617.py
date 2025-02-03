################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from typing import Generator
import statistics
import dataclasses

import pytest

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1617
from pytrinamic.modules.tmcl_module import ParameterGroup, Parameter
from pytrinamic.datalogger import DataLoggerConfigError


ENUM = TMCM1617._MotorTypeA.ENUM

class TMCM1617Ex(TMCM1617):
    def adc_offset_correction(self):
        @dataclasses.dataclass
        class AdcChannel:
            value_ap: int
            offset_ap: int
        motor = self.motors[0]
        last_commutation_mode = motor.get_axis_parameter(motor.AP.CommutationMode)
        motor.set_axis_parameter(motor.AP.CommutationMode, ENUM.COMM_MODE_DISABLED)
        old_adc_offsets = []
        for ch in [AdcChannel(motor.AP.AdcPhaseA, motor.AP.AdcOffsetPhaseA), AdcChannel(motor.AP.AdcPhaseB, motor.AP.AdcOffsetPhaseB)]:
            old_adc_offsets.append((ch.offset_ap, motor.get_axis_parameter(ch.offset_ap)))
            adc_samples = [motor.get_axis_parameter(ch.value_ap) for _ in range(20)]
            adc_samples_mean = round(statistics.mean(adc_samples))
            motor.set_axis_parameter(ch.offset_ap, adc_samples_mean)
        motor.set_axis_parameter(motor.AP.CommutationMode, last_commutation_mode)
        yield None
        for old_adc_offset_ap, old_adc_offset_value in old_adc_offsets:
            motor.set_axis_parameter(old_adc_offset_ap, old_adc_offset_value)


@pytest.fixture(scope="module")
def kvaser_interface():
    connection_manager = ConnectionManager("--interface kvaser_tmcl")
    with connection_manager.connect() as my_interface:
        yield my_interface


@pytest.fixture(scope="function")
def tmcm1617(kvaser_interface) -> Generator[TMCM1617Ex, None, None]:
    module = TMCM1617Ex(kvaser_interface)
    yield module

    
@pytest.fixture
def rotate_motor_one_rps(tmcm1617: TMCM1617Ex):
    tmcm1617.adc_offset_correction()
    motor = tmcm1617.motors[0]
    motor.set_axis_parameter(motor.AP.EnableRamp, 0)
    motor.set_axis_parameter(motor.AP.ActualPosition, 0)
    motor.set_axis_parameter(motor.AP.CommutationMode, ENUM.COMM_MODE_OPENLOOP)
    motor.set_axis_parameter(motor.AP.TargetVelocity, 60)
    yield None
    motor.set_axis_parameter(motor.AP.TargetVelocity, 0)
    motor.set_axis_parameter(motor.AP.CommutationMode, ENUM.COMM_MODE_OPENLOOP)


def test_error_no_samples_per_channel_given(tmcm1617: TMCM1617Ex):
    """Check if a proper error is raised when `samples_per_channel` is not given."""

    dl = tmcm1617.datalogger

    dl.config.log_data = {
        "test": dl.DataTypeAp(index=0),
    }

    with pytest.raises(DataLoggerConfigError) as excinfo:
        dl.activate_trigger()
    assert str(excinfo.value) == "No samples per channel specified!"


def test_error_exceed_channels(tmcm1617: TMCM1617Ex):
    """Check if a proper error is raised when the number of channels exceeds the module's RAMDebug capabilities."""

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    dl.config.log_data = {
        "a": dl.DataTypeAp(index=0),
        "b": dl.DataTypeAp(index=1),
        "c": dl.DataTypeAp(index=2),
        "d": dl.DataTypeAp(index=3),
        "e": dl.DataTypeAp(index=4),
    }

    with pytest.raises(DataLoggerConfigError) as excinfo:
        dl.activate_trigger()
    assert str(excinfo.value) == "Exceeding number of channels!"


def test_error_exceed_buffer_limit(tmcm1617: TMCM1617Ex):
    """Check if a proper error is raised when a module's RAMDebug buffer limit is exceeded."""

    dl = tmcm1617.datalogger
    info = dl.get_info()

    dl.config.samples_per_channel = info.sample_buffer_length + 1
    dl.config.log_data = {
        "a": dl.DataTypeAp(index=0),
    }

    with pytest.raises(DataLoggerConfigError) as excinfo:
        dl.activate_trigger()
    assert str(excinfo.value) == "Samples per channel exceeds sample buffer length!"


def test_error_missing_trigger_channel(tmcm1617: TMCM1617Ex):
    """Check if a proper error is raised when trigger is conditional but no trigger data is given."""

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    dl.config.log_data = {
        "a": dl.DataTypeAp(index=0),
    }
    dl.config.trigger_type = dl.TriggerType.RISING_EDGE_SIGNED
    dl.config.trigger_threshold = 0

    with pytest.raises(DataLoggerConfigError) as excinfo:
        dl.activate_trigger()
    assert str(excinfo.value) == "Trigger type specified but no trigger data given in `config.trigger_on`!"


def test_error_missing_trigger_threshold(tmcm1617: TMCM1617Ex):
    """Check if a proper error is raised when trigger is conditional but no trigger threshold is given."""

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    dl.config.log_data = {
        "a": dl.DataTypeAp(index=0),
    }
    dl.config.trigger_type = dl.TriggerType.RISING_EDGE_SIGNED
    dl.config.trigger_on = dl.DataTypeAp(index=0)

    with pytest.raises(DataLoggerConfigError) as excinfo:
        dl.activate_trigger()
    assert str(excinfo.value) == "Trigger type specified is conditional but no threshold given in `config.trigger_threshold!"


def test_info(tmcm1617: TMCM1617Ex):
    """Check if the DataLogger's `get_info` method returns the correct information."""

    dl = tmcm1617.datalogger
    info = dl.get_info()

    assert info.base_frequency_hz == 2000
    assert info.sample_buffer_length == 8192
    assert info.number_of_channels == 4


@pytest.mark.parametrize("download_stepwise", [False, True])
@pytest.mark.parametrize("use_log_data_list", [False, True])
def test_success_unconditional_trigger(tmcm1617: TMCM1617Ex, download_stepwise, use_log_data_list):

    motor = tmcm1617.motors[0]

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    if use_log_data_list:
        group = ParameterGroup("All", ParameterGroup.Category.AXIS, 0)
        dl.config.log_data = [
            Parameter(group, "ADC_I0", motor.AP.AdcPhaseA, Parameter.Access.R, Parameter.Datatype.UNSIGNED),
            Parameter(group, "ADC_I1", motor.AP.AdcPhaseB, Parameter.Access.R, Parameter.Datatype.UNSIGNED),
        ]
    else:
        dl.config.log_data = {
            "ADC_I0": dl.DataTypeAp(index=motor.AP.AdcPhaseA),
            "ADC_I1": dl.DataTypeAp.from_parameter(Parameter(None, None, motor.AP.AdcPhaseB, Parameter.Access.R, Parameter.Datatype.UNSIGNED)),
        }

    dl.activate_trigger()

    while not dl.is_done():
        pass

    if download_stepwise:
        while dl.download_logs_step():
            assert 0.0 < dl.download_progress < 100.0
        assert dl.download_progress == 100.0
    else:
        dl.download_logs()

    for log in [dl.logs["ADC_I0"], dl.logs["ADC_I1"]]:
        assert len(log.samples) == 10
        assert log.rate_hz == 2000
        assert all(30_000 <= sample <= 40_000 for sample in log.samples)
        assert statistics.stdev(log.samples) != 0


@pytest.mark.parametrize("down_sampling_factor", [4, 8, 16, 128])
def test_success_sample_sanity(tmcm1617: TMCM1617Ex, rotate_motor_one_rps, down_sampling_factor):
    motor = tmcm1617.motors[0]

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    dl.config.down_sampling_factor = down_sampling_factor
    dl.config.log_data = {
        "ActualPosition": dl.DataTypeAp(index=motor.AP.ActualPosition),
    }

    dl.activate_trigger()

    while not dl.is_done():
        pass

    dl.download_logs()

    # speed = distance / time
    expected_position_increase_per_sample = motor.get_axis_parameter(motor.AP.PositionScaler) * motor.get_axis_parameter(motor.AP.TargetVelocity) / dl.logs["ActualPosition"].rate_hz / 60
    diff = [dl.logs["ActualPosition"].samples[i] - dl.logs["ActualPosition"].samples[i-1] for i in range(1, len(dl.logs["ActualPosition"].samples))]

    # Check if the motor is rotating in the right direction
    assert all(d >= 0 for d in diff)
    # Check if the position increase per sample is correct
    assert all(abs(d-expected_position_increase_per_sample) < 3 for d in diff)


@pytest.mark.parametrize("use_parameter_class", [False, True])
def test_success_rising_edge_trigger(tmcm1617: TMCM1617Ex, rotate_motor_one_rps, use_parameter_class):
    motor = tmcm1617.motors[0]

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    dl.config.down_sampling_factor = 4
    dl.config.log_data = {
        "ActualPosition": dl.DataTypeAp(index=motor.AP.ActualPosition),
    }
    dl.config.trigger_type = dl.TriggerType.RISING_EDGE_SIGNED
    if use_parameter_class:
        group = ParameterGroup("All", ParameterGroup.Category.AXIS, 0)
        dl.config.trigger_on = Parameter(group, "", motor.AP.ActualPosition, Parameter.Access.R, Parameter.Datatype.SIGNED)
    else:
        dl.config.trigger_on = dl.DataTypeAp(index=motor.AP.ActualPosition)
    dl.config.trigger_threshold = motor.get_axis_parameter(motor.AP.PositionScaler)

    dl.activate_trigger()

    while not dl.is_done():
        pass

    dl.download_logs()

    assert dl.logs["ActualPosition"].samples[0] >= dl.config.trigger_threshold


def test_success_rising_edge_trigger_pretrigger(tmcm1617: TMCM1617Ex, rotate_motor_one_rps):
    motor = tmcm1617.motors[0]

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 1000
    dl.config.down_sampling_factor = 4
    dl.config.log_data = {
        "ActualPosition": dl.DataTypeAp(index=motor.AP.ActualPosition),
    }
    dl.config.trigger_type = dl.TriggerType.RISING_EDGE_SIGNED
    dl.config.trigger_on = dl.DataTypeAp(index=motor.AP.ActualPosition)
    dl.config.trigger_threshold = motor.get_axis_parameter(motor.AP.PositionScaler)
    dl.config.pretrigger_samples = 100

    dl.activate_trigger()

    while not dl.is_done():
        pass

    dl.download_logs()

    expected_position_increase_per_sample = motor.get_axis_parameter(motor.AP.PositionScaler) * motor.get_axis_parameter(motor.AP.TargetVelocity) / dl.logs["ActualPosition"].rate_hz / 60

    expected_first_sample_position = dl.config.trigger_threshold - expected_position_increase_per_sample * dl.config.pretrigger_samples
    assert abs(dl.logs["ActualPosition"].samples[0] - expected_first_sample_position) < expected_position_increase_per_sample


def test_success_copies(tmcm1617: TMCM1617Ex):

    motor = tmcm1617.motors[0]

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10

    dl.config.log_data = {
        "ADC_I0_A": dl.DataTypeAp(index=motor.AP.AdcPhaseA),
        "ADC_I0_B": dl.DataTypeAp(index=motor.AP.AdcPhaseA),
        "ADC_I1_A": dl.DataTypeAp(index=motor.AP.AdcPhaseB),
        "ADC_I1_B": dl.DataTypeAp(index=motor.AP.AdcPhaseB),
        "ADC_I1_C": dl.DataTypeAp(index=motor.AP.AdcPhaseB),
    }

    dl.activate_trigger()

    while not dl.is_done():
        pass

    assert len(dl._effectively_log_data) == 2
    
    dl.download_logs()

    assert all(sample_i0_a == sample_i0_b for sample_i0_a, sample_i0_b in zip(dl.logs["ADC_I0_A"].samples, dl.logs["ADC_I0_B"].samples))
