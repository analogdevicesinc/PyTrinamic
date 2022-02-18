from abc import ABC, abstractmethod


class Current(ABC):
    """
    Current feature implementation
    """
    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_run_current(self, current):
        """
        Sets the run current of the given axis.

        Parameters:
        value: Value of the run current. This value is hardware specific, please refer
        to the documentation of the hardware.
        """
        raise NotImplementedError

    @abstractmethod
    def get_run_current(self):
        """
        Gets the run current of the given axis.

        Parameters:
        Returns: Run current for the given axis.
        """
        raise NotImplementedError

    @abstractmethod
    def set_standby_current(self, current):
        """
        Sets the standby current of the given axis.

        Parameters:
        value: Value of the standby current. This value is hardware specific, please refer
        to the documentation of the hardware.
        """
        raise NotImplementedError

    @abstractmethod
    def get_standby_current(self):
        """
        Gets the standby current of the given axis.

        Parameters:
        Returns: Standby current for the given axis.
        """
        raise NotImplementedError
