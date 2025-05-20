################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.evalboards import MAX22216_eval
from pytrinamic.datalogger import DataLogger


with ConnectionManager().connect() as my_interface:

    eval = MAX22216_eval(my_interface)

    dl = DataLogger(my_interface)

    eval.write_register_field(MAX22216.FIELD.ACTIVE, 1)

    dl.config.samples_per_channel = 10
    dl.config.log_data = {
        "ADC_VM_MEASUREMENT": dl.DataTypeRegister(block=0, channel=1, address=MAX22216.REG.ADC_VM_MEASUREMENT),
    }

    dl.start_capture()

    dl.wait_for_capture_completion()

    dl.download_log()

    print(dl.log.data["ADC_VM_MEASUREMENT"].samples)
