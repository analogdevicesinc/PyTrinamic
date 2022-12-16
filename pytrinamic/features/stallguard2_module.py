from ..features.stallguard2 import StallGuard2
import time


class StallGuard2Module(StallGuard2):
    """
    StallGuard2 feature implementation for modules
    """
    def __init__(self, module, axis, aps):
        """
        Constructor for the feature grouping instance.
        """
        super().__init__(module, axis)
        self._aps = aps

    def set_filter(self, enable_filter):
        """
        Enable/Disable hardware StallGuard2 filter.
        This value is stored as SG2FilterEnable axis parameter.

        Parameters:
        filter:
        0 - Disable StallGuard2 filter
        1 - Enable StallGuard2 filter
        """
        self._parent.set_axis_parameter(self._aps.SG2FilterEnable, self._axis, filter)

    def get_filter(self):
        """
        Gets the StallGuard2 filter status.
        This value is stored as SG2FilterEnable axis parameter.

        Returns:
        0 - StallGuard2 filter disabled
        1 - StallGuard2 filter enabled
        """
        return self._parent.get_axis_parameter(self._aps.SG2FilterEnable, self._axis)

    def set_threshold(self, threshold):
        """
        Sets the StallGuard2 threshold / sensibility.
        This value is stored as SG2Threshold axis parameter.

        Parameters:
        threshold: StallGuard2 threshold. Default 0. Lower values mean higher sensibility.
        """
        self._parent.set_axis_parameter(self._aps.SG2Threshold, self._axis, threshold)

    def get_threshold(self):
        """
        Gets the StallGuard2 threshold / sensibility.
        This value is stored as SG2Threshold axis parameter.

        Returns: StallGuard2 threshold.
        """
        return self._parent.get_axis_parameter(self._aps.SG2Threshold, self._axis, signed=True)

    def set_stop_velocity(self, velocity):
        """
        Sets the minimum velocity, at which stop on stall becomes active.
        Value of 0 will disable the stop.
        This value is stored as SmartEnergyStallVelocity axis parameter.

        Parameters:
        velocity: Velocity threshold.
        """
        self._parent.set_axis_parameter(self._aps.SmartEnergyStallVelocity, self._axis, velocity)

    def get_stop_velocity(self):
        """
        Gets the minimum velocity, at which stop on stall becomes active.
        Value of 0 will disable the stop.
        This value is stored as SmartEnergyStallVelocity axis parameter.

        Returns: Velocity threshold.
        """
        return self._parent.get_axis_parameter(self._aps.SmartEnergyStallVelocity, self._axis)

    def get_load_value(self):
        """
        Gets the load value for monitoring smart energy current scaling or automatic current scaling.
        This value is stored as LoadValue axis parameter.

        Returns: LoadValue
        """
        return self._parent.get_axis_parameter(self._aps.LoadValue, self._axis)

    # module based calibration routine
    def calibrate_zero(self, threshold=1):
        """
        Interactive calibration function.
        Takes threshold as optional input.
        Sets parameter automatically

        """
        temp_threshold = threshold
        print("StallGuard zero calibration.")

        self.stop_velocity = 0

        print("Now, do apply some load to the motor, at which you want it to stop automatically.")
        input("Press enter to continue ...")

        for i in range(3):
            print("Starting calibration in " + str(3-i) + "seconds.")
            time.sleep(1.0)

        print("Calibrating SGT...")
        sgthresh = 0
        sgt = 0
        while (sgt == 0) and (sgthresh < 64):
            print("SGT too low, increasing threshold to " + str(sgthresh))
            self.threshold = sgthresh
            sgthresh += 1
            time.sleep(0.2)

            sgt = self.get_load_value()
            print("SGT load:" + str(sgt))

        self.threshold = sgthresh - 1
        print("Calibration done. Now release the load.")

        input("Press enter to continue ...")
        self.stop_velocity = temp_threshold

    # module based calibration routine
    def calibrate_middle(self):
        """
        Interactive calibration function.
        Takes threshold as optional input.
        Sets parameter automatically

        """
        print("StallGuard middle calibration.")

        self.stop_velocity = 0

        print("Now, do not apply any load to the motor. Let it run freely.")
        input("Press enter to continue ...")

        print("Calibrating SGT.")
        sgthresh = 0
        sgt = 0
        while(sgt < 450) and (sgthresh < 64):
            print("SGT too low, increasing threshold to " + str(sgthresh))
            self.threshold = sgthresh
            sgthresh += 1
            time.sleep(0.1)
            sgt = self.get_load_value()
            print("SGT load:" + str(sgt))

        self.threshold = sgthresh - 1
        print("StallGuard2 calibration done.")

    # Properties
    filter = property(get_filter, set_filter)
    threshold = property(get_threshold, set_threshold)
    stop_velocity = property(get_stop_velocity, set_stop_velocity)
    load_value = property(get_load_value)

    def __str__(self):
        return "{} {}".format(
            "StallGuard2",
            {
                "filter": self.filter,
                "threshold": self.threshold,
                "stop_velocity": self.stop_velocity
            }
        )
