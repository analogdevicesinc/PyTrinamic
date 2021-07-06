# Created on: 06.07.2021
# Author: LK

from PyTrinamic.features.Feature import Feature

class Current(Feature):

    def get_current_run(self, axis):
        raise NotImplementedError()

    def set_current_run(self, axis, value):
        raise NotImplementedError()

    def get_current_standby(self, axis):
        raise NotImplementedError()

    def set_current_standby(self, axis, value):
        raise NotImplementedError()

    def __str__(self):
        return "{} {}".format(
            "Current",
            {
                "current_run": self.current_run,
                "current_standby": self.current_standby
            }
        )

    # Properties
    current_run = property(get_current_run, set_current_run)
    current_standby = property(get_current_standby, set_current_standby)
