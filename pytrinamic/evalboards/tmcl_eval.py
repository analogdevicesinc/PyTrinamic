################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
import typing

from pytrinamic.helpers import BitField
from pytrinamic.ic import Register, Field, Access, Choice

class TMCLEval(object):

    def __init__(self, connection, module_id=1):
        """
        Constructor for the module instance.

        Parameters:
        connection: TMCL connection interface object.
        module_id: Module ID to identify the module. This is used to differentiate
        between different modules on shared busses. Default is set to 1, different
        values have to be configured with the module first.
        """
        self._connection = connection
        self._module_id = module_id
        self.name = ""
        self.desc = ""
        self.motors = []

    def set_axis_parameter(self, ap_type, axis, value):
        """
        Sets the axis parameter for the given axis of this module identified by type to the given value.

        Parameters:
        type: Axis parameter type. These can be retrieved from the APs class of the corresponding axis.
        axis: Axis index for the parameter to be set.
        value: Value to set the axis parameter to.
        """
        self._connection.set_axis_parameter(ap_type, axis, value, self._module_id)

    def get_axis_parameter(self, ap_type, axis, signed=False):
        """
        Gets the axis parameter for the given axis of this module identified by type.

        Parameters:
        type: Axis parameter type. These can be retrieved from the APs class of this axis.
        axis: Axis index for the parameter to get from.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: Axis parameter value.
        """
        return self._connection.get_axis_parameter(ap_type, axis, self._module_id, signed=signed)

    def write_register_field(self, field, value):
        return self.write_register(field[0], BitField.field_set(self.read_register(field[0]),
                                                                field[1], field[2], value))

    def read_register_field(self, field):
        return BitField.field_get(self.read_register(field[0]), field[1], field[2])

    def read_register(self, register_address, signed=False):
        raise NotImplementedError

    def write_register(self, register_address, value):
        raise NotImplementedError

    def read(self, read_target: typing.Union[Register, Field]) -> int:
        """
        Generic read function, will branch out to private read functions.

        read_target: This is the main differentiating argument:
                       - If read_target is a Register object, we do a register read.
                       - If read_target is a Field object, we do a field read.
        """
        if isinstance(read_target, Field):
            # Our target variable is a Field, we do field read in that case
            register_address = read_target.parent.address
            signed = bool(read_target.signed)
            register_content = self.read_register(register_address, signed=signed)

            value = (register_content & read_target.mask) >> read_target.shift
            if signed:
                base_mask = read_target.mask >> read_target.shift
                sign_mask = base_mask & (~base_mask >> 1)
                value = (value ^ sign_mask) - sign_mask
            return value

        elif isinstance(read_target, Register):
            # Our target has the attributes of a register, we do register read in that case
            signed = bool(read_target.signed)
            register_address = read_target.address
            return self.read_register(register_address, signed=signed)

        else:
            raise ValueError(
                f"Argument read_target {read_target} does not appear to be either a Register, or a Field."
            )

    def write(self, write_target: typing.Union[Register, Field, Choice], value: typing.Union[int, bool] = None, *, omit_bounds_check=False, omit_permission_checks=False) -> int:
        """
        Generic write functions, will branch out to private write functions.

        write_target: This is the main differentiating argument:
                       - If write_target is a Choice object, we do a field write.
                       - If write_target is a Field object, we do a field write.
                       - If write_target is a Register object, we do a register write.
        """
        if isinstance(write_target, Choice) and (value == None):
            # Our target variable is a Choice, we do a choice write in that case
            return self.write(write_target.parent, write_target.value)
        if isinstance(write_target, Field) and isinstance(value, int):
            # Our target variable is a Field, we do field read in that case

            if not omit_permission_checks:
                if not write_target.access.is_writable():
                    raise PermissionError(f"Field {write_target.name} has no write permission!!")

            if not omit_bounds_check:
                if not write_target.is_in_bounds(value):
                    raise ValueError(f"Input value {value} is not in the allowed value range!")

            if write_target.access == Access.RWC:
                register_content_new = (value << write_target.shift) & write_target.mask
                self.write_register(write_target.parent.address, register_content_new)
                return register_content_new

            register_address = write_target.parent.address
            register_content_old = self.read_register(register_address)
            register_content_new = (register_content_old & ~write_target.mask) | (value << write_target.shift)
            self.write_register(register_address, register_content_new)
            return register_content_new

        elif isinstance(write_target, Register) and isinstance(value, int):
            # Our target has the attributes of a register, we do register write in that case

            if not omit_permission_checks:
                if not write_target.access.is_writable():
                    raise PermissionError(f"Register {write_target.name} has no write permission!!")

            if not omit_bounds_check:
                if not write_target.is_in_bounds(value):
                    raise ValueError(f"Input value {value} is not in the allowed value range!")

            register_address = write_target.address
            return self.write_register(register_address, value)

        else:
            raise ValueError(
                f"Argument write_target {write_target} does not appear to be either a Register, Field or Choice, or the value is invalid."
            )


    def write_axis_field(self, axis, field, value):
        """
        Writes the given value to the axis-dependent register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.

        Parameters:
        field: Base register field for any axis.
        value: Value to write to the target register field for this axis.
        """
        return self.write_register_field(field[axis] if type(field) == list else field, value)

    def read_axis_field(self, axis, field, signed=False):
        """
        Reads the value of the axis-dependent register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.

        Parameters:
        field: Base register field for any axis.

        Returns: Value of the target register field for the given axis.
        """
        value = self.read_register_field(field[axis] if type(field) == list else field)
        return BitField.to_signed_32(value) if signed else value

    def __str__(self):
        return "{} {}".format(
                self.name,
                {
                    "module_id": self._module_id
                }
        )
