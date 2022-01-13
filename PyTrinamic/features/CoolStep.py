from PyTrinamic.features.Feature import Feature

class CoolStep(Feature):
    "StallGuard2 feature implementation"

    def set_current_minimum(self, axis, current):
        """
        Sets the smartEnergy current minimum.

        Parameters:
        axis: Axis index.
        current: smartEnergy current minimum.
        """
        raise NotImplementedError()

    def set_current_down_step(self, axis, step):
        """
        Sets the smartEnergy current down step.

        Parameters:
        axis: Axis index.
        step: smartEnergy current down step.
        """
        raise NotImplementedError()

    def set_current_up_step(self, axis, ):
        """
        Sets the smartEnergy current up step.

        Parameters:
        axis: Axis index.
        step: smartEnergy current up step.
        """
        raise NotImplementedError()

    def set_hysteresis(self, axis, hysteresis):
        """
        Sets the smartEnergy hysteresis.

        Parameters:
        axis: Axis index.
        hysteresis: smartEnergy hysteresis.
        """
        raise NotImplementedError()

    def set_hysteresis_start(self, axis, hysteresis_start):
        """
        Sets the smartEnergy hysteresis start.

        Parameters:
        axis: Axis index.
        hysteresis_start: smartEnergy hysteresis start .
        """
        raise NotImplementedError()

    def set_threshold_speed(self, axis, speed):
        """
        Sets the smartEnergy speed threshold.

        Parameters:
        axis: Axis index.
        speed: smartEnergy threshold speed.
        """
        raise NotImplementedError()

    def set_slow_run_current(self, axis, current):
        """
        Sets the smartEnergy slow run current.

        Parameters:
        axis: Axis index.
        current: smartEnergy slow run current
        """
        raise NotImplementedError()
    

    def get_current_minimum(self, axis):
        """
        Gets the smartEnergy current minimum.

        Returns: 
        smartEnergy current minimum.
        """
        raise NotImplementedError()

    def get_current_down_step(self, axis):
        """
        Gets the smartEnergy current down step.

        Returns: 
        smartEnergy current down step.
        """
        raise NotImplementedError()

    def get_current_up_step(self, axis):
        """
        Gets the smartEnergy current up step.

        Returns:
        smartEnergy current up step.
        """
        raise NotImplementedError()

    def get_hysteresis(self, axis):
        """
        Gets the smartEnergy hysteresis.

        Returns:
        smartEnergy hysteresis.
        """
        raise NotImplementedError()

    def get_hysteresis_start(self, axis):
        """
        Gets the smartEnergy hysteresis start.

        Returns:
        smartEnergy hysteresis start .
        """
        raise NotImplementedError()

    def get_threshold_speed(self, axis):
        """
        Gets the smartEnergy speed threshold.

        Returns:
        smartEnergy threshold speed.
        """
        raise NotImplementedError()

    def get_slow_run_current(self, axis):
        """
        Gets the smartEnergy slow run current.
        
        Returns:
        smartEnergy slow run current
        """
        raise NotImplementedError()
    
    def __str__(self):
        return "{} {}".format(
            "CoolStep",
            {
                "current minimum" : self.current_minimum,
                "current down step": self.current_down_step,
                "current up step": self.current_up_step,
                "hysteresis": self.hysteresis,
                "hysteresis_start": self.hysteresis_start,
                "threshold_speed": self.threshold_speed,
                "slow_run_current": self.slow_run_current,
            }
        )

    # Properties
    current_minimum = property(get_current_minimum, set_current_minimum)
    current_down_step = property(get_current_down_step, set_current_down_step)
    current_up_step = property(get_current_up_step, set_current_up_step)
    hysteresis = property(get_hysteresis, set_hysteresis)
    hysteresis_start = property(get_hysteresis_start, set_hysteresis_start)
    threshold_speed = property(get_threshold_speed, set_threshold_speed)
    slow_run_current = property(get_slow_run_current, set_slow_run_current)
