################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import logging

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import MAX22216
from pytrinamic.RAMDebug import Channel, RAMDebug, RAMDebug_Trigger

logging.basicConfig(level=logging.DEBUG)
pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    ch = Channel.field(0, MAX22216.FIELD.ADC_VM_RAW, signed=True, eval_channel=1)
    trigger = Channel.field(0, MAX22216.FIELD.ADC_VM_RAW, signed=True, eval_channel=1)

    debug = RAMDebug(my_interface)
    debug.set_channel(ch)
    debug.set_trigger_type(RAMDebug_Trigger.TRIGGER_UNCONDITIONAL)
    debug.set_trigger_threshold(50)
    debug.start_measurement()

    while not debug.is_measurement_done():
        pass

    samples = debug.get_samples()

print("\nDone.")
