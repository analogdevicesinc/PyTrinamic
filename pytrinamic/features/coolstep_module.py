from ..features.coolstep import CoolStep
import time


class CoolStepModule(CoolStep):
    """
    CoolStep feature implementation for modules
    """
    def __init__(self, module, axis, aps, stall_guard):
        """
        Constructor for the feature grouping instance.
        """
        super().__init__(module, axis)
        self._aps = aps
        self._stall_guard = stall_guard

    def set_current_minimum(self, current):
        """
        Sets the smartEnergy current minimum.
        Stored in axis parameter SEIMIN
        Parameters:
        current: smartEnergy current minimum.
        """
        self._parent.set_axis_parameter(self._aps.SEIMIN, self._axis, current)

    def get_current_minimum(self):
        """
        Gets the smartEnergy current minimum.
        Stored in axis parameter SEIMIN

        Returns:
        smartEnergy current minimum.
        """
        return self._parent.get_axis_parameter(self._aps.SEIMIN, self._axis)

    def set_current_down_step(self, step):
        """
        Sets the smartEnergy current down step.

        Parameters:
        step: smartEnergy current down step.
        """
        self._parent.set_axis_parameter(self._aps.SECDS, self._axis, step)

    def get_current_down_step(self):
        """
        Gets the smartEnergy current down step.

        Returns:
        smartEnergy current down step.
        """
        return self._parent.get_axis_parameter(self._aps.SECDS, self._axis)

    def set_current_up_step(self, step):
        """
        Sets the smartEnergy current up step.

        Parameters:
        step: smartEnergy current up step.
        """
        self._parent.set_axis_parameter(self._aps.SECUS, self._axis, step)

    def get_current_up_step(self):
        """
        Gets the smartEnergy current up step.

        Returns:
        smartEnergy current up step.
        """
        return self._parent.get_axis_parameter(self._aps.SECUS, self._axis)

    def set_hysteresis(self, hysteresis):
        """
        Sets the smartEnergy hysteresis.

        Parameters:
        hysteresis: smartEnergy hysteresis.
        """
        self._parent.set_axis_parameter(self._aps.SmartEnergyHysteresis, self._axis, hysteresis)

    def get_hysteresis(self):
        """
        Gets the smartEnergy hysteresis.

        Returns:
        smartEnergy hysteresis.
        """
        return self._parent.get_axis_parameter(self._aps.SmartEnergyHysteresis, self._axis)

    def set_hysteresis_start(self, hysteresis_start):
        """
        Sets the smartEnergy hysteresis start.

        Parameters:
        hysteresis_start: smartEnergy hysteresis start .
        """
        self._parent.set_axis_parameter(self._aps.SmartEnergyHysteresisStart, self._axis, hysteresis_start)

    def get_hysteresis_start(self):
        """
        Gets the smartEnergy hysteresis start.

        Returns:
        smartEnergy hysteresis start .
        """
        return self._parent.get_axis_parameter(self._aps.SmartEnergyHysteresisStart, self._axis)

    def set_threshold_speed(self, speed):
        """
        Sets the smartEnergy speed threshold.

        Parameters:
        speed: smartEnergy threshold speed.
        """
        self._parent.set_axis_parameter(self._aps.SmartEnergyThresholdSpeed, self._axis, speed)

    def get_threshold_speed(self):
        """
        Gets the smartEnergy speed threshold.

        Returns:
        smartEnergy threshold speed.
        """
        return self._parent.get_axis_parameter(self._aps.SmartEnergyThresholdSpeed, self._axis)

    def set_slow_run_current(self, current):
        """
        Sets the smartEnergy slow run current.

        Parameters:
        current: smartEnergy slow run current
        """
        self._parent.set_axis_parameter(self._aps.SmartEnergySlowRunCurrent, self._axis, current)

    def get_slow_run_current(self):
        """
        Gets the smartEnergy slow run current.

        Returns:
        smartEnergy slow run current
        """
        return self._parent.get_axis_parameter(self._aps.SmartEnergySlowRunCurrent, self._axis)

    def calibrate(self, threshold=0):
        """
        Interactive calibration function.
        Takes threshold as optional input.
        Sets parameter automatically

        """
        self._stall_guard.calibrate_middle()

        print("Now, apply some load to the motor, at which you want the current to increase automatically.")
        input("Press enter to continue ...")

        for i in range(3):
            print("Starting calibration in " + str(3-i) + "seconds.")
            time.sleep(1.0)

        hstart = int(round((self._stall_guard.get_load_value() / 1023) * 15, 0))
        print("Hysteresis start:" + str(hstart))

        print("Now, release the load. Let the motor run freely.")
        input("Press enter to continue ...")

        hend = int(round((self._stall_guard.get_load_value() / 1023) * 15, 0))
        print("Hysteresis end: " + str(hend))

        hwidth = hend - hstart
        print("Hysteresis window width: " + str(hwidth))

        self.hysteresis = hwidth
        self.hysteresis_start = hstart
        self.threshold_speed = threshold

    # Properties
    current_minimum = property(get_current_minimum, set_current_minimum)
    current_down_step = property(get_current_down_step, set_current_down_step)
    current_up_step = property(get_current_up_step, set_current_up_step)
    hysteresis = property(get_hysteresis, set_hysteresis)
    hysteresis_start = property(get_hysteresis_start, set_hysteresis_start)
    threshold_speed = property(get_threshold_speed, set_threshold_speed)
    slow_run_current = property(get_slow_run_current, set_slow_run_current)

    def __str__(self):
        return "{} {}".format(
            "CoolStep",
            {
                "current minimum": self.current_minimum,
                "current down step": self.current_down_step,
                "current up step": self.current_up_step,
                "hysteresis": self.hysteresis,
                "hysteresis_start": self.hysteresis_start,
                "threshold_speed": self.threshold_speed,
                "slow_run_current": self.slow_run_current,
            }
        )
