from pytrinamic.features.current import Current


class CurrentIC(Current):
    """
    Current feature implementation for ICs
    """
    def __init__(self, eval_board, ic, axis):
        super().__init__(eval_board, axis)
        self._ic = ic

    def set_run_current(self, current):
        """
        Sets the run current of this axis.
        This value is stored in the IRUN field of the IC.

        Parameters:
        value: Target run current.
        """
        self._parent.write_axis_field(self._ic.FIELD.IRUN, current)

    def get_run_current(self):
        """
        Gets the run current of this axis.
        This value is stored in the IRUN field of the IC.

        Returns: Run current for this axis.
        """
        return self._parent.read_axis_field(self._ic.FIELD.IRUN)

    def set_standby_current(self, current):
        """
        Sets the standby current of this axis.
        This value is stored in the IHOLD field of the IC.

        Parameters:
        value: Target standby current.
        """
        self._parent.write_axis_field(self._ic.FIELD.IHOLD, current)

    def get_standby_current(self):
        """
        Gets the standby current of this axis.
        This value is stored in the IHOLD field of the IC.

        Returns: Standby current for this axis.
        """
        return self._parent.read_axis_field(self._ic.FIELD.IHOLD)

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
