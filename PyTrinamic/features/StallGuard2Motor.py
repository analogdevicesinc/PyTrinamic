# Created on: 14.06.2021
# Author: LK

from PyTrinamic.features.StallGuard2 import StallGuard2

class StallGuard2Motor(StallGuard2):

    def __init__(self, motor):
        self.motor = motor

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
