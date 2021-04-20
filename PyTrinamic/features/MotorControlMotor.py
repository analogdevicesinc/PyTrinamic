# Created on: 04.03.2021
# Author: LK

from PyTrinamic.features.MotorControl import MotorControl

class MotorControlMotor(MotorControl):

    def rotate(self, velocity):
        self.handler.rotate(self.axis, velocity)

    def stop(self):
        self.handler.stop(self.axis)

    def moveTo(self, position, velocity=None):
        self.handler.moveTo(self.axis, position, velocity)

    def moveBy(self, difference, velocity=None):
        self.handler.moveBy(self.axis, difference, velocity)
