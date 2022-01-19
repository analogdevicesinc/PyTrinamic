from abc import ABC


class ABNEncoder(ABC):

    def set_resolution(self, steps):
        raise NotImplementedError
                                             
    def get_resolution(self):
        raise NotImplementedError

    def set_direction(self, direction):
        raise NotImplementedError

    def get_direction(self):
        raise NotImplementedError

    def set_init_mode(self, mode):
        raise NotImplementedError

    def get_init_mode(self):
        raise NotImplementedError

    def clear_once_on_n_channel(self):
        raise NotImplementedError
