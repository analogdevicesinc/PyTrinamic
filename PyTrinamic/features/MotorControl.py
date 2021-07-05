# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.Feature import Feature

class MotorControl(Feature):

    def rotate(self, velocity):
        self.module.rotate(self.axis, velocity)

    def stop(self):
        self.module.stop(self.axis)

    def move_to(self, position, velocity=None):
        self.module.move_to(self.axis, position, velocity)

    def move_by(self, difference, velocity=None):
        self.module.move_by(self.axis, difference, velocity)
