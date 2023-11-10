################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

from abc import ABC, abstractmethod

class SolenoidControl(ABC):
    """
    Solenoid control implementation
    """
    def __init__(self, parent, axis):
        self._parent = parent
        self._axis = axis
    
    @abstractmethod
    def set_high(self):
        """
        Apply high voltage.
        """
        raise NotImplementedError

    @abstractmethod
    def set_low(self):
        """
        Apply low voltage.
        """
        raise NotImplementedError
