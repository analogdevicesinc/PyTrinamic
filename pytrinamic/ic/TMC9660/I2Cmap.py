################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Field, Register


class I2CMap:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)




class _ALL_REGISTERS(RegisterGroup):

    class _I2C_CPR(Register):

        class _PRE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PRE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("I2C_CPR", parent, access, address, block, signed)
            self.PRE  =  self._PRE(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _I2C_CTRL(Register):

        class _IE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("I2C_CTRL", parent, access, address, block, signed)
            self.IE  =  self._IE(self,  Access.RW,  0x00000040,  6,  signed=False)
            self.EN  =  self._EN(self,  Access.RW,  0x00000080,  7,  signed=False)

    class _I2C_RX(Register):

        class _RX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("I2C_RX", parent, access, address, block, signed)
            self.RX  =  self._RX(self,  Access.RW,  0x000000FF,  0,  signed=False)

    class _I2C_STATUS(Register):

        class _IRQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IRQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TIP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TIP", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BUS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BUS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RXA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RXA", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("I2C_STATUS", parent, access, address, block, signed)
            self.IRQ  =  self._IRQ(self,  Access.RW,  0x00000001,  0,  signed=False)
            self.TIP  =  self._TIP(self,  Access.RW,  0x00000002,  1,  signed=False)
            self.AL   =  self._AL(self,   Access.RW,  0x00000020,  5,  signed=False)
            self.BUS  =  self._BUS(self,  Access.RW,  0x00000040,  6,  signed=False)
            self.RXA  =  self._RXA(self,  Access.RW,  0x00000080,  7,  signed=False)

    class _I2C_TX(Register):

        class _TX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("I2C_TX", parent, access, address, block, signed)
            self.TX  =  self._TX(self,  Access.RW,  0x000000FF,  0,  signed=False)

    class _I2C_CMD(Register):

        class _IA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IA", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ACK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ACK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _WR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STA", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("I2C_CMD", parent, access, address, block, signed)
            self.IA   =  self._IA(self,   Access.RW,  0x00000001,  0,  signed=False)
            self.ACK  =  self._ACK(self,  Access.RW,  0x00000008,  3,  signed=False)
            self.WR   =  self._WR(self,   Access.RW,  0x00000010,  4,  signed=False)
            self.RD   =  self._RD(self,   Access.RW,  0x00000020,  5,  signed=False)
            self.STO  =  self._STO(self,  Access.RW,  0x00000040,  6,  signed=False)
            self.STA  =  self._STA(self,  Access.RW,  0x00000080,  7,  signed=False)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.I2C_CPR     =  self._I2C_CPR(self,     Access.RW,  0x0000,  block,  False)
        self.I2C_CTRL    =  self._I2C_CTRL(self,    Access.RW,  0x0001,  block,  False)
        self.I2C_RX      =  self._I2C_RX(self,      Access.RW,  0x0002,  block,  False)
        self.I2C_STATUS  =  self._I2C_STATUS(self,  Access.RW,  0x0003,  block,  False)
        self.I2C_TX      =  self._I2C_TX(self,      Access.RW,  0x0004,  block,  False)
        self.I2C_CMD     =  self._I2C_CMD(self,     Access.RW,  0x0005,  block,  False)

