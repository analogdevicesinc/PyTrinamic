################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Choice, Field, Register


class ADCMap:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)


class _ALL_REGISTERS(RegisterGroup):

    class _SRC_CONFIG(Register):

        class _ADC0_MUX0_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC0_MUX0_OFF = Choice(0, parent)
                    self.ADC0_MUX0_1ST = Choice(1, parent)
                    self.ADC0_MUX0_2ND = Choice(2, parent)
                    self.ADC0_MUX0_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC0_MUX1_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC0_MUX1_OFF = Choice(0, parent)
                    self.ADC0_MUX1_1ST = Choice(1, parent)
                    self.ADC0_MUX1_2ND = Choice(2, parent)
                    self.ADC0_MUX1_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC0_MUX2_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC0_MUX2_OFF = Choice(0, parent)
                    self.ADC0_MUX2_1ST = Choice(1, parent)
                    self.ADC0_MUX2_2ND = Choice(2, parent)
                    self.ADC0_MUX2_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC0_MUX3_DIS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX3_DIS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC0_MUX2_DETOUR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC1_MUX0_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC1_MUX0_OFF = Choice(0, parent)
                    self.ADC1_MUX0_1ST = Choice(1, parent)
                    self.ADC1_MUX0_2ND = Choice(2, parent)
                    self.ADC1_MUX0_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC1_MUX1_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC1_MUX1_OFF = Choice(0, parent)
                    self.ADC1_MUX1_1ST = Choice(1, parent)
                    self.ADC1_MUX1_2ND = Choice(2, parent)
                    self.ADC1_MUX1_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC1_MUX2_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC1_MUX2_OFF = Choice(0, parent)
                    self.ADC1_MUX2_1ST = Choice(1, parent)
                    self.ADC1_MUX2_2ND = Choice(2, parent)
                    self.ADC1_MUX2_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC1_MUX2_DETOUR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_MUX0_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC2_MUX0_OFF = Choice(0, parent)
                    self.ADC2_MUX0_1ST = Choice(1, parent)
                    self.ADC2_MUX0_2ND = Choice(2, parent)
                    self.ADC2_MUX0_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC2_MUX1_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC2_MUX1_OFF = Choice(0, parent)
                    self.ADC2_MUX1_1ST = Choice(1, parent)
                    self.ADC2_MUX1_2ND = Choice(2, parent)
                    self.ADC2_MUX1_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC2_MUX2_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC2_MUX2_OFF = Choice(0, parent)
                    self.ADC2_MUX2_1ST = Choice(1, parent)
                    self.ADC2_MUX2_2ND = Choice(2, parent)
                    self.ADC2_MUX2_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC2_MUX3_DIS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX3_DIS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_MUX2_DETOUR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC3_MUX0_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC3_MUX0_OFF = Choice(0, parent)
                    self.ADC3_MUX0_1ST = Choice(1, parent)
                    self.ADC3_MUX0_2ND = Choice(2, parent)
                    self.ADC3_MUX0_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC3_MUX1_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC3_MUX1_OFF = Choice(0, parent)
                    self.ADC3_MUX1_1ST = Choice(1, parent)
                    self.ADC3_MUX1_2ND = Choice(2, parent)
                    self.ADC3_MUX1_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC3_MUX2_CFG(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC3_MUX2_OFF = Choice(0, parent)
                    self.ADC3_MUX2_1ST = Choice(1, parent)
                    self.ADC3_MUX2_2ND = Choice(2, parent)
                    self.ADC3_MUX2_3RD = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADC3_MUX2_DETOUR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SRC_CONFIG", parent, access, address, block, signed)
            self.ADC0_MUX0_CFG     =  self._ADC0_MUX0_CFG(   self,  Access.RW,  0x00000003,  0,   signed=False)
            self.ADC0_MUX1_CFG     =  self._ADC0_MUX1_CFG(   self,  Access.RW,  0x0000000C,  2,   signed=False)
            self.ADC0_MUX2_CFG     =  self._ADC0_MUX2_CFG(   self,  Access.RW,  0x00000030,  4,   signed=False)
            self.ADC0_MUX3_DIS     =  self._ADC0_MUX3_DIS(   self,  Access.RW,  0x00000040,  6,   signed=False)
            self.ADC0_MUX2_DETOUR  =  self._ADC0_MUX2_DETOUR(self,  Access.RW,  0x00000080,  7,   signed=False)
            self.ADC1_MUX0_CFG     =  self._ADC1_MUX0_CFG(   self,  Access.RW,  0x00000300,  8,   signed=False)
            self.ADC1_MUX1_CFG     =  self._ADC1_MUX1_CFG(   self,  Access.RW,  0x00000C00,  10,  signed=False)
            self.ADC1_MUX2_CFG     =  self._ADC1_MUX2_CFG(   self,  Access.RW,  0x00003000,  12,  signed=False)
            self.ADC1_MUX2_DETOUR  =  self._ADC1_MUX2_DETOUR(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.ADC2_MUX0_CFG     =  self._ADC2_MUX0_CFG(   self,  Access.RW,  0x00030000,  16,  signed=False)
            self.ADC2_MUX1_CFG     =  self._ADC2_MUX1_CFG(   self,  Access.RW,  0x000C0000,  18,  signed=False)
            self.ADC2_MUX2_CFG     =  self._ADC2_MUX2_CFG(   self,  Access.RW,  0x00300000,  20,  signed=False)
            self.ADC2_MUX3_DIS     =  self._ADC2_MUX3_DIS(   self,  Access.RW,  0x00400000,  22,  signed=False)
            self.ADC2_MUX2_DETOUR  =  self._ADC2_MUX2_DETOUR(self,  Access.RW,  0x00800000,  23,  signed=False)
            self.ADC3_MUX0_CFG     =  self._ADC3_MUX0_CFG(   self,  Access.RW,  0x03000000,  24,  signed=False)
            self.ADC3_MUX1_CFG     =  self._ADC3_MUX1_CFG(   self,  Access.RW,  0x0C000000,  26,  signed=False)
            self.ADC3_MUX2_CFG     =  self._ADC3_MUX2_CFG(   self,  Access.RW,  0x30000000,  28,  signed=False)
            self.ADC3_MUX2_DETOUR  =  self._ADC3_MUX2_DETOUR(self,  Access.RW,  0x80000000,  31,  signed=False)

    class _SETUP(Register):

        class _ADC_SHIFT_SAMPLE(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC_SHIFT_500NS = Choice(0, parent)
                    self.ADC_SHIFT_600NS = Choice(1, parent)
                    self.ADC_SHIFT_700NS = Choice(2, parent)
                    self.ADC_SHIFT_800NS = Choice(3, parent)
                    self.ADC_SHIFT_900NS = Choice(4, parent)
                    self.ADC_SHIFT_1000NS = Choice(5, parent)
                    self.ADC_SHIFT_1100NS = Choice(6, parent)
                    self.ADC_SHIFT_1200NS = Choice(7, parent)
                    self.ADC_SHIFT_1300NS = Choice(8, parent)
                    self.ADC_SHIFT_1400NS = Choice(9, parent)
                    self.ADC_SHIFT_1500NS = Choice(10, parent)
                    self.ADC_SHIFT_1600NS = Choice(11, parent)
                    self.ADC_SHIFT_1700NS = Choice(12, parent)
                    self.ADC_SHIFT_1800NS = Choice(13, parent)
                    self.ADC_SHIFT_1900NS = Choice(14, parent)
                    self.ADC_SHIFT_2000NS = Choice(15, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_SHIFT_SAMPLE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SETUP", parent, access, address, block, signed)
            self.ADC_SHIFT_SAMPLE  =  self._ADC_SHIFT_SAMPLE(self,  Access.RW,  0x000F0000,  16,  signed=False)

    class _STATUS(Register):

        class _RDY_ADC_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RDY_ADC_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RDY_ADC_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RDY_ADC_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RDY_ADC_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RDY_ADC_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RDY_ADC_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RDY_ADC_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC0_WTCHDG_FAIL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_WTCHDG_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC1_WTCHDG_FAIL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_WTCHDG_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_WTCHDG_FAIL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_WTCHDG_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC3_WTCHDG_FAIL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_WTCHDG_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC0_MUXSEQ_FAIL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUXSEQ_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC1_MUXSEQ_FAIL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUXSEQ_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_MUXSEQ_FAIL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUXSEQ_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC3_MUXSEQ_FAIL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUXSEQ_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("STATUS", parent, access, address, block, signed)
            self.RDY_ADC_0         =  self._RDY_ADC_0(       self,  Access.R,  0x00000001,  0,   signed=False)
            self.RDY_ADC_1         =  self._RDY_ADC_1(       self,  Access.R,  0x00000002,  1,   signed=False)
            self.RDY_ADC_2         =  self._RDY_ADC_2(       self,  Access.R,  0x00000004,  2,   signed=False)
            self.RDY_ADC_3         =  self._RDY_ADC_3(       self,  Access.R,  0x00000008,  3,   signed=False)
            self.ADC0_WTCHDG_FAIL  =  self._ADC0_WTCHDG_FAIL(self,  Access.R,  0x00000100,  8,   signed=False)
            self.ADC1_WTCHDG_FAIL  =  self._ADC1_WTCHDG_FAIL(self,  Access.R,  0x00000200,  9,   signed=False)
            self.ADC2_WTCHDG_FAIL  =  self._ADC2_WTCHDG_FAIL(self,  Access.R,  0x00000400,  10,  signed=False)
            self.ADC3_WTCHDG_FAIL  =  self._ADC3_WTCHDG_FAIL(self,  Access.R,  0x00000800,  11,  signed=False)
            self.ADC0_MUXSEQ_FAIL  =  self._ADC0_MUXSEQ_FAIL(self,  Access.R,  0x00001000,  12,  signed=False)
            self.ADC1_MUXSEQ_FAIL  =  self._ADC1_MUXSEQ_FAIL(self,  Access.R,  0x00002000,  13,  signed=False)
            self.ADC2_MUXSEQ_FAIL  =  self._ADC2_MUXSEQ_FAIL(self,  Access.R,  0x00004000,  14,  signed=False)
            self.ADC3_MUXSEQ_FAIL  =  self._ADC3_MUXSEQ_FAIL(self,  Access.R,  0x00008000,  15,  signed=False)

    class _CSA_SETUP(Register):

        class _CSA0_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA0_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA1_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA1_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA2_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA2_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA3_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA012_GAIN(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.csa012_gain_x5 = Choice(0, parent)
                    self.csa012_gain_x10 = Choice(1, parent)
                    self.csa012_gain_x20 = Choice(2, parent)
                    self.csa012_gain_x40 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA012_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _CSA012_BYPASS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA012_BYPASS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA3_GAIN(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.csa3_gain_x5 = Choice(0, parent)
                    self.csa3_gain_x10 = Choice(1, parent)
                    self.csa3_gain_x20 = Choice(2, parent)
                    self.csa3_gain_x40 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _CSA3_BYPASS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_BYPASS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA012_FILT(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.csa012_filt_0u55 = Choice(0, parent)
                    self.csa012_filt_0u75 = Choice(1, parent)
                    self.csa012_filt_1u00 = Choice(2, parent)
                    self.csa012_filt_1u35 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA012_FILT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _CSA3_FILT(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.csa3_filt_0u55 = Choice(0, parent)
                    self.csa3_filt_0u75 = Choice(1, parent)
                    self.csa3_filt_1u00 = Choice(2, parent)
                    self.csa3_filt_1u35 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_FILT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _CSA_AZ_FLTLNGTH_EXP(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.csa_az_filt_off = Choice(0, parent)
                    self.csa_az_filt_2 = Choice(1, parent)
                    self.csa_az_filt_4 = Choice(2, parent)
                    self.csa_az_filt_8 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA_AZ_FLTLNGTH_EXP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        def __init__(self, parent, access, address, block, signed):
            super().__init__("CSA_SETUP", parent, access, address, block, signed)
            self.CSA0_EN              =  self._CSA0_EN(            self,  Access.RW,  0x00000001,  0,   signed=False)
            self.CSA1_EN              =  self._CSA1_EN(            self,  Access.RW,  0x00000002,  1,   signed=False)
            self.CSA2_EN              =  self._CSA2_EN(            self,  Access.RW,  0x00000004,  2,   signed=False)
            self.CSA3_EN              =  self._CSA3_EN(            self,  Access.RW,  0x00000008,  3,   signed=False)
            self.CSA012_GAIN          =  self._CSA012_GAIN(        self,  Access.RW,  0x00000030,  4,   signed=False)
            self.CSA012_BYPASS        =  self._CSA012_BYPASS(      self,  Access.RW,  0x00000040,  6,   signed=False)
            self.CSA3_GAIN            =  self._CSA3_GAIN(          self,  Access.RW,  0x00000300,  8,   signed=False)
            self.CSA3_BYPASS          =  self._CSA3_BYPASS(        self,  Access.RW,  0x00000400,  10,  signed=False)
            self.CSA012_FILT          =  self._CSA012_FILT(        self,  Access.RW,  0x00003000,  12,  signed=False)
            self.CSA3_FILT            =  self._CSA3_FILT(          self,  Access.RW,  0x0000C000,  14,  signed=False)
            self.CSA_AZ_FLTLNGTH_EXP  =  self._CSA_AZ_FLTLNGTH_EXP(self,  Access.RW,  0x000F0000,  16,  signed=False)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.SRC_CONFIG  =  self._SRC_CONFIG(self,  Access.RW,  0x0001,  block,  False)
        self.SETUP       =  self._SETUP(     self,  Access.RW,  0x0002,  block,  False)
        self.STATUS      =  self._STATUS(    self,  Access.R,   0x0005,  block,  False)
        self.CSA_SETUP   =  self._CSA_SETUP( self,  Access.RW,  0x0007,  block,  False)
