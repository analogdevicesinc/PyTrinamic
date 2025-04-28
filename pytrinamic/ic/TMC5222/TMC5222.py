################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
 
from ...ic import TMCIc
from .TMC5222map import TMC5222Map
 
 
class TMC5222(TMCIc):
    """<chip-description>"""
     
    REGMAP = TMC5222Map(channel=0, block=0).ALL_REGISTERS
 
    def __init__(self):
        super().__init__("TMC5222", self.__doc__)