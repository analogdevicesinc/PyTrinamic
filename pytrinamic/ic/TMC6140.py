from ..ic.tmc_ic import TMCIc


class TMC6140(TMCIc):
    """
    TMC6140 is a fully integrated universal 3-phase MOSFET gate driver for PMSM servo or BLDC motors.
    External MOSFETs for up to 100 A motor current are supported. Supply voltage: 5-30V
    """
    def __init__(self):
        super().__init__("TMC6140", self.__doc__)
