from PyTrinamic.features.feature import Feature, FeatureProvider
from PyTrinamic.features.StallGuard2 import StallGuard2


class StallGuard2IC(StallGuard2, FeatureProvider):
    "StallGuard2 feature implementation for ICs"

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
            This value is stored in the SFILT field of the IC.

            Parameters:
            filter:
            0 - Disable StallGuard2 filter
            1 - Enable StallGuard2 filter
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.SFILT, filter)

        def set_threshold(self, threshold):
            """
            Sets the StallGuard2 threshold / sensibility.
            This value is stored in the SGT field of the IC.

            Parameters:
            threshold: StallGuard2 threshold. Default 0. Lower values mean higher sensibility.
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.SGT, threshold)

        def set_stop_velocity(self, velocity):
            """
            Sets the minimum velocity, at which stop on stall becomes active.
            Value of 0 will disable the stop.
            This will become enabled by setting the SG_STOP field of the IC.
            This value is stored in the TCOOLTHRS field of the IC.

            Parameters:
            velocity: Velocity threshold.
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.SG_STOP, int(min(velocity, 1)))
            velocity = int(min(0xFFFFF, (1 << 24) / max(1, velocity)))
            self.parent.write_axis_field(self.parent.ic.FIELDS.TCOOLTHRS, velocity)

        def get_filter(self):
            """
            Gets the StallGuard2 filter status.
            This value is stored in the SFILT field of the IC.

            Returns:
            0 - StallGuard2 filter disabled
            1 - StallGuard2 filter enabled
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.SFILT)

        def get_threshold(self):
            """
            Gets the StallGuard2 threshold / sensibility.
            This value is stored in the SGT field of the IC.

            Returns: StallGuard2 threshold.
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.SGT)

        def get_stop_velocity(self):
            """
            Gets the minimum velocity, at which stop on stall becomes active.
            Value of 0 will disable the stop.
            This will become enabled by setting the SG_STOP field of the IC.
            This value is stored in the TCOOLTHRS field of the IC.

            Returns: Velocity threshold.
            """
            velocity = self.parent.read_axis_field(self.parent.ic.FIELDS.TCOOLTHRS)
            return int(min(0xFFFFF, (1 << 24) / max(1, velocity)))

        # Properties
        filter = property(get_filter, set_filter)
        threshold = property(get_threshold, set_threshold)
        stop_velocity = property(get_stop_velocity, set_stop_velocity)

    # Feature initialization
    def __init__(self):
        self.StallGuard2 = self.__GROUPING(self)
