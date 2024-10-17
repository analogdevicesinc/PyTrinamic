################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from typing import Union

from pytrinamic.modules import Parameter
from pytrinamic.ic import TMC9660


class TMC9660_eval:
    """Generic class for TMC9660 eval boards."""
    def __init__(self, connection):
        self._connection = connection
        self._ap_index_bit_width = 12
        self._module_id = 1
        self.ics = [TMC9660()]
        
    def get_axis_parameter(self, ap: Union[Parameter, int]):
        return self._connection.get_axis_parameter(ap, 0, index_bit_width=self._ap_index_bit_width)

    def set_axis_parameter(self, ap: Union[Parameter, int], value):
        return self._connection.set_axis_parameter(ap, 0, value, index_bit_width=self._ap_index_bit_width)

    def get_global_parameter(self, gp: Union[Parameter, int], bank):
        return self._connection.get_global_parameter(gp, bank)

    def set_global_parameter(self, gp: Union[Parameter, int], bank, value):
        return self._connection.set_global_parameter(gp, bank, value)
    

class TMC9660_3PH_eval(TMC9660_eval):
    pass


class TMC9660_STEPPER_eval(TMC9660_eval):
    pass