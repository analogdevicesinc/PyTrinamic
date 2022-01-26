from pytrinamic2.features.feature import Feature, FeatureProvider
from pytrinamic2.features.Current import Current


class CurrentModule(Current, FeatureProvider):
    "Current feature implementation for modules"

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
            This value is stored as RunCurrent axis parameter.

            Returns: Run current for this axis.
            """
            return self.parent.get_axis_parameter(self.parent.AP.RunCurrent)

        def set_current_run(self, value):
            """
            Sets the run current of this axis.
            This value is stored as RunCurrent axis parameter.

            Parameters:
            value: Target run current.
            """
            self.parent.set_axis_parameter(self.parent.AP.RunCurrent, value)

        def get_current_standby(self):
            """
            Gets the standby current of this axis.
            This value is stored as StandbyCurrent axis parameter.

            Returns: Standby current for this axis.
            """
            return self.parent.get_axis_parameter(self.parent.AP.StandbyCurrent)

        def set_current_standby(self, value):
            """
            Sets the standby current of this axis.
            This value is stored as StandbyCurrent axis parameter.

            Parameters:
            value: Target standby current.
            """
            self.parent.set_axis_parameter(self.parent.AP.StandbyCurrent, value)

        # Properties
        run = property(get_current_run, set_current_run)
        standby = property(get_current_standby, set_current_standby)

    def __init__(self):
        self.Current = self.__GROUPING(self)
