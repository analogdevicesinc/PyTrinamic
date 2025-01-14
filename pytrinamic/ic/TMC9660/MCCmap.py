################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Choice, Field, Register


class MCCMap:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)


class _ALL_REGISTERS(RegisterGroup):

    class _INFO_CHIP(Register):

        class _ID(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ID", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PREFIX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PREFIX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("INFO_CHIP", parent, access, address, block, signed)
            self.ID      =  self._ID(    self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.PREFIX  =  self._PREFIX(self,  Access.R,  0xFFFF0000,  16,  signed=False)

    class _INFO_VARIANT(Register):

        class _PMU_VAR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PMU_VAR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _GDRV_VAR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GDRV_VAR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("INFO_VARIANT", parent, access, address, block, signed)
            self.PMU_VAR   =  self._PMU_VAR( self,  Access.R,  0x00000003,  0,  signed=False)
            self.GDRV_VAR  =  self._GDRV_VAR(self,  Access.R,  0x0000000C,  2,  signed=False)

    class _INFO_REVISION(Register):

        class _REVISION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REVISION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("INFO_REVISION", parent, access, address, block, signed)
            self.REVISION  =  self._REVISION(self,  Access.R,  0x7FFFFFFF,  0,  signed=False)

    class _ADC_I1_I0_RAW(Register):

        class _I0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I1_I0_RAW", parent, access, address, block, signed)
            self.I0  =  self._I0(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.I1  =  self._I1(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_I3_I2_RAW(Register):

        class _I2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I3_I2_RAW", parent, access, address, block, signed)
            self.I2  =  self._I2(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.I3  =  self._I3(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_U1_U0_RAW(Register):

        class _U0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_U1_U0_RAW", parent, access, address, block, signed)
            self.U0  =  self._U0(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.U1  =  self._U1(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_U3_U2_RAW(Register):

        class _U2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_U3_U2_RAW", parent, access, address, block, signed)
            self.U2  =  self._U2(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.U3  =  self._U3(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_TEMP_VM_RAW(Register):

        class _VM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TEMP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_TEMP_VM_RAW", parent, access, address, block, signed)
            self.VM    =  self._VM(  self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.TEMP  =  self._TEMP(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_AIN1_AIN0_RAW(Register):

        class _AIN0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_AIN1_AIN0_RAW", parent, access, address, block, signed)
            self.AIN0  =  self._AIN0(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.AIN1  =  self._AIN1(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_AIN3_AIN2_RAW(Register):

        class _AIN2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_AIN3_AIN2_RAW", parent, access, address, block, signed)
            self.AIN2  =  self._AIN2(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.AIN3  =  self._AIN3(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_I_GEN_CONFIG(Register):

        class _UX1_SELECT(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC_I0 = Choice(0, parent)
                    self.ADC_I1 = Choice(1, parent)
                    self.ADC_I2 = Choice(2, parent)
                    self.ADC_I3 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UX1_SELECT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _VX2_SELECT(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC_I0 = Choice(0, parent)
                    self.ADC_I1 = Choice(1, parent)
                    self.ADC_I2 = Choice(2, parent)
                    self.ADC_I3 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VX2_SELECT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _WY1_SELECT(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC_I0 = Choice(0, parent)
                    self.ADC_I1 = Choice(1, parent)
                    self.ADC_I2 = Choice(2, parent)
                    self.ADC_I3 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WY1_SELECT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _Y2_SELECT(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.ADC_I0 = Choice(0, parent)
                    self.ADC_I1 = Choice(1, parent)
                    self.ADC_I2 = Choice(2, parent)
                    self.ADC_I3 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("Y2_SELECT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _MEASUREMENT_MODE(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.INLINE = Choice(0, parent)
                    self.INLINE_VW = Choice(1, parent)
                    self.INLINE_UW = Choice(2, parent)
                    self.INLINE_UV = Choice(3, parent)
                    self.BOTTOM = Choice(4, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MEASUREMENT_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _TRIGGER_SELECT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRIGGER_SELECT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TRIGGER_POS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TRIGGER_POS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I_GEN_CONFIG", parent, access, address, block, signed)
            self.UX1_SELECT        =  self._UX1_SELECT(      self,  Access.RW,  0x00000003,  0,   signed=False)
            self.VX2_SELECT        =  self._VX2_SELECT(      self,  Access.RW,  0x0000000C,  2,   signed=False)
            self.WY1_SELECT        =  self._WY1_SELECT(      self,  Access.RW,  0x00000030,  4,   signed=False)
            self.Y2_SELECT         =  self._Y2_SELECT(       self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.MEASUREMENT_MODE  =  self._MEASUREMENT_MODE(self,  Access.RW,  0x00000E00,  9,   signed=False)
            self.TRIGGER_SELECT    =  self._TRIGGER_SELECT(  self,  Access.RW,  0x00001000,  12,  signed=False)
            self.TRIGGER_POS       =  self._TRIGGER_POS(     self,  Access.RW,  0xFFFF0000,  16,  signed=False)

    class _ADC_I0_CONFIG(Register):

        class _OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I0_CONFIG", parent, access, address, block, signed)
            self.OFFSET  =  self._OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.SCALE   =  self._SCALE( self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I1_CONFIG(Register):

        class _OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I1_CONFIG", parent, access, address, block, signed)
            self.OFFSET  =  self._OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.SCALE   =  self._SCALE( self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I2_CONFIG(Register):

        class _OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I2_CONFIG", parent, access, address, block, signed)
            self.OFFSET  =  self._OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.SCALE   =  self._SCALE( self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I3_CONFIG(Register):

        class _OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I3_CONFIG", parent, access, address, block, signed)
            self.OFFSET  =  self._OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.SCALE   =  self._SCALE( self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I1_I0_SCALED(Register):

        class _I0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I1_I0_SCALED", parent, access, address, block, signed)
            self.I0  =  self._I0(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.I1  =  self._I1(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_I3_I2_SCALED(Register):

        class _I2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I3_I2_SCALED", parent, access, address, block, signed)
            self.I2  =  self._I2(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.I3  =  self._I3(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_IWY_IUX(Register):

        class _IUX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IUX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IWY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IWY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_IWY_IUX", parent, access, address, block, signed)
            self.IUX  =  self._IUX(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.IWY  =  self._IWY(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ADC_IV(Register):

        class _IV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_IV", parent, access, address, block, signed)
            self.IV  =  self._IV(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _ADC_STATUS(Register):

        class _I0_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I0_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I1_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I2_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I3_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I3_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U0_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U0_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U1_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U1_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U2_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U2_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U3_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U3_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN0_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN0_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN1_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN1_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN2_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN2_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN3_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN3_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VM_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TEMP_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I0_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I0_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I1_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I2_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I3_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I3_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U0_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U0_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U1_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U1_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U2_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U2_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U3_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U3_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN0_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN0_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN1_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN1_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN2_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN2_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _AIN3_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN3_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VM_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TEMP_DONE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_DONE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_STATUS", parent, access, address, block, signed)
            self.I0_CLIPPED    =  self._I0_CLIPPED(  self,  Access.RWC,  0x00000001,  0,   signed=False)
            self.I1_CLIPPED    =  self._I1_CLIPPED(  self,  Access.RWC,  0x00000002,  1,   signed=False)
            self.I2_CLIPPED    =  self._I2_CLIPPED(  self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.I3_CLIPPED    =  self._I3_CLIPPED(  self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.U0_CLIPPED    =  self._U0_CLIPPED(  self,  Access.RWC,  0x00000010,  4,   signed=False)
            self.U1_CLIPPED    =  self._U1_CLIPPED(  self,  Access.RWC,  0x00000020,  5,   signed=False)
            self.U2_CLIPPED    =  self._U2_CLIPPED(  self,  Access.RWC,  0x00000040,  6,   signed=False)
            self.U3_CLIPPED    =  self._U3_CLIPPED(  self,  Access.RWC,  0x00000080,  7,   signed=False)
            self.AIN0_CLIPPED  =  self._AIN0_CLIPPED(self,  Access.RWC,  0x00000100,  8,   signed=False)
            self.AIN1_CLIPPED  =  self._AIN1_CLIPPED(self,  Access.RWC,  0x00000200,  9,   signed=False)
            self.AIN2_CLIPPED  =  self._AIN2_CLIPPED(self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.AIN3_CLIPPED  =  self._AIN3_CLIPPED(self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.VM_CLIPPED    =  self._VM_CLIPPED(  self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.TEMP_CLIPPED  =  self._TEMP_CLIPPED(self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.I0_DONE       =  self._I0_DONE(     self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.I1_DONE       =  self._I1_DONE(     self,  Access.RWC,  0x00020000,  17,  signed=False)
            self.I2_DONE       =  self._I2_DONE(     self,  Access.RWC,  0x00040000,  18,  signed=False)
            self.I3_DONE       =  self._I3_DONE(     self,  Access.RWC,  0x00080000,  19,  signed=False)
            self.U0_DONE       =  self._U0_DONE(     self,  Access.RWC,  0x00100000,  20,  signed=False)
            self.U1_DONE       =  self._U1_DONE(     self,  Access.RWC,  0x00200000,  21,  signed=False)
            self.U2_DONE       =  self._U2_DONE(     self,  Access.RWC,  0x00400000,  22,  signed=False)
            self.U3_DONE       =  self._U3_DONE(     self,  Access.RWC,  0x00800000,  23,  signed=False)
            self.AIN0_DONE     =  self._AIN0_DONE(   self,  Access.RWC,  0x01000000,  24,  signed=False)
            self.AIN1_DONE     =  self._AIN1_DONE(   self,  Access.RWC,  0x02000000,  25,  signed=False)
            self.AIN2_DONE     =  self._AIN2_DONE(   self,  Access.RWC,  0x04000000,  26,  signed=False)
            self.AIN3_DONE     =  self._AIN3_DONE(   self,  Access.RWC,  0x08000000,  27,  signed=False)
            self.VM_DONE       =  self._VM_DONE(     self,  Access.RWC,  0x10000000,  28,  signed=False)
            self.TEMP_DONE     =  self._TEMP_DONE(   self,  Access.RWC,  0x20000000,  29,  signed=False)

    class _MOTOR_CONFIG(Register):

        class _N_POLE_PAIRS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_POLE_PAIRS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TYPE(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.NONE = Choice(0, parent)
                    self.DC = Choice(1, parent)
                    self.STEPPER = Choice(2, parent)
                    self.BLDC = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TYPE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        def __init__(self, parent, access, address, block, signed):
            super().__init__("MOTOR_CONFIG", parent, access, address, block, signed)
            self.N_POLE_PAIRS  =  self._N_POLE_PAIRS(self,  Access.RW,  0x0000007F,  0,   signed=False)
            self.TYPE          =  self._TYPE(        self,  Access.RW,  0x00030000,  16,  signed=False)

    class _MOTION_CONFIG(Register):

        class _MOTION_MODE(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.STOPPED = Choice(0, parent)
                    self.TORQUE = Choice(1, parent)
                    self.VELOCITY = Choice(2, parent)
                    self.POSITION = Choice(3, parent)
                    self.PRBS_FLUX = Choice(4, parent)
                    self.PRBS_TORQUE = Choice(5, parent)
                    self.PRBS_VELOCITY = Choice(6, parent)
                    self.PRBS_POSITION = Choice(7, parent)
                    self.VOLTAGE_EXT = Choice(8, parent)
                    self.PRBS_UD = Choice(9, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MOTION_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _RAMP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RAMP_MODE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_MODE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _FEEDFORWARD(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.DISABLED = Choice(0, parent)
                    self.MCC_RAMPER_V_ACTUAL = Choice(1, parent)
                    self.MCC_RAMPER_A_ACTUAL = Choice(2, parent)
                    self.BOTH = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FEEDFORWARD", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        def __init__(self, parent, access, address, block, signed):
            super().__init__("MOTION_CONFIG", parent, access, address, block, signed)
            self.MOTION_MODE  =  self._MOTION_MODE(self,  Access.RW,  0x0000000F,  0,  signed=False)
            self.RAMP_ENABLE  =  self._RAMP_ENABLE(self,  Access.RW,  0x00000010,  4,  signed=False)
            self.RAMP_MODE    =  self._RAMP_MODE(  self,  Access.RW,  0x00000020,  5,  signed=False)
            self.FEEDFORWARD  =  self._FEEDFORWARD(self,  Access.RW,  0x000000C0,  6,  signed=False)

    class _PHI_E_SELECTION(Register):

        class _PHI_E_SELECTION(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.RESERVED = Choice(0, parent)
                    self.PHI_E_EXT = Choice(1, parent)
                    self.PHI_E_RAMP = Choice(2, parent)
                    self.PHI_E_ABN = Choice(3, parent)
                    self.RAMP_X_ACTUAL = Choice(4, parent)
                    self.PHI_E_HAL = Choice(5, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_SELECTION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PHI_E_SELECTION", parent, access, address, block, signed)
            self.PHI_E_SELECTION  =  self._PHI_E_SELECTION(self,  Access.RW,  0x0000000F,  0,  signed=False)

    class _PHI_E(Register):

        class _PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PHI_E", parent, access, address, block, signed)
            self.PHI_E  =  self._PHI_E(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _PWM_CONFIG(Register):

        class _CHOP(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.OFF_FREE = Choice(0, parent)
                    self.OFF_LSON = Choice(1, parent)
                    self.OFF_HSON = Choice(2, parent)
                    self.OFF_FREE2 = Choice(3, parent)
                    self.OFF_FREE3 = Choice(4, parent)
                    self.LSPWM_HSOFF = Choice(5, parent)
                    self.HSPWM_LSOFF = Choice(6, parent)
                    self.CENTERED = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHOP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _SV_MODE(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.DISABLED = Choice(0, parent)
                    self.HARMONIC = Choice(1, parent)
                    self.BOTTOM = Choice(2, parent)
                    self.BOTTOM_OFFSET = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SV_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _Y2_HS_SRC(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.Y2_HS = Choice(0, parent)
                    self.Y2_ALT = Choice(1, parent)
                    self.TIM_BASIC = Choice(2, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("Y2_HS_SRC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ENABLE_UX1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_UX1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE_VX2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_VX2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE_WY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_WY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_ENABLE_UX1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_ENABLE_UX1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_ENABLE_VX2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_ENABLE_VX2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_ENABLE_WY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_ENABLE_WY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXT_ENABLE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_ENABLE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DUTY_CYCLE_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DUTY_CYCLE_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_CONFIG", parent, access, address, block, signed)
            self.CHOP               =  self._CHOP(             self,  Access.RW,  0x00000007,  0,   signed=False)
            self.SV_MODE            =  self._SV_MODE(          self,  Access.RW,  0x00000030,  4,   signed=False)
            self.Y2_HS_SRC          =  self._Y2_HS_SRC(        self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.ENABLE_UX1         =  self._ENABLE_UX1(       self,  Access.RW,  0x00000100,  8,   signed=False)
            self.ENABLE_VX2         =  self._ENABLE_VX2(       self,  Access.RW,  0x00000200,  9,   signed=False)
            self.ENABLE_WY1         =  self._ENABLE_WY1(       self,  Access.RW,  0x00000400,  10,  signed=False)
            self.ENABLE_Y2          =  self._ENABLE_Y2(        self,  Access.RW,  0x00000800,  11,  signed=False)
            self.EXT_ENABLE_UX1     =  self._EXT_ENABLE_UX1(   self,  Access.RW,  0x00001000,  12,  signed=False)
            self.EXT_ENABLE_VX2     =  self._EXT_ENABLE_VX2(   self,  Access.RW,  0x00002000,  13,  signed=False)
            self.EXT_ENABLE_WY1     =  self._EXT_ENABLE_WY1(   self,  Access.RW,  0x00004000,  14,  signed=False)
            self.EXT_ENABLE_Y2      =  self._EXT_ENABLE_Y2(    self,  Access.RW,  0x00008000,  15,  signed=False)
            self.DUTY_CYCLE_OFFSET  =  self._DUTY_CYCLE_OFFSET(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

    class _PWM_MAXCNT(Register):

        class _PWM_MAXCNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_MAXCNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_MAXCNT", parent, access, address, block, signed)
            self.PWM_MAXCNT  =  self._PWM_MAXCNT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _PWM_SWITCH_LIMIT(Register):

        class _PWM_SWITCH_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_SWITCH_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_SWITCH_LIMIT", parent, access, address, block, signed)
            self.PWM_SWITCH_LIMIT  =  self._PWM_SWITCH_LIMIT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _ABN_PHI_E_PHI_M(Register):

        class _PHI_M(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_M", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_PHI_E_PHI_M", parent, access, address, block, signed)
            self.PHI_M  =  self._PHI_M(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.PHI_E  =  self._PHI_E(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _ABN_MODE(Register):

        class _A_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _B_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("B_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _N_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _COMBINED_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMBINED_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLEAR_COUNT_ON_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLEAR_COUNT_ON_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DISABLE_FILTER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DISABLE_FILTER", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CLN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DIRECTION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIRECTION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_MODE", parent, access, address, block, signed)
            self.A_POL             =  self._A_POL(           self,  Access.RW,  0x00000001,  0,   signed=False)
            self.B_POL             =  self._B_POL(           self,  Access.RW,  0x00000002,  1,   signed=False)
            self.N_POL             =  self._N_POL(           self,  Access.RW,  0x00000004,  2,   signed=False)
            self.COMBINED_N        =  self._COMBINED_N(      self,  Access.RW,  0x00000008,  3,   signed=False)
            self.CLEAR_COUNT_ON_N  =  self._CLEAR_COUNT_ON_N(self,  Access.RW,  0x00000010,  4,   signed=False)
            self.DISABLE_FILTER    =  self._DISABLE_FILTER(  self,  Access.RW,  0x00000020,  5,   signed=False)
            self.CLN               =  self._CLN(             self,  Access.RW,  0x00000100,  8,   signed=False)
            self.DIRECTION         =  self._DIRECTION(       self,  Access.RW,  0x00001000,  12,  signed=False)

    class _ABN_CPR(Register):

        class _ABN_CPR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_CPR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_CPR", parent, access, address, block, signed)
            self.ABN_CPR  =  self._ABN_CPR(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

    class _ABN_CPR_INV(Register):

        class _ABN_CPR_INV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_CPR_INV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_CPR_INV", parent, access, address, block, signed)
            self.ABN_CPR_INV  =  self._ABN_CPR_INV(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

    class _ABN_COUNT(Register):

        class _ABN_COUNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_COUNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_COUNT", parent, access, address, block, signed)
            self.ABN_COUNT  =  self._ABN_COUNT(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

    class _ABN_COUNT_N(Register):

        class _ABN_COUNT_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_COUNT_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_COUNT_N", parent, access, address, block, signed)
            self.ABN_COUNT_N  =  self._ABN_COUNT_N(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

    class _ABN_PHI_E_OFFSET(Register):

        class _ABN_PHI_E_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ABN_PHI_E_OFFSET", parent, access, address, block, signed)
            self.ABN_PHI_E_OFFSET  =  self._ABN_PHI_E_OFFSET(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

    class _HALL_MODE(Register):

        class _POLARITY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POLARITY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EXTRAPOLATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXTRAPOLATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ORDER(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.UVW = Choice(0, parent)
                    self.VWU = Choice(1, parent)
                    self.WUV = Choice(2, parent)
                    self.RESERVED = Choice(3, parent)
                    self.UWV = Choice(4, parent)
                    self.VUW = Choice(5, parent)
                    self.WVU = Choice(6, parent)
                    self.RESERVED2 = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ORDER", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _FILTER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FILTER", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_MODE", parent, access, address, block, signed)
            self.POLARITY       =  self._POLARITY(     self,  Access.RW,  0x00000001,  0,  signed=False)
            self.EXTRAPOLATION  =  self._EXTRAPOLATION(self,  Access.RW,  0x00000002,  1,  signed=False)
            self.ORDER          =  self._ORDER(        self,  Access.RW,  0x00000070,  4,  signed=False)
            self.FILTER         =  self._FILTER(       self,  Access.RW,  0x0000FF00,  8,  signed=False)

    class _HALL_DPHI_MAX(Register):

        class _HALL_DPHI_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_DPHI_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_DPHI_MAX", parent, access, address, block, signed)
            self.HALL_DPHI_MAX  =  self._HALL_DPHI_MAX(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _HALL_PHI_E_OFFSET(Register):

        class _HALL_PHI_E_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_PHI_E_OFFSET", parent, access, address, block, signed)
            self.HALL_PHI_E_OFFSET  =  self._HALL_PHI_E_OFFSET(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

    class _HALL_COUNT(Register):

        class _HALL_COUNT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_COUNT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_COUNT", parent, access, address, block, signed)
            self.HALL_COUNT  =  self._HALL_COUNT(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _HALL_PHI_E_EXTRAPOLATED_PHI_E(Register):

        class _PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PHI_E_EXTRAPOLATED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_EXTRAPOLATED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_PHI_E_EXTRAPOLATED_PHI_E", parent, access, address, block, signed)
            self.PHI_E               =  self._PHI_E(             self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.PHI_E_EXTRAPOLATED  =  self._PHI_E_EXTRAPOLATED(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _HALL_POSITION_060_POSITION_000(Register):

        class _POSITION_000(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_000", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_060(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_060", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_POSITION_060_POSITION_000", parent, access, address, block, signed)
            self.POSITION_000  =  self._POSITION_000(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.POSITION_060  =  self._POSITION_060(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _HALL_POSITION_180_POSITION_120(Register):

        class _POSITION_120(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_120", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_180(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_180", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_POSITION_180_POSITION_120", parent, access, address, block, signed)
            self.POSITION_120  =  self._POSITION_120(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.POSITION_180  =  self._POSITION_180(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _HALL_POSITION_300_POSITION_240(Register):

        class _POSITION_240(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_240", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_300(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_300", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("HALL_POSITION_300_POSITION_240", parent, access, address, block, signed)
            self.POSITION_240  =  self._POSITION_240(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.POSITION_300  =  self._POSITION_300(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _BIQUAD_V_A_1(Register):

        class _BIQUAD_V_A_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_A_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_A_1", parent, access, address, block, signed)
            self.BIQUAD_V_A_1  =  self._BIQUAD_V_A_1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_A_2(Register):

        class _BIQUAD_V_A_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_A_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_A_2", parent, access, address, block, signed)
            self.BIQUAD_V_A_2  =  self._BIQUAD_V_A_2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_B_0(Register):

        class _BIQUAD_V_B_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_B_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_B_0", parent, access, address, block, signed)
            self.BIQUAD_V_B_0  =  self._BIQUAD_V_B_0(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_B_1(Register):

        class _BIQUAD_V_B_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_B_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_B_1", parent, access, address, block, signed)
            self.BIQUAD_V_B_1  =  self._BIQUAD_V_B_1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_B_2(Register):

        class _BIQUAD_V_B_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_B_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_B_2", parent, access, address, block, signed)
            self.BIQUAD_V_B_2  =  self._BIQUAD_V_B_2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_V_ENABLE(Register):

        class _BIQUAD_V_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_V_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_V_ENABLE", parent, access, address, block, signed)
            self.BIQUAD_V_ENABLE  =  self._BIQUAD_V_ENABLE(self,  Access.RW,  0x00000001,  0,  signed=False)

    class _BIQUAD_T_A_1(Register):

        class _BIQUAD_T_A_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_A_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_A_1", parent, access, address, block, signed)
            self.BIQUAD_T_A_1  =  self._BIQUAD_T_A_1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_A_2(Register):

        class _BIQUAD_T_A_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_A_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_A_2", parent, access, address, block, signed)
            self.BIQUAD_T_A_2  =  self._BIQUAD_T_A_2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_B_0(Register):

        class _BIQUAD_T_B_0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_B_0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_B_0", parent, access, address, block, signed)
            self.BIQUAD_T_B_0  =  self._BIQUAD_T_B_0(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_B_1(Register):

        class _BIQUAD_T_B_1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_B_1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_B_1", parent, access, address, block, signed)
            self.BIQUAD_T_B_1  =  self._BIQUAD_T_B_1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_B_2(Register):

        class _BIQUAD_T_B_2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_B_2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_B_2", parent, access, address, block, signed)
            self.BIQUAD_T_B_2  =  self._BIQUAD_T_B_2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

    class _BIQUAD_T_ENABLE(Register):

        class _BIQUAD_T_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIQUAD_T_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("BIQUAD_T_ENABLE", parent, access, address, block, signed)
            self.BIQUAD_T_ENABLE  =  self._BIQUAD_T_ENABLE(self,  Access.RW,  0x00000001,  0,  signed=False)

    class _VELOCITY_CONFIG(Register):

        class _SELECTION(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.PHI_E = Choice(0, parent)
                    self.PHI_E_EXT = Choice(1, parent)
                    self.PHI_E_RAMP = Choice(2, parent)
                    self.PHI_E_ABN = Choice(3, parent)
                    self.RAMP_X_ACTUAL = Choice(4, parent)
                    self.PHI_E_HAL = Choice(5, parent)
                    self.PHI_M_EXT = Choice(6, parent)
                    self.Reserved = Choice(11, parent)
                    self.ABN_COUNT = Choice(8, parent)
                    self.PHI_M_ABN = Choice(9, parent)
                    self.HALL_COUNT = Choice(12, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SELECTION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _METER_SYNC_PULSE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("METER_SYNC_PULSE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _METER_TYPE(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.VELOCITY_PER = Choice(0, parent)
                    self.VELOCITY_FREQ = Choice(1, parent)
                    self.VELOCITY_EXT = Choice(2, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("METER_TYPE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _MOVING_AVRG_FILTER_SAMPLES(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.AVRG_1 = Choice(0, parent)
                    self.AVRG_2 = Choice(1, parent)
                    self.AVRG_3 = Choice(2, parent)
                    self.AVRG_4 = Choice(3, parent)
                    self.AVRG_5 = Choice(4, parent)
                    self.AVRG_6 = Choice(5, parent)
                    self.AVRG_7 = Choice(6, parent)
                    self.AVRG_8 = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MOVING_AVRG_FILTER_SAMPLES", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_CONFIG", parent, access, address, block, signed)
            self.SELECTION                   =  self._SELECTION(                 self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.METER_SYNC_PULSE            =  self._METER_SYNC_PULSE(          self,  Access.RW,  0x00000100,  8,   signed=False)
            self.METER_TYPE                  =  self._METER_TYPE(                self,  Access.RW,  0x00000600,  9,   signed=False)
            self.MOVING_AVRG_FILTER_SAMPLES  =  self._MOVING_AVRG_FILTER_SAMPLES(self,  Access.RW,  0x00007000,  12,  signed=False)

    class _VELOCITY_SCALING(Register):

        class _VELOCITY_SCALING(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_SCALING", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_SCALING", parent, access, address, block, signed)
            self.VELOCITY_SCALING  =  self._VELOCITY_SCALING(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

    class _V_MIN_POS_DEV_TIME_COUNTER_LIMIT(Register):

        class _TIME_COUNTER_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TIME_COUNTER_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _V_MIN_POS_DEV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_MIN_POS_DEV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("V_MIN_POS_DEV_TIME_COUNTER_LIMIT", parent, access, address, block, signed)
            self.TIME_COUNTER_LIMIT  =  self._TIME_COUNTER_LIMIT(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.V_MIN_POS_DEV       =  self._V_MIN_POS_DEV(     self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _MAX_VEL_DEVIATION(Register):

        class _MAX_VEL_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MAX_VEL_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("MAX_VEL_DEVIATION", parent, access, address, block, signed)
            self.MAX_VEL_DEVIATION  =  self._MAX_VEL_DEVIATION(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

    class _POSITION_CONFIG(Register):

        class _SELECTION(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.PHI_E = Choice(0, parent)
                    self.PHI_E_EXT = Choice(1, parent)
                    self.PHI_E_RAMP = Choice(2, parent)
                    self.PHI_E_ABN = Choice(3, parent)
                    self.RAMP_X_ACTUAL = Choice(4, parent)
                    self.PHI_E_HAL = Choice(5, parent)
                    self.PHI_M_EXT = Choice(6, parent)
                    self.Reserved = Choice(11, parent)
                    self.ABN_COUNT = Choice(8, parent)
                    self.PHI_M_ABN = Choice(9, parent)
                    self.HALL_COUNT = Choice(12, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SELECTION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        def __init__(self, parent, access, address, block, signed):
            super().__init__("POSITION_CONFIG", parent, access, address, block, signed)
            self.SELECTION  =  self._SELECTION(self,  Access.RW,  0x000000FF,  0,  signed=False)

    class _MAX_POS_DEVIATION(Register):

        class _MAX_POS_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MAX_POS_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("MAX_POS_DEVIATION", parent, access, address, block, signed)
            self.MAX_POS_DEVIATION  =  self._MAX_POS_DEVIATION(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

    class _RAMPER_STATUS(Register):

        class _STATUS_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_STOP_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_STOP_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_LATCH_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_LATCH_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_LATCH_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_LATCH_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_STOP_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_STOP_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_STOP_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_STOP_SG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_STOP_SG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _EVENT_POS_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EVENT_POS_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VELOCITY_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _V_ZERO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_ZERO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_ZEROWAIT_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_ZEROWAIT_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SECOND_MOVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SECOND_MOVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STALL_IN_VEL_ERR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALL_IN_VEL_ERR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STALL_IN_POS_ERR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALL_IN_POS_ERR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_STATUS", parent, access, address, block, signed)
            self.STATUS_STOP_L      =  self._STATUS_STOP_L(    self,  Access.R,    0x00000001,  0,   signed=False)
            self.STATUS_STOP_R      =  self._STATUS_STOP_R(    self,  Access.R,    0x00000002,  1,   signed=False)
            self.STATUS_STOP_H      =  self._STATUS_STOP_H(    self,  Access.R,    0x00000004,  2,   signed=False)
            self.STATUS_LATCH_L     =  self._STATUS_LATCH_L(   self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.STATUS_LATCH_R     =  self._STATUS_LATCH_R(   self,  Access.RWC,  0x00000010,  4,   signed=False)
            self.STATUS_LATCH_H     =  self._STATUS_LATCH_H(   self,  Access.RWC,  0x00000020,  5,   signed=False)
            self.EVENT_STOP_L       =  self._EVENT_STOP_L(     self,  Access.R,    0x00000040,  6,   signed=False)
            self.EVENT_STOP_R       =  self._EVENT_STOP_R(     self,  Access.R,    0x00000080,  7,   signed=False)
            self.EVENT_STOP_H       =  self._EVENT_STOP_H(     self,  Access.R,    0x00000100,  8,   signed=False)
            self.EVENT_STOP_SG      =  self._EVENT_STOP_SG(    self,  Access.RWC,  0x00000200,  9,   signed=False)
            self.EVENT_POS_REACHED  =  self._EVENT_POS_REACHED(self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.VELOCITY_REACHED   =  self._VELOCITY_REACHED( self,  Access.R,    0x00000800,  11,  signed=False)
            self.POSITION_REACHED   =  self._POSITION_REACHED( self,  Access.R,    0x00001000,  12,  signed=False)
            self.V_ZERO             =  self._V_ZERO(           self,  Access.R,    0x00002000,  13,  signed=False)
            self.T_ZEROWAIT_ACTIVE  =  self._T_ZEROWAIT_ACTIVE(self,  Access.R,    0x00004000,  14,  signed=False)
            self.SECOND_MOVE        =  self._SECOND_MOVE(      self,  Access.RWC,  0x00008000,  15,  signed=False)
            self.STALL_IN_VEL_ERR   =  self._STALL_IN_VEL_ERR( self,  Access.R,    0x00010000,  16,  signed=False)
            self.STALL_IN_POS_ERR   =  self._STALL_IN_POS_ERR( self,  Access.R,    0x00020000,  17,  signed=False)

    class _RAMPER_A1(Register):

        class _RAMPER_A1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_A1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_A1", parent, access, address, block, signed)
            self.RAMPER_A1  =  self._RAMPER_A1(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_A2(Register):

        class _RAMPER_A2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_A2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_A2", parent, access, address, block, signed)
            self.RAMPER_A2  =  self._RAMPER_A2(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_A_MAX(Register):

        class _RAMPER_A_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_A_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_A_MAX", parent, access, address, block, signed)
            self.RAMPER_A_MAX  =  self._RAMPER_A_MAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_D1(Register):

        class _RAMPER_D1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_D1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_D1", parent, access, address, block, signed)
            self.RAMPER_D1  =  self._RAMPER_D1(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_D2(Register):

        class _RAMPER_D2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_D2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_D2", parent, access, address, block, signed)
            self.RAMPER_D2  =  self._RAMPER_D2(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_D_MAX(Register):

        class _RAMPER_D_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_D_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_D_MAX", parent, access, address, block, signed)
            self.RAMPER_D_MAX  =  self._RAMPER_D_MAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_V_START(Register):

        class _RAMPER_V_START(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_START", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_START", parent, access, address, block, signed)
            self.RAMPER_V_START  =  self._RAMPER_V_START(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_V1(Register):

        class _RAMPER_V1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V1", parent, access, address, block, signed)
            self.RAMPER_V1  =  self._RAMPER_V1(self,  Access.RW,  0x07FFFFFF,  0,  signed=False)

    class _RAMPER_V2(Register):

        class _RAMPER_V2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V2", parent, access, address, block, signed)
            self.RAMPER_V2  =  self._RAMPER_V2(self,  Access.RW,  0x07FFFFFF,  0,  signed=False)

    class _RAMPER_V_STOP(Register):

        class _RAMPER_V_STOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_STOP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_STOP", parent, access, address, block, signed)
            self.RAMPER_V_STOP  =  self._RAMPER_V_STOP(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

    class _RAMPER_V_MAX(Register):

        class _RAMPER_V_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_MAX", parent, access, address, block, signed)
            self.RAMPER_V_MAX  =  self._RAMPER_V_MAX(self,  Access.RW,  0x07FFFFFF,  0,  signed=False)

    class _RAMPER_V_TARGET(Register):

        class _RAMPER_V_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_TARGET", parent, access, address, block, signed)
            self.RAMPER_V_TARGET  =  self._RAMPER_V_TARGET(self,  Access.RW,  0x0FFFFFFF,  0,  signed=True)

    class _RAMPER_SWITCH_MODE(Register):

        class _STOP_L_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_L_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_R_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_R_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_H_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_H_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_L_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_L_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_R_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_R_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_H_POL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_H_POL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SWAP_LR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SWAP_LR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_L_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_L_INACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_L_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_R_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_R_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_R_INACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_R_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_H_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_H_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LATCH_H_INACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_H_INACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SG_STOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SG_STOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SOFTSTOP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SOFTSTOP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SW_HARD_STOP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SW_HARD_STOP", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_ON_POS_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_ON_POS_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STOP_ON_VEL_DEVIATION(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_ON_VEL_DEVIATION", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VELOCITY_OVERWRITE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_OVERWRITE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_SWITCH_MODE", parent, access, address, block, signed)
            self.STOP_L_ENABLE          =  self._STOP_L_ENABLE(        self,  Access.RW,  0x00000001,  0,   signed=False)
            self.STOP_R_ENABLE          =  self._STOP_R_ENABLE(        self,  Access.RW,  0x00000002,  1,   signed=False)
            self.STOP_H_ENABLE          =  self._STOP_H_ENABLE(        self,  Access.RW,  0x00000004,  2,   signed=False)
            self.STOP_L_POL             =  self._STOP_L_POL(           self,  Access.RW,  0x00000008,  3,   signed=False)
            self.STOP_R_POL             =  self._STOP_R_POL(           self,  Access.RW,  0x00000010,  4,   signed=False)
            self.STOP_H_POL             =  self._STOP_H_POL(           self,  Access.RW,  0x00000020,  5,   signed=False)
            self.SWAP_LR                =  self._SWAP_LR(              self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LATCH_L_ACTIVE         =  self._LATCH_L_ACTIVE(       self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LATCH_L_INACTIVE       =  self._LATCH_L_INACTIVE(     self,  Access.RW,  0x00000100,  8,   signed=False)
            self.LATCH_R_ACTIVE         =  self._LATCH_R_ACTIVE(       self,  Access.RW,  0x00000200,  9,   signed=False)
            self.LATCH_R_INACTIVE       =  self._LATCH_R_INACTIVE(     self,  Access.RW,  0x00000400,  10,  signed=False)
            self.LATCH_H_ACTIVE         =  self._LATCH_H_ACTIVE(       self,  Access.RW,  0x00000800,  11,  signed=False)
            self.LATCH_H_INACTIVE       =  self._LATCH_H_INACTIVE(     self,  Access.RW,  0x00001000,  12,  signed=False)
            self.SG_STOP_ENABLE         =  self._SG_STOP_ENABLE(       self,  Access.RW,  0x00004000,  14,  signed=False)
            self.SOFTSTOP_ENABLE        =  self._SOFTSTOP_ENABLE(      self,  Access.RW,  0x00008000,  15,  signed=False)
            self.SW_HARD_STOP           =  self._SW_HARD_STOP(         self,  Access.RW,  0x00010000,  16,  signed=False)
            self.STOP_ON_POS_DEVIATION  =  self._STOP_ON_POS_DEVIATION(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.STOP_ON_VEL_DEVIATION  =  self._STOP_ON_VEL_DEVIATION(self,  Access.RW,  0x00040000,  18,  signed=False)
            self.VELOCITY_OVERWRITE     =  self._VELOCITY_OVERWRITE(   self,  Access.RW,  0x00080000,  19,  signed=False)

    class _RAMPER_TIME_CONFIG(Register):

        class _T_ZEROWAIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_ZEROWAIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_VMAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_VMAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_TIME_CONFIG", parent, access, address, block, signed)
            self.T_ZEROWAIT  =  self._T_ZEROWAIT(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.T_VMAX      =  self._T_VMAX(    self,  Access.RW,  0xFFFF0000,  16,  signed=False)

    class _RAMPER_A_ACTUAL(Register):

        class _RAMPER_A_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_A_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_A_ACTUAL", parent, access, address, block, signed)
            self.RAMPER_A_ACTUAL  =  self._RAMPER_A_ACTUAL(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

    class _RAMPER_X_ACTUAL(Register):

        class _RAMPER_X_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_X_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_X_ACTUAL", parent, access, address, block, signed)
            self.RAMPER_X_ACTUAL  =  self._RAMPER_X_ACTUAL(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _RAMPER_V_ACTUAL(Register):

        class _RAMPER_V_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_V_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_V_ACTUAL", parent, access, address, block, signed)
            self.RAMPER_V_ACTUAL  =  self._RAMPER_V_ACTUAL(self,  Access.R,  0x0FFFFFFF,  0,  signed=True)

    class _RAMPER_X_TARGET(Register):

        class _RAMPER_X_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_X_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_X_TARGET", parent, access, address, block, signed)
            self.RAMPER_X_TARGET  =  self._RAMPER_X_TARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _RAMPER_PHI_E(Register):

        class _RAMPER_PHI_E(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_PHI_E", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_PHI_E", parent, access, address, block, signed)
            self.RAMPER_PHI_E  =  self._RAMPER_PHI_E(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _RAMPER_PHI_E_OFFSET(Register):

        class _RAMPER_PHI_E_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_PHI_E_OFFSET", parent, access, address, block, signed)
            self.RAMPER_PHI_E_OFFSET  =  self._RAMPER_PHI_E_OFFSET(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

    class _RAMPER_ACC_FF(Register):

        class _GAIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GAIN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SHIFT(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.SHIFT_0 = Choice(0, parent)
                    self.SHIFT_4 = Choice(1, parent)
                    self.SHIFT_8 = Choice(2, parent)
                    self.SHIFT_12 = Choice(3, parent)
                    self.SHIFT_16 = Choice(4, parent)
                    self.SHIFT_20 = Choice(5, parent)
                    self.SHIFT_24 = Choice(6, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHIFT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_ACC_FF", parent, access, address, block, signed)
            self.GAIN   =  self._GAIN( self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.SHIFT  =  self._SHIFT(self,  Access.RW,  0x00070000,  16,  signed=False)

    class _RAMPER_X_ACTUAL_LATCH(Register):

        class _RAMPER_X_ACTUAL_LATCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMPER_X_ACTUAL_LATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("RAMPER_X_ACTUAL_LATCH", parent, access, address, block, signed)
            self.RAMPER_X_ACTUAL_LATCH  =  self._RAMPER_X_ACTUAL_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _POSITION_ACTUAL_LATCH(Register):

        class _POSITION_ACTUAL_LATCH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_ACTUAL_LATCH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("POSITION_ACTUAL_LATCH", parent, access, address, block, signed)
            self.POSITION_ACTUAL_LATCH  =  self._POSITION_ACTUAL_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PRBS_AMPLITUDE(Register):

        class _PRBS_AMPLITUDE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PRBS_AMPLITUDE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PRBS_AMPLITUDE", parent, access, address, block, signed)
            self.PRBS_AMPLITUDE  =  self._PRBS_AMPLITUDE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PRBS_DOWN_SAMPLING_RATIO(Register):

        class _PRBS_DOWN_SAMPLING_RATIO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PRBS_DOWN_SAMPLING_RATIO", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PRBS_DOWN_SAMPLING_RATIO", parent, access, address, block, signed)
            self.PRBS_DOWN_SAMPLING_RATIO  =  self._PRBS_DOWN_SAMPLING_RATIO(self,  Access.RW,  0x000000FF,  0,  signed=False)

    class _PID_CONFIG(Register):

        class _KEEP_POS_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("KEEP_POS_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CURRENT_NORM_P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_NORM_P", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CURRENT_NORM_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_NORM_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VELOCITY_NORM_P(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.SHIFT_0 = Choice(0, parent)
                    self.SHIFT_8 = Choice(1, parent)
                    self.SHIFT_16 = Choice(2, parent)
                    self.SHIFT_24 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_NORM_P", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _VELOCITY_NORM_I(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.SHIFT_8 = Choice(0, parent)
                    self.SHIFT_16 = Choice(1, parent)
                    self.SHIFT_24 = Choice(2, parent)
                    self.SHIFT_32 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_NORM_I", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _POSITION_NORM_P(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.SHIFT_0 = Choice(0, parent)
                    self.SHIFT_8 = Choice(1, parent)
                    self.SHIFT_16 = Choice(2, parent)
                    self.SHIFT_24 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_NORM_P", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _POSITION_NORM_I(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.SHIFT_8 = Choice(0, parent)
                    self.SHIFT_16 = Choice(1, parent)
                    self.SHIFT_24 = Choice(2, parent)
                    self.SHIFT_32 = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_NORM_I", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _VEL_SCALE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEL_SCALE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POS_SMPL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POS_SMPL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VEL_SMPL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEL_SMPL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_CONFIG", parent, access, address, block, signed)
            self.KEEP_POS_TARGET  =  self._KEEP_POS_TARGET(self,  Access.RW,  0x00000001,  0,   signed=False)
            self.CURRENT_NORM_P   =  self._CURRENT_NORM_P( self,  Access.RW,  0x00000004,  2,   signed=False)
            self.CURRENT_NORM_I   =  self._CURRENT_NORM_I( self,  Access.RW,  0x00000008,  3,   signed=False)
            self.VELOCITY_NORM_P  =  self._VELOCITY_NORM_P(self,  Access.RW,  0x00000030,  4,   signed=False)
            self.VELOCITY_NORM_I  =  self._VELOCITY_NORM_I(self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.POSITION_NORM_P  =  self._POSITION_NORM_P(self,  Access.RW,  0x00000300,  8,   signed=False)
            self.POSITION_NORM_I  =  self._POSITION_NORM_I(self,  Access.RW,  0x00000C00,  10,  signed=False)
            self.VEL_SCALE        =  self._VEL_SCALE(      self,  Access.RW,  0x0000F000,  12,  signed=False)
            self.POS_SMPL         =  self._POS_SMPL(       self,  Access.RW,  0x007F0000,  16,  signed=False)
            self.VEL_SMPL         =  self._VEL_SMPL(       self,  Access.RW,  0x7F000000,  24,  signed=False)

    class _PID_FLUX_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_FLUX_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_TORQUE_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_FIELDWEAK_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_FIELDWEAK_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_U_S_MAX(Register):

        class _U_S_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U_S_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_U_S_MAX", parent, access, address, block, signed)
            self.U_S_MAX  =  self._U_S_MAX(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _PID_VELOCITY_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_POSITION_COEFF(Register):

        class _I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _P(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_COEFF", parent, access, address, block, signed)
            self.I  =  self._I(self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.P  =  self._P(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_POSITION_TOLERANCE(Register):

        class _PID_POSITION_TOLERANCE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TOLERANCE", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_TOLERANCE", parent, access, address, block, signed)
            self.PID_POSITION_TOLERANCE  =  self._PID_POSITION_TOLERANCE(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

    class _PID_POSITION_TOLERANCE_DELAY(Register):

        class _PID_POSITION_TOLERANCE_DELAY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TOLERANCE_DELAY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_TOLERANCE_DELAY", parent, access, address, block, signed)
            self.PID_POSITION_TOLERANCE_DELAY  =  self._PID_POSITION_TOLERANCE_DELAY(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _PID_UQ_UD_LIMITS(Register):

        class _PID_UQ_UD_LIMITS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_UQ_UD_LIMITS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_UQ_UD_LIMITS", parent, access, address, block, signed)
            self.PID_UQ_UD_LIMITS  =  self._PID_UQ_UD_LIMITS(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _PID_TORQUE_FLUX_LIMITS(Register):

        class _PID_FLUX_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_FLUX_LIMITS", parent, access, address, block, signed)
            self.PID_FLUX_LIMIT    =  self._PID_FLUX_LIMIT(  self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.PID_TORQUE_LIMIT  =  self._PID_TORQUE_LIMIT(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

    class _PID_VELOCITY_LIMIT(Register):

        class _PID_VELOCITY_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_LIMIT", parent, access, address, block, signed)
            self.PID_VELOCITY_LIMIT  =  self._PID_VELOCITY_LIMIT(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

    class _PID_POSITION_LIMIT_LOW(Register):

        class _PID_POSITION_LIMIT_LOW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_LIMIT_LOW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_LIMIT_LOW", parent, access, address, block, signed)
            self.PID_POSITION_LIMIT_LOW  =  self._PID_POSITION_LIMIT_LOW(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_LIMIT_HIGH(Register):

        class _PID_POSITION_LIMIT_HIGH(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_LIMIT_HIGH", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_LIMIT_HIGH", parent, access, address, block, signed)
            self.PID_POSITION_LIMIT_HIGH  =  self._PID_POSITION_LIMIT_HIGH(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_TORQUE_FLUX_TARGET(Register):

        class _PID_FLUX_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_FLUX_TARGET", parent, access, address, block, signed)
            self.PID_FLUX_TARGET    =  self._PID_FLUX_TARGET(  self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.PID_TORQUE_TARGET  =  self._PID_TORQUE_TARGET(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _PID_TORQUE_FLUX_OFFSET(Register):

        class _PID_FLUX_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_FLUX_OFFSET", parent, access, address, block, signed)
            self.PID_FLUX_OFFSET    =  self._PID_FLUX_OFFSET(  self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.PID_TORQUE_OFFSET  =  self._PID_TORQUE_OFFSET(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _PID_VELOCITY_TARGET(Register):

        class _PID_VELOCITY_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_TARGET", parent, access, address, block, signed)
            self.PID_VELOCITY_TARGET  =  self._PID_VELOCITY_TARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_VELOCITY_OFFSET(Register):

        class _PID_VELOCITY_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_OFFSET", parent, access, address, block, signed)
            self.PID_VELOCITY_OFFSET  =  self._PID_VELOCITY_OFFSET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_TARGET(Register):

        class _PID_POSITION_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_TARGET", parent, access, address, block, signed)
            self.PID_POSITION_TARGET  =  self._PID_POSITION_TARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_TORQUE_FLUX_ACTUAL(Register):

        class _PID_FLUX_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_TORQUE_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_FLUX_ACTUAL", parent, access, address, block, signed)
            self.PID_FLUX_ACTUAL    =  self._PID_FLUX_ACTUAL(  self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.PID_TORQUE_ACTUAL  =  self._PID_TORQUE_ACTUAL(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _PID_VELOCITY_ACTUAL(Register):

        class _PID_VELOCITY_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_ACTUAL", parent, access, address, block, signed)
            self.PID_VELOCITY_ACTUAL  =  self._PID_VELOCITY_ACTUAL(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_ACTUAL(Register):

        class _PID_POSITION_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_ACTUAL", parent, access, address, block, signed)
            self.PID_POSITION_ACTUAL  =  self._PID_POSITION_ACTUAL(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_ACTUAL_OFFSET(Register):

        class _PID_POSITION_ACTUAL_OFFSET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ACTUAL_OFFSET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_ACTUAL_OFFSET", parent, access, address, block, signed)
            self.PID_POSITION_ACTUAL_OFFSET  =  self._PID_POSITION_ACTUAL_OFFSET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_TORQUE_ERROR(Register):

        class _PID_TORQUE_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_ERROR", parent, access, address, block, signed)
            self.PID_TORQUE_ERROR  =  self._PID_TORQUE_ERROR(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _PID_FLUX_ERROR(Register):

        class _PID_FLUX_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_FLUX_ERROR", parent, access, address, block, signed)
            self.PID_FLUX_ERROR  =  self._PID_FLUX_ERROR(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _PID_VELOCITY_ERROR(Register):

        class _PID_VELOCITY_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_ERROR", parent, access, address, block, signed)
            self.PID_VELOCITY_ERROR  =  self._PID_VELOCITY_ERROR(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_ERROR(Register):

        class _PID_POSITION_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_ERROR", parent, access, address, block, signed)
            self.PID_POSITION_ERROR  =  self._PID_POSITION_ERROR(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PID_TORQUE_INTEGRATOR(Register):

        class _PID_TORQUE_INTEGRATOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_INTEGRATOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_TORQUE_INTEGRATOR", parent, access, address, block, signed)
            self.PID_TORQUE_INTEGRATOR  =  self._PID_TORQUE_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_FLUX_INTEGRATOR(Register):

        class _PID_FLUX_INTEGRATOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_INTEGRATOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_FLUX_INTEGRATOR", parent, access, address, block, signed)
            self.PID_FLUX_INTEGRATOR  =  self._PID_FLUX_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_VELOCITY_INTEGRATOR(Register):

        class _PID_VELOCITY_INTEGRATOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_INTEGRATOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_VELOCITY_INTEGRATOR", parent, access, address, block, signed)
            self.PID_VELOCITY_INTEGRATOR  =  self._PID_VELOCITY_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PID_POSITION_INTEGRATOR(Register):

        class _PID_POSITION_INTEGRATOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_INTEGRATOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PID_POSITION_INTEGRATOR", parent, access, address, block, signed)
            self.PID_POSITION_INTEGRATOR  =  self._PID_POSITION_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    class _PIDIN_TORQUE_FLUX_TARGET(Register):

        class _PIDIN_FLUX_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_FLUX_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIDIN_TORQUE_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_TORQUE_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_TORQUE_FLUX_TARGET", parent, access, address, block, signed)
            self.PIDIN_FLUX_TARGET    =  self._PIDIN_FLUX_TARGET(  self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.PIDIN_TORQUE_TARGET  =  self._PIDIN_TORQUE_TARGET(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _PIDIN_VELOCITY_TARGET(Register):

        class _PIDIN_VELOCITY_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_VELOCITY_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_VELOCITY_TARGET", parent, access, address, block, signed)
            self.PIDIN_VELOCITY_TARGET  =  self._PIDIN_VELOCITY_TARGET(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PIDIN_POSITION_TARGET(Register):

        class _PIDIN_POSITION_TARGET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_POSITION_TARGET", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_POSITION_TARGET", parent, access, address, block, signed)
            self.PIDIN_POSITION_TARGET  =  self._PIDIN_POSITION_TARGET(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PIDIN_TORQUE_FLUX_TARGET_LIMITED(Register):

        class _PIDIN_FLUX_TARGET_LIMITED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_FLUX_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PIDIN_TORQUE_TARGET_LIMITED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_TORQUE_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_TORQUE_FLUX_TARGET_LIMITED", parent, access, address, block, signed)
            self.PIDIN_FLUX_TARGET_LIMITED    =  self._PIDIN_FLUX_TARGET_LIMITED(  self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.PIDIN_TORQUE_TARGET_LIMITED  =  self._PIDIN_TORQUE_TARGET_LIMITED(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _PIDIN_VELOCITY_TARGET_LIMITED(Register):

        class _PIDIN_VELOCITY_TARGET_LIMITED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_VELOCITY_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_VELOCITY_TARGET_LIMITED", parent, access, address, block, signed)
            self.PIDIN_VELOCITY_TARGET_LIMITED  =  self._PIDIN_VELOCITY_TARGET_LIMITED(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _PIDIN_POSITION_TARGET_LIMITED(Register):

        class _PIDIN_POSITION_TARGET_LIMITED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_POSITION_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PIDIN_POSITION_TARGET_LIMITED", parent, access, address, block, signed)
            self.PIDIN_POSITION_TARGET_LIMITED  =  self._PIDIN_POSITION_TARGET_LIMITED(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _FOC_IBETA_IALPHA(Register):

        class _IALPHA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IALPHA", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IBETA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IBETA", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_IBETA_IALPHA", parent, access, address, block, signed)
            self.IALPHA  =  self._IALPHA(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.IBETA   =  self._IBETA( self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_IQ_ID(Register):

        class _ID(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ID", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_IQ_ID", parent, access, address, block, signed)
            self.ID  =  self._ID(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.IQ  =  self._IQ(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UQ_UD(Register):

        class _UD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UQ_UD", parent, access, address, block, signed)
            self.UD  =  self._UD(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UQ  =  self._UQ(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UQ_UD_LIMITED(Register):

        class _UD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UQ_UD_LIMITED", parent, access, address, block, signed)
            self.UD  =  self._UD(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UQ  =  self._UQ(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UBETA_UALPHA(Register):

        class _UALPHA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UALPHA", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UBETA(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UBETA", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UBETA_UALPHA", parent, access, address, block, signed)
            self.UALPHA  =  self._UALPHA(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UBETA   =  self._UBETA( self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UWY_UUX(Register):

        class _UUX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UUX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UWY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UWY", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UWY_UUX", parent, access, address, block, signed)
            self.UUX  =  self._UUX(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UWY  =  self._UWY(self,  Access.R,  0xFFFF0000,  16,  signed=True)

    class _FOC_UV(Register):

        class _UV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FOC_UV", parent, access, address, block, signed)
            self.UV  =  self._UV(self,  Access.R,  0x0000FFFF,  0,  signed=True)

    class _PWM_VX2_UX1(Register):

        class _UX1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UX1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VX2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VX2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_VX2_UX1", parent, access, address, block, signed)
            self.UX1  =  self._UX1(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.VX2  =  self._VX2(self,  Access.R,  0xFFFF0000,  16,  signed=False)

    class _PWM_Y2_WY1(Register):

        class _WY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_Y2_WY1", parent, access, address, block, signed)
            self.WY1  =  self._WY1(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.Y2   =  self._Y2( self,  Access.R,  0xFFFF0000,  16,  signed=False)

    class _VELOCITY_FRQ(Register):

        class _VELOCITY_FRQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_FRQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_FRQ", parent, access, address, block, signed)
            self.VELOCITY_FRQ  =  self._VELOCITY_FRQ(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _VELOCITY_PER(Register):

        class _VELOCITY_PER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_PER", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_PER", parent, access, address, block, signed)
            self.VELOCITY_PER  =  self._VELOCITY_PER(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

    class _U_S_ACTUAL_I_S_ACTUAL(Register):

        class _I_S_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I_S_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _U_S_ACTUAL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U_S_ACTUAL", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("U_S_ACTUAL_I_S_ACTUAL", parent, access, address, block, signed)
            self.I_S_ACTUAL  =  self._I_S_ACTUAL(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.U_S_ACTUAL  =  self._U_S_ACTUAL(self,  Access.R,  0xFFFF0000,  16,  signed=False)

    class _P_MOTOR(Register):

        class _P_MOTOR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P_MOTOR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("P_MOTOR", parent, access, address, block, signed)
            self.P_MOTOR  =  self._P_MOTOR(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

    class _INPUTS_RAW(Register):

        class _ENC_A(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_A", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENC_B(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_B", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENC_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENI", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_U_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_U_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_V_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_V_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_W_FILT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_W_FILT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("INPUTS_RAW", parent, access, address, block, signed)
            self.ENC_A        =  self._ENC_A(      self,  Access.R,  0x00000001,  0,   signed=False)
            self.ENC_B        =  self._ENC_B(      self,  Access.R,  0x00000002,  1,   signed=False)
            self.ENC_N        =  self._ENC_N(      self,  Access.R,  0x00000004,  2,   signed=False)
            self.HALL_U       =  self._HALL_U(     self,  Access.R,  0x00000100,  8,   signed=False)
            self.HALL_V       =  self._HALL_V(     self,  Access.R,  0x00000200,  9,   signed=False)
            self.HALL_W       =  self._HALL_W(     self,  Access.R,  0x00000400,  10,  signed=False)
            self.REF_SW_R     =  self._REF_SW_R(   self,  Access.R,  0x00001000,  12,  signed=False)
            self.REF_SW_L     =  self._REF_SW_L(   self,  Access.R,  0x00002000,  13,  signed=False)
            self.REF_SW_H     =  self._REF_SW_H(   self,  Access.R,  0x00004000,  14,  signed=False)
            self.ENI          =  self._ENI(        self,  Access.R,  0x00008000,  15,  signed=False)
            self.HALL_U_FILT  =  self._HALL_U_FILT(self,  Access.R,  0x00100000,  20,  signed=False)
            self.HALL_V_FILT  =  self._HALL_V_FILT(self,  Access.R,  0x00200000,  21,  signed=False)
            self.HALL_W_FILT  =  self._HALL_W_FILT(self,  Access.R,  0x00400000,  22,  signed=False)

    class _OUTPUTS_RAW(Register):

        class _PWM_UX1_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_UX1_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_UX1_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_UX1_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_VX2_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_VX2_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_VX2_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_VX2_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_WY1_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_WY1_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_WY1_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_WY1_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_Y2_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_Y2_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_Y2_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_Y2_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("OUTPUTS_RAW", parent, access, address, block, signed)
            self.PWM_UX1_L  =  self._PWM_UX1_L(self,  Access.R,  0x00000001,  0,  signed=False)
            self.PWM_UX1_H  =  self._PWM_UX1_H(self,  Access.R,  0x00000002,  1,  signed=False)
            self.PWM_VX2_L  =  self._PWM_VX2_L(self,  Access.R,  0x00000004,  2,  signed=False)
            self.PWM_VX2_H  =  self._PWM_VX2_H(self,  Access.R,  0x00000008,  3,  signed=False)
            self.PWM_WY1_L  =  self._PWM_WY1_L(self,  Access.R,  0x00000010,  4,  signed=False)
            self.PWM_WY1_H  =  self._PWM_WY1_H(self,  Access.R,  0x00000020,  5,  signed=False)
            self.PWM_Y2_L   =  self._PWM_Y2_L( self,  Access.R,  0x00000040,  6,  signed=False)
            self.PWM_Y2_H   =  self._PWM_Y2_H( self,  Access.R,  0x00000080,  7,  signed=False)

    class _STATUS_FLAGS(Register):

        class _PID_X_TARGET_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_X_TARGET_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_X_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_X_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_V_TARGET_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_V_TARGET_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_V_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_V_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_ID_TARGET_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_ID_TARGET_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_ID_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_ID_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_IQ_TARGET_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_IQ_TARGET_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_IQ_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_IQ_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _IPARK_VOLTLIM_LIMIT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IPARK_VOLTLIM_LIMIT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PWM_SWITCH_LIMIT_ACTIVE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_SWITCH_LIMIT_ACTIVE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HALL_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_TRACKING_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_TRACKING_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VELOCITY_TRACKING_ERROR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_TRACKING_ERROR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PID_FW_OUTPUT_LIMIT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FW_OUTPUT_LIMIT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _WATCHDOG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WATCHDOG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SHORT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHORT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_L(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_L", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_R(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_R", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _REF_SW_H(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_SW_H", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _POSITION_REACHED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_REACHED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADC_I_CLIPPED(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_CLIPPED", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENC_N(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_N", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENI(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENI", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("STATUS_FLAGS", parent, access, address, block, signed)
            self.PID_X_TARGET_LIMIT       =  self._PID_X_TARGET_LIMIT(     self,  Access.RWC,  0x00000001,  0,   signed=False)
            self.PID_X_OUTPUT_LIMIT       =  self._PID_X_OUTPUT_LIMIT(     self,  Access.RWC,  0x00000002,  1,   signed=False)
            self.PID_V_TARGET_LIMIT       =  self._PID_V_TARGET_LIMIT(     self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.PID_V_OUTPUT_LIMIT       =  self._PID_V_OUTPUT_LIMIT(     self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.PID_ID_TARGET_LIMIT      =  self._PID_ID_TARGET_LIMIT(    self,  Access.RWC,  0x00000010,  4,   signed=False)
            self.PID_ID_OUTPUT_LIMIT      =  self._PID_ID_OUTPUT_LIMIT(    self,  Access.RWC,  0x00000020,  5,   signed=False)
            self.PID_IQ_TARGET_LIMIT      =  self._PID_IQ_TARGET_LIMIT(    self,  Access.RWC,  0x00000040,  6,   signed=False)
            self.PID_IQ_OUTPUT_LIMIT      =  self._PID_IQ_OUTPUT_LIMIT(    self,  Access.RWC,  0x00000080,  7,   signed=False)
            self.IPARK_VOLTLIM_LIMIT_U    =  self._IPARK_VOLTLIM_LIMIT_U(  self,  Access.RWC,  0x00000100,  8,   signed=False)
            self.PWM_SWITCH_LIMIT_ACTIVE  =  self._PWM_SWITCH_LIMIT_ACTIVE(self,  Access.RWC,  0x00000200,  9,   signed=False)
            self.HALL_ERROR               =  self._HALL_ERROR(             self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.POSITION_TRACKING_ERROR  =  self._POSITION_TRACKING_ERROR(self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.VELOCITY_TRACKING_ERROR  =  self._VELOCITY_TRACKING_ERROR(self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.PID_FW_OUTPUT_LIMIT      =  self._PID_FW_OUTPUT_LIMIT(    self,  Access.RWC,  0x00004000,  14,  signed=False)
            self.WATCHDOG                 =  self._WATCHDOG(               self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.SHORT                    =  self._SHORT(                  self,  Access.RWC,  0x00020000,  17,  signed=False)
            self.REF_SW_L                 =  self._REF_SW_L(               self,  Access.RWC,  0x00100000,  20,  signed=False)
            self.REF_SW_R                 =  self._REF_SW_R(               self,  Access.RWC,  0x00200000,  21,  signed=False)
            self.REF_SW_H                 =  self._REF_SW_H(               self,  Access.RWC,  0x00400000,  22,  signed=False)
            self.POSITION_REACHED         =  self._POSITION_REACHED(       self,  Access.RWC,  0x00800000,  23,  signed=False)
            self.ADC_I_CLIPPED            =  self._ADC_I_CLIPPED(          self,  Access.RWC,  0x04000000,  26,  signed=False)
            self.ENC_N                    =  self._ENC_N(                  self,  Access.RWC,  0x10000000,  28,  signed=False)
            self.ENI                      =  self._ENI(                    self,  Access.RWC,  0x80000000,  31,  signed=False)

    class _GDRV_HW(Register):

        class _BRIDGE_ENABLE_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BRIDGE_ENABLE_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BRIDGE_ENABLE_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BRIDGE_ENABLE_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BRIDGE_ENABLE_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BRIDGE_ENABLE_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BRIDGE_ENABLE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BRIDGE_ENABLE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_OCP_CMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_CMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_OCP_CMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_CMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO_CMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO_CMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_CMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_CMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_ILIM_MAX(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_ILIM_MAX", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_SW_CP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_SW_CP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHARGEPUMP_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHARGEPUMP_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BIAS_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BIAS_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_AS_LS_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_AS_LS_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_HW", parent, access, address, block, signed)
            self.BRIDGE_ENABLE_U   =  self._BRIDGE_ENABLE_U( self,  Access.RW,  0x00000001,  0,   signed=False)
            self.BRIDGE_ENABLE_V   =  self._BRIDGE_ENABLE_V( self,  Access.RW,  0x00000002,  1,   signed=False)
            self.BRIDGE_ENABLE_W   =  self._BRIDGE_ENABLE_W( self,  Access.RW,  0x00000004,  2,   signed=False)
            self.BRIDGE_ENABLE_Y2  =  self._BRIDGE_ENABLE_Y2(self,  Access.RW,  0x00000008,  3,   signed=False)
            self.LS_OCP_CMP_EN     =  self._LS_OCP_CMP_EN(   self,  Access.RW,  0x00000010,  4,   signed=False)
            self.HS_OCP_CMP_EN     =  self._HS_OCP_CMP_EN(   self,  Access.RW,  0x00000020,  5,   signed=False)
            self.VDRV_UVLO_CMP_EN  =  self._VDRV_UVLO_CMP_EN(self,  Access.RW,  0x00000040,  6,   signed=False)
            self.VS_UVLO_CMP_EN    =  self._VS_UVLO_CMP_EN(  self,  Access.RW,  0x00000080,  7,   signed=False)
            self.BST_ILIM_MAX      =  self._BST_ILIM_MAX(    self,  Access.RW,  0x00000700,  8,   signed=False)
            self.BST_SW_CP_EN      =  self._BST_SW_CP_EN(    self,  Access.RW,  0x00000800,  11,  signed=False)
            self.CHARGEPUMP_EN     =  self._CHARGEPUMP_EN(   self,  Access.RW,  0x01000000,  24,  signed=False)
            self.BIAS_EN           =  self._BIAS_EN(         self,  Access.RW,  0x02000000,  25,  signed=False)
            self.HS_AS_LS_Y2       =  self._HS_AS_LS_Y2(     self,  Access.RW,  0x10000000,  28,  signed=False)

    class _GDRV_CFG(Register):

        class _IGATE_SINK_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.SINK_50MA = Choice(0, parent)
                    self.SINK_100MA = Choice(1, parent)
                    self.SINK_160MA = Choice(2, parent)
                    self.SINK_210MA = Choice(3, parent)
                    self.SINK_270MA = Choice(4, parent)
                    self.SINK_320MA = Choice(5, parent)
                    self.SINK_380MA = Choice(6, parent)
                    self.SINK_430MA = Choice(7, parent)
                    self.SINK_580MA = Choice(8, parent)
                    self.SINK_720MA = Choice(9, parent)
                    self.SINK_860MA = Choice(10, parent)
                    self.SINK_1000MA = Choice(11, parent)
                    self.SINK_1250MA = Choice(12, parent)
                    self.SINK_1510MA = Choice(13, parent)
                    self.SINK_1770MA = Choice(14, parent)
                    self.SINK_2000MA = Choice(15, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGATE_SINK_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _IGATE_SOURCE_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.SOURCE_25MA = Choice(0, parent)
                    self.SOURCE_50MA = Choice(1, parent)
                    self.SOURCE_80MA = Choice(2, parent)
                    self.SOURCE_105MA = Choice(3, parent)
                    self.SOURCE_135MA = Choice(4, parent)
                    self.SOURCE_160MA = Choice(5, parent)
                    self.SOURCE_190MA = Choice(6, parent)
                    self.SOURCE_215MA = Choice(7, parent)
                    self.SOURCE_290MA = Choice(8, parent)
                    self.SOURCE_360MA = Choice(9, parent)
                    self.SOURCE_430MA = Choice(10, parent)
                    self.SOURCE_500MA = Choice(11, parent)
                    self.SOURCE_625MA = Choice(12, parent)
                    self.SOURCE_755MA = Choice(13, parent)
                    self.SOURCE_885MA = Choice(14, parent)
                    self.SOURCE_1000MA = Choice(15, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGATE_SOURCE_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _IGATE_SINK_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.SINK_50MA = Choice(0, parent)
                    self.SINK_100MA = Choice(1, parent)
                    self.SINK_160MA = Choice(2, parent)
                    self.SINK_210MA = Choice(3, parent)
                    self.SINK_270MA = Choice(4, parent)
                    self.SINK_320MA = Choice(5, parent)
                    self.SINK_380MA = Choice(6, parent)
                    self.SINK_430MA = Choice(7, parent)
                    self.SINK_580MA = Choice(8, parent)
                    self.SINK_720MA = Choice(9, parent)
                    self.SINK_860MA = Choice(10, parent)
                    self.SINK_1000MA = Choice(11, parent)
                    self.SINK_1250MA = Choice(12, parent)
                    self.SINK_1510MA = Choice(13, parent)
                    self.SINK_1770MA = Choice(14, parent)
                    self.SINK_2000MA = Choice(15, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGATE_SINK_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _IGATE_SOURCE_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.SOURCE_25MA = Choice(0, parent)
                    self.SOURCE_50MA = Choice(1, parent)
                    self.SOURCE_80MA = Choice(2, parent)
                    self.SOURCE_105MA = Choice(3, parent)
                    self.SOURCE_135MA = Choice(4, parent)
                    self.SOURCE_160MA = Choice(5, parent)
                    self.SOURCE_190MA = Choice(6, parent)
                    self.SOURCE_215MA = Choice(7, parent)
                    self.SOURCE_290MA = Choice(8, parent)
                    self.SOURCE_360MA = Choice(9, parent)
                    self.SOURCE_430MA = Choice(10, parent)
                    self.SOURCE_500MA = Choice(11, parent)
                    self.SOURCE_625MA = Choice(12, parent)
                    self.SOURCE_755MA = Choice(13, parent)
                    self.SOURCE_885MA = Choice(14, parent)
                    self.SOURCE_1000MA = Choice(15, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IGATE_SOURCE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _ADAPTIVE_MODE_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADAPTIVE_MODE_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ADAPTIVE_MODE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADAPTIVE_MODE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_LVL(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.VSUVLO_44 = Choice(0, parent)
                    self.VSUVLO_46 = Choice(1, parent)
                    self.VSUVLO_48 = Choice(2, parent)
                    self.VSUVLO_50 = Choice(3, parent)
                    self.VSUVLO_52 = Choice(4, parent)
                    self.VSUVLO_54 = Choice(5, parent)
                    self.VSUVLO_56 = Choice(6, parent)
                    self.VSUVLO_58 = Choice(7, parent)
                    self.VSUVLO_60 = Choice(8, parent)
                    self.VSUVLO_63 = Choice(9, parent)
                    self.VSUVLO_66 = Choice(10, parent)
                    self.VSUVLO_69 = Choice(11, parent)
                    self.VSUVLO_72 = Choice(12, parent)
                    self.VSUVLO_75 = Choice(13, parent)
                    self.VSUVLO_78 = Choice(14, parent)
                    self.VSUVLO_81 = Choice(15, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_LVL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_CFG", parent, access, address, block, signed)
            self.IGATE_SINK_UVW     =  self._IGATE_SINK_UVW(   self,  Access.RW,  0x0000000F,  0,   signed=False)
            self.IGATE_SOURCE_UVW   =  self._IGATE_SOURCE_UVW( self,  Access.RW,  0x000000F0,  4,   signed=False)
            self.IGATE_SINK_Y2      =  self._IGATE_SINK_Y2(    self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.IGATE_SOURCE_Y2    =  self._IGATE_SOURCE_Y2(  self,  Access.RW,  0x0000F000,  12,  signed=False)
            self.ADAPTIVE_MODE_UVW  =  self._ADAPTIVE_MODE_UVW(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.ADAPTIVE_MODE_Y2   =  self._ADAPTIVE_MODE_Y2( self,  Access.RW,  0x00020000,  17,  signed=False)
            self.VS_UVLO_LVL        =  self._VS_UVLO_LVL(      self,  Access.RW,  0x00F00000,  20,  signed=False)

    class _GDRV_TIMING(Register):

        class _T_DRIVE_SINK_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_DRIVE_SINK_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_DRIVE_SOURCE_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_DRIVE_SOURCE_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_DRIVE_SINK_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_DRIVE_SINK_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _T_DRIVE_SOURCE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_DRIVE_SOURCE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_TIMING", parent, access, address, block, signed)
            self.T_DRIVE_SINK_UVW    =  self._T_DRIVE_SINK_UVW(  self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.T_DRIVE_SOURCE_UVW  =  self._T_DRIVE_SOURCE_UVW(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.T_DRIVE_SINK_Y2     =  self._T_DRIVE_SINK_Y2(   self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.T_DRIVE_SOURCE_Y2   =  self._T_DRIVE_SOURCE_Y2( self,  Access.RW,  0xFF000000,  24,  signed=False)

    class _GDRV_BBM(Register):

        class _BBM_L_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BBM_L_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BBM_H_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BBM_H_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BBM_L_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BBM_L_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BBM_H_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BBM_H_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_BBM", parent, access, address, block, signed)
            self.BBM_L_UVW  =  self._BBM_L_UVW(self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.BBM_H_UVW  =  self._BBM_H_UVW(self,  Access.RW,  0x0000FF00,  8,   signed=False)
            self.BBM_L_Y2   =  self._BBM_L_Y2( self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.BBM_H_Y2   =  self._BBM_H_Y2( self,  Access.RW,  0xFF000000,  24,  signed=False)

    class _GDRV_PROT(Register):

        class _VGS_DEGLITCH_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.DEG_OFF = Choice(0, parent)
                    self.DEG_250NS = Choice(1, parent)
                    self.DEG_500NS = Choice(2, parent)
                    self.DEG_1000NS = Choice(3, parent)
                    self.DEG_2000NS = Choice(4, parent)
                    self.DEG_4000NS = Choice(5, parent)
                    self.DEG_6000NS = Choice(6, parent)
                    self.DEG_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VGS_DEGLITCH_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _VGS_BLANKING_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.BLK_OFF = Choice(0, parent)
                    self.BLK_250NS = Choice(1, parent)
                    self.BLK_500NS = Choice(2, parent)
                    self.BLK_1000NS = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VGS_BLANKING_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _VGS_DEGLITCH_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.DEG_OFF = Choice(0, parent)
                    self.DEG_250NS = Choice(1, parent)
                    self.DEG_500NS = Choice(2, parent)
                    self.DEG_1000NS = Choice(3, parent)
                    self.DEG_2000NS = Choice(4, parent)
                    self.DEG_4000NS = Choice(5, parent)
                    self.DEG_6000NS = Choice(6, parent)
                    self.DEG_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VGS_DEGLITCH_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _VGS_BLANKING_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.BLK_OFF = Choice(0, parent)
                    self.BLK_250NS = Choice(1, parent)
                    self.BLK_500NS = Choice(2, parent)
                    self.BLK_1000NS = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VGS_BLANKING_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _LS_RETRIES_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.OFF = Choice(0, parent)
                    self.ONE = Choice(1, parent)
                    self.TWO = Choice(2, parent)
                    self.THREE = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_RETRIES_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _HS_RETRIES_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.OFF = Choice(0, parent)
                    self.ONE = Choice(1, parent)
                    self.TWO = Choice(2, parent)
                    self.THREE = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_RETRIES_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _LS_RETRIES_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.OFF = Choice(0, parent)
                    self.ONE = Choice(1, parent)
                    self.TWO = Choice(2, parent)
                    self.THREE = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_RETRIES_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _HS_RETRIES_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.OFF = Choice(0, parent)
                    self.ONE = Choice(1, parent)
                    self.TWO = Choice(2, parent)
                    self.THREE = Choice(3, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_RETRIES_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _TERM_PWM_ON_SHORT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TERM_PWM_ON_SHORT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_PROT", parent, access, address, block, signed)
            self.VGS_DEGLITCH_UVW   =  self._VGS_DEGLITCH_UVW( self,  Access.RW,  0x00000007,  0,   signed=False)
            self.VGS_BLANKING_UVW   =  self._VGS_BLANKING_UVW( self,  Access.RW,  0x00000030,  4,   signed=False)
            self.VGS_DEGLITCH_Y2    =  self._VGS_DEGLITCH_Y2(  self,  Access.RW,  0x00000700,  8,   signed=False)
            self.VGS_BLANKING_Y2    =  self._VGS_BLANKING_Y2(  self,  Access.RW,  0x00003000,  12,  signed=False)
            self.LS_RETRIES_UVW     =  self._LS_RETRIES_UVW(   self,  Access.RW,  0x00030000,  16,  signed=False)
            self.HS_RETRIES_UVW     =  self._HS_RETRIES_UVW(   self,  Access.RW,  0x000C0000,  18,  signed=False)
            self.LS_RETRIES_Y2      =  self._LS_RETRIES_Y2(    self,  Access.RW,  0x00300000,  20,  signed=False)
            self.HS_RETRIES_Y2      =  self._HS_RETRIES_Y2(    self,  Access.RW,  0x00C00000,  22,  signed=False)
            self.TERM_PWM_ON_SHORT  =  self._TERM_PWM_ON_SHORT(self,  Access.RW,  0x10000000,  28,  signed=False)

    class _GDRV_OCP_UVW(Register):

        class _LS_OCP_DEGLITCH_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.DEG_OFF = Choice(0, parent)
                    self.DEG_250NS = Choice(1, parent)
                    self.DEG_500NS = Choice(2, parent)
                    self.DEG_1000NS = Choice(3, parent)
                    self.DEG_2000NS = Choice(4, parent)
                    self.DEG_4000NS = Choice(5, parent)
                    self.DEG_6000NS = Choice(6, parent)
                    self.DEG_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_DEGLITCH_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _LS_OCP_BLANKING_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.BLK_OFF = Choice(0, parent)
                    self.BLK_250NS = Choice(1, parent)
                    self.BLK_500NS = Choice(2, parent)
                    self.BLK_1000NS = Choice(3, parent)
                    self.BLK_2000NS = Choice(4, parent)
                    self.BLK_4000NS = Choice(5, parent)
                    self.BLK_6000NS = Choice(6, parent)
                    self.BLK_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_BLANKING_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _LS_OCP_THRES_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.THRES_80_63MV = Choice(0, parent)
                    self.THRES_165_125MV = Choice(1, parent)
                    self.THRES_250_187MV = Choice(2, parent)
                    self.THRES_330_248MV = Choice(3, parent)
                    self.THRES_415_312MV = Choice(4, parent)
                    self.THRES_500_374MV = Choice(5, parent)
                    self.THRES_582_434MV = Choice(6, parent)
                    self.THRES_660_504MV = Choice(7, parent)
                    self.THRES_125_705MV = Choice(8, parent)
                    self.THRES_250_940MV = Choice(9, parent)
                    self.THRES_375_1180MV = Choice(10, parent)
                    self.THRES_500_1410MV = Choice(11, parent)
                    self.THRES_625_1650MV = Choice(12, parent)
                    self.THRES_750_1880MV = Choice(13, parent)
                    self.THRES_873_2110MV = Choice(14, parent)
                    self.THRES_1000_2350MV = Choice(15, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_THRES_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _LS_OCP_USE_VDS_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_USE_VDS_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_OCP_DEGLITCH_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.DEG_OFF = Choice(0, parent)
                    self.DEG_250NS = Choice(1, parent)
                    self.DEG_500NS = Choice(2, parent)
                    self.DEG_1000NS = Choice(3, parent)
                    self.DEG_2000NS = Choice(4, parent)
                    self.DEG_4000NS = Choice(5, parent)
                    self.DEG_6000NS = Choice(6, parent)
                    self.DEG_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_DEGLITCH_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _HS_OCP_BLANKING_UVW(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.BLK_OFF = Choice(0, parent)
                    self.BLK_250NS = Choice(1, parent)
                    self.BLK_500NS = Choice(2, parent)
                    self.BLK_1000NS = Choice(3, parent)
                    self.BLK_2000NS = Choice(4, parent)
                    self.BLK_4000NS = Choice(5, parent)
                    self.BLK_6000NS = Choice(6, parent)
                    self.BLK_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_BLANKING_UVW", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _HS_OCP_THRES_UVW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_THRES_UVW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_OCP_UVW", parent, access, address, block, signed)
            self.LS_OCP_DEGLITCH_UVW  =  self._LS_OCP_DEGLITCH_UVW(self,  Access.RW,  0x00000007,  0,   signed=False)
            self.LS_OCP_BLANKING_UVW  =  self._LS_OCP_BLANKING_UVW(self,  Access.RW,  0x00000070,  4,   signed=False)
            self.LS_OCP_THRES_UVW     =  self._LS_OCP_THRES_UVW(   self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.LS_OCP_USE_VDS_UVW   =  self._LS_OCP_USE_VDS_UVW( self,  Access.RW,  0x00008000,  15,  signed=False)
            self.HS_OCP_DEGLITCH_UVW  =  self._HS_OCP_DEGLITCH_UVW(self,  Access.RW,  0x00070000,  16,  signed=False)
            self.HS_OCP_BLANKING_UVW  =  self._HS_OCP_BLANKING_UVW(self,  Access.RW,  0x00700000,  20,  signed=False)
            self.HS_OCP_THRES_UVW     =  self._HS_OCP_THRES_UVW(   self,  Access.RW,  0x0F000000,  24,  signed=False)

    class _GDRV_OCP_Y2(Register):

        class _LS_OCP_DEGLITCH_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.DEG_OFF = Choice(0, parent)
                    self.DEG_250NS = Choice(1, parent)
                    self.DEG_500NS = Choice(2, parent)
                    self.DEG_1000NS = Choice(3, parent)
                    self.DEG_2000NS = Choice(4, parent)
                    self.DEG_4000NS = Choice(5, parent)
                    self.DEG_6000NS = Choice(6, parent)
                    self.DEG_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_DEGLITCH_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _LS_OCP_BLANKING_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.BLK_OFF = Choice(0, parent)
                    self.BLK_250NS = Choice(1, parent)
                    self.BLK_500NS = Choice(2, parent)
                    self.BLK_1000NS = Choice(3, parent)
                    self.BLK_2000NS = Choice(4, parent)
                    self.BLK_4000NS = Choice(5, parent)
                    self.BLK_6000NS = Choice(6, parent)
                    self.BLK_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_BLANKING_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _LS_OCP_THRES_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.THRES_80_63MV = Choice(0, parent)
                    self.THRES_165_125MV = Choice(1, parent)
                    self.THRES_250_187MV = Choice(2, parent)
                    self.THRES_330_248MV = Choice(3, parent)
                    self.THRES_415_312MV = Choice(4, parent)
                    self.THRES_500_374MV = Choice(5, parent)
                    self.THRES_582_434MV = Choice(6, parent)
                    self.THRES_660_504MV = Choice(7, parent)
                    self.THRES_125_705MV = Choice(8, parent)
                    self.THRES_250_940MV = Choice(9, parent)
                    self.THRES_375_1180MV = Choice(10, parent)
                    self.THRES_500_1410MV = Choice(11, parent)
                    self.THRES_625_1650MV = Choice(12, parent)
                    self.THRES_750_1880MV = Choice(13, parent)
                    self.THRES_873_2110MV = Choice(14, parent)
                    self.THRES_1000_2350MV = Choice(15, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_THRES_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _LS_OCP_USE_VDS_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_OCP_USE_VDS_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_OCP_DEGLITCH_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.DEG_OFF = Choice(0, parent)
                    self.DEG_250NS = Choice(1, parent)
                    self.DEG_500NS = Choice(2, parent)
                    self.DEG_1000NS = Choice(3, parent)
                    self.DEG_2000NS = Choice(4, parent)
                    self.DEG_4000NS = Choice(5, parent)
                    self.DEG_6000NS = Choice(6, parent)
                    self.DEG_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_DEGLITCH_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _HS_OCP_BLANKING_Y2(Field):

            class _Choices:
                def __init__(self, parent) -> None:
                    self.BLK_OFF = Choice(0, parent)
                    self.BLK_250NS = Choice(1, parent)
                    self.BLK_500NS = Choice(2, parent)
                    self.BLK_1000NS = Choice(3, parent)
                    self.BLK_2000NS = Choice(4, parent)
                    self.BLK_4000NS = Choice(5, parent)
                    self.BLK_6000NS = Choice(6, parent)
                    self.BLK_8000NS = Choice(7, parent)

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_BLANKING_Y2", parent, access, mask, shift, signed=signed)

                self.choice = self._Choices(self)

        class _HS_OCP_THRES_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_OCP_THRES_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_OCP_Y2", parent, access, address, block, signed)
            self.LS_OCP_DEGLITCH_Y2  =  self._LS_OCP_DEGLITCH_Y2(self,  Access.RW,  0x00000007,  0,   signed=False)
            self.LS_OCP_BLANKING_Y2  =  self._LS_OCP_BLANKING_Y2(self,  Access.RW,  0x00000070,  4,   signed=False)
            self.LS_OCP_THRES_Y2     =  self._LS_OCP_THRES_Y2(   self,  Access.RW,  0x00000F00,  8,   signed=False)
            self.LS_OCP_USE_VDS_Y2   =  self._LS_OCP_USE_VDS_Y2( self,  Access.RW,  0x00008000,  15,  signed=False)
            self.HS_OCP_DEGLITCH_Y2  =  self._HS_OCP_DEGLITCH_Y2(self,  Access.RW,  0x00070000,  16,  signed=False)
            self.HS_OCP_BLANKING_Y2  =  self._HS_OCP_BLANKING_Y2(self,  Access.RW,  0x00700000,  20,  signed=False)
            self.HS_OCP_THRES_Y2     =  self._HS_OCP_THRES_Y2(   self,  Access.RW,  0x0F000000,  24,  signed=False)

    class _GDRV_PROT_EN(Register):

        class _LS_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_PROT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_PROT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_PROT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_PROT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_PROT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_PROT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_PROT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_PROT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO_PROT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO_PROT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_PROT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_PROT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_PROT_EN", parent, access, address, block, signed)
            self.LS_SHORT_PROT_U           =  self._LS_SHORT_PROT_U(         self,  Access.RW,  0x00000001,  0,   signed=False)
            self.LS_SHORT_PROT_V           =  self._LS_SHORT_PROT_V(         self,  Access.RW,  0x00000002,  1,   signed=False)
            self.LS_SHORT_PROT_W           =  self._LS_SHORT_PROT_W(         self,  Access.RW,  0x00000004,  2,   signed=False)
            self.LS_SHORT_PROT_Y2          =  self._LS_SHORT_PROT_Y2(        self,  Access.RW,  0x00000008,  3,   signed=False)
            self.LS_VGS_OFF_SHORT_PROT_U   =  self._LS_VGS_OFF_SHORT_PROT_U( self,  Access.RW,  0x00000010,  4,   signed=False)
            self.LS_VGS_OFF_SHORT_PROT_V   =  self._LS_VGS_OFF_SHORT_PROT_V( self,  Access.RW,  0x00000020,  5,   signed=False)
            self.LS_VGS_OFF_SHORT_PROT_W   =  self._LS_VGS_OFF_SHORT_PROT_W( self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LS_VGS_OFF_SHORT_PROT_Y2  =  self._LS_VGS_OFF_SHORT_PROT_Y2(self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LS_VGS_ON_SHORT_PROT_U    =  self._LS_VGS_ON_SHORT_PROT_U(  self,  Access.RW,  0x00000100,  8,   signed=False)
            self.LS_VGS_ON_SHORT_PROT_V    =  self._LS_VGS_ON_SHORT_PROT_V(  self,  Access.RW,  0x00000200,  9,   signed=False)
            self.LS_VGS_ON_SHORT_PROT_W    =  self._LS_VGS_ON_SHORT_PROT_W(  self,  Access.RW,  0x00000400,  10,  signed=False)
            self.LS_VGS_ON_SHORT_PROT_Y2   =  self._LS_VGS_ON_SHORT_PROT_Y2( self,  Access.RW,  0x00000800,  11,  signed=False)
            self.BST_UVLO_PROT_U           =  self._BST_UVLO_PROT_U(         self,  Access.RW,  0x00001000,  12,  signed=False)
            self.BST_UVLO_PROT_V           =  self._BST_UVLO_PROT_V(         self,  Access.RW,  0x00002000,  13,  signed=False)
            self.BST_UVLO_PROT_W           =  self._BST_UVLO_PROT_W(         self,  Access.RW,  0x00004000,  14,  signed=False)
            self.BST_UVLO_PROT_Y2          =  self._BST_UVLO_PROT_Y2(        self,  Access.RW,  0x00008000,  15,  signed=False)
            self.HS_SHORT_PROT_U           =  self._HS_SHORT_PROT_U(         self,  Access.RW,  0x00010000,  16,  signed=False)
            self.HS_SHORT_PROT_V           =  self._HS_SHORT_PROT_V(         self,  Access.RW,  0x00020000,  17,  signed=False)
            self.HS_SHORT_PROT_W           =  self._HS_SHORT_PROT_W(         self,  Access.RW,  0x00040000,  18,  signed=False)
            self.HS_SHORT_PROT_Y2          =  self._HS_SHORT_PROT_Y2(        self,  Access.RW,  0x00080000,  19,  signed=False)
            self.HS_VGS_OFF_SHORT_PROT_U   =  self._HS_VGS_OFF_SHORT_PROT_U( self,  Access.RW,  0x00100000,  20,  signed=False)
            self.HS_VGS_OFF_SHORT_PROT_V   =  self._HS_VGS_OFF_SHORT_PROT_V( self,  Access.RW,  0x00200000,  21,  signed=False)
            self.HS_VGS_OFF_SHORT_PROT_W   =  self._HS_VGS_OFF_SHORT_PROT_W( self,  Access.RW,  0x00400000,  22,  signed=False)
            self.HS_VGS_OFF_SHORT_PROT_Y2  =  self._HS_VGS_OFF_SHORT_PROT_Y2(self,  Access.RW,  0x00800000,  23,  signed=False)
            self.HS_VGS_ON_SHORT_PROT_U    =  self._HS_VGS_ON_SHORT_PROT_U(  self,  Access.RW,  0x01000000,  24,  signed=False)
            self.HS_VGS_ON_SHORT_PROT_V    =  self._HS_VGS_ON_SHORT_PROT_V(  self,  Access.RW,  0x02000000,  25,  signed=False)
            self.HS_VGS_ON_SHORT_PROT_W    =  self._HS_VGS_ON_SHORT_PROT_W(  self,  Access.RW,  0x04000000,  26,  signed=False)
            self.HS_VGS_ON_SHORT_PROT_Y2   =  self._HS_VGS_ON_SHORT_PROT_Y2( self,  Access.RW,  0x08000000,  27,  signed=False)
            self.VDRV_UVLO_PROT            =  self._VDRV_UVLO_PROT(          self,  Access.RW,  0x20000000,  29,  signed=False)
            self.VS_UVLO_PROT              =  self._VS_UVLO_PROT(            self,  Access.RW,  0x80000000,  31,  signed=False)

    class _GDRV_STATUS_EN(Register):

        class _LS_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_EN_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_EN_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_EN_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_EN_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_EN_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_EN_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_EN_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_EN_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLWRN_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLWRN_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_EN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_EN", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_STATUS_EN", parent, access, address, block, signed)
            self.LS_SHORT_EN_U           =  self._LS_SHORT_EN_U(         self,  Access.RW,  0x00000001,  0,   signed=False)
            self.LS_SHORT_EN_V           =  self._LS_SHORT_EN_V(         self,  Access.RW,  0x00000002,  1,   signed=False)
            self.LS_SHORT_EN_W           =  self._LS_SHORT_EN_W(         self,  Access.RW,  0x00000004,  2,   signed=False)
            self.LS_SHORT_EN_Y2          =  self._LS_SHORT_EN_Y2(        self,  Access.RW,  0x00000008,  3,   signed=False)
            self.LS_VGS_OFF_SHORT_EN_U   =  self._LS_VGS_OFF_SHORT_EN_U( self,  Access.RW,  0x00000010,  4,   signed=False)
            self.LS_VGS_OFF_SHORT_EN_V   =  self._LS_VGS_OFF_SHORT_EN_V( self,  Access.RW,  0x00000020,  5,   signed=False)
            self.LS_VGS_OFF_SHORT_EN_W   =  self._LS_VGS_OFF_SHORT_EN_W( self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LS_VGS_OFF_SHORT_EN_Y2  =  self._LS_VGS_OFF_SHORT_EN_Y2(self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LS_VGS_ON_SHORT_EN_U    =  self._LS_VGS_ON_SHORT_EN_U(  self,  Access.RW,  0x00000100,  8,   signed=False)
            self.LS_VGS_ON_SHORT_EN_V    =  self._LS_VGS_ON_SHORT_EN_V(  self,  Access.RW,  0x00000200,  9,   signed=False)
            self.LS_VGS_ON_SHORT_EN_W    =  self._LS_VGS_ON_SHORT_EN_W(  self,  Access.RW,  0x00000400,  10,  signed=False)
            self.LS_VGS_ON_SHORT_EN_Y2   =  self._LS_VGS_ON_SHORT_EN_Y2( self,  Access.RW,  0x00000800,  11,  signed=False)
            self.BST_UVLO_EN_U           =  self._BST_UVLO_EN_U(         self,  Access.RW,  0x00001000,  12,  signed=False)
            self.BST_UVLO_EN_V           =  self._BST_UVLO_EN_V(         self,  Access.RW,  0x00002000,  13,  signed=False)
            self.BST_UVLO_EN_W           =  self._BST_UVLO_EN_W(         self,  Access.RW,  0x00004000,  14,  signed=False)
            self.BST_UVLO_EN_Y2          =  self._BST_UVLO_EN_Y2(        self,  Access.RW,  0x00008000,  15,  signed=False)
            self.HS_SHORT_EN_U           =  self._HS_SHORT_EN_U(         self,  Access.RW,  0x00010000,  16,  signed=False)
            self.HS_SHORT_EN_V           =  self._HS_SHORT_EN_V(         self,  Access.RW,  0x00020000,  17,  signed=False)
            self.HS_SHORT_EN_W           =  self._HS_SHORT_EN_W(         self,  Access.RW,  0x00040000,  18,  signed=False)
            self.HS_SHORT_EN_Y2          =  self._HS_SHORT_EN_Y2(        self,  Access.RW,  0x00080000,  19,  signed=False)
            self.HS_VGS_OFF_SHORT_EN_U   =  self._HS_VGS_OFF_SHORT_EN_U( self,  Access.RW,  0x00100000,  20,  signed=False)
            self.HS_VGS_OFF_SHORT_EN_V   =  self._HS_VGS_OFF_SHORT_EN_V( self,  Access.RW,  0x00200000,  21,  signed=False)
            self.HS_VGS_OFF_SHORT_EN_W   =  self._HS_VGS_OFF_SHORT_EN_W( self,  Access.RW,  0x00400000,  22,  signed=False)
            self.HS_VGS_OFF_SHORT_EN_Y2  =  self._HS_VGS_OFF_SHORT_EN_Y2(self,  Access.RW,  0x00800000,  23,  signed=False)
            self.HS_VGS_ON_SHORT_EN_U    =  self._HS_VGS_ON_SHORT_EN_U(  self,  Access.RW,  0x01000000,  24,  signed=False)
            self.HS_VGS_ON_SHORT_EN_V    =  self._HS_VGS_ON_SHORT_EN_V(  self,  Access.RW,  0x02000000,  25,  signed=False)
            self.HS_VGS_ON_SHORT_EN_W    =  self._HS_VGS_ON_SHORT_EN_W(  self,  Access.RW,  0x04000000,  26,  signed=False)
            self.HS_VGS_ON_SHORT_EN_Y2   =  self._HS_VGS_ON_SHORT_EN_Y2( self,  Access.RW,  0x08000000,  27,  signed=False)
            self.VDRV_UVLO_EN            =  self._VDRV_UVLO_EN(          self,  Access.RW,  0x20000000,  29,  signed=False)
            self.VDRV_UVLWRN_EN          =  self._VDRV_UVLWRN_EN(        self,  Access.RW,  0x40000000,  30,  signed=False)
            self.VS_UVLO_EN              =  self._VS_UVLO_EN(            self,  Access.RW,  0x80000000,  31,  signed=False)

    class _GDRV_STATUS(Register):

        class _LS_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_OFF_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_OFF_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_VGS_ON_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_VGS_ON_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_OFF_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_OFF_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_VGS_ON_SHORT_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_VGS_ON_SHORT_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLWRN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLWRN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_STATUS", parent, access, address, block, signed)
            self.LS_SHORT_U           =  self._LS_SHORT_U(         self,  Access.RWC,  0x00000001,  0,   signed=False)
            self.LS_SHORT_V           =  self._LS_SHORT_V(         self,  Access.RWC,  0x00000002,  1,   signed=False)
            self.LS_SHORT_W           =  self._LS_SHORT_W(         self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.LS_SHORT_Y2          =  self._LS_SHORT_Y2(        self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.LS_VGS_OFF_SHORT_U   =  self._LS_VGS_OFF_SHORT_U( self,  Access.RWC,  0x00000010,  4,   signed=False)
            self.LS_VGS_OFF_SHORT_V   =  self._LS_VGS_OFF_SHORT_V( self,  Access.RWC,  0x00000020,  5,   signed=False)
            self.LS_VGS_OFF_SHORT_W   =  self._LS_VGS_OFF_SHORT_W( self,  Access.RWC,  0x00000040,  6,   signed=False)
            self.LS_VGS_OFF_SHORT_Y2  =  self._LS_VGS_OFF_SHORT_Y2(self,  Access.RWC,  0x00000080,  7,   signed=False)
            self.LS_VGS_ON_SHORT_U    =  self._LS_VGS_ON_SHORT_U(  self,  Access.RWC,  0x00000100,  8,   signed=False)
            self.LS_VGS_ON_SHORT_V    =  self._LS_VGS_ON_SHORT_V(  self,  Access.RWC,  0x00000200,  9,   signed=False)
            self.LS_VGS_ON_SHORT_W    =  self._LS_VGS_ON_SHORT_W(  self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.LS_VGS_ON_SHORT_Y2   =  self._LS_VGS_ON_SHORT_Y2( self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.BST_UVLO_U           =  self._BST_UVLO_U(         self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.BST_UVLO_V           =  self._BST_UVLO_V(         self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.BST_UVLO_W           =  self._BST_UVLO_W(         self,  Access.RWC,  0x00004000,  14,  signed=False)
            self.BST_UVLO_Y2          =  self._BST_UVLO_Y2(        self,  Access.RWC,  0x00008000,  15,  signed=False)
            self.HS_SHORT_U           =  self._HS_SHORT_U(         self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.HS_SHORT_V           =  self._HS_SHORT_V(         self,  Access.RWC,  0x00020000,  17,  signed=False)
            self.HS_SHORT_W           =  self._HS_SHORT_W(         self,  Access.RWC,  0x00040000,  18,  signed=False)
            self.HS_SHORT_Y2          =  self._HS_SHORT_Y2(        self,  Access.RWC,  0x00080000,  19,  signed=False)
            self.HS_VGS_OFF_SHORT_U   =  self._HS_VGS_OFF_SHORT_U( self,  Access.RWC,  0x00100000,  20,  signed=False)
            self.HS_VGS_OFF_SHORT_V   =  self._HS_VGS_OFF_SHORT_V( self,  Access.RWC,  0x00200000,  21,  signed=False)
            self.HS_VGS_OFF_SHORT_W   =  self._HS_VGS_OFF_SHORT_W( self,  Access.RWC,  0x00400000,  22,  signed=False)
            self.HS_VGS_OFF_SHORT_Y2  =  self._HS_VGS_OFF_SHORT_Y2(self,  Access.RWC,  0x00800000,  23,  signed=False)
            self.HS_VGS_ON_SHORT_U    =  self._HS_VGS_ON_SHORT_U(  self,  Access.RWC,  0x01000000,  24,  signed=False)
            self.HS_VGS_ON_SHORT_V    =  self._HS_VGS_ON_SHORT_V(  self,  Access.RWC,  0x02000000,  25,  signed=False)
            self.HS_VGS_ON_SHORT_W    =  self._HS_VGS_ON_SHORT_W(  self,  Access.RWC,  0x04000000,  26,  signed=False)
            self.HS_VGS_ON_SHORT_Y2   =  self._HS_VGS_ON_SHORT_Y2( self,  Access.RWC,  0x08000000,  27,  signed=False)
            self.VDRV_UVLO            =  self._VDRV_UVLO(          self,  Access.RWC,  0x20000000,  29,  signed=False)
            self.VDRV_UVLWRN          =  self._VDRV_UVLWRN(        self,  Access.RWC,  0x40000000,  30,  signed=False)
            self.VS_UVLO              =  self._VS_UVLO(            self,  Access.RWC,  0x80000000,  31,  signed=False)

    class _GDRV_FAULT(Register):

        class _LS_FAULT_ACTIVE_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_FAULT_ACTIVE_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_FAULT_ACTIVE_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_FAULT_ACTIVE_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_FAULT_ACTIVE_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_FAULT_ACTIVE_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LS_FAULT_ACTIVE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_FAULT_ACTIVE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_STS_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_STS_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_STS_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_STS_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_STS_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_STS_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BST_UVLO_STS_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BST_UVLO_STS_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_FAULT_ACTIVE_U(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_FAULT_ACTIVE_U", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_FAULT_ACTIVE_V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_FAULT_ACTIVE_V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_FAULT_ACTIVE_W(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_FAULT_ACTIVE_W", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _HS_FAULT_ACTIVE_Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HS_FAULT_ACTIVE_Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLO_STS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLO_STS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDRV_UVLWRN_STS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDRV_UVLWRN_STS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VS_UVLO_STS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VS_UVLO_STS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("GDRV_FAULT", parent, access, address, block, signed)
            self.LS_FAULT_ACTIVE_U   =  self._LS_FAULT_ACTIVE_U( self,  Access.RWC,  0x00000001,  0,   signed=False)
            self.LS_FAULT_ACTIVE_V   =  self._LS_FAULT_ACTIVE_V( self,  Access.RWC,  0x00000002,  1,   signed=False)
            self.LS_FAULT_ACTIVE_W   =  self._LS_FAULT_ACTIVE_W( self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.LS_FAULT_ACTIVE_Y2  =  self._LS_FAULT_ACTIVE_Y2(self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.BST_UVLO_STS_U      =  self._BST_UVLO_STS_U(    self,  Access.R,    0x00001000,  12,  signed=False)
            self.BST_UVLO_STS_V      =  self._BST_UVLO_STS_V(    self,  Access.R,    0x00002000,  13,  signed=False)
            self.BST_UVLO_STS_W      =  self._BST_UVLO_STS_W(    self,  Access.R,    0x00004000,  14,  signed=False)
            self.BST_UVLO_STS_Y2     =  self._BST_UVLO_STS_Y2(   self,  Access.R,    0x00008000,  15,  signed=False)
            self.HS_FAULT_ACTIVE_U   =  self._HS_FAULT_ACTIVE_U( self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.HS_FAULT_ACTIVE_V   =  self._HS_FAULT_ACTIVE_V( self,  Access.RWC,  0x00020000,  17,  signed=False)
            self.HS_FAULT_ACTIVE_W   =  self._HS_FAULT_ACTIVE_W( self,  Access.RWC,  0x00040000,  18,  signed=False)
            self.HS_FAULT_ACTIVE_Y2  =  self._HS_FAULT_ACTIVE_Y2(self,  Access.RWC,  0x00080000,  19,  signed=False)
            self.VDRV_UVLO_STS       =  self._VDRV_UVLO_STS(     self,  Access.R,    0x20000000,  29,  signed=False)
            self.VDRV_UVLWRN_STS     =  self._VDRV_UVLWRN_STS(   self,  Access.R,    0x40000000,  30,  signed=False)
            self.VS_UVLO_STS         =  self._VS_UVLO_STS(       self,  Access.R,    0x80000000,  31,  signed=False)

    class _ADC_I1_I0_EXT(Register):

        class _I0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _I1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I1_I0_EXT", parent, access, address, block, signed)
            self.I0  =  self._I0(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.I1  =  self._I1(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _ADC_I2_EXT(Register):

        class _I2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_I2_EXT", parent, access, address, block, signed)
            self.I2  =  self._I2(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

    class _PWM_VX2_UX1_EXT(Register):

        class _UX1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UX1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VX2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VX2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_VX2_UX1_EXT", parent, access, address, block, signed)
            self.UX1  =  self._UX1(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.VX2  =  self._VX2(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

    class _PWM_Y2_WY1_EXT(Register):

        class _WY1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WY1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _Y2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("Y2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_Y2_WY1_EXT", parent, access, address, block, signed)
            self.WY1  =  self._WY1(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.Y2   =  self._Y2( self,  Access.RW,  0xFFFF0000,  16,  signed=False)

    class _PWM_EXT_Y2_ALT(Register):

        class _PWM_EXT_Y2_ALT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_EXT_Y2_ALT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PWM_EXT_Y2_ALT", parent, access, address, block, signed)
            self.PWM_EXT_Y2_ALT  =  self._PWM_EXT_Y2_ALT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

    class _VOLTAGE_EXT(Register):

        class _UD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UQ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VOLTAGE_EXT", parent, access, address, block, signed)
            self.UD  =  self._UD(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.UQ  =  self._UQ(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _PHI_EXT(Register):

        class _PHI_E_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _PHI_M_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_M_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PHI_EXT", parent, access, address, block, signed)
            self.PHI_E_EXT  =  self._PHI_E_EXT(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.PHI_M_EXT  =  self._PHI_M_EXT(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

    class _VELOCITY_EXT(Register):

        class _VELOCITY_EXT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_EXT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("VELOCITY_EXT", parent, access, address, block, signed)
            self.VELOCITY_EXT  =  self._VELOCITY_EXT(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.INFO_CHIP                         =  self._INFO_CHIP(                       self,  Access.R,    0x0000,  block,  False)
        self.INFO_VARIANT                      =  self._INFO_VARIANT(                    self,  Access.R,    0x0001,  block,  False)
        self.INFO_REVISION                     =  self._INFO_REVISION(                   self,  Access.R,    0x0002,  block,  False)
        self.ADC_I1_I0_RAW                     =  self._ADC_I1_I0_RAW(                   self,  Access.R,    0x0020,  block,  False)
        self.ADC_I3_I2_RAW                     =  self._ADC_I3_I2_RAW(                   self,  Access.R,    0x0021,  block,  False)
        self.ADC_U1_U0_RAW                     =  self._ADC_U1_U0_RAW(                   self,  Access.R,    0x0022,  block,  False)
        self.ADC_U3_U2_RAW                     =  self._ADC_U3_U2_RAW(                   self,  Access.R,    0x0023,  block,  False)
        self.ADC_TEMP_VM_RAW                   =  self._ADC_TEMP_VM_RAW(                 self,  Access.R,    0x0024,  block,  False)
        self.ADC_AIN1_AIN0_RAW                 =  self._ADC_AIN1_AIN0_RAW(               self,  Access.R,    0x0025,  block,  False)
        self.ADC_AIN3_AIN2_RAW                 =  self._ADC_AIN3_AIN2_RAW(               self,  Access.R,    0x0026,  block,  False)
        self.ADC_I_GEN_CONFIG                  =  self._ADC_I_GEN_CONFIG(                self,  Access.RW,   0x0040,  block,  False)
        self.ADC_I0_CONFIG                     =  self._ADC_I0_CONFIG(                   self,  Access.RW,   0x0041,  block,  False)
        self.ADC_I1_CONFIG                     =  self._ADC_I1_CONFIG(                   self,  Access.RW,   0x0042,  block,  False)
        self.ADC_I2_CONFIG                     =  self._ADC_I2_CONFIG(                   self,  Access.RW,   0x0043,  block,  False)
        self.ADC_I3_CONFIG                     =  self._ADC_I3_CONFIG(                   self,  Access.RW,   0x0044,  block,  False)
        self.ADC_I1_I0_SCALED                  =  self._ADC_I1_I0_SCALED(                self,  Access.R,    0x0045,  block,  False)
        self.ADC_I3_I2_SCALED                  =  self._ADC_I3_I2_SCALED(                self,  Access.R,    0x0046,  block,  False)
        self.ADC_IWY_IUX                       =  self._ADC_IWY_IUX(                     self,  Access.R,    0x0047,  block,  False)
        self.ADC_IV                            =  self._ADC_IV(                          self,  Access.R,    0x0048,  block,  True)
        self.ADC_STATUS                        =  self._ADC_STATUS(                      self,  Access.RWC,  0x0049,  block,  False)
        self.MOTOR_CONFIG                      =  self._MOTOR_CONFIG(                    self,  Access.RW,   0x0060,  block,  False)
        self.MOTION_CONFIG                     =  self._MOTION_CONFIG(                   self,  Access.RW,   0x0061,  block,  False)
        self.PHI_E_SELECTION                   =  self._PHI_E_SELECTION(                 self,  Access.RW,   0x0062,  block,  False)
        self.PHI_E                             =  self._PHI_E(                           self,  Access.R,    0x0063,  block,  True)
        self.PWM_CONFIG                        =  self._PWM_CONFIG(                      self,  Access.RW,   0x0080,  block,  False)
        self.PWM_MAXCNT                        =  self._PWM_MAXCNT(                      self,  Access.RW,   0x0081,  block,  False)
        self.PWM_SWITCH_LIMIT                  =  self._PWM_SWITCH_LIMIT(                self,  Access.RW,   0x0083,  block,  False)
        self.ABN_PHI_E_PHI_M                   =  self._ABN_PHI_E_PHI_M(                 self,  Access.R,    0x00A0,  block,  False)
        self.ABN_MODE                          =  self._ABN_MODE(                        self,  Access.RW,   0x00A1,  block,  False)
        self.ABN_CPR                           =  self._ABN_CPR(                         self,  Access.RW,   0x00A2,  block,  False)
        self.ABN_CPR_INV                       =  self._ABN_CPR_INV(                     self,  Access.RW,   0x00A3,  block,  False)
        self.ABN_COUNT                         =  self._ABN_COUNT(                       self,  Access.RW,   0x00A4,  block,  False)
        self.ABN_COUNT_N                       =  self._ABN_COUNT_N(                     self,  Access.RW,   0x00A5,  block,  False)
        self.ABN_PHI_E_OFFSET                  =  self._ABN_PHI_E_OFFSET(                self,  Access.RW,   0x00A6,  block,  True)
        self.HALL_MODE                         =  self._HALL_MODE(                       self,  Access.RW,   0x00C0,  block,  False)
        self.HALL_DPHI_MAX                     =  self._HALL_DPHI_MAX(                   self,  Access.RW,   0x00C1,  block,  False)
        self.HALL_PHI_E_OFFSET                 =  self._HALL_PHI_E_OFFSET(               self,  Access.RW,   0x00C2,  block,  True)
        self.HALL_COUNT                        =  self._HALL_COUNT(                      self,  Access.R,    0x00C3,  block,  True)
        self.HALL_PHI_E_EXTRAPOLATED_PHI_E     =  self._HALL_PHI_E_EXTRAPOLATED_PHI_E(   self,  Access.R,    0x00C4,  block,  False)
        self.HALL_POSITION_060_POSITION_000    =  self._HALL_POSITION_060_POSITION_000(  self,  Access.RW,   0x00C5,  block,  False)
        self.HALL_POSITION_180_POSITION_120    =  self._HALL_POSITION_180_POSITION_120(  self,  Access.RW,   0x00C6,  block,  False)
        self.HALL_POSITION_300_POSITION_240    =  self._HALL_POSITION_300_POSITION_240(  self,  Access.RW,   0x00C7,  block,  False)
        self.BIQUAD_V_A_1                      =  self._BIQUAD_V_A_1(                    self,  Access.RW,   0x00E0,  block,  True)
        self.BIQUAD_V_A_2                      =  self._BIQUAD_V_A_2(                    self,  Access.RW,   0x00E1,  block,  True)
        self.BIQUAD_V_B_0                      =  self._BIQUAD_V_B_0(                    self,  Access.RW,   0x00E2,  block,  True)
        self.BIQUAD_V_B_1                      =  self._BIQUAD_V_B_1(                    self,  Access.RW,   0x00E3,  block,  True)
        self.BIQUAD_V_B_2                      =  self._BIQUAD_V_B_2(                    self,  Access.RW,   0x00E4,  block,  True)
        self.BIQUAD_V_ENABLE                   =  self._BIQUAD_V_ENABLE(                 self,  Access.RW,   0x00E5,  block,  False)
        self.BIQUAD_T_A_1                      =  self._BIQUAD_T_A_1(                    self,  Access.RW,   0x00E6,  block,  True)
        self.BIQUAD_T_A_2                      =  self._BIQUAD_T_A_2(                    self,  Access.RW,   0x00E7,  block,  True)
        self.BIQUAD_T_B_0                      =  self._BIQUAD_T_B_0(                    self,  Access.RW,   0x00E8,  block,  True)
        self.BIQUAD_T_B_1                      =  self._BIQUAD_T_B_1(                    self,  Access.RW,   0x00E9,  block,  True)
        self.BIQUAD_T_B_2                      =  self._BIQUAD_T_B_2(                    self,  Access.RW,   0x00EA,  block,  True)
        self.BIQUAD_T_ENABLE                   =  self._BIQUAD_T_ENABLE(                 self,  Access.RW,   0x00EB,  block,  False)
        self.VELOCITY_CONFIG                   =  self._VELOCITY_CONFIG(                 self,  Access.RW,   0x0100,  block,  False)
        self.VELOCITY_SCALING                  =  self._VELOCITY_SCALING(                self,  Access.RW,   0x0101,  block,  True)
        self.V_MIN_POS_DEV_TIME_COUNTER_LIMIT  =  self._V_MIN_POS_DEV_TIME_COUNTER_LIMIT(self,  Access.RW,   0x0102,  block,  False)
        self.MAX_VEL_DEVIATION                 =  self._MAX_VEL_DEVIATION(               self,  Access.RW,   0x0103,  block,  False)
        self.POSITION_CONFIG                   =  self._POSITION_CONFIG(                 self,  Access.RW,   0x0120,  block,  False)
        self.MAX_POS_DEVIATION                 =  self._MAX_POS_DEVIATION(               self,  Access.RW,   0x0121,  block,  False)
        self.RAMPER_STATUS                     =  self._RAMPER_STATUS(                   self,  Access.RWC,  0x0140,  block,  False)
        self.RAMPER_A1                         =  self._RAMPER_A1(                       self,  Access.RW,   0x0141,  block,  False)
        self.RAMPER_A2                         =  self._RAMPER_A2(                       self,  Access.RW,   0x0142,  block,  False)
        self.RAMPER_A_MAX                      =  self._RAMPER_A_MAX(                    self,  Access.RW,   0x0143,  block,  False)
        self.RAMPER_D1                         =  self._RAMPER_D1(                       self,  Access.RW,   0x0144,  block,  False)
        self.RAMPER_D2                         =  self._RAMPER_D2(                       self,  Access.RW,   0x0145,  block,  False)
        self.RAMPER_D_MAX                      =  self._RAMPER_D_MAX(                    self,  Access.RW,   0x0146,  block,  False)
        self.RAMPER_V_START                    =  self._RAMPER_V_START(                  self,  Access.RW,   0x0147,  block,  False)
        self.RAMPER_V1                         =  self._RAMPER_V1(                       self,  Access.RW,   0x0148,  block,  False)
        self.RAMPER_V2                         =  self._RAMPER_V2(                       self,  Access.RW,   0x0149,  block,  False)
        self.RAMPER_V_STOP                     =  self._RAMPER_V_STOP(                   self,  Access.RW,   0x014A,  block,  False)
        self.RAMPER_V_MAX                      =  self._RAMPER_V_MAX(                    self,  Access.RW,   0x014B,  block,  False)
        self.RAMPER_V_TARGET                   =  self._RAMPER_V_TARGET(                 self,  Access.RW,   0x014C,  block,  True)
        self.RAMPER_SWITCH_MODE                =  self._RAMPER_SWITCH_MODE(              self,  Access.RW,   0x014D,  block,  False)
        self.RAMPER_TIME_CONFIG                =  self._RAMPER_TIME_CONFIG(              self,  Access.RW,   0x014E,  block,  False)
        self.RAMPER_A_ACTUAL                   =  self._RAMPER_A_ACTUAL(                 self,  Access.R,    0x014F,  block,  True)
        self.RAMPER_X_ACTUAL                   =  self._RAMPER_X_ACTUAL(                 self,  Access.R,    0x0150,  block,  True)
        self.RAMPER_V_ACTUAL                   =  self._RAMPER_V_ACTUAL(                 self,  Access.R,    0x0151,  block,  True)
        self.RAMPER_X_TARGET                   =  self._RAMPER_X_TARGET(                 self,  Access.RW,   0x0152,  block,  True)
        self.RAMPER_PHI_E                      =  self._RAMPER_PHI_E(                    self,  Access.R,    0x0153,  block,  True)
        self.RAMPER_PHI_E_OFFSET               =  self._RAMPER_PHI_E_OFFSET(             self,  Access.RW,   0x0154,  block,  True)
        self.RAMPER_ACC_FF                     =  self._RAMPER_ACC_FF(                   self,  Access.RW,   0x0155,  block,  False)
        self.RAMPER_X_ACTUAL_LATCH             =  self._RAMPER_X_ACTUAL_LATCH(           self,  Access.R,    0x0156,  block,  True)
        self.POSITION_ACTUAL_LATCH             =  self._POSITION_ACTUAL_LATCH(           self,  Access.R,    0x0157,  block,  True)
        self.PRBS_AMPLITUDE                    =  self._PRBS_AMPLITUDE(                  self,  Access.RW,   0x0160,  block,  True)
        self.PRBS_DOWN_SAMPLING_RATIO          =  self._PRBS_DOWN_SAMPLING_RATIO(        self,  Access.RW,   0x0161,  block,  False)
        self.PID_CONFIG                        =  self._PID_CONFIG(                      self,  Access.RW,   0x0180,  block,  False)
        self.PID_FLUX_COEFF                    =  self._PID_FLUX_COEFF(                  self,  Access.RW,   0x0181,  block,  False)
        self.PID_TORQUE_COEFF                  =  self._PID_TORQUE_COEFF(                self,  Access.RW,   0x0182,  block,  False)
        self.PID_FIELDWEAK_COEFF               =  self._PID_FIELDWEAK_COEFF(             self,  Access.RW,   0x0183,  block,  False)
        self.PID_U_S_MAX                       =  self._PID_U_S_MAX(                     self,  Access.RW,   0x0184,  block,  False)
        self.PID_VELOCITY_COEFF                =  self._PID_VELOCITY_COEFF(              self,  Access.RW,   0x0185,  block,  False)
        self.PID_POSITION_COEFF                =  self._PID_POSITION_COEFF(              self,  Access.RW,   0x0186,  block,  False)
        self.PID_POSITION_TOLERANCE            =  self._PID_POSITION_TOLERANCE(          self,  Access.RW,   0x0187,  block,  False)
        self.PID_POSITION_TOLERANCE_DELAY      =  self._PID_POSITION_TOLERANCE_DELAY(    self,  Access.RW,   0x0188,  block,  False)
        self.PID_UQ_UD_LIMITS                  =  self._PID_UQ_UD_LIMITS(                self,  Access.RW,   0x0189,  block,  False)
        self.PID_TORQUE_FLUX_LIMITS            =  self._PID_TORQUE_FLUX_LIMITS(          self,  Access.RW,   0x018A,  block,  False)
        self.PID_VELOCITY_LIMIT                =  self._PID_VELOCITY_LIMIT(              self,  Access.RW,   0x018B,  block,  False)
        self.PID_POSITION_LIMIT_LOW            =  self._PID_POSITION_LIMIT_LOW(          self,  Access.RW,   0x018C,  block,  True)
        self.PID_POSITION_LIMIT_HIGH           =  self._PID_POSITION_LIMIT_HIGH(         self,  Access.RW,   0x018D,  block,  True)
        self.PID_TORQUE_FLUX_TARGET            =  self._PID_TORQUE_FLUX_TARGET(          self,  Access.RW,   0x018E,  block,  False)
        self.PID_TORQUE_FLUX_OFFSET            =  self._PID_TORQUE_FLUX_OFFSET(          self,  Access.RW,   0x018F,  block,  False)
        self.PID_VELOCITY_TARGET               =  self._PID_VELOCITY_TARGET(             self,  Access.RW,   0x0190,  block,  True)
        self.PID_VELOCITY_OFFSET               =  self._PID_VELOCITY_OFFSET(             self,  Access.RW,   0x0191,  block,  True)
        self.PID_POSITION_TARGET               =  self._PID_POSITION_TARGET(             self,  Access.RW,   0x0192,  block,  True)
        self.PID_TORQUE_FLUX_ACTUAL            =  self._PID_TORQUE_FLUX_ACTUAL(          self,  Access.R,    0x0193,  block,  False)
        self.PID_VELOCITY_ACTUAL               =  self._PID_VELOCITY_ACTUAL(             self,  Access.R,    0x0194,  block,  True)
        self.PID_POSITION_ACTUAL               =  self._PID_POSITION_ACTUAL(             self,  Access.RW,   0x0195,  block,  True)
        self.PID_POSITION_ACTUAL_OFFSET        =  self._PID_POSITION_ACTUAL_OFFSET(      self,  Access.RW,   0x0196,  block,  True)
        self.PID_TORQUE_ERROR                  =  self._PID_TORQUE_ERROR(                self,  Access.R,    0x0197,  block,  True)
        self.PID_FLUX_ERROR                    =  self._PID_FLUX_ERROR(                  self,  Access.R,    0x0198,  block,  True)
        self.PID_VELOCITY_ERROR                =  self._PID_VELOCITY_ERROR(              self,  Access.R,    0x0199,  block,  True)
        self.PID_POSITION_ERROR                =  self._PID_POSITION_ERROR(              self,  Access.R,    0x019A,  block,  True)
        self.PID_TORQUE_INTEGRATOR             =  self._PID_TORQUE_INTEGRATOR(           self,  Access.RW,   0x019B,  block,  True)
        self.PID_FLUX_INTEGRATOR               =  self._PID_FLUX_INTEGRATOR(             self,  Access.RW,   0x019C,  block,  True)
        self.PID_VELOCITY_INTEGRATOR           =  self._PID_VELOCITY_INTEGRATOR(         self,  Access.RW,   0x019D,  block,  True)
        self.PID_POSITION_INTEGRATOR           =  self._PID_POSITION_INTEGRATOR(         self,  Access.RW,   0x019E,  block,  True)
        self.PIDIN_TORQUE_FLUX_TARGET          =  self._PIDIN_TORQUE_FLUX_TARGET(        self,  Access.R,    0x01A0,  block,  False)
        self.PIDIN_VELOCITY_TARGET             =  self._PIDIN_VELOCITY_TARGET(           self,  Access.R,    0x01A1,  block,  True)
        self.PIDIN_POSITION_TARGET             =  self._PIDIN_POSITION_TARGET(           self,  Access.R,    0x01A2,  block,  True)
        self.PIDIN_TORQUE_FLUX_TARGET_LIMITED  =  self._PIDIN_TORQUE_FLUX_TARGET_LIMITED(self,  Access.R,    0x01A3,  block,  False)
        self.PIDIN_VELOCITY_TARGET_LIMITED     =  self._PIDIN_VELOCITY_TARGET_LIMITED(   self,  Access.R,    0x01A4,  block,  True)
        self.PIDIN_POSITION_TARGET_LIMITED     =  self._PIDIN_POSITION_TARGET_LIMITED(   self,  Access.R,    0x01A5,  block,  True)
        self.FOC_IBETA_IALPHA                  =  self._FOC_IBETA_IALPHA(                self,  Access.R,    0x01A6,  block,  False)
        self.FOC_IQ_ID                         =  self._FOC_IQ_ID(                       self,  Access.R,    0x01A7,  block,  False)
        self.FOC_UQ_UD                         =  self._FOC_UQ_UD(                       self,  Access.R,    0x01A8,  block,  False)
        self.FOC_UQ_UD_LIMITED                 =  self._FOC_UQ_UD_LIMITED(               self,  Access.R,    0x01A9,  block,  False)
        self.FOC_UBETA_UALPHA                  =  self._FOC_UBETA_UALPHA(                self,  Access.R,    0x01AA,  block,  False)
        self.FOC_UWY_UUX                       =  self._FOC_UWY_UUX(                     self,  Access.R,    0x01AB,  block,  False)
        self.FOC_UV                            =  self._FOC_UV(                          self,  Access.R,    0x01AC,  block,  True)
        self.PWM_VX2_UX1                       =  self._PWM_VX2_UX1(                     self,  Access.R,    0x01AD,  block,  False)
        self.PWM_Y2_WY1                        =  self._PWM_Y2_WY1(                      self,  Access.R,    0x01AE,  block,  False)
        self.VELOCITY_FRQ                      =  self._VELOCITY_FRQ(                    self,  Access.R,    0x01AF,  block,  True)
        self.VELOCITY_PER                      =  self._VELOCITY_PER(                    self,  Access.R,    0x01B0,  block,  True)
        self.U_S_ACTUAL_I_S_ACTUAL             =  self._U_S_ACTUAL_I_S_ACTUAL(           self,  Access.R,    0x01C0,  block,  False)
        self.P_MOTOR                           =  self._P_MOTOR(                         self,  Access.R,    0x01C1,  block,  False)
        self.INPUTS_RAW                        =  self._INPUTS_RAW(                      self,  Access.R,    0x01C2,  block,  False)
        self.OUTPUTS_RAW                       =  self._OUTPUTS_RAW(                     self,  Access.R,    0x01C3,  block,  False)
        self.STATUS_FLAGS                      =  self._STATUS_FLAGS(                    self,  Access.RWC,  0x01C4,  block,  False)
        self.GDRV_HW                           =  self._GDRV_HW(                         self,  Access.RW,   0x01E3,  block,  False)
        self.GDRV_CFG                          =  self._GDRV_CFG(                        self,  Access.RW,   0x01E4,  block,  False)
        self.GDRV_TIMING                       =  self._GDRV_TIMING(                     self,  Access.RW,   0x01E9,  block,  False)
        self.GDRV_BBM                          =  self._GDRV_BBM(                        self,  Access.RW,   0x01EA,  block,  False)
        self.GDRV_PROT                         =  self._GDRV_PROT(                       self,  Access.RW,   0x01EB,  block,  False)
        self.GDRV_OCP_UVW                      =  self._GDRV_OCP_UVW(                    self,  Access.RW,   0x01EC,  block,  False)
        self.GDRV_OCP_Y2                       =  self._GDRV_OCP_Y2(                     self,  Access.RW,   0x01ED,  block,  False)
        self.GDRV_PROT_EN                      =  self._GDRV_PROT_EN(                    self,  Access.RW,   0x01EE,  block,  False)
        self.GDRV_STATUS_EN                    =  self._GDRV_STATUS_EN(                  self,  Access.RW,   0x01EF,  block,  False)
        self.GDRV_STATUS                       =  self._GDRV_STATUS(                     self,  Access.RWC,  0x01F0,  block,  False)
        self.GDRV_FAULT                        =  self._GDRV_FAULT(                      self,  Access.RWC,  0x01F1,  block,  False)
        self.ADC_I1_I0_EXT                     =  self._ADC_I1_I0_EXT(                   self,  Access.RW,   0x0200,  block,  False)
        self.ADC_I2_EXT                        =  self._ADC_I2_EXT(                      self,  Access.RW,   0x0201,  block,  True)
        self.PWM_VX2_UX1_EXT                   =  self._PWM_VX2_UX1_EXT(                 self,  Access.RW,   0x0202,  block,  False)
        self.PWM_Y2_WY1_EXT                    =  self._PWM_Y2_WY1_EXT(                  self,  Access.RW,   0x0203,  block,  False)
        self.PWM_EXT_Y2_ALT                    =  self._PWM_EXT_Y2_ALT(                  self,  Access.RW,   0x0204,  block,  False)
        self.VOLTAGE_EXT                       =  self._VOLTAGE_EXT(                     self,  Access.RW,   0x0205,  block,  False)
        self.PHI_EXT                           =  self._PHI_EXT(                         self,  Access.RW,   0x0206,  block,  False)
        self.VELOCITY_EXT                      =  self._VELOCITY_EXT(                    self,  Access.RW,   0x0208,  block,  True)
