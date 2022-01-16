from abc import ABC, abstractmethod


class ConnectionInterface(ABC):

    def __init__(self):
        self._debug = False

    def enable_debug(self, debug):
        self._debug = debug

    def debug_enabled(self):
        return self._debug

    def supports_tmcl(self):
        return False

    def supports_canopen(self):
        return False

    def print_info(self):
        info = "ConnectionInterface {"
        info += "'debug_enabled':" + str(self._debug) + ", "

        if self.supports_tmcl():
            info += "'supports_tmcl': True, "

        if self.supports_canopen():
            info += "'supports_canopen': True, "

        info = info[:-2]
        info += "}"
        print(info)

    @abstractmethod
    def list(self):
        raise NotImplementedError
