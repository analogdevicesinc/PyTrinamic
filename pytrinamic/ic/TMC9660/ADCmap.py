################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Choice, Option, Field, Register


class ADCMap:

    def __init__(self, *, channel=None, block=None, width=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(channel, block, width)


class _ALL_REGISTERS(RegisterGroup):

    class _SRC_CONFIG(Register):

        class _ADC0_MUX0_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC0_MUX0_OFF  =  Option(0,  parent,  "ADC0_MUX0_OFF")
                    self.ADC0_MUX0_1ST  =  Option(1,  parent,  "ADC0_MUX0_1ST")
                    self.ADC0_MUX0_2ND  =  Option(2,  parent,  "ADC0_MUX0_2ND")
                    self.ADC0_MUX0_3RD  =  Option(3,  parent,  "ADC0_MUX0_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC0_MUX1_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC0_MUX1_OFF  =  Option(0,  parent,  "ADC0_MUX1_OFF")
                    self.ADC0_MUX1_1ST  =  Option(1,  parent,  "ADC0_MUX1_1ST")
                    self.ADC0_MUX1_2ND  =  Option(2,  parent,  "ADC0_MUX1_2ND")
                    self.ADC0_MUX1_3RD  =  Option(3,  parent,  "ADC0_MUX1_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC0_MUX2_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC0_MUX2_OFF  =  Option(0,  parent,  "ADC0_MUX2_OFF")
                    self.ADC0_MUX2_1ST  =  Option(1,  parent,  "ADC0_MUX2_1ST")
                    self.ADC0_MUX2_2ND  =  Option(2,  parent,  "ADC0_MUX2_2ND")
                    self.ADC0_MUX2_3RD  =  Option(3,  parent,  "ADC0_MUX2_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC0_MUX3_DIS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX3_DIS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC0_MUX2_DETOUR(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_CHANGE         =  Option(False,  parent,  "NO_CHANGE")
                    self.ADC0_MUX2_DETOUR  =  Option(True,   parent,  "ADC0_MUX2_DETOUR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC1_MUX0_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC1_MUX0_OFF  =  Option(0,  parent,  "ADC1_MUX0_OFF")
                    self.ADC1_MUX0_1ST  =  Option(1,  parent,  "ADC1_MUX0_1ST")
                    self.ADC1_MUX0_2ND  =  Option(2,  parent,  "ADC1_MUX0_2ND")
                    self.ADC1_MUX0_3RD  =  Option(3,  parent,  "ADC1_MUX0_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC1_MUX1_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC1_MUX1_OFF  =  Option(0,  parent,  "ADC1_MUX1_OFF")
                    self.ADC1_MUX1_1ST  =  Option(1,  parent,  "ADC1_MUX1_1ST")
                    self.ADC1_MUX1_2ND  =  Option(2,  parent,  "ADC1_MUX1_2ND")
                    self.ADC1_MUX1_3RD  =  Option(3,  parent,  "ADC1_MUX1_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC1_MUX2_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC1_MUX2_OFF  =  Option(0,  parent,  "ADC1_MUX2_OFF")
                    self.ADC1_MUX2_1ST  =  Option(1,  parent,  "ADC1_MUX2_1ST")
                    self.ADC1_MUX2_2ND  =  Option(2,  parent,  "ADC1_MUX2_2ND")
                    self.ADC1_MUX2_3RD  =  Option(3,  parent,  "ADC1_MUX2_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC1_MUX2_DETOUR(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_CHANGE         =  Option(False,  parent,  "NO_CHANGE")
                    self.ADC1_MUX2_DETOUR  =  Option(True,   parent,  "ADC1_MUX2_DETOUR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC2_MUX0_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC2_MUX0_OFF  =  Option(0,  parent,  "ADC2_MUX0_OFF")
                    self.ADC2_MUX0_1ST  =  Option(1,  parent,  "ADC2_MUX0_1ST")
                    self.ADC2_MUX0_2ND  =  Option(2,  parent,  "ADC2_MUX0_2ND")
                    self.ADC2_MUX0_3RD  =  Option(3,  parent,  "ADC2_MUX0_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC2_MUX1_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC2_MUX1_OFF  =  Option(0,  parent,  "ADC2_MUX1_OFF")
                    self.ADC2_MUX1_1ST  =  Option(1,  parent,  "ADC2_MUX1_1ST")
                    self.ADC2_MUX1_2ND  =  Option(2,  parent,  "ADC2_MUX1_2ND")
                    self.ADC2_MUX1_3RD  =  Option(3,  parent,  "ADC2_MUX1_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC2_MUX2_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC2_MUX2_OFF  =  Option(0,  parent,  "ADC2_MUX2_OFF")
                    self.ADC2_MUX2_1ST  =  Option(1,  parent,  "ADC2_MUX2_1ST")
                    self.ADC2_MUX2_2ND  =  Option(2,  parent,  "ADC2_MUX2_2ND")
                    self.ADC2_MUX2_3RD  =  Option(3,  parent,  "ADC2_MUX2_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC2_MUX3_DIS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX3_DIS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_MUX2_DETOUR(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_CHANGE         =  Option(False,  parent,  "NO_CHANGE")
                    self.ADC2_MUX2_DETOUR  =  Option(True,   parent,  "ADC2_MUX2_DETOUR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC3_MUX0_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC3_MUX0_OFF  =  Option(0,  parent,  "ADC3_MUX0_OFF")
                    self.ADC3_MUX0_1ST  =  Option(1,  parent,  "ADC3_MUX0_1ST")
                    self.ADC3_MUX0_2ND  =  Option(2,  parent,  "ADC3_MUX0_2ND")
                    self.ADC3_MUX0_3RD  =  Option(3,  parent,  "ADC3_MUX0_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC3_MUX1_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC3_MUX1_OFF  =  Option(0,  parent,  "ADC3_MUX1_OFF")
                    self.ADC3_MUX1_1ST  =  Option(1,  parent,  "ADC3_MUX1_1ST")
                    self.ADC3_MUX1_2ND  =  Option(2,  parent,  "ADC3_MUX1_2ND")
                    self.ADC3_MUX1_3RD  =  Option(3,  parent,  "ADC3_MUX1_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC3_MUX2_CFG(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC3_MUX2_OFF  =  Option(0,  parent,  "ADC3_MUX2_OFF")
                    self.ADC3_MUX2_1ST  =  Option(1,  parent,  "ADC3_MUX2_1ST")
                    self.ADC3_MUX2_2ND  =  Option(2,  parent,  "ADC3_MUX2_2ND")
                    self.ADC3_MUX2_3RD  =  Option(3,  parent,  "ADC3_MUX2_3RD")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC3_MUX2_DETOUR(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_CHANGE         =  Option(False,  parent,  "NO_CHANGE")
                    self.ADC3_MUX2_DETOUR  =  Option(True,   parent,  "ADC3_MUX2_DETOUR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("SRC_CONFIG", parent, access, address, signed)
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

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC_SHIFT_500NS   =  Option(0,   parent,  "ADC_SHIFT_500NS")
                    self.ADC_SHIFT_600NS   =  Option(1,   parent,  "ADC_SHIFT_600NS")
                    self.ADC_SHIFT_700NS   =  Option(2,   parent,  "ADC_SHIFT_700NS")
                    self.ADC_SHIFT_800NS   =  Option(3,   parent,  "ADC_SHIFT_800NS")
                    self.ADC_SHIFT_900NS   =  Option(4,   parent,  "ADC_SHIFT_900NS")
                    self.ADC_SHIFT_1000NS  =  Option(5,   parent,  "ADC_SHIFT_1000NS")
                    self.ADC_SHIFT_1100NS  =  Option(6,   parent,  "ADC_SHIFT_1100NS")
                    self.ADC_SHIFT_1200NS  =  Option(7,   parent,  "ADC_SHIFT_1200NS")
                    self.ADC_SHIFT_1300NS  =  Option(8,   parent,  "ADC_SHIFT_1300NS")
                    self.ADC_SHIFT_1400NS  =  Option(9,   parent,  "ADC_SHIFT_1400NS")
                    self.ADC_SHIFT_1500NS  =  Option(10,  parent,  "ADC_SHIFT_1500NS")
                    self.ADC_SHIFT_1600NS  =  Option(11,  parent,  "ADC_SHIFT_1600NS")
                    self.ADC_SHIFT_1700NS  =  Option(12,  parent,  "ADC_SHIFT_1700NS")
                    self.ADC_SHIFT_1800NS  =  Option(13,  parent,  "ADC_SHIFT_1800NS")
                    self.ADC_SHIFT_1900NS  =  Option(14,  parent,  "ADC_SHIFT_1900NS")
                    self.ADC_SHIFT_2000NS  =  Option(15,  parent,  "ADC_SHIFT_2000NS")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_SHIFT_SAMPLE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("SETUP", parent, access, address, signed)
            self.ADC_SHIFT_SAMPLE  =  self._ADC_SHIFT_SAMPLE(self,  Access.RW,  0x000F0000,  16,  signed=False)

    class _STATUS(Register):

        class _RDY_ADC_0(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC0_NRDY  =  Option(False,  parent,  "ADC0_NRDY")
                    self.ADC0_RDY   =  Option(True,   parent,  "ADC0_RDY")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RDY_ADC_0", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _RDY_ADC_1(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC1_NRDY  =  Option(False,  parent,  "ADC1_NRDY")
                    self.ADC1_RDY   =  Option(True,   parent,  "ADC1_RDY")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RDY_ADC_1", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _RDY_ADC_2(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC2_NRDY  =  Option(False,  parent,  "ADC2_NRDY")
                    self.ADC2_RDY   =  Option(True,   parent,  "ADC2_RDY")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RDY_ADC_2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _RDY_ADC_3(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC3_NRDY  =  Option(False,  parent,  "ADC3_NRDY")
                    self.ADC3_RDY   =  Option(True,   parent,  "ADC3_RDY")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RDY_ADC_3", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC0_WTCHDG_FAIL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC0_OK    =  Option(False,  parent,  "ADC0_OK")
                    self.ADC0_FAIL  =  Option(True,   parent,  "ADC0_FAIL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_WTCHDG_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC1_WTCHDG_FAIL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC1_OK    =  Option(False,  parent,  "ADC1_OK")
                    self.ADC1_FAIL  =  Option(True,   parent,  "ADC1_FAIL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_WTCHDG_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC2_WTCHDG_FAIL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC2_OK    =  Option(False,  parent,  "ADC2_OK")
                    self.ADC2_FAIL  =  Option(True,   parent,  "ADC2_FAIL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_WTCHDG_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC3_WTCHDG_FAIL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC3_OK    =  Option(False,  parent,  "ADC3_OK")
                    self.ADC3_FAIL  =  Option(True,   parent,  "ADC3_FAIL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_WTCHDG_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC0_MUXSEQ_FAIL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC0_SEQ_OK    =  Option(False,  parent,  "ADC0_SEQ_OK")
                    self.ADC0_SEQ_FAIL  =  Option(True,   parent,  "ADC0_SEQ_FAIL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUXSEQ_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC1_MUXSEQ_FAIL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC1_SEQ_OK    =  Option(False,  parent,  "ADC1_SEQ_OK")
                    self.ADC1_SEQ_FAIL  =  Option(True,   parent,  "ADC1_SEQ_FAIL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUXSEQ_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC2_MUXSEQ_FAIL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC2_SEQ_OK    =  Option(False,  parent,  "ADC2_SEQ_OK")
                    self.ADC2_SEQ_FAIL  =  Option(True,   parent,  "ADC2_SEQ_FAIL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUXSEQ_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC3_MUXSEQ_FAIL(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ADC3_SEQ_OK    =  Option(False,  parent,  "ADC3_SEQ_OK")
                    self.ADC3_SEQ_FAIL  =  Option(True,   parent,  "ADC3_SEQ_FAIL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUXSEQ_FAIL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS", parent, access, address, signed)
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

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA0_OFF  =  Option(False,  parent,  "CSA0_OFF")
                    self.CSA0_EN   =  Option(True,   parent,  "CSA0_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA0_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA1_EN(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA1_OFF  =  Option(False,  parent,  "CSA1_OFF")
                    self.CSA1_EN   =  Option(True,   parent,  "CSA1_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA1_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA2_EN(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA2_OFF  =  Option(False,  parent,  "CSA2_OFF")
                    self.CSA2_EN   =  Option(True,   parent,  "CSA2_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA2_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA3_EN(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA3_OFF  =  Option(False,  parent,  "CSA3_OFF")
                    self.CSA3_EN   =  Option(True,   parent,  "CSA3_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA012_GAIN(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA012_GAIN_x5   =  Option(0,  parent,  "CSA012_GAIN_x5")
                    self.CSA012_GAIN_x10  =  Option(1,  parent,  "CSA012_GAIN_x10")
                    self.CSA012_GAIN_x20  =  Option(2,  parent,  "CSA012_GAIN_x20")
                    self.CSA012_GAIN_x40  =  Option(3,  parent,  "CSA012_GAIN_x40")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA012_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA012_BYPASS(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA012_BYPASS_OFF  =  Option(False,  parent,  "CSA012_BYPASS_OFF")
                    self.CSA012_BYPASS_EN   =  Option(True,   parent,  "CSA012_BYPASS_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA012_BYPASS", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA3_GAIN(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA3_GAIN_x5   =  Option(0,  parent,  "CSA3_GAIN_x5")
                    self.CSA3_GAIN_x10  =  Option(1,  parent,  "CSA3_GAIN_x10")
                    self.CSA3_GAIN_x20  =  Option(2,  parent,  "CSA3_GAIN_x20")
                    self.CSA3_GAIN_x40  =  Option(3,  parent,  "CSA3_GAIN_x40")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA3_BYPASS(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA3_BYPASS_OFF  =  Option(False,  parent,  "CSA3_BYPASS_OFF")
                    self.CSA3_BYPASS_EN   =  Option(True,   parent,  "CSA3_BYPASS_EN")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_BYPASS", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA012_FILT(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA012_FILT_0u55  =  Option(0,  parent,  "CSA012_FILT_0u55")
                    self.CSA012_FILT_0u75  =  Option(1,  parent,  "CSA012_FILT_0u75")
                    self.CSA012_FILT_1u00  =  Option(2,  parent,  "CSA012_FILT_1u00")
                    self.CSA012_FILT_1u35  =  Option(3,  parent,  "CSA012_FILT_1u35")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA012_FILT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA3_FILT(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA3_FILT_0u55  =  Option(0,  parent,  "CSA3_FILT_0u55")
                    self.CSA3_FILT_0u75  =  Option(1,  parent,  "CSA3_FILT_0u75")
                    self.CSA3_FILT_1u00  =  Option(2,  parent,  "CSA3_FILT_1u00")
                    self.CSA3_FILT_1u35  =  Option(3,  parent,  "CSA3_FILT_1u35")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_FILT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA_AZ_FLTLNGTH_EXP(Field):

            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CSA_AZ_FILT_off  =  Option(0,  parent,  "CSA_AZ_FILT_off")
                    self.CSA_AZ_FILT_2    =  Option(1,  parent,  "CSA_AZ_FILT_2")
                    self.CSA_AZ_FILT_4    =  Option(2,  parent,  "CSA_AZ_FILT_4")
                    self.CSA_AZ_FILT_8    =  Option(3,  parent,  "CSA_AZ_FILT_8")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA_AZ_FLTLNGTH_EXP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        def __init__(self, parent, access, address, signed):
            super().__init__("CSA_SETUP", parent, access, address, signed)
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

    def __init__(self, channel, block, width):
        super().__init__("ALL_REGISTERS", channel, block, width)
        self.SRC_CONFIG  =  self._SRC_CONFIG(self,  Access.RW,  0x0001,  False)
        self.SETUP       =  self._SETUP(     self,  Access.RW,  0x0002,  False)
        self.STATUS      =  self._STATUS(    self,  Access.R,   0x0005,  False)
        self.CSA_SETUP   =  self._CSA_SETUP( self,  Access.RW,  0x0007,  False)
