# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.LinearRamp import LinearRamp

class LinearRampMotor(LinearRamp):

    def __init__(self, motor):
        self.motor = motor

    def get_target_position(self):
        return self.motor.get_axis_parameter(self.motor.APs.TargetPosition)

    def set_target_position(self, position):
        self.motor.set_axis_parameter(self.motor.APs.TargetPosition, position)

    def get_actual_position(self):
        return self.motor.get_axis_parameter(self.motor.APs.ActualPosition)

    def set_actual_position(self, position):
        self.motor.set_axis_parameter(self.motor.APs.ActualPosition, position)

    def get_target_velocity(self):
        return self.motor.get_axis_parameter(self.motor.APs.TargetVelocity)

    def set_target_velocity(self, velocity):
        self.motor.set_axis_parameter(self.motor.APs.TargetVelocity, velocity)

    def get_actual_velocity(self):
        return self.motor.get_axis_parameter(self.motor.APs.ActualVelocity)

    def get_max_velocity(self):
        return self.motor.get_axis_parameter(self.motor.APs.MaxVelocity)

    def set_max_velocity(self, velocity):
        self.motor.set_axis_parameter(self.motor.APs.MaxVelocity, velocity)

    def get_max_acceleration(self):
        return self.motor.get_axis_parameter(self.motor.APs.MaxAcceleration)

    def set_max_acceleration(self, acceleration):
        self.motor.set_axis_parameter(self.motor.APs.MaxAcceleration, acceleration)
