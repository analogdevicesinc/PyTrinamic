################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Choice, Option, Field, Register


class TMC5241Map:

    def __init__(self, *, channel=None, block=None, width=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(channel, block, width)


class _ALL_REGISTERS(RegisterGroup):

    class _GCONF(Register):

        class _FAST_STANDSTILL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.STST_2_20  =  Option(False,  parent,  "STST_2_20")
                    self.STST_2_18  =  Option(True,   parent,  "STST_2_18")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FAST_STANDSTILL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

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

        class _DIAG0_NINT_STEP(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INTERRUPT  =  Option(False,  parent,  "INTERRUPT")
                    self.STEP       =  Option(True,   parent,  "STEP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_NINT_STEP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_NPOSCOMP_DIR(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.XCOMP  =  Option(False,  parent,  "XCOMP")
                    self.DIR    =  Option(True,   parent,  "DIR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_NPOSCOMP_DIR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_INT_PUSHPULL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPEN_DRAIN  =  Option(False,  parent,  "OPEN_DRAIN")
                    self.PUSH_PULL   =  Option(True,   parent,  "PUSH_PULL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_INT_PUSHPULL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_POSCOMP_PUSHPULL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPEN_DRAIN  =  Option(False,  parent,  "OPEN_DRAIN")
                    self.PUSH_PULL   =  Option(True,   parent,  "PUSH_PULL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_POSCOMP_PUSHPULL", parent, access, mask, shift, signed=signed)

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

        class _DIRECT_MODE(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NORMAL_MODE  =  Option(False,  parent,  "NORMAL_MODE")
                    self.DIRECT_MODE  =  Option(True,   parent,  "DIRECT_MODE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIRECT_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LENGTH_STEP_PULSE(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HALF    =  Option(0,   parent,  "HALF")
                    self.CLK_1   =  Option(1,   parent,  "CLK_1")
                    self.CLK_2   =  Option(2,   parent,  "CLK_2")
                    self.CLK_3   =  Option(3,   parent,  "CLK_3")
                    self.CLK_4   =  Option(4,   parent,  "CLK_4")
                    self.CLK_5   =  Option(5,   parent,  "CLK_5")
                    self.CLK_6   =  Option(6,   parent,  "CLK_6")
                    self.CLK_7   =  Option(7,   parent,  "CLK_7")
                    self.CLK_8   =  Option(8,   parent,  "CLK_8")
                    self.CLK_9   =  Option(9,   parent,  "CLK_9")
                    self.CLK_10  =  Option(10,  parent,  "CLK_10")
                    self.CLK_11  =  Option(11,  parent,  "CLK_11")
                    self.CLK_12  =  Option(12,  parent,  "CLK_12")
                    self.CLK_13  =  Option(13,  parent,  "CLK_13")
                    self.CLK_14  =  Option(14,  parent,  "CLK_14")
                    self.CLK_15  =  Option(15,  parent,  "CLK_15")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LENGTH_STEP_PULSE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("GCONF", parent, access, address, signed)
            self.FAST_STANDSTILL         =  self._FAST_STANDSTILL(       self,  Access.RW,  0x00000002,  1,   signed=False)
            self.EN_PWM_MODE             =  self._EN_PWM_MODE(           self,  Access.RW,  0x00000004,  2,   signed=False)
            self.MULTISTEP_FILT          =  self._MULTISTEP_FILT(        self,  Access.RW,  0x00000008,  3,   signed=False)
            self.SHAFT                   =  self._SHAFT(                 self,  Access.RW,  0x00000010,  4,   signed=False)
            self.DIAG0_NINT_STEP         =  self._DIAG0_NINT_STEP(       self,  Access.RW,  0x00000080,  7,   signed=False)
            self.DIAG1_NPOSCOMP_DIR      =  self._DIAG1_NPOSCOMP_DIR(    self,  Access.RW,  0x00000100,  8,   signed=False)
            self.DIAG0_INT_PUSHPULL      =  self._DIAG0_INT_PUSHPULL(    self,  Access.RW,  0x00001000,  12,  signed=False)
            self.DIAG1_POSCOMP_PUSHPULL  =  self._DIAG1_POSCOMP_PUSHPULL(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.SMALL_HYSTERESIS        =  self._SMALL_HYSTERESIS(      self,  Access.RW,  0x00004000,  14,  signed=False)
            self.STOP_ENABLE             =  self._STOP_ENABLE(           self,  Access.RW,  0x00008000,  15,  signed=False)
            self.DIRECT_MODE             =  self._DIRECT_MODE(           self,  Access.RW,  0x00010000,  16,  signed=False)
            self.LENGTH_STEP_PULSE       =  self._LENGTH_STEP_PULSE(     self,  Access.RW,  0x001E0000,  17,  signed=False)

    class _GSTAT(Register):

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

        class _UV_CP(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OPERATIONAL  =  Option(False,  parent,  "OPERATIONAL")
                    self.UV_CP_DET    =  Option(True,   parent,  "UV_CP_DET")

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

        def __init__(self, parent, access, address, signed):
            super().__init__("GSTAT", parent, access, address, signed)
            self.RESET           =  self._RESET(         self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.DRV_ERR         =  self._DRV_ERR(       self,  Access.RWC,  0x00000002,  1,  signed=False)
            self.UV_CP           =  self._UV_CP(         self,  Access.RWC,  0x00000004,  2,  signed=False)
            self.REGISTER_RESET  =  self._REGISTER_RESET(self,  Access.RWC,  0x00000008,  3,  signed=False)
            self.VM_UVLO         =  self._VM_UVLO(       self,  Access.RWC,  0x00000010,  4,  signed=False)

    class _IFCNT(Register):

        class _IFCNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IFCNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("IFCNT", parent, access, address, signed)
            self.IFCNT  =  self._IFCNT(self,  Access.R,  0x000000FF,  0,  signed=False)

    class _NODECONF(Register):

        class _NODEADDR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NODEADDR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SENDDELAY(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.BIT_T_8    =  Option(0,   parent,  "BIT_T_8")
                    self.BIT_T_24   =  Option(2,   parent,  "BIT_T_24")
                    self.BIT_T_40   =  Option(4,   parent,  "BIT_T_40")
                    self.BIT_T_56   =  Option(6,   parent,  "BIT_T_56")
                    self.BIT_T_72   =  Option(8,   parent,  "BIT_T_72")
                    self.BIT_T_88   =  Option(10,  parent,  "BIT_T_88")
                    self.BIT_T_104  =  Option(12,  parent,  "BIT_T_104")
                    self.BIT_T_120  =  Option(14,  parent,  "BIT_T_120")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SENDDELAY", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("NODECONF", parent, access, address, signed)
            self.NODEADDR   =  self._NODEADDR( self,  Access.RW,  0x000000FF,  0,  signed=False)
            self.SENDDELAY  =  self._SENDDELAY(self,  Access.RW,  0x00000F00,  8,  signed=False)

    class _IOIN(Register):

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

        class _UART_EN(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOW   =  Option(False,  parent,  "LOW")
                    self.HIGH  =  Option(True,   parent,  "HIGH")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UART_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OUTPUT(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NAO_LOW  =  Option(False,  parent,  "NAO_LOW")
                    self.NAO_HI   =  Option(True,   parent,  "NAO_HI")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUTPUT", parent, access, mask, shift, signed=signed)

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

        def __init__(self, parent, access, address, signed):
            super().__init__("IOIN", parent, access, address, signed)
            self.REFL         =  self._REFL(       self,  Access.R,   0x00000001,  0,   signed=False)
            self.REFR         =  self._REFR(       self,  Access.R,   0x00000002,  1,   signed=False)
            self.ENCB         =  self._ENCB(       self,  Access.R,   0x00000004,  2,   signed=False)
            self.ENCA         =  self._ENCA(       self,  Access.R,   0x00000008,  3,   signed=False)
            self.DRV_ENN      =  self._DRV_ENN(    self,  Access.R,   0x00000010,  4,   signed=False)
            self.ENCN         =  self._ENCN(       self,  Access.R,   0x00000020,  5,   signed=False)
            self.UART_EN      =  self._UART_EN(    self,  Access.R,   0x00000040,  6,   signed=False)
            self.OUTPUT       =  self._OUTPUT(     self,  Access.RW,  0x00001000,  12,  signed=False)
            self.EXT_RES_DET  =  self._EXT_RES_DET(self,  Access.R,   0x00002000,  13,  signed=False)
            self.EXT_CLK      =  self._EXT_CLK(    self,  Access.R,   0x00004000,  14,  signed=False)
            self.SILICON_RV   =  self._SILICON_RV( self,  Access.R,   0x00070000,  16,  signed=False)

    class _X_COMPARE(Register):

        class _X_COMPARE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_COMPARE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("X_COMPARE", parent, access, address, signed)
            self.X_COMPARE  =  self._X_COMPARE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _X_COMPARE_REPEAT(Register):

        class _X_COMPARE_REPEAT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_COMPARE_REPEAT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("X_COMPARE_REPEAT", parent, access, address, signed)
            self.X_COMPARE_REPEAT  =  self._X_COMPARE_REPEAT(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

    class _DIAG_GCONF(Register):

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

        class _DIAG0_EV_N_DEVIATION(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_EV_N_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG0_OVERVOLTAGE(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG0_OVERVOLTAGE", parent, access, mask, shift, signed=signed)

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

        class _DIAG1_EV_N_DEVIATION(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_EV_N_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DIAG1_OVERVOLTAGE(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.ENABLED   =  Option(True,   parent,  "ENABLED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG1_OVERVOLTAGE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("DIAG_GCONF", parent, access, address, signed)
            self.DIAG0_ERROR           =  self._DIAG0_ERROR(         self,  Access.RW,  0x00000001,  0,   signed=False)
            self.DIAG0_OTPW            =  self._DIAG0_OTPW(          self,  Access.RW,  0x00000002,  1,   signed=False)
            self.DIAG0_STALL           =  self._DIAG0_STALL(         self,  Access.RW,  0x00000004,  2,   signed=False)
            self.DIAG0_INDEX           =  self._DIAG0_INDEX(         self,  Access.RW,  0x00000008,  3,   signed=False)
            self.DIAG0_STEP            =  self._DIAG0_STEP(          self,  Access.RW,  0x00000010,  4,   signed=False)
            self.DIAG0_DIR             =  self._DIAG0_DIR(           self,  Access.RW,  0x00000020,  5,   signed=False)
            self.DIAG0_XCOMP           =  self._DIAG0_XCOMP(         self,  Access.RW,  0x00000040,  6,   signed=False)
            self.DIAG0_EV_STOP_REF     =  self._DIAG0_EV_STOP_REF(   self,  Access.RW,  0x00000080,  7,   signed=False)
            self.DIAG0_EV_STOP_SG      =  self._DIAG0_EV_STOP_SG(    self,  Access.RW,  0x00000100,  8,   signed=False)
            self.DIAG0_EV_POS_REACHED  =  self._DIAG0_EV_POS_REACHED(self,  Access.RW,  0x00000200,  9,   signed=False)
            self.DIAG0_EV_N_DEVIATION  =  self._DIAG0_EV_N_DEVIATION(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.DIAG0_OVERVOLTAGE     =  self._DIAG0_OVERVOLTAGE(   self,  Access.RW,  0x00000800,  11,  signed=False)
            self.DIAG1_ERROR           =  self._DIAG1_ERROR(         self,  Access.RW,  0x00010000,  16,  signed=False)
            self.DIAG1_OTPW            =  self._DIAG1_OTPW(          self,  Access.RW,  0x00020000,  17,  signed=False)
            self.DIAG1_STALL           =  self._DIAG1_STALL(         self,  Access.RW,  0x00040000,  18,  signed=False)
            self.DIAG1_INDEX           =  self._DIAG1_INDEX(         self,  Access.RW,  0x00080000,  19,  signed=False)
            self.DIAG1_STEP            =  self._DIAG1_STEP(          self,  Access.RW,  0x00100000,  20,  signed=False)
            self.DIAG1_DIR             =  self._DIAG1_DIR(           self,  Access.RW,  0x00200000,  21,  signed=False)
            self.DIAG1_XCOMP           =  self._DIAG1_XCOMP(         self,  Access.RW,  0x00400000,  22,  signed=False)
            self.DIAG1_EV_STOP_REF     =  self._DIAG1_EV_STOP_REF(   self,  Access.RW,  0x00800000,  23,  signed=False)
            self.DIAG1_EV_STOP_SG      =  self._DIAG1_EV_STOP_SG(    self,  Access.RW,  0x01000000,  24,  signed=False)
            self.DIAG1_EV_POS_REACHED  =  self._DIAG1_EV_POS_REACHED(self,  Access.RW,  0x02000000,  25,  signed=False)
            self.DIAG1_EV_N_DEVIATION  =  self._DIAG1_EV_N_DEVIATION(self,  Access.RW,  0x04000000,  26,  signed=False)
            self.DIAG1_OVERVOLTAGE     =  self._DIAG1_OVERVOLTAGE(   self,  Access.RW,  0x08000000,  27,  signed=False)

    class _DRV_CONF(Register):

        class _CURRENT_RANGE(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CR_1A  =  Option(0,  parent,  "CR_1A")
                    self.CR_2A  =  Option(1,  parent,  "CR_2A")
                    self.CR_3A  =  Option(2,  parent,  "CR_3A")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_RANGE", parent, access, mask, shift, signed=signed)

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

        def __init__(self, parent, access, address, signed):
            super().__init__("DRV_CONF", parent, access, address, signed)
            self.CURRENT_RANGE  =  self._CURRENT_RANGE(self,  Access.RW,  0x00000003,  0,  signed=False)
            self.SLOPE_CONTROL  =  self._SLOPE_CONTROL(self,  Access.RW,  0x00000030,  4,  signed=False)

    class _GLOBAL_SCALER(Register):

        class _GLOBAL_SCALER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GLOBAL_SCALER", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("GLOBAL_SCALER", parent, access, address, signed)
            self.GLOBAL_SCALER  =  self._GLOBAL_SCALER(self,  Access.RW,  0x000000FF,  0,  signed=False)

    class _IHOLD_IRUN(Register):

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

        def __init__(self, parent, access, address, signed):
            super().__init__("IHOLD_IRUN", parent, access, address, signed)
            self.IHOLD       =  self._IHOLD(     self,  Access.RW,  0x0000001F,  0,   signed=False)
            self.IRUN        =  self._IRUN(      self,  Access.RW,  0x00001F00,  8,   signed=False)
            self.IHOLDDELAY  =  self._IHOLDDELAY(self,  Access.RW,  0x000F0000,  16,  signed=False)
            self.IRUNDELAY   =  self._IRUNDELAY( self,  Access.RW,  0x0F000000,  24,  signed=False)

    class _TPOWERDOWN(Register):

        class _TPOWERDOWN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPOWERDOWN", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TPOWERDOWN", parent, access, address, signed)
            self.TPOWERDOWN  =  self._TPOWERDOWN(self,  Access.RW,  0x000000FF,  0,  signed=False)

    class _TSTEP(Register):

        class _TSTEP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSTEP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TSTEP", parent, access, address, signed)
            self.TSTEP  =  self._TSTEP(self,  Access.R,  0x000FFFFF,  0,  signed=False)

    class _TPWMTHRS(Register):

        class _TPWMTHRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TPWMTHRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TPWMTHRS", parent, access, address, signed)
            self.TPWMTHRS  =  self._TPWMTHRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _TCOOLTHRS(Register):

        class _TCOOLTHRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TCOOLTHRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TCOOLTHRS", parent, access, address, signed)
            self.TCOOLTHRS  =  self._TCOOLTHRS(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _THIGH(Register):

        class _THIGH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("THIGH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("THIGH", parent, access, address, signed)
            self.THIGH  =  self._THIGH(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _RAMPMODE(Register):

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

        def __init__(self, parent, access, address, signed):
            super().__init__("RAMPMODE", parent, access, address, signed)
            self.RAMPMODE  =  self._RAMPMODE(self,  Access.RW,  0x00000003,  0,  signed=False)

    class _XACTUAL(Register):

        class _XACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("XACTUAL", parent, access, address, signed)
            self.XACTUAL  =  self._XACTUAL(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _VACTUAL(Register):

        class _VACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VACTUAL", parent, access, address, signed)
            self.VACTUAL  =  self._VACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

    class _VSTART(Register):

        class _VSTART(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSTART", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VSTART", parent, access, address, signed)
            self.VSTART  =  self._VSTART(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _A1(Register):

        class _A1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("A1", parent, access, address, signed)
            self.A1  =  self._A1(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _V1(Register):

        class _V1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("V1", parent, access, address, signed)
            self.V1  =  self._V1(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _AMAX(Register):

        class _AMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AMAX", parent, access, address, signed)
            self.AMAX  =  self._AMAX(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _VMAX(Register):

        class _VMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VMAX", parent, access, address, signed)
            self.VMAX  =  self._VMAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _DMAX(Register):

        class _DMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("DMAX", parent, access, address, signed)
            self.DMAX  =  self._DMAX(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _TVMAX(Register):

        class _TVMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TVMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TVMAX", parent, access, address, signed)
            self.TVMAX  =  self._TVMAX(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _D1(Register):

        class _D1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("D1", parent, access, address, signed)
            self.D1  =  self._D1(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _VSTOP(Register):

        class _VSTOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSTOP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VSTOP", parent, access, address, signed)
            self.VSTOP  =  self._VSTOP(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _TZEROWAIT(Register):

        class _TZEROWAIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TZEROWAIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("TZEROWAIT", parent, access, address, signed)
            self.TZEROWAIT  =  self._TZEROWAIT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _XTARGET(Register):

        class _XTARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XTARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("XTARGET", parent, access, address, signed)
            self.XTARGET  =  self._XTARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _V2(Register):

        class _V2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("V2", parent, access, address, signed)
            self.V2  =  self._V2(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _A2(Register):

        class _A2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("A2", parent, access, address, signed)
            self.A2  =  self._A2(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _D2(Register):

        class _D2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("D2", parent, access, address, signed)
            self.D2  =  self._D2(self,  Access.RW,  0x0003FFFF,  0,  signed=False)

    class _AACTUAL(Register):

        class _AACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("AACTUAL", parent, access, address, signed)
            self.AACTUAL  =  self._AACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

    class _VDCMIN(Register):

        class _UNUSED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UNUSED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDCMIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDCMIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VDCMIN", parent, access, address, signed)
            self.UNUSED  =  self._UNUSED(self,  Access.R,   0x000000FF,  0,  signed=False)
            self.VDCMIN  =  self._VDCMIN(self,  Access.RW,  0x007FFF00,  0,  signed=False)

    class _SW_MODE(Register):

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
                    self.LATCH_RE  =  Option(True,   parent,  "LATCH_RE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LATCH_L_INACTIVE(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.LATCH_FE  =  Option(True,   parent,  "LATCH_FE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LATCH_R_ACTIVE(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.LATCH_RE  =  Option(True,   parent,  "LATCH_RE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_R_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LATCH_R_INACTIVE(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED  =  Option(False,  parent,  "DISABLED")
                    self.LATCH_FE  =  Option(True,   parent,  "LATCH_FE")

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
                    self.SRC_XACTUAL  =  Option(False,  parent,  "SRC_XACTUAL")
                    self.SRC_X_ENC    =  Option(True,   parent,  "SRC_X_ENC")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_ENC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("SW_MODE", parent, access, address, signed)
            self.STOP_L_ENABLE      =  self._STOP_L_ENABLE(    self,  Access.RW,  0x00000001,  0,   signed=False)
            self.STOP_R_ENABLE      =  self._STOP_R_ENABLE(    self,  Access.RW,  0x00000002,  1,   signed=False)
            self.POL_STOP_L         =  self._POL_STOP_L(       self,  Access.RW,  0x00000004,  2,   signed=False)
            self.POL_STOP_R         =  self._POL_STOP_R(       self,  Access.RW,  0x00000008,  3,   signed=False)
            self.SWAP_LR            =  self._SWAP_LR(          self,  Access.RW,  0x00000010,  4,   signed=False)
            self.LATCH_L_ACTIVE     =  self._LATCH_L_ACTIVE(   self,  Access.RW,  0x00000020,  5,   signed=False)
            self.LATCH_L_INACTIVE   =  self._LATCH_L_INACTIVE( self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LATCH_R_ACTIVE     =  self._LATCH_R_ACTIVE(   self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LATCH_R_INACTIVE   =  self._LATCH_R_INACTIVE( self,  Access.RW,  0x00000100,  8,   signed=False)
            self.EN_LATCH_ENCODER   =  self._EN_LATCH_ENCODER( self,  Access.RW,  0x00000200,  9,   signed=False)
            self.SG_STOP            =  self._SG_STOP(          self,  Access.RW,  0x00000400,  10,  signed=False)
            self.EN_SOFTSTOP        =  self._EN_SOFTSTOP(      self,  Access.RW,  0x00000800,  11,  signed=False)
            self.EN_VIRTUAL_STOP_L  =  self._EN_VIRTUAL_STOP_L(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.EN_VIRTUAL_STOP_R  =  self._EN_VIRTUAL_STOP_R(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.VIRTUAL_STOP_ENC   =  self._VIRTUAL_STOP_ENC( self,  Access.RW,  0x00004000,  14,  signed=False)

    class _RAMP_STAT(Register):

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

    class _XLATCH(Register):

        class _XLATCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("XLATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("XLATCH", parent, access, address, signed)
            self.XLATCH  =  self._XLATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _ENCMODE(Register):

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

    class _X_ENC(Register):

        class _X_ENC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("X_ENC", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("X_ENC", parent, access, address, signed)
            self.X_ENC  =  self._X_ENC(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _ENC_CONST(Register):

        class _ENC_CONST(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_CONST", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_CONST", parent, access, address, signed)
            self.ENC_CONST  =  self._ENC_CONST(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _ENC_STATUS(Register):

        class _N_EVENT(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_EVENT        =  Option(False,  parent,  "NO_EVENT")
                    self.EVENT_DETECTED  =  Option(True,   parent,  "EVENT_DETECTED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_EVENT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DEVIATION_WARN(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_DEVIATION  =  Option(False,  parent,  "NO_DEVIATION")
                    self.DEVIATION     =  Option(True,   parent,  "DEVIATION")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DEVIATION_WARN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_STATUS", parent, access, address, signed)
            self.N_EVENT         =  self._N_EVENT(       self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.DEVIATION_WARN  =  self._DEVIATION_WARN(self,  Access.RWC,  0x00000002,  1,  signed=False)

    class _ENC_LATCH(Register):

        class _ENC_LATCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_LATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_LATCH", parent, access, address, signed)
            self.ENC_LATCH  =  self._ENC_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _ENC_DEVIATION(Register):

        class _ENC_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ENC_DEVIATION", parent, access, address, signed)
            self.ENC_DEVIATION  =  self._ENC_DEVIATION(self,  Access.RW,  0x000FFFFF,  0,  signed=False)

    class _VIRTUAL_STOP_L(Register):

        class _VIRTUAL_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VIRTUAL_STOP_L", parent, access, address, signed)
            self.VIRTUAL_STOP_L  =  self._VIRTUAL_STOP_L(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _VIRTUAL_STOP_R(Register):

        class _VIRTUAL_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VIRTUAL_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("VIRTUAL_STOP_R", parent, access, address, signed)
            self.VIRTUAL_STOP_R  =  self._VIRTUAL_STOP_R(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _ADC_VSUPPLY_AIN(Register):

        class _ADC_VSUPPLY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_VSUPPLY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_AIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_AIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_VSUPPLY_AIN", parent, access, address, signed)
            self.ADC_VSUPPLY  =  self._ADC_VSUPPLY(self,  Access.R,  0x00001FFF,  0,   signed=True)
            self.ADC_AIN      =  self._ADC_AIN(    self,  Access.R,  0x1FFF0000,  16,  signed=True)

    class _ADC_TEMP(Register):

        class _ADC_TEMP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_TEMP", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RESERVED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESERVED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_TEMP", parent, access, address, signed)
            self.ADC_TEMP  =  self._ADC_TEMP(self,  Access.R,  0x00001FFF,  0,   signed=True)
            self.RESERVED  =  self._RESERVED(self,  Access.R,  0x1FFF0000,  16,  signed=False)

    class _OTW_OV_VTH(Register):

        class _OVERVOLTAGE_VTH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERVOLTAGE_VTH", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OVERTEMPPREWARNING_VTH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMPPREWARNING_VTH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("OTW_OV_VTH", parent, access, address, signed)
            self.OVERVOLTAGE_VTH         =  self._OVERVOLTAGE_VTH(       self,  Access.RW,  0x00001FFF,  0,   signed=False)
            self.OVERTEMPPREWARNING_VTH  =  self._OVERTEMPPREWARNING_VTH(self,  Access.RW,  0x1FFF0000,  16,  signed=False)

    class _MSLUT_0(Register):

        class _MSLUT_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_0", parent, access, address, signed)
            self.MSLUT_0  =  self._MSLUT_0(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_1(Register):

        class _MSLUT_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_1", parent, access, address, signed)
            self.MSLUT_1  =  self._MSLUT_1(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_2(Register):

        class _MSLUT_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_2", parent, access, address, signed)
            self.MSLUT_2  =  self._MSLUT_2(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_3(Register):

        class _MSLUT_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_3", parent, access, address, signed)
            self.MSLUT_3  =  self._MSLUT_3(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_4(Register):

        class _MSLUT_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_4", parent, access, address, signed)
            self.MSLUT_4  =  self._MSLUT_4(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_5(Register):

        class _MSLUT_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_5", parent, access, address, signed)
            self.MSLUT_5  =  self._MSLUT_5(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_6(Register):

        class _MSLUT_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_6", parent, access, address, signed)
            self.MSLUT_6  =  self._MSLUT_6(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUT_7(Register):

        class _MSLUT_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSLUT_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUT_7", parent, access, address, signed)
            self.MSLUT_7  =  self._MSLUT_7(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _MSLUTSEL(Register):

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

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUTSEL", parent, access, address, signed)
            self.W0  =  self._W0(self,  Access.RW,  0x00000003,  0,   signed=False)
            self.W1  =  self._W1(self,  Access.RW,  0x0000000C,  2,   signed=False)
            self.W2  =  self._W2(self,  Access.RW,  0x00000030,  4,   signed=False)
            self.W3  =  self._W3(self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.X1  =  self._X1(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.X2  =  self._X2(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.X3  =  self._X3(self,  Access.RW,  0xFF000000,  24,  signed=False)

    class _MSLUTSTART(Register):

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

        def __init__(self, parent, access, address, signed):
            super().__init__("MSLUTSTART", parent, access, address, signed)
            self.START_SIN     =  self._START_SIN(   self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.START_SIN90   =  self._START_SIN90( self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.OFFSET_SIN90  =  self._OFFSET_SIN90(self,  Access.RW,  0xFF000000,  24,  signed=True)

    class _MSCNT(Register):

        class _MSCNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MSCNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSCNT", parent, access, address, signed)
            self.MSCNT  =  self._MSCNT(self,  Access.R,  0x000003FF,  0,  signed=False)

    class _MSCURACT(Register):

        class _CUR_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CUR_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CUR_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("MSCURACT", parent, access, address, signed)
            self.CUR_B  =  self._CUR_B(self,  Access.R,  0x000001FF,  0,   signed=True)
            self.CUR_A  =  self._CUR_A(self,  Access.R,  0x01FF0000,  16,  signed=True)

    class _CHOPCONF(Register):

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

        class _HSTRT_TFD210(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HSTRT_TFD210", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HEND_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HEND_OFFSET", parent, access, mask, shift, signed=signed)

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
                    self.FD_COMP_EN   =  Option(False,  parent,  "FD_COMP_EN")
                    self.FD_COMP_DIS  =  Option(True,   parent,  "FD_COMP_DIS")

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
                    self.TBL_16  =  Option(0,  parent,  "TBL_16")
                    self.TBL_24  =  Option(1,  parent,  "TBL_24")
                    self.TBL_36  =  Option(2,  parent,  "TBL_36")
                    self.TBL_48  =  Option(3,  parent,  "TBL_48")

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

        def __init__(self, parent, access, address, signed):
            super().__init__("CHOPCONF", parent, access, address, signed)
            self.TOFF          =  self._TOFF(        self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.HSTRT_TFD210  =  self._HSTRT_TFD210(self,  Access.RW,  0x00000070,  4,   signed=False)
            self.HEND_OFFSET   =  self._HEND_OFFSET( self,  Access.RW,  0x00000780,  7,   signed=False)
            self.FD3           =  self._FD3(         self,  Access.RW,  0x00000800,  11,  signed=False)
            self.DISFDCC       =  self._DISFDCC(     self,  Access.RW,  0x00001000,  12,  signed=False)
            self.CHM           =  self._CHM(         self,  Access.RW,  0x00004000,  14,  signed=False)
            self.TBL           =  self._TBL(         self,  Access.RW,  0x00018000,  15,  signed=False)
            self.VHIGHFS       =  self._VHIGHFS(     self,  Access.RW,  0x00040000,  18,  signed=False)
            self.VHIGHCHM      =  self._VHIGHCHM(    self,  Access.RW,  0x00080000,  19,  signed=False)
            self.TPFD          =  self._TPFD(        self,  Access.RW,  0x00F00000,  20,  signed=False)
            self.MRES          =  self._MRES(        self,  Access.RW,  0x0F000000,  24,  signed=False)
            self.INTPOL        =  self._INTPOL(      self,  Access.RW,  0x10000000,  28,  signed=False)

    class _COOLCONF(Register):

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

        def __init__(self, parent, access, address, signed):
            super().__init__("COOLCONF", parent, access, address, signed)
            self.SEMIN   =  self._SEMIN( self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.SEUP    =  self._SEUP(  self,  Access.RW,  0x00000060,  5,   signed=False)
            self.SEMAX   =  self._SEMAX( self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.SEDN    =  self._SEDN(  self,  Access.RW,  0x00006000,  13,  signed=False)
            self.SEIMIN  =  self._SEIMIN(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.SGT     =  self._SGT(   self,  Access.RW,  0x007F0000,  16,  signed=True)
            self.SFILT   =  self._SFILT( self,  Access.RW,  0x01000000,  24,  signed=False)

    class _DCCTRL(Register):

        class _DC_TIME(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DC_TIME", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DC_SG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DC_SG", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("DCCTRL", parent, access, address, signed)
            self.DC_TIME  =  self._DC_TIME(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.DC_SG    =  self._DC_SG(  self,  Access.RW,  0x00FF0000,  16,  signed=False)

    class _DRV_STATUS(Register):

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
                    self.INACTIVE  =  Option(False,  parent,  "INACTIVE")
                    self.ACTIVE    =  Option(True,   parent,  "ACTIVE")

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

        def __init__(self, parent, access, address, signed):
            super().__init__("DRV_STATUS", parent, access, address, signed)
            self.SG_RESULT   =  self._SG_RESULT( self,  Access.R,  0x000003FF,  0,   signed=False)
            self.S2VSA       =  self._S2VSA(     self,  Access.R,  0x00001000,  12,  signed=False)
            self.S2VSB       =  self._S2VSB(     self,  Access.R,  0x00002000,  13,  signed=False)
            self.STEALTH     =  self._STEALTH(   self,  Access.R,  0x00004000,  14,  signed=False)
            self.FSACTIVE    =  self._FSACTIVE(  self,  Access.R,  0x00008000,  15,  signed=False)
            self.CS_ACTUAL   =  self._CS_ACTUAL( self,  Access.R,  0x001F0000,  16,  signed=False)
            self.STALLGUARD  =  self._STALLGUARD(self,  Access.R,  0x01000000,  24,  signed=False)
            self.OT          =  self._OT(        self,  Access.R,  0x02000000,  25,  signed=False)
            self.OTPW        =  self._OTPW(      self,  Access.R,  0x04000000,  26,  signed=False)
            self.S2GA        =  self._S2GA(      self,  Access.R,  0x08000000,  27,  signed=False)
            self.S2GB        =  self._S2GB(      self,  Access.R,  0x10000000,  28,  signed=False)
            self.OLA         =  self._OLA(       self,  Access.R,  0x20000000,  29,  signed=False)
            self.OLB         =  self._OLB(       self,  Access.R,  0x40000000,  30,  signed=False)
            self.STST        =  self._STST(      self,  Access.R,  0x80000000,  31,  signed=False)

    class _PWMCONF(Register):

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
                    self.CTRL_ACTIVE    =  Option(False,  parent,  "CTRL_ACTIVE")
                    self.CTRL_INACTIVE  =  Option(True,   parent,  "CTRL_INACTIVE")

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

        def __init__(self, parent, access, address, signed):
            super().__init__("PWMCONF", parent, access, address, signed)
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

    class _PWM_SCALE(Register):

        class _PWM_SCALE_SUM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_SCALE_SUM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_SCALE_AUTO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_SCALE_AUTO", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_SCALE", parent, access, address, signed)
            self.PWM_SCALE_SUM   =  self._PWM_SCALE_SUM( self,  Access.R,  0x000003FF,  0,   signed=False)
            self.PWM_SCALE_AUTO  =  self._PWM_SCALE_AUTO(self,  Access.R,  0x01FF0000,  16,  signed=False)

    class _PWM_AUTO(Register):

        class _PWM_OFS_AUTO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_OFS_AUTO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_GRAD_AUTO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_GRAD_AUTO", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_AUTO", parent, access, address, signed)
            self.PWM_OFS_AUTO   =  self._PWM_OFS_AUTO( self,  Access.R,  0x000000FF,  0,   signed=False)
            self.PWM_GRAD_AUTO  =  self._PWM_GRAD_AUTO(self,  Access.R,  0x00FF0000,  16,  signed=False)

    class _SG4_CONF(Register):

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

        class _sg_angle_offset(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLE  =  Option(False,  parent,  "DISABLE")
                    self.ENABLE   =  Option(True,   parent,  "ENABLE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("sg_angle_offset", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("SG4_CONF", parent, access, address, signed)
            self.SG4_THRS         =  self._SG4_THRS(       self,  Access.RW,  0x000000FF,  0,  signed=False)
            self.SG4_FILT_EN      =  self._SG4_FILT_EN(    self,  Access.RW,  0x00000100,  8,  signed=False)
            self.sg_angle_offset  =  self._sg_angle_offset(self,  Access.RW,  0x00000200,  9,  signed=False)

    class _SG4_RESULT(Register):

        class _SG4_RESULT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG4_RESULT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("SG4_RESULT", parent, access, address, signed)
            self.SG4_RESULT  =  self._SG4_RESULT(self,  Access.R,  0x000003FF,  0,  signed=False)

    class _SG4_IND(Register):

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

        def __init__(self, parent, access, address, signed):
            super().__init__("SG4_IND", parent, access, address, signed)
            self.SG4_IND_0  =  self._SG4_IND_0(self,  Access.R,  0x000000FF,  0,   signed=False)
            self.SG4_IND_1  =  self._SG4_IND_1(self,  Access.R,  0x0000FF00,  8,   signed=False)
            self.SG4_IND_2  =  self._SG4_IND_2(self,  Access.R,  0x00FF0000,  16,  signed=False)
            self.SG4_IND_3  =  self._SG4_IND_3(self,  Access.R,  0xFF000000,  24,  signed=False)

    def __init__(self, channel, block, width):
        super().__init__("ALL_REGISTERS", channel, block, width)
        self.GCONF             =  self._GCONF(           self,  Access.RW,   0x0000,  False)
        self.GSTAT             =  self._GSTAT(           self,  Access.RWC,  0x0001,  False)
        self.IFCNT             =  self._IFCNT(           self,  Access.R,    0x0002,  False)
        self.NODECONF          =  self._NODECONF(        self,  Access.RW,   0x0003,  False)
        self.IOIN              =  self._IOIN(            self,  Access.RW,   0x0004,  False)
        self.X_COMPARE         =  self._X_COMPARE(       self,  Access.RW,   0x0005,  True)
        self.X_COMPARE_REPEAT  =  self._X_COMPARE_REPEAT(self,  Access.RW,   0x0006,  False)
        self.DIAG_GCONF        =  self._DIAG_GCONF(      self,  Access.RW,   0x0007,  False)
        self.DRV_CONF          =  self._DRV_CONF(        self,  Access.RW,   0x000A,  False)
        self.GLOBAL_SCALER     =  self._GLOBAL_SCALER(   self,  Access.RW,   0x000B,  False)
        self.IHOLD_IRUN        =  self._IHOLD_IRUN(      self,  Access.RW,   0x0010,  False)
        self.TPOWERDOWN        =  self._TPOWERDOWN(      self,  Access.RW,   0x0011,  False)
        self.TSTEP             =  self._TSTEP(           self,  Access.R,    0x0012,  False)
        self.TPWMTHRS          =  self._TPWMTHRS(        self,  Access.RW,   0x0013,  False)
        self.TCOOLTHRS         =  self._TCOOLTHRS(       self,  Access.RW,   0x0014,  False)
        self.THIGH             =  self._THIGH(           self,  Access.RW,   0x0015,  False)
        self.RAMPMODE          =  self._RAMPMODE(        self,  Access.RW,   0x0020,  False)
        self.XACTUAL           =  self._XACTUAL(         self,  Access.RW,   0x0021,  True)
        self.VACTUAL           =  self._VACTUAL(         self,  Access.R,    0x0022,  True)
        self.VSTART            =  self._VSTART(          self,  Access.RW,   0x0023,  False)
        self.A1                =  self._A1(              self,  Access.RW,   0x0024,  False)
        self.V1                =  self._V1(              self,  Access.RW,   0x0025,  False)
        self.AMAX              =  self._AMAX(            self,  Access.RW,   0x0026,  False)
        self.VMAX              =  self._VMAX(            self,  Access.RW,   0x0027,  False)
        self.DMAX              =  self._DMAX(            self,  Access.RW,   0x0028,  False)
        self.TVMAX             =  self._TVMAX(           self,  Access.RW,   0x0029,  False)
        self.D1                =  self._D1(              self,  Access.RW,   0x002A,  False)
        self.VSTOP             =  self._VSTOP(           self,  Access.RW,   0x002B,  False)
        self.TZEROWAIT         =  self._TZEROWAIT(       self,  Access.RW,   0x002C,  False)
        self.XTARGET           =  self._XTARGET(         self,  Access.RW,   0x002D,  True)
        self.V2                =  self._V2(              self,  Access.RW,   0x002E,  False)
        self.A2                =  self._A2(              self,  Access.RW,   0x002F,  False)
        self.D2                =  self._D2(              self,  Access.RW,   0x0030,  False)
        self.AACTUAL           =  self._AACTUAL(         self,  Access.R,    0x0031,  True)
        self.VDCMIN            =  self._VDCMIN(          self,  Access.RW,   0x0033,  False)
        self.SW_MODE           =  self._SW_MODE(         self,  Access.RW,   0x0034,  False)
        self.RAMP_STAT         =  self._RAMP_STAT(       self,  Access.RWC,  0x0035,  False)
        self.XLATCH            =  self._XLATCH(          self,  Access.R,    0x0036,  True)
        self.ENCMODE           =  self._ENCMODE(         self,  Access.RW,   0x0038,  False)
        self.X_ENC             =  self._X_ENC(           self,  Access.RW,   0x0039,  True)
        self.ENC_CONST         =  self._ENC_CONST(       self,  Access.RW,   0x003A,  True)
        self.ENC_STATUS        =  self._ENC_STATUS(      self,  Access.RWC,  0x003B,  False)
        self.ENC_LATCH         =  self._ENC_LATCH(       self,  Access.R,    0x003C,  True)
        self.ENC_DEVIATION     =  self._ENC_DEVIATION(   self,  Access.RW,   0x003D,  False)
        self.VIRTUAL_STOP_L    =  self._VIRTUAL_STOP_L(  self,  Access.RW,   0x003E,  True)
        self.VIRTUAL_STOP_R    =  self._VIRTUAL_STOP_R(  self,  Access.RW,   0x003F,  True)
        self.ADC_VSUPPLY_AIN   =  self._ADC_VSUPPLY_AIN( self,  Access.R,    0x0050,  False)
        self.ADC_TEMP          =  self._ADC_TEMP(        self,  Access.R,    0x0051,  False)
        self.OTW_OV_VTH        =  self._OTW_OV_VTH(      self,  Access.RW,   0x0052,  False)
        self.MSLUT_0           =  self._MSLUT_0(         self,  Access.RW,   0x0060,  False)
        self.MSLUT_1           =  self._MSLUT_1(         self,  Access.RW,   0x0061,  False)
        self.MSLUT_2           =  self._MSLUT_2(         self,  Access.RW,   0x0062,  False)
        self.MSLUT_3           =  self._MSLUT_3(         self,  Access.RW,   0x0063,  False)
        self.MSLUT_4           =  self._MSLUT_4(         self,  Access.RW,   0x0064,  False)
        self.MSLUT_5           =  self._MSLUT_5(         self,  Access.RW,   0x0065,  False)
        self.MSLUT_6           =  self._MSLUT_6(         self,  Access.RW,   0x0066,  False)
        self.MSLUT_7           =  self._MSLUT_7(         self,  Access.RW,   0x0067,  False)
        self.MSLUTSEL          =  self._MSLUTSEL(        self,  Access.RW,   0x0068,  False)
        self.MSLUTSTART        =  self._MSLUTSTART(      self,  Access.RW,   0x0069,  False)
        self.MSCNT             =  self._MSCNT(           self,  Access.R,    0x006A,  False)
        self.MSCURACT          =  self._MSCURACT(        self,  Access.R,    0x006B,  False)
        self.CHOPCONF          =  self._CHOPCONF(        self,  Access.RW,   0x006C,  False)
        self.COOLCONF          =  self._COOLCONF(        self,  Access.RW,   0x006D,  False)
        self.DCCTRL            =  self._DCCTRL(          self,  Access.RW,   0x006E,  False)
        self.DRV_STATUS        =  self._DRV_STATUS(      self,  Access.R,    0x006F,  False)
        self.PWMCONF           =  self._PWMCONF(         self,  Access.RW,   0x0070,  False)
        self.PWM_SCALE         =  self._PWM_SCALE(       self,  Access.R,    0x0071,  False)
        self.PWM_AUTO          =  self._PWM_AUTO(        self,  Access.R,    0x0072,  False)
        self.SG4_CONF          =  self._SG4_CONF(        self,  Access.RW,   0x0074,  False)
        self.SG4_RESULT        =  self._SG4_RESULT(      self,  Access.R,    0x0075,  False)
        self.SG4_IND           =  self._SG4_IND(         self,  Access.R,    0x0076,  False)
