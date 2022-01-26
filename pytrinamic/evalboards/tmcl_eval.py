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

    def __str__(self):
        return "{} {}".format(
                self.name,
                {
                    "module_id": self._module_id
                }
        )
