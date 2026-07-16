################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Choice, Option, Field, Register


class TMC5221Map:
    def __init__(self, *, channel=None, block=None, width=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(channel, block, width)


class _ALL_REGISTERS(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("ALL_REGISTERS", channel, block, width)
        self.GCR_GCONF                            =  self._GCR_GCONF(                          self,  Access.RW,   0x0000,  False)
        self.GCR_GSTAT                            =  self._GCR_GSTAT(                          self,  Access.RWC,  0x0001,  False)
        self.GCR_IOIN                             =  self._GCR_IOIN(                           self,  Access.R,    0x0004,  False)
        self.GCR_DRV_CONF                         =  self._GCR_DRV_CONF(                       self,  Access.RW,   0x0005,  False)
        self.GCR_GLOBAL_SCALER                    =  self._GCR_GLOBAL_SCALER(                  self,  Access.RW,   0x0006,  False)
        self.GCR_DIAG_CONF                        =  self._GCR_DIAG_CONF(                      self,  Access.RW,   0x0007,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT0       =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT0(     self,  Access.RW,   0x0008,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT1       =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT1(     self,  Access.RW,   0x0009,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT2       =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT2(     self,  Access.RW,   0x000A,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT3       =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT3(     self,  Access.RW,   0x000B,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT4       =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT4(     self,  Access.RW,   0x000C,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT5       =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT5(     self,  Access.RW,   0x000D,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT6       =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT6(     self,  Access.RW,   0x000E,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT7       =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT7(     self,  Access.RW,   0x000F,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT_START  =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT_START(self,  Access.RW,   0x0010,  False)
        self.MICROSTEP_LOOK_UP_TABLE_MSLUT_SEL    =  self._MICROSTEP_LOOK_UP_TABLE_MSLUT_SEL(  self,  Access.RW,   0x0011,  False)
        self.PC_X_COMPARE                         =  self._PC_X_COMPARE(                       self,  Access.RW,   0x0012,  True)
        self.PC_X_COMPARE_REPEAT                  =  self._PC_X_COMPARE_REPEAT(                self,  Access.RW,   0x0013,  False)
        self.VDR_IHOLD_IRUN                       =  self._VDR_IHOLD_IRUN(                     self,  Access.RW,   0x0014,  False)
        self.VDR_TPOWERDOWN                       =  self._VDR_TPOWERDOWN(                     self,  Access.RW,   0x0015,  False)
        self.VDR_TSTEP                            =  self._VDR_TSTEP(                          self,  Access.R,    0x0016,  False)
        self.VDR_TPWMTHRS                         =  self._VDR_TPWMTHRS(                       self,  Access.RW,   0x0017,  False)
        self.VDR_TCOOLTHRS                        =  self._VDR_TCOOLTHRS(                      self,  Access.RW,   0x0018,  False)
        self.VDR_THIGH                            =  self._VDR_THIGH(                          self,  Access.RW,   0x0019,  False)
        self.RGR_RAMPMODE                         =  self._RGR_RAMPMODE(                       self,  Access.RW,   0x001A,  False)
        self.RGR_XACTUAL                          =  self._RGR_XACTUAL(                        self,  Access.RW,   0x001B,  True)
        self.RGR_VACTUAL                          =  self._RGR_VACTUAL(                        self,  Access.R,    0x001C,  True)
        self.RGR_AACTUAL                          =  self._RGR_AACTUAL(                        self,  Access.R,    0x001D,  True)
        self.RGR_VSTART                           =  self._RGR_VSTART(                         self,  Access.RW,   0x001E,  False)
        self.RGR_A1                               =  self._RGR_A1(                             self,  Access.RW,   0x001F,  False)
        self.RGR_V1                               =  self._RGR_V1(                             self,  Access.RW,   0x0020,  False)
        self.RGR_A2                               =  self._RGR_A2(                             self,  Access.RW,   0x0021,  False)
        self.RGR_V2                               =  self._RGR_V2(                             self,  Access.RW,   0x0022,  False)
        self.RGR_AMAX                             =  self._RGR_AMAX(                           self,  Access.RW,   0x0023,  False)
        self.RGR_VMAX                             =  self._RGR_VMAX(                           self,  Access.RW,   0x0024,  False)
        self.RGR_DMAX                             =  self._RGR_DMAX(                           self,  Access.RW,   0x0025,  False)
        self.RGR_D2                               =  self._RGR_D2(                             self,  Access.RW,   0x0026,  False)
        self.RGR_D1                               =  self._RGR_D1(                             self,  Access.RW,   0x0027,  False)
        self.RGR_VSTOP                            =  self._RGR_VSTOP(                          self,  Access.RW,   0x0028,  False)
        self.RGR_TZEROWAIT                        =  self._RGR_TZEROWAIT(                      self,  Access.RW,   0x0029,  False)
        self.RGR_TVMAX                            =  self._RGR_TVMAX(                          self,  Access.RW,   0x002A,  False)
        self.RGR_XTARGET                          =  self._RGR_XTARGET(                        self,  Access.RW,   0x002B,  True)
        self.RGDR_VDCMIN                          =  self._RGDR_VDCMIN(                        self,  Access.RW,   0x002C,  False)
        self.RGDR_SW_MODE                         =  self._RGDR_SW_MODE(                       self,  Access.RW,   0x002D,  False)
        self.RGDR_RAMP_STAT                       =  self._RGDR_RAMP_STAT(                     self,  Access.RWC,  0x002E,  False)
        self.RGDR_XLATCH                          =  self._RGDR_XLATCH(                        self,  Access.R,    0x002F,  True)
        self.ER_X_BEMF                            =  self._ER_X_BEMF(                          self,  Access.RW,   0x0030,  True)
        self.ER_BEMF_CONF                         =  self._ER_BEMF_CONF(                       self,  Access.RW,   0x0031,  False)
        self.ER_BEMF_DEVIATION                    =  self._ER_BEMF_DEVIATION(                  self,  Access.RWC,  0x0032,  False)
        self.ER_VIRTUAL_STOP_L                    =  self._ER_VIRTUAL_STOP_L(                  self,  Access.RW,   0x0033,  True)
        self.ER_VIRTUAL_STOP_R                    =  self._ER_VIRTUAL_STOP_R(                  self,  Access.RW,   0x0034,  True)
        self.ER_X_BEMF_LATCH                      =  self._ER_X_BEMF_LATCH(                    self,  Access.R,    0x0035,  True)
        self.MDR_MSCNT                            =  self._MDR_MSCNT(                          self,  Access.R,    0x0036,  False)
        self.MDR_MSCURACT                         =  self._MDR_MSCURACT(                       self,  Access.R,    0x0037,  False)
        self.MDR_CHOPCONF                         =  self._MDR_CHOPCONF(                       self,  Access.RW,   0x0038,  False)
        self.MDR_COOLCONF                         =  self._MDR_COOLCONF(                       self,  Access.RW,   0x0039,  False)
        self.MDR_DCCTRL                           =  self._MDR_DCCTRL(                         self,  Access.RW,   0x003A,  False)
        self.MDR_DRV_STATUS                       =  self._MDR_DRV_STATUS(                     self,  Access.R,    0x003B,  False)
        self.MDR_PWMCONF                          =  self._MDR_PWMCONF(                        self,  Access.RW,   0x003C,  False)
        self.MDR_PWM_SCALE                        =  self._MDR_PWM_SCALE(                      self,  Access.R,    0x003D,  False)
        self.MDR_PWM_AUTO                         =  self._MDR_PWM_AUTO(                       self,  Access.R,    0x003E,  False)
        self.MDR_SG4_THRS                         =  self._MDR_SG4_THRS(                       self,  Access.RW,   0x003F,  False)
        self.MDR_SG4_RESULT                       =  self._MDR_SG4_RESULT(                     self,  Access.R,    0x0040,  False)
        self.MDR_SG4_IND                          =  self._MDR_SG4_IND(                        self,  Access.R,    0x0041,  False)
        self.MDR_SG_PREWARN_CONF                  =  self._MDR_SG_PREWARN_CONF(                self,  Access.RW,   0x0042,  False)
        self.ADC_ADC_SUPPLY_TEMP                  =  self._ADC_ADC_SUPPLY_TEMP(                self,  Access.RW,   0x0043,  False)
        self.LIMITS_VMAX_LIMIT                    =  self._LIMITS_VMAX_LIMIT(                  self,  Access.RW,   0x0044,  False)
        self.LIMITS_LIMIT_VALUES                  =  self._LIMITS_LIMIT_VALUES(                self,  Access.RW,   0x0045,  False)
        self.USER_DATA_USER_DATA_0                =  self._USER_DATA_USER_DATA_0(              self,  Access.RW,   0x0046,  False)
        self.USER_DATA_USER_DATA_1                =  self._USER_DATA_USER_DATA_1(              self,  Access.RW,   0x0047,  False)
        self.USER_DATA_USER_DATA_2                =  self._USER_DATA_USER_DATA_2(              self,  Access.RW,   0x0048,  False)
        self.USER_DATA_USER_DATA_3                =  self._USER_DATA_USER_DATA_3(              self,  Access.RW,   0x0049,  False)
        self.USER_DATA_USER_DATA_4                =  self._USER_DATA_USER_DATA_4(              self,  Access.RW,   0x004A,  False)
        self.USER_DATA_USER_DATA_5                =  self._USER_DATA_USER_DATA_5(              self,  Access.RW,   0x004B,  False)
        self.USER_DATA_USER_DATA_6                =  self._USER_DATA_USER_DATA_6(              self,  Access.RW,   0x004C,  False)
        self.USER_DATA_USER_DATA_7                =  self._USER_DATA_USER_DATA_7(              self,  Access.RW,   0x004D,  False)
        self.OTP_MODE_OTP_MODE                    =  self._OTP_MODE_OTP_MODE(                  self,  Access.RW,   0x007D,  False)

    class _GCR_GCONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("GCR_GCONF", parent, access, address, signed)
            self.EN_PWM_MODE             =  self._EN_PWM_MODE(           self,  Access.RW,  0x00000001,  0,   signed=False)
            self.MULTISTEP_FILT          =  self._MULTISTEP_FILT(        self,  Access.RW,  0x00000002,  1,   signed=False)
            self.SHAFT                   =  self._SHAFT(                 self,  Access.RW,  0x00000004,  2,   signed=False)
            self.SMALL_HYSTERESIS        =  self._SMALL_HYSTERESIS(      self,  Access.RW,  0x00000008,  3,   signed=False)
            self.STOP_ENABLE             =  self._STOP_ENABLE(           self,  Access.RW,  0x00000010,  4,   signed=False)
            self.REFR_STOP               =  self._REFR_STOP(             self,  Access.RW,  0x00000020,  5,   signed=False)
            self.DIRECT_MODE             =  self._DIRECT_MODE(           self,  Access.RW,  0x00000040,  6,   signed=False)
            self.SD                      =  self._SD(                    self,  Access.RW,  0x00000080,  7,   signed=False)
            self.QSC_STS_ENA             =  self._QSC_STS_ENA(           self,  Access.RW,  0x00000100,  8,   signed=False)
            self.DRV_EN_SW               =  self._DRV_EN_SW(             self,  Access.RW,  0x00000200,  9,   signed=False)
            self.SW_RESET                =  self._SW_RESET(              self,  Access.RW,  0x00000400,  10,  signed=False)
            self.S_IREF_INTCUR_EN        =  self._S_IREF_INTCUR_EN(      self,  Access.RW,  0x00000800,  11,  signed=False)
            self.DISABLE_DRIVER_ON_UVLO  =  self._DISABLE_DRIVER_ON_UVLO(self,  Access.RW,  0x00001000,  12,  signed=False)

        class _EN_PWM_MODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SPREADCYCLE  =  Option(False,  parent,  "SPREADCYCLE")
                    self.STEALTHCHOP  =  Option(True,   parent,  "STEALTHCHOP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_PWM_MODE", parent, access, mask, shift, signed=signed)

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
                    self.NORMAL   =  Option(False,  parent,  "NORMAL")
                    self.EM_STOP  =  Option(True,   parent,  "EM_STOP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _REFR_STOP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.REFL_EM_STOP  =  Option(False,  parent,  "REFL_EM_STOP")
                    self.REFR_EM_STOP  =  Option(True,   parent,  "REFR_EM_STOP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REFR_STOP", parent, access, mask, shift, signed=signed)

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

        class _SD(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INT_MCC  =  Option(False,  parent,  "INT_MCC")
                    self.EXT_SD   =  Option(True,   parent,  "EXT_SD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SD", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _QSC_STS_ENA(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("QSC_STS_ENA", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DRV_EN_SW(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DRV_EN_SW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SW_RESET(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FUNCTIONAL  =  Option(False,  parent,  "FUNCTIONAL")
                    self.SW_RESET    =  Option(True,   parent,  "SW_RESET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SW_RESET", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _S_IREF_INTCUR_EN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.EXT_RES  =  Option(False,  parent,  "EXT_RES")
                    self.INT_RES  =  Option(True,   parent,  "INT_RES")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("S_IREF_INTCUR_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DISABLE_DRIVER_ON_UVLO(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DISABLE_DRIVER_ON_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _GCR_GSTAT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("GCR_GSTAT", parent, access, address, signed)
            self.RESET           =  self._RESET(         self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.DRV_ERR         =  self._DRV_ERR(       self,  Access.RWC,  0x00000002,  1,  signed=False)
            self.UV_LDO          =  self._UV_LDO(        self,  Access.RWC,  0x00000004,  2,  signed=False)
            self.REGISTER_RESET  =  self._REGISTER_RESET(self,  Access.RWC,  0x00000008,  3,  signed=False)
            self.VM_UVLO         =  self._VM_UVLO(       self,  Access.RWC,  0x00000010,  4,  signed=False)
            self.VCCIO_RST       =  self._VCCIO_RST(     self,  Access.RWC,  0x00000020,  5,  signed=False)
            self.RREF_ERR        =  self._RREF_ERR(      self,  Access.RWC,  0x00000040,  6,  signed=False)
            self.VDD_UVLO        =  self._VDD_UVLO(      self,  Access.RWC,  0x00000080,  7,  signed=False)

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
                    self.DRV_DIS_DET  =  Option(True,   parent,  "DRV_DIS_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DRV_ERR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _UV_LDO(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.UV_LDO       =  Option(True,   parent,  "UV_LDO")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UV_LDO", parent, access, mask, shift, signed=signed)

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

        class _VCCIO_RST(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL     =  Option(False,  parent,  "OPERATIONAL")
                    self.VCCIO_UVLO_DET  =  Option(True,   parent,  "VCCIO_UVLO_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VCCIO_RST", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _RREF_ERR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL   =  Option(False,  parent,  "OPERATIONAL")
                    self.RREF_ERR_DET  =  Option(True,   parent,  "RREF_ERR_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RREF_ERR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VDD_UVLO(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL   =  Option(False,  parent,  "OPERATIONAL")
                    self.VDD_UVLO_DET  =  Option(True,   parent,  "VDD_UVLO_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDD_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _GCR_IOIN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("GCR_IOIN", parent, access, address, signed)
            self.SILICON_RV  =  self._SILICON_RV(self,  Access.R,  0x00700000,  20,  signed=False)
            self.EXT_CLK     =  self._EXT_CLK(   self,  Access.R,  0x01800000,  23,  signed=False)
            self.QSC         =  self._QSC(       self,  Access.R,  0x02000000,  25,  signed=False)
            self.ONSTATE     =  self._ONSTATE(   self,  Access.R,  0x04000000,  26,  signed=False)
            self.VERSION     =  self._VERSION(   self,  Access.R,  0xF0000000,  28,  signed=False)

        class _SILICON_RV(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SILICON_RV", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_CLK(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CLK_INT      =  Option(0,  parent,  "CLK_INT")
                    self.CLK_EXT      =  Option(1,  parent,  "CLK_EXT")
                    self.CLK_INT_QSC  =  Option(2,  parent,  "CLK_INT_QSC")
                    self.NOT_USED     =  Option(3,  parent,  "NOT_USED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_CLK", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _QSC(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.QSC          =  Option(True,   parent,  "QSC")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("QSC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ONSTATE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED    =  Option(False,  parent,  "DISABLED")
                    self.FUNCTIONAL  =  Option(True,   parent,  "FUNCTIONAL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ONSTATE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VERSION(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VERSION", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _GCR_DRV_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("GCR_DRV_CONF", parent, access, address, signed)
            self.FS_SENSE         =  self._FS_SENSE(       self,  Access.RW,  0x00000003,  0,   signed=False)
            self.FS_GAIN          =  self._FS_GAIN(        self,  Access.RW,  0x0000000C,  2,   signed=False)
            self.STANDSTILL_TIME  =  self._STANDSTILL_TIME(self,  Access.RW,  0x00070000,  16,  signed=False)

        class _FS_SENSE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RDSON_200  =  Option(0,  parent,  "RDSON_200")
                    self.RDSON_100  =  Option(1,  parent,  "RDSON_100")
                    self.RDSON_67   =  Option(2,  parent,  "RDSON_67")
                    self.RDSON_50   =  Option(3,  parent,  "RDSON_50")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FS_SENSE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _FS_GAIN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.GAIN_025  =  Option(0,  parent,  "GAIN_025")
                    self.GAIN_05   =  Option(1,  parent,  "GAIN_05")
                    self.GAIN_075  =  Option(2,  parent,  "GAIN_075")
                    self.GAIN_100  =  Option(3,  parent,  "GAIN_100")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FS_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STANDSTILL_TIME(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.T_STST_20  =  Option(0,  parent,  "T_STST_20")
                    self.T_STST_19  =  Option(1,  parent,  "T_STST_19")
                    self.T_STST_18  =  Option(2,  parent,  "T_STST_18")
                    self.T_STST_17  =  Option(3,  parent,  "T_STST_17")
                    self.T_STST_16  =  Option(4,  parent,  "T_STST_16")
                    self.T_STST_15  =  Option(5,  parent,  "T_STST_15")
                    self.T_STST_14  =  Option(6,  parent,  "T_STST_14")
                    self.T_STST_13  =  Option(7,  parent,  "T_STST_13")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STANDSTILL_TIME", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _GCR_GLOBAL_SCALER(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("GCR_GLOBAL_SCALER", parent, access, address, signed)
            self.GLOBALSCALER_A  =  self._GLOBALSCALER_A(self,  Access.RW,  0x000000FF,  0,  signed=False)
            self.GLOBALSCALER_B  =  self._GLOBALSCALER_B(self,  Access.RW,  0x0000FF00,  8,  signed=False)

        class _GLOBALSCALER_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GLOBALSCALER_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GLOBALSCALER_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GLOBALSCALER_B", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _GCR_DIAG_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("GCR_DIAG_CONF", parent, access, address, signed)
            self.DIAG0_ERROR             =  self._DIAG0_ERROR(           self,  Access.RW,  0x00000001,  0,   signed=False)
            self.DIAG0_OTPW              =  self._DIAG0_OTPW(            self,  Access.RW,  0x00000002,  1,   signed=False)
            self.DIAG0_STALL_PREWARN     =  self._DIAG0_STALL_PREWARN(   self,  Access.RW,  0x00000004,  2,   signed=False)
            self.DIAG0_STALL             =  self._DIAG0_STALL(           self,  Access.RW,  0x00000008,  3,   signed=False)
            self.DIAG0_INDEX             =  self._DIAG0_INDEX(           self,  Access.RW,  0x00000010,  4,   signed=False)
            self.DIAG0_STEP              =  self._DIAG0_STEP(            self,  Access.RW,  0x00000020,  5,   signed=False)
            self.DIAG0_DIR               =  self._DIAG0_DIR(             self,  Access.RW,  0x00000040,  6,   signed=False)
            self.DIAG0_XCOMP             =  self._DIAG0_XCOMP(           self,  Access.RW,  0x00000080,  7,   signed=False)
            self.DIAG0_EV_STOP_REF       =  self._DIAG0_EV_STOP_REF(     self,  Access.RW,  0x00000100,  8,   signed=False)
            self.DIAG0_EV_STOP_SG        =  self._DIAG0_EV_STOP_SG(      self,  Access.RW,  0x00000200,  9,   signed=False)
            self.DIAG0_EV_POS_REACHED    =  self._DIAG0_EV_POS_REACHED(  self,  Access.RW,  0x00000400,  10,  signed=False)
            self.DIAG0_EV_DEVIATION      =  self._DIAG0_EV_DEVIATION(    self,  Access.RW,  0x00000800,  11,  signed=False)
            self.DIAG0_EV_HOMING         =  self._DIAG0_EV_HOMING(       self,  Access.RW,  0x00001000,  12,  signed=False)
            self.DIAG0_POSITION_REACHED  =  self._DIAG0_POSITION_REACHED(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.DIAG1_ERROR             =  self._DIAG1_ERROR(           self,  Access.RW,  0x00004000,  14,  signed=False)
            self.DIAG1_OTPW              =  self._DIAG1_OTPW(            self,  Access.RW,  0x00008000,  15,  signed=False)
            self.DIAG1_STALL_PREWARN     =  self._DIAG1_STALL_PREWARN(   self,  Access.RW,  0x00010000,  16,  signed=False)
            self.DIAG1_STALL             =  self._DIAG1_STALL(           self,  Access.RW,  0x00020000,  17,  signed=False)
            self.DIAG1_INDEX             =  self._DIAG1_INDEX(           self,  Access.RW,  0x00040000,  18,  signed=False)
            self.DIAG1_STEP              =  self._DIAG1_STEP(            self,  Access.RW,  0x00080000,  19,  signed=False)
            self.DIAG1_DIR               =  self._DIAG1_DIR(             self,  Access.RW,  0x00100000,  20,  signed=False)
            self.DIAG1_XCOMP             =  self._DIAG1_XCOMP(           self,  Access.RW,  0x00200000,  21,  signed=False)
            self.DIAG1_EV_STOP_REF       =  self._DIAG1_EV_STOP_REF(     self,  Access.RW,  0x00400000,  22,  signed=False)
            self.DIAG1_EV_STOP_SG        =  self._DIAG1_EV_STOP_SG(      self,  Access.RW,  0x00800000,  23,  signed=False)
            self.DIAG1_EV_POS_REACHED    =  self._DIAG1_EV_POS_REACHED(  self,  Access.RW,  0x01000000,  24,  signed=False)
            self.DIAG1_EV_DEVIATION      =  self._DIAG1_EV_DEVIATION(    self,  Access.RW,  0x02000000,  25,  signed=False)
            self.DIAG1_EV_HOMING         =  self._DIAG1_EV_HOMING(       self,  Access.RW,  0x04000000,  26,  signed=False)
            self.DIAG1_POSITION_REACHED  =  self._DIAG1_POSITION_REACHED(self,  Access.RW,  0x08000000,  27,  signed=False)
            self.DIAG0_NOD_PP            =  self._DIAG0_NOD_PP(          self,  Access.RW,  0x10000000,  28,  signed=False)
            self.DIAG0_INVPP             =  self._DIAG0_INVPP(           self,  Access.RW,  0x20000000,  29,  signed=False)
            self.DIAG1_NOD_PP            =  self._DIAG1_NOD_PP(          self,  Access.RW,  0x40000000,  30,  signed=False)
            self.DIAG1_INVPP             =  self._DIAG1_INVPP(           self,  Access.RW,  0x80000000,  31,  signed=False)

        class _DIAG0_ERROR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_OTPW(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_OTPW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_STALL_PREWARN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_STALL_PREWARN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_STALL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_STALL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_INDEX(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_INDEX", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_STEP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_STEP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_DIR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_DIR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_XCOMP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_XCOMP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_EV_STOP_REF(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_EV_STOP_REF", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_EV_STOP_SG(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_EV_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_EV_POS_REACHED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_EV_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_EV_DEVIATION(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_EV_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_EV_HOMING(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_EV_HOMING", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_POSITION_REACHED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_POSITION_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_ERROR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_OTPW(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_OTPW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_STALL_PREWARN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_STALL_PREWARN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_STALL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_STALL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_INDEX(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_INDEX", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_STEP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_STEP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_DIR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_DIR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_XCOMP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_XCOMP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_EV_STOP_REF(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_EV_STOP_REF", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_EV_STOP_SG(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_EV_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_EV_POS_REACHED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_EV_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_EV_DEVIATION(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_EV_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_EV_HOMING(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_EV_HOMING", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_POSITION_REACHED(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_POSITION_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_NOD_PP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPEN_DRAIN  =  Option(False,  parent,  "OPEN_DRAIN")
                    self.PUSH_PULL   =  Option(True,   parent,  "PUSH_PULL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_NOD_PP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_INVPP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HI_ACTIVE  =  Option(False,  parent,  "HI_ACTIVE")
                    self.LO_ACTIVE  =  Option(True,   parent,  "LO_ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_INVPP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_NOD_PP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPEN_DRAIN  =  Option(False,  parent,  "OPEN_DRAIN")
                    self.PUSH_PULL   =  Option(True,   parent,  "PUSH_PULL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_NOD_PP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_INVPP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HI_ACTIVE  =  Option(False,  parent,  "HI_ACTIVE")
                    self.LO_ACTIVE  =  Option(True,   parent,  "LO_ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_INVPP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT0(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT0", parent, access, address, signed)
            self.MSLUT_0  =  self._MSLUT_0(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_0(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_0", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT1", parent, access, address, signed)
            self.MSLUT_1  =  self._MSLUT_1(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT2", parent, access, address, signed)
            self.MSLUT_2  =  self._MSLUT_2(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_2", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT3(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT3", parent, access, address, signed)
            self.MSLUT_3  =  self._MSLUT_3(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_3(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_3", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT4(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT4", parent, access, address, signed)
            self.MSLUT_4  =  self._MSLUT_4(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_4(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_4", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT5(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT5", parent, access, address, signed)
            self.MSLUT_5  =  self._MSLUT_5(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_5(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_5", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT6(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT6", parent, access, address, signed)
            self.MSLUT_6  =  self._MSLUT_6(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_6(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_6", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT7(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT7", parent, access, address, signed)
            self.MSLUT_7  =  self._MSLUT_7(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _MSLUT_7(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_7", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT_START(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT_START", parent, access, address, signed)
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

    class _MICROSTEP_LOOK_UP_TABLE_MSLUT_SEL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MICROSTEP_LOOK_UP_TABLE_MSLUT_SEL", parent, access, address, signed)
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

    class _PC_X_COMPARE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PC_X_COMPARE", parent, access, address, signed)
            self.X_COMPARE  =  self._X_COMPARE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _X_COMPARE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_COMPARE", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _PC_X_COMPARE_REPEAT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PC_X_COMPARE_REPEAT", parent, access, address, signed)
            self.X_COMPARE_REPEAT  =  self._X_COMPARE_REPEAT(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

        class _X_COMPARE_REPEAT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_COMPARE_REPEAT", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VDR_IHOLD_IRUN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VDR_IHOLD_IRUN", parent, access, address, signed)
            self.IHOLD       =  self._IHOLD(     self,  Access.RW,  0x0000001F,  0,   signed=False)
            self.IRUN        =  self._IRUN(      self,  Access.RW,  0x00001F00,  8,   signed=False)
            self.IHOLDDELAY  =  self._IHOLDDELAY(self,  Access.RW,  0x000F0000,  16,  signed=False)
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
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INSTANT       =  Option(0,   parent,  "INSTANT")
                    self.DELAY_1_218   =  Option(1,   parent,  "DELAY_1_218")
                    self.DELAY_2_218   =  Option(2,   parent,  "DELAY_2_218")
                    self.DELAY_3_218   =  Option(3,   parent,  "DELAY_3_218")
                    self.DELAY_4_218   =  Option(4,   parent,  "DELAY_4_218")
                    self.DELAY_5_218   =  Option(5,   parent,  "DELAY_5_218")
                    self.DELAY_6_218   =  Option(6,   parent,  "DELAY_6_218")
                    self.DELAY_7_218   =  Option(7,   parent,  "DELAY_7_218")
                    self.DELAY_8_218   =  Option(8,   parent,  "DELAY_8_218")
                    self.DELAY_9_218   =  Option(9,   parent,  "DELAY_9_218")
                    self.DELAY_10_218  =  Option(10,  parent,  "DELAY_10_218")
                    self.DELAY_11_218  =  Option(11,  parent,  "DELAY_11_218")
                    self.DELAY_12_218  =  Option(12,  parent,  "DELAY_12_218")
                    self.DELAY_13_218  =  Option(13,  parent,  "DELAY_13_218")
                    self.DELAY_14_218  =  Option(14,  parent,  "DELAY_14_218")
                    self.DELAY_15_218  =  Option(15,  parent,  "DELAY_15_218")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IHOLDDELAY", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _IRUNDELAY(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INSTANT     =  Option(0,   parent,  "INSTANT")
                    self.DELAY_512   =  Option(1,   parent,  "DELAY_512")
                    self.DELAY_1024  =  Option(2,   parent,  "DELAY_1024")
                    self.DELAY_1536  =  Option(3,   parent,  "DELAY_1536")
                    self.DELAY_2048  =  Option(4,   parent,  "DELAY_2048")
                    self.DELAY_2560  =  Option(5,   parent,  "DELAY_2560")
                    self.DELAY_3072  =  Option(6,   parent,  "DELAY_3072")
                    self.DELAY_3584  =  Option(7,   parent,  "DELAY_3584")
                    self.DELAY_4096  =  Option(8,   parent,  "DELAY_4096")
                    self.DELAY_4608  =  Option(9,   parent,  "DELAY_4608")
                    self.DELAY_5120  =  Option(10,  parent,  "DELAY_5120")
                    self.DELAY_5632  =  Option(11,  parent,  "DELAY_5632")
                    self.DELAY_6144  =  Option(12,  parent,  "DELAY_6144")
                    self.DELAY_6656  =  Option(13,  parent,  "DELAY_6656")
                    self.DELAY_7168  =  Option(14,  parent,  "DELAY_7168")
                    self.DELAY_7680  =  Option(15,  parent,  "DELAY_7680")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IRUNDELAY", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _VDR_TPOWERDOWN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VDR_TPOWERDOWN", parent, access, address, signed)
            self.TPOWERDOWN  =  self._TPOWERDOWN(self,  Access.RW,  0x000000FF,  0,  signed=False)

        class _TPOWERDOWN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPOWERDOWN", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VDR_TSTEP(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VDR_TSTEP", parent, access, address, signed)
            self.TSTEP  =  self._TSTEP(self,  Access.R,  0x000FFFFF,  0,  signed=False)

        class _TSTEP(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSTEP", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VDR_TPWMTHRS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VDR_TPWMTHRS", parent, access, address, signed)
            self.TPWMTHRS  =  self._TPWMTHRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _TPWMTHRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPWMTHRS", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VDR_TCOOLTHRS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VDR_TCOOLTHRS", parent, access, address, signed)
            self.TCOOLTHRS  =  self._TCOOLTHRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _TCOOLTHRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TCOOLTHRS", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _VDR_THIGH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VDR_THIGH", parent, access, address, signed)
            self.THIGH  =  self._THIGH(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _THIGH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("THIGH", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_RAMPMODE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_RAMPMODE", parent, access, address, signed)
            self.RAMPMODE  =  self._RAMPMODE(self,  Access.RW,  0x00000003,  0,  signed=False)

        class _RAMPMODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.POS_MODE  =  Option(0,  parent,  "POS_MODE")
                    self.VEL_POS   =  Option(1,  parent,  "VEL_POS")
                    self.VEL_NEG   =  Option(2,  parent,  "VEL_NEG")
                    self.HOLD      =  Option(3,  parent,  "HOLD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPMODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _RGR_XACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_XACTUAL", parent, access, address, signed)
            self.XACTUAL  =  self._XACTUAL(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _XACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_VACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_VACTUAL", parent, access, address, signed)
            self.VACTUAL  =  self._VACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

        class _VACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_AACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_AACTUAL", parent, access, address, signed)
            self.AACTUAL  =  self._AACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

        class _AACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_VSTART(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_VSTART", parent, access, address, signed)
            self.VSTART  =  self._VSTART(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _VSTART(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSTART", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_A1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_A1", parent, access, address, signed)
            self.A1  =  self._A1(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _A1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_V1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_V1", parent, access, address, signed)
            self.V1  =  self._V1(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _V1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_A2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_A2", parent, access, address, signed)
            self.A2  =  self._A2(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _A2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A2", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_V2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_V2", parent, access, address, signed)
            self.V2  =  self._V2(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

        class _V2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V2", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_AMAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_AMAX", parent, access, address, signed)
            self.AMAX  =  self._AMAX(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _AMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_VMAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_VMAX", parent, access, address, signed)
            self.VMAX  =  self._VMAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _VMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_DMAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_DMAX", parent, access, address, signed)
            self.DMAX  =  self._DMAX(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _DMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_D2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_D2", parent, access, address, signed)
            self.D2  =  self._D2(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _D2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D2", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_D1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_D1", parent, access, address, signed)
            self.D1  =  self._D1(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _D1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_VSTOP(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_VSTOP", parent, access, address, signed)
            self.VSTOP  =  self._VSTOP(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

        class _VSTOP(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSTOP", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_TZEROWAIT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_TZEROWAIT", parent, access, address, signed)
            self.TZEROWAIT  =  self._TZEROWAIT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _TZEROWAIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TZEROWAIT", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_TVMAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_TVMAX", parent, access, address, signed)
            self.TVMAX  =  self._TVMAX(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _TVMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TVMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGR_XTARGET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGR_XTARGET", parent, access, address, signed)
            self.XTARGET  =  self._XTARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _XTARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XTARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGDR_VDCMIN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGDR_VDCMIN", parent, access, address, signed)
            self.VDCMIN  =  self._VDCMIN(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _VDCMIN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDCMIN", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _RGDR_SW_MODE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGDR_SW_MODE", parent, access, address, signed)
            self.STOP_L_ENABLE      =  self._STOP_L_ENABLE(    self,  Access.RW,  0x00000001,  0,   signed=False)
            self.STOP_R_ENABLE      =  self._STOP_R_ENABLE(    self,  Access.RW,  0x00000002,  1,   signed=False)
            self.POL_STOP_L         =  self._POL_STOP_L(       self,  Access.RW,  0x00000004,  2,   signed=False)
            self.POL_STOP_R         =  self._POL_STOP_R(       self,  Access.RW,  0x00000008,  3,   signed=False)
            self.SWAP_LR            =  self._SWAP_LR(          self,  Access.RW,  0x00000010,  4,   signed=False)
            self.LATCH_L_ACTIVE     =  self._LATCH_L_ACTIVE(   self,  Access.RW,  0x00000020,  5,   signed=False)
            self.LATCH_L_INACTIVE   =  self._LATCH_L_INACTIVE( self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LATCH_R_ACTIVE     =  self._LATCH_R_ACTIVE(   self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LATCH_R_INACTIVE   =  self._LATCH_R_INACTIVE( self,  Access.RW,  0x00000100,  8,   signed=False)
            self.SG_STOP            =  self._SG_STOP(          self,  Access.RW,  0x00000400,  10,  signed=False)
            self.EN_SOFTSTOP        =  self._EN_SOFTSTOP(      self,  Access.RW,  0x00000800,  11,  signed=False)
            self.EN_VIRTUAL_STOP_L  =  self._EN_VIRTUAL_STOP_L(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.EN_VIRTUAL_STOP_R  =  self._EN_VIRTUAL_STOP_R(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.EN_REFL_HOMING     =  self._EN_REFL_HOMING(   self,  Access.RW,  0x00004000,  14,  signed=False)
            self.EN_REFR_HOMING     =  self._EN_REFR_HOMING(   self,  Access.RW,  0x00008000,  15,  signed=False)
            self.EN_AUTO_FEATURE    =  self._EN_AUTO_FEATURE(  self,  Access.RW,  0x00010000,  16,  signed=False)

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

        class _EN_REFL_HOMING(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_REFL_HOMING", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EN_REFR_HOMING(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_REFR_HOMING", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _EN_AUTO_FEATURE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN_AUTO_FEATURE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _RGDR_RAMP_STAT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGDR_RAMP_STAT", parent, access, address, signed)
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
            self.REFL_HOMING            =  self._REFL_HOMING(          self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.REFR_HOMING            =  self._REFR_HOMING(          self,  Access.RWC,  0x00020000,  17,  signed=False)

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
                    self.VEL_NOT_VMAX  =  Option(False,  parent,  "VEL_NOT_VMAX")
                    self.VEL_VMAX      =  Option(True,   parent,  "VEL_VMAX")

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
                    self.VEL_NOT_0  =  Option(False,  parent,  "VEL_NOT_0")
                    self.VEL_0      =  Option(True,   parent,  "VEL_0")

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
                    self.NO_STALL  =  Option(False,  parent,  "NO_STALL")
                    self.STALL     =  Option(True,   parent,  "STALL")

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

        class _REFL_HOMING(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REFL_HOMING", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _REFR_HOMING(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REFR_HOMING", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _RGDR_XLATCH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RGDR_XLATCH", parent, access, address, signed)
            self.XLATCH  =  self._XLATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _XLATCH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XLATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ER_X_BEMF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ER_X_BEMF", parent, access, address, signed)
            self.X_BEMF  =  self._X_BEMF(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _X_BEMF(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_BEMF", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ER_BEMF_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ER_BEMF_CONF", parent, access, address, signed)
            self.BEMF_HYST        =  self._BEMF_HYST(      self,  Access.RW,  0x00000007,  0,   signed=False)
            self.QSC_TRICODER_EN  =  self._QSC_TRICODER_EN(self,  Access.RW,  0x00000008,  3,   signed=False)
            self.BEMF_BLANK_TIME  =  self._BEMF_BLANK_TIME(self,  Access.RW,  0x00000FF0,  4,   signed=False)
            self.BEMF_FILTER_SEL  =  self._BEMF_FILTER_SEL(self,  Access.RW,  0x00003000,  12,  signed=False)
            self.BEMF_INCREMENT   =  self._BEMF_INCREMENT( self,  Access.RW,  0x000F0000,  16,  signed=False)
            self.BEMF_DIR         =  self._BEMF_DIR(       self,  Access.RW,  0x00100000,  20,  signed=False)
            self.BEMF_OVERWRITE   =  self._BEMF_OVERWRITE( self,  Access.RW,  0x00200000,  21,  signed=False)

        class _BEMF_HYST(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HYST_10MV   =  Option(0,  parent,  "HYST_10MV")
                    self.HYST_25MV   =  Option(1,  parent,  "HYST_25MV")
                    self.HYST_50MV   =  Option(2,  parent,  "HYST_50MV")
                    self.HYST_75MV   =  Option(3,  parent,  "HYST_75MV")
                    self.HYST_100MV  =  Option(4,  parent,  "HYST_100MV")
                    self.HYST_150MV  =  Option(5,  parent,  "HYST_150MV")
                    self.HYST_200MV  =  Option(6,  parent,  "HYST_200MV")
                    self.HYST_250MV  =  Option(7,  parent,  "HYST_250MV")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_HYST", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _QSC_TRICODER_EN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.QSC_OFF  =  Option(False,  parent,  "QSC_OFF")
                    self.QSC_ON   =  Option(True,   parent,  "QSC_ON")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("QSC_TRICODER_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _BEMF_BLANK_TIME(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_BLANK_TIME", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BEMF_FILTER_SEL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.F_DIV24600  =  Option(0,  parent,  "F_DIV24600")
                    self.F_DIV12300  =  Option(1,  parent,  "F_DIV12300")
                    self.F_DIV6150   =  Option(2,  parent,  "F_DIV6150")
                    self.F_DIV2870   =  Option(3,  parent,  "F_DIV2870")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_FILTER_SEL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _BEMF_INCREMENT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FS_1    =  Option(0,  parent,  "FS_1")
                    self.FS_2    =  Option(1,  parent,  "FS_2")
                    self.FS_4    =  Option(2,  parent,  "FS_4")
                    self.FS_8    =  Option(3,  parent,  "FS_8")
                    self.FS_16   =  Option(4,  parent,  "FS_16")
                    self.FS_32   =  Option(5,  parent,  "FS_32")
                    self.FS_64   =  Option(6,  parent,  "FS_64")
                    self.FS_128  =  Option(7,  parent,  "FS_128")
                    self.FS_256  =  Option(8,  parent,  "FS_256")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_INCREMENT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _BEMF_DIR(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NON_INV  =  Option(False,  parent,  "NON_INV")
                    self.INV      =  Option(True,   parent,  "INV")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_DIR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _BEMF_OVERWRITE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BEMF_OVERWRITE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _ER_BEMF_DEVIATION(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ER_BEMF_DEVIATION", parent, access, address, signed)
            self.DEVIATION       =  self._DEVIATION(     self,  Access.RW,   0x000FFFFF,  0,   signed=False)
            self.DEVIATION_WARN  =  self._DEVIATION_WARN(self,  Access.RWC,  0x01000000,  24,  signed=False)

        class _DEVIATION(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DEVIATION_WARN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DEVIATION_WARN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _ER_VIRTUAL_STOP_L(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ER_VIRTUAL_STOP_L", parent, access, address, signed)
            self.VIRTUAL_STOP_L  =  self._VIRTUAL_STOP_L(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _VIRTUAL_STOP_L(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ER_VIRTUAL_STOP_R(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ER_VIRTUAL_STOP_R", parent, access, address, signed)
            self.VIRTUAL_STOP_R  =  self._VIRTUAL_STOP_R(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _VIRTUAL_STOP_R(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _ER_X_BEMF_LATCH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ER_X_BEMF_LATCH", parent, access, address, signed)
            self.X_BEMF_LATCH  =  self._X_BEMF_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _X_BEMF_LATCH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_BEMF_LATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MDR_MSCNT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_MSCNT", parent, access, address, signed)
            self.MSCNT  =  self._MSCNT(self,  Access.R,  0x000003FF,  0,  signed=False)

        class _MSCNT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSCNT", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MDR_MSCURACT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_MSCURACT", parent, access, address, signed)
            self.CUR_A  =  self._CUR_A(self,  Access.R,  0x000001FF,  0,   signed=True)
            self.CUR_B  =  self._CUR_B(self,  Access.R,  0x01FF0000,  16,  signed=True)

        class _CUR_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CUR_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_B", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MDR_CHOPCONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_CHOPCONF", parent, access, address, signed)
            self.TOFF      =  self._TOFF(    self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.HSTRT     =  self._HSTRT(   self,  Access.RW,  0x00000070,  4,   signed=False)
            self.HEND      =  self._HEND(    self,  Access.RW,  0x00000780,  7,   signed=False)
            self.FD3       =  self._FD3(     self,  Access.RW,  0x00000800,  11,  signed=False)
            self.DISFDCC   =  self._DISFDCC( self,  Access.RW,  0x00001000,  12,  signed=False)
            self.CHM       =  self._CHM(     self,  Access.RW,  0x00004000,  14,  signed=False)
            self.TBL       =  self._TBL(     self,  Access.RW,  0x00018000,  15,  signed=False)
            self.VHIGHFS   =  self._VHIGHFS( self,  Access.RW,  0x00040000,  18,  signed=False)
            self.VHIGHCHM  =  self._VHIGHCHM(self,  Access.RW,  0x00080000,  19,  signed=False)
            self.TPFD      =  self._TPFD(    self,  Access.RW,  0x00F00000,  20,  signed=False)
            self.MRES      =  self._MRES(    self,  Access.RW,  0x0F000000,  24,  signed=False)
            self.INTPOL    =  self._INTPOL(  self,  Access.RW,  0x10000000,  28,  signed=False)
            self.DEDGE     =  self._DEDGE(   self,  Access.RW,  0x20000000,  29,  signed=False)

        class _TOFF(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DRIVER_OFF  =  Option(0,   parent,  "DRIVER_OFF")
                    self.TOFF_56     =  Option(1,   parent,  "TOFF_56")
                    self.TOFF_88     =  Option(2,   parent,  "TOFF_88")
                    self.TOFF_120    =  Option(3,   parent,  "TOFF_120")
                    self.TOFF_152    =  Option(4,   parent,  "TOFF_152")
                    self.TOFF_184    =  Option(5,   parent,  "TOFF_184")
                    self.TOFF_216    =  Option(6,   parent,  "TOFF_216")
                    self.TOFF_248    =  Option(7,   parent,  "TOFF_248")
                    self.TOFF_280    =  Option(8,   parent,  "TOFF_280")
                    self.TOFF_312    =  Option(9,   parent,  "TOFF_312")
                    self.TOFF_344    =  Option(10,  parent,  "TOFF_344")
                    self.TOFF_376    =  Option(11,  parent,  "TOFF_376")
                    self.TOFF_408    =  Option(12,  parent,  "TOFF_408")
                    self.TOFF_440    =  Option(13,  parent,  "TOFF_440")
                    self.TOFF_472    =  Option(14,  parent,  "TOFF_472")
                    self.TOFF_504    =  Option(15,  parent,  "TOFF_504")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TOFF", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _HSTRT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HSTRT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HEND(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HEND", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _FD3(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.TFD3_0  =  Option(False,  parent,  "TFD3_0")
                    self.TFD3_1  =  Option(True,   parent,  "TFD3_1")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FD3", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DISFDCC(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DISFDCC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CHM(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.spread_cycle  =  Option(False,  parent,  "spread_cycle")
                    self.classic_chop  =  Option(True,   parent,  "classic_chop")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHM", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _TBL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.TBL_20  =  Option(0,  parent,  "TBL_20")
                    self.TBL_28  =  Option(1,  parent,  "TBL_28")
                    self.TBL_36  =  Option(2,  parent,  "TBL_36")
                    self.TBL_54  =  Option(3,  parent,  "TBL_54")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TBL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VHIGHFS(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FS_THIGH_DIS  =  Option(False,  parent,  "FS_THIGH_DIS")
                    self.FS_THIGH_EN   =  Option(True,   parent,  "FS_THIGH_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VHIGHFS", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VHIGHCHM(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CTOFF_THIGH_DIS  =  Option(False,  parent,  "CTOFF_THIGH_DIS")
                    self.CTOFF_THIGH_EN   =  Option(True,   parent,  "CTOFF_THIGH_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VHIGHCHM", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _TPFD(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.TPFD_OFF   =  Option(0,   parent,  "TPFD_OFF")
                    self.TPFD_128   =  Option(1,   parent,  "TPFD_128")
                    self.TPFD_256   =  Option(2,   parent,  "TPFD_256")
                    self.TPFD_384   =  Option(3,   parent,  "TPFD_384")
                    self.TPFD_512   =  Option(4,   parent,  "TPFD_512")
                    self.TPFD_640   =  Option(5,   parent,  "TPFD_640")
                    self.TPFD_768   =  Option(6,   parent,  "TPFD_768")
                    self.TPFD_896   =  Option(7,   parent,  "TPFD_896")
                    self.TPFD_1024  =  Option(8,   parent,  "TPFD_1024")
                    self.TPFD_1152  =  Option(9,   parent,  "TPFD_1152")
                    self.TPFD_1280  =  Option(10,  parent,  "TPFD_1280")
                    self.TPFD_1408  =  Option(11,  parent,  "TPFD_1408")
                    self.TPFD_1536  =  Option(12,  parent,  "TPFD_1536")
                    self.TPFD_1664  =  Option(13,  parent,  "TPFD_1664")
                    self.TPFD_1792  =  Option(14,  parent,  "TPFD_1792")
                    self.TPFD_1920  =  Option(15,  parent,  "TPFD_1920")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPFD", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

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
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DEDGE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _MDR_COOLCONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_COOLCONF", parent, access, address, signed)
            self.SEMIN   =  self._SEMIN( self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.SEUP    =  self._SEUP(  self,  Access.RW,  0x00000060,  5,   signed=False)
            self.SEMAX   =  self._SEMAX( self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.SEDN    =  self._SEDN(  self,  Access.RW,  0x00006000,  13,  signed=False)
            self.SEIMIN  =  self._SEIMIN(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.SGT     =  self._SGT(   self,  Access.RW,  0x007F0000,  16,  signed=True)
            self.SFILT   =  self._SFILT( self,  Access.RW,  0x01000000,  24,  signed=False)

        class _SEMIN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEMIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEUP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.STEP_UP_1  =  Option(0,  parent,  "STEP_UP_1")
                    self.STEP_UP_2  =  Option(1,  parent,  "STEP_UP_2")
                    self.STEP_UP_4  =  Option(2,  parent,  "STEP_UP_4")
                    self.STEP_UP_8  =  Option(3,  parent,  "STEP_UP_8")

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
                    self.STEP_DOWN_EACH_32  =  Option(0,  parent,  "STEP_DOWN_EACH_32")
                    self.STEP_DOWN_EACH_8   =  Option(1,  parent,  "STEP_DOWN_EACH_8")
                    self.STEP_DOWN_EACH_2   =  Option(2,  parent,  "STEP_DOWN_EACH_2")
                    self.STEP_DOWN_EACH_1   =  Option(3,  parent,  "STEP_DOWN_EACH_1")

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

        class _SFILT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FILT_DISABLED  =  Option(False,  parent,  "FILT_DISABLED")
                    self.FILT_ENABLED   =  Option(True,   parent,  "FILT_ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SFILT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _MDR_DCCTRL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_DCCTRL", parent, access, address, signed)
            self.DC_TIME  =  self._DC_TIME(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.DC_SG    =  self._DC_SG(  self,  Access.RW,  0x00FF0000,  16,  signed=False)

        class _DC_TIME(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DC_TIME", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DC_SG(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DC_SG", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MDR_DRV_STATUS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_DRV_STATUS", parent, access, address, signed)
            self.SG_RESULT           =  self._SG_RESULT(         self,  Access.R,  0x000003FF,  0,   signed=False)
            self.S2VSA               =  self._S2VSA(             self,  Access.R,  0x00001000,  12,  signed=False)
            self.S2VSB               =  self._S2VSB(             self,  Access.R,  0x00002000,  13,  signed=False)
            self.STEALTH             =  self._STEALTH(           self,  Access.R,  0x00004000,  14,  signed=False)
            self.FSACTIVE            =  self._FSACTIVE(          self,  Access.R,  0x00008000,  15,  signed=False)
            self.CS_ACTUAL           =  self._CS_ACTUAL(         self,  Access.R,  0x001F0000,  16,  signed=False)
            self.RES_DET             =  self._RES_DET(           self,  Access.R,  0x00400000,  22,  signed=False)
            self.STALLGUARD_PREWARN  =  self._STALLGUARD_PREWARN(self,  Access.R,  0x00800000,  23,  signed=False)
            self.STALLGUARD          =  self._STALLGUARD(        self,  Access.R,  0x01000000,  24,  signed=False)
            self.OT                  =  self._OT(                self,  Access.R,  0x02000000,  25,  signed=False)
            self.OTPW                =  self._OTPW(              self,  Access.R,  0x04000000,  26,  signed=False)
            self.S2GA                =  self._S2GA(              self,  Access.R,  0x08000000,  27,  signed=False)
            self.S2GB                =  self._S2GB(              self,  Access.R,  0x10000000,  28,  signed=False)
            self.OLA                 =  self._OLA(               self,  Access.R,  0x20000000,  29,  signed=False)
            self.OLB                 =  self._OLB(               self,  Access.R,  0x40000000,  30,  signed=False)
            self.STST                =  self._STST(              self,  Access.R,  0x80000000,  31,  signed=False)

        class _SG_RESULT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_RESULT", parent, access, mask, shift, signed=signed)

                self.choice = None

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
                    self.SPREADCYCLE_CTOFF  =  Option(False,  parent,  "SPREADCYCLE_CTOFF")
                    self.STEALTHCHOP        =  Option(True,   parent,  "STEALTHCHOP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STEALTH", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _FSACTIVE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.USTEP  =  Option(False,  parent,  "USTEP")
                    self.FSTEP  =  Option(True,   parent,  "FSTEP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FSACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CS_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RES_DET(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_RES_DET  =  Option(False,  parent,  "NO_RES_DET")
                    self.RES_DET     =  Option(True,   parent,  "RES_DET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RES_DET", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STALLGUARD_PREWARN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALLGUARD_PREWARN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STALLGUARD(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

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
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.ERROR        =  Option(True,   parent,  "ERROR")

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

    class _MDR_PWMCONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_PWMCONF", parent, access, address, signed)
            self.PWM_OFS             =  self._PWM_OFS(           self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.PWM_GRAD            =  self._PWM_GRAD(          self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.PWM_FREQ            =  self._PWM_FREQ(          self,  Access.RW,  0x00030000,  16,  signed=False)
            self.PWM_AUTOSCALE       =  self._PWM_AUTOSCALE(     self,  Access.RW,  0x00040000,  18,  signed=False)
            self.PWM_AUTOGRAD        =  self._PWM_AUTOGRAD(      self,  Access.RW,  0x00080000,  19,  signed=False)
            self.FREEWHEEL           =  self._FREEWHEEL(         self,  Access.RW,  0x00300000,  20,  signed=False)
            self.PWM_MEAS_SD_ENABLE  =  self._PWM_MEAS_SD_ENABLE(self,  Access.RW,  0x00400000,  22,  signed=False)
            self.PWM_DIS_REG_STST    =  self._PWM_DIS_REG_STST(  self,  Access.RW,  0x00800000,  23,  signed=False)
            self.PWM_REG             =  self._PWM_REG(           self,  Access.RW,  0x0F000000,  24,  signed=False)
            self.PWM_LIM             =  self._PWM_LIM(           self,  Access.RW,  0xF0000000,  28,  signed=False)

        class _PWM_OFS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_OFS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_GRAD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_GRAD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_FREQ(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FCLK_2DIV1024  =  Option(0,  parent,  "FCLK_2DIV1024")
                    self.FCLK_2DIV683   =  Option(1,  parent,  "FCLK_2DIV683")
                    self.FCLK_2DIV512   =  Option(2,  parent,  "FCLK_2DIV512")
                    self.FCLK_2DIV410   =  Option(3,  parent,  "FCLK_2DIV410")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_FREQ", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PWM_AUTOSCALE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.USER  =  Option(False,  parent,  "USER")
                    self.AUTO  =  Option(True,   parent,  "AUTO")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_AUTOSCALE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PWM_AUTOGRAD(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FIXED  =  Option(False,  parent,  "FIXED")
                    self.AUTO   =  Option(True,   parent,  "AUTO")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_AUTOGRAD", parent, access, mask, shift, signed=signed)

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

        class _PWM_MEAS_SD_ENABLE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_MEAS_SD_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PWM_DIS_REG_STST(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ACTIVE    =  Option(False,  parent,  "ACTIVE")
                    self.INACTIVE  =  Option(True,   parent,  "INACTIVE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_DIS_REG_STST", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PWM_REG(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RESERVED  =  Option(0,   parent,  "RESERVED")
                    self.INC_05    =  Option(1,   parent,  "INC_05")
                    self.INC_10    =  Option(2,   parent,  "INC_10")
                    self.INC_15    =  Option(3,   parent,  "INC_15")
                    self.INC_20    =  Option(4,   parent,  "INC_20")
                    self.INC_25    =  Option(5,   parent,  "INC_25")
                    self.INC_30    =  Option(6,   parent,  "INC_30")
                    self.INC_35    =  Option(7,   parent,  "INC_35")
                    self.INC_40    =  Option(8,   parent,  "INC_40")
                    self.INC_45    =  Option(9,   parent,  "INC_45")
                    self.INC_50    =  Option(10,  parent,  "INC_50")
                    self.INC_55    =  Option(11,  parent,  "INC_55")
                    self.INC_60    =  Option(12,  parent,  "INC_60")
                    self.INC_65    =  Option(13,  parent,  "INC_65")
                    self.INC_70    =  Option(14,  parent,  "INC_70")
                    self.INC_75    =  Option(15,  parent,  "INC_75")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_REG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PWM_LIM(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_LIM", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MDR_PWM_SCALE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_PWM_SCALE", parent, access, address, signed)
            self.PWM_SCALE_SUM   =  self._PWM_SCALE_SUM( self,  Access.R,  0x000003FF,  0,   signed=False)
            self.PWM_SCALE_AUTO  =  self._PWM_SCALE_AUTO(self,  Access.R,  0x01FF0000,  16,  signed=False)

        class _PWM_SCALE_SUM(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_SCALE_SUM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_SCALE_AUTO(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_SCALE_AUTO", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MDR_PWM_AUTO(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_PWM_AUTO", parent, access, address, signed)
            self.PWM_OFS_AUTO   =  self._PWM_OFS_AUTO( self,  Access.R,  0x000000FF,  0,   signed=False)
            self.PWM_GRAD_AUTO  =  self._PWM_GRAD_AUTO(self,  Access.R,  0x00FF0000,  16,  signed=False)

        class _PWM_OFS_AUTO(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_OFS_AUTO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_GRAD_AUTO(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_GRAD_AUTO", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MDR_SG4_THRS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_SG4_THRS", parent, access, address, signed)
            self.SG4_THRS     =  self._SG4_THRS(   self,  Access.RW,  0x000001FF,  0,  signed=False)
            self.SG4_FILT_EN  =  self._SG4_FILT_EN(self,  Access.RW,  0x00000200,  9,  signed=False)

        class _SG4_THRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG4_THRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SG4_FILT_EN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FILT_DISABLE  =  Option(False,  parent,  "FILT_DISABLE")
                    self.FILT_ENABLE   =  Option(True,   parent,  "FILT_ENABLE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG4_FILT_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _MDR_SG4_RESULT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_SG4_RESULT", parent, access, address, signed)
            self.SG4_RESULT  =  self._SG4_RESULT(self,  Access.R,  0x000003FF,  0,  signed=False)

        class _SG4_RESULT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG4_RESULT", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MDR_SG4_IND(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_SG4_IND", parent, access, address, signed)
            self.SG4_IND_0  =  self._SG4_IND_0(self,  Access.R,  0x000000FF,  0,   signed=False)
            self.SG4_IND_1  =  self._SG4_IND_1(self,  Access.R,  0x0000FF00,  8,   signed=False)
            self.SG4_IND_2  =  self._SG4_IND_2(self,  Access.R,  0x00FF0000,  16,  signed=False)
            self.SG4_IND_3  =  self._SG4_IND_3(self,  Access.R,  0xFF000000,  24,  signed=False)

        class _SG4_IND_0(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG4_IND_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SG4_IND_1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG4_IND_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SG4_IND_2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG4_IND_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SG4_IND_3(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG4_IND_3", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _MDR_SG_PREWARN_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MDR_SG_PREWARN_CONF", parent, access, address, signed)
            self.SG_PREWARN_RESULT        =  self._SG_PREWARN_RESULT(      self,  Access.R,   0x000003FF,  0,   signed=False)
            self.SG_PREWARN_RESULT_VALID  =  self._SG_PREWARN_RESULT_VALID(self,  Access.R,   0x00001000,  12,  signed=False)
            self.SG_PREWARN_THRSH         =  self._SG_PREWARN_THRSH(       self,  Access.RW,  0x01FF0000,  16,  signed=False)
            self.SG_PREWARN_FILTER        =  self._SG_PREWARN_FILTER(      self,  Access.RW,  0x70000000,  28,  signed=False)

        class _SG_PREWARN_RESULT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_PREWARN_RESULT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SG_PREWARN_RESULT_VALID(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INVALID  =  Option(False,  parent,  "INVALID")
                    self.VALID    =  Option(True,   parent,  "VALID")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_PREWARN_RESULT_VALID", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SG_PREWARN_THRSH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_PREWARN_THRSH", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SG_PREWARN_FILTER(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(0,  parent,  "DISABLED")
                    self.FILT_2    =  Option(1,  parent,  "FILT_2")
                    self.FILT_4    =  Option(2,  parent,  "FILT_4")
                    self.FILT_8    =  Option(3,  parent,  "FILT_8")
                    self.FILT_16   =  Option(4,  parent,  "FILT_16")
                    self.FILT_32   =  Option(5,  parent,  "FILT_32")
                    self.FILT_64   =  Option(6,  parent,  "FILT_64")
                    self.NOT_USED  =  Option(7,  parent,  "NOT_USED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_PREWARN_FILTER", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _ADC_ADC_SUPPLY_TEMP(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_ADC_SUPPLY_TEMP", parent, access, address, signed)
            self.TEMPERATURE  =  self._TEMPERATURE(self,  Access.R,   0x000001FF,  0,   signed=False)
            self.ADC_EN       =  self._ADC_EN(     self,  Access.RW,  0x00001000,  12,  signed=False)
            self.SUPPLY       =  self._SUPPLY(     self,  Access.R,   0x01FF0000,  16,  signed=False)

        class _TEMPERATURE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMPERATURE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_EN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC_DISABLED  =  Option(False,  parent,  "ADC_DISABLED")
                    self.ADC_ENABLED   =  Option(True,   parent,  "ADC_ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SUPPLY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SUPPLY", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _LIMITS_VMAX_LIMIT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("LIMITS_VMAX_LIMIT", parent, access, address, signed)
            self.VMAX_LIMIT  =  self._VMAX_LIMIT(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _VMAX_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VMAX_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _LIMITS_LIMIT_VALUES(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("LIMITS_LIMIT_VALUES", parent, access, address, signed)
            self.GLOBAL_SCALER_LIMIT  =  self._GLOBAL_SCALER_LIMIT(self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.RREF_LIMIT           =  self._RREF_LIMIT(         self,  Access.RW,  0x00000300,  8,   signed=False)
            self.GAIN_SCALER_LIMIT    =  self._GAIN_SCALER_LIMIT(  self,  Access.RW,  0x00000C00,  10,  signed=False)
            self.IRUN_LIMIT           =  self._IRUN_LIMIT(         self,  Access.RW,  0x001F0000,  16,  signed=False)
            self.IHOLD_LIMIT          =  self._IHOLD_LIMIT(        self,  Access.RW,  0x1F000000,  24,  signed=False)

        class _GLOBAL_SCALER_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GLOBAL_SCALER_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RREF_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RREF_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GAIN_SCALER_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GAIN_SCALER_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IRUN_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IRUN_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IHOLD_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IHOLD_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _USER_DATA_USER_DATA_0(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("USER_DATA_USER_DATA_0", parent, access, address, signed)
            self.USER_DATA_0  =  self._USER_DATA_0(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _USER_DATA_0(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USER_DATA_0", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _USER_DATA_USER_DATA_1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("USER_DATA_USER_DATA_1", parent, access, address, signed)
            self.USER_DATA_1  =  self._USER_DATA_1(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _USER_DATA_1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USER_DATA_1", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _USER_DATA_USER_DATA_2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("USER_DATA_USER_DATA_2", parent, access, address, signed)
            self.USER_DATA_2  =  self._USER_DATA_2(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _USER_DATA_2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USER_DATA_2", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _USER_DATA_USER_DATA_3(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("USER_DATA_USER_DATA_3", parent, access, address, signed)
            self.USER_DATA_3  =  self._USER_DATA_3(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _USER_DATA_3(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USER_DATA_3", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _USER_DATA_USER_DATA_4(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("USER_DATA_USER_DATA_4", parent, access, address, signed)
            self.USER_DATA_4  =  self._USER_DATA_4(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _USER_DATA_4(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USER_DATA_4", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _USER_DATA_USER_DATA_5(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("USER_DATA_USER_DATA_5", parent, access, address, signed)
            self.USER_DATA_5  =  self._USER_DATA_5(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _USER_DATA_5(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USER_DATA_5", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _USER_DATA_USER_DATA_6(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("USER_DATA_USER_DATA_6", parent, access, address, signed)
            self.USER_DATA_6  =  self._USER_DATA_6(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _USER_DATA_6(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USER_DATA_6", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _USER_DATA_USER_DATA_7(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("USER_DATA_USER_DATA_7", parent, access, address, signed)
            self.USER_DATA_7  =  self._USER_DATA_7(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _USER_DATA_7(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USER_DATA_7", parent, access, mask, shift, signed=signed)

                self.choice = None

    class _OTP_MODE_OTP_MODE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("OTP_MODE_OTP_MODE", parent, access, address, signed)
            self.OTP_MODE_PASSWORD  =  self._OTP_MODE_PASSWORD(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _OTP_MODE_PASSWORD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OTP_MODE_PASSWORD", parent, access, mask, shift, signed=signed)

                self.choice = None
