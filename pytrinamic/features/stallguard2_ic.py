from pytrinamic.features.stallguard2 import StallGuard2


class StallGuard2IC(StallGuard2):
    """
    StallGuard2 feature implementation for ICs
    """

    def __init__(self, eval_board, ic, axis):
        super().__init__(eval_board, axis)
        self._ic = ic

    def set_filter(self, enable_filter):
        """
        Enable/Disable hardware StallGuard2 filter.
        This value is stored in the SFILT field of the IC.

        Parameters:
        filter:
        0 - Disable StallGuard2 filter
        1 - Enable StallGuard2 filter
        """
        self._parent.write_axis_field(self._ic.FIELD.SFILT, enable_filter)

    def get_filter(self):
        """
        Gets the StallGuard2 filter status.
        This value is stored in the SFILT field of the IC.

        Returns:
        0 - StallGuard2 filter disabled
        1 - StallGuard2 filter enabled
        """
        return self._parent.read_axis_field(self._ic.FIELD.SFILT)

    def set_threshold(self, threshold):
        """
        Sets the StallGuard2 threshold / sensibility.
        This value is stored in the SGT field of the IC.

        Parameters:
        threshold: StallGuard2 threshold. Default 0. Lower values mean higher sensibility.
        """
        self._parent.write_axis_field(self._ic.FIELD.SGT, threshold)

    def get_threshold(self):
        """
        Gets the StallGuard2 threshold / sensibility.
        This value is stored in the SGT field of the IC.

        Returns: StallGuard2 threshold.
        """
        return self._parent.read_axis_field(self._ic.FIELD.SGT)

    def set_stop_velocity(self, velocity):
        """
        Sets the minimum velocity, at which stop on stall becomes active.
        Value of 0 will disable the stop.
        This will become enabled by setting the SG_STOP field of the IC.
        This value is stored in the TCOOLTHRS field of the IC.

        Parameters:
        velocity: Velocity threshold.
        """
        self._parent.write_axis_field(self._ic.FIELD.SG_STOP, int(min(velocity, 1)))
        velocity = int(min(0xFFFFF, int((1 << 24) / max(1, velocity))))
        self._parent.write_axis_field(self._ic.FIELD.TCOOLTHRS, velocity)

    def get_stop_velocity(self):
        """
        Gets the minimum velocity, at which stop on stall becomes active.
        Value of 0 will disable the stop.
        This will become enabled by setting the SG_STOP field of the IC.
        This value is stored in the TCOOLTHRS field of the IC.

        Returns: Velocity threshold.
        """
        velocity = self._parent.read_axis_field(self._ic.FIELD.TCOOLTHRS)
        return int(min(0xFFFFF, int((1 << 24) / max(1, velocity))))

    def get_load_value(self):
        return self._parent.read_axis_field(self._ic.FIELD.SG_RESULT)

    # Properties
    filter = property(get_filter, set_filter)
    threshold = property(get_threshold, set_threshold)
    stop_velocity = property(get_stop_velocity, set_stop_velocity)
    load_value = property(get_load_value)

    def __str__(self):
        return "{} {}".format(
            "StallGuard2",
            {
                "filter": self.filter,
                "threshold": self.threshold,
                "stop_velocity": self.stop_velocity
            }
        )
