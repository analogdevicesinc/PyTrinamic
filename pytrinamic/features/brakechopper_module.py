################################################################################
# Copyright © 2021 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from ..features.brakechopper import BrakeChopper


class BrakeChopperModule(BrakeChopper):

    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps
        
    def set_enable_parameter(self, enable):
        self._parent.set_axis_parameter(self._aps.BrakeChopperEnabled, self._axis, enable)

    def get_enable_parameter(self):
        return self._parent.get_axis_parameter(self._aps.BrakeChopperEnabled, self._axis)
        
    def set_type_parameter(self, type):
        self._parent.set_axis_parameter(self._aps.BrakeChopperType, self._axis, type)

    def get_type_parameter(self):
        return self._parent.get_axis_parameter(self._aps.BrakeChopperType, self._axis)

    def set_voltage_limit_parameter(self, limit):
        self._parent.set_axis_parameter(self._aps.BrakeChopperVoltage, self._axis, limit)

    def get_voltage_limit_parameter(self):
        return self._parent.get_axis_parameter(self._aps.BrakeChopperVoltage, self._axis)

    def set_hysteresis_parameter(self, hysteresis):
        self._parent.set_axis_parameter(self._aps.BrakeChopperHysteresis, self._axis, hysteresis)

    def get_hysteresis_parameter(self):
        return self._parent.get_axis_parameter(self._aps.BrakeChopperHysteresis, self._axis)

    # properties
    enabled = property(get_enable_parameter, set_enable_parameter)
    type = property(get_type_parameter, set_type_parameter)
    voltage_limit = property(get_voltage_limit_parameter, set_voltage_limit_parameter)
    hystersis = property(get_hysteresis_parameter, set_hysteresis_parameter)

    def __str__(self):
        return "{} {}".format(
            "Brake Chopper",
            {
                "enabled": self.enabled,
                "type": self.type,
                "voltage_limit": self.voltage_limit,
                "hystersis": self.hystersis
            }
        )
