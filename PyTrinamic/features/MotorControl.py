# Created on: 04.03.2021
# Author: LK

class MotorControl(object):

    def rotate(self, axis, velocity):
        raise NotImplementedError()

    def stop(self, axis):
        raise NotImplementedError()

    def moveTo(self, axis, position, velocity=None):
        raise NotImplementedError()

    def moveBy(self, axis, difference, velocity=None):
        raise NotImplementedError()
