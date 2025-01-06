################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Field, Register


class ADCMap:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)




class _ALL_REGISTERS(RegisterGroup):

    class _ADC_RW_ADDR_DATA(Register):

        class _REG_ADDR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REG_ADDR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REG_DATA_WR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REG_DATA_WR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RD_STROBE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RD_STROBE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _WR_STROBE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WR_STROBE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RD_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RD_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _WR_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WR_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC0_CONFIG_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_CONFIG_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC1_CONFIG_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_CONFIG_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_CONFIG_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_CONFIG_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC3_CONFIG_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_CONFIG_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_RW_ADDR_DATA", parent, access, address, block, signed)
            self.REG_ADDR          =  self._REG_ADDR(self,          Access.RW,  0x0000003F,  0,   signed=False)
            self.REG_DATA_WR       =  self._REG_DATA_WR(self,       Access.RW,  0x0000FF00,  8,   signed=False)
            self.RD_STROBE         =  self._RD_STROBE(self,         Access.RW,  0x00010000,  16,  signed=False)
            self.WR_STROBE         =  self._WR_STROBE(self,         Access.RW,  0x00020000,  17,  signed=False)
            self.RD_DONE           =  self._RD_DONE(self,           Access.R,   0x00040000,  18,  signed=False)
            self.WR_DONE           =  self._WR_DONE(self,           Access.R,   0x00080000,  19,  signed=False)
            self.ADC0_CONFIG_DONE  =  self._ADC0_CONFIG_DONE(self,  Access.RW,  0x03000000,  24,  signed=False)
            self.ADC1_CONFIG_DONE  =  self._ADC1_CONFIG_DONE(self,  Access.RW,  0x0C000000,  26,  signed=False)
            self.ADC2_CONFIG_DONE  =  self._ADC2_CONFIG_DONE(self,  Access.RW,  0x30000000,  28,  signed=False)
            self.ADC3_CONFIG_DONE  =  self._ADC3_CONFIG_DONE(self,  Access.RW,  0xC0000000,  30,  signed=False)

    class _ADC_SRC_CONFIG(Register):

        class _ADC0_MUX0_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC0_MUX1_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC0_MUX2_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC0_MUX3_DIS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX3_DIS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC0_MUX2_DETOUR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC0_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC1_MUX0_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC1_MUX1_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC1_MUX2_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC1_MUX3_DIS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX3_DIS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC1_MUX2_DETOUR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC1_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_MUX0_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_MUX1_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_MUX2_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_MUX3_DIS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX3_DIS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC2_MUX2_DETOUR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC2_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC3_MUX0_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC3_MUX1_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC3_MUX2_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC3_MUX3_DIS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX3_DIS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC3_MUX2_DETOUR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC3_MUX2_DETOUR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_SRC_CONFIG", parent, access, address, block, signed)
            self.ADC0_MUX0_CFG     =  self._ADC0_MUX0_CFG(self,     Access.RW,  0x00000003,  0,   signed=False)
            self.ADC0_MUX1_CFG     =  self._ADC0_MUX1_CFG(self,     Access.RW,  0x0000000C,  2,   signed=False)
            self.ADC0_MUX2_CFG     =  self._ADC0_MUX2_CFG(self,     Access.RW,  0x00000030,  4,   signed=False)
            self.ADC0_MUX3_DIS     =  self._ADC0_MUX3_DIS(self,     Access.RW,  0x00000040,  6,   signed=False)
            self.ADC0_MUX2_DETOUR  =  self._ADC0_MUX2_DETOUR(self,  Access.RW,  0x00000080,  7,   signed=False)
            self.ADC1_MUX0_CFG     =  self._ADC1_MUX0_CFG(self,     Access.RW,  0x00000300,  8,   signed=False)
            self.ADC1_MUX1_CFG     =  self._ADC1_MUX1_CFG(self,     Access.RW,  0x00000C00,  10,  signed=False)
            self.ADC1_MUX2_CFG     =  self._ADC1_MUX2_CFG(self,     Access.RW,  0x00003000,  12,  signed=False)
            self.ADC1_MUX3_DIS     =  self._ADC1_MUX3_DIS(self,     Access.RW,  0x00004000,  14,  signed=False)
            self.ADC1_MUX2_DETOUR  =  self._ADC1_MUX2_DETOUR(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.ADC2_MUX0_CFG     =  self._ADC2_MUX0_CFG(self,     Access.RW,  0x00030000,  16,  signed=False)
            self.ADC2_MUX1_CFG     =  self._ADC2_MUX1_CFG(self,     Access.RW,  0x000C0000,  18,  signed=False)
            self.ADC2_MUX2_CFG     =  self._ADC2_MUX2_CFG(self,     Access.RW,  0x00300000,  20,  signed=False)
            self.ADC2_MUX3_DIS     =  self._ADC2_MUX3_DIS(self,     Access.RW,  0x00400000,  22,  signed=False)
            self.ADC2_MUX2_DETOUR  =  self._ADC2_MUX2_DETOUR(self,  Access.RW,  0x00800000,  23,  signed=False)
            self.ADC3_MUX0_CFG     =  self._ADC3_MUX0_CFG(self,     Access.RW,  0x03000000,  24,  signed=False)
            self.ADC3_MUX1_CFG     =  self._ADC3_MUX1_CFG(self,     Access.RW,  0x0C000000,  26,  signed=False)
            self.ADC3_MUX2_CFG     =  self._ADC3_MUX2_CFG(self,     Access.RW,  0x30000000,  28,  signed=False)
            self.ADC3_MUX3_DIS     =  self._ADC3_MUX3_DIS(self,     Access.RW,  0x40000000,  30,  signed=False)
            self.ADC3_MUX2_DETOUR  =  self._ADC3_MUX2_DETOUR(self,  Access.RW,  0x80000000,  31,  signed=False)

    class _ADC_SETUP(Register):

        class _SELECT_ADC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SELECT_ADC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _NRST_ADC_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NRST_ADC_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _NRST_ADC_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NRST_ADC_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _NRST_ADC_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NRST_ADC_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _NRST_ADC_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NRST_ADC_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MUX0_AUTO_CHOP_DISABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MUX0_AUTO_CHOP_DISABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MUX1_CHOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MUX1_CHOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MUX2_CHOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MUX2_CHOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MUX3_CHOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MUX3_CHOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ23CM_CHOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ23CM_CHOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ_CHOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ_CHOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_ADC_AUTO_PROT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_ADC_AUTO_PROT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MMU_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MMU_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_SHIFT_SAMPLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_SHIFT_SAMPLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC4_OV_MSKI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC4_OV_MSKI", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC5_OV_MSKI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC5_OV_MSKI", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC6_OV_MSKI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC6_OV_MSKI", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC7_OV_MSKI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC7_OV_MSKI", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALF_WAKEUP_FREQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALF_WAKEUP_FREQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_SETUP", parent, access, address, block, signed)
            self.SELECT_ADC              =  self._SELECT_ADC(self,              Access.RW,  0x0000000F,  0,   signed=False)
            self.NRST_ADC_0              =  self._NRST_ADC_0(self,              Access.RW,  0x00000010,  4,   signed=False)
            self.NRST_ADC_1              =  self._NRST_ADC_1(self,              Access.RW,  0x00000020,  5,   signed=False)
            self.NRST_ADC_2              =  self._NRST_ADC_2(self,              Access.RW,  0x00000040,  6,   signed=False)
            self.NRST_ADC_3              =  self._NRST_ADC_3(self,              Access.RW,  0x00000080,  7,   signed=False)
            self.MUX0_AUTO_CHOP_DISABLE  =  self._MUX0_AUTO_CHOP_DISABLE(self,  Access.RW,  0x00000100,  8,   signed=False)
            self.MUX1_CHOP_ENABLE        =  self._MUX1_CHOP_ENABLE(self,        Access.RW,  0x00000200,  9,   signed=False)
            self.MUX2_CHOP_ENABLE        =  self._MUX2_CHOP_ENABLE(self,        Access.RW,  0x00000400,  10,  signed=False)
            self.MUX3_CHOP_ENABLE        =  self._MUX3_CHOP_ENABLE(self,        Access.RW,  0x00000800,  11,  signed=False)
            self.AZ23CM_CHOP_ENABLE      =  self._AZ23CM_CHOP_ENABLE(self,      Access.RW,  0x00001000,  12,  signed=False)
            self.AZ_CHOP_ENABLE          =  self._AZ_CHOP_ENABLE(self,          Access.RW,  0x00002000,  13,  signed=False)
            self.EXT_ADC_AUTO_PROT       =  self._EXT_ADC_AUTO_PROT(self,       Access.RW,  0x00004000,  14,  signed=False)
            self.MMU_ENABLE              =  self._MMU_ENABLE(self,              Access.RW,  0x00008000,  15,  signed=False)
            self.ADC_SHIFT_SAMPLE        =  self._ADC_SHIFT_SAMPLE(self,        Access.RW,  0x000F0000,  16,  signed=False)
            self.ADC4_OV_MSKI            =  self._ADC4_OV_MSKI(self,            Access.RW,  0x00100000,  20,  signed=False)
            self.ADC5_OV_MSKI            =  self._ADC5_OV_MSKI(self,            Access.RW,  0x00200000,  21,  signed=False)
            self.ADC6_OV_MSKI            =  self._ADC6_OV_MSKI(self,            Access.RW,  0x00400000,  22,  signed=False)
            self.ADC7_OV_MSKI            =  self._ADC7_OV_MSKI(self,            Access.RW,  0x00800000,  23,  signed=False)
            self.HALF_WAKEUP_FREQ        =  self._HALF_WAKEUP_FREQ(self,        Access.RW,  0x01000000,  24,  signed=False)

    class _ADC_RD_DATA(Register):

        class _DATA_ADC_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_ADC_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DATA_ADC_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_ADC_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DATA_ADC_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_ADC_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DATA_ADC_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_ADC_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_RD_DATA", parent, access, address, block, signed)
            self.DATA_ADC_0  =  self._DATA_ADC_0(self,  Access.R,  0x000000FF,  0,   signed=False)
            self.DATA_ADC_1  =  self._DATA_ADC_1(self,  Access.R,  0x0000FF00,  8,   signed=False)
            self.DATA_ADC_2  =  self._DATA_ADC_2(self,  Access.R,  0x00FF0000,  16,  signed=False)
            self.DATA_ADC_3  =  self._DATA_ADC_3(self,  Access.R,  0xFF000000,  24,  signed=False)

    class _ADC_VERSION(Register):

        class _VERSION_NUMBER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VERSION_NUMBER", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_VERSION", parent, access, address, block, signed)
            self.VERSION_NUMBER  =  self._VERSION_NUMBER(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _ADC_STATUS(Register):

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

        class _ADC4_OV_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC4_OV_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC5_OV_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC5_OV_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC6_OV_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC6_OV_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC7_OV_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC7_OV_FLAG", parent, access, mask, shift, signed=signed)

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
            super().__init__("ADC_STATUS", parent, access, address, block, signed)
            self.RDY_ADC_0         =  self._RDY_ADC_0(self,         Access.R,  0x00000001,  0,   signed=False)
            self.RDY_ADC_1         =  self._RDY_ADC_1(self,         Access.R,  0x00000002,  1,   signed=False)
            self.RDY_ADC_2         =  self._RDY_ADC_2(self,         Access.R,  0x00000004,  2,   signed=False)
            self.RDY_ADC_3         =  self._RDY_ADC_3(self,         Access.R,  0x00000008,  3,   signed=False)
            self.ADC4_OV_FLAG      =  self._ADC4_OV_FLAG(self,      Access.R,  0x00000010,  4,   signed=False)
            self.ADC5_OV_FLAG      =  self._ADC5_OV_FLAG(self,      Access.R,  0x00000020,  5,   signed=False)
            self.ADC6_OV_FLAG      =  self._ADC6_OV_FLAG(self,      Access.R,  0x00000040,  6,   signed=False)
            self.ADC7_OV_FLAG      =  self._ADC7_OV_FLAG(self,      Access.R,  0x00000080,  7,   signed=False)
            self.ADC0_WTCHDG_FAIL  =  self._ADC0_WTCHDG_FAIL(self,  Access.R,  0x00000100,  8,   signed=False)
            self.ADC1_WTCHDG_FAIL  =  self._ADC1_WTCHDG_FAIL(self,  Access.R,  0x00000200,  9,   signed=False)
            self.ADC2_WTCHDG_FAIL  =  self._ADC2_WTCHDG_FAIL(self,  Access.R,  0x00000400,  10,  signed=False)
            self.ADC3_WTCHDG_FAIL  =  self._ADC3_WTCHDG_FAIL(self,  Access.R,  0x00000800,  11,  signed=False)
            self.ADC0_MUXSEQ_FAIL  =  self._ADC0_MUXSEQ_FAIL(self,  Access.R,  0x00001000,  12,  signed=False)
            self.ADC1_MUXSEQ_FAIL  =  self._ADC1_MUXSEQ_FAIL(self,  Access.R,  0x00002000,  13,  signed=False)
            self.ADC2_MUXSEQ_FAIL  =  self._ADC2_MUXSEQ_FAIL(self,  Access.R,  0x00004000,  14,  signed=False)
            self.ADC3_MUXSEQ_FAIL  =  self._ADC3_MUXSEQ_FAIL(self,  Access.R,  0x00008000,  15,  signed=False)

    class _CSA_AZ_VALS(Register):

        class _CSA_AZ_OFS_VALUES(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA_AZ_OFS_VALUES", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("CSA_AZ_VALS", parent, access, address, block, signed)
            self.CSA_AZ_OFS_VALUES  =  self._CSA_AZ_OFS_VALUES(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

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

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA012_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA012_BYPASS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA012_BYPASS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA3_GAIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA3_BYPASS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_BYPASS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA012_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA012_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA3_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA3_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA_AZ_FLTLNGTH_EXP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA_AZ_FLTLNGTH_EXP", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA_SLCT_AZ_VALS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA_SLCT_AZ_VALS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ_SLCT_AZ_VALS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ_SLCT_AZ_VALS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA_AZ_TIME(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA_AZ_TIME", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CSA_ADC_TRIG_BLK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA_ADC_TRIG_BLK", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("CSA_SETUP", parent, access, address, block, signed)
            self.CSA0_EN              =  self._CSA0_EN(self,              Access.RW,  0x00000001,  0,   signed=False)
            self.CSA1_EN              =  self._CSA1_EN(self,              Access.RW,  0x00000002,  1,   signed=False)
            self.CSA2_EN              =  self._CSA2_EN(self,              Access.RW,  0x00000004,  2,   signed=False)
            self.CSA3_EN              =  self._CSA3_EN(self,              Access.RW,  0x00000008,  3,   signed=False)
            self.CSA012_GAIN          =  self._CSA012_GAIN(self,          Access.RW,  0x00000030,  4,   signed=False)
            self.CSA012_BYPASS        =  self._CSA012_BYPASS(self,        Access.RW,  0x00000040,  6,   signed=False)
            self.CSA3_GAIN            =  self._CSA3_GAIN(self,            Access.RW,  0x00000300,  8,   signed=False)
            self.CSA3_BYPASS          =  self._CSA3_BYPASS(self,          Access.RW,  0x00000400,  10,  signed=False)
            self.CSA012_FILT          =  self._CSA012_FILT(self,          Access.RW,  0x00003000,  12,  signed=False)
            self.CSA3_FILT            =  self._CSA3_FILT(self,            Access.RW,  0x0000C000,  14,  signed=False)
            self.CSA_AZ_FLTLNGTH_EXP  =  self._CSA_AZ_FLTLNGTH_EXP(self,  Access.RW,  0x000F0000,  16,  signed=False)
            self.CSA_SLCT_AZ_VALS     =  self._CSA_SLCT_AZ_VALS(self,     Access.RW,  0x00300000,  20,  signed=False)
            self.AZ_SLCT_AZ_VALS      =  self._AZ_SLCT_AZ_VALS(self,      Access.RW,  0x00C00000,  22,  signed=False)
            self.CSA_AZ_TIME          =  self._CSA_AZ_TIME(self,          Access.RW,  0x07000000,  24,  signed=False)
            self.CSA_ADC_TRIG_BLK     =  self._CSA_ADC_TRIG_BLK(self,     Access.RW,  0x70000000,  28,  signed=False)

    class _CSA0_CONFIG(Register):

        class _OFSL0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSL0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSM0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSM0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSH0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSH0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFS_READY0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFS_READY0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFS_READY_FRC0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFS_READY_FRC0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_CMR0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_CMR0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_OFS0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_OFS0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSCSA_EN0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSCSA_EN0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSADC_EN0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSADC_EN0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ2_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ2_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ3_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ3_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZCM_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZCM_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CALIB_EN0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CALIB_EN0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _NVALID0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NVALID0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TRIG0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRIG0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("CSA0_CONFIG", parent, access, address, block, signed)
            self.OFSL0           =  self._OFSL0(self,           Access.RW,  0x0000003F,  0,   signed=False)
            self.OFSM0           =  self._OFSM0(self,           Access.RW,  0x00000FC0,  6,   signed=False)
            self.OFSH0           =  self._OFSH0(self,           Access.RW,  0x0003F000,  12,  signed=False)
            self.OFS_READY0      =  self._OFS_READY0(self,      Access.R,   0x00040000,  18,  signed=False)
            self.OFS_READY_FRC0  =  self._OFS_READY_FRC0(self,  Access.RW,  0x00080000,  19,  signed=False)
            self.SKIP_CMR0       =  self._SKIP_CMR0(self,       Access.RW,  0x00100000,  20,  signed=False)
            self.SKIP_OFS0       =  self._SKIP_OFS0(self,       Access.RW,  0x00200000,  21,  signed=False)
            self.OFSCSA_EN0      =  self._OFSCSA_EN0(self,      Access.RW,  0x00400000,  22,  signed=False)
            self.OFSADC_EN0      =  self._OFSADC_EN0(self,      Access.RW,  0x00800000,  23,  signed=False)
            self.AZ_0            =  self._AZ_0(self,            Access.RW,  0x01000000,  24,  signed=False)
            self.AZ2_0           =  self._AZ2_0(self,           Access.RW,  0x02000000,  25,  signed=False)
            self.AZ3_0           =  self._AZ3_0(self,           Access.RW,  0x04000000,  26,  signed=False)
            self.AZCM_0          =  self._AZCM_0(self,          Access.RW,  0x08000000,  27,  signed=False)
            self.CALIB_EN0       =  self._CALIB_EN0(self,       Access.RW,  0x10000000,  28,  signed=False)
            self.NVALID0         =  self._NVALID0(self,         Access.R,   0x40000000,  30,  signed=False)
            self.TRIG0           =  self._TRIG0(self,           Access.RW,  0x80000000,  31,  signed=False)

    class _CSA1_CONFIG(Register):

        class _OFSL1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSL1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSM1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSM1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSH1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSH1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFS_READY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFS_READY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFS_READY_FRC1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFS_READY_FRC1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_CMR1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_CMR1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_OFS1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_OFS1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSCSA_EN1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSCSA_EN1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSADC_EN1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSADC_EN1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ2_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ2_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ3_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ3_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZCM_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZCM_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CALIB_EN1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CALIB_EN1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _NVALID1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NVALID1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TRIG1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRIG1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("CSA1_CONFIG", parent, access, address, block, signed)
            self.OFSL1           =  self._OFSL1(self,           Access.RW,  0x0000003F,  0,   signed=False)
            self.OFSM1           =  self._OFSM1(self,           Access.RW,  0x00000FC0,  6,   signed=False)
            self.OFSH1           =  self._OFSH1(self,           Access.RW,  0x0003F000,  12,  signed=False)
            self.OFS_READY1      =  self._OFS_READY1(self,      Access.R,   0x00040000,  18,  signed=False)
            self.OFS_READY_FRC1  =  self._OFS_READY_FRC1(self,  Access.RW,  0x00080000,  19,  signed=False)
            self.SKIP_CMR1       =  self._SKIP_CMR1(self,       Access.RW,  0x00100000,  20,  signed=False)
            self.SKIP_OFS1       =  self._SKIP_OFS1(self,       Access.RW,  0x00200000,  21,  signed=False)
            self.OFSCSA_EN1      =  self._OFSCSA_EN1(self,      Access.RW,  0x00400000,  22,  signed=False)
            self.OFSADC_EN1      =  self._OFSADC_EN1(self,      Access.RW,  0x00800000,  23,  signed=False)
            self.AZ_1            =  self._AZ_1(self,            Access.RW,  0x01000000,  24,  signed=False)
            self.AZ2_1           =  self._AZ2_1(self,           Access.RW,  0x02000000,  25,  signed=False)
            self.AZ3_1           =  self._AZ3_1(self,           Access.RW,  0x04000000,  26,  signed=False)
            self.AZCM_1          =  self._AZCM_1(self,          Access.RW,  0x08000000,  27,  signed=False)
            self.CALIB_EN1       =  self._CALIB_EN1(self,       Access.RW,  0x10000000,  28,  signed=False)
            self.NVALID1         =  self._NVALID1(self,         Access.R,   0x40000000,  30,  signed=False)
            self.TRIG1           =  self._TRIG1(self,           Access.RW,  0x80000000,  31,  signed=False)

    class _CSA2_CONFIG(Register):

        class _OFSL2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSL2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSM2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSM2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSH2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSH2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFS_READY2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFS_READY2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFS_READY_FRC2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFS_READY_FRC2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_CMR2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_CMR2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_OFS2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_OFS2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSCSA_EN2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSCSA_EN2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSADC_EN2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSADC_EN2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ2_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ2_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ3_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ3_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZCM_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZCM_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CALIB_EN2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CALIB_EN2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _NVALID2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NVALID2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TRIG2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRIG2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("CSA2_CONFIG", parent, access, address, block, signed)
            self.OFSL2           =  self._OFSL2(self,           Access.RW,  0x0000003F,  0,   signed=False)
            self.OFSM2           =  self._OFSM2(self,           Access.RW,  0x00000FC0,  6,   signed=False)
            self.OFSH2           =  self._OFSH2(self,           Access.RW,  0x0003F000,  12,  signed=False)
            self.OFS_READY2      =  self._OFS_READY2(self,      Access.R,   0x00040000,  18,  signed=False)
            self.OFS_READY_FRC2  =  self._OFS_READY_FRC2(self,  Access.RW,  0x00080000,  19,  signed=False)
            self.SKIP_CMR2       =  self._SKIP_CMR2(self,       Access.RW,  0x00100000,  20,  signed=False)
            self.SKIP_OFS2       =  self._SKIP_OFS2(self,       Access.RW,  0x00200000,  21,  signed=False)
            self.OFSCSA_EN2      =  self._OFSCSA_EN2(self,      Access.RW,  0x00400000,  22,  signed=False)
            self.OFSADC_EN2      =  self._OFSADC_EN2(self,      Access.RW,  0x00800000,  23,  signed=False)
            self.AZ_2            =  self._AZ_2(self,            Access.RW,  0x01000000,  24,  signed=False)
            self.AZ2_2           =  self._AZ2_2(self,           Access.RW,  0x02000000,  25,  signed=False)
            self.AZ3_2           =  self._AZ3_2(self,           Access.RW,  0x04000000,  26,  signed=False)
            self.AZCM_2          =  self._AZCM_2(self,          Access.RW,  0x08000000,  27,  signed=False)
            self.CALIB_EN2       =  self._CALIB_EN2(self,       Access.RW,  0x10000000,  28,  signed=False)
            self.NVALID2         =  self._NVALID2(self,         Access.R,   0x40000000,  30,  signed=False)
            self.TRIG2           =  self._TRIG2(self,           Access.RW,  0x80000000,  31,  signed=False)

    class _CSA3_CONFIG(Register):

        class _OFSL3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSL3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSM3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSM3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSH3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSH3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFS_READY3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFS_READY3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFS_READY_FRC3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFS_READY_FRC3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_CMR3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_CMR3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_OFS3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_OFS3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSCSA_EN3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSCSA_EN3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OFSADC_EN3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFSADC_EN3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ2_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ2_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZ3_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZ3_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AZCM_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AZCM_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CALIB_EN3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CALIB_EN3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _NVALID3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NVALID3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TRIG3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRIG3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("CSA3_CONFIG", parent, access, address, block, signed)
            self.OFSL3           =  self._OFSL3(self,           Access.RW,  0x0000003F,  0,   signed=False)
            self.OFSM3           =  self._OFSM3(self,           Access.RW,  0x00000FC0,  6,   signed=False)
            self.OFSH3           =  self._OFSH3(self,           Access.RW,  0x0003F000,  12,  signed=False)
            self.OFS_READY3      =  self._OFS_READY3(self,      Access.R,   0x00040000,  18,  signed=False)
            self.OFS_READY_FRC3  =  self._OFS_READY_FRC3(self,  Access.RW,  0x00080000,  19,  signed=False)
            self.SKIP_CMR3       =  self._SKIP_CMR3(self,       Access.RW,  0x00100000,  20,  signed=False)
            self.SKIP_OFS3       =  self._SKIP_OFS3(self,       Access.RW,  0x00200000,  21,  signed=False)
            self.OFSCSA_EN3      =  self._OFSCSA_EN3(self,      Access.RW,  0x00400000,  22,  signed=False)
            self.OFSADC_EN3      =  self._OFSADC_EN3(self,      Access.RW,  0x00800000,  23,  signed=False)
            self.AZ_3            =  self._AZ_3(self,            Access.RW,  0x01000000,  24,  signed=False)
            self.AZ2_3           =  self._AZ2_3(self,           Access.RW,  0x02000000,  25,  signed=False)
            self.AZ3_3           =  self._AZ3_3(self,           Access.RW,  0x04000000,  26,  signed=False)
            self.AZCM_3          =  self._AZCM_3(self,          Access.RW,  0x08000000,  27,  signed=False)
            self.CALIB_EN3       =  self._CALIB_EN3(self,       Access.RW,  0x10000000,  28,  signed=False)
            self.NVALID3         =  self._NVALID3(self,         Access.R,   0x40000000,  30,  signed=False)
            self.TRIG3           =  self._TRIG3(self,           Access.RW,  0x80000000,  31,  signed=False)

    class _CSA1_0_CMR_CFG(Register):

        class _CMRN_DAC0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRN_DAC0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRP_DAC0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRP_DAC0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRN_DAC1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRN_DAC1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRP_DAC1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRP_DAC1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("CSA1_0_CMR_CFG", parent, access, address, block, signed)
            self.CMRN_DAC0  =  self._CMRN_DAC0(self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.CMRP_DAC0  =  self._CMRP_DAC0(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.CMRN_DAC1  =  self._CMRN_DAC1(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.CMRP_DAC1  =  self._CMRP_DAC1(self,  Access.RW,  0xFF000000,  24,  signed=False)

    class _CSA3_2_CMR_CFG(Register):

        class _CMRN_DAC2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRN_DAC2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRP_DAC2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRP_DAC2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRN_DAC3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRN_DAC3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRP_DAC3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRP_DAC3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("CSA3_2_CMR_CFG", parent, access, address, block, signed)
            self.CMRN_DAC2  =  self._CMRN_DAC2(self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.CMRP_DAC2  =  self._CMRP_DAC2(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.CMRN_DAC3  =  self._CMRN_DAC3(self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.CMRP_DAC3  =  self._CMRP_DAC3(self,  Access.RW,  0xFF000000,  24,  signed=False)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.ADC_RW_ADDR_DATA  =  self._ADC_RW_ADDR_DATA(self,  Access.RW,  0x0000,  block,  False)
        self.ADC_SRC_CONFIG    =  self._ADC_SRC_CONFIG(self,    Access.RW,  0x0001,  block,  False)
        self.ADC_SETUP         =  self._ADC_SETUP(self,         Access.RW,  0x0002,  block,  False)
        self.ADC_RD_DATA       =  self._ADC_RD_DATA(self,       Access.R,   0x0003,  block,  False)
        self.ADC_VERSION       =  self._ADC_VERSION(self,       Access.R,   0x0004,  block,  False)
        self.ADC_STATUS        =  self._ADC_STATUS(self,        Access.R,   0x0005,  block,  False)
        self.CSA_AZ_VALS       =  self._CSA_AZ_VALS(self,       Access.R,   0x0006,  block,  False)
        self.CSA_SETUP         =  self._CSA_SETUP(self,         Access.RW,  0x0007,  block,  False)
        self.CSA0_CONFIG       =  self._CSA0_CONFIG(self,       Access.RW,  0x0008,  block,  False)
        self.CSA1_CONFIG       =  self._CSA1_CONFIG(self,       Access.RW,  0x0009,  block,  False)
        self.CSA2_CONFIG       =  self._CSA2_CONFIG(self,       Access.RW,  0x000A,  block,  False)
        self.CSA3_CONFIG       =  self._CSA3_CONFIG(self,       Access.RW,  0x000B,  block,  False)
        self.CSA1_0_CMR_CFG    =  self._CSA1_0_CMR_CFG(self,    Access.RW,  0x000C,  block,  False)
        self.CSA3_2_CMR_CFG    =  self._CSA3_2_CMR_CFG(self,    Access.RW,  0x000D,  block,  False)

