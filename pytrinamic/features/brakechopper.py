################################################################################
# Copyright © 2021 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from abc import ABC, abstractmethod


class BrakeChopper(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis
        
    @abstractmethod
    def set_enable_parameter(self, enable):
        raise NotImplementedError

    @abstractmethod
    def get_enable_parameter(self):
        raise NotImplementedError
        
    @abstractmethod
    def set_type_parameter(self, type):
        raise NotImplementedError

    @abstractmethod
    def get_type_parameter(self):
        raise NotImplementedError

    @abstractmethod
    def set_voltage_limit_parameter(self, limit):
        raise NotImplementedError

    @abstractmethod
    def get_voltage_limit_parameter(self):
        raise NotImplementedError

    @abstractmethod
    def set_hysteresis_parameter(self, hysteresis):
        raise NotImplementedError

    @abstractmethod
    def get_hysteresis_parameter(self):
        raise NotImplementedError
