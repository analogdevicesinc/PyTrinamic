# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.Feature import Feature

class LinearRamp(Feature):
    "LinearRamp feature implementation"

    def get_target_position(self, axis):
        """
        Gets the target position of the given axis.

        Parameters:
        axis: Axis index.

        Returns: Target position for the given axis.
        """
        raise NotImplementedError()

    def set_target_position(self, axis, position):
        """
        Sets the target position of the given axis.

        Parameters:
        axis: Axis index.
        position: Target position.
        """
        raise NotImplementedError()

    def get_actual_position(self, axis):
        """
        Gets the actual position of the given axis.

        Parameters:
        axis: Axis index.

        Returns: Actual position for the given axis.
        """
        raise NotImplementedError()

    def set_actual_position(self, axis, position):
        """
        Sets the actual position of the given axis.

        Parameters:
        axis: Axis index.
        position: Actual position.
        """
        raise NotImplementedError()

    def get_target_velocity(self, axis):
        """
        Gets the target velocity of the given axis.

        Parameters:
        axis: Axis index.

        Returns: Target velocity for the given axis.
        """
        raise NotImplementedError()

    def set_target_velocity(self, axis, velocity):
        """
        Sets the target velocity of the given axis.

        Parameters:
        axis: Axis index.
        velocity: Target velocity.
        """
        raise NotImplementedError()

    def get_actual_velocity(self, axis):
        """
        Gets the actual velocity of the given axis.

        Parameters:
        axis: Axis index.

        Returns: Actual velocity for the given axis.
        """
        raise NotImplementedError()

    def get_max_velocity(self, axis):
        """
        Gets the maximum positioning velocity of the given axis.

        Parameters:
        axis: Axis index.

        Returns: Maximum positioning velocity for the given axis.
        """
        raise NotImplementedError()

    def set_max_velocity(self, axis, velocity):
        """
        Sets the maximum positioning velocity of the given axis.

        Parameters:
        axis: Axis index.
        velocity: Maximum positioning velocity.
        """
        raise NotImplementedError()

    def get_max_acceleration(self, axis):
        """
        Gets the maximum acceleration of the given axis.

        Parameters:
        axis: Axis index.

        Returns: Maximum acceleration for the given axis.
        """
        raise NotImplementedError()

    def set_max_acceleration(self, axis, acceleration):
        """
        Sets the maximum acceleration of the given axis.

        Parameters:
        axis: Axis index.
        acceleration: Maximum acceleration.
        """
        raise NotImplementedError()

    def __str__(self):
        return "{} {}".format(
            "LinearRamp",
            {
                "target_position": self.target_position,
                "actual_position": self.actual_position,
                "target_velocity": self.target_velocity,
                "actual_velocity": self.actual_velocity,
                "max_velocity": self.max_velocity,
                "max_acceleration": self.max_acceleration
            }
        )

    # Properties
    target_position = property(get_target_position, set_target_position)
    actual_position = property(get_actual_position, set_actual_position)
    target_velocity = property(get_target_velocity, set_target_velocity)
    actual_velocity = property(get_actual_velocity)
    max_velocity = property(get_max_velocity, set_max_velocity)
    max_acceleration = property(get_max_acceleration, set_max_acceleration)
