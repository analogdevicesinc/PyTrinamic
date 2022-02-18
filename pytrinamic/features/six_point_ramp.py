from abc import ABC, abstractmethod


class SixPointRamp(ABC):
    """
    SixPointRamp feature implementation
    """
    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_ramp_type(self, ramp_type):
        """
        Sets if Ramp that is used for this axis.
        This value is stored as RampType axis parameter.

        Parameters:
        ramp_type: ramp type value
        """
        raise NotImplementedError

    @abstractmethod
    def get_ramp_type(self):
        """
        Gets if Ramp that is used for this axis.
        This value is stored in the  RampType axis parameter.

        Returns: ramp type 
        """
        raise NotImplementedError

    @abstractmethod
    def set_start_velocity(self, start_velocity):
        """
        Sets start velocity used for this axis.
        This value is stored as StartVelocity axis parameter.

        Parameters:
        start_velocity: start velocity
        """
        raise NotImplementedError

    @abstractmethod
    def get_start_velocity(self):
        """
        Gets start velocity used for this axis.
        This value is stored as StartVelocity axis parameter. 

        Returns: start velocity 
        """
        raise NotImplementedError

    @abstractmethod
    def set_start_acceleration(self, start_acceleration):
        """
        Sets start acceleration used for this axis.
        This value is stored as StartAcceleration axis parameter.

        Parameters:
        start_acceleration: start acceleration
        """
        raise NotImplementedError

    @abstractmethod
    def get_start_acceleration(self):
        """
        Gets start acceleration used for this axis.
        This value is stored as StartAcceleration axis parameter. 

        Returns: start acceleration 
        """
        raise NotImplementedError

    @abstractmethod
    def set_max_deceleration(self, max_deceleration):
        """
        Sets maximum deceleration used for this axis.
        This value is stored as MaxDeceleration axis parameter.

        Parameters:
        max_deceleration: maximum deceleration
        """
        raise NotImplementedError

    @abstractmethod
    def get_max_deceleration(self):
        """
        Gets maximum deceleration used for this axis.
        This value is stored as MaxDeceleration axis parameter. 

        Returns: maximum deceleration
        """
        raise NotImplementedError

    @abstractmethod
    def set_break_velocity(self, break_velocity):
        """
        Sets break velocity used for this axis.
        This value is stored as BreakVelocity axis parameter.

        Parameters:
        break_velocity: break velocity
        """
        raise NotImplementedError

    @abstractmethod
    def get_break_velocity(self):
        """
        Gets break velocity used for this axis.
        This value is stored as BreakVelocity axis parameter. 

        Returns: break velocity
        """
        raise NotImplementedError

    @abstractmethod
    def set_final_deceleration(self, final_deceleration):
        """
        Sets final deceleration used for this axis.
        This value is stored as FinalDeceleration axis parameter.

        Parameters:
        final_deceleration: final deceleration
        """
        raise NotImplementedError

    @abstractmethod
    def get_final_deceleration(self):
        """
        Gets final deceleration used for this axis.
        This value is stored as FinalDeceleration axis parameter. 

        Returns: final deceleration
        """
        raise NotImplementedError

    @abstractmethod
    def set_stop_velocity(self, stop_velocity):
        """
        Sets stop velocity used for this axis.
        This value is stored as StopVelocity axis parameter.

        Parameters:
        stop_velocity: stop velocity
        """
        raise NotImplementedError

    @abstractmethod
    def get_stop_velocity(self):
        """
        Gets stop velocity used for this axis.
        This value is stored as StopVelocity axis parameter. 

        Returns: stop velocity 
        """
        raise NotImplementedError

    @abstractmethod
    def set_stop_deceleration(self, stop_deceleration):
        """
        Sets stop deceleration used for this axis.
        This value is stored as StopDeceleration axis parameter.

        Parameters:
        stop_deceleration: stop deceleration
        """
        raise NotImplementedError

    @abstractmethod
    def get_stop_deceleration(self):
        """
        Gets stop deceleration used for this axis.
        This value is stored as StopDeceleration axis parameter. 

        Returns: stop deceleration 
        """
        raise NotImplementedError
