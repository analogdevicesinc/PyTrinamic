################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC4671_eval
from pytrinamic.ic import TMC4671


with ConnectionManager().connect() as my_interface:

    mc_eval = TMC4671_eval(my_interface)

    dl = mc_eval.datalogger

    dl.config.samples_per_channel = 10
    dl.config.log_data = {
        "CHIPINFO_DATA": dl.DataTypeRegister(block=0, channel=0, address=TMC4671.REG.CHIPINFO_DATA),
        "ADC_IV": dl.DataTypeField(block=0, channel=0, field=TMC4671.FIELD.ADC_IWY, signed=True),
    }

    dl.start_logging()

    while not dl.is_capture_complete():
        time.sleep(0.1)

    dl.download_log()

    print([f"0x{sample:x}" for sample in dl.log.data["CHIPINFO_DATA"].samples])
    print(dl.log.data["ADC_IV"].samples)
