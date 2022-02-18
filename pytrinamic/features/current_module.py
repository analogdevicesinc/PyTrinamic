from pytrinamic.features.current import Current


class CurrentModule(Current):
    """
    Current feature implementation for modules
    """
    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps

    def set_run_current(self, current):
        """
        Sets the run current of this axis.
        This value is stored as RunCurrent axis parameter.

        Parameters:
        value: Target run current.
        """
        self._parent.set_axis_parameter(self._aps.RunCurrent, current)

    def get_run_current(self):
        """
        Gets the run current of this axis.
        This value is stored as RunCurrent axis parameter.

        Returns: Run current for this axis.
        """
        return self._parent.get_axis_parameter(self._aps.RunCurrent)

    def set_standby_current(self, current):
        """
        Sets the standby current of this axis.
        This value is stored as StandbyCurrent axis parameter.

        Parameters:
        value: Target standby current.
        """
        self._parent.set_axis_parameter(self._aps.StandbyCurrent, current)

    def get_standby_current(self):
        """
        Gets the standby current of this axis.
        This value is stored as StandbyCurrent axis parameter.

        Returns: Standby current for this axis.
        """
        return self._parent.get_axis_parameter(self._aps.StandbyCurrent)

    # Properties
    run = property(get_run_current, set_run_current)
    standby = property(get_standby_current, set_standby_current)

    def __str__(self):
        return "{} {}".format(
            "Current",
            {
                "run": self.run,
                "standby": self.standby
            }
        )
