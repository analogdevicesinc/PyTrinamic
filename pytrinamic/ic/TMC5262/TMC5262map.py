################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Choice, Option, Field, Register


class TMC5262Map:
    def __init__(self, *, channel=None, block=None, width=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(channel, block, width)


class _ALL_REGISTERS(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("ALL_REGISTERS", channel, block, width)
        self.GCONF                      =  self._GCONF(                    self,  Access.RW,   0x0000,  False)
        self.GSTAT                      =  self._GSTAT(                    self,  Access.RWC,  0x0001,  False)
        self.DO_CONF                    =  self._DO_CONF(                  self,  Access.RW,   0x0002,  False)
        self.DO_SCOPE_CONF              =  self._DO_SCOPE_CONF(            self,  Access.RW,   0x0003,  False)
        self.IOIN                       =  self._IOIN(                     self,  Access.R,    0x0004,  False)
        self.X_COMPARE                  =  self._X_COMPARE(                self,  Access.RW,   0x0005,  True)
        self.X_COMPARE_REPEAT           =  self._X_COMPARE_REPEAT(         self,  Access.RW,   0x0006,  False)
        self.DRV_CONF                   =  self._DRV_CONF(                 self,  Access.RW,   0x000A,  False)
        self.PLL                        =  self._PLL(                      self,  Access.RW,   0x000B,  False)
        self.IHOLD_IRUN                 =  self._IHOLD_IRUN(               self,  Access.RW,   0x0010,  False)
        self.TPOWERDOWN                 =  self._TPOWERDOWN(               self,  Access.RW,   0x0011,  False)
        self.TSTEP                      =  self._TSTEP(                    self,  Access.R,    0x0012,  False)
        self.TPWMTHRS                   =  self._TPWMTHRS(                 self,  Access.RW,   0x0013,  False)
        self.TCOOLTHRS                  =  self._TCOOLTHRS(                self,  Access.RW,   0x0014,  False)
        self.THIGH                      =  self._THIGH(                    self,  Access.RW,   0x0015,  False)
        self.TSGP_LOW_VEL_THRS          =  self._TSGP_LOW_VEL_THRS(        self,  Access.RW,   0x0016,  False)
        self.T_RCOIL_MEAS               =  self._T_RCOIL_MEAS(             self,  Access.RW,   0x0017,  False)
        self.TUDCSTEP                   =  self._TUDCSTEP(                 self,  Access.RW,   0x0018,  False)
        self.UDC_CONF                   =  self._UDC_CONF(                 self,  Access.RW,   0x0019,  False)
        self.STEPS_LOST                 =  self._STEPS_LOST(               self,  Access.RW,   0x001A,  True)
        self.RAMPMODE                   =  self._RAMPMODE(                 self,  Access.RW,   0x0020,  False)
        self.XACTUAL                    =  self._XACTUAL(                  self,  Access.RW,   0x0021,  True)
        self.VACTUAL                    =  self._VACTUAL(                  self,  Access.R,    0x0022,  True)
        self.VSTART                     =  self._VSTART(                   self,  Access.RW,   0x0023,  False)
        self.A1                         =  self._A1(                       self,  Access.RW,   0x0024,  False)
        self.V1                         =  self._V1(                       self,  Access.RW,   0x0025,  False)
        self.AMAX                       =  self._AMAX(                     self,  Access.RW,   0x0026,  False)
        self.VMAX                       =  self._VMAX(                     self,  Access.RW,   0x0027,  False)
        self.DMAX                       =  self._DMAX(                     self,  Access.RW,   0x0028,  False)
        self.TVMAX                      =  self._TVMAX(                    self,  Access.RW,   0x0029,  False)
        self.D1                         =  self._D1(                       self,  Access.RW,   0x002A,  False)
        self.VSTOP                      =  self._VSTOP(                    self,  Access.RW,   0x002B,  False)
        self.TZEROWAIT                  =  self._TZEROWAIT(                self,  Access.RW,   0x002C,  False)
        self.XTARGET                    =  self._XTARGET(                  self,  Access.RW,   0x002D,  True)
        self.V2                         =  self._V2(                       self,  Access.RW,   0x002E,  False)
        self.A2                         =  self._A2(                       self,  Access.RW,   0x002F,  False)
        self.D2                         =  self._D2(                       self,  Access.RW,   0x0030,  False)
        self.AACTUAL                    =  self._AACTUAL(                  self,  Access.R,    0x0031,  True)
        self.SW_MODE                    =  self._SW_MODE(                  self,  Access.RW,   0x0034,  False)
        self.RAMP_STAT                  =  self._RAMP_STAT(                self,  Access.RWC,  0x0035,  False)
        self.XLATCH                     =  self._XLATCH(                   self,  Access.R,    0x0036,  True)
        self.ENCMODE                    =  self._ENCMODE(                  self,  Access.RW,   0x0038,  False)
        self.X_ENC                      =  self._X_ENC(                    self,  Access.RW,   0x0039,  True)
        self.ENC_CONST                  =  self._ENC_CONST(                self,  Access.RW,   0x003A,  True)
        self.ENC_STATUS                 =  self._ENC_STATUS(               self,  Access.RWC,  0x003B,  False)
        self.ENC_LATCH                  =  self._ENC_LATCH(                self,  Access.R,    0x003C,  True)
        self.ENC_DEVIATION              =  self._ENC_DEVIATION(            self,  Access.R,    0x003D,  False)
        self.VIRTUAL_STOP_L             =  self._VIRTUAL_STOP_L(           self,  Access.RW,   0x003E,  True)
        self.VIRTUAL_STOP_R             =  self._VIRTUAL_STOP_R(           self,  Access.RW,   0x003F,  True)
        self.CURRENT_PI_REG             =  self._CURRENT_PI_REG(           self,  Access.RW,   0x0040,  False)
        self.ANGLE_PI_REG               =  self._ANGLE_PI_REG(             self,  Access.RW,   0x0041,  False)
        self.CUR_ANGLE_LIMIT            =  self._CUR_ANGLE_LIMIT(          self,  Access.RW,   0x0042,  False)
        self.ANGLE_LOWER_LIMIT          =  self._ANGLE_LOWER_LIMIT(        self,  Access.RW,   0x0043,  False)
        self.CUR_ANGLE_MEAS             =  self._CUR_ANGLE_MEAS(           self,  Access.R,    0x0044,  False)
        self.PI_RESULTS                 =  self._PI_RESULTS(               self,  Access.R,    0x0045,  False)
        self.COIL_INDUCT                =  self._COIL_INDUCT(              self,  Access.RW,   0x0046,  False)
        self.R_COIL                     =  self._R_COIL(                   self,  Access.R,    0x0047,  False)
        self.R_COIL_USER                =  self._R_COIL_USER(              self,  Access.RW,   0x0048,  False)
        self.SGP_CONF                   =  self._SGP_CONF(                 self,  Access.RW,   0x0049,  False)
        self.SGP_IND_2_3                =  self._SGP_IND_2_3(              self,  Access.R,    0x004A,  False)
        self.SGP_IND_0_1                =  self._SGP_IND_0_1(              self,  Access.R,    0x004B,  False)
        self.INDUCTANCE_VOLTAGE         =  self._INDUCTANCE_VOLTAGE(       self,  Access.R,    0x004C,  False)
        self.SGP_BEMF                   =  self._SGP_BEMF(                 self,  Access.R,    0x004D,  False)
        self.COOLSTEPPLUS_CONF          =  self._COOLSTEPPLUS_CONF(        self,  Access.RW,   0x004E,  False)
        self.COOLSTEPPLUS_PI_REG        =  self._COOLSTEPPLUS_PI_REG(      self,  Access.RW,   0x004F,  False)
        self.COOLSTEPPLUS_PI_DOWN       =  self._COOLSTEPPLUS_PI_DOWN(     self,  Access.RW,   0x0050,  False)
        self.COOLSTEPPLUS_RESERVE_CONF  =  self._COOLSTEPPLUS_RESERVE_CONF(self,  Access.RW,   0x0051,  False)
        self.COOLSTEPPLUS_LOAD_RESERVE  =  self._COOLSTEPPLUS_LOAD_RESERVE(self,  Access.R,    0x0052,  False)
        self.TSTEP_VELOCITY             =  self._TSTEP_VELOCITY(           self,  Access.R,    0x0053,  True)
        self.ADC_VSUPPLY_TEMP           =  self._ADC_VSUPPLY_TEMP(         self,  Access.R,    0x0058,  False)
        self.ADC_I                      =  self._ADC_I(                    self,  Access.R,    0x0059,  False)
        self.OTW_OV_VTH                 =  self._OTW_OV_VTH(               self,  Access.RW,   0x005A,  False)
        self.MSLUT_0                    =  self._MSLUT_0(                  self,  Access.RW,   0x0060,  False)
        self.MSLUT_1                    =  self._MSLUT_1(                  self,  Access.RW,   0x0061,  False)
        self.MSLUT_2                    =  self._MSLUT_2(                  self,  Access.RW,   0x0062,  False)
        self.MSLUT_3                    =  self._MSLUT_3(                  self,  Access.RW,   0x0063,  False)
        self.MSLUT_4                    =  self._MSLUT_4(                  self,  Access.RW,   0x0064,  False)
        self.MSLUT_5                    =  self._MSLUT_5(                  self,  Access.RW,   0x0065,  False)
        self.MSLUT_6                    =  self._MSLUT_6(                  self,  Access.RW,   0x0066,  False)
        self.MSLUT_7                    =  self._MSLUT_7(                  self,  Access.RW,   0x0067,  False)
        self.MSLUTSEL                   =  self._MSLUTSEL(                 self,  Access.RW,   0x0068,  False)
        self.MSLUTSTART                 =  self._MSLUTSTART(               self,  Access.RW,   0x0069,  False)
        self.MSCNT                      =  self._MSCNT(                    self,  Access.R,    0x006A,  False)
        self.MSCURACT                   =  self._MSCURACT(                 self,  Access.R,    0x006B,  False)
        self.CHOPCONF                   =  self._CHOPCONF(                 self,  Access.RW,   0x006C,  False)
        self.COOLCONF                   =  self._COOLCONF(                 self,  Access.RW,   0x006D,  False)
        self.DRV_STATUS                 =  self._DRV_STATUS(               self,  Access.R,    0x006F,  False)
        self.PWMCONF                    =  self._PWMCONF(                  self,  Access.RW,   0x0070,  False)

    class _GCONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("GCONF", parent, access, address, signed)
            self.FAST_STANDSTILL   =  self._FAST_STANDSTILL( self,  Access.RW,  0x00000001,  0,   signed=False)
            self.EN_STEALTHCHOP    =  self._EN_STEALTHCHOP(  self,  Access.RW,  0x00000002,  1,   signed=False)
            self.MULTISTEP_FILT    =  self._MULTISTEP_FILT(  self,  Access.RW,  0x00000004,  2,   signed=False)
            self.SHAFT             =  self._SHAFT(           self,  Access.RW,  0x00000008,  3,   signed=False)
            self.SMALL_HYSTERESIS  =  self._SMALL_HYSTERESIS(self,  Access.RW,  0x00000010,  4,   signed=False)
            self.STOP_ENABLE       =  self._STOP_ENABLE(     self,  Access.RW,  0x00000020,  5,   signed=False)
            self.DIRECT_MODE       =  self._DIRECT_MODE(     self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LENGTH_STEPPULSE  =  self._LENGTH_STEPPULSE(self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.OV_NN             =  self._OV_NN(           self,  Access.RW,  0x00001000,  12,  signed=False)
            self.step_dir          =  self._step_dir(        self,  Access.RW,  0x80000000,  31,  signed=False)

        class _FAST_STANDSTILL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.STST_2_20  =  Option(False,  parent,  "STST_2_20")
                    self.STST_2_18  =  Option(True,   parent,  "STST_2_18")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FAST_STANDSTILL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EN_STEALTHCHOP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SPREADCYCLE  =  Option(False,  parent,  "SPREADCYCLE")
                    self.STEALTHCHOP  =  Option(True,   parent,  "STEALTHCHOP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_STEALTHCHOP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _MULTISTEP_FILT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FILT_DIS  =  Option(False,  parent,  "FILT_DIS")
                    self.FILT_EN   =  Option(True,   parent,  "FILT_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MULTISTEP_FILT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SHAFT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DIR      =  Option(False,  parent,  "DIR")
                    self.DIR_INV  =  Option(True,   parent,  "DIR_INV")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHAFT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SMALL_HYSTERESIS(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HYST_1_16  =  Option(False,  parent,  "HYST_1_16")
                    self.HYST_1_32  =  Option(True,   parent,  "HYST_1_32")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SMALL_HYSTERESIS", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STOP_ENABLE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NONE     =  Option(False,  parent,  "NONE")
                    self.EM_STOP  =  Option(True,   parent,  "EM_STOP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIRECT_MODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NORMAL_MODE  =  Option(False,  parent,  "NORMAL_MODE")
                    self.DIRECT_MODE  =  Option(True,   parent,  "DIRECT_MODE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIRECT_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LENGTH_STEPPULSE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LENGTH_STEPPULSE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OV_NN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.N_CHANNEL  =  Option(False,  parent,  "N_CHANNEL")
                    self.OV_PIN     =  Option(True,   parent,  "OV_PIN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OV_NN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _step_dir(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RAMP      =  Option(False,  parent,  "RAMP")
                    self.STEP_DIR  =  Option(True,   parent,  "STEP_DIR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("step_dir", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _GSTAT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("GSTAT", parent, access, address, signed)
            self.RESET           =  self._RESET(         self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.DRV_ERR         =  self._DRV_ERR(       self,  Access.RWC,  0x00000002,  1,  signed=False)
            self.UV_CP           =  self._UV_CP(         self,  Access.RWC,  0x00000004,  2,  signed=False)
            self.REGISTER_RESET  =  self._REGISTER_RESET(self,  Access.RWC,  0x00000008,  3,  signed=False)
            self.VM_UVLO         =  self._VM_UVLO(       self,  Access.RWC,  0x00000010,  4,  signed=False)
            self.VCCIO_UV        =  self._VCCIO_UV(      self,  Access.RWC,  0x00000020,  5,  signed=False)

        class _RESET(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_RESET   =  Option(False,  parent,  "NO_RESET")
                    self.RESET_DET  =  Option(True,   parent,  "RESET_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DRV_ERR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.DRV_ERR_DET  =  Option(True,   parent,  "DRV_ERR_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DRV_ERR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _UV_CP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.CP_UV_DET    =  Option(True,   parent,  "CP_UV_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UV_CP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _REGISTER_RESET(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.REG_RES_DET  =  Option(True,   parent,  "REG_RES_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REGISTER_RESET", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VM_UVLO(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.VM_UVLO_DET  =  Option(True,   parent,  "VM_UVLO_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VCCIO_UV(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL   =  Option(False,  parent,  "OPERATIONAL")
                    self.VCCIO_UV_DET  =  Option(True,   parent,  "VCCIO_UV_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VCCIO_UV", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _DO_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("DO_CONF", parent, access, address, signed)
            self.DO0_ERROR           =  self._DO0_ERROR(         self,  Access.RW,  0x00000001,  0,   signed=False)
            self.DO0_OTPW            =  self._DO0_OTPW(          self,  Access.RW,  0x00000002,  1,   signed=False)
            self.DO0_STALL           =  self._DO0_STALL(         self,  Access.RW,  0x00000004,  2,   signed=False)
            self.DO0_INDEX           =  self._DO0_INDEX(         self,  Access.RW,  0x00000008,  3,   signed=False)
            self.DO0_STEP            =  self._DO0_STEP(          self,  Access.RW,  0x00000010,  4,   signed=False)
            self.DO0_DIR             =  self._DO0_DIR(           self,  Access.RW,  0x00000020,  5,   signed=False)
            self.DO0_XCOMP           =  self._DO0_XCOMP(         self,  Access.RW,  0x00000040,  6,   signed=False)
            self.DO0_OV              =  self._DO0_OV(            self,  Access.RW,  0x00000080,  7,   signed=False)
            self.DO0_DCUSTEP         =  self._DO0_DCUSTEP(       self,  Access.RW,  0x00000100,  8,   signed=False)
            self.DO0_EV_STOP_REF     =  self._DO0_EV_STOP_REF(   self,  Access.RW,  0x00000200,  9,   signed=False)
            self.DO0_EV_STOP_SG      =  self._DO0_EV_STOP_SG(    self,  Access.RW,  0x00000400,  10,  signed=False)
            self.DO0_EV_POS_REACHED  =  self._DO0_EV_POS_REACHED(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.DO0_EV_N_DEVIATION  =  self._DO0_EV_N_DEVIATION(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.DO1_ERROR           =  self._DO1_ERROR(         self,  Access.RW,  0x00002000,  13,  signed=False)
            self.DO1_OTPW            =  self._DO1_OTPW(          self,  Access.RW,  0x00004000,  14,  signed=False)
            self.DO1_STALL           =  self._DO1_STALL(         self,  Access.RW,  0x00008000,  15,  signed=False)
            self.DO1_INDEX           =  self._DO1_INDEX(         self,  Access.RW,  0x00010000,  16,  signed=False)
            self.DO1_STEP            =  self._DO1_STEP(          self,  Access.RW,  0x00020000,  17,  signed=False)
            self.DO1_DIR             =  self._DO1_DIR(           self,  Access.RW,  0x00040000,  18,  signed=False)
            self.DO1_XCOMP           =  self._DO1_XCOMP(         self,  Access.RW,  0x00080000,  19,  signed=False)
            self.DO1_OV              =  self._DO1_OV(            self,  Access.RW,  0x00100000,  20,  signed=False)
            self.DO1_UDCSTEP         =  self._DO1_UDCSTEP(       self,  Access.RW,  0x00200000,  21,  signed=False)
            self.DO1_EV_STOP_REF     =  self._DO1_EV_STOP_REF(   self,  Access.RW,  0x00400000,  22,  signed=False)
            self.DO1_EV_STOP_SG      =  self._DO1_EV_STOP_SG(    self,  Access.RW,  0x00800000,  23,  signed=False)
            self.DO1_EV_POS_REACHED  =  self._DO1_EV_POS_REACHED(self,  Access.RW,  0x01000000,  24,  signed=False)
            self.DO1_EV_N_DEVIATION  =  self._DO1_EV_N_DEVIATION(self,  Access.RW,  0x02000000,  25,  signed=False)
            self.DO0_NOD_PP          =  self._DO0_NOD_PP(        self,  Access.RW,  0x10000000,  28,  signed=False)
            self.DO0_INVPP           =  self._DO0_INVPP(         self,  Access.RW,  0x20000000,  29,  signed=False)
            self.DO1_NOD_PP          =  self._DO1_NOD_PP(        self,  Access.RW,  0x40000000,  30,  signed=False)
            self.DO1_INVPP           =  self._DO1_INVPP(         self,  Access.RW,  0x80000000,  31,  signed=False)

        class _DO0_ERROR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_OTPW(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_OTPW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_STALL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_STALL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_INDEX(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_INDEX", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_STEP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_STEP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_DIR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_DIR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_XCOMP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_XCOMP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_OV(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_OV", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_DCUSTEP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_DCUSTEP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_EV_STOP_REF(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_EV_STOP_REF", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_EV_STOP_SG(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_EV_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_EV_POS_REACHED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_EV_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_EV_N_DEVIATION(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_EV_N_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_ERROR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_OTPW(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_OTPW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_STALL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_STALL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_INDEX(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_INDEX", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_STEP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_STEP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_DIR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_DIR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_XCOMP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_XCOMP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_OV(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_OV", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_UDCSTEP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_UDCSTEP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_EV_STOP_REF(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_EV_STOP_REF", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_EV_STOP_SG(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_EV_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_EV_POS_REACHED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_EV_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_EV_N_DEVIATION(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_EV_N_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_NOD_PP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPEN_DRAIN  =  Option(False,  parent,  "OPEN_DRAIN")
                    self.PUSH_PULL   =  Option(True,   parent,  "PUSH_PULL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_NOD_PP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_INVPP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HIGH_ACTIVE  =  Option(False,  parent,  "HIGH_ACTIVE")
                    self.LOW_ACTIVE   =  Option(True,   parent,  "LOW_ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_INVPP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_NOD_PP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPEN_DRAIN  =  Option(False,  parent,  "OPEN_DRAIN")
                    self.PUSH_PULL   =  Option(True,   parent,  "PUSH_PULL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_NOD_PP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_INVPP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HIGH_ACTIVE  =  Option(False,  parent,  "HIGH_ACTIVE")
                    self.LOW_ACTIVE   =  Option(True,   parent,  "LOW_ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_INVPP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _DO_SCOPE_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("DO_SCOPE_CONF", parent, access, address, signed)
            self.DO0_SCOPE_EN   =  self._DO0_SCOPE_EN( self,  Access.RW,  0x00000001,  0,   signed=False)
            self.DO0_SCOPE_SEL  =  self._DO0_SCOPE_SEL(self,  Access.RW,  0x000001F0,  4,   signed=False)
            self.DO1_SCOPE_EN   =  self._DO1_SCOPE_EN( self,  Access.RW,  0x00001000,  12,  signed=False)
            self.DO1_SCOPE_SEL  =  self._DO1_SCOPE_SEL(self,  Access.RW,  0x001F0000,  16,  signed=False)

        class _DO0_SCOPE_EN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_SCOPE_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO0_SCOPE_SEL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC_I_A        =  Option(0,   parent,  "ADC_I_A")
                    self.ADC_I_B        =  Option(1,   parent,  "ADC_I_B")
                    self.RCOIL_A        =  Option(2,   parent,  "RCOIL_A")
                    self.RCOIL_B        =  Option(3,   parent,  "RCOIL_B")
                    self.UL_A           =  Option(4,   parent,  "UL_A")
                    self.UL_B           =  Option(5,   parent,  "UL_B")
                    self.CS_LOAD_R      =  Option(6,   parent,  "CS_LOAD_R")
                    self.ADC_TEMP       =  Option(7,   parent,  "ADC_TEMP")
                    self.ANGLE_MEAS     =  Option(8,   parent,  "ANGLE_MEAS")
                    self.SGP_RAW        =  Option(9,   parent,  "SGP_RAW")
                    self.ANGLE_CORR     =  Option(10,  parent,  "ANGLE_CORR")
                    self.AMPL_MEAS      =  Option(11,  parent,  "AMPL_MEAS")
                    self.PWM_CALC       =  Option(12,  parent,  "PWM_CALC")
                    self.CS_ACTUAL      =  Option(13,  parent,  "CS_ACTUAL")
                    self.UBEMF_ABS      =  Option(14,  parent,  "UBEMF_ABS")
                    self.SG_RESULT      =  Option(15,  parent,  "SG_RESULT")
                    self.SGP_RESULT     =  Option(16,  parent,  "SGP_RESULT")
                    self.CUR_A          =  Option(17,  parent,  "CUR_A")
                    self.CUR_B          =  Option(18,  parent,  "CUR_B")
                    self.DAC_X          =  Option(19,  parent,  "DAC_X")
                    self.DAC_Y          =  Option(20,  parent,  "DAC_Y")
                    self.ANGLE_ERR      =  Option(21,  parent,  "ANGLE_ERR")
                    self.MSCNT          =  Option(22,  parent,  "MSCNT")
                    self.MSCNT_SNP      =  Option(23,  parent,  "MSCNT_SNP")
                    self.MSCNT_OFF      =  Option(24,  parent,  "MSCNT_OFF")
                    self.TSTEP_V_20_13  =  Option(25,  parent,  "TSTEP_V_20_13")
                    self.TSTEP_V_18_11  =  Option(26,  parent,  "TSTEP_V_18_11")
                    self.TSTEP_V_16_9   =  Option(27,  parent,  "TSTEP_V_16_9")
                    self.USER           =  Option(28,  parent,  "USER")
                    self.BEMF_A_13_7    =  Option(29,  parent,  "BEMF_A_13_7")
                    self.BEMF_A_11_5    =  Option(30,  parent,  "BEMF_A_11_5")
                    self.BEMF_A_9_3     =  Option(31,  parent,  "BEMF_A_9_3")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO0_SCOPE_SEL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_SCOPE_EN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_SCOPE_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DO1_SCOPE_SEL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC_I_A        =  Option(0,   parent,  "ADC_I_A")
                    self.ADC_I_B        =  Option(1,   parent,  "ADC_I_B")
                    self.RCOIL_A        =  Option(2,   parent,  "RCOIL_A")
                    self.RCOIL_B        =  Option(3,   parent,  "RCOIL_B")
                    self.UL_A           =  Option(4,   parent,  "UL_A")
                    self.UL_B           =  Option(5,   parent,  "UL_B")
                    self.CS_LOAD_R      =  Option(6,   parent,  "CS_LOAD_R")
                    self.ADC_TEMP       =  Option(7,   parent,  "ADC_TEMP")
                    self.ANGLE_MEAS     =  Option(8,   parent,  "ANGLE_MEAS")
                    self.SGP_RAW        =  Option(9,   parent,  "SGP_RAW")
                    self.ANGLE_CORR     =  Option(10,  parent,  "ANGLE_CORR")
                    self.AMPL_MEAS      =  Option(11,  parent,  "AMPL_MEAS")
                    self.PWM_CALC       =  Option(12,  parent,  "PWM_CALC")
                    self.CS_ACTUAL      =  Option(13,  parent,  "CS_ACTUAL")
                    self.UBEMF_ABS      =  Option(14,  parent,  "UBEMF_ABS")
                    self.SG_RESULT      =  Option(15,  parent,  "SG_RESULT")
                    self.SGP_RESULT     =  Option(16,  parent,  "SGP_RESULT")
                    self.CUR_A          =  Option(17,  parent,  "CUR_A")
                    self.CUR_B          =  Option(18,  parent,  "CUR_B")
                    self.DAC_X          =  Option(19,  parent,  "DAC_X")
                    self.DAC_Y          =  Option(20,  parent,  "DAC_Y")
                    self.ANGLE_ERR      =  Option(21,  parent,  "ANGLE_ERR")
                    self.MSCNT          =  Option(22,  parent,  "MSCNT")
                    self.MSCNT_SNP      =  Option(23,  parent,  "MSCNT_SNP")
                    self.MSCNT_OFF      =  Option(24,  parent,  "MSCNT_OFF")
                    self.TSTEP_V_20_13  =  Option(25,  parent,  "TSTEP_V_20_13")
                    self.TSTEP_V_18_11  =  Option(26,  parent,  "TSTEP_V_18_11")
                    self.TSTEP_V_16_9   =  Option(27,  parent,  "TSTEP_V_16_9")
                    self.USER           =  Option(28,  parent,  "USER")
                    self.BEMF_B_13_7    =  Option(29,  parent,  "BEMF_B_13_7")
                    self.BEMF_B_11_5    =  Option(30,  parent,  "BEMF_B_11_5")
                    self.BEMF_B_9_3     =  Option(31,  parent,  "BEMF_B_9_3")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DO1_SCOPE_SEL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _IOIN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("IOIN", parent, access, address, signed)
            self.REFL         =  self._REFL(       self,  Access.R,  0x00000001,  0,   signed=False)
            self.REFR         =  self._REFR(       self,  Access.R,  0x00000002,  1,   signed=False)
            self.ENCB         =  self._ENCB(       self,  Access.R,  0x00000004,  2,   signed=False)
            self.ENCA         =  self._ENCA(       self,  Access.R,  0x00000008,  3,   signed=False)
            self.DRV_ENN      =  self._DRV_ENN(    self,  Access.R,  0x00000010,  4,   signed=False)
            self.ENCN         =  self._ENCN(       self,  Access.R,  0x00000020,  5,   signed=False)
            self.EXT_RES_DET  =  self._EXT_RES_DET(self,  Access.R,  0x00002000,  13,  signed=False)
            self.EXT_CLK      =  self._EXT_CLK(    self,  Access.R,  0x00004000,  14,  signed=False)
            self.SILICON_RV   =  self._SILICON_RV( self,  Access.R,  0x00070000,  16,  signed=False)

        class _REFL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOW   =  Option(False,  parent,  "LOW")
                    self.HIGH  =  Option(True,   parent,  "HIGH")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REFL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _REFR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOW   =  Option(False,  parent,  "LOW")
                    self.HIGH  =  Option(True,   parent,  "HIGH")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REFR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ENCB(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOW   =  Option(False,  parent,  "LOW")
                    self.HIGH  =  Option(True,   parent,  "HIGH")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENCB", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ENCA(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOW   =  Option(False,  parent,  "LOW")
                    self.HIGH  =  Option(True,   parent,  "HIGH")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENCA", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DRV_ENN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOW   =  Option(False,  parent,  "LOW")
                    self.HIGH  =  Option(True,   parent,  "HIGH")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DRV_ENN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ENCN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOW   =  Option(False,  parent,  "LOW")
                    self.HIGH  =  Option(True,   parent,  "HIGH")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENCN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EXT_RES_DET(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.REF_RES_FAULT  =  Option(False,  parent,  "REF_RES_FAULT")
                    self.REF_RES_DET    =  Option(True,   parent,  "REF_RES_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_RES_DET", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EXT_CLK(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INT_OSC  =  Option(False,  parent,  "INT_OSC")
                    self.EXT_OSC  =  Option(True,   parent,  "EXT_OSC")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_CLK", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SILICON_RV(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SILICON_RV", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _X_COMPARE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("X_COMPARE", parent, access, address, signed)
            self.X_COMPARE  =  self._X_COMPARE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _X_COMPARE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_COMPARE", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _X_COMPARE_REPEAT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("X_COMPARE_REPEAT", parent, access, address, signed)
            self.X_COMPARE_REPEAT  =  self._X_COMPARE_REPEAT(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

        class _X_COMPARE_REPEAT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_COMPARE_REPEAT", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _DRV_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("DRV_CONF", parent, access, address, signed)
            self.CURRENT_RANGE        =  self._CURRENT_RANGE(      self,  Access.RW,  0x00000003,  0,  signed=False)
            self.CURRENT_RANGE_SCALE  =  self._CURRENT_RANGE_SCALE(self,  Access.RW,  0x0000000C,  2,  signed=False)
            self.SLOPE_CONTROL        =  self._SLOPE_CONTROL(      self,  Access.RW,  0x00000030,  4,  signed=False)

        class _CURRENT_RANGE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RMS_1A  =  Option(0,  parent,  "RMS_1A")
                    self.RMS_2A  =  Option(1,  parent,  "RMS_2A")
                    self.RMS_3A  =  Option(2,  parent,  "RMS_3A")
                    self.RMS_4A  =  Option(3,  parent,  "RMS_4A")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_RANGE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CURRENT_RANGE_SCALE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SCALE_025  =  Option(0,  parent,  "SCALE_025")
                    self.SCALE_050  =  Option(1,  parent,  "SCALE_050")
                    self.SCALE_075  =  Option(2,  parent,  "SCALE_075")
                    self.SCALE_100  =  Option(3,  parent,  "SCALE_100")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_RANGE_SCALE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SLOPE_CONTROL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SC_100V_US  =  Option(0,  parent,  "SC_100V_US")
                    self.SC_200V_US  =  Option(1,  parent,  "SC_200V_US")
                    self.SC_400V_US  =  Option(2,  parent,  "SC_400V_US")
                    self.SC_800V_US  =  Option(3,  parent,  "SC_800V_US")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SLOPE_CONTROL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _PLL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PLL", parent, access, address, signed)
            self.COMMIT         =  self._COMMIT(       self,  Access.RW,  0x00000001,  0,   signed=False)
            self.EXT_NOT_INT    =  self._EXT_NOT_INT(  self,  Access.RW,  0x00000002,  1,   signed=False)
            self.CLK_SYS_SEL    =  self._CLK_SYS_SEL(  self,  Access.RW,  0x00000004,  2,   signed=False)
            self.CLK_FSM_ENA    =  self._CLK_FSM_ENA(  self,  Access.RW,  0x00000008,  3,   signed=False)
            self.CLOCK_DIVIDER  =  self._CLOCK_DIVIDER(self,  Access.RW,  0x000003E0,  5,   signed=False)
            self.CLK_1MO_TMO    =  self._CLK_1MO_TMO(  self,  Access.RW,  0x00001000,  12,  signed=False)
            self.CLK_LOSS       =  self._CLK_LOSS(     self,  Access.RW,  0x00002000,  13,  signed=False)
            self.CLK_IS_STUCK   =  self._CLK_IS_STUCK( self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PLL_LOCK_LOSS  =  self._PLL_LOCK_LOSS(self,  Access.RW,  0x00008000,  15,  signed=False)

        class _COMMIT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_OP            =  Option(False,  parent,  "NO_OP")
                    self.UPDATE_SETTINGS  =  Option(True,   parent,  "UPDATE_SETTINGS")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMMIT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EXT_NOT_INT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INT_OSC  =  Option(False,  parent,  "INT_OSC")
                    self.EXT_OSC  =  Option(True,   parent,  "EXT_OSC")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_NOT_INT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLK_SYS_SEL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INTERNAL  =  Option(False,  parent,  "INTERNAL")
                    self.PLL       =  Option(True,   parent,  "PLL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_SYS_SEL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLK_FSM_ENA(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_FSM_ENA", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLOCK_DIVIDER(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CLK_1M       =  Option(0,   parent,  "CLK_1M")
                    self.CLK_2M       =  Option(1,   parent,  "CLK_2M")
                    self.CLK_3M       =  Option(2,   parent,  "CLK_3M")
                    self.CLK_4M       =  Option(3,   parent,  "CLK_4M")
                    self.CLK_5M       =  Option(4,   parent,  "CLK_5M")
                    self.CLK_6M       =  Option(5,   parent,  "CLK_6M")
                    self.CLK_7M       =  Option(6,   parent,  "CLK_7M")
                    self.CLK_8M       =  Option(7,   parent,  "CLK_8M")
                    self.CLK_9M       =  Option(8,   parent,  "CLK_9M")
                    self.CLK_10M      =  Option(9,   parent,  "CLK_10M")
                    self.CLK_11M      =  Option(10,  parent,  "CLK_11M")
                    self.CLK_12M      =  Option(11,  parent,  "CLK_12M")
                    self.CLK_13M      =  Option(12,  parent,  "CLK_13M")
                    self.CLK_14M      =  Option(13,  parent,  "CLK_14M")
                    self.CLK_15M      =  Option(14,  parent,  "CLK_15M")
                    self.CLK_16M_INT  =  Option(15,  parent,  "CLK_16M_INT")
                    self.CLK_17M      =  Option(16,  parent,  "CLK_17M")
                    self.CLK_18M      =  Option(17,  parent,  "CLK_18M")
                    self.CLK_19M      =  Option(18,  parent,  "CLK_19M")
                    self.CLK_20M      =  Option(19,  parent,  "CLK_20M")
                    self.CLK_21M      =  Option(20,  parent,  "CLK_21M")
                    self.CLK_22M      =  Option(21,  parent,  "CLK_22M")
                    self.CLK_23M      =  Option(22,  parent,  "CLK_23M")
                    self.CLK_24M      =  Option(23,  parent,  "CLK_24M")
                    self.CLK_25M      =  Option(24,  parent,  "CLK_25M")
                    self.CLK_26M      =  Option(25,  parent,  "CLK_26M")
                    self.CLK_27M      =  Option(26,  parent,  "CLK_27M")
                    self.CLK_28M      =  Option(27,  parent,  "CLK_28M")
                    self.CLK_29M      =  Option(28,  parent,  "CLK_29M")
                    self.CLK_30M      =  Option(29,  parent,  "CLK_30M")
                    self.CLK_31M      =  Option(30,  parent,  "CLK_31M")
                    self.CLK_32M      =  Option(31,  parent,  "CLK_32M")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLOCK_DIVIDER", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLK_1MO_TMO(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CLK_OK   =  Option(False,  parent,  "CLK_OK")
                    self.TIMEOUT  =  Option(True,   parent,  "TIMEOUT")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_1MO_TMO", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLK_LOSS(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CLK_OK    =  Option(False,  parent,  "CLK_OK")
                    self.CLK_LOSS  =  Option(True,   parent,  "CLK_LOSS")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_LOSS", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLK_IS_STUCK(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CLK_OK    =  Option(False,  parent,  "CLK_OK")
                    self.CLK_NONE  =  Option(True,   parent,  "CLK_NONE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_IS_STUCK", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PLL_LOCK_LOSS(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.PLL_OK    =  Option(False,  parent,  "PLL_OK")
                    self.PLL_LOSS  =  Option(True,   parent,  "PLL_LOSS")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PLL_LOCK_LOSS", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _IHOLD_IRUN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("IHOLD_IRUN", parent, access, address, signed)
            self.IHOLD       =  self._IHOLD(     self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.IRUN        =  self._IRUN(      self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.IHOLDDELAY  =  self._IHOLDDELAY(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.IRUNDELAY   =  self._IRUNDELAY( self,  Access.RW,  0x0F000000,  24,  signed=False)

        class _IHOLD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IHOLD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IRUN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IRUN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IHOLDDELAY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IHOLDDELAY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IRUNDELAY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IRUNDELAY", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _TPOWERDOWN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TPOWERDOWN", parent, access, address, signed)
            self.TPOWERDOWN  =  self._TPOWERDOWN(self,  Access.RW,  0x000000FF,  0,  signed=False)

        class _TPOWERDOWN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPOWERDOWN", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _TSTEP(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TSTEP", parent, access, address, signed)
            self.TSTEP  =  self._TSTEP(self,  Access.R,  0x000FFFFF,  0,  signed=False)

        class _TSTEP(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSTEP", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _TPWMTHRS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TPWMTHRS", parent, access, address, signed)
            self.TPWMTHRS  =  self._TPWMTHRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _TPWMTHRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPWMTHRS", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _TCOOLTHRS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TCOOLTHRS", parent, access, address, signed)
            self.TCOOLTHRS  =  self._TCOOLTHRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _TCOOLTHRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TCOOLTHRS", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _THIGH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("THIGH", parent, access, address, signed)
            self.THIGH  =  self._THIGH(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _THIGH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("THIGH", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _TSGP_LOW_VEL_THRS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TSGP_LOW_VEL_THRS", parent, access, address, signed)
            self.TSGP_LOW_VEL_THRS  =  self._TSGP_LOW_VEL_THRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _TSGP_LOW_VEL_THRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSGP_LOW_VEL_THRS", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _T_RCOIL_MEAS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("T_RCOIL_MEAS", parent, access, address, signed)
            self.T_RCOIL_MEAS  =  self._T_RCOIL_MEAS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _T_RCOIL_MEAS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_RCOIL_MEAS", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _TUDCSTEP(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TUDCSTEP", parent, access, address, signed)
            self.TUDCSTEP  =  self._TUDCSTEP(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _TUDCSTEP(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TUDCSTEP", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _UDC_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("UDC_CONF", parent, access, address, signed)
            self.DECEL_THRS  =  self._DECEL_THRS(self,  Access.RW,  0x0000000F,  0,  signed=False)
            self.ACCEL_THRS  =  self._ACCEL_THRS(self,  Access.RW,  0x000000F0,  4,  signed=False)
            self.UDC_ENABLE  =  self._UDC_ENABLE(self,  Access.RW,  0x00000100,  8,  signed=False)

        class _DECEL_THRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DECEL_THRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ACCEL_THRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ACCEL_THRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UDC_ENABLE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UDC_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _STEPS_LOST(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("STEPS_LOST", parent, access, address, signed)
            self.STEPS_LOST  =  self._STEPS_LOST(self,  Access.RW,  0x000FFFFF,  0,  signed=True)

        class _STEPS_LOST(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STEPS_LOST", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RAMPMODE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RAMPMODE", parent, access, address, signed)
            self.RAMPMODE  =  self._RAMPMODE(self,  Access.RW,  0x00000003,  0,  signed=False)

        class _RAMPMODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.POSITION  =  Option(0,  parent,  "POSITION")
                    self.VEL_POS   =  Option(1,  parent,  "VEL_POS")
                    self.VEL_NEG   =  Option(2,  parent,  "VEL_NEG")
                    self.HOLD      =  Option(3,  parent,  "HOLD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPMODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _XACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("XACTUAL", parent, access, address, signed)
            self.XACTUAL  =  self._XACTUAL(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _XACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VACTUAL", parent, access, address, signed)
            self.VACTUAL  =  self._VACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

        class _VACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VSTART(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VSTART", parent, access, address, signed)
            self.VSTART  =  self._VSTART(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _VSTART(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSTART", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _A1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("A1", parent, access, address, signed)
            self.A1  =  self._A1(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _A1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _V1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("V1", parent, access, address, signed)
            self.V1  =  self._V1(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _V1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _AMAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("AMAX", parent, access, address, signed)
            self.AMAX  =  self._AMAX(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _AMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VMAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VMAX", parent, access, address, signed)
            self.VMAX  =  self._VMAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _VMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _DMAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("DMAX", parent, access, address, signed)
            self.DMAX  =  self._DMAX(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _DMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _TVMAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TVMAX", parent, access, address, signed)
            self.TVMAX  =  self._TVMAX(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _TVMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TVMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _D1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("D1", parent, access, address, signed)
            self.D1  =  self._D1(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _D1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VSTOP(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VSTOP", parent, access, address, signed)
            self.VSTOP  =  self._VSTOP(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _VSTOP(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSTOP", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _TZEROWAIT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TZEROWAIT", parent, access, address, signed)
            self.TZEROWAIT  =  self._TZEROWAIT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _TZEROWAIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TZEROWAIT", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _XTARGET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("XTARGET", parent, access, address, signed)
            self.XTARGET  =  self._XTARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _XTARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XTARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _V2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("V2", parent, access, address, signed)
            self.V2  =  self._V2(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _V2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V2", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _A2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("A2", parent, access, address, signed)
            self.A2  =  self._A2(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _A2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A2", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _D2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("D2", parent, access, address, signed)
            self.D2  =  self._D2(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _D2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D2", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _AACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("AACTUAL", parent, access, address, signed)
            self.AACTUAL  =  self._AACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

        class _AACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _SW_MODE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("SW_MODE", parent, access, address, signed)
            self.STOP_L_ENABLE          =  self._STOP_L_ENABLE(        self,  Access.RW,  0x00000001,  0,   signed=False)
            self.STOP_R_ENABLE          =  self._STOP_R_ENABLE(        self,  Access.RW,  0x00000002,  1,   signed=False)
            self.POL_STOP_L             =  self._POL_STOP_L(           self,  Access.RW,  0x00000004,  2,   signed=False)
            self.POL_STOP_R             =  self._POL_STOP_R(           self,  Access.RW,  0x00000008,  3,   signed=False)
            self.SWAP_LR                =  self._SWAP_LR(              self,  Access.RW,  0x00000010,  4,   signed=False)
            self.LATCH_L_ACTIVE         =  self._LATCH_L_ACTIVE(       self,  Access.RW,  0x00000020,  5,   signed=False)
            self.LATCH_L_INACTIVE       =  self._LATCH_L_INACTIVE(     self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LATCH_R_ACTIVE         =  self._LATCH_R_ACTIVE(       self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LATCH_R_INACTIVE       =  self._LATCH_R_INACTIVE(     self,  Access.RW,  0x00000100,  8,   signed=False)
            self.EN_LATCH_ENCODER       =  self._EN_LATCH_ENCODER(     self,  Access.RW,  0x00000200,  9,   signed=False)
            self.SG_STOP                =  self._SG_STOP(              self,  Access.RW,  0x00000400,  10,  signed=False)
            self.EN_SOFTSTOP            =  self._EN_SOFTSTOP(          self,  Access.RW,  0x00000800,  11,  signed=False)
            self.EN_VIRTUAL_STOP_L      =  self._EN_VIRTUAL_STOP_L(    self,  Access.RW,  0x00001000,  12,  signed=False)
            self.EN_VIRTUAL_STOP_R      =  self._EN_VIRTUAL_STOP_R(    self,  Access.RW,  0x00002000,  13,  signed=False)
            self.VIRTUAL_STOP_ENC       =  self._VIRTUAL_STOP_ENC(     self,  Access.RW,  0x00004000,  14,  signed=False)
            self.HARD_STOP_CLR_CUR_INT  =  self._HARD_STOP_CLR_CUR_INT(self,  Access.RW,  0x00008000,  15,  signed=False)

        class _STOP_L_ENABLE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_L_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STOP_R_ENABLE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_R_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _POL_STOP_L(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NON_INV  =  Option(False,  parent,  "NON_INV")
                    self.INV      =  Option(True,   parent,  "INV")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _POL_STOP_R(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NON_INV  =  Option(False,  parent,  "NON_INV")
                    self.INV      =  Option(True,   parent,  "INV")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SWAP_LR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DEFAULT  =  Option(False,  parent,  "DEFAULT")
                    self.SWAPPED  =  Option(True,   parent,  "SWAPPED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SWAP_LR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LATCH_L_ACTIVE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LATCH_L_INACTIVE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LATCH_R_ACTIVE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_R_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LATCH_R_INACTIVE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_R_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EN_LATCH_ENCODER(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_LATCH_ENCODER", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SG_STOP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_STOP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EN_SOFTSTOP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HARD_STOP  =  Option(False,  parent,  "HARD_STOP")
                    self.SOFT_STOP  =  Option(True,   parent,  "SOFT_STOP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_SOFTSTOP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EN_VIRTUAL_STOP_L(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_VIRTUAL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EN_VIRTUAL_STOP_R(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_VIRTUAL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VIRTUAL_STOP_ENC(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_ENC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _HARD_STOP_CLR_CUR_INT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HARD_STOP_CLR_CUR_INT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _RAMP_STAT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RAMP_STAT", parent, access, address, signed)
            self.STATUS_STOP_L          =  self._STATUS_STOP_L(        self,  Access.R,    0x00000001,  0,   signed=False)
            self.STATUS_STOP_R          =  self._STATUS_STOP_R(        self,  Access.R,    0x00000002,  1,   signed=False)
            self.STATUS_LATCH_L         =  self._STATUS_LATCH_L(       self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.STATUS_LATCH_R         =  self._STATUS_LATCH_R(       self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.EVENT_STOP_L           =  self._EVENT_STOP_L(         self,  Access.R,    0x00000010,  4,   signed=False)
            self.EVENT_STOP_R           =  self._EVENT_STOP_R(         self,  Access.R,    0x00000020,  5,   signed=False)
            self.EVENT_STOP_SG          =  self._EVENT_STOP_SG(        self,  Access.RWC,  0x00000040,  6,   signed=False)
            self.EVENT_POS_REACHED      =  self._EVENT_POS_REACHED(    self,  Access.RWC,  0x00000080,  7,   signed=False)
            self.VELOCITY_REACHED       =  self._VELOCITY_REACHED(     self,  Access.R,    0x00000100,  8,   signed=False)
            self.POSITION_REACHED       =  self._POSITION_REACHED(     self,  Access.R,    0x00000200,  9,   signed=False)
            self.VZERO                  =  self._VZERO(                self,  Access.R,    0x00000400,  10,  signed=False)
            self.T_ZEROWAIT_ACTIVE      =  self._T_ZEROWAIT_ACTIVE(    self,  Access.R,    0x00000800,  11,  signed=False)
            self.SECOND_MOVE            =  self._SECOND_MOVE(          self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.STATUS_SG              =  self._STATUS_SG(            self,  Access.R,    0x00002000,  13,  signed=False)
            self.STATUS_VIRTUAL_STOP_L  =  self._STATUS_VIRTUAL_STOP_L(self,  Access.R,    0x00004000,  14,  signed=False)
            self.STATUS_VIRTUAL_STOP_R  =  self._STATUS_VIRTUAL_STOP_R(self,  Access.R,    0x00008000,  15,  signed=False)

        class _STATUS_STOP_L(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STATUS_STOP_R(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STATUS_LATCH_L(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_L", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STATUS_LATCH_R(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_R", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EVENT_STOP_L(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EVENT_STOP_R(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EVENT_STOP_SG(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EVENT_POS_REACHED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VELOCITY_REACHED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.VMAX_NOT_REACHED  =  Option(False,  parent,  "VMAX_NOT_REACHED")
                    self.VMAX_REACHED      =  Option(True,   parent,  "VMAX_REACHED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _POSITION_REACHED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.POS_NOT_REACHED  =  Option(False,  parent,  "POS_NOT_REACHED")
                    self.POS_REACHED      =  Option(True,   parent,  "POS_REACHED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VZERO(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.V_NOT_0  =  Option(False,  parent,  "V_NOT_0")
                    self.V_0      =  Option(True,   parent,  "V_0")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VZERO", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _T_ZEROWAIT_ACTIVE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_ZEROWAIT_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SECOND_MOVE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SECOND_MOVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STATUS_SG(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NOSTALL  =  Option(False,  parent,  "NOSTALL")
                    self.STALL    =  Option(True,   parent,  "STALL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_SG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STATUS_VIRTUAL_STOP_L(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_VIRTUAL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STATUS_VIRTUAL_STOP_R(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_VIRTUAL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _XLATCH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("XLATCH", parent, access, address, signed)
            self.XLATCH  =  self._XLATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _XLATCH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XLATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ENCMODE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ENCMODE", parent, access, address, signed)
            self.POL_A            =  self._POL_A(          self,  Access.RW,  0x00000001,  0,   signed=False)
            self.POL_B            =  self._POL_B(          self,  Access.RW,  0x00000002,  1,   signed=False)
            self.POL_N            =  self._POL_N(          self,  Access.RW,  0x00000004,  2,   signed=False)
            self.IGNORE_AB        =  self._IGNORE_AB(      self,  Access.RW,  0x00000008,  3,   signed=False)
            self.CLR_CONT         =  self._CLR_CONT(       self,  Access.RW,  0x00000010,  4,   signed=False)
            self.CLR_ONCE         =  self._CLR_ONCE(       self,  Access.RW,  0x00000020,  5,   signed=False)
            self.POS_NEG_EDGE     =  self._POS_NEG_EDGE(   self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.CLR_ENC_X        =  self._CLR_ENC_X(      self,  Access.RW,  0x00000100,  8,   signed=False)
            self.LATCH_X_ACT      =  self._LATCH_X_ACT(    self,  Access.RW,  0x00000200,  9,   signed=False)
            self.ENC_SEL_DECIMAL  =  self._ENC_SEL_DECIMAL(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.NBEMF_ABN_SEL    =  self._NBEMF_ABN_SEL(  self,  Access.RW,  0x00000800,  11,  signed=False)
            self.BEMF_HYST        =  self._BEMF_HYST(      self,  Access.RW,  0x00007000,  12,  signed=False)
            self.BEMF_BLANK_TIME  =  self._BEMF_BLANK_TIME(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.BEMF_FILTER_SEL  =  self._BEMF_FILTER_SEL(self,  Access.RW,  0x30000000,  28,  signed=False)

        class _POL_A(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NEG  =  Option(False,  parent,  "NEG")
                    self.POS  =  Option(True,   parent,  "POS")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_A", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _POL_B(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NEG  =  Option(False,  parent,  "NEG")
                    self.POS  =  Option(True,   parent,  "POS")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_B", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _POL_N(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOW_ACTIVE   =  Option(False,  parent,  "LOW_ACTIVE")
                    self.HIGH_ACTIVE  =  Option(True,   parent,  "HIGH_ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POL_N", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _IGNORE_AB(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.N_AB_MATCH    =  Option(False,  parent,  "N_AB_MATCH")
                    self.N_AB_IGNORED  =  Option(True,   parent,  "N_AB_IGNORED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGNORE_AB", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLR_CONT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OFF         =  Option(False,  parent,  "OFF")
                    self.LATCH_CONT  =  Option(True,   parent,  "LATCH_CONT")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLR_CONT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLR_ONCE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OFF         =  Option(False,  parent,  "OFF")
                    self.LATCH_ONCE  =  Option(True,   parent,  "LATCH_ONCE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLR_ONCE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _POS_NEG_EDGE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HIGH_ACTIVE   =  Option(0,  parent,  "HIGH_ACTIVE")
                    self.RISING_EDGE   =  Option(1,  parent,  "RISING_EDGE")
                    self.FALLING_EDGE  =  Option(2,  parent,  "FALLING_EDGE")
                    self.BOTH_EDGES    =  Option(3,  parent,  "BOTH_EDGES")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POS_NEG_EDGE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLR_ENC_X(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.KEEP   =  Option(False,  parent,  "KEEP")
                    self.CLEAR  =  Option(True,   parent,  "CLEAR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLR_ENC_X", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LATCH_X_ACT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED       =  Option(False,  parent,  "DISABLED")
                    self.LATCH_XACTUAL  =  Option(True,   parent,  "LATCH_XACTUAL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_X_ACT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ENC_SEL_DECIMAL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.BINARY   =  Option(False,  parent,  "BINARY")
                    self.DECIMAL  =  Option(True,   parent,  "DECIMAL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_SEL_DECIMAL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _NBEMF_ABN_SEL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.TRICODER  =  Option(False,  parent,  "TRICODER")
                    self.ABN       =  Option(True,   parent,  "ABN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NBEMF_ABN_SEL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _BEMF_HYST(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HYST_10   =  Option(0,  parent,  "HYST_10")
                    self.HYST_25   =  Option(1,  parent,  "HYST_25")
                    self.HYST_50   =  Option(2,  parent,  "HYST_50")
                    self.HYST_75   =  Option(3,  parent,  "HYST_75")
                    self.HYST_100  =  Option(4,  parent,  "HYST_100")
                    self.HYST_150  =  Option(5,  parent,  "HYST_150")
                    self.HYST_200  =  Option(6,  parent,  "HYST_200")
                    self.HYST_250  =  Option(7,  parent,  "HYST_250")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_HYST", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _BEMF_BLANK_TIME(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_BLANK_TIME", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BEMF_FILTER_SEL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FILT_500   =  Option(0,  parent,  "FILT_500")
                    self.FILT_1000  =  Option(1,  parent,  "FILT_1000")
                    self.FILT_2000  =  Option(2,  parent,  "FILT_2000")
                    self.FILT_4300  =  Option(3,  parent,  "FILT_4300")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_FILTER_SEL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _X_ENC(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("X_ENC", parent, access, address, signed)
            self.X_ENC  =  self._X_ENC(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _X_ENC(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_ENC", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ENC_CONST(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_CONST", parent, access, address, signed)
            self.ENC_CONST  =  self._ENC_CONST(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _ENC_CONST(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_CONST", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ENC_STATUS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_STATUS", parent, access, address, signed)
            self.N_EVENT         =  self._N_EVENT(       self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.DEVIATION_WARN  =  self._DEVIATION_WARN(self,  Access.RWC,  0x00000002,  1,  signed=False)

        class _N_EVENT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_EVENT   =  Option(False,  parent,  "NO_EVENT")
                    self.EVENT_DET  =  Option(True,   parent,  "EVENT_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_EVENT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DEVIATION_WARN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_DEVIATON  =  Option(False,  parent,  "NO_DEVIATON")
                    self.DEVIATION    =  Option(True,   parent,  "DEVIATION")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DEVIATION_WARN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _ENC_LATCH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_LATCH", parent, access, address, signed)
            self.ENC_LATCH  =  self._ENC_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _ENC_LATCH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_LATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ENC_DEVIATION(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_DEVIATION", parent, access, address, signed)
            self.ENC_DEVIATION  =  self._ENC_DEVIATION(self,  Access.R,  0x000FFFFF,  0,  signed=False)

        class _ENC_DEVIATION(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VIRTUAL_STOP_L(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VIRTUAL_STOP_L", parent, access, address, signed)
            self.VIRTUAL_STOP_L  =  self._VIRTUAL_STOP_L(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _VIRTUAL_STOP_L(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VIRTUAL_STOP_R(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VIRTUAL_STOP_R", parent, access, address, signed)
            self.VIRTUAL_STOP_R  =  self._VIRTUAL_STOP_R(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _VIRTUAL_STOP_R(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _CURRENT_PI_REG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CURRENT_PI_REG", parent, access, address, signed)
            self.CUR_P  =  self._CUR_P(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.CUR_I  =  self._CUR_I(self,  Access.RW,  0x03FF0000,  16,  signed=False)

        class _CUR_P(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CUR_I(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_I", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ANGLE_PI_REG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANGLE_PI_REG", parent, access, address, signed)
            self.ANGLE_P  =  self._ANGLE_P(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.ANGLE_I  =  self._ANGLE_I(self,  Access.RW,  0x03FF0000,  16,  signed=False)

        class _ANGLE_P(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_I(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_I", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _CUR_ANGLE_LIMIT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CUR_ANGLE_LIMIT", parent, access, address, signed)
            self.ANGLE_PI_LIMIT         =  self._ANGLE_PI_LIMIT(       self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.ANGLE_PI_INT_POS_CLIP  =  self._ANGLE_PI_INT_POS_CLIP(self,  Access.R,   0x00001000,  12,  signed=False)
            self.ANGLE_PI_INT_NEG_CLIP  =  self._ANGLE_PI_INT_NEG_CLIP(self,  Access.R,   0x00002000,  13,  signed=False)
            self.ANGLE_PI_POS_CLIP      =  self._ANGLE_PI_POS_CLIP(    self,  Access.R,   0x00004000,  14,  signed=False)
            self.ANGLE_PI_NEG_CLIP      =  self._ANGLE_PI_NEG_CLIP(    self,  Access.R,   0x00008000,  15,  signed=False)
            self.CUR_PI_LIMIT           =  self._CUR_PI_LIMIT(         self,  Access.RW,  0x0FFF0000,  16,  signed=False)
            self.CUR_PI_INT_POS_CLIP    =  self._CUR_PI_INT_POS_CLIP(  self,  Access.R,   0x10000000,  28,  signed=False)
            self.CUR_PI_INT_NEG_CLIP    =  self._CUR_PI_INT_NEG_CLIP(  self,  Access.R,   0x20000000,  29,  signed=False)
            self.CUR_PI_POS_CLIP        =  self._CUR_PI_POS_CLIP(      self,  Access.R,   0x40000000,  30,  signed=False)
            self.CUR_PI_NEG_CLIP        =  self._CUR_PI_NEG_CLIP(      self,  Access.R,   0x80000000,  31,  signed=False)

        class _ANGLE_PI_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_PI_INT_POS_CLIP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IN_RANGE  =  Option(False,  parent,  "IN_RANGE")
                    self.CLIP      =  Option(True,   parent,  "CLIP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_INT_POS_CLIP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ANGLE_PI_INT_NEG_CLIP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IN_RANGE  =  Option(False,  parent,  "IN_RANGE")
                    self.CLIP      =  Option(True,   parent,  "CLIP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_INT_NEG_CLIP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ANGLE_PI_POS_CLIP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IN_RANGE  =  Option(False,  parent,  "IN_RANGE")
                    self.CLIP      =  Option(True,   parent,  "CLIP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_POS_CLIP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ANGLE_PI_NEG_CLIP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IN_RANGE  =  Option(False,  parent,  "IN_RANGE")
                    self.CLIP      =  Option(True,   parent,  "CLIP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_PI_NEG_CLIP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CUR_PI_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CUR_PI_INT_POS_CLIP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IN_RANGE  =  Option(False,  parent,  "IN_RANGE")
                    self.CLIP      =  Option(True,   parent,  "CLIP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_INT_POS_CLIP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CUR_PI_INT_NEG_CLIP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IN_RANGE  =  Option(False,  parent,  "IN_RANGE")
                    self.CLIP      =  Option(True,   parent,  "CLIP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_INT_NEG_CLIP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CUR_PI_POS_CLIP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IN_RANGE  =  Option(False,  parent,  "IN_RANGE")
                    self.CLIP      =  Option(True,   parent,  "CLIP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_POS_CLIP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CUR_PI_NEG_CLIP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IN_RANGE  =  Option(False,  parent,  "IN_RANGE")
                    self.CLIP      =  Option(True,   parent,  "CLIP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_PI_NEG_CLIP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _ANGLE_LOWER_LIMIT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANGLE_LOWER_LIMIT", parent, access, address, signed)
            self.ANGLE_LOWER_I_LIMIT  =  self._ANGLE_LOWER_I_LIMIT(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.ANGLE_ERROR          =  self._ANGLE_ERROR(        self,  Access.R,   0x03FF0000,  16,  signed=True)

        class _ANGLE_LOWER_I_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_LOWER_I_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_ERROR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _CUR_ANGLE_MEAS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CUR_ANGLE_MEAS", parent, access, address, signed)
            self.AMPL_MEAS   =  self._AMPL_MEAS( self,  Access.R,  0x00000FFF,  0,   signed=False)
            self.ANGLE_MEAS  =  self._ANGLE_MEAS(self,  Access.R,  0x03FF0000,  16,  signed=False)

        class _AMPL_MEAS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AMPL_MEAS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_MEAS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_MEAS", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _PI_RESULTS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PI_RESULTS", parent, access, address, signed)
            self.PWM_CALC         =  self._PWM_CALC(       self,  Access.R,  0x00001FFF,  0,   signed=True)
            self.ANGLE_CORR_CALC  =  self._ANGLE_CORR_CALC(self,  Access.R,  0x03FF0000,  16,  signed=True)

        class _PWM_CALC(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_CALC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ANGLE_CORR_CALC(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANGLE_CORR_CALC", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _COIL_INDUCT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COIL_INDUCT", parent, access, address, signed)
            self.COIL_INDUCT             =  self._COIL_INDUCT(           self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.RCOIL_MANUAL            =  self._RCOIL_MANUAL(          self,  Access.RW,  0x00010000,  16,  signed=False)
            self.RCOIL_THERMAL_COUPLING  =  self._RCOIL_THERMAL_COUPLING(self,  Access.RW,  0x00020000,  17,  signed=False)

        class _COIL_INDUCT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COIL_INDUCT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RCOIL_MANUAL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.AUTOMATIC  =  Option(False,  parent,  "AUTOMATIC")
                    self.USER       =  Option(True,   parent,  "USER")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RCOIL_MANUAL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _RCOIL_THERMAL_COUPLING(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RCOIL_THERMAL_COUPLING", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _R_COIL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("R_COIL", parent, access, address, signed)
            self.R_COIL_AUTO_B  =  self._R_COIL_AUTO_B(self,  Access.R,  0x00000FFF,  0,   signed=False)
            self.R_COIL_AUTO_A  =  self._R_COIL_AUTO_A(self,  Access.R,  0x0FFF0000,  16,  signed=False)

        class _R_COIL_AUTO_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("R_COIL_AUTO_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _R_COIL_AUTO_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("R_COIL_AUTO_A", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _R_COIL_USER(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("R_COIL_USER", parent, access, address, signed)
            self.R_COIL_USER_B  =  self._R_COIL_USER_B(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.R_COIL_USER_A  =  self._R_COIL_USER_A(self,  Access.RW,  0x0FFF0000,  16,  signed=False)

        class _R_COIL_USER_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("R_COIL_USER_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _R_COIL_USER_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("R_COIL_USER_A", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _SGP_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("SGP_CONF", parent, access, address, signed)
            self.SGP_THRS            =  self._SGP_THRS(          self,  Access.RW,  0x000001FF,  0,   signed=True)
            self.SGP_FILT_EN         =  self._SGP_FILT_EN(       self,  Access.RW,  0x00001000,  12,  signed=False)
            self.SGP_LOW_VEL_FREEZE  =  self._SGP_LOW_VEL_FREEZE(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.SGP_CLEAR_CUR_PI    =  self._SGP_CLEAR_CUR_PI(  self,  Access.RW,  0x00004000,  14,  signed=False)
            self.SGP_LOW_VEL_SLOPE   =  self._SGP_LOW_VEL_SLOPE( self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.SGP_LOW_VEL_CNTS    =  self._SGP_LOW_VEL_CNTS(  self,  Access.RW,  0x30000000,  28,  signed=False)

        class _SGP_THRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_THRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SGP_FILT_EN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FILT_DISABLED  =  Option(False,  parent,  "FILT_DISABLED")
                    self.FILT_ENABLED   =  Option(True,   parent,  "FILT_ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_FILT_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SGP_LOW_VEL_FREEZE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SET_0   =  Option(False,  parent,  "SET_0")
                    self.FREEZE  =  Option(True,   parent,  "FREEZE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_LOW_VEL_FREEZE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SGP_CLEAR_CUR_PI(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED   =  Option(False,  parent,  "DISABLED")
                    self.CLEAR_INT  =  Option(True,   parent,  "CLEAR_INT")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_CLEAR_CUR_PI", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SGP_LOW_VEL_SLOPE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_LOW_VEL_SLOPE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SGP_LOW_VEL_CNTS(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.EV_COUNT_1  =  Option(0,  parent,  "EV_COUNT_1")
                    self.EV_COUNT_2  =  Option(1,  parent,  "EV_COUNT_2")
                    self.EV_COUNT_3  =  Option(2,  parent,  "EV_COUNT_3")
                    self.EV_COUNT_4  =  Option(3,  parent,  "EV_COUNT_4")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_LOW_VEL_CNTS", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _SGP_IND_2_3(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("SGP_IND_2_3", parent, access, address, signed)
            self.SGP_IND_2  =  self._SGP_IND_2(self,  Access.R,  0x000003FF,  0,   signed=True)
            self.SGP_IND_3  =  self._SGP_IND_3(self,  Access.R,  0x03FF0000,  16,  signed=True)

        class _SGP_IND_2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_IND_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SGP_IND_3(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_IND_3", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _SGP_IND_0_1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("SGP_IND_0_1", parent, access, address, signed)
            self.SGP_IND_0  =  self._SGP_IND_0(self,  Access.R,  0x000003FF,  0,   signed=True)
            self.SGP_IND_1  =  self._SGP_IND_1(self,  Access.R,  0x03FF0000,  16,  signed=True)

        class _SGP_IND_0(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_IND_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SGP_IND_1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_IND_1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _INDUCTANCE_VOLTAGE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("INDUCTANCE_VOLTAGE", parent, access, address, signed)
            self.UL_B  =  self._UL_B(self,  Access.R,  0x00000FFF,  0,   signed=True)
            self.UL_A  =  self._UL_A(self,  Access.R,  0x0FFF0000,  16,  signed=True)

        class _UL_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UL_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UL_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UL_A", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _SGP_BEMF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("SGP_BEMF", parent, access, address, signed)
            self.SGP_RAW    =  self._SGP_RAW(  self,  Access.R,  0x000003FF,  0,   signed=True)
            self.UBEMF_ABS  =  self._UBEMF_ABS(self,  Access.R,  0x0FFF0000,  16,  signed=False)

        class _SGP_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_RAW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UBEMF_ABS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UBEMF_ABS", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _COOLSTEPPLUS_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_CONF", parent, access, address, signed)
            self.COOL_CUR_DIV  =  self._COOL_CUR_DIV(self,  Access.RW,  0x0000000F,  0,  signed=False)
            self.LOAD_FILT_EN  =  self._LOAD_FILT_EN(self,  Access.RW,  0x00000010,  4,  signed=False)

        class _COOL_CUR_DIV(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OFF_INSTANT    =  Option(0,   parent,  "OFF_INSTANT")
                    self.OFF_OFF_SPEED  =  Option(1,   parent,  "OFF_OFF_SPEED")
                    self.DIV_2          =  Option(2,   parent,  "DIV_2")
                    self.DIV_3          =  Option(3,   parent,  "DIV_3")
                    self.DIV_4          =  Option(4,   parent,  "DIV_4")
                    self.DIV_5          =  Option(5,   parent,  "DIV_5")
                    self.DIV_6          =  Option(6,   parent,  "DIV_6")
                    self.DIV_7          =  Option(7,   parent,  "DIV_7")
                    self.DIV_8          =  Option(8,   parent,  "DIV_8")
                    self.DIV_9          =  Option(9,   parent,  "DIV_9")
                    self.DIV_10         =  Option(10,  parent,  "DIV_10")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_CUR_DIV", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LOAD_FILT_EN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FILT_DISABLED  =  Option(False,  parent,  "FILT_DISABLED")
                    self.FILT_ENABLED   =  Option(True,   parent,  "FILT_ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LOAD_FILT_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _COOLSTEPPLUS_PI_REG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_PI_REG", parent, access, address, signed)
            self.COOLSTEP_P  =  self._COOLSTEP_P(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.COOLSTEP_I  =  self._COOLSTEP_I(self,  Access.RW,  0x03FF0000,  16,  signed=False)

        class _COOLSTEP_P(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOLSTEP_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COOLSTEP_I(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOLSTEP_I", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _COOLSTEPPLUS_PI_DOWN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_PI_DOWN", parent, access, address, signed)
            self.COOL_PI_DOWN_LIMIT  =  self._COOL_PI_DOWN_LIMIT(self,  Access.RW,  0x00000FFF,  0,   signed=False)
            self.COOL_PI_OFF_SPEED   =  self._COOL_PI_OFF_SPEED( self,  Access.RW,  0x0FFF0000,  16,  signed=False)

        class _COOL_PI_DOWN_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_PI_DOWN_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COOL_PI_OFF_SPEED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOL_PI_OFF_SPEED", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _COOLSTEPPLUS_RESERVE_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_RESERVE_CONF", parent, access, address, signed)
            self.LOW_LOAD_RESERVE         =  self._LOW_LOAD_RESERVE(       self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.HI_LOAD_RESERVE          =  self._HI_LOAD_RESERVE(        self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.LOW_GENERATORIC_RESERVE  =  self._LOW_GENERATORIC_RESERVE(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.HI_GENERATORIC_RESERVE   =  self._HI_GENERATORIC_RESERVE( self,  Access.RW,  0xFF000000,  24,  signed=False)

        class _LOW_LOAD_RESERVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LOW_LOAD_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HI_LOAD_RESERVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HI_LOAD_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LOW_GENERATORIC_RESERVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LOW_GENERATORIC_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HI_GENERATORIC_RESERVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HI_GENERATORIC_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _COOLSTEPPLUS_LOAD_RESERVE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COOLSTEPPLUS_LOAD_RESERVE", parent, access, address, signed)
            self.SGP_RESULT             =  self._SGP_RESULT(           self,  Access.R,  0x000003FF,  0,   signed=True)
            self.COOLSTEP_LOAD_RESERVE  =  self._COOLSTEP_LOAD_RESERVE(self,  Access.R,  0x01FF0000,  16,  signed=False)

        class _SGP_RESULT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGP_RESULT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COOLSTEP_LOAD_RESERVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COOLSTEP_LOAD_RESERVE", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _TSTEP_VELOCITY(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TSTEP_VELOCITY", parent, access, address, signed)
            self.TSTEP_VELOCITY  =  self._TSTEP_VELOCITY(self,  Access.R,  0x007FFFFF,  0,  signed=True)

        class _TSTEP_VELOCITY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSTEP_VELOCITY", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ADC_VSUPPLY_TEMP(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_VSUPPLY_TEMP", parent, access, address, signed)
            self.ADC_VSUPPLY  =  self._ADC_VSUPPLY(self,  Access.R,  0x000001FF,  0,   signed=False)
            self.ADC_TEMP     =  self._ADC_TEMP(   self,  Access.R,  0x01FF0000,  16,  signed=False)

        class _ADC_VSUPPLY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_VSUPPLY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_TEMP(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_TEMP", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ADC_I(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_I", parent, access, address, signed)
            self.ADC_I_A  =  self._ADC_I_A(self,  Access.R,  0x00000FFF,  0,   signed=True)
            self.ADC_I_B  =  self._ADC_I_B(self,  Access.R,  0x0FFF0000,  16,  signed=True)

        class _ADC_I_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_I_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_B", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _OTW_OV_VTH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("OTW_OV_VTH", parent, access, address, signed)
            self.OVERVOLTAGE_VTH         =  self._OVERVOLTAGE_VTH(       self,  Access.RW,  0x000001FF,  0,   signed=False)
            self.OVERTEMPPREWARNING_VTH  =  self._OVERTEMPPREWARNING_VTH(self,  Access.RW,  0x01FF0000,  16,  signed=False)

        class _OVERVOLTAGE_VTH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERVOLTAGE_VTH", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OVERTEMPPREWARNING_VTH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMPPREWARNING_VTH", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUT_0(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_0", parent, access, address, signed)
            self.MSLUT_0  =  self._MSLUT_0(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_0(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_0", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUT_1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_1", parent, access, address, signed)
            self.MSLUT_1  =  self._MSLUT_1(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUT_2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_2", parent, access, address, signed)
            self.MSLUT_2  =  self._MSLUT_2(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_2", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUT_3(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_3", parent, access, address, signed)
            self.MSLUT_3  =  self._MSLUT_3(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_3(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_3", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUT_4(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_4", parent, access, address, signed)
            self.MSLUT_4  =  self._MSLUT_4(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_4(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_4", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUT_5(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_5", parent, access, address, signed)
            self.MSLUT_5  =  self._MSLUT_5(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_5(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_5", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUT_6(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_6", parent, access, address, signed)
            self.MSLUT_6  =  self._MSLUT_6(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_6(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_6", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUT_7(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_7", parent, access, address, signed)
            self.MSLUT_7  =  self._MSLUT_7(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_7(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_7", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUTSEL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUTSEL", parent, access, address, signed)
            self.W0  =  self._W0(self,  Access.RW,  0x00000003,  0,   signed=False)
            self.W1  =  self._W1(self,  Access.RW,  0x0000000C,  2,   signed=False)
            self.W2  =  self._W2(self,  Access.RW,  0x00000030,  4,   signed=False)
            self.W3  =  self._W3(self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.X1  =  self._X1(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.X2  =  self._X2(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.X3  =  self._X3(self,  Access.RW,  0xFF000000,  24,  signed=False)

        class _W0(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.W0_SUB1_ADD0  =  Option(0,  parent,  "W0_SUB1_ADD0")
                    self.W0_ADD0_ADD1  =  Option(1,  parent,  "W0_ADD0_ADD1")
                    self.W0_ADD1_ADD2  =  Option(2,  parent,  "W0_ADD1_ADD2")
                    self.W0_ADD2_ADD3  =  Option(3,  parent,  "W0_ADD2_ADD3")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("W0", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _W1(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.W1_SUB1_ADD0  =  Option(0,  parent,  "W1_SUB1_ADD0")
                    self.W1_ADD0_ADD1  =  Option(1,  parent,  "W1_ADD0_ADD1")
                    self.W1_ADD1_ADD2  =  Option(2,  parent,  "W1_ADD1_ADD2")
                    self.W1_ADD2_ADD3  =  Option(3,  parent,  "W1_ADD2_ADD3")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("W1", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _W2(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.W2_SUB1_ADD0  =  Option(0,  parent,  "W2_SUB1_ADD0")
                    self.W2_ADD0_ADD1  =  Option(1,  parent,  "W2_ADD0_ADD1")
                    self.W2_ADD1_ADD2  =  Option(2,  parent,  "W2_ADD1_ADD2")
                    self.W2_ADD2_ADD3  =  Option(3,  parent,  "W2_ADD2_ADD3")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("W2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _W3(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.W3_SUB1_ADD0  =  Option(0,  parent,  "W3_SUB1_ADD0")
                    self.W3_ADD0_ADD1  =  Option(1,  parent,  "W3_ADD0_ADD1")
                    self.W3_ADD1_ADD2  =  Option(2,  parent,  "W3_ADD1_ADD2")
                    self.W3_ADD2_ADD3  =  Option(3,  parent,  "W3_ADD2_ADD3")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("W3", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _X1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _X2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _X3(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X3", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSLUTSTART(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUTSTART", parent, access, address, signed)
            self.START_SIN     =  self._START_SIN(   self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.START_SIN90   =  self._START_SIN90( self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.OFFSET_SIN90  =  self._OFFSET_SIN90(self,  Access.RW,  0xFF000000,  24,  signed=True)

        class _START_SIN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("START_SIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _START_SIN90(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("START_SIN90", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFFSET_SIN90(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET_SIN90", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSCNT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSCNT", parent, access, address, signed)
            self.MSCNT  =  self._MSCNT(self,  Access.R,  0x000003FF,  0,  signed=False)

        class _MSCNT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSCNT", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MSCURACT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MSCURACT", parent, access, address, signed)
            self.CUR_B  =  self._CUR_B(self,  Access.R,  0x000001FF,  0,   signed=True)
            self.CUR_A  =  self._CUR_A(self,  Access.R,  0x01FF0000,  16,  signed=True)

        class _CUR_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CUR_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_A", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _CHOPCONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CHOPCONF", parent, access, address, signed)
            self.TOFF          =  self._TOFF(        self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.HSTRT_TFD210  =  self._HSTRT_TFD210(self,  Access.RW,  0x00000070,  4,   signed=False)
            self.HEND_OFFSET   =  self._HEND_OFFSET( self,  Access.RW,  0x00000780,  7,   signed=False)
            self.FD3           =  self._FD3(         self,  Access.RW,  0x00000800,  11,  signed=False)
            self.DISFDCC       =  self._DISFDCC(     self,  Access.RW,  0x00001000,  12,  signed=False)
            self.CHM           =  self._CHM(         self,  Access.RW,  0x00004000,  14,  signed=False)
            self.TBL           =  self._TBL(         self,  Access.RW,  0x00018000,  15,  signed=False)
            self.TPFD          =  self._TPFD(        self,  Access.RW,  0x00F00000,  20,  signed=False)
            self.MRES          =  self._MRES(        self,  Access.RW,  0x0F000000,  24,  signed=False)
            self.INTPOL        =  self._INTPOL(      self,  Access.RW,  0x10000000,  28,  signed=False)
            self.DEDGE         =  self._DEDGE(       self,  Access.RW,  0x20000000,  29,  signed=False)

        class _TOFF(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DRIVER_OFF   =  Option(0,   parent,  "DRIVER_OFF")
                    self.TOFF_3_5US   =  Option(1,   parent,  "TOFF_3_5US")
                    self.TOFF_5_5US   =  Option(2,   parent,  "TOFF_5_5US")
                    self.TOFF_7_5US   =  Option(3,   parent,  "TOFF_7_5US")
                    self.TOFF_9_5US   =  Option(4,   parent,  "TOFF_9_5US")
                    self.TOFF_11_5US  =  Option(5,   parent,  "TOFF_11_5US")
                    self.TOFF_13_5US  =  Option(6,   parent,  "TOFF_13_5US")
                    self.TOFF_15_5US  =  Option(7,   parent,  "TOFF_15_5US")
                    self.TOFF_17_5US  =  Option(8,   parent,  "TOFF_17_5US")
                    self.TOFF_19_5US  =  Option(9,   parent,  "TOFF_19_5US")
                    self.TOFF_21_5US  =  Option(10,  parent,  "TOFF_21_5US")
                    self.TOFF_23_5US  =  Option(11,  parent,  "TOFF_23_5US")
                    self.TOFF_25_5US  =  Option(12,  parent,  "TOFF_25_5US")
                    self.TOFF_27_5US  =  Option(13,  parent,  "TOFF_27_5US")
                    self.TOFF_29_5US  =  Option(14,  parent,  "TOFF_29_5US")
                    self.TOFF_31_5US  =  Option(15,  parent,  "TOFF_31_5US")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TOFF", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _HSTRT_TFD210(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HSTRT_TFD210", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HEND_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HEND_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _FD3(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FD3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DISFDCC(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.COMP_ENABLED   =  Option(False,  parent,  "COMP_ENABLED")
                    self.COMP_DISABLED  =  Option(True,   parent,  "COMP_DISABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DISFDCC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CHM(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SPREADCYCLE   =  Option(False,  parent,  "SPREADCYCLE")
                    self.CLASSIC_CHOP  =  Option(True,   parent,  "CLASSIC_CHOP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHM", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _TBL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.TBL_1250  =  Option(0,  parent,  "TBL_1250")
                    self.TBL_1750  =  Option(1,  parent,  "TBL_1750")
                    self.TBL_2500  =  Option(2,  parent,  "TBL_2500")
                    self.TBL_3625  =  Option(3,  parent,  "TBL_3625")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TBL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _TPFD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPFD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MRES(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RES_256  =  Option(0,  parent,  "RES_256")
                    self.RES_128  =  Option(1,  parent,  "RES_128")
                    self.RES_64   =  Option(2,  parent,  "RES_64")
                    self.RES_32   =  Option(3,  parent,  "RES_32")
                    self.RES_16   =  Option(4,  parent,  "RES_16")
                    self.RES_8    =  Option(5,  parent,  "RES_8")
                    self.RES_4    =  Option(6,  parent,  "RES_4")
                    self.RES_HS   =  Option(7,  parent,  "RES_HS")
                    self.RES_FS   =  Option(8,  parent,  "RES_FS")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MRES", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _INTPOL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INTPOL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DEDGE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RISING_EDGE  =  Option(False,  parent,  "RISING_EDGE")
                    self.BOTH_EDGES   =  Option(True,   parent,  "BOTH_EDGES")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DEDGE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _COOLCONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COOLCONF", parent, access, address, signed)
            self.SEMIN         =  self._SEMIN(       self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.SEUP          =  self._SEUP(        self,  Access.RW,  0x00000060,  5,   signed=False)
            self.SEMAX         =  self._SEMAX(       self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.SEDN          =  self._SEDN(        self,  Access.RW,  0x00007000,  12,  signed=False)
            self.SEIMIN        =  self._SEIMIN(      self,  Access.RW,  0x00008000,  15,  signed=False)
            self.SGT           =  self._SGT(         self,  Access.RW,  0x007F0000,  16,  signed=True)
            self.THIGH_SG_OFF  =  self._THIGH_SG_OFF(self,  Access.RW,  0x00800000,  23,  signed=False)
            self.SFILT         =  self._SFILT(       self,  Access.RW,  0x01000000,  24,  signed=False)

        class _SEMIN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEMIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEUP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.STEP_UP_8   =  Option(0,  parent,  "STEP_UP_8")
                    self.STEP_UP_16  =  Option(1,  parent,  "STEP_UP_16")
                    self.STEP_UP_32  =  Option(2,  parent,  "STEP_UP_32")
                    self.STEP_UP_64  =  Option(3,  parent,  "STEP_UP_64")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEUP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SEMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEDN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.STEP_DOWN_EACH_8    =  Option(0,  parent,  "STEP_DOWN_EACH_8")
                    self.STEP_DOWN_EACH_4    =  Option(1,  parent,  "STEP_DOWN_EACH_4")
                    self.STEP_DOWN_EACH_2    =  Option(2,  parent,  "STEP_DOWN_EACH_2")
                    self.STEP_DOWN_EACH_1    =  Option(3,  parent,  "STEP_DOWN_EACH_1")
                    self.STEP_DOWN2_EACH_1   =  Option(4,  parent,  "STEP_DOWN2_EACH_1")
                    self.STEP_DOWN4_EACH_1   =  Option(5,  parent,  "STEP_DOWN4_EACH_1")
                    self.STEP_DOWN8_EACH_1   =  Option(6,  parent,  "STEP_DOWN8_EACH_1")
                    self.STEP_DOWN16_EACH_1  =  Option(7,  parent,  "STEP_DOWN16_EACH_1")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEDN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SEIMIN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IRUN_DIV2  =  Option(False,  parent,  "IRUN_DIV2")
                    self.IRUN_DIV4  =  Option(True,   parent,  "IRUN_DIV4")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEIMIN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SGT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SGT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _THIGH_SG_OFF(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DIS_CS                =  Option(False,  parent,  "DIS_CS")
                    self.DIS_CS_STOP_ON_STALL  =  Option(True,   parent,  "DIS_CS_STOP_ON_STALL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("THIGH_SG_OFF", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SFILT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FILT_DIS  =  Option(False,  parent,  "FILT_DIS")
                    self.FILT_EN   =  Option(True,   parent,  "FILT_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SFILT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _DRV_STATUS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("DRV_STATUS", parent, access, address, signed)
            self.SG_RESULT    =  self._SG_RESULT(  self,  Access.R,  0x000003FF,  0,   signed=False)
            self.SEQ_STOPPED  =  self._SEQ_STOPPED(self,  Access.R,  0x00000400,  10,  signed=False)
            self.OV           =  self._OV(         self,  Access.R,  0x00000800,  11,  signed=False)
            self.S2VSA        =  self._S2VSA(      self,  Access.R,  0x00001000,  12,  signed=False)
            self.S2VSB        =  self._S2VSB(      self,  Access.R,  0x00002000,  13,  signed=False)
            self.STEALTH      =  self._STEALTH(    self,  Access.R,  0x00004000,  14,  signed=False)
            self.CS_ACTUAL    =  self._CS_ACTUAL(  self,  Access.R,  0x00FF0000,  16,  signed=False)
            self.STALLGUARD   =  self._STALLGUARD( self,  Access.R,  0x01000000,  24,  signed=False)
            self.OT           =  self._OT(         self,  Access.R,  0x02000000,  25,  signed=False)
            self.OTPW         =  self._OTPW(       self,  Access.R,  0x04000000,  26,  signed=False)
            self.S2GA         =  self._S2GA(       self,  Access.R,  0x08000000,  27,  signed=False)
            self.S2GB         =  self._S2GB(       self,  Access.R,  0x10000000,  28,  signed=False)
            self.OLA          =  self._OLA(        self,  Access.R,  0x20000000,  29,  signed=False)
            self.OLB          =  self._OLB(        self,  Access.R,  0x40000000,  30,  signed=False)
            self.STST         =  self._STST(       self,  Access.R,  0x80000000,  31,  signed=False)

        class _SG_RESULT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_RESULT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEQ_STOPPED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.STOPPED      =  Option(True,   parent,  "STOPPED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEQ_STOPPED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OV(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.STOPPED      =  Option(True,   parent,  "STOPPED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OV", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _S2VSA(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.ERROR        =  Option(True,   parent,  "ERROR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("S2VSA", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _S2VSB(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.ERROR        =  Option(True,   parent,  "ERROR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("S2VSB", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STEALTH(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SPREADCYCLE  =  Option(False,  parent,  "SPREADCYCLE")
                    self.STEALTHCHOP  =  Option(True,   parent,  "STEALTHCHOP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STEALTH", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CS_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STALLGUARD(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NORMAL  =  Option(False,  parent,  "NORMAL")
                    self.STALL   =  Option(True,   parent,  "STALL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALLGUARD", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.ERROR        =  Option(True,   parent,  "ERROR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OTPW(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL   =  Option(False,  parent,  "OPERATIONAL")
                    self.OTPW_REACHED  =  Option(True,   parent,  "OTPW_REACHED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OTPW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _S2GA(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.ERROR        =  Option(True,   parent,  "ERROR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("S2GA", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _S2GB(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.ERROR        =  Option(True,   parent,  "ERROR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("S2GB", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OLA(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.OPEN_LOAD    =  Option(True,   parent,  "OPEN_LOAD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OLA", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OLB(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.OPEN_LOAD    =  Option(True,   parent,  "OPEN_LOAD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OLB", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STST(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STST", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _PWMCONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PWMCONF", parent, access, address, signed)
            self.PWM_FREQ       =  self._PWM_FREQ(     self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.FREEWHEEL      =  self._FREEWHEEL(    self,  Access.RW,  0x00000030,  4,   signed=False)
            self.OL_THRSH       =  self._OL_THRSH(     self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.SD_ON_MEAS_LO  =  self._SD_ON_MEAS_LO(self,  Access.RW,  0x0000F000,  12,  signed=False)
            self.SD_ON_MEAS_HI  =  self._SD_ON_MEAS_HI(self,  Access.RW,  0x000F0000,  16,  signed=False)

        class _PWM_FREQ(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.F_19_5  =  Option(0,  parent,  "F_19_5")
                    self.F_24_4  =  Option(1,  parent,  "F_24_4")
                    self.F_29_3  =  Option(2,  parent,  "F_29_3")
                    self.F_34_2  =  Option(3,  parent,  "F_34_2")
                    self.F_39_1  =  Option(4,  parent,  "F_39_1")
                    self.F_44    =  Option(5,  parent,  "F_44")
                    self.F_48_8  =  Option(6,  parent,  "F_48_8")
                    self.F_53_7  =  Option(7,  parent,  "F_53_7")
                    self.F_58_6  =  Option(8,  parent,  "F_58_6")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_FREQ", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _FREEWHEEL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NORMAL     =  Option(0,  parent,  "NORMAL")
                    self.FREEWHEEL  =  Option(1,  parent,  "FREEWHEEL")
                    self.LS_SHORT   =  Option(2,  parent,  "LS_SHORT")
                    self.HS_SHORT   =  Option(3,  parent,  "HS_SHORT")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FREEWHEEL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OL_THRSH(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.IRUN_12_5  =  Option(0,  parent,  "IRUN_12_5")
                    self.IRUN_25    =  Option(1,  parent,  "IRUN_25")
                    self.IRUN_50    =  Option(2,  parent,  "IRUN_50")
                    self.IRUN_75    =  Option(3,  parent,  "IRUN_75")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OL_THRSH", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SD_ON_MEAS_LO(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SD_ON_MEAS_LO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SD_ON_MEAS_HI(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SD_ON_MEAS_HI", parent, access, mask, shift, signed=signed)

                self.choice = None
