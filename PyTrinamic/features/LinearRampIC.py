# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.Feature import Feature, FeatureProvider
from PyTrinamic.features.LinearRamp import LinearRamp

class LinearRampIC(LinearRamp, FeatureProvider):

    class __GROUPING(LinearRamp, FeatureProvider):

        # Grouping parent handling

        def __init__(self, parent):
            self.parent = parent

        # Grouped feature functions

        def get_target_position(self):
            return self.parent.read_axis_field(self.parent.ic.FIELDS.XTARGET)

        def set_target_position(self, position):
            self.parent.write_axis_field(self.parent.ic.FIELDS.XTARGET, position)

        def get_actual_position(self):
            return self.parent.read_axis_field(self.parent.ic.FIELDS.XACTUAL)

        def set_actual_position(self, position):
            self.parent.write_axis_field(self.parent.ic.FIELDS.XACTUAL, position)

        def get_target_velocity(self):
            return self.parent.read_axis_field(self.parent.ic.FIELDS.VMAX)

        def set_target_velocity(self, velocity):
            self.parent.write_axis_field(self.parent.ic.FIELDS.VMAX, velocity)

        def get_actual_velocity(self):
            return self.parent.read_axis_field(self.parent.ic.FIELDS.VACTUAL)

        def get_max_velocity(self):
            return self.parent.read_axis_field(self.parent.ic.FIELDS.VMAX)

        def set_max_velocity(self, velocity):
            self.parent.write_axis_field(self.parent.ic.FIELDS.VMAX, velocity)

        def get_max_acceleration(self):
            return self.parent.read_axis_field(self.parent.ic.FIELDS.AMAX)

        def set_max_acceleration(self, acceleration):
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
        return self.LinearRamp.get_target_position()

    def set_target_position(self, position):
        self.LinearRamp.set_target_position(position)

    def get_actual_position(self):
        return self.LinearRamp.get_actual_position()

    def set_actual_position(self, position):
        self.LinearRamp.set_actual_position(position)

    def get_target_velocity(self):
        return self.LinearRamp.get_target_velocity()

    def set_target_velocity(self, velocity):
        self.LinearRamp.set_target_velocity(velocity)

    def get_actual_velocity(self):
        return self.LinearRamp.get_actual_velocity()

    def get_max_velocity(self):
        return self.LinearRamp.get_max_velocity()

    def set_max_velocity(self, velocity):
        self.LinearRamp.set_max_velocity(velocity)

    def get_max_acceleration(self):
        return self.LinearRamp.get_max_acceleration()

    def set_max_acceleration(self, acceleration):
        self.LinearRamp.set_max_acceleration(acceleration)

    # Motor-global properties
    target_position = property(get_target_position, set_target_position)
    actual_position = property(get_actual_position, set_actual_position)
    target_velocity = property(get_target_velocity, set_target_velocity)
    actual_velocity = property(get_actual_velocity)
    max_velocity = property(get_max_velocity, set_max_velocity)
    max_acceleration = property(get_max_acceleration, set_max_acceleration)
