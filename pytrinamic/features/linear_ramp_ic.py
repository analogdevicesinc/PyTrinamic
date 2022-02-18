from pytrinamic.features.linear_ramp import LinearRamp


class LinearRampIC(LinearRamp):
    """
    LinearRamp feature implementation for ICs
    """
    def __init__(self, eval_board, ic, axis):
        super().__init__(eval_board, axis)
        self._ic = ic

    def set_max_velocity(self, velocity):
        """
        Sets the maximum positioning velocity of this axis.
        This value is stored in the VMAX field of the IC.

        Parameters:
        velocity: Maximum positioning velocity.
        """
        self._parent.write_axis_field(self._ic.FIELD.VMAX, velocity)

    def get_max_velocity(self):
        """
        Gets the maximum positioning velocity of this axis.
        This value is stored in the VMAX field of the IC.

        Returns: Maximum positioning velocity for this axis.
        """
        return self._parent.read_axis_field(self._ic.FIELD.VMAX)

    def set_max_acceleration(self, acceleration):
        """
        Sets the maximum acceleration of this axis.
        This value is stored in the AMAX field of the IC.

        Parameters:
        acceleration: Maximum acceleration.
        """
        self._parent.write_axis_field(self._ic.FIELD.AMAX, acceleration)

    def get_max_acceleration(self):
        """
        Gets the maximum acceleration of this axis.
        This value is stored in the AMAX field of the IC.

        Returns: Maximum acceleration for this axis.
        """
        return self._parent.read_axis_field(self._ic.FIELD.AMAX)

    # Properties
    max_velocity = property(get_max_velocity, set_max_velocity)
    max_acceleration = property(get_max_acceleration, set_max_acceleration)

    def __str__(self):
        return "{} {}".format(
            "LinearRamp",
            {
                "max_velocity": self.max_velocity,
                "max_acceleration": self.max_acceleration,
            }
        )
