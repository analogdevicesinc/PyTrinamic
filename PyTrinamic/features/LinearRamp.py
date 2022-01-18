from PyTrinamic.features.feature import Feature


class LinearRamp(Feature):

    # LinearRamp feature implementation

    def get_target_position(self):
        """
        Gets the target position of this axis.

        Parameters:
        axis: Axis index.

        Returns: Target position for this axis.
        """
        raise NotImplementedError()

    def set_target_position(self, position):
        """
        Sets the target position of this axis.

        Parameters:
        axis: Axis index.
        position: Target position.
        """
        raise NotImplementedError()

    def get_actual_position(self):
        """
        Gets the actual position of this axis.

        Parameters:
        axis: Axis index.

        Returns: Actual position for this axis.
        """
        raise NotImplementedError()

    def set_actual_position(self, position):
        """
        Sets the actual position of this axis.

        Parameters:
        axis: Axis index.
        position: Actual position.
        """
        raise NotImplementedError()

    def get_target_velocity(self):
        """
        Gets the target velocity of this axis.

        Parameters:
        axis: Axis index.

        Returns: Target velocity for this axis.
        """
        raise NotImplementedError()

    def set_target_velocity(self, velocity):
        """
        Sets the target velocity of this axis.

        Parameters:
        axis: Axis index.
        velocity: Target velocity.
        """
        raise NotImplementedError()

    def get_actual_velocity(self):
        """
        Gets the actual velocity of this axis.

        Parameters:
        axis: Axis index.

        Returns: Actual velocity for this axis.
        """
        raise NotImplementedError()

    def get_max_velocity(self):
        """
        Gets the maximum positioning velocity of this axis.

        Parameters:
        axis: Axis index.

        Returns: Maximum positioning velocity for this axis.
        """
        raise NotImplementedError()

    def set_max_velocity(self, velocity):
        """
        Sets the maximum positioning velocity of this axis.

        Parameters:
        axis: Axis index.
        velocity: Maximum positioning velocity.
        """
        raise NotImplementedError()

    def get_max_acceleration(self):
        """
        Gets the maximum acceleration of this axis.

        Parameters:
        axis: Axis index.

        Returns: Maximum acceleration for this axis.
        """
        raise NotImplementedError()

    def set_max_acceleration(self, acceleration):
        """
        Sets the maximum acceleration of this axis.

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
