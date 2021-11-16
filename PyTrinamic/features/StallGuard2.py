# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.Feature import Feature

class StallGuard2(Feature):
    "StallGuard2 feature implementation"

    def set_filter(self, axis, filter):
        """
        Enable/Disable hardware StallGuard2 filter.

        Parameters:
        axis: Axis index.
        filter:
        0 - Disable StallGuard2 filter
        1 - Enable StallGuard2 filter
        """
        raise NotImplementedError()

    def set_threshold(self, axis, threshold):
        """
        Sets the StallGuard2 threshold / sensibility.

        Parameters:
        axis: Axis index.
        threshold: StallGuard2 threshold. Default 0. Lower values mean higher sensibility.
        """
        raise NotImplementedError()

    def set_stop_velocity(self, axis, velocity):
        """
        Sets the minimum velocity, at which stop on stall becomes active.
        Value of 0 will disable the stop.

        Parameters:
        axis: Axis index.
        velocity: Velocity threshold.
        """
        raise NotImplementedError()

    def get_filter(self, axis):
        """
        Gets the StallGuard2 filter status.

        Parameters:
        axis: Axis index.

        Returns:
        0 - StallGuard2 filter disabled
        1 - StallGuard2 filter enabled
        """
        raise NotImplementedError()

    def get_threshold(self, axis):
        """
        Gets the StallGuard2 threshold / sensibility.

        Parameters:
        axis: Axis index.

        Returns: StallGuard2 threshold.
        """
        raise NotImplementedError()

    def get_stop_velocity(self, axis):
        """
        Gets the minimum velocity, at which stop on stall becomes active.
        Value of 0 will disable the stop.

        Parameters:
        axis: Axis index.

        Returns: Velocity threshold.
        """
        raise NotImplementedError()
    
    def get_load_value(self):
        """
        Gets the load value for monitoring smart energy current scaling or automatic current scaling.
        This value is stored as LoadValue axis parameter.

        Returns: LoadValue
        """
        raise NotImplementedError()
    
    def __str__(self):
        return "{} {}".format(
            "StallGuard2",
            {
                "filter": self.filter,
                "threshold": self.threshold,
                "stop_velocity": self.stop_velocity
            }
        )

    # Properties
    filter = property(get_filter, set_filter)
    threshold = property(get_threshold, set_threshold)
    stop_velocity = property(get_stop_velocity, set_stop_velocity)
