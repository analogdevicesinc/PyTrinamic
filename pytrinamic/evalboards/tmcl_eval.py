from pytrinamic.helpers import TMC_helpers

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
        return self.write_register(field[0], TMC_helpers.field_set(self.read_register(field[0]),
                                   field[1], field[2], value))

    def read_register_field(self, field):
        return TMC_helpers.field_get(self.read_register(field[0]), field[1], field[2])

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
        return TMC_helpers.to_signed_32(value) if signed else value

    def __str__(self):
        return "{} {}".format(
                self.name,
                {
                    "module_id": self._module_id
                }
        )
