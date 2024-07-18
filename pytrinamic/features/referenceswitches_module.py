################################################################################
# Copyright © 2021 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from ..features.referenceswitches import ReferenceSwitches


class ReferenceSwitchesModule(ReferenceSwitches):

    def __init__(self, module, axis, aps):
        super().__init__(module, axis)
        self._aps = aps
        self._rightSwitchPosition = 0
        self._leftSwitchPosition = 1
        
    def set_enable_right_switch(self, enable):
        old_state = self._parent.get_axis_parameter(self._aps.ReferenceSwitchEnable, self._axis)
        new_state = (old_state | (1 << self._rightSwitchPosition)) if enable else (old_state & (~(1 << self._rightSwitchPosition)))
        self._parent.set_axis_parameter(self._aps.ReferenceSwitchEnable, self._axis, new_state)
                                             
    def get_enable_right_switch(self):
        old_state = self._parent.get_axis_parameter(self._aps.ReferenceSwitchEnable, self._axis)
        right_switch_state = old_state & (1 << self._rightSwitchPosition)
        return right_switch_state >> self._rightSwitchPosition
        
    def set_enable_left_switch(self, enable):
        old_state = self._parent.get_axis_parameter(self._aps.ReferenceSwitchEnable, self._axis)
        new_state = (old_state | (1 << self._leftSwitchPosition)) if enable else (old_state & (~(1 << self._leftSwitchPosition)))
        self._parent.set_axis_parameter(self._aps.ReferenceSwitchEnable, self._axis, new_state)
                                             
    def get_enable_left_switch(self):
        old_state = self._parent.get_axis_parameter(self._aps.ReferenceSwitchEnable, self._axis)
        left_switch_state = old_state & (1 << self._leftSwitchPosition)
        return left_switch_state >> self._leftSwitchPosition

    def set_polarity_right_switch(self, enable):
        old_polarity = self._parent.get_axis_parameter(self._aps.ReferenceSwitchPolarity, self._axis)
        new_polarity = (old_polarity | (1 << self._rightSwitchPosition)) if enable else (old_polarity & (~(1 << self._rightSwitchPosition)))
        self._parent.set_axis_parameter(self._aps.ReferenceSwitchPolarity, self._axis, new_polarity)

    def get_polarity_right_switch(self):
        old_polarity = self._parent.get_axis_parameter(self._aps.ReferenceSwitchPolarity, self._axis)
        right_switch_polarity = old_polarity & (1 << self._rightSwitchPosition)
        return right_switch_polarity >> self._rightSwitchPosition

    def set_polarity_left_switch(self, enable):
        old_polarity = self._parent.get_axis_parameter(self._aps.ReferenceSwitchPolarity, self._axis)
        new_polarity = (old_polarity | (1 << self._leftSwitchPosition)) if enable else (old_polarity & (~(1 << self._leftSwitchPosition)))
        self._parent.set_axis_parameter(self._aps.ReferenceSwitchPolarity, self._axis, new_polarity)

    def get_polarity_left_switch(self):
        old_polarity = self._parent.get_axis_parameter(self._aps.ReferenceSwitchPolarity, self._axis)
        left_switch_polarity = old_polarity & (1 << self._leftSwitchPosition)
        return left_switch_polarity >> self._leftSwitchPosition

    def get_right_switch_parameter(self):
        return self._parent.get_axis_parameter(self._aps.RightStopSwitch, self._axis)

    def get_left_switch_parameter(self):
        return self._parent.get_axis_parameter(self._aps.LeftStopSwitch, self._axis)

    enable_right_switch     = property(get_enable_right_switch, set_enable_right_switch)
    enable_left_switch      = property(get_enable_left_switch, set_enable_left_switch)
    polarity_right_switch   = property(get_polarity_right_switch, set_polarity_right_switch)
    polarity_left_switch    = property(get_polarity_left_switch, set_polarity_left_switch)

    def __str__(self):
        return "{} {}".format(
            "Reference Switches",
            {
                "enenable_right_switchabled": self.enable_right_switch,
                "enable_left_switch": self.enable_left_switch,
                "polarity_right_switch": self.polarity_right_switch,
                "polarity_left_switch": self.polarity_left_switch
            }
        )
