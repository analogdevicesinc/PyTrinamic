from ..ic.tmc_ic import TMCIc


class TMC6300(TMCIc):
    """
    The TMC6300 is a highly efficient low voltage, zero standby current driver for 3-Phase BLDC/PMSM motors
    up to 2A. Supply voltage: 2-11V
    """
    def __init__(self):
        super().__init__("TMC6300", self.__doc__)
