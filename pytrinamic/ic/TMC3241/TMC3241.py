################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

from ...ic import TMCIc
from .TMC3241map import TMC3241Map


class TMC3241(TMCIc):
    """65V/4.2A, Fully-Integrated, Smart, Three-Phase Stepper Motor Driver"""

    REGMAP = TMC3241Map(channel=0, block=0).ALL_REGISTERS

    def __init__(self):
        super().__init__("TMC3241", self.__doc__)
