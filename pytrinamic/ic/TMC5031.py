from ..ic.tmc_ic import TMCIc


class TMC5031(TMCIc):
    """
    The TMC5031 is a cost-effective dual stepper motion controller and driver IC with serial communication interface.
    Supply voltage: 4,75-16V
    """
    def __init__(self):
        super().__init__("TMC5031", self.__doc__)

#   # Motion Control functions

#    def rotate(self, motor, value):
#        if not(0 <= motor < self.MOTORS):
#            raise ValueError

#        self.writeRegister(self.registers.AMAX[motor], 1000, self.__channel)

#        if value >= 0:
#            self.writeRegister(self.registers.VMAX[motor], value, self.__channel)
#            self.writeRegister(self.registers.RAMPMODE[motor], 1, self.__channel)
#        else:
#            self.writeRegister(self.registers.VMAX[motor], -value, self.__channel)
#            self.writeRegister(self.registers.RAMPMODE[motor], 2, self.__channel)

#    def stop(self, motor):
#        self.rotate(motor, 0)

#    def moveTo(self, motor, position, velocity):
#        if not(0 <= motor < self.MOTORS):
#            raise ValueError

#        self.writeRegister(self.registers.RAMPMODE[motor], 0, self.__channel)

#        if velocity != 0:
#            self.writeRegister(self.registers.VMAX[motor], velocity, self.__channel)

#        self.writeRegister(self.registers.XTARGET[motor], position, self.__channel)

    class REG:
        """
        Define all registers of the TMC5031.

        Each register is defined either as an integer or as a tuple of integers.
        Each integer represents a register address. Tuples of addresses are used to
        represent a register that exists multiple times for multiple motors.
        """
        GCONF         = 0x00
        GSTAT         = 0x01
        SLAVECONF     = 0x03
        INPUT         = 0x04
        X_COMPARE     = 0x05
        RAMPMODE      = (0x20, 0x40)
        XACTUAL       = (0x21, 0x41)
        VACTUAL       = (0x22, 0x42)
        VSTART        = (0x23, 0x43)
        A1            = (0x24, 0x44)
        V1            = (0x25, 0x45)
        AMAX          = (0x26, 0x46)
        VMAX          = (0x27, 0x47)
        DMAX          = (0x28, 0x48)
        D1            = (0x2A, 0x4A)
        VSTOP         = (0x2B, 0x4B)
        TZEROWAIT     = (0x2C, 0x4C)
        XTARGET       = (0x2D, 0x4D)
        IHOLD_IRUN    = (0x30, 0x50)
        VCOOLTHRS     = (0x31, 0x51)
        VHIGH         = (0x32, 0x52)
        SW_MODE       = (0x34, 0x54)
        RAMP_STAT     = (0x35, 0x55)
        XLATCH        = (0x36, 0x56)

        MSLUT0        = (0x60, 0x70)
        MSLUT1        = (0x61, 0x71)
        MSLUT2        = (0x62, 0x72)
        MSLUT3        = (0x63, 0x73)
        MSLUT4        = (0x64, 0x74)
        MSLUT5        = (0x65, 0x75)
        MSLUT6        = (0x66, 0x76)
        MSLUT7        = (0x67, 0x77)
        MSLUTSEL      = (0x68, 0x78)
        MSLUTSTART    = (0x69, 0x79)
        MSCNT         = (0x6A, 0x7A)
        MSCURACT      = (0x6B, 0x7B)
        CHOPCONF      = (0x6C, 0x7C)
        COOLCONF      = (0x6D, 0x7D)
        DRV_STATUS    = (0x6F, 0x7F)

    class FIELD:
        """
        Define all register bitfields of the TMC5031.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).
        Fields that are present multiple times in different registers (for multiple
        motors) all the bitfield tuples are bundled together into another tuple.

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """

        # GCONF
        POSCMP_ENABLE = (0x00, 0x00000008, 3)
        TEST_MODE     = (0x00, 0x00000080, 7)
        SHAFT1        = (0x00, 0x00000100, 8)
        SHAFT2        = (0x00, 0x00000200, 9)
        LOCK_GCONF    = (0x00, 0x00000400, 10)

        # GSTAT
        RESET         = (0x01, 0x00000001, 0)
        DRV_ERR1      = (0x01, 0x00000002, 1)
        UV_CP         = (0x01, 0x00000008, 3)

        # SLAVECONF
        TEST_SEL      = (0x03, 0x0000000F, 0)

        # INPUT
        DRV_ENN       = (0x04, 0x00000080, 7)
        VERSION       = (0x04, 0xFF000000, 24)

        # X_COMPARE
        X_COMPARE     = (0x05, 0xFFFFFFFF, 0)

        # RAMPMODE_M1
        RAMPMODE      = (0x20, 0x00000003, 0)

        # XACTUAL_M1
        XACTUAL       = (0x21, 0xFFFFFFFF, 0)

        # VACTUAL_M1
        VACTUAL       = (0x22, 0x00FFFFFF, 0)

        # VSTART_M1
        VSTART        = (0x23, 0x0003FFFF, 0)

        # A1_M1
        A1            = (0x24, 0x0000FFFF, 0)

        # V1_M1
        V1            = (0x25, 0x000FFFFF, 0)

        # AMAX_M1
        AMAX          = (0x26, 0x0000FFFF, 0)

        # VMAX_M1
        VMAX          = (0x27, 0x007FFFFF, 0)

        # DMAX_M1
        DMAX          = (0x28, 0x0000FFFF, 0)

        # D1_M1
        D1            = (0x2A, 0x0000FFFF, 0)

        # VSTOP_M1
        VSTOP         = (0x2B, 0x0003FFFF, 0)

        # TZEROWAIT_M1
        TZEROWAIT     = (0x2C, 0x0000FFFF, 0)

        # XTARGET_M1
        XTARGET       = (0x2D, 0xFFFFFFFF, 0)

        # IHOLD_IRUN_M1
        IHOLD         = (0x30, 0x0000001F, 0)
        IRUN          = (0x30, 0x00001F00, 8)
        IHOLDDELAY    = (0x30, 0x000F0000, 16)

        # VCOOLTHRS_M1
        VCOOLTHRS     = (0x31, 0x007FFFFF, 0)

        # VHIGH_M1
        VHIGH         = (0x32, 0x007FFFFF, 0)

        # SW_MODE_M1
        STOP_L_ENABLE     = (0x34, 0x00000001, 0)
        STOP_R_ENABLE     = (0x34, 0x00000002, 1)
        POL_STOP_L        = (0x34, 0x00000004, 2)
        POL_STOP_R        = (0x34, 0x00000008, 3)
        SWAP_LR           = (0x34, 0x00000010, 4)
        LATCH_L_ACTIVE    = (0x34, 0x00000020, 5)
        LATCH_L_INACTIVE  = (0x34, 0x00000040, 6)
        LATCH_R_ACTIVE    = (0x34, 0x00000080, 7)
        LATCH_R_INACTIVE  = (0x34, 0x00000100, 8)
        SG_STOP           = (0x34, 0x00000400, 10)
        EN_SOFTSTOP       = (0x34, 0x00000800, 11)

        # RAMP_STAT_M1
        STATUS_STOP_L     = (0x35, 0x00000001, 0)
        STATUS_STOP_R     = (0x35, 0x00000002, 1)
        STATUS_LATCH_L    = (0x35, 0x00000004, 2)
        STATUS_LATCH_R    = (0x35, 0x00000008, 3)
        EVENT_STOP_L      = (0x35, 0x00000010, 4)
        EVENT_STOP_R      = (0x35, 0x00000020, 5)
        EVENT_STOP_SG     = (0x35, 0x00000040, 6)
        EVENT_POS_REACHED = (0x35, 0x00000080, 7)
        VELOCITY_REACHED  = (0x35, 0x00000100, 8)
        POSITION_REACHED  = (0x35, 0x00000200, 9)
        VZERO             = (0x35, 0x00000400, 10)
        T_ZEROWAIT_ACTIVE = (0x35, 0x00000800, 11)
        SECOND_MOVE       = (0x35, 0x00001000, 12)
        STATUS_SG         = (0x35, 0x00002000, 13)

        # XLATCH_M1
        XLATCH            = (0x36, 0xFFFFFFFF, 0)

        # MSLUTSEL_M1
        W0                = (0x68, 0x00000003, 0)
        W1                = (0x68, 0x0000000C, 2)
        W2                = (0x68, 0x00000030, 4)
        W3                = (0x68, 0x000000C0, 6)
        X1                = (0x68, 0x0000FF00, 8)
        X2                = (0x68, 0x00FF0000, 16)
        X3                = (0x68, 0xFF000000, 24)

        # MSLUTSTART_M1
        START_SIN         = (0x69, 0x000000FF, 0)
        START_SIN90       = (0x69, 0x00FF0000, 16)

        # MSCNT_M1
        MSCNT             = (0x6A, 0x000003FF, 0)

        # MSCURACT_M1
        CUR_A             = (0x6B, 0x000001FF, 0)
        CUR_B             = (0x6B, 0x01FF0000, 16)

        # CHOPCONF_M1
        TOFF              = (0x6C, 0x0000000F, 0)
        TFD_2__0_         = (0x6C, 0x00000070, 4)
        OFFSET            = (0x6C, 0x00000780, 7)
        HSTRT             = (0x6C, 0x00000070, 4)
        HEND              = (0x6C, 0x00000780, 7)
        TFD__             = (0x6C, 0x00000800, 11)
        DISFDCC           = (0x6C, 0x00001000, 12)
        RNDTF             = (0x6C, 0x00002000, 13)
        CHM               = (0x6C, 0x00004000, 14)
        TBL               = (0x6C, 0x00018000, 15)
        VSENSE            = (0x6C, 0x00020000, 17)
        VHIGHFS           = (0x6C, 0x00040000, 18)
        VHIGHCHM          = (0x6C, 0x00080000, 19)
        SYNC              = (0x6C, 0x00F00000, 20)
        DISS2G            = (0x6C, 0x40000000, 30)

        # COOLCONF_M1
        SEMIN             = (0x6D, 0x0000000F, 0)
        SEUP              = (0x6D, 0x00000060, 5)
        SEMAX             = (0x6D, 0x00000F00, 8)
        SEDN              = (0x6D, 0x00006000, 13)
        SEIMIN            = (0x6D, 0x00008000, 15)
        SGT               = (0x6D, 0x007F0000, 16)
        SFILT             = (0x6D, 0x01000000, 24)

        # DRV_STATUS_M1
        SG_RESULT         = (0x6F, 0x000003FF, 0)
        FSACTIVE          = (0x6F, 0x00008000, 15)
        CS_ACTUAL         = (0x6F, 0x001F0000, 16)
        STALLGUARD        = (0x6F, 0x01000000, 24)
        OT                = (0x6F, 0x02000000, 25)
        OTPW              = (0x6F, 0x04000000, 26)
        S2GA              = (0x6F, 0x08000000, 27)
        S2GB              = (0x6F, 0x10000000, 28)
        OLA               = (0x6F, 0x20000000, 29)
        OLB               = (0x6F, 0x40000000, 30)
        STST              = (0x6F, 0x80000000, 31)
