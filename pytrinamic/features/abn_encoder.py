from abc import ABC, abstractmethod


class ABNEncoder(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_resolution(self, steps):
        raise NotImplementedError

    @abstractmethod
    def get_resolution(self):
        raise NotImplementedError

    @abstractmethod
    def set_direction(self, direction):
        raise NotImplementedError

    @abstractmethod
    def get_direction(self):
        raise NotImplementedError

    @abstractmethod
    def set_init_mode(self, mode):
        raise NotImplementedError

    @abstractmethod
    def get_init_mode(self):
        raise NotImplementedError

    @abstractmethod
    def clear_once_on_n_channel(self):
        raise NotImplementedError
