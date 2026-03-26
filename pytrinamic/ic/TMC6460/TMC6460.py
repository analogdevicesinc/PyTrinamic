################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

from ...ic import TMCIc
from .TMC6460map import TMC6460Map


class TMC6460(TMCIc):
    """TMC6460 - Fully Integrated FOC BLDC drive

    The TMC6460 is the first fully integrated Servo Drive IC
    including FOC controller, power stage, current sensing
    and feedback engine all in one chip. Highly integrated,
    the TMC6460 enables the design of FOC position /
    speed / torque motion control with unrivalled
    miniaturization.
    """
    REGMAP = TMC6460Map(channel=0)

    def __init__(self):
        super().__init__("TMC6460", self.__doc__)
