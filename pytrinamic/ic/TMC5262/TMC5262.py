################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
 
from ...ic import TMCIc
from .TMC5262map import TMC5262Map
 
 
class TMC5262(TMCIc):
    """<chip-description>"""
     
    REGMAP = TMC5262Map(channel=0, block=0).ALL_REGISTERS
 
    def __init__(self):
        super().__init__("TMC5262", self.__doc__)