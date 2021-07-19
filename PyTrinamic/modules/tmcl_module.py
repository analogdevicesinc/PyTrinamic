'''
Created on 24.03.2021

@author: LK
'''

class tmcl_module(object):

    class Motor(object):
        "TMCL compatible motor instance."

        def __init__(self, module, axis):
            """
            Constructor for the TMCL motor instance.

            Parameters:
            module: Module object this motor is part of.
            axis: Axis index of this motor.
            """
            self.module = module
            self.axis = axis

        def set_axis_parameter(self, type, value):
            """
            Sets the axis parameter for this axis identified by type to the given value.

            Parameters:
            type: Axis parameter type. These can be retrieved from the APs class of this axis.
            value: Value to set the axis parameter to.
            """
            self.module.set_axis_parameter(type, self.axis, value)

        def get_axis_parameter(self, type, signed=False):
            """
            Gets the axis parameter for this axis identified by type.

            Parameters:
            type: Axis parameter type. These can be retrieved from the APs class of this axis.
            signed: Indicates whether the value should be interpreted as signed or not.
            By default, this is False, so the value will be interpreted as unsigned.

            Returns: Axis parameter value.
            """
            return self.module.get_axis_parameter(type, self.axis, signed)

        def get_status_flags(self):
            """
            Gets the status flags for this axis.

            Returns: Status flags.
            """
            return self.get_axis_parameter(self.APs.StatusFlags)

        def get_error_flags(self):
            """
            Gets the error flags for this axis.

            Returns: Error flags.
            """
            return self.get_axis_parameter(self.APs.ErrorFlags)

    def __init__(self, connection, module_id=1):
        """
        Constructor for the module instance.

        Parameters:
        connection: TMCL connection interface object.
        module_id: Module ID to identify the module. This is used to differentiate
        between different modules on shared busses. Default is set to 1, different
        values have to be configured with the module first.
        """
        self.MOTORS = 0
        self.connection = connection
        self.module_id = module_id
        self.name = ""
        self.desc = ""

    def list_features(self):
        """
        Lists all compatible feature classes for all axes of this module.

        Returns: Unified list of features of all axes.
        """
        features = list()
        for motor in self.MOTORS:
            features.append(motor.list_features())
        return features

    def __str__(self):
        return "{}\{module_id={}\}".format(self.name, self.module_id)

    def showModuleInfo(self):
        print(self)

    def set_axis_parameter(self, type, axis, value):
        """
        Sets the axis parameter for the given axis of this module identified by type to the given value.

        Parameters:
        type: Axis parameter type. These can be retrieved from the APs class of the corresponding axis.
        axis: Axis index for the parameter to be set.
        value: Value to set the axis parameter to.
        """
        self.connection.setAxisParameter(type, axis, value, self.module_id)

    def get_axis_parameter(self, type, axis, signed=False):
        """
        Gets the axis parameter for the given axis of this module identified by type.

        Parameters:
        type: Axis parameter type. These can be retrieved from the APs class of this axis.
        axis: Axis index for the parameter to get from.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: Axis parameter value.
        """
        return self.connection.axisParameter(type, axis, self.module_id, signed=signed)

    def setGlobalParameter(self, type, bank, value):
        """
        Sets the global parameter on this module identified by type to the given value.

        Parameters:
        type: Global parameter type. These can be retrieved from the GPs class of this module.
        bank: Bank number for the parameter to be set.
        value: Value to set the global parameter to.
        """
        self.connection.setGlobalParameter(type, bank, value, self.module_id)

    def globalParameter(self, type, bank, signed=False):
        """
        Gets the global parameter on this module identified by type.

        Parameters:
        type: Global parameter type. These can be retrieved from the GPs class of this module.
        bank: Bank number for the parameter to be set.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: Global parameter value.
        """
        return self.connection.globalParameter(type, bank, self.module_id, signed=signed)

    def analogInput(self, x):
        """
        Gets the analog input value identified by index x.

        Parameters:
        x: Analog input index.

        Returns: Analog input value.
        """
        return self.connection.analogInput(x, self.moduleID)

    def digitalInput(self, x):
        """
        Gets the digital input value identified by index x.

        Parameters:
        x: Digital input index.

        Returns: Digital input value.
        """
        return self.connection.digitalInput(x, self.moduleID)

    def digitalOutput(self, x):
        """
        Gets the digital output value identified by index x.

        Parameters:
        x: Digital output index.

        Returns: Digital output value.
        """
        return self.connection.digitalOutput(x, self.moduleID)

    " write outputs "
    def setDigitalOutput(self, x):
        """
        Sets the digital output value identified by index x.

        Parameters:
        x: Digital output index.
        """
        return self.connection.setDigitalOutput(x, self.moduleID)

    def clearDigitalOutput(self, x):
        """
        Clears the digital output identified by index x.

        Parameters:
        x: Digital output index.
        """
        return self.connection.clearDigitalOutput(x, self.moduleID)
