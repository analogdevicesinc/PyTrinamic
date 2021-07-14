# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.Feature import Feature, FeatureProvider
from PyTrinamic.features.LinearRamp import LinearRamp

class LinearRampModule(LinearRamp, FeatureProvider):

    class __GROUPING(LinearRamp, FeatureProvider):

        # Grouping parent handling

        def __init__(self, parent):
            self.parent = parent

        # Grouped feature functions

        def get_target_position(self):
            return self.parent.get_axis_parameter(self.parent.APs.TargetPosition)

        def set_target_position(self, position):
            self.parent.set_axis_parameter(self.parent.APs.TargetPosition, position)

        def get_actual_position(self):
            return self.parent.get_axis_parameter(self.parent.APs.ActualPosition)

        def set_actual_position(self, position):
            self.parent.set_axis_parameter(self.parent.APs.ActualPosition, position)

        def get_target_velocity(self):
            return self.parent.get_axis_parameter(self.parent.APs.TargetVelocity)

        def set_target_velocity(self, velocity):
            self.parent.set_axis_parameter(self.parent.APs.TargetVelocity, velocity)

        def get_actual_velocity(self):
            return self.parent.get_axis_parameter(self.parent.APs.ActualVelocity)

        def get_max_velocity(self):
            return self.parent.get_axis_parameter(self.parent.APs.MaxVelocity)

        def set_max_velocity(self, velocity):
            self.parent.set_axis_parameter(self.parent.APs.MaxVelocity, velocity)

        def get_max_acceleration(self):
            return self.parent.get_axis_parameter(self.parent.APs.MaxAcceleration)

        def set_max_acceleration(self, acceleration):
            self.parent.set_axis_parameter(self.parent.APs.MaxAcceleration, acceleration)

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
        return self.get_axis_parameter(self.APs.TargetPosition)

    def set_target_position(self, position):
        self.set_axis_parameter(self.APs.TargetPosition, position)

    def get_actual_position(self):
        return self.get_axis_parameter(self.APs.ActualPosition)

    def set_actual_position(self, position):
        self.set_axis_parameter(self.APs.ActualPosition, position)

    def get_target_velocity(self):
        return self.get_axis_parameter(self.APs.TargetVelocity)

    def set_target_velocity(self, velocity):
        self.set_axis_parameter(self.APs.TargetVelocity, velocity)

    def get_actual_velocity(self):
        return self.get_axis_parameter(self.APs.ActualVelocity)

    def get_max_velocity(self):
        return self.get_axis_parameter(self.APs.MaxVelocity)

    def set_max_velocity(self, velocity):
        self.set_axis_parameter(self.APs.MaxVelocity, velocity)

    def get_max_acceleration(self):
        return self.get_axis_parameter(self.APs.MaxAcceleration)

    def set_max_acceleration(self, acceleration):
        self.set_axis_parameter(self.APs.MaxAcceleration, acceleration)

    # Motor-global properties
    target_position = property(get_target_position, set_target_position)
    actual_position = property(get_actual_position, set_actual_position)
    target_velocity = property(get_target_velocity, set_target_velocity)
    actual_velocity = property(get_actual_velocity)
    max_velocity = property(get_max_velocity, set_max_velocity)
    max_acceleration = property(get_max_acceleration, set_max_acceleration)
