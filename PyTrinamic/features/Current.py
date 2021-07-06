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
