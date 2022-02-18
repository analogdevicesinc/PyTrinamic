from abc import ABC, abstractmethod


class SRamp(ABC):
    """
    SRamp feature implementation
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
    def set_bow_1(self, pps):
        """
        Sets the bow 1 value for the S-Ramp of this axis.
        This value is stored as Bow1 axis parameter.

        Parameters:
        pps: Bow 1 value
        """
        raise NotImplementedError

    @abstractmethod
    def get_bow_1(self):
        """
        Gets the bow 1 value for the S-Ramp of this axis.
        This value is stored as Bow1 axis parameter.

        Returns: Bow 1 value 
        """
        raise NotImplementedError

    @abstractmethod
    def set_bow_2(self, pps):
        """
        Sets the bow 2 value for the S-Ramp of this axis.
        This value is stored as Bow2 axis parameter.

        Parameters:
        pps: Bow 2 value
        """
        raise NotImplementedError

    @abstractmethod
    def get_bow_2(self):
        """
        Gets the bow 1 value for the S-Ramp of this axis.
        This value is stored as Bow1 axis parameter.

        Returns: Bow 1 value 
        """
        raise NotImplementedError

    @abstractmethod
    def set_bow_3(self, pps):
        """
        Sets the bow 3 value for the S-Ramp of this axis.
        This value is stored as Bow3 axis parameter.

        Parameters:
        pps: Bow 3 value
        """
        raise NotImplementedError

    @abstractmethod
    def get_bow_3(self):
        """
        Gets the bow 3 value for the S-Ramp of this axis.
        This value is stored as Bow3 axis parameter.

        Returns: Bow 3 value 
        """
        raise NotImplementedError

    @abstractmethod
    def set_bow_4(self, pps):
        """
        Sets the bow 4 value for the S-Ramp of this axis.
        This value is stored as Bow4 axis parameter.

        Parameters:
        pps: Bow 4 value
        """
        raise NotImplementedError

    @abstractmethod
    def get_bow_4(self):
        """
        Gets the bow 4 value for the S-Ramp of this axis.
        This value is stored as Bow4 axis parameter.

        Returns: Bow 4 value 
        """
        raise NotImplementedError
