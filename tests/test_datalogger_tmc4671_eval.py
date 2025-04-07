################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from typing import Generator
import statistics

import pytest

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import TMC4671
from pytrinamic.ic.tmc_ic import RegisterGroup, Register, Field, Access


@pytest.fixture(scope="module")
def eval_interface():
    with ConnectionManager().connect() as my_interface:
        yield my_interface


@pytest.fixture(scope="function")
def tmc4671_eval(eval_interface) -> Generator[TMC4671_eval, None, None]:
    eval = TMC4671_eval(eval_interface)
    yield eval


@pytest.mark.parametrize("use_log_data_list", [False, True])
def test_datalogger_eval_4671(tmc4671_eval: TMC4671_eval, use_log_data_list):

    dl = tmc4671_eval.datalogger

    dl.config.samples_per_channel = 10
    if use_log_data_list:
        all_register = RegisterGroup(name="All", channel=0, block=None, width=None)
        adc_iwy_iux = Register(name="ADC_IWY_IUX", parent=all_register, access=Access.R, address=TMC4671.REG.ADC_IWY_IUX)
        adc_iv = Register(name="ADC_IV", parent=all_register, access=Access.R, address=TMC4671.REG.ADC_IV)
        dl.config.log_data = [
            Register(name="CHIPINFO_DATA", parent=all_register, access=Access.R, address=TMC4671.REG.CHIPINFO_DATA),
            Field(name="ADC_IUX", parent=adc_iwy_iux, access=Access.R, mask=TMC4671.FIELD.ADC_IUX[1], shift=TMC4671.FIELD.ADC_IUX[2], signed=True),
            Field(name="ADC_IWY", parent=adc_iwy_iux, access=Access.R, mask=TMC4671.FIELD.ADC_IWY[1], shift=TMC4671.FIELD.ADC_IWY[2], signed=True),
            Field(name="ADC_IV", parent=adc_iv, access=Access.R, mask=TMC4671.FIELD.ADC_IV[1], shift=TMC4671.FIELD.ADC_IV[2], signed=True),
        ]
    else:
        dl.config.log_data = {
            "CHIPINFO_DATA": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.CHIPINFO_DATA),
            "ADC_IUX": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.ADC_IUX, signed=True),
            "ADC_IWY": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.ADC_IWY, signed=True),
            "ADC_IV": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.ADC_IV, signed=True),
        }

    dl.start_capture()

    dl.wait_for_capture_completion()

    dl.download_log()

    assert all(sample == 0x34363731 for sample in dl.log.data["CHIPINFO_DATA"].samples)
    if use_log_data_list:
        adc_channels = ["ADC_IWY_IUX.ADC_IUX", "ADC_IWY_IUX.ADC_IWY", "ADC_IV.ADC_IV"]
    else:
        adc_channels = ["ADC_IUX", "ADC_IWY", "ADC_IV"]

    for adc_channel in adc_channels:
        assert len(dl.log.data[adc_channel].samples) == 10
        assert statistics.stdev(dl.log.data[adc_channel].samples) != 0


def test_datalogger_eval_4671_register_copy(tmc4671_eval: TMC4671_eval):

    dl = tmc4671_eval.datalogger

    dl.config.samples_per_channel = 10

    dl.config.log_data = {
        "CHIPINFO_DATA_0": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.CHIPINFO_DATA),
        "CHIPINFO_DATA_1": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.CHIPINFO_DATA),
        "CHIPINFO_DATA_2": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.CHIPINFO_DATA),
        "CHIPINFO_DATA_3": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.CHIPINFO_DATA),
        "CHIPINFO_DATA_4": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.CHIPINFO_DATA),
    }

    dl.start_capture()

    dl.wait_for_capture_completion()

    dl.download_log()

    for i in range(len(dl.config.log_data)):
        assert all(sample == 0x34363731 for sample in dl.log.data[f"CHIPINFO_DATA_{i}"].samples)


def test_datalogger_eval_4671_field_reduction(tmc4671_eval: TMC4671_eval):

    tmc4671_eval.write_register_field(TMC4671.FIELD.N_POLE_PAIRS, 0x5A5A)
    tmc4671_eval.write_register_field(TMC4671.FIELD.MOTOR_TYPE, 3)
    tmc4671_eval.write_register_field(TMC4671.FIELD.HALL_POLARITY, 1)
    tmc4671_eval.write_register_field(TMC4671.FIELD.HALL_INTERPOLATION, 0)
    tmc4671_eval.write_register_field(TMC4671.FIELD.HALL_DIRECTION, 0)
    tmc4671_eval.write_register_field(TMC4671.FIELD.HALL_HALL_BLANK, 1)

    dl = tmc4671_eval.datalogger

    dl.config.samples_per_channel = 10

    dl.config.log_data = {
        "MOTOR_TYPE_N_POLE_PAIRS": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.MOTOR_TYPE_N_POLE_PAIRS),
        "N_POLE_PAIRS": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.N_POLE_PAIRS),
        "MOTOR_TYPE": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.MOTOR_TYPE),
        "HALL_POLARITY": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.HALL_POLARITY),
        "HALL_INTERPOLATION": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.HALL_INTERPOLATION),
        "HALL_DIRECTION": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.HALL_DIRECTION),
        "HALL_HALL_BLANK": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.HALL_HALL_BLANK),
    }

    dl.start_capture()

    dl.wait_for_capture_completion()

    assert len(dl._effectively_log_data) == 2
    dl.download_log()

    assert all(sample == 0x00035A5A for sample in dl.log.data[f"MOTOR_TYPE_N_POLE_PAIRS"].samples)
    assert all(sample == 0x5A5A for sample in dl.log.data[f"N_POLE_PAIRS"].samples)
    assert all(sample == 0x3 for sample in dl.log.data[f"MOTOR_TYPE"].samples)
    assert all(sample == 1 for sample in dl.log.data[f"HALL_POLARITY"].samples)
    assert all(sample == 0 for sample in dl.log.data[f"HALL_INTERPOLATION"].samples)
    assert all(sample == 0 for sample in dl.log.data[f"HALL_DIRECTION"].samples)
    assert all(sample == 1 for sample in dl.log.data[f"HALL_HALL_BLANK"].samples)