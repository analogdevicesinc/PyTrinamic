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


@pytest.fixture(scope="module")
def eval_interface():
    with ConnectionManager().connect() as my_interface:
        yield my_interface


@pytest.fixture(scope="function")
def tmc4671_eval(eval_interface) -> Generator[TMC4671_eval, None, None]:
    eval = TMC4671_eval(eval_interface)
    yield eval


def test_datalogger_eval_4671(tmc4671_eval: TMC4671_eval):

    dl = tmc4671_eval.datalogger

    dl.config.samples_per_channel = 10
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