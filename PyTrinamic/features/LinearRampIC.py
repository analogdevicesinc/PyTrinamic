# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.Feature import Feature, FeatureProvider
from PyTrinamic.features.LinearRamp import LinearRamp


class LinearRampIC(LinearRamp, FeatureProvider):

    # LinearRamp feature implementation for ICs

    class __GROUPING(LinearRamp, FeatureProvider):

        def __init__(self, parent):
            self.parent = parent

        def get_target_position(self):
            """
            Gets the target position of this axis.
            This value is stored in the XTARGET field of the IC.

            Returns: Target position for this axis.
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.XTARGET)

        def set_target_position(self, position):
            """
            Sets the target position of this axis.
            This value is stored in the XTARGET field of the IC.

            Parameters:
            position: Target position.
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.XTARGET, position)

        def get_actual_position(self):
            """
            Gets the actual position of this axis.
            This value is stored in the XACTUAL field of the IC.

            Returns: Actual position for this axis.
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.XACTUAL)

        def set_actual_position(self, position):
            """
            Sets the actual position of this axis.
            This value is stored in the XACTUAL field of the IC.

            Parameters:
            position: Actual position.
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.XACTUAL, position)

        def get_target_velocity(self):
            """
            Gets the target velocity of this axis.
            This value is stored in the VMAX field of the IC.

            Returns: Target velocity for this axis.
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.VMAX)

        def set_target_velocity(self, velocity):
            """
            Sets the target velocity of this axis.
            This value is stored in the VMAX field of the IC.

            Parameters:
            velocity: Target velocity.
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.VMAX, velocity)

        def get_actual_velocity(self):
            """
            Gets the actual velocity of this axis.
            This value is stored in the VACTUAL field of the IC.

            Returns: Actual velocity for this axis.
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.VACTUAL)

        def get_max_velocity(self):
            """
            Gets the maximum positioning velocity of this axis.
            This value is stored in the VMAX field of the IC.

            Returns: Maximum positioning velocity for this axis.
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.VMAX)

        def set_max_velocity(self, velocity):
            """
            Sets the maximum positioning velocity of this axis.
            This value is stored in the VMAX field of the IC.

            Parameters:
            velocity: Maximum positioning velocity.
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.VMAX, velocity)

        def get_max_acceleration(self):
            """
            Gets the maximum acceleration of this axis.
            This value is stored in the AMAX field of the IC.

            Returns: Maximum acceleration for this axis.
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.AMAX)

        def set_max_acceleration(self, acceleration):
            """
            Sets the maximum acceleration of this axis.
            This value is stored in the AMAX field of the IC.

            Parameters:
            acceleration: Maximum acceleration.
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.AMAX, acceleration)

        # Properties
        target_position = property(get_target_position, set_target_position)
        actual_position = property(get_actual_position, set_actual_position)
        target_velocity = property(get_target_velocity, set_target_velocity)
        actual_velocity = property(get_actual_velocity)
        max_velocity = property(get_max_velocity, set_max_velocity)
        max_acceleration = property(get_max_acceleration, set_max_acceleration)

    # Feature initialization and aggregation
    def __init__(self):
        self.LinearRamp = self.__GROUPING(self)

    # Motor-global functions

    def get_axis_parameter(self, parameter, signed=False):
        raise NotImplementedError()

    def set_axis_parameter(self, parameter, value):
        raise NotImplementedError()

    def get_target_position(self):
        """
        Gets the target position of this axis.
        This value is stored in the XTARGET field of the IC.

        Returns: Target position for this axis.
        """
        return self.LinearRamp.get_target_position()

    def set_target_position(self, position):
        """
        Sets the target position of this axis.
        This value is stored in the XTARGET field of the IC.

        Parameters:
        position: Target position.
        """
        self.LinearRamp.set_target_position(position)

    def get_actual_position(self):
        """
        Gets the actual position of this axis.
        This value is stored in the XACTUAL field of the IC.

        Returns: Actual position for this axis.
        """
        return self.LinearRamp.get_actual_position()

    def set_actual_position(self, position):
        """
        Sets the actual position of this axis.
        This value is stored in the XACTUAL field of the IC.

        Parameters:
        position: Actual position.
        """
        self.LinearRamp.set_actual_position(position)

    def get_target_velocity(self):
        """
        Gets the target velocity of this axis.
        This value is stored in the VMAX field of the IC.

        Returns: Target velocity for this axis.
        """
        return self.LinearRamp.get_target_velocity()

    def set_target_velocity(self, velocity):
        """
        Sets the target velocity of this axis.
        This value is stored in the VMAX field of the IC.

        Parameters:
        velocity: Target velocity.
        """
        self.LinearRamp.set_target_velocity(velocity)

    def get_actual_velocity(self):
        """
        Gets the actual velocity of this axis.
        This value is stored in the VACTUAL field of the IC.

        Returns: Actual velocity for this axis.
        """
        return self.LinearRamp.get_actual_velocity()

    def get_max_velocity(self):
        """
        Gets the maximum positioning velocity of this axis.
        This value is stored in the VMAX field of the IC.

        Returns: Maximum positioning velocity for this axis.
        """
        return self.LinearRamp.get_max_velocity()

    def set_max_velocity(self, velocity):
        """
        Sets the maximum positioning velocity of this axis.
        This value is stored in the VMAX field of the IC.

        Parameters:
        velocity: Maximum positioning velocity.
        """
        self.LinearRamp.set_max_velocity(velocity)

    def get_max_acceleration(self):
        """
        Gets the maximum acceleration of this axis.
        This value is stored in the AMAX field of the IC.

        Returns: Maximum acceleration for this axis.
        """
        return self.LinearRamp.get_max_acceleration()

    def set_max_acceleration(self, acceleration):
        """
        Sets the maximum acceleration of this axis.
        This value is stored in the AMAX field of the IC.

        Parameters:
        acceleration: Maximum acceleration.
        """
        self.LinearRamp.set_max_acceleration(acceleration)

    # Motor-global properties
    target_position = property(get_target_position, set_target_position)
    actual_position = property(get_actual_position, set_actual_position)
    target_velocity = property(get_target_velocity, set_target_velocity)
    actual_velocity = property(get_actual_velocity)
    max_velocity = property(get_max_velocity, set_max_velocity)
    max_acceleration = property(get_max_acceleration, set_max_acceleration)
