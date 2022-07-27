from ..ic.tmc_ic import TMCIc


class TMC2660(TMCIc):
    """
    The TMC2660 is a driver for two-phase stepper motors. Supply voltage: up to 30V
    """
    def __init__(self):
        super().__init__("TMC2660", self.__doc__)

    class REG:
        """
        Define all registers of the TMC2660.
        """
        DRVSTATUS_MSTEP    = 0x00
        DRVSTATUS_SG       = 0x01
        DRVSTATUS_SG_SE    = 0x02
        DRVCTRL            = 0x08
        CHOPCONF           = 0x0C
        SMARTEN            = 0x0D
        SGCSCONF           = 0x0E
        DRVCONF            = 0x0F

    class FIELD:
        """
        Define all register bitfields of the TMC2660.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        # DRVSTATUS / MSTEP
        MSTEP                  = (0x00, 0x000FFC00, 10)
        STST                   = (0x00, 0x00000080,  7)
        OLB                    = (0x00, 0x00000040,  6)
        OLA                    = (0x00, 0x00000020,  5)
        S2GB                   = (0x00, 0x00000010,  4)
        S2GA                   = (0x00, 0x00000008,  3)
        OTPW                   = (0x00, 0x00000004,  2)
        OT                     = (0x00, 0x00000002,  1)
        SG                     = (0x00, 0x00000001,  0)

        # DRVSTATUS / SG
        SG                     = (0x01, 0x000FFC00, 10)
        STST                   = (0x01, 0x00000080,  7)
        OLB                    = (0x01, 0x00000040,  6)
        OLA                    = (0x01, 0x00000020,  5)
        S2GB                   = (0x01, 0x00000010,  4)
        S2GA                   = (0x01, 0x00000008,  3)
        OTPW                   = (0x01, 0x00000004,  2)
        OT                     = (0x01, 0x00000002,  1)
        SG                     = (0x01, 0x00000001,  0)

        # DRVSTATUS / SG_SE
        SG                     = (0x02, 0x000F8000, 15)
        SE                     = (0x02, 0x00007C00, 10)
        STST                   = (0x02, 0x00000080,  7)
        OLB                    = (0x02, 0x00000040,  6)
        OLA                    = (0x02, 0x00000020,  5)
        S2GB                   = (0x02, 0x00000010,  4)
        S2GA                   = (0x02, 0x00000008,  3)
        OTPW                   = (0x02, 0x00000004,  2)
        OT                     = (0x02, 0x00000002,  1)
        SG                     = (0x02, 0x00000001,  0)

        # DRVCTRL
        INTPOL                 = (0x08, 0x00000200,  9)
        DEDGE                  = (0x08, 0x00000100,  8)
        MRES                   = (0x08, 0x0000000F,  0)

        PHA                    = (0x08, 0x00020000, 17)
        CA                     = (0x08, 0x0001FE00,  9)
        PHB                    = (0x08, 0x00000100,  8)
        CB                     = (0x08, 0x000000FF,  0)

        # CHOPCONF
        REGISTER_ADDRESS_BITS  = (0x0C, 0x000E0000, 17)
        TBL                    = (0x0C, 0x00018000, 15)
        CHM                    = (0x0C, 0x00004000, 14)
        RNDTF                  = (0x0C, 0x00002000, 13)
        HDEC                   = (0x0C, 0x00001800, 11)
        HEND                   = (0x0C, 0x00000780,  7)
        HDEC1                  = (0x0C, 0x00002000, 12)
        HEND                   = (0x0C, 0x00000780,  7)
        HSTRT                  = (0x0C, 0x00000070,  3)
        TOFF                   = (0x0C, 0x0000000F,  0)

        # SMARTEN
        SEIMIN                 = (0x0D, 0x00008000, 15)
        SEDN                   = (0x0D, 0x00006000, 13)
        SEUP                   = (0x0D, 0x00000060,  5)
        SEMAX                  = (0x0D, 0x00000F00,  8)
        SEMIN                  = (0x0D, 0x0000000F,  0)

        # SGCSCONF
        SFILT                  = (0x0E, 0x00010000, 16)
        SGT                    = (0x0E, 0x00007F00,  8)
        CS                     = (0x0E, 0x0000001F,  0)

        # DRVCONF
        TST                    = (0x0F, 0x00010000, 16)
        SLPH                   = (0x0F, 0x0000C000, 14)
        SLPL                   = (0x0F, 0x00003000, 12)
        DISS2G                 = (0x0F, 0x00000400, 10)
        TS2G                   = (0x0F, 0x00000300,  8)
        SDOFF                  = (0x0F, 0x00000080,  7)
        VSENSE                 = (0x0F, 0x00000040,  6)
        RDSEL                  = (0x0F, 0x00000030,  4)
