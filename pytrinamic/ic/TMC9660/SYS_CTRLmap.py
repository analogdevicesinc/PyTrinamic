################################################################################
# Copyright © 2025 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Field, Register


class SYS_CTRLMap:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)


class _ALL_REGISTERS(RegisterGroup):

    class _FAULT_STS(Register):

        class _BCK_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BCK_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BCK_SHORT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BCK_SHORT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT_TSD(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT_TSD", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT1_SHORT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT1_SHORT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT2_SHORT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT2_SHORT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHGP_OK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHGP_OK", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHGP_SHORT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHGP_SHORT", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VSA_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSA_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDD_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDD_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDDA_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDDA_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VCCIO_UVLO(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VCCIO_UVLO", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDO1_READY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDO1_READY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDO2_READY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDO2_READY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _V_EN_OK(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_EN_OK", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FAULT_STS", parent, access, address, block, signed)
            self.BCK_UVLO       =  self._BCK_UVLO(     self,  Access.R,  0x00000001,  0,   signed=False)
            self.BCK_SHORT      =  self._BCK_SHORT(    self,  Access.R,  0x00000002,  1,   signed=False)
            self.LDOEXT_TSD     =  self._LDOEXT_TSD(   self,  Access.R,  0x00000004,  2,   signed=False)
            self.LDOEXT1_SHORT  =  self._LDOEXT1_SHORT(self,  Access.R,  0x00000008,  3,   signed=False)
            self.LDOEXT2_SHORT  =  self._LDOEXT2_SHORT(self,  Access.R,  0x00000010,  4,   signed=False)
            self.CHGP_OK        =  self._CHGP_OK(      self,  Access.R,  0x00000020,  5,   signed=False)
            self.CHGP_SHORT     =  self._CHGP_SHORT(   self,  Access.R,  0x00000040,  6,   signed=False)
            self.VSA_UVLO       =  self._VSA_UVLO(     self,  Access.R,  0x00000080,  7,   signed=False)
            self.VDD_UVLO       =  self._VDD_UVLO(     self,  Access.R,  0x00000100,  8,   signed=False)
            self.VDDA_UVLO      =  self._VDDA_UVLO(    self,  Access.R,  0x00000200,  9,   signed=False)
            self.VCCIO_UVLO     =  self._VCCIO_UVLO(   self,  Access.R,  0x00000400,  10,  signed=False)
            self.LDO1_READY     =  self._LDO1_READY(   self,  Access.R,  0x00000800,  11,  signed=False)
            self.LDO2_READY     =  self._LDO2_READY(   self,  Access.R,  0x00001000,  12,  signed=False)
            self.V_EN_OK        =  self._V_EN_OK(      self,  Access.R,  0x00002000,  13,  signed=False)

    class _FAULT_R_INT(Register):

        class _BCK_UVLO_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BCK_UVLO_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BCK_SHORT_RE_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BCK_SHORT_RE_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT_TSD_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT_TSD_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT1_SHORT_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT1_SHORT_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT2_SHORT_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT2_SHORT_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHGP_OK_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHGP_OK_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHGP_SHORT_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHGP_SHORT_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VSA_UVLO_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSA_UVLO_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDD_UVLO_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDD_UVLO_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDDA_UVLO_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDDA_UVLO_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VCCIO_UVLO_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VCCIO_UVLO_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDO1_READY_RE_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDO1_READY_RE_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDO2_READY_RE_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDO2_READY_RE_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _V_EN_OK_RE_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_EN_OK_RE_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _UC_FAULT(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("UC_FAULT", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FAULT_R_INT", parent, access, address, block, signed)
            self.BCK_UVLO_LTC       =  self._BCK_UVLO_LTC(     self,  Access.RWC,  0x00000001,  0,   signed=False)
            self.BCK_SHORT_RE_LTC   =  self._BCK_SHORT_RE_LTC( self,  Access.RWC,  0x00000002,  1,   signed=False)
            self.LDOEXT_TSD_LTC     =  self._LDOEXT_TSD_LTC(   self,  Access.RWC,  0x00000004,  2,   signed=False)
            self.LDOEXT1_SHORT_LTC  =  self._LDOEXT1_SHORT_LTC(self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.LDOEXT2_SHORT_LTC  =  self._LDOEXT2_SHORT_LTC(self,  Access.RWC,  0x00000010,  4,   signed=False)
            self.CHGP_OK_LTC        =  self._CHGP_OK_LTC(      self,  Access.RWC,  0x00000020,  5,   signed=False)
            self.CHGP_SHORT_LTC     =  self._CHGP_SHORT_LTC(   self,  Access.RWC,  0x00000040,  6,   signed=False)
            self.VSA_UVLO_LTC       =  self._VSA_UVLO_LTC(     self,  Access.RWC,  0x00000080,  7,   signed=False)
            self.VDD_UVLO_LTC       =  self._VDD_UVLO_LTC(     self,  Access.RWC,  0x00000100,  8,   signed=False)
            self.VDDA_UVLO_LTC      =  self._VDDA_UVLO_LTC(    self,  Access.RWC,  0x00000200,  9,   signed=False)
            self.VCCIO_UVLO_LTC     =  self._VCCIO_UVLO_LTC(   self,  Access.RWC,  0x00000400,  10,  signed=False)
            self.LDO1_READY_RE_LTC  =  self._LDO1_READY_RE_LTC(self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.LDO2_READY_RE_LTC  =  self._LDO2_READY_RE_LTC(self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.V_EN_OK_RE_LTC     =  self._V_EN_OK_RE_LTC(   self,  Access.RWC,  0x00002000,  13,  signed=False)
            self.UC_FAULT           =  self._UC_FAULT(         self,  Access.RW,   0x00008000,  15,  signed=False)

    class _FAULT_R_ENA_F(Register):

        class _BCK_UVLO_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BCK_UVLO_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BCK_SHORT_RE_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BCK_SHORT_RE_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT_TSD_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT_TSD_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT1_SHORT_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT1_SHORT_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT2_SHORT_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT2_SHORT_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHGP_OK_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHGP_OK_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHGP_SHORT_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHGP_SHORT_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VSA_UVLO_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VSA_UVLO_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDD_UVLO_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDD_UVLO_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VDDA_UVLO_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VDDA_UVLO_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VCCIO_UVLO_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VCCIO_UVLO_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDO1_READY_RE_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDO1_READY_RE_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDO2_READY_RE_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDO2_READY_RE_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _V_EN_OK_RE_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_EN_OK_RE_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FAULT_R_ENA_F", parent, access, address, block, signed)
            self.BCK_UVLO_ENA_F       =  self._BCK_UVLO_ENA_F(     self,  Access.RW,  0x00000001,  0,   signed=False)
            self.BCK_SHORT_RE_ENA_F   =  self._BCK_SHORT_RE_ENA_F( self,  Access.RW,  0x00000002,  1,   signed=False)
            self.LDOEXT_TSD_ENA_F     =  self._LDOEXT_TSD_ENA_F(   self,  Access.RW,  0x00000004,  2,   signed=False)
            self.LDOEXT1_SHORT_ENA_F  =  self._LDOEXT1_SHORT_ENA_F(self,  Access.RW,  0x00000008,  3,   signed=False)
            self.LDOEXT2_SHORT_ENA_F  =  self._LDOEXT2_SHORT_ENA_F(self,  Access.RW,  0x00000010,  4,   signed=False)
            self.CHGP_OK_ENA_F        =  self._CHGP_OK_ENA_F(      self,  Access.RW,  0x00000020,  5,   signed=False)
            self.CHGP_SHORT_ENA_F     =  self._CHGP_SHORT_ENA_F(   self,  Access.RW,  0x00000040,  6,   signed=False)
            self.VSA_UVLO_ENA_F       =  self._VSA_UVLO_ENA_F(     self,  Access.RW,  0x00000080,  7,   signed=False)
            self.VDD_UVLO_ENA_F       =  self._VDD_UVLO_ENA_F(     self,  Access.RW,  0x00000100,  8,   signed=False)
            self.VDDA_UVLO_ENA_F      =  self._VDDA_UVLO_ENA_F(    self,  Access.RW,  0x00000200,  9,   signed=False)
            self.VCCIO_UVLO_ENA_F     =  self._VCCIO_UVLO_ENA_F(   self,  Access.RW,  0x00000400,  10,  signed=False)
            self.LDO1_READY_RE_ENA_F  =  self._LDO1_READY_RE_ENA_F(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.LDO2_READY_RE_ENA_F  =  self._LDO2_READY_RE_ENA_F(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.V_EN_OK_RE_ENA_F     =  self._V_EN_OK_RE_ENA_F(   self,  Access.RW,  0x00002000,  13,  signed=False)

    class _FAULT_F_INT(Register):

        class _V_EN_OK_FE_LTC(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_EN_OK_FE_LTC", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FAULT_F_INT", parent, access, address, block, signed)
            self.V_EN_OK_FE_LTC  =  self._V_EN_OK_FE_LTC(self,  Access.RWC,  0x00002000,  13,  signed=False)

    class _FAULT_F_ENA_F(Register):

        class _V_EN_OK_FE_ENA_F(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_EN_OK_FE_ENA_F", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FAULT_F_ENA_F", parent, access, address, block, signed)
            self.V_EN_OK_FE_ENA_F  =  self._V_EN_OK_FE_ENA_F(self,  Access.RW,  0x00002000,  13,  signed=False)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.FAULT_STS      =  self._FAULT_STS(    self,  Access.R,    0x0008,  block,  False)
        self.FAULT_R_INT    =  self._FAULT_R_INT(  self,  Access.RWC,  0x0009,  block,  False)
        self.FAULT_R_ENA_F  =  self._FAULT_R_ENA_F(self,  Access.RW,   0x000A,  block,  False)
        self.FAULT_F_INT    =  self._FAULT_F_INT(  self,  Access.RWC,  0x000C,  block,  False)
        self.FAULT_F_ENA_F  =  self._FAULT_F_ENA_F(self,  Access.RW,   0x000D,  block,  False)
