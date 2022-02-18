from abc import ABC, abstractmethod


class LinearRamp(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_max_velocity(self, velocity):
        """
        Sets the maximum positioning velocity of this axis.

        Parameters:
        axis: Axis index.
        velocity: Maximum positioning velocity.
        """
        raise NotImplementedError

    @abstractmethod
    def get_max_velocity(self):
        """
        Gets the maximum positioning velocity of this axis.

        Parameters:
        axis: Axis index.

        Returns: Maximum positioning velocity for this axis.
        """
        raise NotImplementedError

    @abstractmethod
    def set_max_acceleration(self, acceleration):
        """
        Sets the maximum acceleration of this axis.

        Parameters:
        axis: Axis index.
        acceleration: Maximum acceleration.
        """
        raise NotImplementedError

    @abstractmethod
    def get_max_acceleration(self):
        """
        Gets the maximum acceleration of this axis.

        Parameters:
        axis: Axis index.

        Returns: Maximum acceleration for this axis.
        """
        raise NotImplementedError
