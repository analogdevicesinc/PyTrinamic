from PyTrinamic.features.feature import FeatureProvider
from PyTrinamic.features.motor_control import MotorControl


class MotorControlIC(MotorControl, FeatureProvider):

    def rotate(self, velocity):
        self.ic.rotate(self.axis, velocity)

    def stop(self):
        self.ic.stop(self.axis)

    def move_to(self, position, velocity=None):
        self.ic.move_to(self.axis, position, velocity)

    def move_by(self, difference, velocity=None):
        self.ic.move_by(self.axis, difference, velocity)
