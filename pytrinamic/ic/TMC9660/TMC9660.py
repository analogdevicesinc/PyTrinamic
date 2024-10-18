################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from typing import Union

from ...ic.tmc_ic import TMCIc, UblApiDevice
from ...modules import Parameter
from ...tmcl import TMCLCommand

from .TMC9660_ap import Ap
from .TMC9660_bank0 import Bank0
from .TMC9660_bank2 import Bank2
from .TMC9660_bank3 import Bank3

class TMC9660(TMCIc, UblApiDevice):
    """
    """
    ap = Ap()
    gp_bank0 = Bank0()
    gp_bank2 = Bank2()
    gp_bank3 = Bank3()
    
    def __init__(self, connection=None, module_id=0):
        """You only need a module ID if you have multiple TMC9660 ICs on a shared RS485 bus."""

        super().__init__("TMC9660", self.__doc__)
        self._connection = connection
        self.ap_index_bit_width = 12
        self.module_id = module_id

    # Implementation of UblApiDevice-write_register
    def write_register(self, register_address, block, value):
        return self._connection.write_register(register_address, TMCLCommand.WRITE_MC, block, value, self._module_id)

    # Implementation of UblApiDevice-read_register
    def read_register(self, register_address, block, signed=False):
        return self._connection.read_register(register_address, TMCLCommand.READ_MC, block, self._module_id, signed)
    
    def get_axis_parameter(self, ap: Union[Parameter, int]):
        return self._connection.get_axis_parameter(ap, 0, self.module_id, index_bit_width=self.ap_index_bit_width)

    def set_axis_parameter(self, ap: Union[Parameter, int], value):
        return self._connection.set_axis_parameter(ap, 0, value, self.module_id, self.ap_index_bit_width)

    def get_global_parameter(self, gp: Union[Parameter, int], bank):
        return self._connection.get_global_parameter(gp, bank, self.module_id)

    def set_global_parameter(self, gp: Union[Parameter, int], bank, value):
        return self._connection.set_global_parameter(gp, bank, value, self.module_id)