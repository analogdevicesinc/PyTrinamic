################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
 
from ...ic import TMCIc
from .TMC2262map import TMC2262Map
 
 
class TMC2262(TMCIc):
    """<chip-description>"""
     
    REGMAP = TMC2262Map(channel=1, block=0).ALL_REGISTERS
 
    def __init__(self):
        super().__init__("TMC2262", self.__doc__)