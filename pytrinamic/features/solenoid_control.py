from abc import ABC, abstractmethod

class SolenoidControl(ABC):
    """
    Solenoid control implementation
    """
    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis
    
    @abstractmethod
    def set_high(self):
        """
        Apply high voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def set_low(self):
        """
        Apply low voltage.
        """
        raise NotImplementedError
