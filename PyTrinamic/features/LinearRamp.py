# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.Feature import Feature

class LinearRamp(Feature):

    def get_target_position(self, axis):
        raise NotImplementedError()

    def set_target_position(self, axis, position):
        raise NotImplementedError()

    def get_actual_position(self, axis):
        raise NotImplementedError()

    def set_actual_position(self, axis, position):
        raise NotImplementedError()

    def get_target_velocity(self, axis):
        raise NotImplementedError()

    def set_target_velocity(self, axis, velocity):
        raise NotImplementedError()

    def get_actual_velocity(self, axis):
        raise NotImplementedError()

    def get_max_velocity(self, axis):
        raise NotImplementedError()

    def set_max_velocity(self, axis, velocity):
        raise NotImplementedError()

    def get_max_acceleration(self, axis):
        raise NotImplementedError()

    def set_max_acceleration(self, axis, acceleration):
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
