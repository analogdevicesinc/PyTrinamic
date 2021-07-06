# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.MotorControl import MotorControl

class MotorControlIC(MotorControl):

    def rotate(self, velocity):
        self.ic.rotate(self.axis, velocity)

    def stop(self):
        self.ic.stop(self.axis)

    def move_to(self, position, velocity=None):
        self.ic.move_to(self.axis, position, velocity)

    def move_by(self, difference, velocity=None):
        self.ic.move_by(self.axis, difference, velocity)
