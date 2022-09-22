from abc import ABC, abstractmethod

class Solenoid(ABC):
    """
    Solenoid feature implementation
    """
    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis
    
    @abstractmethod
    def set_voltage_high(self, u_dc_h):
        """
        Set high DC voltage.

        Parameters:
        u_dc_h: High DC voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def get_voltage_high(self):
        """
        Get high DC voltage.

        Returns:
        High DC voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def set_voltage_low(self, u_dc_l):
        """
        Set low DC voltage.

        Parameters:
        u_dc_l: Low DC voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def get_voltage_low(self):
        """
        Get low DC voltage.

        Returns:
        Low DC voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def set_voltage_low_high(self, u_dc_l2h):
        """
        Set low to high DC voltage.

        Parameters:
        u_dc_l2h: Low to high DC voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def get_voltage_low_high(self):
        """
        Get low to high DC voltage.

        Returns:
        Low to high DC voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def set_voltage_high_low(self, u_dc_h2l):
        """
        Set high to low DC voltage.

        Parameters:
        u_dc_h2l: High to low DC voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def get_voltage_high_low(self):
        """
        Get high to low DC voltage.

        Returns:
        High to low DC voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def set_frequency(self, u_ac_freq):
        """
        Set AC frequency.

        Parameters:
        u_ac_freq: AC frequency.
        """
        raise NotImplementedError

    @abstractmethod
    def get_frequency(self):
        """
        Get AC frequency.

        Returns:
        AC frequency.
        """
        raise NotImplementedError

    @abstractmethod
    def set_voltage_ac(self, u_ac):
        """
        Set AC voltage.

        Parameters:
        u_ac: AC voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def get_voltage_ac(self):
        """
        Get AC voltage.

        Returns:
        AC voltage.
        """
        raise NotImplementedError
