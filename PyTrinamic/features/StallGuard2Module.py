# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.Feature import Feature, FeatureProvider
from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2Module(StallGuard2, FeatureProvider):
    "StallGuard2 feature implementation for modules"

    class __GROUPING(StallGuard2, FeatureProvider):

        def __init__(self, parent):
            """
            Constructor for the feature grouping instance.

            Parameters:
            parent: Parent instance. This is the Feature itself aswell as its
            descendants.
            """
            self.parent = parent

        def set_filter(self, filter):
            """
            Enable/Disable hardware StallGuard2 filter.
            This value is stored as SG2FilterEnable axis parameter.

            Parameters:
            filter:
            0 - Disable StallGuard2 filter
            1 - Enable StallGuard2 filter
            """
            self.parent.set_axis_parameter(self.parent.APs.SG2FilterEnable, filter)

        def set_threshold(self, threshold):
            """
            Sets the StallGuard2 threshold / sensibility.
            This value is stored as SG2Threshold axis parameter.

            Parameters:
            threshold: StallGuard2 threshold. Default 0. Lower values mean higher sensibility.
            """
            self.parent.set_axis_parameter(self.parent.APs.SG2Threshold, threshold)

        def set_stop_velocity(self, velocity):
            """
            Sets the minimum velocity, at which stop on stall becomes active.
            Value of 0 will disable the stop.
            This value is stored as SmartEnergyStallVelocity axis parameter.

            Parameters:
            velocity: Velocity threshold.
            """
            self.parent.set_axis_parameter(self.parent.APs.SmartEnergyStallVelocity, velocity)

        def get_filter(self):
            """
            Gets the StallGuard2 filter status.
            This value is stored as SG2FilterEnable axis parameter.

            Returns:
            0 - StallGuard2 filter disabled
            1 - StallGuard2 filter enabled
            """
            return self.parent.get_axis_parameter(self.parent.APs.SG2FilterEnable)

        def get_threshold(self):
            """
            Gets the StallGuard2 threshold / sensibility.
            This value is stored as SG2Threshold axis parameter.

            Returns: StallGuard2 threshold.
            """
            return self.parent.get_axis_parameter(self.parent.APs.SG2Threshold)

        def get_stop_velocity(self):
            """
            Gets the minimum velocity, at which stop on stall becomes active.
            Value of 0 will disable the stop.
            This value is stored as SmartEnergyStallVelocity axis parameter.

            Returns: Velocity threshold.
            """
            return self.parent.get_axis_parameter(self.parent.APs.SmartEnergyStallVelocity)

        # Properties
        filter = property(get_filter, set_filter)
        threshold = property(get_threshold, set_threshold)
        stop_velocity = property(get_stop_velocity, set_stop_velocity)

    # Feature initialization
    def __init__(self):
        self.StallGuard2 = self.__GROUPING(self)
