from abc import ABC, abstractmethod


class StallGuard2(ABC):
    """
    StallGuard2 feature implementation
    """
    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_filter(self, enable_filter):
        """
        Enable/Disable hardware StallGuard2 filter.

        Parameters:
        filter:
        0 - Disable StallGuard2 filter
        1 - Enable StallGuard2 filter
        """
        raise NotImplementedError

    @abstractmethod
    def get_filter(self):
        """
        Gets the StallGuard2 filter status.

        Parameters:

        Returns:
        0 - StallGuard2 filter disabled
        1 - StallGuard2 filter enabled
        """
        raise NotImplementedError

    @abstractmethod
    def set_threshold(self, threshold):
        """
        Sets the StallGuard2 threshold / sensibility.

        Parameters:
        threshold: StallGuard2 threshold. Default 0. Lower values mean higher sensibility.
        """
        raise NotImplementedError

    @abstractmethod
    def get_threshold(self):
        """
        Gets the StallGuard2 threshold / sensibility.

        Parameters:

        Returns: StallGuard2 threshold.
        """
        raise NotImplementedError

    @abstractmethod
    def set_stop_velocity(self, velocity):
        """
        Sets the minimum velocity, at which stop on stall becomes active.
        Value of 0 will disable the stop.

        Parameters:
        velocity: Velocity threshold.
        """
        raise NotImplementedError

    @abstractmethod
    def get_stop_velocity(self):
        """
        Gets the minimum velocity, at which stop on stall becomes active.
        Value of 0 will disable the stop.

        Parameters:

        Returns: Velocity threshold.
        """
        raise NotImplementedError

    @abstractmethod
    def get_load_value(self):
        """
        Gets the load value for monitoring smart energy current scaling or automatic current scaling.
        This value is stored as LoadValue axis parameter.

        Returns: LoadValue
        """
        raise NotImplementedError
