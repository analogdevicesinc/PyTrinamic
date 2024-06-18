################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Copy the settings of axis 0 write them to axis 0 and store the settings in non-volatile memory.

* Requires firmware version 1.0

"""

import dataclasses

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM2611


@dataclasses.dataclass
class Parameter:
    name: str
    index: int
    signed: bool


aps = [
    Parameter("Motor pole pairs", 0, False),
    Parameter("Maximum current", 1, False),
    Parameter("Open loop current", 2, False),
    Parameter("Motor direction", 3, False),
    Parameter("Commutation mode", 4, False),
    Parameter("Motor PWM frequency", 6, False),
    Parameter("ADC I0 offset", 10, True),
    Parameter("ADC I1 offset", 11, True),
    Parameter("Torque P", 20, False),
    Parameter("Torque I", 21, False),
    Parameter("Velocity P", 22, False),
    Parameter("Velocity I", 23, False),
    Parameter("Position P", 24, False),
    Parameter("Velocity P scaler", 25, False),
    Parameter("Velocity I scaler", 26, False),
    Parameter("Position P scaler", 27, False),
    Parameter("Maximum velocity", 40, False),
    Parameter("Acceleration", 41, False),
    Parameter("Enable velocity ramp", 50, False),
    Parameter("Velocity filter", 51, False),
    Parameter("Motor halted velocity", 53, False),
    Parameter("Position reached distance", 54, False),
    Parameter("Position reached velocity", 55, False),
    Parameter("Position scaler", 56, False),
    Parameter("Enable velocity feed forward", 57, False),
    Parameter("Velocity meter counter limit", 58, False),
    Parameter("Hall polarity", 60, False),
    Parameter("Hall direction", 61, False),
    Parameter("Hall interpolation", 62, False),
    Parameter("Hall phi_e offset", 63, True),
    Parameter("Encoder steps", 70, False),
    Parameter("Encoder direction", 71, False),
    Parameter("Encoder init mode", 72, False),
    Parameter("Encoder init delay", 73, False),
    Parameter("Encoder init velocity", 74, True),
    Parameter("Encoder offset", 76, False),
    Parameter("Brake release duty cycle", 81, False),
    Parameter("Brake release duration", 82, False),
    Parameter("Brake holding duty cycle", 83, False),
    Parameter("Thermal winding time constant 1", 110, False),
    Parameter("IIt limit 1", 111, False),
    Parameter("Thermal winding time constant 2", 113, False),
    Parameter("IIt limit 2", 114, False),
]

connection_manager = ConnectionManager()

with connection_manager.connect() as my_interface:
    module = TMCM2611(my_interface)

    for ap in aps:
        value_axis_0 = module.get_axis_parameter(ap.index, 0, ap.signed)
        module.set_axis_parameter(ap.index, 1, value_axis_0)
        module.store_axis_parameter(ap.index, 1)

    print("Done")
