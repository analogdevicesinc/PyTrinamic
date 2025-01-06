################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Field, Register


class GPIOMap:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)




class _ALL_REGISTERS(RegisterGroup):

    class _GPIO_DATA(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_DATA", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RW,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RW,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RW,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RW,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RW,  0x00040000,  18,  signed=False)

    class _GPIO_SET(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_SET", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RW,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RW,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RW,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RW,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RW,  0x00040000,  18,  signed=False)

    class _GPIO_CLEAR(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_CLEAR", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RWC,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RWC,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RWC,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RWC,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RWC,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RWC,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RWC,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RWC,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RWC,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RWC,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RWC,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RWC,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RWC,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RWC,  0x00040000,  18,  signed=False)

    class _GPIO_TOGGLE(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_TOGGLE", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RW,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RW,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RW,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RW,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RW,  0x00040000,  18,  signed=False)

    class _GPIO_DIR(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_DIR", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RW,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RW,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RW,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RW,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RW,  0x00040000,  18,  signed=False)

    class _GPIO_IRQ_POLARITY(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_IRQ_POLARITY", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RW,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RW,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RW,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RW,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RW,  0x00040000,  18,  signed=False)

    class _GPIO_IRQ_MASK(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_IRQ_MASK", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RW,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RW,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RW,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RW,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RW,  0x00040000,  18,  signed=False)

    class _GPIO_IRQ_STATUS(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_IRQ_STATUS", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RWC,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RWC,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RWC,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RWC,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RWC,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RWC,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RWC,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RWC,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RWC,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RWC,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RWC,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RWC,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RWC,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RWC,  0x00040000,  18,  signed=False)

    class _GPIO_IRQ_BOTH_EDGES(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_IRQ_BOTH_EDGES", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RW,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RW,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RW,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RW,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RW,  0x00040000,  18,  signed=False)

    class _GPIO_IRQ_EDGE_LEVEL(Register):

        class _PIN_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_4(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_4", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_5(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_5", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_6(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_6", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_7(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_7", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_8(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_8", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_9(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_9", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_10(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_10", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_11(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_11", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_12(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_12", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_13(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_13", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_14(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_14", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_15(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_15", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_16(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_16", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_17(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_17", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIN_18(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_18", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GPIO_IRQ_EDGE_LEVEL", parent, access, address, block, signed)
            self.PIN_0   =  self._PIN_0(self,   Access.RW,  0x00000001,  0,   signed=False)
            self.PIN_1   =  self._PIN_1(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.PIN_2   =  self._PIN_2(self,   Access.RW,  0x00000004,  2,   signed=False)
            self.PIN_3   =  self._PIN_3(self,   Access.RW,  0x00000008,  3,   signed=False)
            self.PIN_4   =  self._PIN_4(self,   Access.RW,  0x00000010,  4,   signed=False)
            self.PIN_5   =  self._PIN_5(self,   Access.RW,  0x00000020,  5,   signed=False)
            self.PIN_6   =  self._PIN_6(self,   Access.RW,  0x00000040,  6,   signed=False)
            self.PIN_7   =  self._PIN_7(self,   Access.RW,  0x00000080,  7,   signed=False)
            self.PIN_8   =  self._PIN_8(self,   Access.RW,  0x00000100,  8,   signed=False)
            self.PIN_9   =  self._PIN_9(self,   Access.RW,  0x00000200,  9,   signed=False)
            self.PIN_10  =  self._PIN_10(self,  Access.RW,  0x00000400,  10,  signed=False)
            self.PIN_11  =  self._PIN_11(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.PIN_12  =  self._PIN_12(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.PIN_13  =  self._PIN_13(self,  Access.RW,  0x00002000,  13,  signed=False)
            self.PIN_14  =  self._PIN_14(self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PIN_15  =  self._PIN_15(self,  Access.RW,  0x00008000,  15,  signed=False)
            self.PIN_16  =  self._PIN_16(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.PIN_17  =  self._PIN_17(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.PIN_18  =  self._PIN_18(self,  Access.RW,  0x00040000,  18,  signed=False)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.GPIO_DATA            =  self._GPIO_DATA(self,            Access.RW,   0x0000,  block,  False)
        self.GPIO_SET             =  self._GPIO_SET(self,             Access.RW,   0x0001,  block,  False)
        self.GPIO_CLEAR           =  self._GPIO_CLEAR(self,           Access.RWC,  0x0002,  block,  False)
        self.GPIO_TOGGLE          =  self._GPIO_TOGGLE(self,          Access.RW,   0x0003,  block,  False)
        self.GPIO_DIR             =  self._GPIO_DIR(self,             Access.RW,   0x0004,  block,  False)
        self.GPIO_IRQ_POLARITY    =  self._GPIO_IRQ_POLARITY(self,    Access.RW,   0x0005,  block,  False)
        self.GPIO_IRQ_MASK        =  self._GPIO_IRQ_MASK(self,        Access.RW,   0x0006,  block,  False)
        self.GPIO_IRQ_STATUS      =  self._GPIO_IRQ_STATUS(self,      Access.RWC,  0x0007,  block,  False)
        self.GPIO_IRQ_BOTH_EDGES  =  self._GPIO_IRQ_BOTH_EDGES(self,  Access.RW,   0x0008,  block,  False)
        self.GPIO_IRQ_EDGE_LEVEL  =  self._GPIO_IRQ_EDGE_LEVEL(self,  Access.RW,   0x0009,  block,  False)

