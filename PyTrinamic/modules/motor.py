class Motor(object):
    """
    TMCL compatible motor instance.
    """
    def __init__(self, module, axis):
        """
        Constructor for the TMCL motor instance.

        Parameters:
        module: Module object this motor is part of.
        axis: Axis index of this motor.
        """
        self.module = module
        self.axis = axis

    def set_axis_parameter(self, ap_type, value):
        """
        Sets the axis parameter for this axis identified by type to the given value.

        Parameters:
        ap_type: Axis parameter type. These can be retrieved from the APs class of this axis.
        value: Value to set the axis parameter to.
        """
        self.module.set_axis_parameter(ap_type, self.axis, value)

    def get_axis_parameter(self, ap_type, signed=False):
        """
        Gets the axis parameter for this axis identified by type.

        Parameters:
        ap_type: Axis parameter type. These can be retrieved from the APs class of this axis.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: Axis parameter value.
        """
        return self.module.get_axis_parameter(ap_type, self.axis, signed)

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
