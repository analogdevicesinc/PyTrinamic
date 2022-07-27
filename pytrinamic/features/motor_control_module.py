from ..features.motor_control import MotorControl


class MotorControlModule(MotorControl):

    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps

    def move_to(self, position, velocity=None):
        self._parent.move_to(self._axis, position, velocity)

    def move_by(self, difference, velocity=None):
        self._parent.move_by(self._axis, difference, velocity)

    def rotate(self, velocity):
        self._parent.rotate(self._axis, velocity)

    def stop(self):
        self._parent.stop(self._axis)

    def set_target_position(self, position):
        """
        Sets the target position of this axis.
        This value is stored as TargetPosition axis parameter.

        Parameters:
        position: Target position.
        """
        self._parent.set_axis_parameter(self._aps.TargetPosition, self._axis, position)

    def get_target_position(self):
        """
        Gets the target position of this axis.
        This value is stored as TargetPosition axis parameter.

        Returns: Target position for this axis.
        """
        return self._parent.get_axis_parameter(self._aps.TargetPosition, self._axis, True)

    def set_actual_position(self, position):
        """
        Sets the actual position of this axis.
        This value is stored as ActualPosition axis parameter.

        Parameters:
        position: Actual position.
        """
        self._parent.set_axis_parameter(self._aps.ActualPosition, self._axis, position)

    def get_actual_position(self):
        """
        Gets the actual position of this axis.
        This value is stored as ActualPosition axis parameter.

        Returns: Actual position for this axis.
        """
        return self._parent.get_axis_parameter(self._aps.ActualPosition, self._axis, True)

    def set_target_velocity(self, velocity):
        """
        Sets the target velocity of this axis.
        This value is stored as TargetVelocity axis parameter.

        Parameters:
        velocity: Target velocity.
        """
        self._parent.set_axis_parameter(self._aps.TargetVelocity, self._axis, velocity)

    def get_target_velocity(self):
        """
        Gets the target velocity of this axis.
        This value is stored as TargetVelocity axis parameter.

        Returns: Target velocity for this axis.
        """
        return self._parent.get_axis_parameter(self._aps.TargetVelocity, self._axis, True)

    def get_actual_velocity(self):
        """
        Gets the actual velocity of this axis.
        This value is stored as ActualVelocity axis parameter.

        Returns: Actual velocity for this axis.
        """
        return self._parent.get_axis_parameter(self._aps.ActualVelocity, self._axis, True)

    # module specific functions

    def set_axis_parameter(self, ap_type, value):
        """
        Sets the axis parameter for this axis identified by type to the given value.

        Parameters:
        ap_type: Axis parameter type. These can be retrieved from the APs class of this axis.
        value: Value to set the axis parameter to.
        """
        self._parent.set_axis_parameter(ap_type, self._axis, value)

    def get_axis_parameter(self, ap_type, signed=False):
        """
        Gets the axis parameter for this axis identified by type.

        Parameters:
        ap_type: Axis parameter type. These can be retrieved from the APs class of this axis.
        signed: Indicates whether the value should be interpreted as signed or not.
        By default, this is False, so the value will be interpreted as unsigned.

        Returns: Axis parameter value.
        """
        return self._parent.get_axis_parameter(ap_type, self._axis, signed)

    def get_status_flags(self):
        """
        Gets the status flags for this axis.

        Returns: Status flags.
        """
        return self._parent.get_axis_parameter(self._aps.StatusFlags)

    def get_error_flags(self):
        """
        Gets the error flags for this axis.

        Returns: Error flags.
        """
        return self._parent.get_axis_parameter(self._aps.ErrorFlags)

    # Properties
    target_position = property(get_target_position, set_target_position)
    actual_position = property(get_actual_position, set_actual_position)
    target_velocity = property(get_target_velocity, set_target_velocity)
    actual_velocity = property(get_actual_velocity)

    def __str__(self):
        return "{} {}".format(
            "MotorControl",
            {
                "motor": self._axis,
                "target_position": self.target_position,
                "actual_position": self.actual_position,
                "target_velocity": self.target_velocity,
                "actual_velocity": self.actual_velocity
            }
        )
