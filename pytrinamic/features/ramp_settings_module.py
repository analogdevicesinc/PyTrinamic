from ramp_settings import RampSettings


class RampSettingsModule(RampSettings):

    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps
        self._hasRampEnable = False

        if hasattr(self._aps, "EnableRamp"):
            self._hasRampEnable = True

    def set_ramp_type(self, ramp_type):
        """
        Selects the ramp type to linear or sine ramp
        This value is stored as RampType axis parameter.

        Parameters:
        ramp_type: Ramp Type.
        """
        self._parent.set_axis_parameter(self._aps.RampType, self._axis, ramp_type)

    def get_ramp_type(self):
        """
        Gets the current ramp type
        This value is stored as RampType axis parameter.

        Returns: Current selected ramp type
        """
        return self._parent.get_axis_parameter(self._aps.RampType, self._axis)

    def set_max_velocity(self, velocity):
        """
        Sets the maximum positioning velocity of this axis.
        This value is stored as MaxVelocity axis parameter.

        Parameters:
        velocity: Maximum positioning velocity.
        """
        self._parent.set_axis_parameter(self._aps.MaxVelocity, self._axis, velocity)

    def get_max_velocity(self):
        """
        Gets the maximum positioning velocity of this axis.
        This value is stored as MaxVelocity axis parameter.

        Returns: Maximum positioning velocity for this axis.
        """
        return self._parent.get_axis_parameter(self._aps.MaxVelocity, self._axis)

    def set_max_acceleration(self, acceleration):
        """
        Sets the maximum acceleration of this axis.
        This value is stored as MaxAcceleration axis parameter.

        Parameters:
        acceleration: Maximum acceleration.
        """
        self._parent.set_axis_parameter(self._aps.MaxAcceleration, self._axis, acceleration)

    def get_max_acceleration(self):
        """
        Gets the maximum acceleration of this axis.
        This value is stored as MaxAcceleration axis parameter.

        Returns: Maximum acceleration for this axis.
        """
        return self._parent.get_axis_parameter(self._aps.MaxAcceleration, self._axis)

    def set_ramp_enabled(self, enabled):
        """
        Sets if ramp is enabled for this axis.
        This value is stored as EnableRamp axis parameter.

        Parameters:
        enabled: ramp enable
        """
        if self._hasRampEnable:
            self._parent.set_axis_parameter(self._aps.EnableRamp, self._axis, enabled)

    def get_ramp_enabled(self):
        """
        Gets if ramp is enabled for this axis.
        This value is stored as EnableRamp axis parameter.

        Returns: ramp enable
        """
        if self._hasRampEnable:
            return self._parent.get_axis_parameter(self._aps.EnableRamp, self._axis)
        else:
            return None

    # Properties
    ramp_type = property(get_ramp_type, set_ramp_type)
    max_velocity = property(get_max_velocity, set_max_velocity)
    max_acceleration = property(get_max_acceleration, set_max_acceleration)
    enabled = property(get_ramp_enabled, set_ramp_enabled)

    def __str__(self):
        return "{} {}".format(
            "RampSettings",
            {
                "ramp_type": self.ramp_type,
                "max_velocity": self.max_velocity,
                "max_acceleration": self.max_acceleration,
                "enable": self.enabled
            }
        )
