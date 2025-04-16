################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################
 
from ...ic import TMCIc
from .MAX22215map import MAX22215Map
 
 
class MAX22215(TMCIc):
    """ Motor Brake Driver with Current Sense Amplifier and Advanced Diagnostics"""
     
    REGMAP = MAX22215Map(channel=1, block=0).ALL_REGISTERS
 
    def __init__(self):
        super().__init__("MAX22215", self.__doc__)