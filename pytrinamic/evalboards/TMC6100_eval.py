################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.evalboards import TMCLEval
from pytrinamic.ic import TMC6100


class TMC6100_eval(TMCLEval):
    """
    Use TMC6100-EVAL with Landungsbrücke/Startrampe at DRV spi channel to access the TMC6100.
    """
    def __init__(self, connection, module_id=1):
        TMCLEval.__init__(self, connection, module_id)
        self.ics = [TMC6100()]

    # use Landungsbrücke/Startrampe with DRV channel for register access

    def write_register(self, register_address, value):
        return self._connection.write_drv(register_address, value, self._module_id)

    def read_register(self, register_address, signed=False):
        return self._connection.read_drv(register_address, self._module_id, signed)
