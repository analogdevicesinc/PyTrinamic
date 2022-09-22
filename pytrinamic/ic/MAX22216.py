from ..ic.tmc_ic import TMCIc

from ..features.solenoid_ic import SolenoidIC
from ..features.solenoid_control_ic import SolenoidControlIC

class MAX22216(TMCIc):
    """
    QUAD SERIAL PROGRAMMABLE 2A HALF BRIDGE DRIVER
    """
    def __init__(self, parent_eval):
        """
        Constructor for the TMC_IC instance.

        Parameters:
        handler: Handler object for register access operations.
        This object is expected to implement write_register and read_register functions
        to read/write registers via platform-specific communication.
        channel: Channel identifier for this IC. This will be handed to the
        write_register and read_register functions of the handler to differentiate
        between multiple ICs.
        """
        super().__init__("MAX22216", self.__doc__)
        self._parent = parent_eval
        self.motors = [
            self._MotorTypeA(parent_eval, self, 0),
            self._MotorTypeA(parent_eval, self, 1),
            self._MotorTypeA(parent_eval, self, 2),
            self._MotorTypeA(parent_eval, self, 3)
        ]

    class _MotorTypeA(SolenoidIC, SolenoidControlIC):
        """
        Motor class for the generic motor.
        """
        def __init__(self, parent_eval, ic, axis):
            SolenoidIC.__init__(self, parent_eval, ic, axis)
            SolenoidControlIC.__init__(self, parent_eval, ic, axis)

    class REG:
        """
        Define all registers of the MAX22216.

        Each register is defined either as an integer or as a tuple of integers.
        Each integer represents a register address. Tuples of addresses are used to
        represent a register that exists multiple times for multiple motors.
        """
        GLOBAL_CTRL         = 0x00
        GLOBAL_CFG          = 0x01
        STATUS              = 0x02
        STATUS_CFG          = 0x03
        DEMAG_VOLTAGE       = 0x04
        ADC_VM_MEASUREMENT  = 0x05
        VM_THRESHOLD        = 0x06
        F_AC                = 0x07
        U_AC_SCAN           = 0x08
        CFG_DC_L2H_0        = 0x09
        CFG_DC_H_0          = 0x0A
        CFG_DC_L_0          = 0x0B
        CFG_L2H_TIME_0      = 0x0C
        CFG_CTRL0_0         = 0x0D
        CFG_CTRL1_0         = 0x0E
        CFG_DPM0_0          = 0x0F
        CFG_DPM1_0          = 0x10
        CFG_DC_0            = 0x11
        CFG_R_THLD_0        = 0x12
        CFG_IND_0_0         = 0x13
        CFG_IND_1_0         = 0x14
        CFG_P_0             = 0x15
        CFG_I_0             = 0x16
        CFG_DC_L2H_1        = 0x17
        CFG_DC_H_1          = 0x18
        CFG_DC_L_1          = 0x19
        CFG_L2H_TIME_1      = 0x1A
        CFG_CTRL0_1         = 0x1B
        CFG_CTRL1_1         = 0x1C
        CFG_DPM0_1          = 0x1D
        CFG_DPM1_1          = 0x1E
        CFG_DC_1            = 0x1F
        CFG_R_THLD_1        = 0x20
        CFG_IND_0_1         = 0x21
        CFG_IND_1_1         = 0x22
        CFG_P_1             = 0x23
        CFG_I_1             = 0x24
        CFG_DC_L2H_2        = 0x25
        CFG_DC_H_2          = 0x26
        CFG_DC_L_2          = 0x27
        CFG_L2H_TIME_2      = 0x28
        CFG_CTRL0_2         = 0x29
        CFG_CTRL1_2         = 0x2A
        CFG_DPM0_2          = 0x2B
        CFG_DPM1_2          = 0x2C
        CFG_DC_2            = 0x2D
        CFG_R_THLD_2        = 0x2E
        CFG_IND_0_2         = 0x2F
        CFG_IND_1_2         = 0x30
        CFG_P_2             = 0x31
        CFG_I_2             = 0x32
        CFG_DC_L2H_3        = 0x33
        CFG_DC_H_3          = 0x34
        CFG_DC_L_3          = 0x35
        CFG_L2H_TIME_3      = 0x36
        CFG_CTRL0_3         = 0x37
        CFG_CTRL1_3         = 0x38
        CFG_DPM0_3          = 0x39
        CFG_DPM1_3          = 0x3A
        CFG_DC_3            = 0x3B
        CFG_R_THLD_3        = 0x3C
        CFG_IND_0_3         = 0x3D
        CFG_IND_1_3         = 0x3E
        CFG_P_3             = 0x3F
        CFG_I_3             = 0x40
        I_DPM_PEAK_0        = 0x41
        I_DPM_VALLEY_0      = 0x42
        TRAVEL_TIME_0       = 0x43
        REACTION_TIME_0     = 0x44
        I_ADC_0             = 0x45
        I_DC_0              = 0x46
        I_IND_AC_0          = 0x47
        R_0                 = 0x48
        PWM_DUTY_0          = 0x49
        I_DPM_PEAK_1        = 0x4A
        I_DPM_VALLEY_1      = 0x4B
        TRAVEL_TIME_1       = 0x4C
        REACTION_TIME_1     = 0x4D
        I_ADC_1             = 0x4E
        I_DC_1              = 0x4F
        I_IND_AC_1          = 0x50
        R_1                 = 0x51
        PWM_DUTY_1          = 0x52
        I_DPM_PEAK_2        = 0x53
        I_DPM_VALLEY_2      = 0x54
        TRAVEL_TIME_2       = 0x55
        REACTION_TIME_2     = 0x56
        I_ADC_2             = 0x57
        I_DC_2              = 0x58
        I_IND_AC_2          = 0x59
        R_2                 = 0x5A
        PWM_DUTY_2          = 0x5B
        I_DPM_PEAK_3        = 0x5C
        I_DPM_VALLEY_3      = 0x5D
        TRAVEL_TIME_3       = 0x5E
        REACTION_TIME_3     = 0x5F
        I_ADC_3             = 0x60
        I_DC_3              = 0x61
        I_IND_AC_3          = 0x62
        R_3                 = 0x63
        PWM_DUTY_3          = 0x64
        FAULT0              = 0x65
        FAULT1              = 0x66

    class FIELD:
        """
        Define all register bitfields of the MAX22216.

        Each field is defined as a tuple consisting of ( Address, Mask, Shift ).

        The name of the register is written as a comment behind each tuple. This is
        intended for IDE users viewing the definition of a field by hovering over
        it. This allows the user to see the corresponding register name of a field
        without opening this file and searching for the definition.
        """
        CNTL0                     = ( 0x00, 0x00000001,  0 )
        CNTL1                     = ( 0x00, 0x00000002,  1 )
        CNTL2                     = ( 0x00, 0x00000004,  2 )
        CNTL3                     = ( 0x00, 0x00000008,  3 )
        F_PWM_M                   = ( 0x00, 0x000000F0,  4 )
        CHS                       = ( 0x01, 0x0000000F,  0 )
        VDR_NDUTY                 = ( 0x01, 0x00000010,  4 )
        STAT_POL                  = ( 0x01, 0x00000040,  6 )
        CNTL_POL                  = ( 0x01, 0x00000080,  7 )
        M_UVM                     = ( 0x01, 0x00000100,  8 )
        M_COMF                    = ( 0x01, 0x00000200,  9 )
        M_DPM                     = ( 0x01, 0x00000400, 10 )
        M_HHF                     = ( 0x01, 0x00000800, 11 )
        M_OLF                     = ( 0x01, 0x00001000, 12 )
        M_OCP                     = ( 0x01, 0x00002000, 13 )
        M_OVT                     = ( 0x01, 0x00004000, 14 )
        ACTIVE                    = ( 0x01, 0x00008000, 15 )
        RFU                       = ( 0x02, 0x00000001,  0 )
        UVM                       = ( 0x02, 0x00000002,  1 )
        COMER                     = ( 0x02, 0x00000004,  2 )
        DPM                       = ( 0x02, 0x00000008,  3 )
        HHF                       = ( 0x02, 0x00000010,  4 )
        OLF                       = ( 0x02, 0x00000020,  5 )
        OCP                       = ( 0x02, 0x00000040,  6 )
        OVT                       = ( 0x02, 0x00000080,  7 )
        IND                       = ( 0x02, 0x00000100,  8 )
        RES                       = ( 0x02, 0x00000200,  9 )
        MIN_T_ON                  = ( 0x02, 0x00000400, 10 )
        STAT0                     = ( 0x02, 0x00000800, 11 )
        STAT1                     = ( 0x02, 0x00001000, 12 )
        STAT2                     = ( 0x02, 0x00002000, 13 )
        STAT3                     = ( 0x02, 0x00004000, 14 )
        STAT_FUN                  = ( 0x03, 0x00000007,  0 )
        STAT_SEL0                 = ( 0x03, 0x00000008,  3 )
        STAT_SEL1                 = ( 0x03, 0x00000010,  4 )
        STRETCH_EN                = ( 0x03, 0x00000060,  5 )
        EN_LDO                    = ( 0x03, 0x00000080,  7 )
        V5_NV3                    = ( 0x03, 0x00000100,  8 )
        M_UVM_CMP                 = ( 0x03, 0x00000200,  9 )
        DC_H2L                    = ( 0x04, 0x0000FFFF,  0 )
        ADC_VM_RAW                = ( 0x05, 0x00001FFF,  0 )
        VM_THLD_DOWN              = ( 0x06, 0x0000000F,  0 )
        VM_THLD_UP                = ( 0x06, 0x000000F0,  4 )
        DELTA_PHI                 = ( 0x07, 0x00000FFF,  0 )
        U_AC                      = ( 0x08, 0x00007FFF,  0 )
        DC_L2H_0                  = ( 0x09, 0x0000FFFF,  0 )
        DC_H_0                    = ( 0x0A, 0x0000FFFF,  0 )
        DC_L_0                    = ( 0x0B, 0x0000FFFF,  0 )
        TIME_L2H_0                = ( 0x0C, 0x0000FFFF,  0 )
        RAMP_0                    = ( 0x0D, 0x000000FF,  0 )
        RUPE_0                    = ( 0x0D, 0x00000100,  8 )
        RMDE_0                    = ( 0x0D, 0x00000200,  9 )
        RDWE_0                    = ( 0x0D, 0x00000400, 10 )
        H2L_EN_0                  = ( 0x0D, 0x00000800, 11 )
        OL_EN_0                   = ( 0x0D, 0x00001000, 12 )
        HHF_EN_0                  = ( 0x0D, 0x00002000, 13 )
        CTRL_MODE_0               = ( 0x0D, 0x0000C000, 14 )
        FSF_0                     = ( 0x0E, 0x00000003,  0 )
        SHUNT_SCALE_0             = ( 0x0E, 0x0000000C,  2 )
        SLEW_RATE_0               = ( 0x0E, 0x00000030,  4 )
        T_BLANKING_0              = ( 0x0E, 0x000000C0,  6 )
        F_PWM_0                   = ( 0x0E, 0x00000300,  8 )
        HSNLS_0                   = ( 0x0E, 0x00000400, 10 )
        DPM_THLD_0                = ( 0x0F, 0x00000FFF,  0 )
        DPM_MIN_CURRENT_0         = ( 0x10, 0x000000FF,  0 )
        DPM_MIN_NBR_0             = ( 0x10, 0x00000F00,  8 )
        END_HIT_AUTO_0            = ( 0x10, 0x00001000, 12 )
        END_HIT_START_HIZ_AUTO_0  = ( 0x10, 0x00002000, 13 )
        DPM_EN_0                  = ( 0x10, 0x00004000, 14 )
        IDC_THLD_0                = ( 0x11, 0x0000FFFF,  0 )
        RES_THLD_0                = ( 0x12, 0x0000FFFF,  0 )
        L_NBR_CALC_0              = ( 0x13, 0x0000000F,  0 )
        L_MEAS_WCYCLES_0          = ( 0x13, 0x000000F0,  4 )
        L_MEAS_H_0                = ( 0x13, 0x00000100,  8 )
        L_MEAS_L2H_0              = ( 0x13, 0x00000200,  9 )
        L_MEAS_EN_0               = ( 0x13, 0x00000400, 10 )
        DITH_EN_0                 = ( 0x13, 0x00000800, 11 )
        IAC_THLD_0                = ( 0x14, 0x00000FFF,  0 )
        CFG_P_0                   = ( 0x15, 0x0000FFFF,  0 )
        CFG_I_0                   = ( 0x16, 0x0000FFFF,  0 )
        DC_L2H_1                  = ( 0x17, 0x0000FFFF,  0 )
        DC_H_1                    = ( 0x18, 0x0000FFFF,  0 )
        DC_L_1                    = ( 0x19, 0x0000FFFF,  0 )
        TIME_L2H_1                = ( 0x1A, 0x0000FFFF,  0 )
        RAMP_1                    = ( 0x1B, 0x000000FF,  0 )
        RUPE_1                    = ( 0x1B, 0x00000100,  8 )
        RMDE_1                    = ( 0x1B, 0x00000200,  9 )
        RDWE_1                    = ( 0x1B, 0x00000400, 10 )
        H2L_EN_1                  = ( 0x1B, 0x00000800, 11 )
        OL_EN_1                   = ( 0x1B, 0x00001000, 12 )
        HHF_EN_1                  = ( 0x1B, 0x00002000, 13 )
        CTRL_MODE_1               = ( 0x1B, 0x0000C000, 14 )
        FSF_1                     = ( 0x1C, 0x00000003,  0 )
        SHUNT_SCALE_1             = ( 0x1C, 0x0000000C,  2 )
        SLEW_RATE_1               = ( 0x1C, 0x00000030,  4 )
        T_BLANKING_1              = ( 0x1C, 0x000000C0,  6 )
        F_PWM_1                   = ( 0x1C, 0x00000300,  8 )
        HSNLS_1                   = ( 0x1C, 0x00000400, 10 )
        DPM_THLD_1                = ( 0x1D, 0x00000FFF,  0 )
        DPM_MIN_CURRENT_1         = ( 0x1E, 0x000000FF,  0 )
        DPM_MIN_NBR_1             = ( 0x1E, 0x00000F00,  8 )
        END_HIT_AUTO_1            = ( 0x1E, 0x00001000, 12 )
        END_HIT_START_HIZ_AUTO_1  = ( 0x1E, 0x00002000, 13 )
        DPM_EN_1                  = ( 0x1E, 0x00004000, 14 )
        IDC_THLD_1                = ( 0x1F, 0x0000FFFF,  0 )
        RES_THLD_1                = ( 0x20, 0x0000FFFF,  0 )
        L_NBR_CALC_1              = ( 0x21, 0x0000000F,  0 )
        L_MEAS_WCYCLES_1          = ( 0x21, 0x000000F0,  4 )
        L_MEAS_H_1                = ( 0x21, 0x00000100,  8 )
        L_MEAS_L2H_1              = ( 0x21, 0x00000200,  9 )
        L_MEAS_EN_1               = ( 0x21, 0x00000400, 10 )
        DITH_EN_1                 = ( 0x21, 0x00000800, 11 )
        IAC_THLD_1                = ( 0x22, 0x00000FFF,  0 )
        CFG_P_1                   = ( 0x23, 0x0000FFFF,  0 )
        CFG_I_1                   = ( 0x24, 0x0000FFFF,  0 )
        DC_L2H_2                  = ( 0x25, 0x0000FFFF,  0 )
        DC_H_2                    = ( 0x26, 0x0000FFFF,  0 )
        DC_L_2                    = ( 0x27, 0x0000FFFF,  0 )
        TIME_L2H_2                = ( 0x28, 0x0000FFFF,  0 )
        RAMP_2                    = ( 0x29, 0x000000FF,  0 )
        RUPE_2                    = ( 0x29, 0x00000100,  8 )
        RMDE_2                    = ( 0x29, 0x00000200,  9 )
        RDWE_2                    = ( 0x29, 0x00000400, 10 )
        H2L_EN_2                  = ( 0x29, 0x00000800, 11 )
        OL_EN_2                   = ( 0x29, 0x00001000, 12 )
        HHF_EN_2                  = ( 0x29, 0x00002000, 13 )
        CTRL_MODE_2               = ( 0x29, 0x0000C000, 14 )
        FSF_2                     = ( 0x2A, 0x00000003,  0 )
        SHUNT_SCALE_2             = ( 0x2A, 0x0000000C,  2 )
        SLEW_RATE_2               = ( 0x2A, 0x00000030,  4 )
        T_BLANKING_2              = ( 0x2A, 0x000000C0,  6 )
        F_PWM_2                   = ( 0x2A, 0x00000300,  8 )
        HSNLS_2                   = ( 0x2A, 0x00000400, 10 )
        DPM_THLD_2                = ( 0x2B, 0x00000FFF,  0 )
        DPM_MIN_CURRENT_2         = ( 0x2C, 0x000000FF,  0 )
        DPM_MIN_NBR_2             = ( 0x2C, 0x00000F00,  8 )
        END_HIT_AUTO_2            = ( 0x2C, 0x00001000, 12 )
        END_HIT_START_HIZ_AUTO_2  = ( 0x2C, 0x00002000, 13 )
        DPM_EN_2                  = ( 0x2C, 0x00004000, 14 )
        IDC_THLD_2                = ( 0x2D, 0x0000FFFF,  0 )
        RES_THLD_2                = ( 0x2E, 0x0000FFFF,  0 )
        L_NBR_CALC_2              = ( 0x2F, 0x0000000F,  0 )
        L_MEAS_WCYCLES_2          = ( 0x2F, 0x000000F0,  4 )
        L_MEAS_H_2                = ( 0x2F, 0x00000100,  8 )
        L_MEAS_L2H_2              = ( 0x2F, 0x00000200,  9 )
        L_MEAS_EN_2               = ( 0x2F, 0x00000400, 10 )
        DITH_EN_2                 = ( 0x2F, 0x00000800, 11 )
        IAC_THLD_2                = ( 0x30, 0x00000FFF,  0 )
        CFG_P_2                   = ( 0x31, 0x0000FFFF,  0 )
        CFG_I_2                   = ( 0x32, 0x0000FFFF,  0 )
        DC_L2H_3                  = ( 0x33, 0x0000FFFF,  0 )
        DC_H_3                    = ( 0x34, 0x0000FFFF,  0 )
        DC_L_3                    = ( 0x35, 0x0000FFFF,  0 )
        TIME_L2H_3                = ( 0x36, 0x0000FFFF,  0 )
        RAMP_3                    = ( 0x37, 0x000000FF,  0 )
        RUPE_3                    = ( 0x37, 0x00000100,  8 )
        RMDE_3                    = ( 0x37, 0x00000200,  9 )
        RDWE_3                    = ( 0x37, 0x00000400, 10 )
        H2L_EN_3                  = ( 0x37, 0x00000800, 11 )
        OL_EN_3                   = ( 0x37, 0x00001000, 12 )
        HHF_EN_3                  = ( 0x37, 0x00002000, 13 )
        CTRL_MODE_3               = ( 0x37, 0x0000C000, 14 )
        FSF_3                     = ( 0x38, 0x00000003,  0 )
        SHUNT_SCALE_3             = ( 0x38, 0x0000000C,  2 )
        SLEW_RATE_3               = ( 0x38, 0x00000030,  4 )
        T_BLANKING_3              = ( 0x38, 0x000000C0,  6 )
        F_PWM_3                   = ( 0x38, 0x00000300,  8 )
        HSNLS_3                   = ( 0x38, 0x00000400, 10 )
        DPM_THLD_3                = ( 0x39, 0x00000FFF,  0 )
        DPM_MIN_CURRENT_3         = ( 0x3A, 0x000000FF,  0 )
        DPM_MIN_NBR_3             = ( 0x3A, 0x00000F00,  8 )
        END_HIT_AUTO_3            = ( 0x3A, 0x00001000, 12 )
        END_HIT_START_HIZ_AUTO_3  = ( 0x3A, 0x00002000, 13 )
        DPM_EN_3                  = ( 0x3A, 0x00004000, 14 )
        IDC_THLD_3                = ( 0x3B, 0x0000FFFF,  0 )
        RES_THLD_3                = ( 0x3C, 0x0000FFFF,  0 )
        L_NBR_CALC_3              = ( 0x3D, 0x0000000F,  0 )
        L_MEAS_WCYCLES_3          = ( 0x3D, 0x000000F0,  4 )
        L_MEAS_H_3                = ( 0x3D, 0x00000100,  8 )
        L_MEAS_L2H_3              = ( 0x3D, 0x00000200,  9 )
        L_MEAS_EN_3               = ( 0x3D, 0x00000400, 10 )
        DITH_EN_3                 = ( 0x3D, 0x00000800, 11 )
        IAC_THLD_3                = ( 0x3E, 0x00000FFF,  0 )
        CFG_P_3                   = ( 0x3F, 0x0000FFFF,  0 )
        CFG_I_3                   = ( 0x40, 0x0000FFFF,  0 )
        I_DPM_PEAK_0              = ( 0x41, 0x0000FFFF,  0 )
        I_DPM_VALLEY_0            = ( 0x42, 0x0000FFFF,  0 )
        REACTION_TIME_0           = ( 0x43, 0x0000FFFF,  0 )
        #REACTION_TIME_0           = ( 0x44, 0x0000FFFF,  0 )
        I_MONITOR_0               = ( 0x45, 0x0000FFFF,  0 )
        I_DC_0                    = ( 0x46, 0x0000FFFF,  0 )
        I_AC_0                    = ( 0x47, 0x0000FFFF,  0 )
        R_0                       = ( 0x48, 0x0000FFFF,  0 )
        PWM_DUTYCYCLE_0           = ( 0x49, 0x0000FFFF,  0 )
        I_DPM_PEAK_1              = ( 0x4A, 0x0000FFFF,  0 )
        I_DPM_VALLEY_1            = ( 0x4B, 0x0000FFFF,  0 )
        REACTION_TIME_1           = ( 0x4C, 0x0000FFFF,  0 )
        #REACTION_TIME_1           = ( 0x4D, 0x0000FFFF,  0 )
        I_MONITOR_1               = ( 0x4E, 0x0000FFFF,  0 )
        I_DC_1                    = ( 0x4F, 0x0000FFFF,  0 )
        I_AC_1                    = ( 0x50, 0x0000FFFF,  0 )
        R_1                       = ( 0x51, 0x0000FFFF,  0 )
        PWM_DUTYCYCLE_1           = ( 0x52, 0x0000FFFF,  0 )
        I_DPM_PEAK_2              = ( 0x53, 0x0000FFFF,  0 )
        I_DPM_VALLEY_2            = ( 0x54, 0x0000FFFF,  0 )
        REACTION_TIME_2           = ( 0x55, 0x0000FFFF,  0 )
        #REACTION_TIME_2           = ( 0x56, 0x0000FFFF,  0 )
        I_MONITOR_2               = ( 0x57, 0x0000FFFF,  0 )
        I_DC_2                    = ( 0x58, 0x0000FFFF,  0 )
        I_AC_2                    = ( 0x59, 0x0000FFFF,  0 )
        R_2                       = ( 0x5A, 0x0000FFFF,  0 )
        PWM_DUTYCYCLE_2           = ( 0x5B, 0x0000FFFF,  0 )
        I_DPM_PEAK_3              = ( 0x5C, 0x0000FFFF,  0 )
        I_DPM_VALLEY_3            = ( 0x5D, 0x0000FFFF,  0 )
        REACTION_TIME_3           = ( 0x5E, 0x0000FFFF,  0 )
        #REACTION_TIME_3           = ( 0x5F, 0x0000FFFF,  0 )
        I_MONITOR_3               = ( 0x60, 0x0000FFFF,  0 )
        I_DC_3                    = ( 0x61, 0x0000FFFF,  0 )
        I_AC_3                    = ( 0x62, 0x0000FFFF,  0 )
        R_3                       = ( 0x63, 0x0000FFFF,  0 )
        PWM_DUTYCYCLE_3           = ( 0x64, 0x0000FFFF,  0 )
        OCP0                      = ( 0x65, 0x00000001,  0 )
        OCP1                      = ( 0x65, 0x00000002,  1 )
        OCP2                      = ( 0x65, 0x00000004,  2 )
        OCP3                      = ( 0x65, 0x00000008,  3 )
        HHF0                      = ( 0x65, 0x00000010,  4 )
        HHF1                      = ( 0x65, 0x00000020,  5 )
        HHF2                      = ( 0x65, 0x00000040,  6 )
        HHF3                      = ( 0x65, 0x00000080,  7 )
        OLF0                      = ( 0x65, 0x00000100,  8 )
        OLF1                      = ( 0x65, 0x00000200,  9 )
        OLF2                      = ( 0x65, 0x00000400, 10 )
        OLF3                      = ( 0x65, 0x00000800, 11 )
        DPM0                      = ( 0x65, 0x00001000, 12 )
        DPM1                      = ( 0x65, 0x00002000, 13 )
        DPM2                      = ( 0x65, 0x00004000, 14 )
        DPM3                      = ( 0x65, 0x00008000, 15 )
        IND0                      = ( 0x66, 0x00000001,  0 )
        IND1                      = ( 0x66, 0x00000002,  1 )
        IND2                      = ( 0x66, 0x00000004,  2 )
        IND3                      = ( 0x66, 0x00000008,  3 )
        #UVM                       = ( 0x66, 0x00000010,  4 )
        #COMER                     = ( 0x66, 0x00000020,  5 )
        #OVT                       = ( 0x66, 0x00000040,  6 )
        RES0                      = ( 0x66, 0x00000080,  7 )
        RES1                      = ( 0x66, 0x00000100,  8 )
        RES2                      = ( 0x66, 0x00000200,  9 )
        RES3                      = ( 0x66, 0x00000400, 10 )

        DC_H = [ DC_H_0, DC_H_1, DC_H_2, DC_H_3 ]
        DC_L = [ DC_L_0, DC_L_1, DC_L_2, DC_L_3 ]
        DC_L2H = [ DC_L2H_0, DC_L2H_1, DC_L2H_2, DC_L2H_3 ]
        FSF = [ FSF_0, FSF_1, FSF_2, FSF_3 ]
        CTRL_MODE = [ CTRL_MODE_0, CTRL_MODE_1, CTRL_MODE_2, CTRL_MODE_3 ]
        CNTL = [ CNTL0, CNTL1, CNTL2, CNTL3 ]
