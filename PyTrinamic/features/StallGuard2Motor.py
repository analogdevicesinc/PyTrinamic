# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2Motor(StallGuard2):

    # Feature initialization
    def __init__(self, motor):
        self.motor = motor

    # Setters and getters for feature parameters

    def set_filter(self, filter):
        self.motor.set_axis_parameter(self.motor.APs.SG2FilterEnable, filter)

    def set_threshold(self, threshold):
        self.motor.set_axis_parameter(self.motor.APs.SG2Threshold, threshold)

    def set_stop_velocity(self, velocity):
        self.motor.set_axis_parameter(self.motor.APs.SmartEnergyStallVelocity, velocity)

    def get_filter(self):
        return self.motor.get_axis_parameter(self.motor.APs.SG2FilterEnable)

    def get_threshold(self):
        return self.motor.get_axis_parameter(self.motor.APs.SG2Threshold)

    def get_stop_velocity(self):
        return self.motor.get_axis_parameter(self.motor.APs.SmartEnergyStallVelocity)

    # Properties
    filter = property(get_filter, set_filter)
    threshold = property(get_threshold, set_threshold)
    stop_velocity = property(get_stop_velocity, set_stop_velocity)
