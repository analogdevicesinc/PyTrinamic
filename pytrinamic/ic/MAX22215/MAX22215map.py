################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from typing import TypedDict

from pytrinamic.ic import Access, RegisterGroup, Option, Field, Register


class MAX22215Map:

    def __init__(self, *, channel=None, block=None, width=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(channel, block, width)


_CFG_1_SR_FIELD_CHOICES = TypedDict("_CFG_1_SR_FIELD_CHOICES", {
    "200 V/µs": Option,
    "100 V/µs": Option,
    "50 V/µs": Option,
    "25 V/µs": Option,
})


_CFG_1_GAIN_FIELD_CHOICES = TypedDict("_CFG_1_GAIN_FIELD_CHOICES", {
    "25": Option,
    "50": Option,
    "100": Option,
    "200": Option,
})


_CFG_1_ODM_FIELD_CHOICES = TypedDict("_CFG_1_ODM_FIELD_CHOICES", {
    "12X": Option,
    "18X": Option,
    "24X": Option,
    "60X": Option,
})


_CFG_2_DEMAG_FIELD_CHOICES = TypedDict("_CFG_2_DEMAG_FIELD_CHOICES", {
    "Disabled": Option,
    "8V": Option,
    "10V": Option,
    "12V": Option,
    "14V": Option,
    "16V": Option,
    "18V": Option,
    "20V": Option,
})


_ACTION_ENABLE_ODVM_TIME_FIELD_CHOICES = TypedDict("_ACTION_ENABLE_ODVM_TIME_FIELD_CHOICES", {
    "100 ms": Option,
    "200 ms": Option,
    "400 ms": Option,
    "800 ms": Option,
})


class _ALL_REGISTERS(RegisterGroup):

    class _CHIP_REV(Register):

        class _CHIP_REV(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHIP_REV", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("CHIP_REV", parent, access, address, signed)
            self.CHIP_REV  =  self._CHIP_REV(self,  Access.R,  0x0000000F,  0,  signed=False)

    class _CFG_1(Register):

        class _SR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SR", parent, access, mask, shift, signed=signed)

                self.choice : _CFG_1_SR_FIELD_CHOICES = {
                    "200 V/µs": Option(0, self),
                    "100 V/µs": Option(1, self),
                    "50 V/µs": Option(2, self),
                    "25 V/µs": Option(3, self),
                }

        class _GAIN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GAIN", parent, access, mask, shift, signed=signed)

                self.choice : _CFG_1_GAIN_FIELD_CHOICES = {
                    "25": Option(0, self),
                    "50": Option(1, self),
                    "100": Option(2, self),
                    "200": Option(3, self),
                }

        class _SW_HW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SW_HW", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ODM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ODM", parent, access, mask, shift, signed=signed)

                self.choice : _CFG_1_ODM_FIELD_CHOICES = {
                    "12X": Option(0, self),
                    "18X": Option(1, self),
                    "24X": Option(2, self),
                    "60X": Option(3, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("CFG_1", parent, access, address, signed)
            self.SR     =  self._SR(   self,  Access.RW,  0x00000003,  0,  signed=False)
            self.GAIN   =  self._GAIN( self,  Access.RW,  0x0000000C,  2,  signed=False)
            self.SW_HW  =  self._SW_HW(self,  Access.RW,  0x00000010,  4,  signed=False)
            self.ODM    =  self._ODM(  self,  Access.RW,  0x00000060,  5,  signed=False)

    class _CFG_2(Register):

        class _RESET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DEMAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DEMAG", parent, access, mask, shift, signed=signed)

                self.choice : _CFG_2_DEMAG_FIELD_CHOICES = {
                    "Disabled": Option(0, self),
                    "8V": Option(1, self),
                    "10V": Option(2, self),
                    "12V": Option(3, self),
                    "14V": Option(4, self),
                    "16V": Option(5, self),
                    "18V": Option(6, self),
                    "20V": Option(7, self),
                }

        class _NSLEEP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NSLEEP", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DIAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _RLS_BRK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RLS_BRK", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("CFG_2", parent, access, address, signed)
            self.RESET    =  self._RESET(  self,  Access.W,   0x00000002,  1,  signed=False)
            self.DEMAG    =  self._DEMAG(  self,  Access.RW,  0x0000001C,  2,  signed=False)
            self.NSLEEP   =  self._NSLEEP( self,  Access.RW,  0x00000020,  5,  signed=False)
            self.DIAG     =  self._DIAG(   self,  Access.RW,  0x00000040,  6,  signed=False)
            self.RLS_BRK  =  self._RLS_BRK(self,  Access.RW,  0x00000080,  7,  signed=False)

    class _FAULT1(Register):

        class _OCP0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OCP0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OCP1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OCP1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OCP2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OCP2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TWARN_UL(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TWARN_UL", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TSD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UVLO5V(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UVLO5V", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UVLOCP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UVLOCP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("FAULT1", parent, access, address, signed)
            self.OCP0      =  self._OCP0(    self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.OCP1      =  self._OCP1(    self,  Access.RWC,  0x00000002,  1,  signed=False)
            self.OCP2      =  self._OCP2(    self,  Access.RWC,  0x00000004,  2,  signed=False)
            self.TWARN_UL  =  self._TWARN_UL(self,  Access.RWC,  0x00000008,  3,  signed=False)
            self.TSD       =  self._TSD(     self,  Access.RWC,  0x00000010,  4,  signed=False)
            self.UVLO      =  self._UVLO(    self,  Access.RWC,  0x00000020,  5,  signed=False)
            self.UVLO5V    =  self._UVLO5V(  self,  Access.RWC,  0x00000040,  6,  signed=False)
            self.UVLOCP    =  self._UVLOCP(  self,  Access.RWC,  0x00000080,  7,  signed=False)

    class _FAULT2(Register):

        class _LFD1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LFD1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LFD2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LFD2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SAFEDEM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SAFEDEM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ISM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ISM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ODVM(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ODVM", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DVD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DVD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TWARN(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TWARN", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LFD3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LFD3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("FAULT2", parent, access, address, signed)
            self.LFD1     =  self._LFD1(   self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.LFD2     =  self._LFD2(   self,  Access.RWC,  0x00000002,  1,  signed=False)
            self.SAFEDEM  =  self._SAFEDEM(self,  Access.RWC,  0x00000004,  2,  signed=False)
            self.ISM      =  self._ISM(    self,  Access.RWC,  0x00000008,  3,  signed=False)
            self.ODVM     =  self._ODVM(   self,  Access.RWC,  0x00000010,  4,  signed=False)
            self.DVD      =  self._DVD(    self,  Access.RWC,  0x00000020,  5,  signed=False)
            self.TWARN    =  self._TWARN(  self,  Access.RWC,  0x00000040,  6,  signed=False)
            self.LFD3     =  self._LFD3(   self,  Access.RWC,  0x00000080,  7,  signed=False)

    class _FAULT_MASK1(Register):

        class _OCP0_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OCP0_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OCP1_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OCP1_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OCP2_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OCP2_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TWARN_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TWARN_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _TSDN_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TSDN_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UVLO_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UVLO_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UVLO_5V_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UVLO_5V_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UVLO_CP_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UVLO_CP_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("FAULT_MASK1", parent, access, address, signed)
            self.OCP0_MASK     =  self._OCP0_MASK(   self,  Access.RW,  0x00000001,  0,  signed=False)
            self.OCP1_MASK     =  self._OCP1_MASK(   self,  Access.RW,  0x00000002,  1,  signed=False)
            self.OCP2_MASK     =  self._OCP2_MASK(   self,  Access.RW,  0x00000004,  2,  signed=False)
            self.TWARN_MASK    =  self._TWARN_MASK(  self,  Access.RW,  0x00000008,  3,  signed=False)
            self.TSDN_MASK     =  self._TSDN_MASK(   self,  Access.RW,  0x00000010,  4,  signed=False)
            self.UVLO_MASK     =  self._UVLO_MASK(   self,  Access.RW,  0x00000020,  5,  signed=False)
            self.UVLO_5V_MASK  =  self._UVLO_5V_MASK(self,  Access.RW,  0x00000040,  6,  signed=False)
            self.UVLO_CP_MASK  =  self._UVLO_CP_MASK(self,  Access.RW,  0x00000080,  7,  signed=False)

    class _FAULT_MASK2(Register):

        class _LFD1_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LFD1_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LFD2_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LFD2_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SAFEDEM_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SAFEDEM_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ISM_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ISM_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ODVM_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ODVM_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _DVD_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DVD_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LFD3_MASK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LFD3_MASK", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("FAULT_MASK2", parent, access, address, signed)
            self.LFD1_MASK     =  self._LFD1_MASK(   self,  Access.RW,  0x00000001,  0,  signed=False)
            self.LFD2_MASK     =  self._LFD2_MASK(   self,  Access.RW,  0x00000002,  1,  signed=False)
            self.SAFEDEM_MASK  =  self._SAFEDEM_MASK(self,  Access.RW,  0x00000004,  2,  signed=False)
            self.ISM_MASK      =  self._ISM_MASK(    self,  Access.RW,  0x00000008,  3,  signed=False)
            self.ODVM_MASK     =  self._ODVM_MASK(   self,  Access.RW,  0x00000010,  4,  signed=False)
            self.DVD_MASK      =  self._DVD_MASK(    self,  Access.RW,  0x00000020,  5,  signed=False)
            self.LFD3_MASK     =  self._LFD3_MASK(   self,  Access.RW,  0x00000080,  7,  signed=False)

    class _ACTION_ENABLE(Register):

        class _ENABLE1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ENABLE3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENABLE3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _ODVM_TIME(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ODVM_TIME", parent, access, mask, shift, signed=signed)

                self.choice : _ACTION_ENABLE_ODVM_TIME_FIELD_CHOICES = {
                    "100 ms": Option(0, self),
                    "200 ms": Option(1, self),
                    "400 ms": Option(2, self),
                    "800 ms": Option(3, self),
                }

        def __init__(self, parent, access, address, signed):
            super().__init__("ACTION_ENABLE", parent, access, address, signed)
            self.ENABLE1    =  self._ENABLE1(  self,  Access.RW,  0x00000001,  0,  signed=False)
            self.ENABLE2    =  self._ENABLE2(  self,  Access.RW,  0x00000002,  1,  signed=False)
            self.ENABLE3    =  self._ENABLE3(  self,  Access.RW,  0x00000004,  2,  signed=False)
            self.ODVM_TIME  =  self._ODVM_TIME(self,  Access.RW,  0x00000018,  3,  signed=False)

    class _CONTROL_STS(Register):

        class _STATUS_SLEEP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_SLEEP", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_BRK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_BRK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_RLS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_RLS", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_DIAG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_DIAG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_ENF_DMG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_ENF_DMG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_SAFE_DMG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_SAFE_DMG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _STATUS_FLT_PWP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS_FLT_PWP", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, signed):
            super().__init__("CONTROL_STS", parent, access, address, signed)
            self.STATUS_SLEEP     =  self._STATUS_SLEEP(   self,  Access.R,  0x00000001,  0,  signed=False)
            self.STATUS_BRK       =  self._STATUS_BRK(     self,  Access.R,  0x00000002,  1,  signed=False)
            self.STATUS_RLS       =  self._STATUS_RLS(     self,  Access.R,  0x00000004,  2,  signed=False)
            self.STATUS_DIAG      =  self._STATUS_DIAG(    self,  Access.R,  0x00000008,  3,  signed=False)
            self.STATUS_ENF_DMG   =  self._STATUS_ENF_DMG( self,  Access.R,  0x00000010,  4,  signed=False)
            self.STATUS_SAFE_DMG  =  self._STATUS_SAFE_DMG(self,  Access.R,  0x00000020,  5,  signed=False)
            self.STATUS_FLT_PWP   =  self._STATUS_FLT_PWP( self,  Access.R,  0x00000080,  7,  signed=False)

    def __init__(self, channel, block, width):
        super().__init__("ALL_REGISTERS", channel, block, width)
        self.CHIP_REV       =  self._CHIP_REV(     self,  Access.R,    0x0000,  False)
        self.CFG_1          =  self._CFG_1(        self,  Access.RW,   0x0001,  False)
        self.CFG_2          =  self._CFG_2(        self,  Access.RW,   0x0002,  False)
        self.FAULT1         =  self._FAULT1(       self,  Access.RWC,  0x0003,  False)
        self.FAULT2         =  self._FAULT2(       self,  Access.RWC,  0x0004,  False)
        self.FAULT_MASK1    =  self._FAULT_MASK1(  self,  Access.RW,   0x0005,  False)
        self.FAULT_MASK2    =  self._FAULT_MASK2(  self,  Access.RW,   0x0006,  False)
        self.ACTION_ENABLE  =  self._ACTION_ENABLE(self,  Access.RW,   0x0007,  False)
        self.CONTROL_STS    =  self._CONTROL_STS(  self,  Access.R,    0x0008,  False)
