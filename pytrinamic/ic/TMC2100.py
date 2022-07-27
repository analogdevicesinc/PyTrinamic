from ..ic.tmc_ic import TMCIc


class TMC2100(TMCIc):
    """
    The TMC2100 is a standalone driver IC for two-phase stepper motors. Supply voltage: 4.75 - 46V.
    """
    def __init__(self):
        super().__init__("TMC2100", self.__doc__)

    class REG:
        """
        Define all registers of the TMC2100.
        """
        GCONF  = 0x00

    class FIELD:
        """
        Define all register bitfields of the TMC2100.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """
        # GCONF
        GCONF = (0x00, 0xFFFFFFFF, 0)
