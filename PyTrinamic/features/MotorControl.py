# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.Feature import Feature


class MotorControl(Feature):

    def rotate(self, velocity):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()

    def move_to(self, position, velocity=None):
        raise NotImplementedError()

    def move_by(self, difference, velocity=None):
        raise NotImplementedError()
