################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from abc import ABC, abstractmethod


class PID(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    # torque/flux controller

    @abstractmethod
    def set_torque_p_parameter(self, p_value):
        raise NotImplementedError

    @abstractmethod
    def get_torque_p_parameter(self):
        raise NotImplementedError

    @abstractmethod
    def set_torque_i_parameter(self, i_value):
        raise NotImplementedError

    @abstractmethod
    def get_torque_i_parameter(self):
        raise NotImplementedError

    # velocity controller "

    @abstractmethod
    def set_velocity_p_parameter(self, p_value):
        raise NotImplementedError

    @abstractmethod
    def get_velocity_p_parameter(self):
        raise NotImplementedError

    @abstractmethod
    def set_velocity_i_parameter(self, i_value):
        raise NotImplementedError

    @abstractmethod
    def get_velocity_i_parameter(self):
        raise NotImplementedError

    # position controller

    @abstractmethod
    def set_position_p_parameter(self, p_value):
        raise NotImplementedError

    @abstractmethod
    def get_position_p_parameter(self):
        raise NotImplementedError
