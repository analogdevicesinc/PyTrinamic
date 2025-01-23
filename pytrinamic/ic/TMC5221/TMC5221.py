
################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
 
from ...ic import TMCIc
from .TMC5221map import TMC5221Map
 
 
class TMC5221(TMCIc):
    """<chip-description>"""
     
    REGMAP = TMC5221Map(channel=0, block=0).ALL_REGISTERS
 
    def __init__(self):
        super().__init__("TMC5221", self.__doc__)