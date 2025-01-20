################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
"""Demo on how to read and write digital IOs.

In order for the output to work, the following configuration has to be changed in the ioconfig_tmc9660-3ph-eval.toml file:
```toml
[gpio18]
type          = "output"    # "input", "output", "analog" (optional) (analog only supported on GPIO 2-5)
output_value  = true        # false, true (optional)
```

On Windows the config upload and app start can be done with:
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> write config ubltools_1.0.1/ioconfig_tmc9660-3ph-eval.toml
    python ubltools_1.0.1/ubl_evalsystem_wrapper.py <COM-PORT> start
Where <COM-PORT> needs to be replaced by the COM port of the Landungsbruecke.

Important: first connect USB and then power the TMC9660-3PH-EVAL.

                            +-----+  +-------------------+     
                     USB    |     |==|                   |     
                     -------|     |==|                   |        
Connected to the machine    |     |==|                   |     
running this script.        |LB   |==|TMC9660-3PH-EVAL   |     
                            +-----+  +-------------------+

"""

from pytrinamic.connections import ConnectionManager
from pytrinamic.ic import TMC9660
from pytrinamic.evalboards import TMC9660_3PH_eval


cm = ConnectionManager()

with cm.connect() as my_interface:

    tmc9660_device = TMC9660_3PH_eval(my_interface)

    # Get the state of the digital input GPIO17
    print(f"GPIO17: {tmc9660_device.get_digital_input(17)}")
    print(f"GPIO17: {tmc9660_device.get_digital_input(TMC9660.IO.GPIO17)}")

    # Set the digital output GPIO18 to True and then to False
    tmc9660_device.set_digital_output(18, True)
    tmc9660_device.set_digital_output(TMC9660.IO.GPIO18, False)
