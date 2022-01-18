from PyTrinamic.features.feature import Feature


class MotorControl(Feature):

    # velocity mode

    def rotate(self, velocity):
        raise NotImplementedError()

    def stop(self):
        raise NotImplementedError()

    # position mode

    def move_to(self, position, velocity=None):
        raise NotImplementedError()

    def move_by(self, difference, velocity=None):
        raise NotImplementedError()
