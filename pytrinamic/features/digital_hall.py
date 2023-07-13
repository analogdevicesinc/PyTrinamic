from abc import ABC, abstractmethod


class DigitalHall(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_direction(self, direction):
        raise NotImplementedError

    @abstractmethod
    def get_direction(self):
        raise NotImplementedError

    @abstractmethod
    def set_polarity(self, polarity):
        raise NotImplementedError

    @abstractmethod
    def get_polarity(self):
        raise NotImplementedError

    @abstractmethod
    def set_sector_offset(self, sector_offset):
        raise NotImplementedError

    @abstractmethod
    def get_sector_offset(self):
        raise NotImplementedError

    @abstractmethod
    def set_offset(self, offset):
        raise NotImplementedError

    @abstractmethod
    def get_offset(self):
        raise NotImplementedError

    @abstractmethod
    def set_interpolation(self, enable_interpolation):
        raise NotImplementedError

    @abstractmethod
    def get_interpolation(self):
        raise NotImplementedError
