################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""Example that shows how to download a TMCL script to the TMCL scrip memory of a TMCM-1636.

TMCL scripts are stored non-volatile with the download.
"""

import time

from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1636
from pytrinamic.tmcl import TMCLCommand


connection_manager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")

with connection_manager.connect() as my_interface:
    module = TMCM1636(my_interface)
    motor = module.motors[0]

    module.connection.send(TMCLCommand.START_DOWNLOAD_MODE, 0, 0, 0)

    # The following commands will not be executed but are load into the TMCL script memory of the module.
    # Notice that the parameter for the jump command is the index of the command to jump to.
    # Here the JA jumps to [1] which is "ROR 0, 500".
    module.connection.send(TMCLCommand.SAP, motor.AP.CommutationMode, 0, 3)  # [0] SAP 15, 0, 4
                                                                             #     Loop:
    module.connection.send(TMCLCommand.ROR, 0, 0, 500)                       # [1]     ROR 0, 500
    module.connection.send(TMCLCommand.WAIT, 0, 0, 100)                      # [2]     WAIT TICKS, 0, 100
    module.connection.send(TMCLCommand.ROR, 0, 0, -500)                      # [3]     ROR 0, -500
    module.connection.send(TMCLCommand.WAIT, 0, 0, 100)                      # [4]     WAIT TICKS, 0, 100
    module.connection.send(TMCLCommand.JA, 0, 0, 1)                          # [5]     JA Loop

    module.connection.send(TMCLCommand.QUIT_DOWNLOAD_MODE, 0, 0, 0)

    module.connection.send(TMCLCommand.RESET_APPLICATION, 0, 0, 0)
    module.connection.send(TMCLCommand.RUN_APPLICATION, 0, 0, 0)

    time.sleep(5)  # Wait some time to execute the TMCL script.

    module.connection.send(TMCLCommand.STOP_APPLICATION, 0, 0, 0)

    motor.stop()  # Even though the script stopped we need to stop the motor.
