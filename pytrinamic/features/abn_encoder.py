################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from abc import ABC, abstractmethod


class ABNEncoder(ABC):

    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis

    @abstractmethod
    def set_resolution(self, steps):
        raise NotImplementedError

    @abstractmethod
    def get_resolution(self):
        raise NotImplementedError

    @abstractmethod
    def set_direction(self, direction):
        raise NotImplementedError

    @abstractmethod
    def get_direction(self):
        raise NotImplementedError

    @abstractmethod
    def set_init_mode(self, mode):
        raise NotImplementedError

    @abstractmethod
    def get_init_mode(self):
        raise NotImplementedError

    @abstractmethod
    def clear_once_on_n_channel(self):
        raise NotImplementedError
