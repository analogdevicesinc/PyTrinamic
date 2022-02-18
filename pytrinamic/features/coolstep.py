from abc import ABC, abstractmethod


class CoolStep(ABC):
    """
    StallGuard2 feature implementation
    """
    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_current_minimum(self, current):
        """
        Sets the smartEnergy current minimum.

        Parameters:
        current: smartEnergy current minimum.
        """
        raise NotImplementedError

    @abstractmethod
    def get_current_minimum(self):
        """
        Gets the smartEnergy current minimum.

        Returns:
        smartEnergy current minimum.
        """
        raise NotImplementedError

    @abstractmethod
    def set_current_down_step(self, step):
        """
        Sets the smartEnergy current down step.

        Parameters:
        step: smartEnergy current down step.
        """
        raise NotImplementedError

    @abstractmethod
    def get_current_down_step(self):
        """
        Gets the smartEnergy current down step.

        Returns:
        smartEnergy current down step.
        """
        raise NotImplementedError

    @abstractmethod
    def set_current_up_step(self, step):
        """
        Sets the smartEnergy current up step.

        Parameters:
        step: smartEnergy current up step.
        """
        raise NotImplementedError

    @abstractmethod
    def get_current_up_step(self):
        """
        Gets the smartEnergy current up step.

        Returns:
        smartEnergy current up step.
        """
        raise NotImplementedError

    @abstractmethod
    def set_hysteresis(self, hysteresis):
        """
        Sets the smartEnergy hysteresis.

        Parameters:
        hysteresis: smartEnergy hysteresis.
        """
        raise NotImplementedError

    @abstractmethod
    def get_hysteresis(self):
        """
        Gets the smartEnergy hysteresis.

        Returns:
        smartEnergy hysteresis.
        """
        raise NotImplementedError

    @abstractmethod
    def set_hysteresis_start(self, hysteresis_start):
        """
        Sets the smartEnergy hysteresis start.

        Parameters:
        hysteresis_start: smartEnergy hysteresis start .
        """
        raise NotImplementedError

    @abstractmethod
    def get_hysteresis_start(self):
        """
        Gets the smartEnergy hysteresis start.

        Returns:
        smartEnergy hysteresis start .
        """
        raise NotImplementedError

    @abstractmethod
    def set_threshold_speed(self, speed):
        """
        Sets the smartEnergy speed threshold.

        Parameters:
        speed: smartEnergy threshold speed.
        """
        raise NotImplementedError

    @abstractmethod
    def get_threshold_speed(self):
        """
        Gets the smartEnergy speed threshold.

        Returns:
        smartEnergy threshold speed.
        """
        raise NotImplementedError

    @abstractmethod
    def set_slow_run_current(self, current):
        """
        Sets the smartEnergy slow run current.

        Parameters:
        current: smartEnergy slow run current
        """
        raise NotImplementedError

    @abstractmethod
    def get_slow_run_current(self):
        """
        Gets the smartEnergy slow run current.
        
        Returns:
        smartEnergy slow run current
        """
        raise NotImplementedError

    @abstractmethod
    def calibrate(self, threshold):
        raise NotImplementedError
