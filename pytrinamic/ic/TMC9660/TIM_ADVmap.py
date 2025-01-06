################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Field, Register


class TIM_ADVMap:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)




class _ALL_REGISTERS(RegisterGroup):

    class _TIM_ADV_COUNTER0(Register):

        class _COUNTER0_VALUE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER0_VALUE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_COUNTER0", parent, access, address, block, signed)
            self.COUNTER0_VALUE  =  self._COUNTER0_VALUE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_LIMIT0(Register):

        class _COUNTER0_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER0_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_LIMIT0", parent, access, address, block, signed)
            self.COUNTER0_LIMIT  =  self._COUNTER0_LIMIT(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_CONFIG0(Register):

        class _ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DIR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UP_CLK_CFG0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UP_CLK_CFG0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UP_CLK_CFG1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UP_CLK_CFG1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UP_CLK_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UP_CLK_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DOWN_CLK_CFG0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DOWN_CLK_CFG0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DOWN_CLK_CFG1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DOWN_CLK_CFG1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DOWN_CLK_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DOWN_CLK_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RESET_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RESET_CFG_IN0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET_CFG_IN0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RESET_CFG_IN1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET_CFG_IN1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RESET_CFG_IN2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET_CFG_IN2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_CONFIG0", parent, access, address, block, signed)
            self.ENABLE           =  self._ENABLE(self,           Access.RW,  0x00000003,  0,   signed=False)
            self.DIR              =  self._DIR(self,              Access.RW,  0x00000004,  2,   signed=False)
            self.UP_CLK_CFG0      =  self._UP_CLK_CFG0(self,      Access.RW,  0x000000F0,  4,   signed=False)
            self.UP_CLK_CFG1      =  self._UP_CLK_CFG1(self,      Access.RW,  0x00000700,  8,   signed=False)
            self.UP_CLK_ENABLE    =  self._UP_CLK_ENABLE(self,    Access.RW,  0x00000800,  11,  signed=False)
            self.DOWN_CLK_CFG0    =  self._DOWN_CLK_CFG0(self,    Access.RW,  0x0000F000,  12,  signed=False)
            self.DOWN_CLK_CFG1    =  self._DOWN_CLK_CFG1(self,    Access.RW,  0x00070000,  16,  signed=False)
            self.DOWN_CLK_ENABLE  =  self._DOWN_CLK_ENABLE(self,  Access.RW,  0x00080000,  19,  signed=False)
            self.RESET_ENABLE     =  self._RESET_ENABLE(self,     Access.RW,  0x00300000,  20,  signed=False)
            self.RESET_CFG_IN0    =  self._RESET_CFG_IN0(self,    Access.RW,  0x03800000,  23,  signed=False)
            self.RESET_CFG_IN1    =  self._RESET_CFG_IN1(self,    Access.RW,  0x1C000000,  26,  signed=False)
            self.RESET_CFG_IN2    =  self._RESET_CFG_IN2(self,    Access.RW,  0xE0000000,  29,  signed=False)

    class _TIM_ADV_COUNTER1(Register):

        class _COUNTER1_VALUE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER1_VALUE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_COUNTER1", parent, access, address, block, signed)
            self.COUNTER1_VALUE  =  self._COUNTER1_VALUE(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_LIMIT1(Register):

        class _COUNTER1_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER1_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_LIMIT1", parent, access, address, block, signed)
            self.COUNTER1_LIMIT  =  self._COUNTER1_LIMIT(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_CONFIG1(Register):

        class _ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLK_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RESET_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_CONFIG1", parent, access, address, block, signed)
            self.ENABLE        =  self._ENABLE(self,        Access.RW,  0x00000007,  0,  signed=False)
            self.CLK_CFG       =  self._CLK_CFG(self,       Access.RW,  0x00000018,  3,  signed=False)
            self.RESET_ENABLE  =  self._RESET_ENABLE(self,  Access.RW,  0x00000060,  5,  signed=False)

    class _TIM_ADV_COUNTER2(Register):

        class _COUNTER2_VALUE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER2_VALUE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_COUNTER2", parent, access, address, block, signed)
            self.COUNTER2_VALUE  =  self._COUNTER2_VALUE(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_LIMIT2(Register):

        class _COUNTER2_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER2_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_LIMIT2", parent, access, address, block, signed)
            self.COUNTER2_LIMIT  =  self._COUNTER2_LIMIT(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_CONFIG2(Register):

        class _ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLK_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_CONFIG2", parent, access, address, block, signed)
            self.ENABLE   =  self._ENABLE(self,   Access.RW,  0x00000007,  0,  signed=False)
            self.CLK_CFG  =  self._CLK_CFG(self,  Access.RW,  0x00000018,  3,  signed=False)

    class _TIM_ADV_CAPTURE0(Register):

        class _CAPTURE0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_CAPTURE0", parent, access, address, block, signed)
            self.CAPTURE0  =  self._CAPTURE0(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_CAPTURE1(Register):

        class _CAPTURE1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_CAPTURE1", parent, access, address, block, signed)
            self.CAPTURE1  =  self._CAPTURE1(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_CAPTURE2(Register):

        class _CAPTURE2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_CAPTURE2", parent, access, address, block, signed)
            self.CAPTURE2  =  self._CAPTURE2(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_CAPTURE_CONFIG(Register):

        class _CAPTURE0_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE0_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE0_IN0_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE0_IN0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE0_IN1_LEVEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE0_IN1_LEVEL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE0_IN1_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE0_IN1_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE0_IN2_LEVEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE0_IN2_LEVEL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE0_IN2_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE0_IN2_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE1_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE1_IN1_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1_IN1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE1_IN0_LEVEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1_IN0_LEVEL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE1_IN0_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1_IN0_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE1_IN2_LEVEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1_IN2_LEVEL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE1_IN2_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1_IN2_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE2_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE2_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE2_IN2_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE2_IN2_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE2_IN0_LEVEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE2_IN0_LEVEL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE2_IN0_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE2_IN0_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE2_IN1_LEVEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE2_IN1_LEVEL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE2_IN1_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE2_IN1_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE1_COUNTER1_RESET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1_COUNTER1_RESET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_CAPTURE_CONFIG", parent, access, address, block, signed)
            self.CAPTURE0_ENABLE          =  self._CAPTURE0_ENABLE(self,          Access.RW,  0x00000003,  0,   signed=False)
            self.CAPTURE0_IN0_CFG         =  self._CAPTURE0_IN0_CFG(self,         Access.RW,  0x0000000C,  2,   signed=False)
            self.CAPTURE0_IN1_LEVEL       =  self._CAPTURE0_IN1_LEVEL(self,       Access.RW,  0x00000010,  4,   signed=False)
            self.CAPTURE0_IN1_EN          =  self._CAPTURE0_IN1_EN(self,          Access.RW,  0x00000020,  5,   signed=False)
            self.CAPTURE0_IN2_LEVEL       =  self._CAPTURE0_IN2_LEVEL(self,       Access.RW,  0x00000040,  6,   signed=False)
            self.CAPTURE0_IN2_EN          =  self._CAPTURE0_IN2_EN(self,          Access.RW,  0x00000080,  7,   signed=False)
            self.CAPTURE1_ENABLE          =  self._CAPTURE1_ENABLE(self,          Access.RW,  0x00000300,  8,   signed=False)
            self.CAPTURE1_IN1_CFG         =  self._CAPTURE1_IN1_CFG(self,         Access.RW,  0x00000C00,  10,  signed=False)
            self.CAPTURE1_IN0_LEVEL       =  self._CAPTURE1_IN0_LEVEL(self,       Access.RW,  0x00001000,  12,  signed=False)
            self.CAPTURE1_IN0_EN          =  self._CAPTURE1_IN0_EN(self,          Access.RW,  0x00002000,  13,  signed=False)
            self.CAPTURE1_IN2_LEVEL       =  self._CAPTURE1_IN2_LEVEL(self,       Access.RW,  0x00004000,  14,  signed=False)
            self.CAPTURE1_IN2_EN          =  self._CAPTURE1_IN2_EN(self,          Access.RW,  0x00008000,  15,  signed=False)
            self.CAPTURE2_ENABLE          =  self._CAPTURE2_ENABLE(self,          Access.RW,  0x00030000,  16,  signed=False)
            self.CAPTURE2_IN2_CFG         =  self._CAPTURE2_IN2_CFG(self,         Access.RW,  0x000C0000,  18,  signed=False)
            self.CAPTURE2_IN0_LEVEL       =  self._CAPTURE2_IN0_LEVEL(self,       Access.RW,  0x00100000,  20,  signed=False)
            self.CAPTURE2_IN0_EN          =  self._CAPTURE2_IN0_EN(self,          Access.RW,  0x00200000,  21,  signed=False)
            self.CAPTURE2_IN1_LEVEL       =  self._CAPTURE2_IN1_LEVEL(self,       Access.RW,  0x00400000,  22,  signed=False)
            self.CAPTURE2_IN1_EN          =  self._CAPTURE2_IN1_EN(self,          Access.RW,  0x00800000,  23,  signed=False)
            self.CAPTURE1_COUNTER1_RESET  =  self._CAPTURE1_COUNTER1_RESET(self,  Access.RW,  0x01000000,  24,  signed=False)

    class _TIM_ADV_COMPARE0(Register):

        class _COMPARE0_VALUE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMPARE0_VALUE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_COMPARE0", parent, access, address, block, signed)
            self.COMPARE0_VALUE  =  self._COMPARE0_VALUE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_COMPARE1(Register):

        class _COMPARE1_VALUE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMPARE1_VALUE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_COMPARE1", parent, access, address, block, signed)
            self.COMPARE1_VALUE  =  self._COMPARE1_VALUE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _TIM_ADV_OUT_CONFIG(Register):

        class _OUT0_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT0_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OUT0_COUNTER0_OVERFLOW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT0_COUNTER0_OVERFLOW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OUT0_COMPARE0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT0_COMPARE0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OUT0_COMPARE1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT0_COMPARE1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OUT0_COUNTER1_OVERFLOW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT0_COUNTER1_OVERFLOW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OUT1_CFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT1_CFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OUT1_COUNTER0_OVERFLOW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT1_COUNTER0_OVERFLOW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OUT1_COMPARE0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT1_COMPARE0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OUT1_COMPARE1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT1_COMPARE1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OUT1_COUNTER2_OVERFLOW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OUT1_COUNTER2_OVERFLOW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_OUT_CONFIG", parent, access, address, block, signed)
            self.OUT0_CFG                =  self._OUT0_CFG(self,                Access.RW,  0x00000007,  0,   signed=False)
            self.OUT0_COUNTER0_OVERFLOW  =  self._OUT0_COUNTER0_OVERFLOW(self,  Access.RW,  0x00000018,  3,   signed=False)
            self.OUT0_COMPARE0           =  self._OUT0_COMPARE0(self,           Access.RW,  0x00000060,  5,   signed=False)
            self.OUT0_COMPARE1           =  self._OUT0_COMPARE1(self,           Access.RW,  0x00000180,  7,   signed=False)
            self.OUT0_COUNTER1_OVERFLOW  =  self._OUT0_COUNTER1_OVERFLOW(self,  Access.RW,  0x00000600,  9,   signed=False)
            self.OUT1_CFG                =  self._OUT1_CFG(self,                Access.RW,  0x00003800,  11,  signed=False)
            self.OUT1_COUNTER0_OVERFLOW  =  self._OUT1_COUNTER0_OVERFLOW(self,  Access.RW,  0x0000C000,  14,  signed=False)
            self.OUT1_COMPARE0           =  self._OUT1_COMPARE0(self,           Access.RW,  0x00030000,  16,  signed=False)
            self.OUT1_COMPARE1           =  self._OUT1_COMPARE1(self,           Access.RW,  0x000C0000,  18,  signed=False)
            self.OUT1_COUNTER2_OVERFLOW  =  self._OUT1_COUNTER2_OVERFLOW(self,  Access.RW,  0x00300000,  20,  signed=False)

    class _TIM_ADV_IN_CONFIG(Register):

        class _IN0_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IN0_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IN0_FILTER_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IN0_FILTER_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IN1_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IN1_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IN1_FILTER_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IN1_FILTER_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IN1_USE_IN0_INSTEAD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IN1_USE_IN0_INSTEAD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IN2_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IN2_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IN2_FILTER_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IN2_FILTER_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SAMPLE_RATE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SAMPLE_RATE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_IN_CONFIG", parent, access, address, block, signed)
            self.IN0_EN               =  self._IN0_EN(self,               Access.RW,  0x00000001,  0,  signed=False)
            self.IN0_FILTER_EN        =  self._IN0_FILTER_EN(self,        Access.RW,  0x00000002,  1,  signed=False)
            self.IN1_EN               =  self._IN1_EN(self,               Access.RW,  0x00000004,  2,  signed=False)
            self.IN1_FILTER_EN        =  self._IN1_FILTER_EN(self,        Access.RW,  0x00000008,  3,  signed=False)
            self.IN1_USE_IN0_INSTEAD  =  self._IN1_USE_IN0_INSTEAD(self,  Access.RW,  0x00000010,  4,  signed=False)
            self.IN2_EN               =  self._IN2_EN(self,               Access.RW,  0x00000020,  5,  signed=False)
            self.IN2_FILTER_EN        =  self._IN2_FILTER_EN(self,        Access.RW,  0x00000040,  6,  signed=False)
            self.SAMPLE_RATE          =  self._SAMPLE_RATE(self,          Access.RW,  0x00000380,  7,  signed=False)

    class _TIM_ADV_IRQ_CTRL(Register):

        class _COUNTER0_OVERFLOW_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER0_OVERFLOW_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER1_OVERFLOW_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER1_OVERFLOW_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER2_OVERFLOW_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER2_OVERFLOW_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER0_STOPPED_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER0_STOPPED_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER1_STOPPED_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER1_STOPPED_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER2_STOPPED_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER2_STOPPED_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE0_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE0_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE1_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE2_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE2_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COMPARE0_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMPARE0_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COMPARE1_INT_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMPARE1_INT_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_IRQ_CTRL", parent, access, address, block, signed)
            self.COUNTER0_OVERFLOW_INT_EN  =  self._COUNTER0_OVERFLOW_INT_EN(self,  Access.RW,  0x00000001,  0,   signed=False)
            self.COUNTER1_OVERFLOW_INT_EN  =  self._COUNTER1_OVERFLOW_INT_EN(self,  Access.RW,  0x00000002,  1,   signed=False)
            self.COUNTER2_OVERFLOW_INT_EN  =  self._COUNTER2_OVERFLOW_INT_EN(self,  Access.RW,  0x00000004,  2,   signed=False)
            self.COUNTER0_STOPPED_INT_EN   =  self._COUNTER0_STOPPED_INT_EN(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.COUNTER1_STOPPED_INT_EN   =  self._COUNTER1_STOPPED_INT_EN(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.COUNTER2_STOPPED_INT_EN   =  self._COUNTER2_STOPPED_INT_EN(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.CAPTURE0_INT_EN           =  self._CAPTURE0_INT_EN(self,           Access.RW,  0x00000040,  6,   signed=False)
            self.CAPTURE1_INT_EN           =  self._CAPTURE1_INT_EN(self,           Access.RW,  0x00000080,  7,   signed=False)
            self.CAPTURE2_INT_EN           =  self._CAPTURE2_INT_EN(self,           Access.RW,  0x00000100,  8,   signed=False)
            self.COMPARE0_INT_EN           =  self._COMPARE0_INT_EN(self,           Access.RW,  0x00000200,  9,   signed=False)
            self.COMPARE1_INT_EN           =  self._COMPARE1_INT_EN(self,           Access.RW,  0x00000400,  10,  signed=False)

    class _TIM_ADV_STATUS(Register):

        class _COUNTER0_OVERFLOW_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER0_OVERFLOW_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER1_OVERFLOW_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER1_OVERFLOW_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER2_OVERFLOW_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER2_OVERFLOW_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER0_STOPPED_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER0_STOPPED_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER1_STOPPED_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER1_STOPPED_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COUNTER2_STOPPED_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER2_STOPPED_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE0_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE0_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE1_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE1_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CAPTURE2_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CAPTURE2_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COMPARE0_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMPARE0_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COMPARE1_FLAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMPARE1_FLAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("TIM_ADV_STATUS", parent, access, address, block, signed)
            self.COUNTER0_OVERFLOW_FLAG  =  self._COUNTER0_OVERFLOW_FLAG(self,  Access.RWC,  0x00000001,  0,   signed=False)
            self.COUNTER1_OVERFLOW_FLAG  =  self._COUNTER1_OVERFLOW_FLAG(self,  Access.RWC,  0x00000002,  1,   signed=False)
            self.COUNTER2_OVERFLOW_FLAG  =  self._COUNTER2_OVERFLOW_FLAG(self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.COUNTER0_STOPPED_FLAG   =  self._COUNTER0_STOPPED_FLAG(self,   Access.RWC,  0x00000008,  3,   signed=False)
            self.COUNTER1_STOPPED_FLAG   =  self._COUNTER1_STOPPED_FLAG(self,   Access.RWC,  0x00000010,  4,   signed=False)
            self.COUNTER2_STOPPED_FLAG   =  self._COUNTER2_STOPPED_FLAG(self,   Access.RWC,  0x00000020,  5,   signed=False)
            self.CAPTURE0_FLAG           =  self._CAPTURE0_FLAG(self,           Access.RWC,  0x00000040,  6,   signed=False)
            self.CAPTURE1_FLAG           =  self._CAPTURE1_FLAG(self,           Access.RWC,  0x00000080,  7,   signed=False)
            self.CAPTURE2_FLAG           =  self._CAPTURE2_FLAG(self,           Access.RWC,  0x00000100,  8,   signed=False)
            self.COMPARE0_FLAG           =  self._COMPARE0_FLAG(self,           Access.RWC,  0x00000200,  9,   signed=False)
            self.COMPARE1_FLAG           =  self._COMPARE1_FLAG(self,           Access.RWC,  0x00000400,  10,  signed=False)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.TIM_ADV_COUNTER0        =  self._TIM_ADV_COUNTER0(self,        Access.RW,   0x0000,  block,  False)
        self.TIM_ADV_LIMIT0          =  self._TIM_ADV_LIMIT0(self,          Access.RW,   0x0001,  block,  False)
        self.TIM_ADV_CONFIG0         =  self._TIM_ADV_CONFIG0(self,         Access.RW,   0x0002,  block,  False)
        self.TIM_ADV_COUNTER1        =  self._TIM_ADV_COUNTER1(self,        Access.R,    0x0003,  block,  False)
        self.TIM_ADV_LIMIT1          =  self._TIM_ADV_LIMIT1(self,          Access.RW,   0x0004,  block,  False)
        self.TIM_ADV_CONFIG1         =  self._TIM_ADV_CONFIG1(self,         Access.RW,   0x0005,  block,  False)
        self.TIM_ADV_COUNTER2        =  self._TIM_ADV_COUNTER2(self,        Access.R,    0x0006,  block,  False)
        self.TIM_ADV_LIMIT2          =  self._TIM_ADV_LIMIT2(self,          Access.RW,   0x0007,  block,  False)
        self.TIM_ADV_CONFIG2         =  self._TIM_ADV_CONFIG2(self,         Access.RW,   0x0008,  block,  False)
        self.TIM_ADV_CAPTURE0        =  self._TIM_ADV_CAPTURE0(self,        Access.R,    0x0009,  block,  False)
        self.TIM_ADV_CAPTURE1        =  self._TIM_ADV_CAPTURE1(self,        Access.R,    0x000A,  block,  False)
        self.TIM_ADV_CAPTURE2        =  self._TIM_ADV_CAPTURE2(self,        Access.R,    0x000B,  block,  False)
        self.TIM_ADV_CAPTURE_CONFIG  =  self._TIM_ADV_CAPTURE_CONFIG(self,  Access.RW,   0x000C,  block,  False)
        self.TIM_ADV_COMPARE0        =  self._TIM_ADV_COMPARE0(self,        Access.RW,   0x000D,  block,  False)
        self.TIM_ADV_COMPARE1        =  self._TIM_ADV_COMPARE1(self,        Access.RW,   0x000E,  block,  False)
        self.TIM_ADV_OUT_CONFIG      =  self._TIM_ADV_OUT_CONFIG(self,      Access.RW,   0x000F,  block,  False)
        self.TIM_ADV_IN_CONFIG       =  self._TIM_ADV_IN_CONFIG(self,       Access.RW,   0x0010,  block,  False)
        self.TIM_ADV_IRQ_CTRL        =  self._TIM_ADV_IRQ_CTRL(self,        Access.RW,   0x0011,  block,  False)
        self.TIM_ADV_STATUS          =  self._TIM_ADV_STATUS(self,          Access.RWC,  0x0012,  block,  False)

