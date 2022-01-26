class TMCLModule(object):

    def __init__(self, connection, module_id=1):
        """
        Constructor for the module instance.

        Parameters:
        connection: TMCL connection interface object.
        module_id: Module ID to identify the module. This is used to differentiate
        between different modules on shared busses. Default is set to 1, different
        values have to be configured with the module first.
        """
        self.connection = connection
        self.module_id = module_id
        self.name = ""
        self.desc = ""
        self.motors = []

    def list_features(self):
        """
        Lists all compatible feature classes for all axes of this module.

        Returns: Unified list of features of all axes.
        """
        features = list()
        for motor in self.motors:
            features.append(motor.list_features())
        return features

    def __str__(self):
        features = ""
        # for feature in self.list_features():
        #    features += str(feature) + ", "
        # features = features[1:]
        # features = features[:-3]
        return "{} {}".format(
                self.name,
                {
                    "module_id": self.module_id,
                    "features": features
                }
        )

    def set_axis_parameter(self, ap_type, axis, value):
        """
        Sets the axis parameter for the given axis of this module identified by type to the given value.

        Parameters:
        type: Axis parameter type. These can be retrieved from the APs class of the corresponding axis.
        axis: Axis index for the parameter to be set.
        value: Value to set the axis parameter to.
        """
        self.connection.set_axis_parameter(ap_type, axis, value, self.module_id)

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
        return self.connection.get_axis_parameter(ap_type, axis, self.module_id, signed=signed)

    def set_global_parameter(self, gp_type, bank, value):
        """
        Sets the global parameter on this module identified by type to the given value.

        Parameters:
        type: Global parameter type. These can be retrieved from the GPs class of this module.
        bank: Bank number for the parameter to be set.
        value: Value to set the global parameter to.
        """
        self.connection.set_global_parameter(gp_type, bank, value, self.module_id)

    def get_global_parameter(self, gp_type, bank, signed=False):
        """
        Gets the global parameter on this module identified by type.

        Parameters:
        type: Global parameter type. These can be retrieved from the GPs class of this module.
        bank: Bank number for the parameter to be set.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: Global parameter value.
        """
        return self.connection.get_global_parameter(gp_type, bank, self.module_id, signed=signed)

    def get_analog_input(self, x):
        """
        Gets the analog input value identified by index x.

        Parameters:
        x: Analog input index.

        Returns: Analog input value.
        """
        return self.connection.get_analog_input(x, self.module_id)

    def get_digital_input(self, x):
        """
        Gets the digital input value identified by index x.

        Parameters:
        x: Digital input index.

        Returns: Digital input value.
        """
        return self.connection.get_digital_input(x, self.module_id)

    def get_digital_output(self, x):
        """
        Gets the digital output value identified by index x.

        Parameters:
        x: Digital output index.

        Returns: Digital output value.
        """
        return self.connection.get_digital_output(x, self.module_id)

    " write outputs "
    def set_digital_output(self, x):
        """
        Sets the digital output value identified by index x.

        Parameters:
        x: Digital output index.
        """
        return self.connection.set_digital_output(x, self.module_id)

    def clear_digital_output(self, x):
        """
        Clears the digital output identified by index x.

        Parameters:
        x: Digital output index.
        """
        return self.connection.clear_digital_output(x, self.module_id)
