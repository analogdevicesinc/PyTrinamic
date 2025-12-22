################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from ...ic import TMCIc
from .TMC2241map import TMC2241Map


class TMC2241(TMCIc):
    """65V 2ARMS  SMART INTEGRATED STEPPER DRIVER AND CONTROLLER"""

    REGMAP = TMC2241Map(channel=1, block=0).ALL_REGISTERS

    def __init__(self):
        super().__init__("TMC2241", self.__doc__)
