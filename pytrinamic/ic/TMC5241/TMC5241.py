################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from ...ic import TMCIc
from .TMC5241map import TMC5241Map


class TMC5241(TMCIc):
    """65V 3ARMS  SMART INTEGRATED STEPPER DRIVER AND CONTROLLER"""
    
    REGMAP = TMC5241Map(channel=0, block=0).ALL_REGISTERS

    def __init__(self):
        super().__init__("TMC5241", self.__doc__)