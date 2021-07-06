# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2Module(StallGuard2):

    class __GROUPING:

        def __init__(self, parent):
            self.parent = parent

        def set_filter(self, filter):
            self.parent.set_axis_parameter(self.parent.APs.SG2FilterEnable, filter)

        def set_threshold(self, threshold):
            self.parent.set_axis_parameter(self.parent.APs.SG2Threshold, threshold)

        def set_stop_velocity(self, velocity):
            self.parent.set_axis_parameter(self.parent.APs.SmartEnergyStallVelocity, velocity)

        def get_filter(self):
            return self.parent.get_axis_parameter(self.parent.APs.SG2FilterEnable)

        def get_threshold(self):
            return self.parent.get_axis_parameter(self.parent.APs.SG2Threshold)

        def get_stop_velocity(self):
            return self.parent.get_axis_parameter(self.parent.APs.SmartEnergyStallVelocity)

        # Properties
        filter = property(get_filter, set_filter)
        threshold = property(get_threshold, set_threshold)
        stop_velocity = property(get_stop_velocity, set_stop_velocity)

    # Feature initialization
    def __init__(self):
        self.StallGuard2 = self.__GROUPING(self)
