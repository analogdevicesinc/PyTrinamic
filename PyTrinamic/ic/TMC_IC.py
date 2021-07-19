# Created on: 06.07.2021
# Author: LK

from PyTrinamic.helpers import TMC_helpers

class TMC_IC(object):
    "General Trinamic IC implementation"

    class Motor(object):
        "Trinamic IC motor class"

        def __init__(self, ic, axis):
            """
            Constructor for a Trinamic IC motor instance.

            Parameters:
            ic: IC instance.
            axis: Axis index of this motor.
            """
            self.ic = ic
            self.axis = axis

        def write_axis_field(self, field, value):
            """
            Writes the given value to the axis-dependend register field.
            On multi-axis ICs, this wraps the process of resolving the actual target
            register field to be used for the given axis, when multiple fields with
            same meaning for different axes are available.

            Parameters:
            field: Base register field for any axis.
            value: Value to write to the target register field for this axis.
            """
            return self.ic.write_axis_field(self.axis, field, value)

        def read_axis_field(self, field):
            """
            Reads the value of the axis-dependend register field.
            On multi-axis ICs, this wraps the process of resolving the actual target
            register field to be used for the given axis, when multiple fields with
            same meaning for different axes are available.

            Parameters:
            field: Base register field for any axis.

            Returns: Value of the target register field for this axis.
            """
            return self.ic.read_axis_field(self.axis, field)

    def __init__(self, handler, channel):
        """
        Constructor for the TMC_IC instance.

        Parameters:
        handler: Handler object for register access operations.
        This object is expected to implement write_register and read_register functions
        to read/write registers via platform-specific communication.
        channel: Channel identifier for this IC. This will be handed to the
        write_register and read_register functions of the handler to differentiate
        between multiple ICs.
        """
        self.handler = handler
        self.channel = channel

    def write_register(self, address, value):
        """
        Writes the given value to the register identified by the given address.
        This wraps the handlers write_register function.

        Parameters:
        address: Register address to write to.
        value: Value to write to the register.

        Returns: Return value of the handlers write_register function.
        """
        return self.handler.write_register(self.channel, address, value)

    def read_register(self, address, signed=False):
        """
        Reads the value of the register identified by the given address.
        This wraps the handlers read_register function.

        Parameters:
        address: Register address to read from.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: Register value.
        """
        return self.handler.read_register(self.channel, address, signed)

    def write_register_field(self, field, value):
        """
        Writes the given value to the given register field.
        This will implicitly invoke write_register and read_register functions.
        Register fields are subdivisions of registers and thus identified by
        register address, bitmask and shift count.
        Register fields can be retrieved from the FIELDS class.

        field: Register field to write to.
        value: Value to write to the register field.

        Returns: Return value of the handlers write_register function.
        """
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]), field[1], field[2], value))

    def read_register_field(self, field):
        """
        Read the value from the given register field.
        This will implicitly invoke write_register and read_register functions.
        Register fields are subdivisions of registers and thus identified by
        register address, bitmask and shift count.
        Register fields can be retrieved from the FIELDS class.

        field: Register field to read from.

        Returns: Register field value.
        """
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

    # write and read wrappers for field access with respect to axis.
    # These are used in feature implementations for the motors.
    # Base field is used to identify what to access. With given axis the
    # actual field to be accessed can be resolved for multi-axis ICs in the implementation of this
    # wrapper functions within the IC class.

    def write_axis_field(self, axis, field, value):
        """
        Writes the given value to the axis-dependend register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.

        Parameters:
        axis: Axis index.
        field: Base register field for any axis.
        value: Value to write to the target register field for this axis.
        """
        raise NotImplementedError()

    def read_axis_field(self, axis, field):
        """
        Reads the value of the axis-dependend register field.
        On multi-axis ICs, this wraps the process of resolving the actual target
        register field to be used for the given axis, when multiple fields with
        same meaning for different axes are available.

        Parameters:
        axis: Axis index.
        field: Base register field for any axis.

        Returns: Value of the target register field for the given axis.
        """
        raise NotImplementedError()
