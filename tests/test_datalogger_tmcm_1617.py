################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from typing import Generator
import statistics
import dataclasses
import time

import pytest

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1617
from pytrinamic.modules.tmcl_module import ParameterGroup, Parameter
from pytrinamic.datalogger import DataLogger, DataLoggerConfigError


ENUM = TMCM1617._MotorTypeA.ENUM

class TMCM1617Ex(TMCM1617):

    def __init__(self, connection, module_id=1):
        super().__init__(connection, module_id)
        self.datalogger = DataLogger(connection, module_id)

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
    yield None
    motor.set_axis_parameter(motor.AP.TargetVelocity, 0)
    motor.set_axis_parameter(motor.AP.CommutationMode, ENUM.COMM_MODE_OPENLOOP)


@pytest.fixture
def rotate_motor_one_rps_positive(tmcm1617: TMCM1617Ex, rotate_motor_one_rps):
    motor = tmcm1617.motors[0]
    motor.set_axis_parameter(motor.AP.TargetVelocity, 60)
    yield None


@pytest.fixture
def rotate_motor_one_rps_negative(tmcm1617: TMCM1617Ex, rotate_motor_one_rps):
    motor = tmcm1617.motors[0]
    motor.set_axis_parameter(motor.AP.TargetVelocity, -60)
    yield None


def test_error_no_samples_per_channel_given(tmcm1617: TMCM1617Ex):
    """Check if a proper error is raised when `samples_per_channel` is not given."""

    dl = tmcm1617.datalogger

    dl.config.log_data = {
        "test": dl.DataTypeAp(index=0),
    }

    with pytest.raises(DataLoggerConfigError) as excinfo:
        dl.start_logging()
    assert str(excinfo.value) == "No samples per channel specified via `config.samples_per_channel`!"


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
        dl.start_logging()
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
        dl.start_logging()
    assert str(excinfo.value) == "`config.samples_per_channel` exceeds sample buffer length! You can use 8192 at max."


def test_error_missing_trigger_channel(tmcm1617: TMCM1617Ex):
    """Check if a proper error is raised when trigger is conditional but no trigger data is given."""

    motor = tmcm1617.motors[0]
    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    dl.config.log_data = {
        "a": dl.DataTypeAp(index=0),
    }

    with pytest.raises(TypeError) as excinfo:
        dl.activate_trigger(
            threshold=motor.get_axis_parameter(motor.AP.PositionScaler),
            edge=dl.TriggerEdge.RISING,
        )


def test_error_missing_trigger_threshold(tmcm1617: TMCM1617Ex):
    """Check if a proper error is raised when trigger is conditional but no trigger threshold is given."""

    motor = tmcm1617.motors[0]
    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    dl.config.log_data = {
        "a": dl.DataTypeAp(index=0),
    }

    with pytest.raises(TypeError) as excinfo:
        dl.activate_trigger(
            on_data=dl.DataTypeAp(index=motor.AP.ActualPosition, axis=0, signed=True),
            edge=dl.TriggerEdge.RISING,
        )


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

    dl.start_logging()

    dl.wait_till_done()

    if download_stepwise:
        while dl.download_log_step():
            assert 0.0 < dl.download_progress < 100.0
        assert dl.download_progress == 100.0
    else:
        dl.download_log()

    assert dl.log.rate_hz == 2000
    for name, log in dl.log.data.items():
        assert len(log.samples) == 10
        assert all(30_000 <= sample <= 40_000 for sample in log.samples)
        assert statistics.stdev(log.samples) != 0
        if use_log_data_list:
            assert log.request_object == next(param for param in dl.config.log_data if param.name == name)
        else:
            assert log.request_object == dl.config.log_data[name]


@pytest.mark.parametrize("down_sampling_factor", [4, 8, 16, 128])
def test_success_sample_sanity(tmcm1617: TMCM1617Ex, rotate_motor_one_rps_positive, down_sampling_factor):
    motor = tmcm1617.motors[0]

    dl = tmcm1617.datalogger
    base_sample_frequency_hz = dl.get_info().base_frequency_hz

    dl.config.samples_per_channel = 10
    dl.config.down_sampling_factor = down_sampling_factor
    dl.config.log_data = {
        "ActualPosition": dl.DataTypeAp(index=motor.AP.ActualPosition),
    }

    dl.start_logging()

    dl.wait_till_done()

    dl.download_log()

    assert dl.log.rate_hz == base_sample_frequency_hz / down_sampling_factor

    # speed = distance / time
    expected_position_increase_per_sample = motor.get_axis_parameter(motor.AP.PositionScaler) * motor.get_axis_parameter(motor.AP.TargetVelocity) / dl.log.data["ActualPosition"].rate_hz / 60
    diff = [dl.log.data["ActualPosition"].samples[i] - dl.log.data["ActualPosition"].samples[i-1] for i in range(1, len(dl.log.data["ActualPosition"].samples))]

    # Check if the motor is rotating in the right direction
    assert all(d >= 0 for d in diff)
    # Check if the position increase per sample is correct
    assert all(abs(d-expected_position_increase_per_sample) < 3 for d in diff)


@pytest.mark.parametrize("use_parameter_class", [False, True])
def test_success_rising_edge_trigger(tmcm1617: TMCM1617Ex, rotate_motor_one_rps_positive, use_parameter_class):
    motor = tmcm1617.motors[0]

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    dl.config.down_sampling_factor = 4
    dl.config.log_data = {
        "ActualPosition": dl.DataTypeAp(index=motor.AP.ActualPosition, axis=0, signed=True),
    }
    if use_parameter_class:
        group = ParameterGroup("All", ParameterGroup.Category.AXIS, 0)
        trigger_on = Parameter(group, "", motor.AP.ActualPosition, Parameter.Access.R, Parameter.Datatype.SIGNED)
    else:
        trigger_on = dl.DataTypeAp(index=motor.AP.ActualPosition, axis=0, signed=True)

    threshold = motor.get_axis_parameter(motor.AP.PositionScaler)
    dl.activate_trigger(
        on_data=trigger_on,
        threshold=threshold,
        edge=dl.TriggerEdge.RISING,
    )

    dl.wait_till_done()

    dl.download_log()

    assert dl.log.data["ActualPosition"].samples[0] >= threshold


def test_success_falling_edge_trigger(tmcm1617: TMCM1617Ex, rotate_motor_one_rps_negative):
    motor = tmcm1617.motors[0]

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 10
    dl.config.down_sampling_factor = 4
    dl.config.log_data = {
        "ActualPosition": dl.DataTypeAp(index=motor.AP.ActualPosition, axis=0, signed=True),
    }

    threshold = -motor.get_axis_parameter(motor.AP.PositionScaler)

    dl.activate_trigger(
        on_data=dl.DataTypeAp(index=motor.AP.ActualPosition, axis=0, signed=True),
        threshold=threshold,
        edge=dl.TriggerEdge.FALLING,
    )
    start_time = time.perf_counter()

    dl.wait_till_done()

    delay_seconds = time.perf_counter() - start_time

    dl.download_log()

    assert dl.log.data["ActualPosition"].samples[0] <= threshold
    
    expected_delay_seconds = threshold * 60 / motor.get_axis_parameter(motor.AP.PositionScaler) / motor.get_axis_parameter(motor.AP.TargetVelocity, signed=True)
    assert abs(delay_seconds - expected_delay_seconds) < 0.1


def test_success_rising_edge_trigger_pretrigger(tmcm1617: TMCM1617Ex, rotate_motor_one_rps_positive):
    motor = tmcm1617.motors[0]

    dl = tmcm1617.datalogger

    dl.config.samples_per_channel = 200
    dl.config.down_sampling_factor = 4
    dl.config.log_data = {
        "ActualPosition": dl.DataTypeAp(index=motor.AP.ActualPosition, axis=0, signed=True),
    }

    threshold = motor.get_axis_parameter(motor.AP.PositionScaler)
    pretrigger_samples = 100

    dl.activate_trigger(
        on_data=dl.DataTypeAp(index=motor.AP.ActualPosition, axis=0, signed=True),
        threshold=threshold,
        edge=dl.TriggerEdge.RISING,
        pretrigger_samples=pretrigger_samples,
    )

    dl.wait_till_done()

    dl.download_log()

    expected_position_increase_per_sample = motor.get_axis_parameter(motor.AP.PositionScaler) * motor.get_axis_parameter(motor.AP.TargetVelocity) / dl.log.rate_hz / 60

    expected_first_sample_position = threshold - expected_position_increase_per_sample * pretrigger_samples
    assert abs(dl.log.data["ActualPosition"].samples[0] - expected_first_sample_position) < expected_position_increase_per_sample


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

    dl.start_logging()

    dl.wait_till_done()

    assert len(dl._effectively_log_data) == 2
    
    dl.download_log()

    assert all(sample_i0_a == sample_i0_b for sample_i0_a, sample_i0_b in zip(dl.log.data["ADC_I0_A"].samples, dl.log.data["ADC_I0_B"].samples))


@pytest.mark.parametrize("sample_frequency_hz,expected_down_sampling_factor", [(500.0, 4), (125.0, 16), (100.0, 20)])
def test_success_sample_sanity(tmcm1617: TMCM1617Ex, sample_frequency_hz, expected_down_sampling_factor):

    dl = tmcm1617.datalogger

    dl.config.set_sample_rate(sample_frequency_hz)
    assert dl.config.down_sampling_factor == expected_down_sampling_factor
