from PyTrinamic.features.Feature import Feature


class Current(Feature):
    "Current feature implementation"

    def get_current_run(self, axis):
        """
        Gets the run current of the given axis.

        Parameters:
        axis: Axis index.

        Returns: Run current for the given axis.
        """
        raise NotImplementedError()

    def set_current_run(self, axis, value):
        """
        Sets the run current of the given axis.

        Parameters:
        axis: Axis index.
        value: Value of the run current. This value is hardware specific, please refer
        to the documentation of the hardware.
        """
        raise NotImplementedError()

    def get_current_standby(self, axis):
        """
        Gets the standby current of the given axis.

        Parameters:
        axis: Axis index.

        Returns: Standby current for the given axis.
        """
        raise NotImplementedError()

    def set_current_standby(self, axis, value):
        """
        Sets the standby current of the given axis.

        Parameters:
        axis: Axis index.
        value: Value of the standby current. This value is hardware specific, please refer
        to the documentation of the hardware.
        """
        raise NotImplementedError()

    def __str__(self):
        return "{} {}".format(
            "Current",
            {
                "run": self.run,
                "standby": self.standby
            }
        )

    # Properties
    run = property(get_current_run, set_current_run)
    standby = property(get_current_standby, set_current_standby)
