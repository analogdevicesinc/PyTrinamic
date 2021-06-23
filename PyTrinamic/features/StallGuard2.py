# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.Feature import Feature

class StallGuard2(Feature):

    def set_filter(self, axis, filter):
        raise NotImplementedError()

    def set_threshold(self, axis, threshold):
        raise NotImplementedError()

    def set_stop_velocity(self, axis, velocity):
        raise NotImplementedError()

    def get_filter(self, axis):
        raise NotImplementedError()

    def get_threshold(self, axis):
        raise NotImplementedError()

    def get_stop_velocity(self, axis):
        raise NotImplementedError()
