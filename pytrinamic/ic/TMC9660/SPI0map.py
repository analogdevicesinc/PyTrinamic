################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Field, Register


class SPI0Map:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)




class _ALL_REGISTERS(RegisterGroup):

    class _SPI0_STATUS(Register):

        class _TRANSACT_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRANSACT_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TRANSACT_STARTED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRANSACT_STARTED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TRANSACT_DONE_SINCE_STATUS_CLR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRANSACT_DONE_SINCE_STATUS_CLR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BUSY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BUSY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BUSY2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BUSY2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CONT_ON(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CONT_ON", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RX_CORK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RX_CORK", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_STATUS", parent, access, address, block, signed)
            self.TRANSACT_DONE                   =  self._TRANSACT_DONE(self,                   Access.R,    0x00000001,  0,  signed=False)
            self.TRANSACT_STARTED                =  self._TRANSACT_STARTED(self,                Access.R,    0x00000002,  1,  signed=False)
            self.TRANSACT_DONE_SINCE_STATUS_CLR  =  self._TRANSACT_DONE_SINCE_STATUS_CLR(self,  Access.RWC,  0x00000004,  2,  signed=False)
            self.BUSY1                           =  self._BUSY1(self,                           Access.R,    0x00000008,  3,  signed=False)
            self.BUSY2                           =  self._BUSY2(self,                           Access.R,    0x00000010,  4,  signed=False)
            self.CONT_ON                         =  self._CONT_ON(self,                         Access.R,    0x00000020,  5,  signed=False)
            self.RX_CORK                         =  self._RX_CORK(self,                         Access.RWC,  0x00000040,  6,  signed=False)

    class _SPI0_GEN_CONFIG(Register):

        class _ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CONFIG_SEL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CONFIG_SEL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _START_NSTOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("START_NSTOP", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _START_PULSE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("START_PULSE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _READ_REQUEST(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("READ_REQUEST", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _READ_REQUEST_CLR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("READ_REQUEST_CLR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_GEN_CONFIG", parent, access, address, block, signed)
            self.ENABLE            =  self._ENABLE(self,            Access.RW,  0x00000001,  0,  signed=False)
            self.CONFIG_SEL        =  self._CONFIG_SEL(self,        Access.RW,  0x00000006,  1,  signed=False)
            self.START_NSTOP       =  self._START_NSTOP(self,       Access.RW,  0x00000008,  3,  signed=False)
            self.START_PULSE       =  self._START_PULSE(self,       Access.RW,  0x00000010,  4,  signed=False)
            self.READ_REQUEST      =  self._READ_REQUEST(self,      Access.RW,  0x00000020,  5,  signed=False)
            self.READ_REQUEST_CLR  =  self._READ_REQUEST_CLR(self,  Access.RW,  0x00000040,  6,  signed=False)

    class _SPI0_SCLK_CONFIG0(Register):

        class _CLK_DIV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_DIV", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS_SETTLE_TIM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS_SETTLE_TIM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PAUSE_TIM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PAUSE_TIM", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_SCLK_CONFIG0", parent, access, address, block, signed)
            self.CLK_DIV        =  self._CLK_DIV(self,        Access.RW,  0x000000FF,  0,   signed=False)
            self.CS_SETTLE_TIM  =  self._CS_SETTLE_TIM(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.PAUSE_TIM      =  self._PAUSE_TIM(self,      Access.RW,  0x00FF0000,  16,  signed=False)

    class _SPI0_SYNC_CONFIG0(Register):

        class _STROBE_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STROBE_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SW_STROBE_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SW_STROBE_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HW_STROBE_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HW_STROBE_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEC_CYCLE_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEC_CYCLE_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_SYNC_CONFIG0", parent, access, address, block, signed)
            self.STROBE_MASK       =  self._STROBE_MASK(self,       Access.RW,  0x000001FF,  0,   signed=False)
            self.SW_STROBE_ENABLE  =  self._SW_STROBE_ENABLE(self,  Access.RW,  0x00000200,  9,   signed=False)
            self.HW_STROBE_ENABLE  =  self._HW_STROBE_ENABLE(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.SEC_CYCLE_ACTIVE  =  self._SEC_CYCLE_ACTIVE(self,  Access.RW,  0x00000800,  11,  signed=False)

    class _SPI0_TRANSFER_CONFIG0(Register):

        class _SCLK_PHASE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCLK_PHASE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCLK_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCLK_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS0_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS0_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS1_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS1_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS2_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS2_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _APPLY_TAD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("APPLY_TAD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DATA_SIZE_SEL_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_SIZE_SEL_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DATA_SIZE_SEL_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_SIZE_SEL_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_TRANSFER_CONFIG0", parent, access, address, block, signed)
            self.SCLK_PHASE       =  self._SCLK_PHASE(self,       Access.RW,  0x00000001,  0,   signed=False)
            self.SCLK_POL         =  self._SCLK_POL(self,         Access.RW,  0x00000002,  1,   signed=False)
            self.CS_POL           =  self._CS_POL(self,           Access.RW,  0x00000004,  2,   signed=False)
            self.CS0_ENABLE       =  self._CS0_ENABLE(self,       Access.RW,  0x00000008,  3,   signed=False)
            self.CS1_ENABLE       =  self._CS1_ENABLE(self,       Access.RW,  0x00000010,  4,   signed=False)
            self.CS2_ENABLE       =  self._CS2_ENABLE(self,       Access.RW,  0x00000020,  5,   signed=False)
            self.APPLY_TAD        =  self._APPLY_TAD(self,        Access.RW,  0x000000C0,  6,   signed=False)
            self.DATA_SIZE_SEL_0  =  self._DATA_SIZE_SEL_0(self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.DATA_SIZE_SEL_1  =  self._DATA_SIZE_SEL_1(self,  Access.RW,  0x0000F000,  12,  signed=False)

    class _SPI0_SCLK_CONFIG1(Register):

        class _CLK_DIV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_DIV", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS_SETTLE_TIM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS_SETTLE_TIM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PAUSE_TIM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PAUSE_TIM", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_SCLK_CONFIG1", parent, access, address, block, signed)
            self.CLK_DIV        =  self._CLK_DIV(self,        Access.RW,  0x000000FE,  1,   signed=False)
            self.CS_SETTLE_TIM  =  self._CS_SETTLE_TIM(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.PAUSE_TIM      =  self._PAUSE_TIM(self,      Access.RW,  0x00FF0000,  16,  signed=False)

    class _SPI0_SYNC_CONFIG1(Register):

        class _STROBE_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STROBE_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SW_STROBE_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SW_STROBE_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HW_STROBE_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HW_STROBE_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEC_CYCLE_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEC_CYCLE_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_SYNC_CONFIG1", parent, access, address, block, signed)
            self.STROBE_MASK       =  self._STROBE_MASK(self,       Access.RW,  0x000001FF,  0,   signed=False)
            self.SW_STROBE_ENABLE  =  self._SW_STROBE_ENABLE(self,  Access.RW,  0x00000200,  9,   signed=False)
            self.HW_STROBE_ENABLE  =  self._HW_STROBE_ENABLE(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.SEC_CYCLE_ACTIVE  =  self._SEC_CYCLE_ACTIVE(self,  Access.RW,  0x00000800,  11,  signed=False)

    class _SPI0_TRANSFER_CONFIG1(Register):

        class _SCLK_PHASE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCLK_PHASE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCLK_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCLK_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS0_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS0_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS1_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS1_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS2_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS2_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _APPLY_TAD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("APPLY_TAD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DATA_SIZE_SEL_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_SIZE_SEL_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DATA_SIZE_SEL_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_SIZE_SEL_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_TRANSFER_CONFIG1", parent, access, address, block, signed)
            self.SCLK_PHASE       =  self._SCLK_PHASE(self,       Access.RW,  0x00000001,  0,   signed=False)
            self.SCLK_POL         =  self._SCLK_POL(self,         Access.RW,  0x00000002,  1,   signed=False)
            self.CS_POL           =  self._CS_POL(self,           Access.RW,  0x00000004,  2,   signed=False)
            self.CS0_ENABLE       =  self._CS0_ENABLE(self,       Access.RW,  0x00000008,  3,   signed=False)
            self.CS1_ENABLE       =  self._CS1_ENABLE(self,       Access.RW,  0x00000010,  4,   signed=False)
            self.CS2_ENABLE       =  self._CS2_ENABLE(self,       Access.RW,  0x00000020,  5,   signed=False)
            self.APPLY_TAD        =  self._APPLY_TAD(self,        Access.RW,  0x000000C0,  6,   signed=False)
            self.DATA_SIZE_SEL_0  =  self._DATA_SIZE_SEL_0(self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.DATA_SIZE_SEL_1  =  self._DATA_SIZE_SEL_1(self,  Access.RW,  0x0000F000,  12,  signed=False)

    class _SPI0_SCLK_CONFIG2(Register):

        class _CLK_DIV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_DIV", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS_SETTLE_TIM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS_SETTLE_TIM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PAUSE_TIM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PAUSE_TIM", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_SCLK_CONFIG2", parent, access, address, block, signed)
            self.CLK_DIV        =  self._CLK_DIV(self,        Access.RW,  0x000000FE,  1,   signed=False)
            self.CS_SETTLE_TIM  =  self._CS_SETTLE_TIM(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.PAUSE_TIM      =  self._PAUSE_TIM(self,      Access.RW,  0x00FF0000,  16,  signed=False)

    class _SPI0_SYNC_CONFIG2(Register):

        class _STROBE_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STROBE_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SW_STROBE_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SW_STROBE_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HW_STROBE_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HW_STROBE_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SEC_CYCLE_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SEC_CYCLE_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_SYNC_CONFIG2", parent, access, address, block, signed)
            self.STROBE_MASK       =  self._STROBE_MASK(self,       Access.RW,  0x000001FF,  0,   signed=False)
            self.SW_STROBE_ENABLE  =  self._SW_STROBE_ENABLE(self,  Access.RW,  0x00000200,  9,   signed=False)
            self.HW_STROBE_ENABLE  =  self._HW_STROBE_ENABLE(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.SEC_CYCLE_ACTIVE  =  self._SEC_CYCLE_ACTIVE(self,  Access.RW,  0x00000800,  11,  signed=False)

    class _SPI0_TRANSFER_CONFIG2(Register):

        class _SCLK_PHASE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCLK_PHASE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCLK_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCLK_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS0_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS0_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS1_ENALBE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS1_ENALBE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CS2_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CS2_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _APPLY_TAD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("APPLY_TAD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DATA_SIZE_SEL_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_SIZE_SEL_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DATA_SIZE_SEL_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DATA_SIZE_SEL_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_TRANSFER_CONFIG2", parent, access, address, block, signed)
            self.SCLK_PHASE       =  self._SCLK_PHASE(self,       Access.RW,  0x00000001,  0,   signed=False)
            self.SCLK_POL         =  self._SCLK_POL(self,         Access.RW,  0x00000002,  1,   signed=False)
            self.CS_POL           =  self._CS_POL(self,           Access.RW,  0x00000004,  2,   signed=False)
            self.CS0_ENABLE       =  self._CS0_ENABLE(self,       Access.RW,  0x00000008,  3,   signed=False)
            self.CS1_ENALBE       =  self._CS1_ENALBE(self,       Access.RW,  0x00000010,  4,   signed=False)
            self.CS2_ENABLE       =  self._CS2_ENABLE(self,       Access.RW,  0x00000020,  5,   signed=False)
            self.APPLY_TAD        =  self._APPLY_TAD(self,        Access.RW,  0x000000C0,  6,   signed=False)
            self.DATA_SIZE_SEL_0  =  self._DATA_SIZE_SEL_0(self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.DATA_SIZE_SEL_1  =  self._DATA_SIZE_SEL_1(self,  Access.RW,  0x0000F000,  12,  signed=False)

    class _SPI0_RD_BUFFER0(Register):

        class _RD_BUFFER0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RD_BUFFER0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_RD_BUFFER0", parent, access, address, block, signed)
            self.RD_BUFFER0  =  self._RD_BUFFER0(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _SPI0_RD_BUFFER1(Register):

        class _RD_BUFFER1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RD_BUFFER1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_RD_BUFFER1", parent, access, address, block, signed)
            self.RD_BUFFER1  =  self._RD_BUFFER1(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _SPI0_RD_BUFFER2(Register):

        class _RD_BUFFER2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RD_BUFFER2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_RD_BUFFER2", parent, access, address, block, signed)
            self.RD_BUFFER2  =  self._RD_BUFFER2(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _SPI0_RD_BUFFER3(Register):

        class _RD_BUFFER3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RD_BUFFER3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_RD_BUFFER3", parent, access, address, block, signed)
            self.RD_BUFFER3  =  self._RD_BUFFER3(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _SPI0_WR_BUFFER0(Register):

        class _WR_BUFFER0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WR_BUFFER0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_WR_BUFFER0", parent, access, address, block, signed)
            self.WR_BUFFER0  =  self._WR_BUFFER0(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _SPI0_WR_BUFFER1(Register):

        class _WR_BUFFER1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WR_BUFFER1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_WR_BUFFER1", parent, access, address, block, signed)
            self.WR_BUFFER1  =  self._WR_BUFFER1(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _SPI0_WR_BUFFER2(Register):

        class _WR_BUFFER2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WR_BUFFER2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_WR_BUFFER2", parent, access, address, block, signed)
            self.WR_BUFFER2  =  self._WR_BUFFER2(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _SPI0_WR_BUFFER3(Register):

        class _WR_BUFFER3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WR_BUFFER3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SPI0_WR_BUFFER3", parent, access, address, block, signed)
            self.WR_BUFFER3  =  self._WR_BUFFER3(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.SPI0_STATUS            =  self._SPI0_STATUS(self,            Access.RWC,  0x0000,  block,  False)
        self.SPI0_GEN_CONFIG        =  self._SPI0_GEN_CONFIG(self,        Access.RW,   0x0001,  block,  False)
        self.SPI0_SCLK_CONFIG0      =  self._SPI0_SCLK_CONFIG0(self,      Access.RW,   0x0002,  block,  False)
        self.SPI0_SYNC_CONFIG0      =  self._SPI0_SYNC_CONFIG0(self,      Access.RW,   0x0003,  block,  False)
        self.SPI0_TRANSFER_CONFIG0  =  self._SPI0_TRANSFER_CONFIG0(self,  Access.RW,   0x0004,  block,  False)
        self.SPI0_SCLK_CONFIG1      =  self._SPI0_SCLK_CONFIG1(self,      Access.RW,   0x0005,  block,  False)
        self.SPI0_SYNC_CONFIG1      =  self._SPI0_SYNC_CONFIG1(self,      Access.RW,   0x0006,  block,  False)
        self.SPI0_TRANSFER_CONFIG1  =  self._SPI0_TRANSFER_CONFIG1(self,  Access.RW,   0x0007,  block,  False)
        self.SPI0_SCLK_CONFIG2      =  self._SPI0_SCLK_CONFIG2(self,      Access.RW,   0x0008,  block,  False)
        self.SPI0_SYNC_CONFIG2      =  self._SPI0_SYNC_CONFIG2(self,      Access.RW,   0x0009,  block,  False)
        self.SPI0_TRANSFER_CONFIG2  =  self._SPI0_TRANSFER_CONFIG2(self,  Access.RW,   0x000A,  block,  False)
        self.SPI0_RD_BUFFER0        =  self._SPI0_RD_BUFFER0(self,        Access.R,    0x000B,  block,  False)
        self.SPI0_RD_BUFFER1        =  self._SPI0_RD_BUFFER1(self,        Access.R,    0x000C,  block,  False)
        self.SPI0_RD_BUFFER2        =  self._SPI0_RD_BUFFER2(self,        Access.R,    0x000D,  block,  False)
        self.SPI0_RD_BUFFER3        =  self._SPI0_RD_BUFFER3(self,        Access.R,    0x000E,  block,  False)
        self.SPI0_WR_BUFFER0        =  self._SPI0_WR_BUFFER0(self,        Access.RW,   0x000F,  block,  False)
        self.SPI0_WR_BUFFER1        =  self._SPI0_WR_BUFFER1(self,        Access.RW,   0x0010,  block,  False)
        self.SPI0_WR_BUFFER2        =  self._SPI0_WR_BUFFER2(self,        Access.RW,   0x0011,  block,  False)
        self.SPI0_WR_BUFFER3        =  self._SPI0_WR_BUFFER3(self,        Access.RW,   0x0012,  block,  False)

