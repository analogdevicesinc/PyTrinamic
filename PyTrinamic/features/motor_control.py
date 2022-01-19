from abc import ABC, abstractmethod


class MotorControl(ABC):

    # velocity mode

    def set_axis_parameter(self, ap_type, value):
        raise NotImplementedError

    def get_axis_parameter(self, ap_type, signed=False):
        raise NotImplementedError

    def rotate(self, velocity):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()

    # position mode

    def move_to(self, position, velocity=None):
        raise NotImplementedError()

    def move_by(self, difference, velocity=None):
        raise NotImplementedError()

    @abstractmethod
    def get_target_position(self):
        """
        Gets the target position of this axis.

        Parameters:
        axis: Axis index.

        Returns: Target position for this axis.
        """
        raise NotImplementedError

    @abstractmethod
    def set_target_position(self, position):
        """
        Sets the target position of this axis.

        Parameters:
        axis: Axis index.
        position: Target position.
        """
        raise NotImplementedError

    @abstractmethod
    def get_actual_position(self):
        """
        Gets the actual position of this axis.

        Parameters:
        axis: Axis index.

        Returns: Actual position for this axis.
        """
        raise NotImplementedError

    @abstractmethod
    def set_actual_position(self, position):
        """
        Sets the actual position of this axis.

        Parameters:
        axis: Axis index.
        position: Actual position.
        """
        raise NotImplementedError

    @abstractmethod
    def get_target_velocity(self):
        """
        Gets the target velocity of this axis.

        Parameters:
        axis: Axis index.

        Returns: Target velocity for this axis.
        """
        raise NotImplementedError

    @abstractmethod
    def set_target_velocity(self, velocity):
        """
        Sets the target velocity of this axis.

        Parameters:
        axis: Axis index.
        velocity: Target velocity.
        """
        raise NotImplementedError

    @abstractmethod
    def get_actual_velocity(self):
        """
        Gets the actual velocity of this axis.

        Parameters:
        axis: Axis index.

        Returns: Actual velocity for this axis.
        """
        raise NotImplementedError
