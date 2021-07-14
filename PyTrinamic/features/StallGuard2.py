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

    def __str__(self):
        return "{} {}".format(
            "StallGuard2",
            {
                "filter": self.filter,
                "threshold": self.threshold,
                "stop_velocity": self.stop_velocity
            }
        )

    # Properties
    filter = property(get_filter, set_filter)
    threshold = property(get_threshold, set_threshold)
    stop_velocity = property(get_stop_velocity, set_stop_velocity)
