from pytrinamic2.features.feature import Feature, FeatureProvider
from pytrinamic2.features.Current import Current


class CurrentIC(Current, FeatureProvider):
    "Current feature implementation for ICs"

    class __GROUPING(Current, FeatureProvider):

        def __init__(self, parent):
            """
            Constructor for the feature grouping instance.

            Parameters:
            parent: Parent instance. This is the Feature itself aswell as its
            descendants.
            """
            self.parent = parent

        def get_current_run(self):
            """
            Gets the run current of this axis.
            This value is stored in the IRUN field of the IC.

            Returns: Run current for this axis.
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.IRUN)

        def set_current_run(self, value):
            """
            Sets the run current of this axis.
            This value is stored in the IRUN field of the IC.

            Parameters:
            value: Target run current.
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.IRUN, value)

        def get_current_standby(self):
            """
            Gets the standby current of this axis.
            This value is stored in the IHOLD field of the IC.

            Returns: Standby current for this axis.
            """
            return self.parent.read_axis_field(self.parent.ic.FIELDS.IHOLD)

        def set_current_standby(self, value):
            """
            Sets the standby current of this axis.
            This value is stored in the IHOLD field of the IC.

            Parameters:
            value: Target standby current.
            """
            self.parent.write_axis_field(self.parent.ic.FIELDS.IHOLD, value)

        # Properties
        run = property(get_current_run, set_current_run)
        standby = property(get_current_standby, set_current_standby)

    def __init__(self):
        self.Current = self.__GROUPING(self)
