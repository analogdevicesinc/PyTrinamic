################################################################################
# Copyright © 2021 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from abc import ABC, abstractmethod


class ReferenceSwitches(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis
        
    @abstractmethod
    def set_enable_right_switch(self, enable):
        raise NotImplementedError
                                             
    @abstractmethod
    def get_enable_right_switch(self):
        raise NotImplementedError
        
    @abstractmethod
    def set_enable_left_switch(self, enable):
        raise NotImplementedError
                                             
    @abstractmethod
    def get_enable_left_switch(self):
        raise NotImplementedError

    @abstractmethod
    def set_polarity_right_switch(self, enable):
        raise NotImplementedError

    @abstractmethod
    def get_polarity_right_switch(self):
        raise NotImplementedError

    @abstractmethod
    def set_polarity_left_switch(self, enable):
        raise NotImplementedError

    @abstractmethod
    def get_polarity_left_switch(self):
        raise NotImplementedError

    @abstractmethod
    def get_right_switch_parameter(self):
        raise NotImplementedError

    @abstractmethod
    def get_left_switch_parameter(self):
        raise NotImplementedError
