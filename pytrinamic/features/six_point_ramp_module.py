from pytrinamic.features.six_point_ramp import SixPointRamp


class SixPointRampModule(SixPointRamp):
    """
    SixPointRamp feature implementation
    """
    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps

    def set_ramp_type(self, ramp_type):
        """
        Sets if Ramp that is used for this axis.
        This value is stored as RampType axis parameter.

        Parameters:
        ramp_type: ramp type value
        """
        self._parent.set_axis_parameter(self._aps.RampType, self._axis, ramp_type)

    def get_ramp_type(self):
        """
        Gets if Ramp that is used for this axis.
        This value is stored in the  RampType axis parameter.

        Returns: ramp type
        """
        return self._parent.get_axis_parameter(self._aps.RampType, self._axis)

    def set_start_velocity(self, start_velocity):
        """
        Sets start velocity used for this axis.
        This value is stored as StartVelocity axis parameter.

        Parameters:
        start_velocity: start velocity
        """
        self._parent.set_axis_parameter(self._aps.StartVelocity, self._axis, start_velocity)

    def get_start_velocity(self):
        """
        Gets start velocity used for this axis.
        This value is stored as StartVelocity axis parameter.

        Returns: start velocity
        """
        return self._parent.get_axis_parameter(self._aps.StartVelocity, self._axis)

    def set_start_acceleration(self, start_acceleration):
        """
        Sets start acceleration used for this axis.
        This value is stored as StartAcceleration axis parameter.

        Parameters:
        start_acceleration: start acceleration
        """
        self._parent.set_axis_parameter(self._aps.StartAcceleration, self._axis, start_acceleration)

    def get_start_acceleration(self):
        """
        Gets start acceleration used for this axis.
        This value is stored as StartAcceleration axis parameter.

        Returns: start acceleration
        """
        return self._parent.get_axis_parameter(self._aps.StartAcceleration, self._axis)

    def set_max_deceleration(self, max_deceleration):
        """
        Sets maximum deceleration used for this axis.
        This value is stored as MaxDeceleration axis parameter.

        Parameters:
        max_deceleration: maximum deceleration
        """
        self._parent.set_axis_parameter(self._aps.MaxDeceleration, self._axis, max_deceleration)

    def get_max_deceleration(self):
        """
        Gets maximum deceleration used for this axis.
        This value is stored as MaxDeceleration axis parameter.

        Returns: maximum deceleration
        """
        return self._parent.get_axis_parameter(self._aps.MaxDeceleration, self._axis)

    def set_break_velocity(self, break_velocity):
        """
        Sets break velocity used for this axis.
        This value is stored as BreakVelocity axis parameter.

        Parameters:
        break_velocity: break velocity
        """
        self._parent.set_axis_parameter(self._aps.BreakVelocity, self._axis, break_velocity)

    def get_break_velocity(self):
        """
        Gets break velocity used for this axis.
        This value is stored as BreakVelocity axis parameter.

        Returns: break velocity
        """
        return self._parent.get_axis_parameter(self._aps.BreakVelocity, self._axis)

    def set_final_deceleration(self, final_deceleration):
        """
        Sets final deceleration used for this axis.
        This value is stored as FinalDeceleration axis parameter.

        Parameters:
        final_deceleration: final deceleration
        """
        self._parent.set_axis_parameter(self._aps.FinalDeceleration, self._axis, final_deceleration)

    def get_final_deceleration(self):
        """
        Gets final deceleration used for this axis.
        This value is stored as FinalDeceleration axis parameter.

        Returns: final deceleration
        """
        return self._parent.get_axis_parameter(self._aps.FinalDeceleration, self._axis)

    def set_stop_velocity(self, stop_velocity):
        """
        Sets stop velocity used for this axis.
        This value is stored as StopVelocity axis parameter.

        Parameters:
        stop_velocity: stop velocity
        """
        self._parent.set_axis_parameter(self._aps.StopVelocity, self._axis, stop_velocity)

    def get_stop_velocity(self):
        """
        Gets stop velocity used for this axis.
        This value is stored as StopVelocity axis parameter.

        Returns: stop velocity
        """
        return self._parent.get_axis_parameter(self._aps.StopVelocity, self._axis)

    def set_stop_deceleration(self, stop_deceleration):
        """
        Sets stop deceleration used for this axis.
        This value is stored as StopDeceleration axis parameter.

        Parameters:
        stop_deceleration: stop deceleration
        """
        self._parent.set_axis_parameter(self._aps.StopDeceleration, self._axis, stop_deceleration)

    def get_stop_deceleration(self):
        """
        Gets stop deceleration used for this axis.
        This value is stored as StopDeceleration axis parameter.

        Returns: stop deceleration
        """
        return self._parent.get_axis_parameter(self._aps.StopDeceleration, self._axis)

    # Properties
    ramp_type = property(get_ramp_type, set_ramp_type)
    start_velocity = property(get_start_velocity, set_start_velocity)
    start_acceleration = property(get_start_acceleration, set_start_acceleration)
    max_deceleration = property(get_max_deceleration, set_max_deceleration)
    break_velocity = property(get_break_velocity, set_break_velocity)
    final_deceleration = property(get_final_deceleration, set_final_deceleration)
    stop_velocity = property(get_stop_velocity, set_stop_velocity)
    stop_deceleration = property(get_stop_deceleration, set_stop_deceleration)

    def __str__(self):
        return "{} {}".format(
            "SixPointRamp",
            {
                "ramp_type": self.ramp_type,
                "start_velocity": self.start_velocity,
                "start_acceleration": self.start_acceleration,
                "max_deceleration": self.max_deceleration,
                "break_velocity": self.break_velocity,
                "final_deceleration": self.final_deceleration,
                "stop_velocity": self.stop_velocity,
                "stop_deceleration": self.stop_deceleration,
            }
        )
