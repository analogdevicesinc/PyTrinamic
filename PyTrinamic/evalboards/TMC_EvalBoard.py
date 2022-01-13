# Created on: 06.07.2021
# Author: LK

from PyTrinamic.modules.tmcl_module import tmcl_module
from PyTrinamic.helpers import TMC_helpers


class TMC_EvalBoard(tmcl_module):
    "General Trinamic EvalBoard implementation"

    class EVAL_TYPES:
        "EvalBoard types"
        MOTION_CONTROLLER = 0
        DRIVER = 1
        UNDEFINED = 2

    def __init__(self, connection, module_id, ic, eval_type):
        """
        Constructor for the evalboard instance.

        Parameters:
        connection: TMCL connection interface instance.
        module_id: Module ID to identify the module. This is used to differentiate
        between different modules on shared busses. Default is set to 1, different
        values have to be configured with the module first.
        ic: IC instance used on this evalboard.
        eval_type: Type of this evalboard. Available types can be retrieved from
        the EVAL_TYPES class.
        """
        super().__init__(connection, module_id)
        self.IC = ic
        self.eval_type = eval_type

    def write_register(self, channel, address, value):
        """
        Writes the given value to the register identified by the given address.
        Register access commands will be invoked via TMCL for evalboards.
        Register addresses can be retrieved from the REGISTERS class of the ic.

        Parameters:
        channel: Channel of the IC to write to. For evalboards this is implemented
        in different write commands and only depends on the eval_type. Thus, this
        parameter can be just have 'None' value.
        address: Register address to write to.
        value: Value to write to the register.

        Returns: TMCL reply.
        """
        del channel
        return {
            self.EVAL_TYPES.MOTION_CONTROLLER: self.connection.writeMC,
            self.EVAL_TYPES.DRIVER: self.connection.writeDRV,
            self.EVAL_TYPES.UNDEFINED: self.connection.writeMC
        }.get(self.eval_type)(address, value, moduleID=self.module_id)

    def read_register(self, channel, address, signed=False):
        """
        Reads the value from the register identified by the given address.
        Register access commands will be invoked via TMCL for evalboards.
        Register addresses can be retrieved from the REGISTERS class of the ic.

        Parameters:
        channel: Channel of the IC to write to. For evalboards this is implemented
        in different write commands and only depends on the eval_type. Thus, this
        parameter can be just have 'None' value.
        address: Register address to write to.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: TMCL reply.
        """
        del channel
        return {
            self.EVAL_TYPES.MOTION_CONTROLLER: self.connection.readMC,
            self.EVAL_TYPES.DRIVER: self.connection.readDRV,
            self.EVAL_TYPES.UNDEFINED: self.connection.readMC
        }.get(self.eval_type)(address, moduleID=self.module_id, signed=signed)

    def write_register_field(self, channel, field, value):
        """
        Writes the given value to the given register field.
        Register access commands will be invoked via TMCL for evalboards.
        Register fields are subdivisions of registers and thus identified by
        register address, bitmask and shift count.
        Register fields can be retrieved from the FIELDS class of the ic.

        channel: Channel of the IC to write to. For evalboards this is implemented
        in different write commands and only depends on the eval_type. Thus, this
        parameter can be just have 'None' value.
        field: Register field to write to.
        value: Value to write to the register field.

        Returns: TMCL reply.
        """
        del channel
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]), field[1], field[2], value))

    def read_register_field(self, channel, field):
        """
        Reads the value from the given register field.
        Register access commands will be invoked via TMCL for evalboards.
        Register fields are subdivisions of registers and thus identified by
        register address, bitmask and shift count.
        Register fields can be retrieved from the FIELDS class of the ic.

        channel: Channel of the IC to write to. For evalboards this is implemented
        in different write commands and only depends on the eval_type. Thus, this
        parameter can be just have 'None' value.
        field: Register field to read from.

        Returns: TMCL reply.
        """
        del channel
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])
