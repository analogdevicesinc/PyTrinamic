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

    dl.activate_trigger()

    while not dl.is_done():
        pass

    dl.download_logs()

    assert all(sample == 0x34363731 for sample in dl.logs["CHIPINFO_DATA"].samples)
    for adc_channel in ["ADC_IUX", "ADC_IWY", "ADC_IV"]:
        assert len(dl.logs[adc_channel].samples) == 10
        assert all(-1000 <= sample <= 1000 for sample in dl.logs[adc_channel].samples)
        assert statistics.stdev(dl.logs[adc_channel].samples) != 0