# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.Feature import Feature, FeatureProvider
from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2IC(StallGuard2, FeatureProvider):

    class __GROUPING(StallGuard2, FeatureProvider):

        def __init__(self, parent):
            self.parent = parent

        def set_filter(self, filter):
            self.parent.write_axis_field(self.parent.ic.FIELDS.SFILT, filter)

        def set_threshold(self, threshold):
            self.parent.write_axis_field(self.parent.ic.FIELDS.SGT, threshold)

        def set_stop_velocity(self, velocity):
            self.parent.write_axis_field(self.parent.ic.FIELDS.SG_STOP, int(min(velocity, 1)))
            velocity = int(min(0xFFFFF, (1 << 24) / max(1, velocity)))
            self.parent.write_axis_field(self.parent.ic.FIELDS.TCOOLTHRS, velocity)

        def get_filter(self):
            return self.parent.read_axis_field(self.parent.ic.FIELDS.SFILT)

        def get_threshold(self):
            return self.parent.read_axis_field(self.parent.ic.FIELDS.SGT)

        def get_stop_velocity(self):
            velocity = self.parent.read_axis_field(self.parent.ic.FIELDS.TCOOLTHRS)
            return int(min(0xFFFFF, (1 << 24) / max(1, velocity)))

        # Properties
        filter = property(get_filter, set_filter)
        threshold = property(get_threshold, set_threshold)
        stop_velocity = property(get_stop_velocity, set_stop_velocity)

    # Feature initialization
    def __init__(self):
        self.StallGuard2 = self.__GROUPING(self)
