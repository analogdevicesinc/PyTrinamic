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

    def showMotionConfiguration(self, axis):
        print("Motion configuration:")
        print("\tMax velocity: " + str(self.get_max_velocity(axis)))
        print("\tAcceleration: " + str(self.get_max_acceleration(axis)))
