################################################################################
# Copyright © 2026 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterSet, RegisterGroup, Choice, Option, Field, Register


class TMC6460Map(RegisterSet):
    def __init__(self, *, channel=None, block=None, width=None):
        self.CHIP          = _CHIP(channel, block, width)
        self.CLK_CTRL      = _CLK_CTRL(channel, block, width)
        self.ADC           = _ADC(channel, block, width)
        self.MCC_ADC       = _MCC_ADC(channel, block, width)
        self.MCC_CONFIG    = _MCC_CONFIG(channel, block, width)
        self.FOC           = _FOC(channel, block, width)
        self.BIQUAD        = _BIQUAD(channel, block, width)
        self.RAMPER        = _RAMPER(channel, block, width)
        self.EXT_CTRL      = _EXT_CTRL(channel, block, width)
        self.FEEDBACK      = _FEEDBACK(channel, block, width)
        self.ABN           = _ABN(channel, block, width)
        self.ABN2          = _ABN2(channel, block, width)
        self.HALL          = _HALL(channel, block, width)
        self.UART          = _UART(channel, block, width)
        self.IO_CONTROLLER = _IO_CONTROLLER(channel, block, width)


class _CHIP(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("CHIP", channel, block, width)
        self.ID               =  self._ID(             self,  Access.R,    0x0000,  False)
        self.VARIANT          =  self._VARIANT(        self,  Access.R,    0x0001,  False)
        self.REVISION         =  self._REVISION(       self,  Access.R,    0x0002,  False)
        self.INPUTS_RAW       =  self._INPUTS_RAW(     self,  Access.R,    0x0004,  False)
        self.OUTPUTS_RAW      =  self._OUTPUTS_RAW(    self,  Access.R,    0x0005,  False)
        self.IO_MATRIX        =  self._IO_MATRIX(      self,  Access.RW,   0x0006,  False)
        self.IO_PU_PD         =  self._IO_PU_PD(       self,  Access.RW,   0x0007,  False)
        self.IO_CONFIG        =  self._IO_CONFIG(      self,  Access.RW,   0x0008,  False)
        self.STATUS_FLAGS     =  self._STATUS_FLAGS(   self,  Access.R,    0x0009,  False)
        self.EVENTS           =  self._EVENTS(         self,  Access.RWC,  0x000A,  False)
        self.FAULTN_INT_MASK  =  self._FAULTN_INT_MASK(self,  Access.RW,   0x000B,  False)
        self.SPI_STATUS_MASK  =  self._SPI_STATUS_MASK(self,  Access.RW,   0x000C,  False)

    class _ID(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ID", parent, access, address, signed)
            self.ID  =  self._ID(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

        class _ID(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ID", parent, access, mask, shift, signed=signed)

    class _VARIANT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VARIANT", parent, access, address, signed)
            self.VARIANT  =  self._VARIANT(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

        class _VARIANT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VARIANT", parent, access, mask, shift, signed=signed)

    class _REVISION(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("REVISION", parent, access, address, signed)
            self.REVISION  =  self._REVISION(self,  Access.R,  0x7FFFFFFF,  0,  signed=False)

        class _REVISION(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REVISION", parent, access, mask, shift, signed=signed)

    class _INPUTS_RAW(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("INPUTS_RAW", parent, access, address, signed)
            self.PIN_ENC_A_RAW     =  self._PIN_ENC_A_RAW(   self,  Access.R,  0x00000001,  0,   signed=False)
            self.PIN_ENC_B_RAW     =  self._PIN_ENC_B_RAW(   self,  Access.R,  0x00000002,  1,   signed=False)
            self.PIN_ENC_N_RAW     =  self._PIN_ENC_N_RAW(   self,  Access.R,  0x00000004,  2,   signed=False)
            self.PIN_HALL_U_RAW    =  self._PIN_HALL_U_RAW(  self,  Access.R,  0x00000008,  3,   signed=False)
            self.PIN_HALL_V_RAW    =  self._PIN_HALL_V_RAW(  self,  Access.R,  0x00000010,  4,   signed=False)
            self.PIN_HALL_W_RAW    =  self._PIN_HALL_W_RAW(  self,  Access.R,  0x00000020,  5,   signed=False)
            self.PIN_REF_L_RAW     =  self._PIN_REF_L_RAW(   self,  Access.R,  0x00000040,  6,   signed=False)
            self.PIN_REF_R_RAW     =  self._PIN_REF_R_RAW(   self,  Access.R,  0x00000080,  7,   signed=False)
            self.PIN_SDI_RAW       =  self._PIN_SDI_RAW(     self,  Access.R,  0x00000100,  8,   signed=False)
            self.PIN_SDO_RAW       =  self._PIN_SDO_RAW(     self,  Access.R,  0x00000200,  9,   signed=False)
            self.PIN_SCK_RAW       =  self._PIN_SCK_RAW(     self,  Access.R,  0x00000400,  10,  signed=False)
            self.PIN_CSN_RAW       =  self._PIN_CSN_RAW(     self,  Access.R,  0x00000800,  11,  signed=False)
            self.PIN_PWM_IN_RAW    =  self._PIN_PWM_IN_RAW(  self,  Access.R,  0x00001000,  12,  signed=False)
            self.PIN_UART_RXD_RAW  =  self._PIN_UART_RXD_RAW(self,  Access.R,  0x00002000,  13,  signed=False)
            self.PIN_DRV_EN        =  self._PIN_DRV_EN(      self,  Access.R,  0x00008000,  15,  signed=False)
            self.ENC_A             =  self._ENC_A(           self,  Access.R,  0x00010000,  16,  signed=False)
            self.ENC_B             =  self._ENC_B(           self,  Access.R,  0x00020000,  17,  signed=False)
            self.ENC_N             =  self._ENC_N(           self,  Access.R,  0x00040000,  18,  signed=False)
            self.ENC2_A            =  self._ENC2_A(          self,  Access.R,  0x00080000,  19,  signed=False)
            self.ENC2_B            =  self._ENC2_B(          self,  Access.R,  0x00100000,  20,  signed=False)
            self.ENC2_N            =  self._ENC2_N(          self,  Access.R,  0x00200000,  21,  signed=False)
            self.HALL_U            =  self._HALL_U(          self,  Access.R,  0x00400000,  22,  signed=False)
            self.HALL_V            =  self._HALL_V(          self,  Access.R,  0x00800000,  23,  signed=False)
            self.HALL_W            =  self._HALL_W(          self,  Access.R,  0x01000000,  24,  signed=False)
            self.REF_L             =  self._REF_L(           self,  Access.R,  0x02000000,  25,  signed=False)
            self.REF_R             =  self._REF_R(           self,  Access.R,  0x04000000,  26,  signed=False)
            self.REF_H             =  self._REF_H(           self,  Access.R,  0x08000000,  27,  signed=False)
            self.DIRECT_IN0        =  self._DIRECT_IN0(      self,  Access.R,  0x10000000,  28,  signed=False)
            self.DIRECT_IN1        =  self._DIRECT_IN1(      self,  Access.R,  0x20000000,  29,  signed=False)
            self.DIR_IN            =  self._DIR_IN(          self,  Access.R,  0x40000000,  30,  signed=False)
            self.PWM_IN            =  self._PWM_IN(          self,  Access.R,  0x80000000,  31,  signed=False)

        class _PIN_ENC_A_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_A_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_ENC_B_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_B_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_ENC_N_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_N_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_HALL_U_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_U_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_HALL_V_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_V_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_HALL_W_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_W_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_REF_L_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_REF_L_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_REF_R_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_REF_R_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_SDI_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SDI_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_SDO_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SDO_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_SCK_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SCK_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_CSN_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_CSN_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_PWM_IN_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_PWM_IN_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_UART_RXD_RAW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_UART_RXD_RAW", parent, access, mask, shift, signed=signed)

        class _PIN_DRV_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_DRV_EN", parent, access, mask, shift, signed=signed)

        class _ENC_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_A", parent, access, mask, shift, signed=signed)

        class _ENC_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_B", parent, access, mask, shift, signed=signed)

        class _ENC_N(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_N", parent, access, mask, shift, signed=signed)

        class _ENC2_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC2_A", parent, access, mask, shift, signed=signed)

        class _ENC2_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC2_B", parent, access, mask, shift, signed=signed)

        class _ENC2_N(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC2_N", parent, access, mask, shift, signed=signed)

        class _HALL_U(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_U", parent, access, mask, shift, signed=signed)

        class _HALL_V(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_V", parent, access, mask, shift, signed=signed)

        class _HALL_W(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_W", parent, access, mask, shift, signed=signed)

        class _REF_L(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_L", parent, access, mask, shift, signed=signed)

        class _REF_R(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_R", parent, access, mask, shift, signed=signed)

        class _REF_H(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_H", parent, access, mask, shift, signed=signed)

        class _DIRECT_IN0(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIRECT_IN0", parent, access, mask, shift, signed=signed)

        class _DIRECT_IN1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIRECT_IN1", parent, access, mask, shift, signed=signed)

        class _DIR_IN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIR_IN", parent, access, mask, shift, signed=signed)

        class _PWM_IN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_IN", parent, access, mask, shift, signed=signed)

    class _OUTPUTS_RAW(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("OUTPUTS_RAW", parent, access, address, signed)
            self.PWM_U_L             =  self._PWM_U_L(           self,  Access.R,  0x00000001,  0,   signed=False)
            self.PWM_U_H             =  self._PWM_U_H(           self,  Access.R,  0x00000002,  1,   signed=False)
            self.PWM_V_L             =  self._PWM_V_L(           self,  Access.R,  0x00000004,  2,   signed=False)
            self.PWM_V_H             =  self._PWM_V_H(           self,  Access.R,  0x00000008,  3,   signed=False)
            self.PWM_W_L             =  self._PWM_W_L(           self,  Access.R,  0x00000010,  4,   signed=False)
            self.PWM_W_H             =  self._PWM_W_H(           self,  Access.R,  0x00000020,  5,   signed=False)
            self.INT_OUT             =  self._INT_OUT(           self,  Access.R,  0x00000040,  6,   signed=False)
            self.FAULTN_OUT          =  self._FAULTN_OUT(        self,  Access.R,  0x00000080,  7,   signed=False)
            self.INVALID_DIFF_ENC_A  =  self._INVALID_DIFF_ENC_A(self,  Access.R,  0x01000000,  24,  signed=False)
            self.INVALID_DIFF_ENC_B  =  self._INVALID_DIFF_ENC_B(self,  Access.R,  0x02000000,  25,  signed=False)
            self.INVALID_DIFF_ENC_N  =  self._INVALID_DIFF_ENC_N(self,  Access.R,  0x04000000,  26,  signed=False)

        class _PWM_U_L(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_U_L", parent, access, mask, shift, signed=signed)

        class _PWM_U_H(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_U_H", parent, access, mask, shift, signed=signed)

        class _PWM_V_L(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_V_L", parent, access, mask, shift, signed=signed)

        class _PWM_V_H(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_V_H", parent, access, mask, shift, signed=signed)

        class _PWM_W_L(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_W_L", parent, access, mask, shift, signed=signed)

        class _PWM_W_H(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_W_H", parent, access, mask, shift, signed=signed)

        class _INT_OUT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INT_OUT", parent, access, mask, shift, signed=signed)

        class _FAULTN_OUT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FAULTN_OUT", parent, access, mask, shift, signed=signed)

        class _INVALID_DIFF_ENC_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INVALID_DIFF_ENC_A", parent, access, mask, shift, signed=signed)

        class _INVALID_DIFF_ENC_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INVALID_DIFF_ENC_B", parent, access, mask, shift, signed=signed)

        class _INVALID_DIFF_ENC_N(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INVALID_DIFF_ENC_N", parent, access, mask, shift, signed=signed)

    class _IO_MATRIX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("IO_MATRIX", parent, access, address, signed)
            self.PIN_ENC_A     =  self._PIN_ENC_A(   self,  Access.RW,  0x00000003,  0,   signed=False)
            self.PIN_ENC_B     =  self._PIN_ENC_B(   self,  Access.RW,  0x0000000C,  2,   signed=False)
            self.PIN_ENC_N     =  self._PIN_ENC_N(   self,  Access.RW,  0x00000030,  4,   signed=False)
            self.PIN_HALL_U    =  self._PIN_HALL_U(  self,  Access.RW,  0x000001C0,  6,   signed=False)
            self.PIN_HALL_V    =  self._PIN_HALL_V(  self,  Access.RW,  0x00000E00,  9,   signed=False)
            self.PIN_HALL_W    =  self._PIN_HALL_W(  self,  Access.RW,  0x00007000,  12,  signed=False)
            self.PIN_REF_L     =  self._PIN_REF_L(   self,  Access.RW,  0x00018000,  15,  signed=False)
            self.PIN_REF_R     =  self._PIN_REF_R(   self,  Access.RW,  0x00060000,  17,  signed=False)
            self.PIN_SDI       =  self._PIN_SDI(     self,  Access.RW,  0x00180000,  19,  signed=False)
            self.PIN_SDO       =  self._PIN_SDO(     self,  Access.RW,  0x00600000,  21,  signed=False)
            self.PIN_SCK       =  self._PIN_SCK(     self,  Access.RW,  0x00800000,  23,  signed=False)
            self.PIN_PWM_IN    =  self._PIN_PWM_IN(  self,  Access.RW,  0x03000000,  24,  signed=False)
            self.PIN_UART_RXD  =  self._PIN_UART_RXD(self,  Access.RW,  0x0C000000,  26,  signed=False)
            self.PIN_UART_TXD  =  self._PIN_UART_TXD(self,  Access.RW,  0x30000000,  28,  signed=False)
            self.PIN_FAULTN    =  self._PIN_FAULTN(  self,  Access.RW,  0xC0000000,  30,  signed=False)

        class _PIN_ENC_A(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ENC_A        =  Option(0,  parent,  "ENC_A")
                    self.AINN_U       =  Option(1,  parent,  "AINN_U")
                    self.HALL_U       =  Option(2,  parent,  "HALL_U")
                    self.DIRECT_OUT0  =  Option(3,  parent,  "DIRECT_OUT0")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_A", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_ENC_B(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ENC_B       =  Option(0,  parent,  "ENC_B")
                    self.AINN_V      =  Option(1,  parent,  "AINN_V")
                    self.HALL_V      =  Option(2,  parent,  "HALL_V")
                    self.DIRECT_IN0  =  Option(3,  parent,  "DIRECT_IN0")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_B", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_ENC_N(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ENC_N            =  Option(0,  parent,  "ENC_N")
                    self.AINN_W           =  Option(1,  parent,  "AINN_W")
                    self.HALL_W           =  Option(2,  parent,  "HALL_W")
                    self.DIRECT_IN1_OUT1  =  Option(3,  parent,  "DIRECT_IN1_OUT1")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_N", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_HALL_U(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HALL_U                  =  Option(0,  parent,  "HALL_U")
                    self.AINP_U                  =  Option(1,  parent,  "AINP_U")
                    self.ENC2_A                  =  Option(2,  parent,  "ENC2_A")
                    self.SDA                     =  Option(3,  parent,  "SDA")
                    self.DIG_DIFF_ENC_A_MONITOR  =  Option(6,  parent,  "DIG_DIFF_ENC_A_MONITOR")
                    self.DIG_DIFF_ENC_A_N        =  Option(7,  parent,  "DIG_DIFF_ENC_A_N")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_U", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_HALL_V(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HALL_V                  =  Option(0,  parent,  "HALL_V")
                    self.AINP_V                  =  Option(1,  parent,  "AINP_V")
                    self.ENC2_B                  =  Option(2,  parent,  "ENC2_B")
                    self.SCL                     =  Option(3,  parent,  "SCL")
                    self.BRAKE                   =  Option(4,  parent,  "BRAKE")
                    self.SCL_OD                  =  Option(5,  parent,  "SCL_OD")
                    self.DIG_DIFF_ENC_B_MONITOR  =  Option(6,  parent,  "DIG_DIFF_ENC_B_MONITOR")
                    self.DIG_DIFF_ENC_B_N        =  Option(7,  parent,  "DIG_DIFF_ENC_B_N")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_V", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_HALL_W(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.HALL_W                  =  Option(0,  parent,  "HALL_W")
                    self.AINP_W                  =  Option(1,  parent,  "AINP_W")
                    self.ENC2_N                  =  Option(2,  parent,  "ENC2_N")
                    self.DIRECT_OUT2             =  Option(3,  parent,  "DIRECT_OUT2")
                    self.REF_H                   =  Option(4,  parent,  "REF_H")
                    self.DIG_DIFF_ENC_N_MONITOR  =  Option(6,  parent,  "DIG_DIFF_ENC_N_MONITOR")
                    self.DIG_DIFF_ENC_N_N        =  Option(7,  parent,  "DIG_DIFF_ENC_N_N")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_W", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_REF_L(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.REF_L       =  Option(0,  parent,  "REF_L")
                    self.REF_H       =  Option(1,  parent,  "REF_H")
                    self.DIRECT_IN0  =  Option(3,  parent,  "DIRECT_IN0")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_REF_L", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_REF_R(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.REF_R        =  Option(0,  parent,  "REF_R")
                    self.REF_H        =  Option(1,  parent,  "REF_H")
                    self.BRAKE        =  Option(2,  parent,  "BRAKE")
                    self.DIRECT_OUT1  =  Option(3,  parent,  "DIRECT_OUT1")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_REF_R", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_SDI(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SDI         =  Option(0,  parent,  "SDI")
                    self.DIR_IN      =  Option(1,  parent,  "DIR_IN")
                    self.DIRECT_IN0  =  Option(3,  parent,  "DIRECT_IN0")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SDI", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_SDO(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SDO          =  Option(0,  parent,  "SDO")
                    self.BRAKE        =  Option(1,  parent,  "BRAKE")
                    self.DIRECT_OUT0  =  Option(3,  parent,  "DIRECT_OUT0")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SDO", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_SCK(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SCK         =  Option(0,  parent,  "SCK")
                    self.DIRECT_IN1  =  Option(1,  parent,  "DIRECT_IN1")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SCK", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_PWM_IN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.PWM_IN      =  Option(0,  parent,  "PWM_IN")
                    self.AIN         =  Option(1,  parent,  "AIN")
                    self.DIRECT_IN1  =  Option(3,  parent,  "DIRECT_IN1")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_PWM_IN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_UART_RXD(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.UART_RXD    =  Option(0,  parent,  "UART_RXD")
                    self.DIR_IN      =  Option(1,  parent,  "DIR_IN")
                    self.DIRECT_IN0  =  Option(3,  parent,  "DIRECT_IN0")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_UART_RXD", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_UART_TXD(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.UART_TXD     =  Option(0,  parent,  "UART_TXD")
                    self.BRAKE        =  Option(1,  parent,  "BRAKE")
                    self.DIRECT_OUT0  =  Option(2,  parent,  "DIRECT_OUT0")
                    self.DIRECT_OUT1  =  Option(3,  parent,  "DIRECT_OUT1")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_UART_TXD", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PIN_FAULTN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.FAULTN_OD  =  Option(0,  parent,  "FAULTN_OD")
                    self.INT_OD     =  Option(1,  parent,  "INT_OD")
                    self.FAULTN_PP  =  Option(2,  parent,  "FAULTN_PP")
                    self.INT_PP     =  Option(3,  parent,  "INT_PP")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_FAULTN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _IO_PU_PD(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("IO_PU_PD", parent, access, address, signed)
            self.PIN_ENC_A_PU     =  self._PIN_ENC_A_PU(   self,  Access.RW,  0x00000001,  0,   signed=False)
            self.PIN_ENC_B_PU     =  self._PIN_ENC_B_PU(   self,  Access.RW,  0x00000002,  1,   signed=False)
            self.PIN_ENC_N_PU     =  self._PIN_ENC_N_PU(   self,  Access.RW,  0x00000004,  2,   signed=False)
            self.PIN_HALL_U_PU    =  self._PIN_HALL_U_PU(  self,  Access.RW,  0x00000008,  3,   signed=False)
            self.PIN_HALL_V_PU    =  self._PIN_HALL_V_PU(  self,  Access.RW,  0x00000010,  4,   signed=False)
            self.PIN_HALL_W_PU    =  self._PIN_HALL_W_PU(  self,  Access.RW,  0x00000020,  5,   signed=False)
            self.PIN_REF_L_PU     =  self._PIN_REF_L_PU(   self,  Access.RW,  0x00000040,  6,   signed=False)
            self.PIN_REF_R_PU     =  self._PIN_REF_R_PU(   self,  Access.RW,  0x00000080,  7,   signed=False)
            self.PIN_ENC_A_PD     =  self._PIN_ENC_A_PD(   self,  Access.RW,  0x00000100,  8,   signed=False)
            self.PIN_ENC_B_PD     =  self._PIN_ENC_B_PD(   self,  Access.RW,  0x00000200,  9,   signed=False)
            self.PIN_ENC_N_PD     =  self._PIN_ENC_N_PD(   self,  Access.RW,  0x00000400,  10,  signed=False)
            self.PIN_HALL_U_PD    =  self._PIN_HALL_U_PD(  self,  Access.RW,  0x00000800,  11,  signed=False)
            self.PIN_HALL_V_PD    =  self._PIN_HALL_V_PD(  self,  Access.RW,  0x00001000,  12,  signed=False)
            self.PIN_HALL_W_PD    =  self._PIN_HALL_W_PD(  self,  Access.RW,  0x00002000,  13,  signed=False)
            self.PIN_REF_L_PD     =  self._PIN_REF_L_PD(   self,  Access.RW,  0x00004000,  14,  signed=False)
            self.PIN_REF_R_PD     =  self._PIN_REF_R_PD(   self,  Access.RW,  0x00008000,  15,  signed=False)
            self.PIN_SDI_PU       =  self._PIN_SDI_PU(     self,  Access.RW,  0x00010000,  16,  signed=False)
            self.PIN_SCK_PU       =  self._PIN_SCK_PU(     self,  Access.RW,  0x00020000,  17,  signed=False)
            self.PIN_PWM_IN_PU    =  self._PIN_PWM_IN_PU(  self,  Access.RW,  0x00040000,  18,  signed=False)
            self.PIN_UART_RXD_PU  =  self._PIN_UART_RXD_PU(self,  Access.RW,  0x00080000,  19,  signed=False)
            self.PIN_SDO_PU       =  self._PIN_SDO_PU(     self,  Access.RW,  0x00100000,  20,  signed=False)
            self.PIN_FAULTN_PU    =  self._PIN_FAULTN_PU(  self,  Access.RW,  0x00400000,  22,  signed=False)
            self.PIN_SDI_PD       =  self._PIN_SDI_PD(     self,  Access.RW,  0x01000000,  24,  signed=False)
            self.PIN_SCK_PD       =  self._PIN_SCK_PD(     self,  Access.RW,  0x02000000,  25,  signed=False)
            self.PIN_PWM_IN_PD    =  self._PIN_PWM_IN_PD(  self,  Access.RW,  0x04000000,  26,  signed=False)
            self.PIN_UART_RXD_PD  =  self._PIN_UART_RXD_PD(self,  Access.RW,  0x08000000,  27,  signed=False)

        class _PIN_ENC_A_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_A_PU", parent, access, mask, shift, signed=signed)

        class _PIN_ENC_B_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_B_PU", parent, access, mask, shift, signed=signed)

        class _PIN_ENC_N_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_N_PU", parent, access, mask, shift, signed=signed)

        class _PIN_HALL_U_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_U_PU", parent, access, mask, shift, signed=signed)

        class _PIN_HALL_V_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_V_PU", parent, access, mask, shift, signed=signed)

        class _PIN_HALL_W_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_W_PU", parent, access, mask, shift, signed=signed)

        class _PIN_REF_L_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_REF_L_PU", parent, access, mask, shift, signed=signed)

        class _PIN_REF_R_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_REF_R_PU", parent, access, mask, shift, signed=signed)

        class _PIN_ENC_A_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_A_PD", parent, access, mask, shift, signed=signed)

        class _PIN_ENC_B_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_B_PD", parent, access, mask, shift, signed=signed)

        class _PIN_ENC_N_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_ENC_N_PD", parent, access, mask, shift, signed=signed)

        class _PIN_HALL_U_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_U_PD", parent, access, mask, shift, signed=signed)

        class _PIN_HALL_V_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_V_PD", parent, access, mask, shift, signed=signed)

        class _PIN_HALL_W_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_HALL_W_PD", parent, access, mask, shift, signed=signed)

        class _PIN_REF_L_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_REF_L_PD", parent, access, mask, shift, signed=signed)

        class _PIN_REF_R_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_REF_R_PD", parent, access, mask, shift, signed=signed)

        class _PIN_SDI_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SDI_PU", parent, access, mask, shift, signed=signed)

        class _PIN_SCK_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SCK_PU", parent, access, mask, shift, signed=signed)

        class _PIN_PWM_IN_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_PWM_IN_PU", parent, access, mask, shift, signed=signed)

        class _PIN_UART_RXD_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_UART_RXD_PU", parent, access, mask, shift, signed=signed)

        class _PIN_SDO_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SDO_PU", parent, access, mask, shift, signed=signed)

        class _PIN_FAULTN_PU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_FAULTN_PU", parent, access, mask, shift, signed=signed)

        class _PIN_SDI_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SDI_PD", parent, access, mask, shift, signed=signed)

        class _PIN_SCK_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_SCK_PD", parent, access, mask, shift, signed=signed)

        class _PIN_PWM_IN_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_PWM_IN_PD", parent, access, mask, shift, signed=signed)

        class _PIN_UART_RXD_PD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIN_UART_RXD_PD", parent, access, mask, shift, signed=signed)

    class _IO_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("IO_CONFIG", parent, access, address, signed)
            self.INV_PIN_ENC_A           =  self._INV_PIN_ENC_A(         self,  Access.RW,  0x00000001,  0,   signed=False)
            self.INV_PIN_ENC_B           =  self._INV_PIN_ENC_B(         self,  Access.RW,  0x00000002,  1,   signed=False)
            self.INV_PIN_ENC_N           =  self._INV_PIN_ENC_N(         self,  Access.RW,  0x00000004,  2,   signed=False)
            self.INV_PIN_HALL_U          =  self._INV_PIN_HALL_U(        self,  Access.RW,  0x00000008,  3,   signed=False)
            self.INV_PIN_HALL_V          =  self._INV_PIN_HALL_V(        self,  Access.RW,  0x00000010,  4,   signed=False)
            self.INV_PIN_HALL_W          =  self._INV_PIN_HALL_W(        self,  Access.RW,  0x00000020,  5,   signed=False)
            self.INV_PIN_REF_L           =  self._INV_PIN_REF_L(         self,  Access.RW,  0x00000040,  6,   signed=False)
            self.INV_PIN_REF_R           =  self._INV_PIN_REF_R(         self,  Access.RW,  0x00000080,  7,   signed=False)
            self.INV_PIN_SDI             =  self._INV_PIN_SDI(           self,  Access.RW,  0x00000100,  8,   signed=False)
            self.INV_PIN_SCK             =  self._INV_PIN_SCK(           self,  Access.RW,  0x00000200,  9,   signed=False)
            self.INV_PIN_PWM_IN          =  self._INV_PIN_PWM_IN(        self,  Access.RW,  0x00000400,  10,  signed=False)
            self.INV_PIN_RXD             =  self._INV_PIN_RXD(           self,  Access.RW,  0x00000800,  11,  signed=False)
            self.ENC_FLT                 =  self._ENC_FLT(               self,  Access.RW,  0x00003000,  12,  signed=False)
            self.HALL_FLT                =  self._HALL_FLT(              self,  Access.RW,  0x0000C000,  14,  signed=False)
            self.REF_FLT                 =  self._REF_FLT(               self,  Access.RW,  0x00030000,  16,  signed=False)
            self.PWM_IN_FLT              =  self._PWM_IN_FLT(            self,  Access.RW,  0x000C0000,  18,  signed=False)
            self.ANA_DIV_VCCIO           =  self._ANA_DIV_VCCIO(         self,  Access.RW,  0x00300000,  20,  signed=False)
            self.ANA_DIV_VCCIOF          =  self._ANA_DIV_VCCIOF(        self,  Access.RW,  0x00C00000,  22,  signed=False)
            self.USE_PIN_REF_L_AS_REF_R  =  self._USE_PIN_REF_L_AS_REF_R(self,  Access.RW,  0x01000000,  24,  signed=False)
            self.USE_PIN_REF_R_AS_REF_L  =  self._USE_PIN_REF_R_AS_REF_L(self,  Access.RW,  0x02000000,  25,  signed=False)
            self.DIFF_DELAY              =  self._DIFF_DELAY(            self,  Access.RW,  0xF0000000,  28,  signed=False)

        class _INV_PIN_ENC_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_ENC_A", parent, access, mask, shift, signed=signed)

        class _INV_PIN_ENC_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_ENC_B", parent, access, mask, shift, signed=signed)

        class _INV_PIN_ENC_N(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_ENC_N", parent, access, mask, shift, signed=signed)

        class _INV_PIN_HALL_U(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_HALL_U", parent, access, mask, shift, signed=signed)

        class _INV_PIN_HALL_V(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_HALL_V", parent, access, mask, shift, signed=signed)

        class _INV_PIN_HALL_W(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_HALL_W", parent, access, mask, shift, signed=signed)

        class _INV_PIN_REF_L(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_REF_L", parent, access, mask, shift, signed=signed)

        class _INV_PIN_REF_R(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_REF_R", parent, access, mask, shift, signed=signed)

        class _INV_PIN_SDI(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_SDI", parent, access, mask, shift, signed=signed)

        class _INV_PIN_SCK(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_SCK", parent, access, mask, shift, signed=signed)

        class _INV_PIN_PWM_IN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_PWM_IN", parent, access, mask, shift, signed=signed)

        class _INV_PIN_RXD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_PIN_RXD", parent, access, mask, shift, signed=signed)

        class _ENC_FLT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_FLT    =  Option(0,  parent,  "NO_FLT")
                    self.FLT_1M    =  Option(1,  parent,  "FLT_1M")
                    self.FLT_500K  =  Option(2,  parent,  "FLT_500K")
                    self.FLT_100K  =  Option(3,  parent,  "FLT_100K")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ENC_FLT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _HALL_FLT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_FLT    =  Option(0,  parent,  "NO_FLT")
                    self.FLT_1M    =  Option(1,  parent,  "FLT_1M")
                    self.FLT_500K  =  Option(2,  parent,  "FLT_500K")
                    self.FLT_100K  =  Option(3,  parent,  "FLT_100K")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_FLT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _REF_FLT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_FLT    =  Option(0,  parent,  "NO_FLT")
                    self.FLT_1M    =  Option(1,  parent,  "FLT_1M")
                    self.FLT_500K  =  Option(2,  parent,  "FLT_500K")
                    self.FLT_100K  =  Option(3,  parent,  "FLT_100K")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("REF_FLT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PWM_IN_FLT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_FLT    =  Option(0,  parent,  "NO_FLT")
                    self.FLT_1M    =  Option(1,  parent,  "FLT_1M")
                    self.FLT_500K  =  Option(2,  parent,  "FLT_500K")
                    self.FLT_100K  =  Option(3,  parent,  "FLT_100K")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_IN_FLT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ANA_DIV_VCCIO(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DIV_BY_4P5  =  Option(0,  parent,  "DIV_BY_4P5")
                    self.DIV_BY_3P0  =  Option(1,  parent,  "DIV_BY_3P0")
                    self.DIV_BY_2P2  =  Option(2,  parent,  "DIV_BY_2P2")
                    self.DIV_BY_1P0  =  Option(3,  parent,  "DIV_BY_1P0")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANA_DIV_VCCIO", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ANA_DIV_VCCIOF(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DIV_BY_4P5  =  Option(0,  parent,  "DIV_BY_4P5")
                    self.DIV_BY_3P0  =  Option(1,  parent,  "DIV_BY_3P0")
                    self.DIV_BY_2P2  =  Option(2,  parent,  "DIV_BY_2P2")
                    self.DIV_BY_1P0  =  Option(3,  parent,  "DIV_BY_1P0")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANA_DIV_VCCIOF", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _USE_PIN_REF_L_AS_REF_R(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USE_PIN_REF_L_AS_REF_R", parent, access, mask, shift, signed=signed)

        class _USE_PIN_REF_R_AS_REF_L(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USE_PIN_REF_R_AS_REF_L", parent, access, mask, shift, signed=signed)

        class _DIFF_DELAY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIFF_DELAY", parent, access, mask, shift, signed=signed)

    class _STATUS_FLAGS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS_FLAGS", parent, access, address, signed)
            self.PWRUP_FAIL_STATUS           =  self._PWRUP_FAIL_STATUS(         self,  Access.R,  0x00000001,  0,   signed=False)
            self.SPI_FAIL_STATUS             =  self._SPI_FAIL_STATUS(           self,  Access.R,  0x00000002,  1,   signed=False)
            self.UART_FAIL_STATUS            =  self._UART_FAIL_STATUS(          self,  Access.R,  0x00000004,  2,   signed=False)
            self.VCC_IOF_FAIL_STATUS         =  self._VCC_IOF_FAIL_STATUS(       self,  Access.R,  0x00000008,  3,   signed=False)
            self.CP_FAIL_STATUS              =  self._CP_FAIL_STATUS(            self,  Access.R,  0x00000010,  4,   signed=False)
            self.UV_VM_STATUS                =  self._UV_VM_STATUS(              self,  Access.R,  0x00000020,  5,   signed=False)
            self.POWER_FAIL_STATUS           =  self._POWER_FAIL_STATUS(         self,  Access.R,  0x00000040,  6,   signed=False)
            self.CLK_PLL_FAIL_STATUS         =  self._CLK_PLL_FAIL_STATUS(       self,  Access.R,  0x00000080,  7,   signed=False)
            self.EXT_RES_FAIL_STATUS         =  self._EXT_RES_FAIL_STATUS(       self,  Access.R,  0x00000100,  8,   signed=False)
            self.ADC_FAIL_STATUS             =  self._ADC_FAIL_STATUS(           self,  Access.R,  0x00000200,  9,   signed=False)
            self.TEMP_LIMIT_FAIL_STATUS      =  self._TEMP_LIMIT_FAIL_STATUS(    self,  Access.R,  0x00000400,  10,  signed=False)
            self.VEL_FAIL_STATUS             =  self._VEL_FAIL_STATUS(           self,  Access.R,  0x00000800,  11,  signed=False)
            self.SHRT_FAIL_STATUS            =  self._SHRT_FAIL_STATUS(          self,  Access.R,  0x00001000,  12,  signed=False)
            self.OT_FAIL_STATUS              =  self._OT_FAIL_STATUS(            self,  Access.R,  0x00002000,  13,  signed=False)
            self.DIFF_ENC_FAIL_STATUS        =  self._DIFF_ENC_FAIL_STATUS(      self,  Access.R,  0x00004000,  14,  signed=False)
            self.IO_CONTROLLER_STATUS        =  self._IO_CONTROLLER_STATUS(      self,  Access.R,  0x00008000,  15,  signed=False)
            self.RAMP_STALL_FAIL_STATUS      =  self._RAMP_STALL_FAIL_STATUS(    self,  Access.R,  0x00010000,  16,  signed=False)
            self.RAMP_TARGET_REACHED_STATUS  =  self._RAMP_TARGET_REACHED_STATUS(self,  Access.R,  0x00020000,  17,  signed=False)
            self.RAMP_V_REACHED_STATUS       =  self._RAMP_V_REACHED_STATUS(     self,  Access.R,  0x00040000,  18,  signed=False)
            self.RAMP_V_ZERO_STATUS          =  self._RAMP_V_ZERO_STATUS(        self,  Access.R,  0x00080000,  19,  signed=False)
            self.RAMP_REF_LR_STATUS          =  self._RAMP_REF_LR_STATUS(        self,  Access.R,  0x00100000,  20,  signed=False)
            self.RAMP_REF_H_STATUS           =  self._RAMP_REF_H_STATUS(         self,  Access.R,  0x00200000,  21,  signed=False)
            self.ABN_FAIL_STATUS             =  self._ABN_FAIL_STATUS(           self,  Access.R,  0x00400000,  22,  signed=False)
            self.HALL_FAIL_STATUS            =  self._HALL_FAIL_STATUS(          self,  Access.R,  0x00800000,  23,  signed=False)
            self.CURRENT_OVERLOAD_STATUS     =  self._CURRENT_OVERLOAD_STATUS(   self,  Access.R,  0x01000000,  24,  signed=False)
            self.I_CLIPPED_STATUS            =  self._I_CLIPPED_STATUS(          self,  Access.R,  0x02000000,  25,  signed=False)
            self.AIN_CLIPPED_STATUS          =  self._AIN_CLIPPED_STATUS(        self,  Access.R,  0x04000000,  26,  signed=False)
            self.VM_TEMP_CLIPPED_STATUS      =  self._VM_TEMP_CLIPPED_STATUS(    self,  Access.R,  0x08000000,  27,  signed=False)
            self.OV_VM_LIMIT_FAIL_STATUS     =  self._OV_VM_LIMIT_FAIL_STATUS(   self,  Access.R,  0x10000000,  28,  signed=False)
            self.OVERTEMP_WARN_STATUS        =  self._OVERTEMP_WARN_STATUS(      self,  Access.R,  0x20000000,  29,  signed=False)
            self.SYS_READY_STATE             =  self._SYS_READY_STATE(           self,  Access.R,  0x40000000,  30,  signed=False)
            self.GDRV_ON_STATE               =  self._GDRV_ON_STATE(             self,  Access.R,  0x80000000,  31,  signed=False)

        class _PWRUP_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWRUP_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _SPI_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SPI_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _UART_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UART_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _VCC_IOF_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VCC_IOF_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _CP_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CP_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _UV_VM_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UV_VM_STATUS", parent, access, mask, shift, signed=signed)

        class _POWER_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POWER_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _CLK_PLL_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_PLL_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _EXT_RES_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_RES_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _ADC_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _TEMP_LIMIT_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_LIMIT_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _VEL_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEL_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _SHRT_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _OT_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OT_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _DIFF_ENC_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIFF_ENC_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _IO_CONTROLLER_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IO_CONTROLLER_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_STALL_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_STALL_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_TARGET_REACHED_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_TARGET_REACHED_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_V_REACHED_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_V_REACHED_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_V_ZERO_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_V_ZERO_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_LR_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_LR_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_H_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_H_STATUS", parent, access, mask, shift, signed=signed)

        class _ABN_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _HALL_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _CURRENT_OVERLOAD_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_OVERLOAD_STATUS", parent, access, mask, shift, signed=signed)

        class _I_CLIPPED_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I_CLIPPED_STATUS", parent, access, mask, shift, signed=signed)

        class _AIN_CLIPPED_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_CLIPPED_STATUS", parent, access, mask, shift, signed=signed)

        class _VM_TEMP_CLIPPED_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_TEMP_CLIPPED_STATUS", parent, access, mask, shift, signed=signed)

        class _OV_VM_LIMIT_FAIL_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OV_VM_LIMIT_FAIL_STATUS", parent, access, mask, shift, signed=signed)

        class _OVERTEMP_WARN_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMP_WARN_STATUS", parent, access, mask, shift, signed=signed)

        class _SYS_READY_STATE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SYS_READY_STATE", parent, access, mask, shift, signed=signed)

        class _GDRV_ON_STATE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GDRV_ON_STATE", parent, access, mask, shift, signed=signed)

    class _EVENTS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("EVENTS", parent, access, address, signed)
            self.RST_EVENT                  =  self._RST_EVENT(                self,  Access.RWC,  0x00000001,  0,   signed=False)
            self.SPI_FAIL_EVENT             =  self._SPI_FAIL_EVENT(           self,  Access.RWC,  0x00000002,  1,   signed=False)
            self.UART_FAIL_EVENT            =  self._UART_FAIL_EVENT(          self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.VCCIOF_FAIL_EVENT          =  self._VCCIOF_FAIL_EVENT(        self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.CP_FAIL_EVENT              =  self._CP_FAIL_EVENT(            self,  Access.RWC,  0x00000010,  4,   signed=False)
            self.UV_VM_EVENT                =  self._UV_VM_EVENT(              self,  Access.RWC,  0x00000020,  5,   signed=False)
            self.POWER_FAIL_EVENT           =  self._POWER_FAIL_EVENT(         self,  Access.RWC,  0x00000040,  6,   signed=False)
            self.CLK_PLL_FAIL_EVENT         =  self._CLK_PLL_FAIL_EVENT(       self,  Access.RWC,  0x00000080,  7,   signed=False)
            self.EXT_RES_FAIL_EVENT         =  self._EXT_RES_FAIL_EVENT(       self,  Access.RWC,  0x00000100,  8,   signed=False)
            self.ADC_FAIL_EVENT             =  self._ADC_FAIL_EVENT(           self,  Access.RWC,  0x00000200,  9,   signed=False)
            self.TEMP_LIMIT_FAIL_EVENT      =  self._TEMP_LIMIT_FAIL_EVENT(    self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.VEL_FAIL_EVENT             =  self._VEL_FAIL_EVENT(           self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.SHRT_FAIL_EVENT            =  self._SHRT_FAIL_EVENT(          self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.OT_FAIL_EVENT              =  self._OT_FAIL_EVENT(            self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.DIFF_ENC_FAIL_EVENT        =  self._DIFF_ENC_FAIL_EVENT(      self,  Access.RWC,  0x00004000,  14,  signed=False)
            self.IO_CONTROLLER_EVENT        =  self._IO_CONTROLLER_EVENT(      self,  Access.RWC,  0x00008000,  15,  signed=False)
            self.RAMP_STALL_FAIL_EVENT      =  self._RAMP_STALL_FAIL_EVENT(    self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.RAMP_TARGET_REACHED_EVENT  =  self._RAMP_TARGET_REACHED_EVENT(self,  Access.RWC,  0x00020000,  17,  signed=False)
            self.RAMP_V_REACHED_EVENT       =  self._RAMP_V_REACHED_EVENT(     self,  Access.RWC,  0x00040000,  18,  signed=False)
            self.RAMP_V_ZERO_EVENT          =  self._RAMP_V_ZERO_EVENT(        self,  Access.RWC,  0x00080000,  19,  signed=False)
            self.RAMP_REF_LR_EVENT          =  self._RAMP_REF_LR_EVENT(        self,  Access.RWC,  0x00100000,  20,  signed=False)
            self.RAMP_REF_H_EVENT           =  self._RAMP_REF_H_EVENT(         self,  Access.RWC,  0x00200000,  21,  signed=False)
            self.ABN_FAIL_EVENT             =  self._ABN_FAIL_EVENT(           self,  Access.RWC,  0x00400000,  22,  signed=False)
            self.HALL_FAIL_EVENT            =  self._HALL_FAIL_EVENT(          self,  Access.RWC,  0x00800000,  23,  signed=False)
            self.CURRENT_OVERLOAD_EVENT     =  self._CURRENT_OVERLOAD_EVENT(   self,  Access.RWC,  0x01000000,  24,  signed=False)
            self.I_CLIPPED_EVENT            =  self._I_CLIPPED_EVENT(          self,  Access.RWC,  0x02000000,  25,  signed=False)
            self.AIN_CLIPPED_EVENT          =  self._AIN_CLIPPED_EVENT(        self,  Access.RWC,  0x04000000,  26,  signed=False)
            self.VM_TEMP_CLIPPED_EVENT      =  self._VM_TEMP_CLIPPED_EVENT(    self,  Access.RWC,  0x08000000,  27,  signed=False)
            self.OV_VM_LIMIT_FAIL_EVENT     =  self._OV_VM_LIMIT_FAIL_EVENT(   self,  Access.RWC,  0x10000000,  28,  signed=False)
            self.OVERTEMP_WARN_EVENT        =  self._OVERTEMP_WARN_EVENT(      self,  Access.RWC,  0x20000000,  29,  signed=False)
            self.SYS_READY_EVENT            =  self._SYS_READY_EVENT(          self,  Access.RWC,  0x40000000,  30,  signed=False)
            self.GDRV_ON_EVENT              =  self._GDRV_ON_EVENT(            self,  Access.RWC,  0x80000000,  31,  signed=False)

        class _RST_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RST_EVENT", parent, access, mask, shift, signed=signed)

        class _SPI_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SPI_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _UART_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UART_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _VCCIOF_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VCCIOF_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _CP_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CP_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _UV_VM_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UV_VM_EVENT", parent, access, mask, shift, signed=signed)

        class _POWER_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POWER_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _CLK_PLL_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_PLL_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _EXT_RES_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("EXT_RES_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _ADC_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _TEMP_LIMIT_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_LIMIT_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _VEL_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEL_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _SHRT_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _OT_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OT_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _DIFF_ENC_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DIFF_ENC_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _IO_CONTROLLER_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IO_CONTROLLER_EVENT", parent, access, mask, shift, signed=signed)

        class _RAMP_STALL_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_STALL_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _RAMP_TARGET_REACHED_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_TARGET_REACHED_EVENT", parent, access, mask, shift, signed=signed)

        class _RAMP_V_REACHED_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_V_REACHED_EVENT", parent, access, mask, shift, signed=signed)

        class _RAMP_V_ZERO_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_V_ZERO_EVENT", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_LR_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_LR_EVENT", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_H_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_H_EVENT", parent, access, mask, shift, signed=signed)

        class _ABN_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ABN_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _HALL_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _CURRENT_OVERLOAD_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_OVERLOAD_EVENT", parent, access, mask, shift, signed=signed)

        class _I_CLIPPED_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I_CLIPPED_EVENT", parent, access, mask, shift, signed=signed)

        class _AIN_CLIPPED_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_CLIPPED_EVENT", parent, access, mask, shift, signed=signed)

        class _VM_TEMP_CLIPPED_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_TEMP_CLIPPED_EVENT", parent, access, mask, shift, signed=signed)

        class _OV_VM_LIMIT_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OV_VM_LIMIT_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _OVERTEMP_WARN_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMP_WARN_EVENT", parent, access, mask, shift, signed=signed)

        class _SYS_READY_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SYS_READY_EVENT", parent, access, mask, shift, signed=signed)

        class _GDRV_ON_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("GDRV_ON_EVENT", parent, access, mask, shift, signed=signed)

    class _FAULTN_INT_MASK(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("FAULTN_INT_MASK", parent, access, address, signed)
            self.FAULTN_INT_MASK  =  self._FAULTN_INT_MASK(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _FAULTN_INT_MASK(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FAULTN_INT_MASK", parent, access, mask, shift, signed=signed)

    class _SPI_STATUS_MASK(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("SPI_STATUS_MASK", parent, access, address, signed)
            self.SPI_STATUS_MASK  =  self._SPI_STATUS_MASK(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _SPI_STATUS_MASK(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SPI_STATUS_MASK", parent, access, mask, shift, signed=signed)

class _CLK_CTRL(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("CLK_CTRL", channel, block, width)
        self.CONFIG  =  self._CONFIG(self,  Access.RW,  0x0040,  False)
        self.STATUS  =  self._STATUS(self,  Access.R,   0x0041,  False)

    class _CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CONFIG", parent, access, address, signed)
            self.COMMIT         =  self._COMMIT(       self,  Access.RW,  0x00000001,  0,  signed=False)
            self.PLL_SRC        =  self._PLL_SRC(      self,  Access.RW,  0x00000002,  1,  signed=False)
            self.PLL_EN         =  self._PLL_EN(       self,  Access.RW,  0x00000004,  2,  signed=False)
            self.ADC_CLK_EN     =  self._ADC_CLK_EN(   self,  Access.RW,  0x00000008,  3,  signed=False)
            self.PWM_CLK_EN     =  self._PWM_CLK_EN(   self,  Access.RW,  0x00000010,  4,  signed=False)
            self.CLK_FSM_EN     =  self._CLK_FSM_EN(   self,  Access.RW,  0x00000020,  5,  signed=False)
            self.CLOCK_DIVIDER  =  self._CLOCK_DIVIDER(self,  Access.RW,  0x00001F00,  8,  signed=False)

        class _COMMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMMIT", parent, access, mask, shift, signed=signed)

        class _PLL_SRC(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INT_CLK  =  Option(0,  parent,  "INT_CLK")
                    self.EXT_CLK  =  Option(1,  parent,  "EXT_CLK")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PLL_SRC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _PLL_EN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.INT_OSC  =  Option(0,  parent,  "INT_OSC")
                    self.PLL      =  Option(1,  parent,  "PLL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PLL_EN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC_CLK_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_CLK_EN", parent, access, mask, shift, signed=signed)

        class _PWM_CLK_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_CLK_EN", parent, access, mask, shift, signed=signed)

        class _CLK_FSM_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_FSM_EN", parent, access, mask, shift, signed=signed)

        class _CLOCK_DIVIDER(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLOCK_DIVIDER", parent, access, mask, shift, signed=signed)

    class _STATUS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS", parent, access, address, signed)
            self.CLK_1M0_OK       =  self._CLK_1M0_OK(     self,  Access.R,  0x00000001,  0,   signed=False)
            self.CLK_1M0_TIMEOUT  =  self._CLK_1M0_TIMEOUT(self,  Access.R,  0x00000002,  1,   signed=False)
            self.CLK_FSM_ERR      =  self._CLK_FSM_ERR(    self,  Access.R,  0x00000004,  2,   signed=False)
            self.CLK_STUCK        =  self._CLK_STUCK(      self,  Access.R,  0x00000008,  3,   signed=False)
            self.PLL_ERR          =  self._PLL_ERR(        self,  Access.R,  0x00000010,  4,   signed=False)
            self.PLL_LOCK_ON      =  self._PLL_LOCK_ON(    self,  Access.R,  0x00000020,  5,   signed=False)
            self.PLL_READY        =  self._PLL_READY(      self,  Access.R,  0x00000040,  6,   signed=False)
            self.CLK_FSM_ERR_RPT  =  self._CLK_FSM_ERR_RPT(self,  Access.R,  0x00FF0000,  16,  signed=False)
            self.CLK_FSM_FLG      =  self._CLK_FSM_FLG(    self,  Access.R,  0xFF000000,  24,  signed=False)

        class _CLK_1M0_OK(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_1M0_OK", parent, access, mask, shift, signed=signed)

        class _CLK_1M0_TIMEOUT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_1M0_TIMEOUT", parent, access, mask, shift, signed=signed)

        class _CLK_FSM_ERR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_FSM_ERR", parent, access, mask, shift, signed=signed)

        class _CLK_STUCK(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_STUCK", parent, access, mask, shift, signed=signed)

        class _PLL_ERR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PLL_ERR", parent, access, mask, shift, signed=signed)

        class _PLL_LOCK_ON(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PLL_LOCK_ON", parent, access, mask, shift, signed=signed)

        class _PLL_READY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PLL_READY", parent, access, mask, shift, signed=signed)

        class _CLK_FSM_ERR_RPT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_ERR_RPT   =  Option(0,    parent,  "NO_ERR_RPT")
                    self.NOT_USED     =  Option(1,    parent,  "NOT_USED")
                    self.DET_ERR_RPT  =  Option(2,    parent,  "DET_ERR_RPT")
                    self.STK_ERR_RPT  =  Option(4,    parent,  "STK_ERR_RPT")
                    self.PLL_ERR_RPT  =  Option(8,    parent,  "PLL_ERR_RPT")
                    self.UNK_ERR_RPT  =  Option(255,  parent,  "UNK_ERR_RPT")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_FSM_ERR_RPT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLK_FSM_FLG(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLK_FSM_FLG", parent, access, mask, shift, signed=signed)

class _ADC(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("ADC", channel, block, width)
        self.CONFIG           =  self._CONFIG(         self,  Access.RW,   0x0080,  False)
        self.ADC_VERSION      =  self._ADC_VERSION(    self,  Access.R,    0x0081,  False)
        self.I2_I1_RAW        =  self._I2_I1_RAW(      self,  Access.RW,   0x0082,  False)
        self.VM_I3_RAW        =  self._VM_I3_RAW(      self,  Access.RW,   0x0083,  False)
        self.TEMP_RAW         =  self._TEMP_RAW(       self,  Access.RW,   0x0084,  False)
        self.AIN_V_AIN_U_RAW  =  self._AIN_V_AIN_U_RAW(self,  Access.RW,   0x0085,  False)
        self.AIN_AIN_W_RAW    =  self._AIN_AIN_W_RAW(  self,  Access.RW,   0x0086,  False)
        self.STATUS           =  self._STATUS(         self,  Access.RWC,  0x008A,  False)
        self.I123             =  self._I123(           self,  Access.RW,   0x008C,  False)

    class _CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CONFIG", parent, access, address, signed)
            self.NRST_ADC_0      =  self._NRST_ADC_0(    self,  Access.RW,  0x00000004,  2,  signed=False)
            self.NRST_ADC_1      =  self._NRST_ADC_1(    self,  Access.RW,  0x00000008,  3,  signed=False)
            self.CSA_AZ_FLT_EXP  =  self._CSA_AZ_FLT_EXP(self,  Access.RW,  0x00000F00,  8,  signed=False)

        class _NRST_ADC_0(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RESET   =  Option(0,  parent,  "RESET")
                    self.ENABLE  =  Option(1,  parent,  "ENABLE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NRST_ADC_0", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _NRST_ADC_1(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RESET   =  Option(0,  parent,  "RESET")
                    self.ENABLE  =  Option(1,  parent,  "ENABLE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NRST_ADC_1", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CSA_AZ_FLT_EXP(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA_AZ_FLT_EXP", parent, access, mask, shift, signed=signed)

    class _ADC_VERSION(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ADC_VERSION", parent, access, address, signed)
            self.VERSION_NUMBER  =  self._VERSION_NUMBER(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

        class _VERSION_NUMBER(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VERSION_NUMBER", parent, access, mask, shift, signed=signed)

    class _I2_I1_RAW(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("I2_I1_RAW", parent, access, address, signed)
            self.I1  =  self._I1(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.I2  =  self._I2(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _I1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1", parent, access, mask, shift, signed=signed)

        class _I2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2", parent, access, mask, shift, signed=signed)

    class _VM_I3_RAW(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VM_I3_RAW", parent, access, address, signed)
            self.I3  =  self._I3(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.VM  =  self._VM(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _I3(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I3", parent, access, mask, shift, signed=signed)

        class _VM(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM", parent, access, mask, shift, signed=signed)

    class _TEMP_RAW(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TEMP_RAW", parent, access, address, signed)
            self.TEMP_EXT  =  self._TEMP_EXT(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.TEMP_INT  =  self._TEMP_INT(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _TEMP_EXT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_EXT", parent, access, mask, shift, signed=signed)

        class _TEMP_INT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_INT", parent, access, mask, shift, signed=signed)

    class _AIN_V_AIN_U_RAW(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("AIN_V_AIN_U_RAW", parent, access, address, signed)
            self.AIN_U  =  self._AIN_U(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.AIN_V  =  self._AIN_V(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _AIN_U(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_U", parent, access, mask, shift, signed=signed)

        class _AIN_V(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_V", parent, access, mask, shift, signed=signed)

    class _AIN_AIN_W_RAW(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("AIN_AIN_W_RAW", parent, access, address, signed)
            self.AIN_W  =  self._AIN_W(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.AIN    =  self._AIN(  self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _AIN_W(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_W", parent, access, mask, shift, signed=signed)

        class _AIN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN", parent, access, mask, shift, signed=signed)

    class _STATUS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS", parent, access, address, signed)
            self.ADC_0_READY            =  self._ADC_0_READY(          self,  Access.R,    0x00000001,  0,   signed=False)
            self.ADC_1_READY            =  self._ADC_1_READY(          self,  Access.R,    0x00000002,  1,   signed=False)
            self.I1_CLIPPED             =  self._I1_CLIPPED(           self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.I2_CLIPPED             =  self._I2_CLIPPED(           self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.I3_CLIPPED             =  self._I3_CLIPPED(           self,  Access.RWC,  0x00000010,  4,   signed=False)
            self.AIN_U_CLIPPED          =  self._AIN_U_CLIPPED(        self,  Access.RWC,  0x00000020,  5,   signed=False)
            self.AIN_V_CLIPPED          =  self._AIN_V_CLIPPED(        self,  Access.RWC,  0x00000040,  6,   signed=False)
            self.AIN_W_CLIPPED          =  self._AIN_W_CLIPPED(        self,  Access.RWC,  0x00000080,  7,   signed=False)
            self.AIN_CLIPPED            =  self._AIN_CLIPPED(          self,  Access.RWC,  0x00000100,  8,   signed=False)
            self.VM_CLIPPED             =  self._VM_CLIPPED(           self,  Access.RWC,  0x00000200,  9,   signed=False)
            self.VM_DONE                =  self._VM_DONE(              self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.TEMP_INT_CLIPPED       =  self._TEMP_INT_CLIPPED(     self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.TEMP_INT_DONE          =  self._TEMP_INT_DONE(        self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.TEMP_EXT_CLIPPED       =  self._TEMP_EXT_CLIPPED(     self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.TEMP_EXT_DONE          =  self._TEMP_EXT_DONE(        self,  Access.RWC,  0x00004000,  14,  signed=False)
            self.I1_DONE                =  self._I1_DONE(              self,  Access.RWC,  0x00008000,  15,  signed=False)
            self.I2_DONE                =  self._I2_DONE(              self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.I3_DONE                =  self._I3_DONE(              self,  Access.RWC,  0x00020000,  17,  signed=False)
            self.AIN_U_DONE             =  self._AIN_U_DONE(           self,  Access.RWC,  0x00040000,  18,  signed=False)
            self.AIN_V_DONE             =  self._AIN_V_DONE(           self,  Access.RWC,  0x00080000,  19,  signed=False)
            self.AIN_W_DONE             =  self._AIN_W_DONE(           self,  Access.RWC,  0x00100000,  20,  signed=False)
            self.AIN_DONE               =  self._AIN_DONE(             self,  Access.RWC,  0x00200000,  21,  signed=False)
            self.ADC_I_VALID            =  self._ADC_I_VALID(          self,  Access.R,    0x00400000,  22,  signed=False)
            self.ADC_EXT_VALID          =  self._ADC_EXT_VALID(        self,  Access.R,    0x00800000,  23,  signed=False)
            self.ADC_I_VALID_EXT        =  self._ADC_I_VALID_EXT(      self,  Access.RW,   0x01000000,  24,  signed=False)
            self.USE_ADC_I_VALID_EXT    =  self._USE_ADC_I_VALID_EXT(  self,  Access.RW,   0x02000000,  25,  signed=False)
            self.ADC_EXT_VALID_EXT      =  self._ADC_EXT_VALID_EXT(    self,  Access.RW,   0x04000000,  26,  signed=False)
            self.USE_ADC_EXT_VALID_EXT  =  self._USE_ADC_EXT_VALID_EXT(self,  Access.RW,   0x08000000,  27,  signed=False)
            self.NO_ACK_ADC             =  self._NO_ACK_ADC(           self,  Access.RWC,  0x40000000,  30,  signed=False)
            self.I123_FAIL              =  self._I123_FAIL(            self,  Access.R,    0x80000000,  31,  signed=True)

        class _ADC_0_READY(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ONGOING  =  Option(0,  parent,  "ONGOING")
                    self.READY    =  Option(1,  parent,  "READY")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_0_READY", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADC_1_READY(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ONGOING  =  Option(0,  parent,  "ONGOING")
                    self.READY    =  Option(1,  parent,  "READY")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_1_READY", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _I1_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1_CLIPPED", parent, access, mask, shift, signed=signed)

        class _I2_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2_CLIPPED", parent, access, mask, shift, signed=signed)

        class _I3_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I3_CLIPPED", parent, access, mask, shift, signed=signed)

        class _AIN_U_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_U_CLIPPED", parent, access, mask, shift, signed=signed)

        class _AIN_V_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_V_CLIPPED", parent, access, mask, shift, signed=signed)

        class _AIN_W_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_W_CLIPPED", parent, access, mask, shift, signed=signed)

        class _AIN_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_CLIPPED", parent, access, mask, shift, signed=signed)

        class _VM_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_CLIPPED", parent, access, mask, shift, signed=signed)

        class _VM_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VM_DONE", parent, access, mask, shift, signed=signed)

        class _TEMP_INT_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_INT_CLIPPED", parent, access, mask, shift, signed=signed)

        class _TEMP_INT_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_INT_DONE", parent, access, mask, shift, signed=signed)

        class _TEMP_EXT_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_EXT_CLIPPED", parent, access, mask, shift, signed=signed)

        class _TEMP_EXT_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_EXT_DONE", parent, access, mask, shift, signed=signed)

        class _I1_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I1_DONE", parent, access, mask, shift, signed=signed)

        class _I2_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I2_DONE", parent, access, mask, shift, signed=signed)

        class _I3_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I3_DONE", parent, access, mask, shift, signed=signed)

        class _AIN_U_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_U_DONE", parent, access, mask, shift, signed=signed)

        class _AIN_V_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_V_DONE", parent, access, mask, shift, signed=signed)

        class _AIN_W_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_W_DONE", parent, access, mask, shift, signed=signed)

        class _AIN_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AIN_DONE", parent, access, mask, shift, signed=signed)

        class _ADC_I_VALID(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_VALID", parent, access, mask, shift, signed=signed)

        class _ADC_EXT_VALID(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_EXT_VALID", parent, access, mask, shift, signed=signed)

        class _ADC_I_VALID_EXT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_I_VALID_EXT", parent, access, mask, shift, signed=signed)

        class _USE_ADC_I_VALID_EXT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USE_ADC_I_VALID_EXT", parent, access, mask, shift, signed=signed)

        class _ADC_EXT_VALID_EXT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_EXT_VALID_EXT", parent, access, mask, shift, signed=signed)

        class _USE_ADC_EXT_VALID_EXT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USE_ADC_EXT_VALID_EXT", parent, access, mask, shift, signed=signed)

        class _NO_ACK_ADC(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NO_ACK_ADC", parent, access, mask, shift, signed=signed)

        class _I123_FAIL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I123_FAIL", parent, access, mask, shift, signed=signed)

    class _I123(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("I123", parent, access, address, signed)
            self.I123        =  self._I123(      self,  Access.R,   0x0000FFFF,  0,   signed=True)
            self.I123_LIMIT  =  self._I123_LIMIT(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _I123(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I123", parent, access, mask, shift, signed=signed)

        class _I123_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I123_LIMIT", parent, access, mask, shift, signed=signed)

class _MCC_ADC(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("MCC_ADC", channel, block, width)
        self.I_GEN_CONFIG           =  self._I_GEN_CONFIG(         self,  Access.RW,   0x00C0,  False)
        self.IW_IU                  =  self._IW_IU(                self,  Access.R,    0x00C1,  False)
        self.IV                     =  self._IV(                   self,  Access.R,    0x00C2,  True)
        self.CSA_GAIN               =  self._CSA_GAIN(             self,  Access.RW,   0x00C3,  False)
        self.EVENTS                 =  self._EVENTS(               self,  Access.RWC,  0x00C4,  False)
        self.DYN_GAIN_LIMITS_4X_3X  =  self._DYN_GAIN_LIMITS_4X_3X(self,  Access.RW,   0x00C5,  False)
        self.DYN_GAIN_LIMIT_2X      =  self._DYN_GAIN_LIMIT_2X(    self,  Access.RW,   0x00C6,  False)
        self.TEMP_LIMITS            =  self._TEMP_LIMITS(          self,  Access.RW,   0x00C7,  False)
        self.CURRENT_OVERLOAD       =  self._CURRENT_OVERLOAD(     self,  Access.RW,   0x00C8,  False)

    class _I_GEN_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("I_GEN_CONFIG", parent, access, address, signed)
            self.MEAS_MODE  =  self._MEAS_MODE(self,  Access.RW,  0x00000001,  0,   signed=False)
            self.STATUS     =  self._STATUS(   self,  Access.R,   0x00003000,  12,  signed=False)

        class _MEAS_MODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.AUTOMATIC_SWITCH  =  Option(0,  parent,  "AUTOMATIC_SWITCH")
                    self.NO_SWITCH         =  Option(1,  parent,  "NO_SWITCH")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MEAS_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STATUS", parent, access, mask, shift, signed=signed)

    class _IW_IU(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("IW_IU", parent, access, address, signed)
            self.IU  =  self._IU(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.IW  =  self._IW(self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _IU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IU", parent, access, mask, shift, signed=signed)

        class _IW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IW", parent, access, mask, shift, signed=signed)

    class _IV(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("IV", parent, access, address, signed)
            self.IV  =  self._IV(self,  Access.R,  0x0000FFFF,  0,  signed=True)

        class _IV(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IV", parent, access, mask, shift, signed=signed)

    class _CSA_GAIN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CSA_GAIN", parent, access, address, signed)
            self.CSA_GAIN        =  self._CSA_GAIN(      self,  Access.RW,  0x00000003,  0,  signed=False)
            self.DYN_GAIN_ACT    =  self._DYN_GAIN_ACT(  self,  Access.R,   0x0000000C,  2,  signed=False)
            self.DYN_GAIN_2X_EN  =  self._DYN_GAIN_2X_EN(self,  Access.RW,  0x00000010,  4,  signed=False)
            self.DYN_GAIN_3X_EN  =  self._DYN_GAIN_3X_EN(self,  Access.RW,  0x00000020,  5,  signed=False)
            self.DYN_GAIN_4X_EN  =  self._DYN_GAIN_4X_EN(self,  Access.RW,  0x00000040,  6,  signed=False)
            self.DYN_GAIN_HYST   =  self._DYN_GAIN_HYST( self,  Access.RW,  0x0000FF00,  8,  signed=False)

        class _CSA_GAIN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.X1  =  Option(0,  parent,  "X1")
                    self.X2  =  Option(1,  parent,  "X2")
                    self.X3  =  Option(2,  parent,  "X3")
                    self.X4  =  Option(3,  parent,  "X4")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CSA_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DYN_GAIN_ACT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DYN_GAIN_ACT", parent, access, mask, shift, signed=signed)

        class _DYN_GAIN_2X_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DYN_GAIN_2X_EN", parent, access, mask, shift, signed=signed)

        class _DYN_GAIN_3X_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DYN_GAIN_3X_EN", parent, access, mask, shift, signed=signed)

        class _DYN_GAIN_4X_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DYN_GAIN_4X_EN", parent, access, mask, shift, signed=signed)

        class _DYN_GAIN_HYST(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DYN_GAIN_HYST", parent, access, mask, shift, signed=signed)

    class _EVENTS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("EVENTS", parent, access, address, signed)
            self.ADC_CLIPPED              =  self._ADC_CLIPPED(            self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.MEAS_DONE                =  self._MEAS_DONE(              self,  Access.RWC,  0x00000002,  1,  signed=False)
            self.TEMP_EXT_LIMIT_EXCEEDED  =  self._TEMP_EXT_LIMIT_EXCEEDED(self,  Access.R,    0x00000010,  4,  signed=False)
            self.TEMP_INT_LIMIT_EXCEEDED  =  self._TEMP_INT_LIMIT_EXCEEDED(self,  Access.R,    0x00000020,  5,  signed=False)
            self.CURRENT_OVERLOAD_STATUS  =  self._CURRENT_OVERLOAD_STATUS(self,  Access.R,    0x00000040,  6,  signed=False)

        class _ADC_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_CLIPPED", parent, access, mask, shift, signed=signed)

        class _MEAS_DONE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MEAS_DONE", parent, access, mask, shift, signed=signed)

        class _TEMP_EXT_LIMIT_EXCEEDED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_EXT_LIMIT_EXCEEDED", parent, access, mask, shift, signed=signed)

        class _TEMP_INT_LIMIT_EXCEEDED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_INT_LIMIT_EXCEEDED", parent, access, mask, shift, signed=signed)

        class _CURRENT_OVERLOAD_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_OVERLOAD_STATUS", parent, access, mask, shift, signed=signed)

    class _DYN_GAIN_LIMITS_4X_3X(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("DYN_GAIN_LIMITS_4X_3X", parent, access, address, signed)
            self.DYN_GAIN_LIMIT_3X  =  self._DYN_GAIN_LIMIT_3X(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.DYN_GAIN_LIMIT_4X  =  self._DYN_GAIN_LIMIT_4X(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _DYN_GAIN_LIMIT_3X(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DYN_GAIN_LIMIT_3X", parent, access, mask, shift, signed=signed)

        class _DYN_GAIN_LIMIT_4X(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DYN_GAIN_LIMIT_4X", parent, access, mask, shift, signed=signed)

    class _DYN_GAIN_LIMIT_2X(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("DYN_GAIN_LIMIT_2X", parent, access, address, signed)
            self.DYN_GAIN_LIMIT_2X  =  self._DYN_GAIN_LIMIT_2X(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _DYN_GAIN_LIMIT_2X(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DYN_GAIN_LIMIT_2X", parent, access, mask, shift, signed=signed)

    class _TEMP_LIMITS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TEMP_LIMITS", parent, access, address, signed)
            self.TEMP_EXT_LIMIT  =  self._TEMP_EXT_LIMIT(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.TEMP_INT_LIMIT  =  self._TEMP_INT_LIMIT(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _TEMP_EXT_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_EXT_LIMIT", parent, access, mask, shift, signed=signed)

        class _TEMP_INT_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TEMP_INT_LIMIT", parent, access, mask, shift, signed=signed)

    class _CURRENT_OVERLOAD(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CURRENT_OVERLOAD", parent, access, address, signed)
            self.CURRENT_OVERLOAD  =  self._CURRENT_OVERLOAD(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _CURRENT_OVERLOAD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_OVERLOAD", parent, access, mask, shift, signed=signed)

class _MCC_CONFIG(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("MCC_CONFIG", channel, block, width)
        self.MOTOR_MOTION                =  self._MOTOR_MOTION(              self,  Access.RW,   0x0100,  False)
        self.GDRV                        =  self._GDRV(                      self,  Access.RW,   0x0101,  False)
        self.PWM                         =  self._PWM(                       self,  Access.RW,   0x0102,  False)
        self.PWM_PERIOD                  =  self._PWM_PERIOD(                self,  Access.RW,   0x0103,  False)
        self.BRAKE_CHOPPER_LIMITS        =  self._BRAKE_CHOPPER_LIMITS(      self,  Access.RW,   0x0104,  False)
        self.MCC_STATUS                  =  self._MCC_STATUS(                self,  Access.RWC,  0x0105,  False)
        self.TORQUE_FF_ACC_CONFIG        =  self._TORQUE_FF_ACC_CONFIG(      self,  Access.RW,   0x0106,  False)
        self.TORQUE_FF_VISC_FRIC_CONFIG  =  self._TORQUE_FF_VISC_FRIC_CONFIG(self,  Access.RW,   0x0107,  False)
        self.TORQUE_FF_COULOMB_FRIC      =  self._TORQUE_FF_COULOMB_FRIC(    self,  Access.RW,   0x0108,  True)
        self.TORQUE_FEEDFORWARD          =  self._TORQUE_FEEDFORWARD(        self,  Access.R,    0x0109,  True)

    class _MOTOR_MOTION(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MOTOR_MOTION", parent, access, address, signed)
            self.N_POLE_PAIRS                   =  self._N_POLE_PAIRS(                 self,  Access.RW,  0x0000007F,  0,   signed=False)
            self.MOTOR_TYPE                     =  self._MOTOR_TYPE(                   self,  Access.RW,  0x00000180,  7,   signed=False)
            self.MOTION_MODE                    =  self._MOTION_MODE(                  self,  Access.RW,  0x00001E00,  9,   signed=False)
            self.RAMP_MODE                      =  self._RAMP_MODE(                    self,  Access.RW,  0x00002000,  13,  signed=False)
            self.RAMP_EN                        =  self._RAMP_EN(                      self,  Access.RW,  0x00004000,  14,  signed=False)
            self.RAMP_USE_PHI_E                 =  self._RAMP_USE_PHI_E(               self,  Access.RW,  0x00008000,  15,  signed=False)
            self.TORQUE_FF_ACC_EN               =  self._TORQUE_FF_ACC_EN(             self,  Access.RW,  0x00010000,  16,  signed=False)
            self.TORQUE_FF_COULOMB_FRICTION_EN  =  self._TORQUE_FF_COULOMB_FRICTION_EN(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.TORQUE_FF_VISC_FRIC_EN         =  self._TORQUE_FF_VISC_FRIC_EN(       self,  Access.RW,  0x00040000,  18,  signed=False)
            self.VELOCITY_FF_EN                 =  self._VELOCITY_FF_EN(               self,  Access.RW,  0x00080000,  19,  signed=False)

        class _N_POLE_PAIRS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_POLE_PAIRS", parent, access, mask, shift, signed=signed)

        class _MOTOR_TYPE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NONE  =  Option(0,  parent,  "NONE")
                    self.DC    =  Option(1,  parent,  "DC")
                    self.BLDC  =  Option(3,  parent,  "BLDC")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MOTOR_TYPE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _MOTION_MODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.PWM_OFF        =  Option(0,   parent,  "PWM_OFF")
                    self.PWM_ON         =  Option(1,   parent,  "PWM_ON")
                    self.TORQUE         =  Option(2,   parent,  "TORQUE")
                    self.VELOCITY       =  Option(3,   parent,  "VELOCITY")
                    self.POSITION       =  Option(4,   parent,  "POSITION")
                    self.PRBS_UD        =  Option(5,   parent,  "PRBS_UD")
                    self.PRBS_FLUX      =  Option(6,   parent,  "PRBS_FLUX")
                    self.PRBS_TORQUE    =  Option(7,   parent,  "PRBS_TORQUE")
                    self.PRBS_VELOCITY  =  Option(8,   parent,  "PRBS_VELOCITY")
                    self.PRBS_POSITION  =  Option(9,   parent,  "PRBS_POSITION")
                    self.PWM_EXT        =  Option(10,  parent,  "PWM_EXT")
                    self.VOLTAGE_EXT    =  Option(11,  parent,  "VOLTAGE_EXT")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MOTION_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _RAMP_MODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RAMP_POSITION  =  Option(0,  parent,  "RAMP_POSITION")
                    self.RAMP_VELOCITY  =  Option(1,  parent,  "RAMP_VELOCITY")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _RAMP_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_EN", parent, access, mask, shift, signed=signed)

        class _RAMP_USE_PHI_E(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_USE_PHI_E", parent, access, mask, shift, signed=signed)

        class _TORQUE_FF_ACC_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TORQUE_FF_ACC_EN", parent, access, mask, shift, signed=signed)

        class _TORQUE_FF_COULOMB_FRICTION_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TORQUE_FF_COULOMB_FRICTION_EN", parent, access, mask, shift, signed=signed)

        class _TORQUE_FF_VISC_FRIC_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TORQUE_FF_VISC_FRIC_EN", parent, access, mask, shift, signed=signed)

        class _VELOCITY_FF_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_FF_EN", parent, access, mask, shift, signed=signed)

    class _GDRV(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("GDRV", parent, access, address, signed)
            self.SLEW_RATE           =  self._SLEW_RATE(         self,  Access.RW,  0x00000003,  0,   signed=False)
            self.LS_RES_ON           =  self._LS_RES_ON(         self,  Access.RW,  0x00000030,  4,   signed=False)
            self.OCP_DETECTION_MODE  =  self._OCP_DETECTION_MODE(self,  Access.RW,  0x00000200,  9,   signed=False)
            self.OCP_DEGLITCH        =  self._OCP_DEGLITCH(      self,  Access.RW,  0x00000C00,  10,  signed=False)
            self.OCP_AUTORETRY       =  self._OCP_AUTORETRY(     self,  Access.RW,  0x00003000,  12,  signed=False)
            self.DRV_EN_BIT          =  self._DRV_EN_BIT(        self,  Access.RW,  0x00010000,  16,  signed=False)
            self.OVERTEMP_LATCH      =  self._OVERTEMP_LATCH(    self,  Access.RW,  0x00100000,  20,  signed=False)
            self.USE_INTERNAL_R_REF  =  self._USE_INTERNAL_R_REF(self,  Access.RW,  0x01000000,  24,  signed=False)
            self.LP_MODE_EN          =  self._LP_MODE_EN(        self,  Access.RW,  0x10000000,  28,  signed=False)
            self.CHARGE_PUMP_EN      =  self._CHARGE_PUMP_EN(    self,  Access.RW,  0x80000000,  31,  signed=False)

        class _SLEW_RATE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.SR_100_V_PER_US  =  Option(0,  parent,  "SR_100_V_PER_US")
                    self.SR_200_V_PER_US  =  Option(1,  parent,  "SR_200_V_PER_US")
                    self.SR_400_V_PER_US  =  Option(2,  parent,  "SR_400_V_PER_US")
                    self.SR_800_V_PER_US  =  Option(3,  parent,  "SR_800_V_PER_US")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SLEW_RATE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LS_RES_ON(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RES_200_MOHM  =  Option(0,  parent,  "RES_200_MOHM")
                    self.RES_112_MOHM  =  Option(1,  parent,  "RES_112_MOHM")
                    self.RES_78_MOHM   =  Option(2,  parent,  "RES_78_MOHM")
                    self.RES_55_MOHM   =  Option(3,  parent,  "RES_55_MOHM")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LS_RES_ON", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OCP_DETECTION_MODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOAD_CURRENT    =  Option(0,  parent,  "LOAD_CURRENT")
                    self.OUTPUT_VOLTAGE  =  Option(1,  parent,  "OUTPUT_VOLTAGE")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OCP_DETECTION_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OCP_DEGLITCH(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DEGLITCH_300_NS   =  Option(0,  parent,  "DEGLITCH_300_NS")
                    self.DEGLITCH_600_NS   =  Option(1,  parent,  "DEGLITCH_600_NS")
                    self.DEGLITCH_1200_NS  =  Option(2,  parent,  "DEGLITCH_1200_NS")
                    self.DEGLITCH_2400_NS  =  Option(3,  parent,  "DEGLITCH_2400_NS")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OCP_DEGLITCH", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _OCP_AUTORETRY(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RETRY_AFTER_1MS   =  Option(0,  parent,  "RETRY_AFTER_1MS")
                    self.RETRY_AFTER_5MS   =  Option(1,  parent,  "RETRY_AFTER_5MS")
                    self.RETRY_AFTER_50MS  =  Option(2,  parent,  "RETRY_AFTER_50MS")
                    self.NO_RETRY          =  Option(3,  parent,  "NO_RETRY")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OCP_AUTORETRY", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _DRV_EN_BIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("DRV_EN_BIT", parent, access, mask, shift, signed=signed)

        class _OVERTEMP_LATCH(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.AUTO_RESTART  =  Option(0,  parent,  "AUTO_RESTART")
                    self.CLEAR         =  Option(1,  parent,  "CLEAR")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMP_LATCH", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _USE_INTERNAL_R_REF(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USE_INTERNAL_R_REF", parent, access, mask, shift, signed=signed)

        class _LP_MODE_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LP_MODE_EN", parent, access, mask, shift, signed=signed)

        class _CHARGE_PUMP_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHARGE_PUMP_EN", parent, access, mask, shift, signed=signed)

    class _PWM(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PWM", parent, access, address, signed)
            self.CHOP                =  self._CHOP(              self,  Access.RW,  0x00000007,  0,   signed=False)
            self.SV_MODE             =  self._SV_MODE(           self,  Access.RW,  0x00000030,  4,   signed=False)
            self.FLAT_BOTTOM_OFFSET  =  self._FLAT_BOTTOM_OFFSET(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _CHOP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OFF_FREE     =  Option(0,  parent,  "OFF_FREE")
                    self.OFF_LSON     =  Option(1,  parent,  "OFF_LSON")
                    self.OFF_HSON     =  Option(2,  parent,  "OFF_HSON")
                    self.OFF_FREE2    =  Option(3,  parent,  "OFF_FREE2")
                    self.OFF_FREE3    =  Option(4,  parent,  "OFF_FREE3")
                    self.LSPWM_HSOFF  =  Option(5,  parent,  "LSPWM_HSOFF")
                    self.HSPWM_LSOFF  =  Option(6,  parent,  "HSPWM_LSOFF")
                    self.CENTERED     =  Option(7,  parent,  "CENTERED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHOP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SV_MODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.DISABLED       =  Option(0,  parent,  "DISABLED")
                    self.HARMONIC       =  Option(1,  parent,  "HARMONIC")
                    self.BOTTOM         =  Option(2,  parent,  "BOTTOM")
                    self.BOTTOM_OFFSET  =  Option(3,  parent,  "BOTTOM_OFFSET")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SV_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _FLAT_BOTTOM_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FLAT_BOTTOM_OFFSET", parent, access, mask, shift, signed=signed)

    class _PWM_PERIOD(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_PERIOD", parent, access, address, signed)
            self.MAX_COUNT          =  self._MAX_COUNT(        self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.AUTO_KIRCHOFF_LIM  =  self._AUTO_KIRCHOFF_LIM(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _MAX_COUNT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MAX_COUNT", parent, access, mask, shift, signed=signed)

        class _AUTO_KIRCHOFF_LIM(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AUTO_KIRCHOFF_LIM", parent, access, mask, shift, signed=signed)

    class _BRAKE_CHOPPER_LIMITS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("BRAKE_CHOPPER_LIMITS", parent, access, address, signed)
            self.LOWER_SWITCH_LIM  =  self._LOWER_SWITCH_LIM(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.UPPER_SWITCH_LIM  =  self._UPPER_SWITCH_LIM(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _LOWER_SWITCH_LIM(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LOWER_SWITCH_LIM", parent, access, mask, shift, signed=signed)

        class _UPPER_SWITCH_LIM(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UPPER_SWITCH_LIM", parent, access, mask, shift, signed=signed)

    class _MCC_STATUS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MCC_STATUS", parent, access, address, signed)
            self.SHRT2G_CH1_STATUS    =  self._SHRT2G_CH1_STATUS(  self,  Access.R,    0x00000001,  0,   signed=False)
            self.SHRT2G_CH2_STATUS    =  self._SHRT2G_CH2_STATUS(  self,  Access.R,    0x00000002,  1,   signed=False)
            self.SHRT2G_CH3_STATUS    =  self._SHRT2G_CH3_STATUS(  self,  Access.R,    0x00000004,  2,   signed=False)
            self.SHRT2V_CH1_STATUS    =  self._SHRT2V_CH1_STATUS(  self,  Access.R,    0x00000008,  3,   signed=False)
            self.SHRT2V_CH2_STATUS    =  self._SHRT2V_CH2_STATUS(  self,  Access.R,    0x00000010,  4,   signed=False)
            self.SHRT2V_CH3_STATUS    =  self._SHRT2V_CH3_STATUS(  self,  Access.R,    0x00000020,  5,   signed=False)
            self.OVERTEMP_CH1_STATUS  =  self._OVERTEMP_CH1_STATUS(self,  Access.R,    0x00000040,  6,   signed=False)
            self.OVERTEMP_CH2_STATUS  =  self._OVERTEMP_CH2_STATUS(self,  Access.R,    0x00000080,  7,   signed=False)
            self.OVERTEMP_CH3_STATUS  =  self._OVERTEMP_CH3_STATUS(self,  Access.R,    0x00000100,  8,   signed=False)
            self.SHRT2G_CH1_EVENT     =  self._SHRT2G_CH1_EVENT(   self,  Access.RWC,  0x00010000,  16,  signed=False)
            self.SHRT2G_CH2_EVENT     =  self._SHRT2G_CH2_EVENT(   self,  Access.RWC,  0x00020000,  17,  signed=False)
            self.SHRT2G_CH3_EVENT     =  self._SHRT2G_CH3_EVENT(   self,  Access.RWC,  0x00040000,  18,  signed=False)
            self.SHRT2V_CH1_EVENT     =  self._SHRT2V_CH1_EVENT(   self,  Access.RWC,  0x00080000,  19,  signed=False)
            self.SHRT2V_CH2_EVENT     =  self._SHRT2V_CH2_EVENT(   self,  Access.RWC,  0x00100000,  20,  signed=False)
            self.SHRT2V_CH3_EVENT     =  self._SHRT2V_CH3_EVENT(   self,  Access.RWC,  0x00200000,  21,  signed=False)
            self.OVERTEMP_CH1_EVENT   =  self._OVERTEMP_CH1_EVENT( self,  Access.RWC,  0x00400000,  22,  signed=False)
            self.OVERTEMP_CH2_EVENT   =  self._OVERTEMP_CH2_EVENT( self,  Access.RWC,  0x00800000,  23,  signed=False)
            self.OVERTEMP_CH3_EVENT   =  self._OVERTEMP_CH3_EVENT( self,  Access.RWC,  0x01000000,  24,  signed=False)

        class _SHRT2G_CH1_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2G_CH1_STATUS", parent, access, mask, shift, signed=signed)

        class _SHRT2G_CH2_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2G_CH2_STATUS", parent, access, mask, shift, signed=signed)

        class _SHRT2G_CH3_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2G_CH3_STATUS", parent, access, mask, shift, signed=signed)

        class _SHRT2V_CH1_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2V_CH1_STATUS", parent, access, mask, shift, signed=signed)

        class _SHRT2V_CH2_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2V_CH2_STATUS", parent, access, mask, shift, signed=signed)

        class _SHRT2V_CH3_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2V_CH3_STATUS", parent, access, mask, shift, signed=signed)

        class _OVERTEMP_CH1_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMP_CH1_STATUS", parent, access, mask, shift, signed=signed)

        class _OVERTEMP_CH2_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMP_CH2_STATUS", parent, access, mask, shift, signed=signed)

        class _OVERTEMP_CH3_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMP_CH3_STATUS", parent, access, mask, shift, signed=signed)

        class _SHRT2G_CH1_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2G_CH1_EVENT", parent, access, mask, shift, signed=signed)

        class _SHRT2G_CH2_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2G_CH2_EVENT", parent, access, mask, shift, signed=signed)

        class _SHRT2G_CH3_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2G_CH3_EVENT", parent, access, mask, shift, signed=signed)

        class _SHRT2V_CH1_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2V_CH1_EVENT", parent, access, mask, shift, signed=signed)

        class _SHRT2V_CH2_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2V_CH2_EVENT", parent, access, mask, shift, signed=signed)

        class _SHRT2V_CH3_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SHRT2V_CH3_EVENT", parent, access, mask, shift, signed=signed)

        class _OVERTEMP_CH1_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMP_CH1_EVENT", parent, access, mask, shift, signed=signed)

        class _OVERTEMP_CH2_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMP_CH2_EVENT", parent, access, mask, shift, signed=signed)

        class _OVERTEMP_CH3_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERTEMP_CH3_EVENT", parent, access, mask, shift, signed=signed)

    class _TORQUE_FF_ACC_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TORQUE_FF_ACC_CONFIG", parent, access, address, signed)
            self.RAMP_ACC_GAIN   =  self._RAMP_ACC_GAIN( self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.RAMP_ACC_SHIFT  =  self._RAMP_ACC_SHIFT(self,  Access.RW,  0x00070000,  16,  signed=False)

        class _RAMP_ACC_GAIN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_ACC_GAIN", parent, access, mask, shift, signed=signed)

        class _RAMP_ACC_SHIFT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_ACC_SHIFT     =  Option(0,  parent,  "NO_ACC_SHIFT")
                    self.ACC_SHIFT_BY_4   =  Option(1,  parent,  "ACC_SHIFT_BY_4")
                    self.ACC_SHIFT_BY_8   =  Option(2,  parent,  "ACC_SHIFT_BY_8")
                    self.ACC_SHIFT_BY_12  =  Option(3,  parent,  "ACC_SHIFT_BY_12")
                    self.ACC_SHIFT_BY_16  =  Option(4,  parent,  "ACC_SHIFT_BY_16")
                    self.ACC_SHIFT_BY_20  =  Option(5,  parent,  "ACC_SHIFT_BY_20")
                    self.ACC_SHIFT_BY_24  =  Option(6,  parent,  "ACC_SHIFT_BY_24")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_ACC_SHIFT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _TORQUE_FF_VISC_FRIC_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TORQUE_FF_VISC_FRIC_CONFIG", parent, access, address, signed)
            self.RAMP_VEL_GAIN   =  self._RAMP_VEL_GAIN( self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.RAMP_VEL_SHIFT  =  self._RAMP_VEL_SHIFT(self,  Access.RW,  0x00070000,  16,  signed=False)

        class _RAMP_VEL_GAIN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_VEL_GAIN", parent, access, mask, shift, signed=signed)

        class _RAMP_VEL_SHIFT(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NO_VEL_SHIFT     =  Option(0,  parent,  "NO_VEL_SHIFT")
                    self.VEL_SHIFT_BY_4   =  Option(1,  parent,  "VEL_SHIFT_BY_4")
                    self.VEL_SHIFT_BY_8   =  Option(2,  parent,  "VEL_SHIFT_BY_8")
                    self.VEL_SHIFT_BY_12  =  Option(3,  parent,  "VEL_SHIFT_BY_12")
                    self.VEL_SHIFT_BY_16  =  Option(4,  parent,  "VEL_SHIFT_BY_16")
                    self.VEL_SHIFT_BY_20  =  Option(5,  parent,  "VEL_SHIFT_BY_20")
                    self.VEL_SHIFT_BY_24  =  Option(6,  parent,  "VEL_SHIFT_BY_24")
                    self.VEL_SHIFT_BY_28  =  Option(7,  parent,  "VEL_SHIFT_BY_28")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_VEL_SHIFT", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _TORQUE_FF_COULOMB_FRIC(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TORQUE_FF_COULOMB_FRIC", parent, access, address, signed)
            self.TORQUE_FF_COULOMB_FRIC  =  self._TORQUE_FF_COULOMB_FRIC(self,  Access.RW,  0x0000FFFF,  0,  signed=True)

        class _TORQUE_FF_COULOMB_FRIC(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TORQUE_FF_COULOMB_FRIC", parent, access, mask, shift, signed=signed)

    class _TORQUE_FEEDFORWARD(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TORQUE_FEEDFORWARD", parent, access, address, signed)
            self.TORQUE_FEEDFORWARD  =  self._TORQUE_FEEDFORWARD(self,  Access.R,  0x0000FFFF,  0,  signed=True)

        class _TORQUE_FEEDFORWARD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TORQUE_FEEDFORWARD", parent, access, mask, shift, signed=signed)

class _FOC(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("FOC", channel, block, width)
        self.PID_CONFIG                        =  self._PID_CONFIG(                      self,  Access.RW,  0x0140,  False)
        self.PID_U_S_MAX                       =  self._PID_U_S_MAX(                     self,  Access.RW,  0x0141,  False)
        self.PID_FLUX_COEFF                    =  self._PID_FLUX_COEFF(                  self,  Access.RW,  0x0142,  False)
        self.PID_TORQUE_COEFF                  =  self._PID_TORQUE_COEFF(                self,  Access.RW,  0x0143,  False)
        self.PID_FIELDWEAK_COEFF               =  self._PID_FIELDWEAK_COEFF(             self,  Access.RW,  0x0144,  False)
        self.PID_VELOCITY_COEFF                =  self._PID_VELOCITY_COEFF(              self,  Access.RW,  0x0145,  False)
        self.PID_POSITION_COEFF                =  self._PID_POSITION_COEFF(              self,  Access.RW,  0x0146,  False)
        self.PID_POSITION_TOLERANCE            =  self._PID_POSITION_TOLERANCE(          self,  Access.RW,  0x0147,  False)
        self.PID_POSITION_TOLERANCE_DELAY      =  self._PID_POSITION_TOLERANCE_DELAY(    self,  Access.RW,  0x0148,  False)
        self.PID_UQ_UD_LIMITS                  =  self._PID_UQ_UD_LIMITS(                self,  Access.RW,  0x0149,  False)
        self.PID_TORQUE_FLUX_LIMITS            =  self._PID_TORQUE_FLUX_LIMITS(          self,  Access.RW,  0x014A,  False)
        self.PID_VELOCITY_LIMIT                =  self._PID_VELOCITY_LIMIT(              self,  Access.RW,  0x014B,  False)
        self.PID_POSITION_LIMIT_LOW            =  self._PID_POSITION_LIMIT_LOW(          self,  Access.RW,  0x014C,  True)
        self.PID_POSITION_LIMIT_HIGH           =  self._PID_POSITION_LIMIT_HIGH(         self,  Access.RW,  0x014D,  True)
        self.PID_TORQUE_FLUX_TARGET            =  self._PID_TORQUE_FLUX_TARGET(          self,  Access.RW,  0x014E,  False)
        self.PID_TORQUE_FLUX_OFFSET            =  self._PID_TORQUE_FLUX_OFFSET(          self,  Access.RW,  0x014F,  False)
        self.PID_VELOCITY_TARGET               =  self._PID_VELOCITY_TARGET(             self,  Access.RW,  0x0150,  True)
        self.PID_VELOCITY_OFFSET               =  self._PID_VELOCITY_OFFSET(             self,  Access.RW,  0x0151,  True)
        self.PID_POSITION_TARGET               =  self._PID_POSITION_TARGET(             self,  Access.RW,  0x0152,  True)
        self.PID_TORQUE_FLUX_ACTUAL            =  self._PID_TORQUE_FLUX_ACTUAL(          self,  Access.R,   0x0153,  False)
        self.PID_VELOCITY_ACTUAL               =  self._PID_VELOCITY_ACTUAL(             self,  Access.R,   0x0154,  True)
        self.PID_POSITION_ACTUAL               =  self._PID_POSITION_ACTUAL(             self,  Access.RW,  0x0155,  True)
        self.PID_POSITION_ACTUAL_OFFSET        =  self._PID_POSITION_ACTUAL_OFFSET(      self,  Access.RW,  0x0156,  True)
        self.PID_TORQUE_ERROR                  =  self._PID_TORQUE_ERROR(                self,  Access.R,   0x0157,  True)
        self.PID_FLUX_ERROR                    =  self._PID_FLUX_ERROR(                  self,  Access.R,   0x0158,  True)
        self.PID_VELOCITY_ERROR                =  self._PID_VELOCITY_ERROR(              self,  Access.R,   0x0159,  True)
        self.PID_VELOCITY_ERROR_MAX            =  self._PID_VELOCITY_ERROR_MAX(          self,  Access.RW,  0x015A,  False)
        self.PID_POSITION_ERROR                =  self._PID_POSITION_ERROR(              self,  Access.R,   0x015B,  True)
        self.PID_POSITION_ERROR_MAX            =  self._PID_POSITION_ERROR_MAX(          self,  Access.RW,  0x015C,  False)
        self.PID_TORQUE_INTEGRATOR             =  self._PID_TORQUE_INTEGRATOR(           self,  Access.RW,  0x015D,  True)
        self.PID_FLUX_INTEGRATOR               =  self._PID_FLUX_INTEGRATOR(             self,  Access.RW,  0x015E,  True)
        self.PID_VELOCITY_INTEGRATOR           =  self._PID_VELOCITY_INTEGRATOR(         self,  Access.RW,  0x015F,  True)
        self.PID_POSITION_INTEGRATOR           =  self._PID_POSITION_INTEGRATOR(         self,  Access.RW,  0x0160,  True)
        self.PIDIN_TORQUE_FLUX_TARGET          =  self._PIDIN_TORQUE_FLUX_TARGET(        self,  Access.R,   0x0161,  False)
        self.PIDIN_VELOCITY_TARGET             =  self._PIDIN_VELOCITY_TARGET(           self,  Access.R,   0x0162,  True)
        self.PIDIN_POSITION_TARGET             =  self._PIDIN_POSITION_TARGET(           self,  Access.R,   0x0163,  True)
        self.PIDIN_TORQUE_FLUX_TARGET_LIMITED  =  self._PIDIN_TORQUE_FLUX_TARGET_LIMITED(self,  Access.R,   0x0164,  False)
        self.PIDIN_VELOCITY_TARGET_LIMITED     =  self._PIDIN_VELOCITY_TARGET_LIMITED(   self,  Access.R,   0x0165,  True)
        self.PIDIN_POSITION_TARGET_LIMITED     =  self._PIDIN_POSITION_TARGET_LIMITED(   self,  Access.R,   0x0166,  True)
        self.FOC_IBETA_IALPHA                  =  self._FOC_IBETA_IALPHA(                self,  Access.R,   0x0167,  False)
        self.FOC_IQ_ID                         =  self._FOC_IQ_ID(                       self,  Access.R,   0x0168,  False)
        self.FOC_UQ_UD                         =  self._FOC_UQ_UD(                       self,  Access.R,   0x0169,  False)
        self.FOC_UQ_UD_LIMITED                 =  self._FOC_UQ_UD_LIMITED(               self,  Access.R,   0x016A,  False)
        self.FOC_UBETA_UALPHA                  =  self._FOC_UBETA_UALPHA(                self,  Access.R,   0x016B,  False)
        self.FOC_UW_UU                         =  self._FOC_UW_UU(                       self,  Access.R,   0x016C,  False)
        self.FOC_UV                            =  self._FOC_UV(                          self,  Access.R,   0x016D,  True)
        self.PWM_V_U                           =  self._PWM_V_U(                         self,  Access.R,   0x016E,  False)
        self.PWM_W                             =  self._PWM_W(                           self,  Access.R,   0x016F,  False)
        self.FOC_STATUS                        =  self._FOC_STATUS(                      self,  Access.R,   0x0170,  False)
        self.U_S_ACTUAL_I_S_ACTUAL             =  self._U_S_ACTUAL_I_S_ACTUAL(           self,  Access.R,   0x0171,  False)
        self.P_MOTOR                           =  self._P_MOTOR(                         self,  Access.R,   0x0172,  False)
        self.I_T_ACTUAL                        =  self._I_T_ACTUAL(                      self,  Access.R,   0x0173,  False)
        self.PRBS_AMPLITUDE                    =  self._PRBS_AMPLITUDE(                  self,  Access.RW,  0x0174,  False)
        self.PRBS_DOWN_SAMPLING_RATIO          =  self._PRBS_DOWN_SAMPLING_RATIO(        self,  Access.RW,  0x0175,  False)

    class _PID_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_CONFIG", parent, access, address, signed)
            self.KEEP_POS_TARGET    =  self._KEEP_POS_TARGET(  self,  Access.RW,  0x00000001,  0,   signed=False)
            self.OVERWRITE_TARGET   =  self._OVERWRITE_TARGET( self,  Access.RW,  0x00000002,  1,   signed=False)
            self.CURRENT_NORM_P     =  self._CURRENT_NORM_P(   self,  Access.RW,  0x00000004,  2,   signed=False)
            self.CURRENT_NORM_I     =  self._CURRENT_NORM_I(   self,  Access.RW,  0x00000008,  3,   signed=False)
            self.VELOCITY_NORM_P    =  self._VELOCITY_NORM_P(  self,  Access.RW,  0x00000030,  4,   signed=False)
            self.VELOCITY_NORM_I    =  self._VELOCITY_NORM_I(  self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.POSITION_NORM_P    =  self._POSITION_NORM_P(  self,  Access.RW,  0x00000300,  8,   signed=False)
            self.POSITION_NORM_I    =  self._POSITION_NORM_I(  self,  Access.RW,  0x00000C00,  10,  signed=False)
            self.VELOCITY_SHIFT     =  self._VELOCITY_SHIFT(   self,  Access.RW,  0x0000F000,  12,  signed=False)
            self.POSITION_SAMPLING  =  self._POSITION_SAMPLING(self,  Access.RW,  0x007F0000,  16,  signed=False)

        class _KEEP_POS_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("KEEP_POS_TARGET", parent, access, mask, shift, signed=signed)

        class _OVERWRITE_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OVERWRITE_TARGET", parent, access, mask, shift, signed=signed)

        class _CURRENT_NORM_P(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CUR_P_NO_SHIFT    =  Option(0,  parent,  "CUR_P_NO_SHIFT")
                    self.CUR_P_SHIFT_BY_8  =  Option(1,  parent,  "CUR_P_SHIFT_BY_8")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_NORM_P", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CURRENT_NORM_I(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.CUR_I_NO_SHIFT    =  Option(0,  parent,  "CUR_I_NO_SHIFT")
                    self.CUR_I_SHIFT_BY_8  =  Option(1,  parent,  "CUR_I_SHIFT_BY_8")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CURRENT_NORM_I", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VELOCITY_NORM_P(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.P_NO_SHIFT     =  Option(0,  parent,  "P_NO_SHIFT")
                    self.P_SHIFT_BY_8   =  Option(1,  parent,  "P_SHIFT_BY_8")
                    self.P_SHIFT_BY_16  =  Option(2,  parent,  "P_SHIFT_BY_16")
                    self.P_SHIFT_BY_24  =  Option(3,  parent,  "P_SHIFT_BY_24")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_NORM_P", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VELOCITY_NORM_I(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.I_SHIFT_BY_8   =  Option(0,  parent,  "I_SHIFT_BY_8")
                    self.I_SHIFT_BY_16  =  Option(1,  parent,  "I_SHIFT_BY_16")
                    self.I_SHIFT_BY_24  =  Option(2,  parent,  "I_SHIFT_BY_24")
                    self.I_SHIFT_BY_32  =  Option(3,  parent,  "I_SHIFT_BY_32")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_NORM_I", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _POSITION_NORM_P(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.P_NO_SHIFT     =  Option(0,  parent,  "P_NO_SHIFT")
                    self.P_SHIFT_BY_8   =  Option(1,  parent,  "P_SHIFT_BY_8")
                    self.P_SHIFT_BY_16  =  Option(2,  parent,  "P_SHIFT_BY_16")
                    self.P_SHIFT_BY_24  =  Option(3,  parent,  "P_SHIFT_BY_24")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_NORM_P", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _POSITION_NORM_I(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.I_SHIFT_BY_8   =  Option(0,  parent,  "I_SHIFT_BY_8")
                    self.I_SHIFT_BY_16  =  Option(1,  parent,  "I_SHIFT_BY_16")
                    self.I_SHIFT_BY_24  =  Option(2,  parent,  "I_SHIFT_BY_24")
                    self.I_SHIFT_BY_32  =  Option(3,  parent,  "I_SHIFT_BY_32")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_NORM_I", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VELOCITY_SHIFT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_SHIFT", parent, access, mask, shift, signed=signed)

        class _POSITION_SAMPLING(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_SAMPLING", parent, access, mask, shift, signed=signed)

    class _PID_U_S_MAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_U_S_MAX", parent, access, address, signed)
            self.U_S_MAX  =  self._U_S_MAX(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _U_S_MAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U_S_MAX", parent, access, mask, shift, signed=signed)

    class _PID_FLUX_COEFF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_FLUX_COEFF", parent, access, address, signed)
            self.FLUX_I  =  self._FLUX_I(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.FLUX_P  =  self._FLUX_P(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _FLUX_I(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FLUX_I", parent, access, mask, shift, signed=signed)

        class _FLUX_P(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FLUX_P", parent, access, mask, shift, signed=signed)

    class _PID_TORQUE_COEFF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_COEFF", parent, access, address, signed)
            self.TORQUE_I  =  self._TORQUE_I(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.TORQUE_P  =  self._TORQUE_P(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _TORQUE_I(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TORQUE_I", parent, access, mask, shift, signed=signed)

        class _TORQUE_P(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TORQUE_P", parent, access, mask, shift, signed=signed)

    class _PID_FIELDWEAK_COEFF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_FIELDWEAK_COEFF", parent, access, address, signed)
            self.FIELDWEAK_I  =  self._FIELDWEAK_I(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.FIELDWEAK_P  =  self._FIELDWEAK_P(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _FIELDWEAK_I(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FIELDWEAK_I", parent, access, mask, shift, signed=signed)

        class _FIELDWEAK_P(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FIELDWEAK_P", parent, access, mask, shift, signed=signed)

    class _PID_VELOCITY_COEFF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_COEFF", parent, access, address, signed)
            self.VELOCITY_I  =  self._VELOCITY_I(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.VELOCITY_P  =  self._VELOCITY_P(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _VELOCITY_I(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_I", parent, access, mask, shift, signed=signed)

        class _VELOCITY_P(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_P", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_COEFF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_COEFF", parent, access, address, signed)
            self.POSITION_I  =  self._POSITION_I(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.POSITION_P  =  self._POSITION_P(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _POSITION_I(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_I", parent, access, mask, shift, signed=signed)

        class _POSITION_P(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_P", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_TOLERANCE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_TOLERANCE", parent, access, address, signed)
            self.PID_POSITION_TOLERANCE  =  self._PID_POSITION_TOLERANCE(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

        class _PID_POSITION_TOLERANCE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TOLERANCE", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_TOLERANCE_DELAY(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_TOLERANCE_DELAY", parent, access, address, signed)
            self.PID_POSITION_TOLERANCE_DELAY  =  self._PID_POSITION_TOLERANCE_DELAY(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _PID_POSITION_TOLERANCE_DELAY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TOLERANCE_DELAY", parent, access, mask, shift, signed=signed)

    class _PID_UQ_UD_LIMITS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_UQ_UD_LIMITS", parent, access, address, signed)
            self.PID_UQ_UD_LIMITS  =  self._PID_UQ_UD_LIMITS(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _PID_UQ_UD_LIMITS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_UQ_UD_LIMITS", parent, access, mask, shift, signed=signed)

    class _PID_TORQUE_FLUX_LIMITS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_LIMITS", parent, access, address, signed)
            self.PID_FLUX_LIMIT    =  self._PID_FLUX_LIMIT(  self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.PID_TORQUE_LIMIT  =  self._PID_TORQUE_LIMIT(self,  Access.RW,  0x7FFF0000,  16,  signed=False)

        class _PID_FLUX_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_LIMIT", parent, access, mask, shift, signed=signed)

        class _PID_TORQUE_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_LIMIT", parent, access, mask, shift, signed=signed)

    class _PID_VELOCITY_LIMIT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_LIMIT", parent, access, address, signed)
            self.PID_VELOCITY_LIMIT  =  self._PID_VELOCITY_LIMIT(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

        class _PID_VELOCITY_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_LIMIT", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_LIMIT_LOW(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_LIMIT_LOW", parent, access, address, signed)
            self.PID_POSITION_LIMIT_LOW  =  self._PID_POSITION_LIMIT_LOW(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_POSITION_LIMIT_LOW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_LIMIT_LOW", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_LIMIT_HIGH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_LIMIT_HIGH", parent, access, address, signed)
            self.PID_POSITION_LIMIT_HIGH  =  self._PID_POSITION_LIMIT_HIGH(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_POSITION_LIMIT_HIGH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_LIMIT_HIGH", parent, access, mask, shift, signed=signed)

    class _PID_TORQUE_FLUX_TARGET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_TARGET", parent, access, address, signed)
            self.PID_FLUX_TARGET    =  self._PID_FLUX_TARGET(  self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.PID_TORQUE_TARGET  =  self._PID_TORQUE_TARGET(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _PID_FLUX_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_TARGET", parent, access, mask, shift, signed=signed)

        class _PID_TORQUE_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_TARGET", parent, access, mask, shift, signed=signed)

    class _PID_TORQUE_FLUX_OFFSET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_OFFSET", parent, access, address, signed)
            self.PID_FLUX_OFFSET    =  self._PID_FLUX_OFFSET(  self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.PID_TORQUE_OFFSET  =  self._PID_TORQUE_OFFSET(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _PID_FLUX_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_OFFSET", parent, access, mask, shift, signed=signed)

        class _PID_TORQUE_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_OFFSET", parent, access, mask, shift, signed=signed)

    class _PID_VELOCITY_TARGET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_TARGET", parent, access, address, signed)
            self.PID_VELOCITY_TARGET  =  self._PID_VELOCITY_TARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_VELOCITY_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_TARGET", parent, access, mask, shift, signed=signed)

    class _PID_VELOCITY_OFFSET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_OFFSET", parent, access, address, signed)
            self.PID_VELOCITY_OFFSET  =  self._PID_VELOCITY_OFFSET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_VELOCITY_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_OFFSET", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_TARGET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_TARGET", parent, access, address, signed)
            self.PID_POSITION_TARGET  =  self._PID_POSITION_TARGET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_POSITION_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_TARGET", parent, access, mask, shift, signed=signed)

    class _PID_TORQUE_FLUX_ACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_FLUX_ACTUAL", parent, access, address, signed)
            self.PID_FLUX_ACTUAL    =  self._PID_FLUX_ACTUAL(  self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.PID_TORQUE_ACTUAL  =  self._PID_TORQUE_ACTUAL(self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _PID_FLUX_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_ACTUAL", parent, access, mask, shift, signed=signed)

        class _PID_TORQUE_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_ACTUAL", parent, access, mask, shift, signed=signed)

    class _PID_VELOCITY_ACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_ACTUAL", parent, access, address, signed)
            self.PID_VELOCITY_ACTUAL  =  self._PID_VELOCITY_ACTUAL(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _PID_VELOCITY_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_ACTUAL", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_ACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_ACTUAL", parent, access, address, signed)
            self.PID_POSITION_ACTUAL  =  self._PID_POSITION_ACTUAL(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_POSITION_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ACTUAL", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_ACTUAL_OFFSET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_ACTUAL_OFFSET", parent, access, address, signed)
            self.PID_POSITION_ACTUAL_OFFSET  =  self._PID_POSITION_ACTUAL_OFFSET(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_POSITION_ACTUAL_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ACTUAL_OFFSET", parent, access, mask, shift, signed=signed)

    class _PID_TORQUE_ERROR(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_ERROR", parent, access, address, signed)
            self.PID_TORQUE_ERROR  =  self._PID_TORQUE_ERROR(self,  Access.R,  0x0000FFFF,  0,  signed=True)

        class _PID_TORQUE_ERROR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_ERROR", parent, access, mask, shift, signed=signed)

    class _PID_FLUX_ERROR(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_FLUX_ERROR", parent, access, address, signed)
            self.PID_FLUX_ERROR  =  self._PID_FLUX_ERROR(self,  Access.R,  0x0000FFFF,  0,  signed=True)

        class _PID_FLUX_ERROR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_ERROR", parent, access, mask, shift, signed=signed)

    class _PID_VELOCITY_ERROR(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_ERROR", parent, access, address, signed)
            self.PID_VELOCITY_ERROR  =  self._PID_VELOCITY_ERROR(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _PID_VELOCITY_ERROR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_ERROR", parent, access, mask, shift, signed=signed)

    class _PID_VELOCITY_ERROR_MAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_ERROR_MAX", parent, access, address, signed)
            self.PID_VELOCITY_ERROR_MAX  =  self._PID_VELOCITY_ERROR_MAX(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

        class _PID_VELOCITY_ERROR_MAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_ERROR_MAX", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_ERROR(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_ERROR", parent, access, address, signed)
            self.PID_POSITION_ERROR  =  self._PID_POSITION_ERROR(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _PID_POSITION_ERROR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ERROR", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_ERROR_MAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_ERROR_MAX", parent, access, address, signed)
            self.PID_POSITION_ERROR_MAX  =  self._PID_POSITION_ERROR_MAX(self,  Access.RW,  0x7FFFFFFF,  0,  signed=False)

        class _PID_POSITION_ERROR_MAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_ERROR_MAX", parent, access, mask, shift, signed=signed)

    class _PID_TORQUE_INTEGRATOR(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_TORQUE_INTEGRATOR", parent, access, address, signed)
            self.PID_TORQUE_INTEGRATOR  =  self._PID_TORQUE_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_TORQUE_INTEGRATOR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_TORQUE_INTEGRATOR", parent, access, mask, shift, signed=signed)

    class _PID_FLUX_INTEGRATOR(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_FLUX_INTEGRATOR", parent, access, address, signed)
            self.PID_FLUX_INTEGRATOR  =  self._PID_FLUX_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_FLUX_INTEGRATOR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_FLUX_INTEGRATOR", parent, access, mask, shift, signed=signed)

    class _PID_VELOCITY_INTEGRATOR(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_VELOCITY_INTEGRATOR", parent, access, address, signed)
            self.PID_VELOCITY_INTEGRATOR  =  self._PID_VELOCITY_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_VELOCITY_INTEGRATOR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_VELOCITY_INTEGRATOR", parent, access, mask, shift, signed=signed)

    class _PID_POSITION_INTEGRATOR(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PID_POSITION_INTEGRATOR", parent, access, address, signed)
            self.PID_POSITION_INTEGRATOR  =  self._PID_POSITION_INTEGRATOR(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _PID_POSITION_INTEGRATOR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PID_POSITION_INTEGRATOR", parent, access, mask, shift, signed=signed)

    class _PIDIN_TORQUE_FLUX_TARGET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PIDIN_TORQUE_FLUX_TARGET", parent, access, address, signed)
            self.PIDIN_FLUX_TARGET    =  self._PIDIN_FLUX_TARGET(  self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.PIDIN_TORQUE_TARGET  =  self._PIDIN_TORQUE_TARGET(self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _PIDIN_FLUX_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_FLUX_TARGET", parent, access, mask, shift, signed=signed)

        class _PIDIN_TORQUE_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_TORQUE_TARGET", parent, access, mask, shift, signed=signed)

    class _PIDIN_VELOCITY_TARGET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PIDIN_VELOCITY_TARGET", parent, access, address, signed)
            self.PIDIN_VELOCITY_TARGET  =  self._PIDIN_VELOCITY_TARGET(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _PIDIN_VELOCITY_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_VELOCITY_TARGET", parent, access, mask, shift, signed=signed)

    class _PIDIN_POSITION_TARGET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PIDIN_POSITION_TARGET", parent, access, address, signed)
            self.PIDIN_POSITION_TARGET  =  self._PIDIN_POSITION_TARGET(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _PIDIN_POSITION_TARGET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_POSITION_TARGET", parent, access, mask, shift, signed=signed)

    class _PIDIN_TORQUE_FLUX_TARGET_LIMITED(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PIDIN_TORQUE_FLUX_TARGET_LIMITED", parent, access, address, signed)
            self.PIDIN_FLUX_TARGET_LIMITED    =  self._PIDIN_FLUX_TARGET_LIMITED(  self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.PIDIN_TORQUE_TARGET_LIMITED  =  self._PIDIN_TORQUE_TARGET_LIMITED(self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _PIDIN_FLUX_TARGET_LIMITED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_FLUX_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

        class _PIDIN_TORQUE_TARGET_LIMITED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_TORQUE_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

    class _PIDIN_VELOCITY_TARGET_LIMITED(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PIDIN_VELOCITY_TARGET_LIMITED", parent, access, address, signed)
            self.PIDIN_VELOCITY_TARGET_LIMITED  =  self._PIDIN_VELOCITY_TARGET_LIMITED(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _PIDIN_VELOCITY_TARGET_LIMITED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_VELOCITY_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

    class _PIDIN_POSITION_TARGET_LIMITED(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PIDIN_POSITION_TARGET_LIMITED", parent, access, address, signed)
            self.PIDIN_POSITION_TARGET_LIMITED  =  self._PIDIN_POSITION_TARGET_LIMITED(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _PIDIN_POSITION_TARGET_LIMITED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PIDIN_POSITION_TARGET_LIMITED", parent, access, mask, shift, signed=signed)

    class _FOC_IBETA_IALPHA(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("FOC_IBETA_IALPHA", parent, access, address, signed)
            self.IALPHA  =  self._IALPHA(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.IBETA   =  self._IBETA( self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _IALPHA(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IALPHA", parent, access, mask, shift, signed=signed)

        class _IBETA(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IBETA", parent, access, mask, shift, signed=signed)

    class _FOC_IQ_ID(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("FOC_IQ_ID", parent, access, address, signed)
            self.ID  =  self._ID(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.IQ  =  self._IQ(self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _ID(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ID", parent, access, mask, shift, signed=signed)

        class _IQ(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IQ", parent, access, mask, shift, signed=signed)

    class _FOC_UQ_UD(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("FOC_UQ_UD", parent, access, address, signed)
            self.UD  =  self._UD(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UQ  =  self._UQ(self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _UD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD", parent, access, mask, shift, signed=signed)

        class _UQ(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ", parent, access, mask, shift, signed=signed)

    class _FOC_UQ_UD_LIMITED(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("FOC_UQ_UD_LIMITED", parent, access, address, signed)
            self.UD_LIMITED  =  self._UD_LIMITED(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UQ_LIMITED  =  self._UQ_LIMITED(self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _UD_LIMITED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD_LIMITED", parent, access, mask, shift, signed=signed)

        class _UQ_LIMITED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ_LIMITED", parent, access, mask, shift, signed=signed)

    class _FOC_UBETA_UALPHA(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("FOC_UBETA_UALPHA", parent, access, address, signed)
            self.UALPHA  =  self._UALPHA(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UBETA   =  self._UBETA( self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _UALPHA(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UALPHA", parent, access, mask, shift, signed=signed)

        class _UBETA(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UBETA", parent, access, mask, shift, signed=signed)

    class _FOC_UW_UU(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("FOC_UW_UU", parent, access, address, signed)
            self.UU  =  self._UU(self,  Access.R,  0x0000FFFF,  0,   signed=True)
            self.UW  =  self._UW(self,  Access.R,  0xFFFF0000,  16,  signed=True)

        class _UU(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UU", parent, access, mask, shift, signed=signed)

        class _UW(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UW", parent, access, mask, shift, signed=signed)

    class _FOC_UV(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("FOC_UV", parent, access, address, signed)
            self.UV  =  self._UV(self,  Access.R,  0x0000FFFF,  0,  signed=True)

        class _UV(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UV", parent, access, mask, shift, signed=signed)

    class _PWM_V_U(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_V_U", parent, access, address, signed)
            self.PWM_U  =  self._PWM_U(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.PWM_V  =  self._PWM_V(self,  Access.R,  0xFFFF0000,  16,  signed=False)

        class _PWM_U(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_U", parent, access, mask, shift, signed=signed)

        class _PWM_V(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_V", parent, access, mask, shift, signed=signed)

    class _PWM_W(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_W", parent, access, address, signed)
            self.PWM_W  =  self._PWM_W(self,  Access.R,  0x0000FFFF,  0,  signed=False)

        class _PWM_W(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_W", parent, access, mask, shift, signed=signed)

    class _FOC_STATUS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("FOC_STATUS", parent, access, address, signed)
            self.FOC_STATUS  =  self._FOC_STATUS(self,  Access.R,  0x0000000F,  0,  signed=False)

        class _FOC_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FOC_STATUS", parent, access, mask, shift, signed=signed)

    class _U_S_ACTUAL_I_S_ACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("U_S_ACTUAL_I_S_ACTUAL", parent, access, address, signed)
            self.I_S_ACTUAL  =  self._I_S_ACTUAL(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.U_S_ACTUAL  =  self._U_S_ACTUAL(self,  Access.R,  0xFFFF0000,  16,  signed=False)

        class _I_S_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I_S_ACTUAL", parent, access, mask, shift, signed=signed)

        class _U_S_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("U_S_ACTUAL", parent, access, mask, shift, signed=signed)

    class _P_MOTOR(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("P_MOTOR", parent, access, address, signed)
            self.P_MOTOR  =  self._P_MOTOR(self,  Access.R,  0xFFFFFFFF,  0,  signed=False)

        class _P_MOTOR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("P_MOTOR", parent, access, mask, shift, signed=signed)

    class _I_T_ACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("I_T_ACTUAL", parent, access, address, signed)
            self.I_T_ACTUAL  =  self._I_T_ACTUAL(self,  Access.R,  0x0000FFFF,  0,  signed=False)

        class _I_T_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("I_T_ACTUAL", parent, access, mask, shift, signed=signed)

    class _PRBS_AMPLITUDE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PRBS_AMPLITUDE", parent, access, address, signed)
            self.PRBS_AMPLITUDE  =  self._PRBS_AMPLITUDE(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _PRBS_AMPLITUDE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PRBS_AMPLITUDE", parent, access, mask, shift, signed=signed)

    class _PRBS_DOWN_SAMPLING_RATIO(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PRBS_DOWN_SAMPLING_RATIO", parent, access, address, signed)
            self.PRBS_DOWN_SAMPLING_RATIO  =  self._PRBS_DOWN_SAMPLING_RATIO(self,  Access.RW,  0x000000FF,  0,  signed=False)

        class _PRBS_DOWN_SAMPLING_RATIO(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PRBS_DOWN_SAMPLING_RATIO", parent, access, mask, shift, signed=signed)

class _BIQUAD(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("BIQUAD", channel, block, width)
        self.BIQUAD_EN    =  self._BIQUAD_EN(  self,  Access.RW,  0x0180,  False)
        self.VELOCITY_A1  =  self._VELOCITY_A1(self,  Access.RW,  0x0181,  True)
        self.VELOCITY_A2  =  self._VELOCITY_A2(self,  Access.RW,  0x0182,  True)
        self.VELOCITY_B0  =  self._VELOCITY_B0(self,  Access.RW,  0x0183,  True)
        self.VELOCITY_B1  =  self._VELOCITY_B1(self,  Access.RW,  0x0184,  True)
        self.VELOCITY_B2  =  self._VELOCITY_B2(self,  Access.RW,  0x0185,  True)
        self.TORQUE_A1    =  self._TORQUE_A1(  self,  Access.RW,  0x0186,  True)
        self.TORQUE_A2    =  self._TORQUE_A2(  self,  Access.RW,  0x0187,  True)
        self.TORQUE_B0    =  self._TORQUE_B0(  self,  Access.RW,  0x0188,  True)
        self.TORQUE_B1    =  self._TORQUE_B1(  self,  Access.RW,  0x0189,  True)
        self.TORQUE_B2    =  self._TORQUE_B2(  self,  Access.RW,  0x018A,  True)

    class _BIQUAD_EN(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("BIQUAD_EN", parent, access, address, signed)
            self.VELOCITY_EN  =  self._VELOCITY_EN(self,  Access.RW,  0x00000001,  0,  signed=False)
            self.TORQUE_EN    =  self._TORQUE_EN(  self,  Access.RW,  0x00000002,  1,  signed=False)

        class _VELOCITY_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_EN", parent, access, mask, shift, signed=signed)

        class _TORQUE_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TORQUE_EN", parent, access, mask, shift, signed=signed)

    class _VELOCITY_A1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_A1", parent, access, address, signed)
            self.COEFF_VELOCITY_A1  =  self._COEFF_VELOCITY_A1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_VELOCITY_A1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_VELOCITY_A1", parent, access, mask, shift, signed=signed)

    class _VELOCITY_A2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_A2", parent, access, address, signed)
            self.COEFF_VELOCITY_A2  =  self._COEFF_VELOCITY_A2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_VELOCITY_A2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_VELOCITY_A2", parent, access, mask, shift, signed=signed)

    class _VELOCITY_B0(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_B0", parent, access, address, signed)
            self.COEFF_VELOCITY_B0  =  self._COEFF_VELOCITY_B0(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_VELOCITY_B0(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_VELOCITY_B0", parent, access, mask, shift, signed=signed)

    class _VELOCITY_B1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_B1", parent, access, address, signed)
            self.COEFF_VELOCITY_B1  =  self._COEFF_VELOCITY_B1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_VELOCITY_B1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_VELOCITY_B1", parent, access, mask, shift, signed=signed)

    class _VELOCITY_B2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_B2", parent, access, address, signed)
            self.COEFF_VELOCITY_B2  =  self._COEFF_VELOCITY_B2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_VELOCITY_B2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_VELOCITY_B2", parent, access, mask, shift, signed=signed)

    class _TORQUE_A1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TORQUE_A1", parent, access, address, signed)
            self.COEFF_TORQUE_A1  =  self._COEFF_TORQUE_A1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_TORQUE_A1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_TORQUE_A1", parent, access, mask, shift, signed=signed)

    class _TORQUE_A2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TORQUE_A2", parent, access, address, signed)
            self.COEFF_TORQUE_A2  =  self._COEFF_TORQUE_A2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_TORQUE_A2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_TORQUE_A2", parent, access, mask, shift, signed=signed)

    class _TORQUE_B0(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TORQUE_B0", parent, access, address, signed)
            self.COEFF_TORQUE_B0  =  self._COEFF_TORQUE_B0(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_TORQUE_B0(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_TORQUE_B0", parent, access, mask, shift, signed=signed)

    class _TORQUE_B1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TORQUE_B1", parent, access, address, signed)
            self.COEFF_TORQUE_B1  =  self._COEFF_TORQUE_B1(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_TORQUE_B1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_TORQUE_B1", parent, access, mask, shift, signed=signed)

    class _TORQUE_B2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TORQUE_B2", parent, access, address, signed)
            self.COEFF_TORQUE_B2  =  self._COEFF_TORQUE_B2(self,  Access.RW,  0x00FFFFFF,  0,  signed=True)

        class _COEFF_TORQUE_B2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COEFF_TORQUE_B2", parent, access, mask, shift, signed=signed)

class _RAMPER(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("RAMPER", channel, block, width)
        self.TIME_CONFIG            =  self._TIME_CONFIG(          self,  Access.RW,   0x01C0,  False)
        self.SWITCH_MODE            =  self._SWITCH_MODE(          self,  Access.RW,   0x01C1,  False)
        self.PHI_E                  =  self._PHI_E(                self,  Access.RW,   0x01C3,  False)
        self.A1                     =  self._A1(                   self,  Access.RW,   0x01C4,  False)
        self.A2                     =  self._A2(                   self,  Access.RW,   0x01C5,  False)
        self.A_MAX                  =  self._A_MAX(                self,  Access.RW,   0x01C6,  False)
        self.D1                     =  self._D1(                   self,  Access.RW,   0x01C7,  False)
        self.D2                     =  self._D2(                   self,  Access.RW,   0x01C8,  False)
        self.D_MAX                  =  self._D_MAX(                self,  Access.RW,   0x01C9,  False)
        self.V_START                =  self._V_START(              self,  Access.RW,   0x01CA,  False)
        self.V1                     =  self._V1(                   self,  Access.RW,   0x01CB,  False)
        self.V2                     =  self._V2(                   self,  Access.RW,   0x01CC,  False)
        self.V_STOP                 =  self._V_STOP(               self,  Access.RW,   0x01CD,  False)
        self.V_MAX                  =  self._V_MAX(                self,  Access.RW,   0x01CE,  False)
        self.ACCELERATION           =  self._ACCELERATION(         self,  Access.R,    0x01CF,  True)
        self.V_ACTUAL               =  self._V_ACTUAL(             self,  Access.R,    0x01D0,  True)
        self.POSITION               =  self._POSITION(             self,  Access.RW,   0x01D1,  True)
        self.POSITION_LATCH         =  self._POSITION_LATCH(       self,  Access.R,    0x01D2,  True)
        self.POSITION_ACTUAL_LATCH  =  self._POSITION_ACTUAL_LATCH(self,  Access.R,    0x01D3,  True)
        self.STATUS                 =  self._STATUS(               self,  Access.R,    0x01D4,  False)
        self.EVENTS                 =  self._EVENTS(               self,  Access.RWC,  0x01D5,  False)

    class _TIME_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TIME_CONFIG", parent, access, address, signed)
            self.T_ZEROWAIT  =  self._T_ZEROWAIT(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.T_VMAX      =  self._T_VMAX(    self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _T_ZEROWAIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_ZEROWAIT", parent, access, mask, shift, signed=signed)

        class _T_VMAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_VMAX", parent, access, mask, shift, signed=signed)

    class _SWITCH_MODE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("SWITCH_MODE", parent, access, address, signed)
            self.RAMP_REF_L_STOP_EN     =  self._RAMP_REF_L_STOP_EN(   self,  Access.RW,  0x00000001,  0,   signed=False)
            self.RAMP_REF_R_STOP_EN     =  self._RAMP_REF_R_STOP_EN(   self,  Access.RW,  0x00000002,  1,   signed=False)
            self.RAMP_REF_H_STOP_EN     =  self._RAMP_REF_H_STOP_EN(   self,  Access.RW,  0x00000004,  2,   signed=False)
            self.RAMP_REF_L_POL         =  self._RAMP_REF_L_POL(       self,  Access.RW,  0x00000008,  3,   signed=False)
            self.RAMP_REF_R_POL         =  self._RAMP_REF_R_POL(       self,  Access.RW,  0x00000010,  4,   signed=False)
            self.RAMP_REF_H_POL         =  self._RAMP_REF_H_POL(       self,  Access.RW,  0x00000020,  5,   signed=False)
            self.SWAP_RAMP_REF_LR       =  self._SWAP_RAMP_REF_LR(     self,  Access.RW,  0x00000040,  6,   signed=False)
            self.LATCH_REF_L_ACTIVE     =  self._LATCH_REF_L_ACTIVE(   self,  Access.RW,  0x00000080,  7,   signed=False)
            self.LATCH_REF_L_INACTIVE   =  self._LATCH_REF_L_INACTIVE( self,  Access.RW,  0x00000100,  8,   signed=False)
            self.LATCH_REF_R_ACTIVE     =  self._LATCH_REF_R_ACTIVE(   self,  Access.RW,  0x00000200,  9,   signed=False)
            self.LATCH_REF_R_INACTIVE   =  self._LATCH_REF_R_INACTIVE( self,  Access.RW,  0x00000400,  10,  signed=False)
            self.LATCH_REF_H_ACTIVE     =  self._LATCH_REF_H_ACTIVE(   self,  Access.RW,  0x00000800,  11,  signed=False)
            self.LATCH_REF_H_INACTIVE   =  self._LATCH_REF_H_INACTIVE( self,  Access.RW,  0x00001000,  12,  signed=False)
            self.STALL_STOP_EN          =  self._STALL_STOP_EN(        self,  Access.RW,  0x00004000,  14,  signed=False)
            self.SOFT_STOP_EN           =  self._SOFT_STOP_EN(         self,  Access.RW,  0x00008000,  15,  signed=False)
            self.FORCE_HARD_STOP        =  self._FORCE_HARD_STOP(      self,  Access.RW,  0x00010000,  16,  signed=False)
            self.STOP_ON_POS_DEVIATION  =  self._STOP_ON_POS_DEVIATION(self,  Access.RW,  0x00020000,  17,  signed=False)
            self.STOP_ON_V_DEVIATION    =  self._STOP_ON_V_DEVIATION(  self,  Access.RW,  0x00040000,  18,  signed=False)

        class _RAMP_REF_L_STOP_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_L_STOP_EN", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_R_STOP_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_R_STOP_EN", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_H_STOP_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_H_STOP_EN", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_L_POL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NON_INVERTED  =  Option(0,  parent,  "NON_INVERTED")
                    self.INVERTED      =  Option(1,  parent,  "INVERTED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_L_POL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _RAMP_REF_R_POL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NON_INVERTED  =  Option(0,  parent,  "NON_INVERTED")
                    self.INVERTED      =  Option(1,  parent,  "INVERTED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_R_POL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _RAMP_REF_H_POL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NON_INVERTED  =  Option(0,  parent,  "NON_INVERTED")
                    self.INVERTED      =  Option(1,  parent,  "INVERTED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_H_POL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _SWAP_RAMP_REF_LR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SWAP_RAMP_REF_LR", parent, access, mask, shift, signed=signed)

        class _LATCH_REF_L_ACTIVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_REF_L_ACTIVE", parent, access, mask, shift, signed=signed)

        class _LATCH_REF_L_INACTIVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_REF_L_INACTIVE", parent, access, mask, shift, signed=signed)

        class _LATCH_REF_R_ACTIVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_REF_R_ACTIVE", parent, access, mask, shift, signed=signed)

        class _LATCH_REF_R_INACTIVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_REF_R_INACTIVE", parent, access, mask, shift, signed=signed)

        class _LATCH_REF_H_ACTIVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_REF_H_ACTIVE", parent, access, mask, shift, signed=signed)

        class _LATCH_REF_H_INACTIVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_REF_H_INACTIVE", parent, access, mask, shift, signed=signed)

        class _STALL_STOP_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALL_STOP_EN", parent, access, mask, shift, signed=signed)

        class _SOFT_STOP_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SOFT_STOP_EN", parent, access, mask, shift, signed=signed)

        class _FORCE_HARD_STOP(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FORCE_HARD_STOP", parent, access, mask, shift, signed=signed)

        class _STOP_ON_POS_DEVIATION(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_ON_POS_DEVIATION", parent, access, mask, shift, signed=signed)

        class _STOP_ON_V_DEVIATION(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STOP_ON_V_DEVIATION", parent, access, mask, shift, signed=signed)

    class _PHI_E(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_E", parent, access, address, signed)
            self.PHI_E         =  self._PHI_E(       self,  Access.R,   0x0000FFFF,  0,   signed=False)
            self.PHI_E_OFFSET  =  self._PHI_E_OFFSET(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _PHI_E(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E", parent, access, mask, shift, signed=signed)

        class _PHI_E_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

    class _A1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("A1", parent, access, address, signed)
            self.A1  =  self._A1(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _A1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A1", parent, access, mask, shift, signed=signed)

    class _A2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("A2", parent, access, address, signed)
            self.A2  =  self._A2(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _A2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A2", parent, access, mask, shift, signed=signed)

    class _A_MAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("A_MAX", parent, access, address, signed)
            self.A_MAX  =  self._A_MAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _A_MAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("A_MAX", parent, access, mask, shift, signed=signed)

    class _D1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("D1", parent, access, address, signed)
            self.D1  =  self._D1(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _D1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D1", parent, access, mask, shift, signed=signed)

    class _D2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("D2", parent, access, address, signed)
            self.D2  =  self._D2(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _D2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D2", parent, access, mask, shift, signed=signed)

    class _D_MAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("D_MAX", parent, access, address, signed)
            self.D_MAX  =  self._D_MAX(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _D_MAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("D_MAX", parent, access, mask, shift, signed=signed)

    class _V_START(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("V_START", parent, access, address, signed)
            self.V_START  =  self._V_START(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _V_START(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_START", parent, access, mask, shift, signed=signed)

    class _V1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("V1", parent, access, address, signed)
            self.V1  =  self._V1(self,  Access.RW,  0x07FFFFFF,  0,  signed=False)

        class _V1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V1", parent, access, mask, shift, signed=signed)

    class _V2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("V2", parent, access, address, signed)
            self.V2  =  self._V2(self,  Access.RW,  0x07FFFFFF,  0,  signed=False)

        class _V2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V2", parent, access, mask, shift, signed=signed)

    class _V_STOP(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("V_STOP", parent, access, address, signed)
            self.V_STOP  =  self._V_STOP(self,  Access.RW,  0x007FFFFF,  0,  signed=False)

        class _V_STOP(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_STOP", parent, access, mask, shift, signed=signed)

    class _V_MAX(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("V_MAX", parent, access, address, signed)
            self.V_MAX  =  self._V_MAX(self,  Access.RW,  0x07FFFFFF,  0,  signed=False)

        class _V_MAX(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_MAX", parent, access, mask, shift, signed=signed)

    class _ACCELERATION(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ACCELERATION", parent, access, address, signed)
            self.ACCELERATION  =  self._ACCELERATION(self,  Access.R,  0x00FFFFFF,  0,  signed=True)

        class _ACCELERATION(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ACCELERATION", parent, access, mask, shift, signed=signed)

    class _V_ACTUAL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("V_ACTUAL", parent, access, address, signed)
            self.V_ACTUAL  =  self._V_ACTUAL(self,  Access.R,  0x0FFFFFFF,  0,  signed=True)

        class _V_ACTUAL(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_ACTUAL", parent, access, mask, shift, signed=signed)

    class _POSITION(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("POSITION", parent, access, address, signed)
            self.POSITION  =  self._POSITION(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _POSITION(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION", parent, access, mask, shift, signed=signed)

    class _POSITION_LATCH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("POSITION_LATCH", parent, access, address, signed)
            self.POSITION_LATCH  =  self._POSITION_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _POSITION_LATCH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_LATCH", parent, access, mask, shift, signed=signed)

    class _POSITION_ACTUAL_LATCH(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("POSITION_ACTUAL_LATCH", parent, access, address, signed)
            self.POSITION_ACTUAL_LATCH  =  self._POSITION_ACTUAL_LATCH(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _POSITION_ACTUAL_LATCH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_ACTUAL_LATCH", parent, access, mask, shift, signed=signed)

    class _STATUS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS", parent, access, address, signed)
            self.RAMP_REF_L_STATUS        =  self._RAMP_REF_L_STATUS(      self,  Access.R,  0x00000001,  0,   signed=False)
            self.RAMP_REF_R_STATUS        =  self._RAMP_REF_R_STATUS(      self,  Access.R,  0x00000002,  1,   signed=False)
            self.RAMP_REF_H_STATUS        =  self._RAMP_REF_H_STATUS(      self,  Access.R,  0x00000004,  2,   signed=False)
            self.RAMP_REF_L_STOP_STATUS   =  self._RAMP_REF_L_STOP_STATUS( self,  Access.R,  0x00000040,  6,   signed=False)
            self.RAMP_REF_R_STOP_STATUS   =  self._RAMP_REF_R_STOP_STATUS( self,  Access.R,  0x00000080,  7,   signed=False)
            self.RAMP_REF_H_STOP_STATUS   =  self._RAMP_REF_H_STOP_STATUS( self,  Access.R,  0x00000100,  8,   signed=False)
            self.V_REACHED_STATUS         =  self._V_REACHED_STATUS(       self,  Access.R,  0x00000800,  11,  signed=False)
            self.POSITION_REACHED_STATUS  =  self._POSITION_REACHED_STATUS(self,  Access.R,  0x00001000,  12,  signed=False)
            self.V_ZERO                   =  self._V_ZERO(                 self,  Access.R,  0x00002000,  13,  signed=False)
            self.T_ZEROWAIT_ACTIVE        =  self._T_ZEROWAIT_ACTIVE(      self,  Access.R,  0x00004000,  14,  signed=False)
            self.STALL_IN_V_ERR           =  self._STALL_IN_V_ERR(         self,  Access.R,  0x00010000,  16,  signed=False)
            self.STALL_IN_POSITION_ERR    =  self._STALL_IN_POSITION_ERR(  self,  Access.R,  0x00020000,  17,  signed=False)

        class _RAMP_REF_L_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_L_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_R_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_R_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_H_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_H_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_L_STOP_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_L_STOP_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_R_STOP_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_R_STOP_STATUS", parent, access, mask, shift, signed=signed)

        class _RAMP_REF_H_STOP_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RAMP_REF_H_STOP_STATUS", parent, access, mask, shift, signed=signed)

        class _V_REACHED_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_REACHED_STATUS", parent, access, mask, shift, signed=signed)

        class _POSITION_REACHED_STATUS(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_REACHED_STATUS", parent, access, mask, shift, signed=signed)

        class _V_ZERO(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_ZERO", parent, access, mask, shift, signed=signed)

        class _T_ZEROWAIT_ACTIVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("T_ZEROWAIT_ACTIVE", parent, access, mask, shift, signed=signed)

        class _STALL_IN_V_ERR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALL_IN_V_ERR", parent, access, mask, shift, signed=signed)

        class _STALL_IN_POSITION_ERR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALL_IN_POSITION_ERR", parent, access, mask, shift, signed=signed)

    class _EVENTS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("EVENTS", parent, access, address, signed)
            self.POSITION_REACHED_EVENT  =  self._POSITION_REACHED_EVENT(self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.STALL_STOP_EVENT        =  self._STALL_STOP_EVENT(      self,  Access.RWC,  0x00000002,  1,  signed=False)
            self.SECOND_MOVE_EVENT       =  self._SECOND_MOVE_EVENT(     self,  Access.RWC,  0x00000004,  2,  signed=False)
            self.LATCH_REF_H_READY       =  self._LATCH_REF_H_READY(     self,  Access.RWC,  0x00000008,  3,  signed=False)
            self.LATCH_REF_L_READY       =  self._LATCH_REF_L_READY(     self,  Access.RWC,  0x00000010,  4,  signed=False)
            self.LATCH_REF_R_READY       =  self._LATCH_REF_R_READY(     self,  Access.RWC,  0x00000020,  5,  signed=False)

        class _POSITION_REACHED_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_REACHED_EVENT", parent, access, mask, shift, signed=signed)

        class _STALL_STOP_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("STALL_STOP_EVENT", parent, access, mask, shift, signed=signed)

        class _SECOND_MOVE_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SECOND_MOVE_EVENT", parent, access, mask, shift, signed=signed)

        class _LATCH_REF_H_READY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_REF_H_READY", parent, access, mask, shift, signed=signed)

        class _LATCH_REF_L_READY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_REF_L_READY", parent, access, mask, shift, signed=signed)

        class _LATCH_REF_R_READY(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LATCH_REF_R_READY", parent, access, mask, shift, signed=signed)

class _EXT_CTRL(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("EXT_CTRL", channel, block, width)
        self.VOLTAGE  =  self._VOLTAGE(self,  Access.RW,  0x0200,  False)
        self.PWM_V_U  =  self._PWM_V_U(self,  Access.RW,  0x0202,  False)
        self.PWM_W    =  self._PWM_W(  self,  Access.RW,  0x0203,  False)

    class _VOLTAGE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VOLTAGE", parent, access, address, signed)
            self.UD  =  self._UD(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.UQ  =  self._UQ(self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _UD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UD", parent, access, mask, shift, signed=signed)

        class _UQ(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UQ", parent, access, mask, shift, signed=signed)

    class _PWM_V_U(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_V_U", parent, access, address, signed)
            self.PWM_U  =  self._PWM_U(self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.PWM_V  =  self._PWM_V(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _PWM_U(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_U", parent, access, mask, shift, signed=signed)

        class _PWM_V(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_V", parent, access, mask, shift, signed=signed)

    class _PWM_W(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PWM_W", parent, access, address, signed)
            self.PWM_W  =  self._PWM_W(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _PWM_W(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PWM_W", parent, access, mask, shift, signed=signed)

class _FEEDBACK(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("FEEDBACK", channel, block, width)
        self.CONF_CH_A            =  self._CONF_CH_A(          self,  Access.RW,  0x0240,  False)
        self.CONF_CH_B            =  self._CONF_CH_B(          self,  Access.RW,  0x0241,  False)
        self.PHI_E_OFFSET         =  self._PHI_E_OFFSET(       self,  Access.RW,  0x0242,  False)
        self.LUT                  =  self._LUT(                self,  Access.RW,  0x0243,  False)
        self.VELOCITY_FRQ_CONF    =  self._VELOCITY_FRQ_CONF(  self,  Access.RW,  0x0244,  False)
        self.VELOCITY_PER_CONF    =  self._VELOCITY_PER_CONF(  self,  Access.RW,  0x0245,  False)
        self.VELOCITY_PER_FILTER  =  self._VELOCITY_PER_FILTER(self,  Access.RW,  0x0246,  False)
        self.PHI_CONVERTED        =  self._PHI_CONVERTED(      self,  Access.R,   0x0247,  False)
        self.CH_A                 =  self._CH_A(               self,  Access.R,   0x0248,  False)
        self.CH_B                 =  self._CH_B(               self,  Access.R,   0x0249,  False)
        self.VELOCITY_FRQ         =  self._VELOCITY_FRQ(       self,  Access.R,   0x024A,  True)
        self.VELOCITY_PER         =  self._VELOCITY_PER(       self,  Access.R,   0x024B,  True)
        self.LUT_WDATA            =  self._LUT_WDATA(          self,  Access.RW,  0x024C,  False)
        self.PHI_EXT_A            =  self._PHI_EXT_A(          self,  Access.RW,  0x024D,  False)
        self.PHI_EXT_B            =  self._PHI_EXT_B(          self,  Access.RW,  0x024E,  False)
        self.VELOCITY_EXT         =  self._VELOCITY_EXT(       self,  Access.RW,  0x024F,  True)
        self.OUTPUT_CONF          =  self._OUTPUT_CONF(        self,  Access.RW,  0x0250,  False)
        self.PHI_E                =  self._PHI_E(              self,  Access.R,   0x0251,  False)
        self.PHI_DIFF_LIMIT       =  self._PHI_DIFF_LIMIT(     self,  Access.RW,  0x0252,  False)

    class _CONF_CH_A(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CONF_CH_A", parent, access, address, signed)
            self.CPR_INV_A  =  self._CPR_INV_A(self,  Access.RW,  0x00FFFFFF,  0,   signed=False)
            self.SRC_SEL_A  =  self._SRC_SEL_A(self,  Access.RW,  0x0F000000,  24,  signed=False)

        class _CPR_INV_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CPR_INV_A", parent, access, mask, shift, signed=signed)

        class _SRC_SEL_A(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ABN_1          =  Option(0,  parent,  "ABN_1")
                    self.ABN_1_FREE     =  Option(1,  parent,  "ABN_1_FREE")
                    self.ABN_2          =  Option(2,  parent,  "ABN_2")
                    self.ABN_2_FREE     =  Option(3,  parent,  "ABN_2_FREE")
                    self.ANALOG_SENSOR  =  Option(4,  parent,  "ANALOG_SENSOR")
                    self.HALL           =  Option(5,  parent,  "HALL")
                    self.HALL_FREE      =  Option(6,  parent,  "HALL_FREE")
                    self.PHI_EXT_A      =  Option(7,  parent,  "PHI_EXT_A")
                    self.PHI_EXT_B      =  Option(8,  parent,  "PHI_EXT_B")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SRC_SEL_A", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _CONF_CH_B(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CONF_CH_B", parent, access, address, signed)
            self.CPR_INV_B  =  self._CPR_INV_B(self,  Access.RW,  0x00FFFFFF,  0,   signed=False)
            self.SRC_SEL_B  =  self._SRC_SEL_B(self,  Access.RW,  0x0F000000,  24,  signed=False)

        class _CPR_INV_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CPR_INV_B", parent, access, mask, shift, signed=signed)

        class _SRC_SEL_B(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ABN_1          =  Option(0,  parent,  "ABN_1")
                    self.ABN_1_FREE     =  Option(1,  parent,  "ABN_1_FREE")
                    self.ABN_2          =  Option(2,  parent,  "ABN_2")
                    self.ABN_2_FREE     =  Option(3,  parent,  "ABN_2_FREE")
                    self.ANALOG_SENSOR  =  Option(4,  parent,  "ANALOG_SENSOR")
                    self.HALL           =  Option(5,  parent,  "HALL")
                    self.HALL_FREE      =  Option(6,  parent,  "HALL_FREE")
                    self.PHI_EXT_A      =  Option(7,  parent,  "PHI_EXT_A")
                    self.PHI_EXT_B      =  Option(8,  parent,  "PHI_EXT_B")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SRC_SEL_B", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _PHI_E_OFFSET(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_E_OFFSET", parent, access, address, signed)
            self.PHI_E_OFFSET  =  self._PHI_E_OFFSET(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _PHI_E_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_OFFSET", parent, access, mask, shift, signed=signed)

    class _LUT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("LUT", parent, access, address, signed)
            self.SPLIT_MODE_EN  =  self._SPLIT_MODE_EN(self,  Access.RW,  0x00000001,  0,   signed=False)
            self.LOOKUP_A_EN    =  self._LOOKUP_A_EN(  self,  Access.RW,  0x00000002,  1,   signed=False)
            self.LOOKUP_B_EN    =  self._LOOKUP_B_EN(  self,  Access.RW,  0x00000004,  2,   signed=False)
            self.LOOKUP_A_GAIN  =  self._LOOKUP_A_GAIN(self,  Access.RW,  0x00000700,  8,   signed=False)
            self.LOOKUP_B_GAIN  =  self._LOOKUP_B_GAIN(self,  Access.RW,  0x00007000,  12,  signed=False)
            self.ADDR           =  self._ADDR(         self,  Access.RW,  0x00FF0000,  16,  signed=False)
            self.RDATA          =  self._RDATA(        self,  Access.R,   0xFF000000,  24,  signed=True)

        class _SPLIT_MODE_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SPLIT_MODE_EN", parent, access, mask, shift, signed=signed)

        class _LOOKUP_A_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LOOKUP_A_EN", parent, access, mask, shift, signed=signed)

        class _LOOKUP_B_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LOOKUP_B_EN", parent, access, mask, shift, signed=signed)

        class _LOOKUP_A_GAIN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.GAIN1   =  Option(0,  parent,  "GAIN1")
                    self.GAIN2   =  Option(1,  parent,  "GAIN2")
                    self.GAIN4   =  Option(2,  parent,  "GAIN4")
                    self.GAIN8   =  Option(3,  parent,  "GAIN8")
                    self.GAIN16  =  Option(4,  parent,  "GAIN16")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LOOKUP_A_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _LOOKUP_B_GAIN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.GAIN1   =  Option(0,  parent,  "GAIN1")
                    self.GAIN2   =  Option(1,  parent,  "GAIN2")
                    self.GAIN4   =  Option(2,  parent,  "GAIN4")
                    self.GAIN8   =  Option(3,  parent,  "GAIN8")
                    self.GAIN16  =  Option(4,  parent,  "GAIN16")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LOOKUP_B_GAIN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ADDR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADDR", parent, access, mask, shift, signed=signed)

        class _RDATA(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RDATA", parent, access, mask, shift, signed=signed)

    class _VELOCITY_FRQ_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_FRQ_CONF", parent, access, address, signed)
            self.VELOCITY_SYNC_SRC  =  self._VELOCITY_SYNC_SRC(self,  Access.RW,  0x00000001,  0,  signed=False)
            self.VELOCITY_SAMPLING  =  self._VELOCITY_SAMPLING(self,  Access.RW,  0x000000FE,  1,  signed=False)
            self.VELOCITY_SCALING   =  self._VELOCITY_SCALING( self,  Access.RW,  0x00FFFF00,  8,  signed=False)

        class _VELOCITY_SYNC_SRC(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.PWM_Z  =  Option(0,  parent,  "PWM_Z")
                    self.PWM_C  =  Option(1,  parent,  "PWM_C")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_SYNC_SRC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VELOCITY_SAMPLING(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_SAMPLING", parent, access, mask, shift, signed=signed)

        class _VELOCITY_SCALING(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_SCALING", parent, access, mask, shift, signed=signed)

    class _VELOCITY_PER_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_PER_CONF", parent, access, address, signed)
            self.POS_DEV_MIN    =  self._POS_DEV_MIN(  self,  Access.RW,  0x00007FFF,  0,   signed=False)
            self.POS_DEV_TIMER  =  self._POS_DEV_TIMER(self,  Access.RW,  0xFFFF0000,  16,  signed=False)

        class _POS_DEV_MIN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POS_DEV_MIN", parent, access, mask, shift, signed=signed)

        class _POS_DEV_TIMER(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POS_DEV_TIMER", parent, access, mask, shift, signed=signed)

    class _VELOCITY_PER_FILTER(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_PER_FILTER", parent, access, address, signed)
            self.FILTER_WIDTH  =  self._FILTER_WIDTH(self,  Access.RW,  0x00000007,  0,  signed=False)

        class _FILTER_WIDTH(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FILTER_WIDTH", parent, access, mask, shift, signed=signed)

    class _PHI_CONVERTED(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_CONVERTED", parent, access, address, signed)
            self.PHI_CONVERTED_A  =  self._PHI_CONVERTED_A(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.PHI_CONVERTED_B  =  self._PHI_CONVERTED_B(self,  Access.R,  0xFFFF0000,  16,  signed=False)

        class _PHI_CONVERTED_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_CONVERTED_A", parent, access, mask, shift, signed=signed)

        class _PHI_CONVERTED_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_CONVERTED_B", parent, access, mask, shift, signed=signed)

    class _CH_A(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CH_A", parent, access, address, signed)
            self.PHI_LOOKUP_A         =  self._PHI_LOOKUP_A(       self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.PHI_EXTRAPOLATED_AB  =  self._PHI_EXTRAPOLATED_AB(self,  Access.R,  0xFFFF0000,  16,  signed=False)

        class _PHI_LOOKUP_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_LOOKUP_A", parent, access, mask, shift, signed=signed)

        class _PHI_EXTRAPOLATED_AB(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_EXTRAPOLATED_AB", parent, access, mask, shift, signed=signed)

    class _CH_B(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CH_B", parent, access, address, signed)
            self.PHI_LOOKUP_B  =  self._PHI_LOOKUP_B(self,  Access.R,  0x0000FFFF,  0,  signed=False)

        class _PHI_LOOKUP_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_LOOKUP_B", parent, access, mask, shift, signed=signed)

    class _VELOCITY_FRQ(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_FRQ", parent, access, address, signed)
            self.VELOCITY_FRQ  =  self._VELOCITY_FRQ(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _VELOCITY_FRQ(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_FRQ", parent, access, mask, shift, signed=signed)

    class _VELOCITY_PER(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_PER", parent, access, address, signed)
            self.VELOCITY_PER  =  self._VELOCITY_PER(self,  Access.R,  0xFFFFFFFF,  0,  signed=True)

        class _VELOCITY_PER(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_PER", parent, access, mask, shift, signed=signed)

    class _LUT_WDATA(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("LUT_WDATA", parent, access, address, signed)
            self.WDATA  =  self._WDATA(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _WDATA(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WDATA", parent, access, mask, shift, signed=signed)

    class _PHI_EXT_A(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_EXT_A", parent, access, address, signed)
            self.PHI_EXT_A  =  self._PHI_EXT_A(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

        class _PHI_EXT_A(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_EXT_A", parent, access, mask, shift, signed=signed)

    class _PHI_EXT_B(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_EXT_B", parent, access, address, signed)
            self.PHI_EXT_B  =  self._PHI_EXT_B(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

        class _PHI_EXT_B(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_EXT_B", parent, access, mask, shift, signed=signed)

    class _VELOCITY_EXT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("VELOCITY_EXT", parent, access, address, signed)
            self.VELOCITY_EXT  =  self._VELOCITY_EXT(self,  Access.RW,  0xFFFFFFFF,  0,  signed=True)

        class _VELOCITY_EXT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_EXT", parent, access, mask, shift, signed=signed)

    class _OUTPUT_CONF(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("OUTPUT_CONF", parent, access, address, signed)
            self.PHI_E_MUL_FACTOR    =  self._PHI_E_MUL_FACTOR(  self,  Access.RW,  0x000000FF,  0,   signed=False)
            self.PHI_E_SRC           =  self._PHI_E_SRC(         self,  Access.RW,  0x00030000,  16,  signed=False)
            self.POSITION_SRC        =  self._POSITION_SRC(      self,  Access.RW,  0x00100000,  20,  signed=False)
            self.VELOCITY_SRC        =  self._VELOCITY_SRC(      self,  Access.RW,  0x00200000,  21,  signed=False)
            self.VELOCITY_SELECTION  =  self._VELOCITY_SELECTION(self,  Access.RW,  0x00C00000,  22,  signed=False)

        class _PHI_E_MUL_FACTOR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_MUL_FACTOR", parent, access, mask, shift, signed=signed)

        class _PHI_E_SRC(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOOKUP_A        =  Option(0,  parent,  "LOOKUP_A")
                    self.LOOKUP_B        =  Option(1,  parent,  "LOOKUP_B")
                    self.EXTRAPOLATOR_A  =  Option(2,  parent,  "EXTRAPOLATOR_A")
                    self.EXTRAPOLATOR_B  =  Option(3,  parent,  "EXTRAPOLATOR_B")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_SRC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _POSITION_SRC(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOOKUP_A  =  Option(0,  parent,  "LOOKUP_A")
                    self.LOOKUP_B  =  Option(1,  parent,  "LOOKUP_B")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("POSITION_SRC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VELOCITY_SRC(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.LOOKUP_A  =  Option(0,  parent,  "LOOKUP_A")
                    self.LOOKUP_B  =  Option(1,  parent,  "LOOKUP_B")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_SRC", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _VELOCITY_SELECTION(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.VELOCITY_FRQ  =  Option(0,  parent,  "VELOCITY_FRQ")
                    self.VELOCITY_PER  =  Option(1,  parent,  "VELOCITY_PER")
                    self.VELOCITY_EXT  =  Option(2,  parent,  "VELOCITY_EXT")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VELOCITY_SELECTION", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _PHI_E(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_E", parent, access, address, signed)
            self.PHI_E_FOC  =  self._PHI_E_FOC(self,  Access.R,  0x0000FFFF,  0,  signed=False)

        class _PHI_E_FOC(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_E_FOC", parent, access, mask, shift, signed=signed)

    class _PHI_DIFF_LIMIT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("PHI_DIFF_LIMIT", parent, access, address, signed)
            self.PHI_DIFF_LIMIT  =  self._PHI_DIFF_LIMIT(self,  Access.RW,  0x0000FFFF,  0,  signed=False)

        class _PHI_DIFF_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("PHI_DIFF_LIMIT", parent, access, mask, shift, signed=signed)

class _ABN(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("ABN", channel, block, width)
        self.CONFIG           =  self._CONFIG(         self,  Access.RW,   0x0280,  False)
        self.COUNT            =  self._COUNT(          self,  Access.RW,   0x0281,  False)
        self.COUNT_N_CAPTURE  =  self._COUNT_N_CAPTURE(self,  Access.R,    0x0282,  False)
        self.COUNT_N_WRITE    =  self._COUNT_N_WRITE(  self,  Access.RW,   0x0283,  False)
        self.EVENTS           =  self._EVENTS(         self,  Access.RWC,  0x0284,  False)

    class _CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CONFIG", parent, access, address, signed)
            self.COMBINED_N  =  self._COMBINED_N(self,  Access.RW,  0x00000001,  0,  signed=False)
            self.CLN         =  self._CLN(       self,  Access.RW,  0x00000002,  1,  signed=False)
            self.INV_DIR     =  self._INV_DIR(   self,  Access.RW,  0x00000008,  3,  signed=False)
            self.CPR         =  self._CPR(       self,  Access.RW,  0xFFFFFF00,  8,  signed=False)

        class _COMBINED_N(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ONLY_N  =  Option(0,  parent,  "ONLY_N")
                    self.ALL     =  Option(1,  parent,  "ALL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMBINED_N", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OFF  =  Option(0,  parent,  "OFF")
                    self.ON   =  Option(1,  parent,  "ON")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _INV_DIR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_DIR", parent, access, mask, shift, signed=signed)

        class _CPR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CPR", parent, access, mask, shift, signed=signed)

    class _COUNT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COUNT", parent, access, address, signed)
            self.COUNT  =  self._COUNT(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

        class _COUNT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNT", parent, access, mask, shift, signed=signed)

    class _COUNT_N_CAPTURE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COUNT_N_CAPTURE", parent, access, address, signed)
            self.COUNT_N_CAPTURE  =  self._COUNT_N_CAPTURE(self,  Access.R,  0x00FFFFFF,  0,  signed=False)

        class _COUNT_N_CAPTURE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNT_N_CAPTURE", parent, access, mask, shift, signed=signed)

    class _COUNT_N_WRITE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COUNT_N_WRITE", parent, access, address, signed)
            self.COUNT_N_WRITE  =  self._COUNT_N_WRITE(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

        class _COUNT_N_WRITE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNT_N_WRITE", parent, access, mask, shift, signed=signed)

    class _EVENTS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("EVENTS", parent, access, address, signed)
            self.INVALID_SIGNAL_EVENT  =  self._INVALID_SIGNAL_EVENT(self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.N_EVENT               =  self._N_EVENT(             self,  Access.RWC,  0x00000002,  1,  signed=False)

        class _INVALID_SIGNAL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INVALID_SIGNAL_EVENT", parent, access, mask, shift, signed=signed)

        class _N_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_EVENT", parent, access, mask, shift, signed=signed)

class _ABN2(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("ABN2", channel, block, width)
        self.CONFIG           =  self._CONFIG(         self,  Access.RW,   0x02C0,  False)
        self.COUNT            =  self._COUNT(          self,  Access.RW,   0x02C1,  False)
        self.COUNT_N_CAPTURE  =  self._COUNT_N_CAPTURE(self,  Access.R,    0x02C2,  False)
        self.COUNT_N_WRITE    =  self._COUNT_N_WRITE(  self,  Access.RW,   0x02C3,  False)
        self.EVENTS           =  self._EVENTS(         self,  Access.RWC,  0x02C4,  False)

    class _CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CONFIG", parent, access, address, signed)
            self.COMBINED_N  =  self._COMBINED_N(self,  Access.RW,  0x00000001,  0,  signed=False)
            self.CLN         =  self._CLN(       self,  Access.RW,  0x00000002,  1,  signed=False)
            self.INV_DIR     =  self._INV_DIR(   self,  Access.RW,  0x00000008,  3,  signed=False)
            self.CPR         =  self._CPR(       self,  Access.RW,  0xFFFFFF00,  8,  signed=False)

        class _COMBINED_N(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ONLY_N  =  Option(0,  parent,  "ONLY_N")
                    self.ALL     =  Option(1,  parent,  "ALL")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMBINED_N", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _CLN(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.OFF  =  Option(0,  parent,  "OFF")
                    self.ON   =  Option(1,  parent,  "ON")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CLN", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _INV_DIR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INV_DIR", parent, access, mask, shift, signed=signed)

        class _CPR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CPR", parent, access, mask, shift, signed=signed)

    class _COUNT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COUNT", parent, access, address, signed)
            self.COUNT  =  self._COUNT(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

        class _COUNT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNT", parent, access, mask, shift, signed=signed)

    class _COUNT_N_CAPTURE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COUNT_N_CAPTURE", parent, access, address, signed)
            self.COUNT_N_CAPTURE  =  self._COUNT_N_CAPTURE(self,  Access.R,  0x00FFFFFF,  0,  signed=False)

        class _COUNT_N_CAPTURE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNT_N_CAPTURE", parent, access, mask, shift, signed=signed)

    class _COUNT_N_WRITE(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COUNT_N_WRITE", parent, access, address, signed)
            self.COUNT_N_WRITE  =  self._COUNT_N_WRITE(self,  Access.RW,  0x00FFFFFF,  0,  signed=False)

        class _COUNT_N_WRITE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNT_N_WRITE", parent, access, mask, shift, signed=signed)

    class _EVENTS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("EVENTS", parent, access, address, signed)
            self.INVALID_SIGNAL_EVENT  =  self._INVALID_SIGNAL_EVENT(self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.N_EVENT               =  self._N_EVENT(             self,  Access.RWC,  0x00000002,  1,  signed=False)

        class _INVALID_SIGNAL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INVALID_SIGNAL_EVENT", parent, access, mask, shift, signed=signed)

        class _N_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_EVENT", parent, access, mask, shift, signed=signed)

class _HALL(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("HALL", channel, block, width)
        self.MAP_CONFIG     =  self._MAP_CONFIG(   self,  Access.RW,   0x0300,  False)
        self.DIG_COUNT      =  self._DIG_COUNT(    self,  Access.R,    0x0301,  False)
        self.ANA_CONFIG     =  self._ANA_CONFIG(   self,  Access.RW,   0x0302,  False)
        self.ANA_UX_CONFIG  =  self._ANA_UX_CONFIG(self,  Access.RW,   0x0303,  False)
        self.ANA_VN_CONFIG  =  self._ANA_VN_CONFIG(self,  Access.RW,   0x0304,  False)
        self.ANA_WY_CONFIG  =  self._ANA_WY_CONFIG(self,  Access.RW,   0x0305,  False)
        self.ANA_UX_OUT     =  self._ANA_UX_OUT(   self,  Access.R,    0x0306,  True)
        self.ANA_VN_OUT     =  self._ANA_VN_OUT(   self,  Access.R,    0x0307,  True)
        self.ANA_WY_OUT     =  self._ANA_WY_OUT(   self,  Access.R,    0x0308,  True)
        self.ANA_OUT        =  self._ANA_OUT(      self,  Access.R,    0x0309,  False)
        self.DIG_EVENTS     =  self._DIG_EVENTS(   self,  Access.RWC,  0x030A,  False)

    class _MAP_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("MAP_CONFIG", parent, access, address, signed)
            self.HALL_MAP      =  self._HALL_MAP(    self,  Access.RW,  0x00000007,  0,  signed=False)
            self.ANA_HALL_MAP  =  self._ANA_HALL_MAP(self,  Access.RW,  0x00000070,  4,  signed=False)

        class _HALL_MAP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.UVW  =  Option(0,  parent,  "UVW")
                    self.UWV  =  Option(1,  parent,  "UWV")
                    self.VUW  =  Option(2,  parent,  "VUW")
                    self.WUV  =  Option(3,  parent,  "WUV")
                    self.VWU  =  Option(4,  parent,  "VWU")
                    self.WVU  =  Option(5,  parent,  "WVU")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("HALL_MAP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _ANA_HALL_MAP(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.ANA_UVW  =  Option(0,  parent,  "ANA_UVW")
                    self.ANA_UWV  =  Option(1,  parent,  "ANA_UWV")
                    self.ANA_VUW  =  Option(2,  parent,  "ANA_VUW")
                    self.ANA_WUV  =  Option(3,  parent,  "ANA_WUV")
                    self.ANA_VWU  =  Option(4,  parent,  "ANA_VWU")
                    self.ANA_WVU  =  Option(5,  parent,  "ANA_WVU")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANA_HALL_MAP", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

    class _DIG_COUNT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("DIG_COUNT", parent, access, address, signed)
            self.COUNT  =  self._COUNT(self,  Access.R,  0x00000007,  0,  signed=False)

        class _COUNT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNT", parent, access, mask, shift, signed=signed)

    class _ANA_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANA_CONFIG", parent, access, address, signed)
            self.N_PULSE_THRESHOLD  =  self._N_PULSE_THRESHOLD(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.ANA_MODE           =  self._ANA_MODE(         self,  Access.RW,  0x00010000,  16,  signed=False)
            self.N_PULSE_EDGE       =  self._N_PULSE_EDGE(     self,  Access.RW,  0x00020000,  17,  signed=False)
            self.N_PULSE_POL        =  self._N_PULSE_POL(      self,  Access.RW,  0x00040000,  18,  signed=False)
            self.TWO_CYCLE_MODE_EN  =  self._TWO_CYCLE_MODE_EN(self,  Access.RW,  0x00080000,  19,  signed=False)
            self.USE_N_PULSE        =  self._USE_N_PULSE(      self,  Access.RW,  0x00100000,  20,  signed=False)
            self.N_PULSE_OUT        =  self._N_PULSE_OUT(      self,  Access.R,   0x00200000,  21,  signed=False)
            self.ADC_CLIPPED        =  self._ADC_CLIPPED(      self,  Access.R,   0x00400000,  22,  signed=False)

        class _N_PULSE_THRESHOLD(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_PULSE_THRESHOLD", parent, access, mask, shift, signed=signed)

        class _ANA_MODE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.XY   =  Option(0,  parent,  "XY")
                    self.UVW  =  Option(1,  parent,  "UVW")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANA_MODE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _N_PULSE_EDGE(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.RISING   =  Option(0,  parent,  "RISING")
                    self.FALLING  =  Option(1,  parent,  "FALLING")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_PULSE_EDGE", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _N_PULSE_POL(Field):
            class _Choice(Choice):
                def __init__(self, parent) -> None:
                    super().__init__(parent)
                    self.NON_INVERTED  =  Option(0,  parent,  "NON_INVERTED")
                    self.INVERTED      =  Option(1,  parent,  "INVERTED")

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_PULSE_POL", parent, access, mask, shift, signed=signed)

                self.choice = self._Choice(self)

        class _TWO_CYCLE_MODE_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TWO_CYCLE_MODE_EN", parent, access, mask, shift, signed=signed)

        class _USE_N_PULSE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("USE_N_PULSE", parent, access, mask, shift, signed=signed)

        class _N_PULSE_OUT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("N_PULSE_OUT", parent, access, mask, shift, signed=signed)

        class _ADC_CLIPPED(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ADC_CLIPPED", parent, access, mask, shift, signed=signed)

    class _ANA_UX_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANA_UX_CONFIG", parent, access, address, signed)
            self.UX_OFFSET  =  self._UX_OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.UX_SCALE   =  self._UX_SCALE( self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _UX_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UX_OFFSET", parent, access, mask, shift, signed=signed)

        class _UX_SCALE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UX_SCALE", parent, access, mask, shift, signed=signed)

    class _ANA_VN_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANA_VN_CONFIG", parent, access, address, signed)
            self.VN_OFFSET  =  self._VN_OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.VN_SCALE   =  self._VN_SCALE( self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _VN_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VN_OFFSET", parent, access, mask, shift, signed=signed)

        class _VN_SCALE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VN_SCALE", parent, access, mask, shift, signed=signed)

    class _ANA_WY_CONFIG(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANA_WY_CONFIG", parent, access, address, signed)
            self.WY_OFFSET  =  self._WY_OFFSET(self,  Access.RW,  0x0000FFFF,  0,   signed=True)
            self.WY_SCALE   =  self._WY_SCALE( self,  Access.RW,  0xFFFF0000,  16,  signed=True)

        class _WY_OFFSET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WY_OFFSET", parent, access, mask, shift, signed=signed)

        class _WY_SCALE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WY_SCALE", parent, access, mask, shift, signed=signed)

    class _ANA_UX_OUT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANA_UX_OUT", parent, access, address, signed)
            self.UX_OUT  =  self._UX_OUT(self,  Access.R,  0x0000FFFF,  0,  signed=True)

        class _UX_OUT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UX_OUT", parent, access, mask, shift, signed=signed)

    class _ANA_VN_OUT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANA_VN_OUT", parent, access, address, signed)
            self.VN_OUT  =  self._VN_OUT(self,  Access.R,  0x0000FFFF,  0,  signed=True)

        class _VN_OUT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VN_OUT", parent, access, mask, shift, signed=signed)

    class _ANA_WY_OUT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANA_WY_OUT", parent, access, address, signed)
            self.WY_OUT  =  self._WY_OUT(self,  Access.R,  0x0000FFFF,  0,  signed=True)

        class _WY_OUT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("WY_OUT", parent, access, mask, shift, signed=signed)

    class _ANA_OUT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("ANA_OUT", parent, access, address, signed)
            self.ANA_PHI_N_CAPTURE  =  self._ANA_PHI_N_CAPTURE(self,  Access.R,  0x0000FFFF,  0,   signed=False)
            self.ANA_PHI            =  self._ANA_PHI(          self,  Access.R,  0xFFFF0000,  16,  signed=False)

        class _ANA_PHI_N_CAPTURE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANA_PHI_N_CAPTURE", parent, access, mask, shift, signed=signed)

        class _ANA_PHI(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("ANA_PHI", parent, access, mask, shift, signed=signed)

    class _DIG_EVENTS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("DIG_EVENTS", parent, access, address, signed)
            self.INVALID_SIGNAL_EVENT  =  self._INVALID_SIGNAL_EVENT(self,  Access.RWC,  0x00000001,  0,  signed=False)

        class _INVALID_SIGNAL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INVALID_SIGNAL_EVENT", parent, access, mask, shift, signed=signed)

class _UART(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("UART", channel, block, width)
        self.CONTROL    =  self._CONTROL(  self,  Access.RW,   0x0340,  False)
        self.TIMEOUT    =  self._TIMEOUT(  self,  Access.RW,   0x0341,  False)
        self.STATUS     =  self._STATUS(   self,  Access.RW,   0x0342,  False)
        self.EVENTS     =  self._EVENTS(   self,  Access.RWC,  0x0343,  False)
        self.RTMI_CH_0  =  self._RTMI_CH_0(self,  Access.RW,   0x0344,  False)
        self.RTMI_CH_1  =  self._RTMI_CH_1(self,  Access.RW,   0x0345,  False)
        self.RTMI_CH_2  =  self._RTMI_CH_2(self,  Access.RW,   0x0346,  False)
        self.RTMI_CH_3  =  self._RTMI_CH_3(self,  Access.RW,   0x0347,  False)
        self.RTMI_CH_4  =  self._RTMI_CH_4(self,  Access.RW,   0x0348,  False)
        self.RTMI_CH_5  =  self._RTMI_CH_5(self,  Access.RW,   0x0349,  False)
        self.RTMI_CH_6  =  self._RTMI_CH_6(self,  Access.RW,   0x034A,  False)
        self.RTMI_CH_7  =  self._RTMI_CH_7(self,  Access.RW,   0x034B,  False)

    class _CONTROL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CONTROL", parent, access, address, signed)
            self.MANTISSA_LIMIT          =  self._MANTISSA_LIMIT(        self,  Access.RW,  0x00001FFF,  0,   signed=False)
            self.TIMEOUT_PRE_DIVIDER_EN  =  self._TIMEOUT_PRE_DIVIDER_EN(self,  Access.RW,  0x00010000,  16,  signed=False)
            self.AUTOBAUD_EN             =  self._AUTOBAUD_EN(           self,  Access.RW,  0x00040000,  18,  signed=False)
            self.RX_FILTER_EN            =  self._RX_FILTER_EN(          self,  Access.RW,  0x00080000,  19,  signed=False)
            self.NORMAL_CRC_EN           =  self._NORMAL_CRC_EN(         self,  Access.RW,  0x00100000,  20,  signed=False)
            self.RTMI_CRC_EN             =  self._RTMI_CRC_EN(           self,  Access.RW,  0x00200000,  21,  signed=False)
            self.RTMI_EN                 =  self._RTMI_EN(               self,  Access.RW,  0x00400000,  22,  signed=False)
            self.RTMI_SAMPLING           =  self._RTMI_SAMPLING(         self,  Access.RW,  0xFF000000,  24,  signed=False)

        class _MANTISSA_LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MANTISSA_LIMIT", parent, access, mask, shift, signed=signed)

        class _TIMEOUT_PRE_DIVIDER_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TIMEOUT_PRE_DIVIDER_EN", parent, access, mask, shift, signed=signed)

        class _AUTOBAUD_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AUTOBAUD_EN", parent, access, mask, shift, signed=signed)

        class _RX_FILTER_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RX_FILTER_EN", parent, access, mask, shift, signed=signed)

        class _NORMAL_CRC_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NORMAL_CRC_EN", parent, access, mask, shift, signed=signed)

        class _RTMI_CRC_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RTMI_CRC_EN", parent, access, mask, shift, signed=signed)

        class _RTMI_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RTMI_EN", parent, access, mask, shift, signed=signed)

        class _RTMI_SAMPLING(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RTMI_SAMPLING", parent, access, mask, shift, signed=signed)

    class _TIMEOUT(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("TIMEOUT", parent, access, address, signed)
            self.LIMIT    =  self._LIMIT(  self,  Access.RW,  0x0000FFFF,  0,   signed=False)
            self.COUNTER  =  self._COUNTER(self,  Access.R,   0xFFFF0000,  16,  signed=False)

        class _LIMIT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LIMIT", parent, access, mask, shift, signed=signed)

        class _COUNTER(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COUNTER", parent, access, mask, shift, signed=signed)

    class _STATUS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("STATUS", parent, access, address, signed)
            self.RX_ACTIVE       =  self._RX_ACTIVE(     self,  Access.R,   0x00000001,  0,  signed=False)
            self.TX_ACTIVE       =  self._TX_ACTIVE(     self,  Access.R,   0x00000004,  2,  signed=False)
            self.AUTOBAUD_VALID  =  self._AUTOBAUD_VALID(self,  Access.RW,  0x00000010,  4,  signed=False)

        class _RX_ACTIVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RX_ACTIVE", parent, access, mask, shift, signed=signed)

        class _TX_ACTIVE(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("TX_ACTIVE", parent, access, mask, shift, signed=signed)

        class _AUTOBAUD_VALID(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("AUTOBAUD_VALID", parent, access, mask, shift, signed=signed)

    class _EVENTS(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("EVENTS", parent, access, address, signed)
            self.UART_SYNC_FAIL_EVENT     =  self._UART_SYNC_FAIL_EVENT(   self,  Access.RWC,  0x00000001,  0,  signed=False)
            self.NOISY_DATA_EVENT         =  self._NOISY_DATA_EVENT(       self,  Access.RWC,  0x00000004,  2,  signed=False)
            self.RTMI_INTERRUPT_EVENT     =  self._RTMI_INTERRUPT_EVENT(   self,  Access.RWC,  0x00000008,  3,  signed=False)
            self.RX_IDLE_TIMEOUT_EVENT    =  self._RX_IDLE_TIMEOUT_EVENT(  self,  Access.RWC,  0x00000010,  4,  signed=False)
            self.INVALID_START_BIT_EVENT  =  self._INVALID_START_BIT_EVENT(self,  Access.RWC,  0x00000020,  5,  signed=False)
            self.INVALID_STOP_BIT_EVENT   =  self._INVALID_STOP_BIT_EVENT( self,  Access.RWC,  0x00000040,  6,  signed=False)
            self.INVALID_CRC_EVENT        =  self._INVALID_CRC_EVENT(      self,  Access.RWC,  0x00000080,  7,  signed=False)

        class _UART_SYNC_FAIL_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UART_SYNC_FAIL_EVENT", parent, access, mask, shift, signed=signed)

        class _NOISY_DATA_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("NOISY_DATA_EVENT", parent, access, mask, shift, signed=signed)

        class _RTMI_INTERRUPT_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RTMI_INTERRUPT_EVENT", parent, access, mask, shift, signed=signed)

        class _RX_IDLE_TIMEOUT_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RX_IDLE_TIMEOUT_EVENT", parent, access, mask, shift, signed=signed)

        class _INVALID_START_BIT_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INVALID_START_BIT_EVENT", parent, access, mask, shift, signed=signed)

        class _INVALID_STOP_BIT_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INVALID_STOP_BIT_EVENT", parent, access, mask, shift, signed=signed)

        class _INVALID_CRC_EVENT(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("INVALID_CRC_EVENT", parent, access, mask, shift, signed=signed)

    class _RTMI_CH_0(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RTMI_CH_0", parent, access, address, signed)
            self.CH_0_ADDR  =  self._CH_0_ADDR(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.CH_0_EN    =  self._CH_0_EN(  self,  Access.RW,  0x00010000,  16,  signed=False)

        class _CH_0_ADDR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_0_ADDR", parent, access, mask, shift, signed=signed)

        class _CH_0_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_0_EN", parent, access, mask, shift, signed=signed)

    class _RTMI_CH_1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RTMI_CH_1", parent, access, address, signed)
            self.CH_1_ADDR  =  self._CH_1_ADDR(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.CH_1_EN    =  self._CH_1_EN(  self,  Access.RW,  0x00010000,  16,  signed=False)

        class _CH_1_ADDR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_1_ADDR", parent, access, mask, shift, signed=signed)

        class _CH_1_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_1_EN", parent, access, mask, shift, signed=signed)

    class _RTMI_CH_2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RTMI_CH_2", parent, access, address, signed)
            self.CH_2_ADDR  =  self._CH_2_ADDR(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.CH_2_EN    =  self._CH_2_EN(  self,  Access.RW,  0x00010000,  16,  signed=False)

        class _CH_2_ADDR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_2_ADDR", parent, access, mask, shift, signed=signed)

        class _CH_2_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_2_EN", parent, access, mask, shift, signed=signed)

    class _RTMI_CH_3(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RTMI_CH_3", parent, access, address, signed)
            self.CH_3_ADDR  =  self._CH_3_ADDR(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.CH_3_EN    =  self._CH_3_EN(  self,  Access.RW,  0x00010000,  16,  signed=False)

        class _CH_3_ADDR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_3_ADDR", parent, access, mask, shift, signed=signed)

        class _CH_3_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_3_EN", parent, access, mask, shift, signed=signed)

    class _RTMI_CH_4(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RTMI_CH_4", parent, access, address, signed)
            self.CH_4_ADDR  =  self._CH_4_ADDR(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.CH_4_EN    =  self._CH_4_EN(  self,  Access.RW,  0x00010000,  16,  signed=False)

        class _CH_4_ADDR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_4_ADDR", parent, access, mask, shift, signed=signed)

        class _CH_4_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_4_EN", parent, access, mask, shift, signed=signed)

    class _RTMI_CH_5(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RTMI_CH_5", parent, access, address, signed)
            self.CH_5_ADDR  =  self._CH_5_ADDR(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.CH_5_EN    =  self._CH_5_EN(  self,  Access.RW,  0x00010000,  16,  signed=False)

        class _CH_5_ADDR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_5_ADDR", parent, access, mask, shift, signed=signed)

        class _CH_5_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_5_EN", parent, access, mask, shift, signed=signed)

    class _RTMI_CH_6(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RTMI_CH_6", parent, access, address, signed)
            self.CH_6_ADDR  =  self._CH_6_ADDR(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.CH_6_EN    =  self._CH_6_EN(  self,  Access.RW,  0x00010000,  16,  signed=False)

        class _CH_6_ADDR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_6_ADDR", parent, access, mask, shift, signed=signed)

        class _CH_6_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_6_EN", parent, access, mask, shift, signed=signed)

    class _RTMI_CH_7(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RTMI_CH_7", parent, access, address, signed)
            self.CH_7_ADDR  =  self._CH_7_ADDR(self,  Access.RW,  0x000003FF,  0,   signed=False)
            self.CH_7_EN    =  self._CH_7_EN(  self,  Access.RW,  0x00010000,  16,  signed=False)

        class _CH_7_ADDR(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_7_ADDR", parent, access, mask, shift, signed=signed)

        class _CH_7_EN(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CH_7_EN", parent, access, mask, shift, signed=signed)

class _IO_CONTROLLER(RegisterGroup):
    def __init__(self, channel, block, width):
        super().__init__("IO_CONTROLLER", channel, block, width)
        self.CONTROL     =  self._CONTROL(   self,  Access.RW,  0x0380,  False)
        self.COMMAND     =  self._COMMAND(   self,  Access.RW,  0x0381,  False)
        self.RESPONSE_0  =  self._RESPONSE_0(self,  Access.RW,  0x0382,  False)
        self.RESPONSE_1  =  self._RESPONSE_1(self,  Access.RW,  0x0383,  False)
        self.RESPONSE_2  =  self._RESPONSE_2(self,  Access.RW,  0x0384,  False)
        self.RESPONSE_3  =  self._RESPONSE_3(self,  Access.RW,  0x0385,  False)

    class _CONTROL(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("CONTROL", parent, access, address, signed)
            self.RESET  =  self._RESET(self,  Access.RW,  0x00000001,  0,  signed=False)

        class _RESET(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET", parent, access, mask, shift, signed=signed)

    class _COMMAND(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("COMMAND", parent, access, address, signed)
            self.COMMAND  =  self._COMMAND(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _COMMAND(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("COMMAND", parent, access, mask, shift, signed=signed)

    class _RESPONSE_0(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RESPONSE_0", parent, access, address, signed)
            self.RESPONSE_0  =  self._RESPONSE_0(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _RESPONSE_0(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESPONSE_0", parent, access, mask, shift, signed=signed)

    class _RESPONSE_1(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RESPONSE_1", parent, access, address, signed)
            self.RESPONSE_1  =  self._RESPONSE_1(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _RESPONSE_1(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESPONSE_1", parent, access, mask, shift, signed=signed)

    class _RESPONSE_2(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RESPONSE_2", parent, access, address, signed)
            self.RESPONSE_2  =  self._RESPONSE_2(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _RESPONSE_2(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESPONSE_2", parent, access, mask, shift, signed=signed)

    class _RESPONSE_3(Register):
        def __init__(self, parent, access, address, signed):
            super().__init__("RESPONSE_3", parent, access, address, signed)
            self.RESPONSE_3  =  self._RESPONSE_3(self,  Access.RW,  0xFFFFFFFF,  0,  signed=False)

        class _RESPONSE_3(Field):
            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESPONSE_3", parent, access, mask, shift, signed=signed)
