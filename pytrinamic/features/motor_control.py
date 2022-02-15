from abc import ABC, abstractmethod


class MotorControl(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def move_to(self, position, velocity=None):
        raise NotImplementedError()

    @abstractmethod
    def move_by(self, distance, velocity=None):
        raise NotImplementedError()

    @abstractmethod
    def rotate(self, velocity):
        raise NotImplementedError()

    @abstractmethod
    def stop(self):
        raise NotImplementedError()

    @abstractmethod
    def set_target_position(self, position):
        """
        Sets the target position of this axis.

        Parameters:
        position: Target position.
        """
        raise NotImplementedError

    @abstractmethod
    def get_target_position(self):
        """
        Gets the target position of this axis.

        Parameters:
        Returns: Target position for this axis.
        """
        raise NotImplementedError

    @abstractmethod
    def set_actual_position(self, position):
        """
        Sets the actual position of this axis.

        Parameters:
        position: Actual position.
        """
        raise NotImplementedError

    @abstractmethod
    def get_actual_position(self):
        """
        Gets the actual position of this axis.

        Parameters:

        Returns: Actual position for this axis.
        """
        raise NotImplementedError

    @abstractmethod
    def set_target_velocity(self, velocity):
        """
        Sets the target velocity of this axis.

        Parameters:
        velocity: Target velocity.
        """
        raise NotImplementedError

    @abstractmethod
    def get_target_velocity(self):
        """
        Gets the target velocity of this axis.

        Parameters:

        Returns: Target velocity for this axis.
        """
        raise NotImplementedError

    @abstractmethod
    def get_actual_velocity(self):
        """
        Gets the actual velocity of this axis.

        Parameters:

        Returns: Actual velocity for this axis.
        """
        raise NotImplementedError
