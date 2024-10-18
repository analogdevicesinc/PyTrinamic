################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

# This file was generated. Do not modify it manually!

from pytrinamic.ic import Access, RegisterGroup, Field, Register


class SYS_CTRLMap:

    def __init__(self, block=None):
        self.ALL_REGISTERS = _ALL_REGISTERS(block)




class _ALL_REGISTERS(RegisterGroup):

    class _SW_RESET(Register):

        class _RESET(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("RESET", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _OTHER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OTHER", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CPU(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CPU", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SW_RESET", parent, access, address, block, signed)
            self.RESET  =  self._RESET(self,  Access.RW,  0x0000000F,  0,  signed=False)
            self.OTHER  =  self._OTHER(self,  Access.RW,  0x00000040,  6,  signed=False)
            self.CPU    =  self._CPU(self,    Access.RW,  0x00000080,  7,  signed=False)

    class _SW_RESET_STATUS(Register):

        class _OTHER(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("OTHER", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CPU(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CPU", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SW_RESET_STATUS", parent, access, address, block, signed)
            self.OTHER  =  self._OTHER(self,  Access.RWC,  0x00000040,  6,  signed=False)
            self.CPU    =  self._CPU(self,    Access.RWC,  0x00000080,  7,  signed=False)

    class _PMU_CTRL(Register):

        class _CP_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CP_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDO_ENABLE(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDO_ENABLE", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VEXT1_CNFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEXT1_CNFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VEXT2_CNFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEXT2_CNFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VEXT1_SS_CNFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEXT1_SS_CNFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _VEXT2_SS_CNFG(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("VEXT2_SS_CNFG", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _FRC_CP_SHTDW(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FRC_CP_SHTDW", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("PMU_CTRL", parent, access, address, block, signed)
            self.CP_ENABLE      =  self._CP_ENABLE(self,      Access.RW,  0x00000001,  0,   signed=False)
            self.LDO_ENABLE     =  self._LDO_ENABLE(self,     Access.RW,  0x00000002,  1,   signed=False)
            self.VEXT1_CNFG     =  self._VEXT1_CNFG(self,     Access.RW,  0x0000000C,  2,   signed=False)
            self.VEXT2_CNFG     =  self._VEXT2_CNFG(self,     Access.RW,  0x00000030,  4,   signed=False)
            self.VEXT1_SS_CNFG  =  self._VEXT1_SS_CNFG(self,  Access.RW,  0x000000C0,  6,   signed=False)
            self.VEXT2_SS_CNFG  =  self._VEXT2_SS_CNFG(self,  Access.RW,  0x00000300,  8,   signed=False)
            self.FRC_CP_SHTDW   =  self._FRC_CP_SHTDW(self,   Access.RW,  0x00000400,  10,  signed=False)

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
            self.BCK_UVLO       =  self._BCK_UVLO(self,       Access.R,  0x00000001,  0,   signed=False)
            self.BCK_SHORT      =  self._BCK_SHORT(self,      Access.R,  0x00000002,  1,   signed=False)
            self.LDOEXT_TSD     =  self._LDOEXT_TSD(self,     Access.R,  0x00000004,  2,   signed=False)
            self.LDOEXT1_SHORT  =  self._LDOEXT1_SHORT(self,  Access.R,  0x00000008,  3,   signed=False)
            self.LDOEXT2_SHORT  =  self._LDOEXT2_SHORT(self,  Access.R,  0x00000010,  4,   signed=False)
            self.CHGP_OK        =  self._CHGP_OK(self,        Access.R,  0x00000020,  5,   signed=False)
            self.CHGP_SHORT     =  self._CHGP_SHORT(self,     Access.R,  0x00000040,  6,   signed=False)
            self.VSA_UVLO       =  self._VSA_UVLO(self,       Access.R,  0x00000080,  7,   signed=False)
            self.VDD_UVLO       =  self._VDD_UVLO(self,       Access.R,  0x00000100,  8,   signed=False)
            self.VDDA_UVLO      =  self._VDDA_UVLO(self,      Access.R,  0x00000200,  9,   signed=False)
            self.VCCIO_UVLO     =  self._VCCIO_UVLO(self,     Access.R,  0x00000400,  10,  signed=False)
            self.LDO1_READY     =  self._LDO1_READY(self,     Access.R,  0x00000800,  11,  signed=False)
            self.LDO2_READY     =  self._LDO2_READY(self,     Access.R,  0x00001000,  12,  signed=False)
            self.V_EN_OK        =  self._V_EN_OK(self,        Access.R,  0x00002000,  13,  signed=False)

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
            self.BCK_UVLO_LTC       =  self._BCK_UVLO_LTC(self,       Access.RWC,  0x00000001,  0,   signed=False)
            self.BCK_SHORT_RE_LTC   =  self._BCK_SHORT_RE_LTC(self,   Access.RWC,  0x00000002,  1,   signed=False)
            self.LDOEXT_TSD_LTC     =  self._LDOEXT_TSD_LTC(self,     Access.RWC,  0x00000004,  2,   signed=False)
            self.LDOEXT1_SHORT_LTC  =  self._LDOEXT1_SHORT_LTC(self,  Access.RWC,  0x00000008,  3,   signed=False)
            self.LDOEXT2_SHORT_LTC  =  self._LDOEXT2_SHORT_LTC(self,  Access.RWC,  0x00000010,  4,   signed=False)
            self.CHGP_OK_LTC        =  self._CHGP_OK_LTC(self,        Access.RWC,  0x00000020,  5,   signed=False)
            self.CHGP_SHORT_LTC     =  self._CHGP_SHORT_LTC(self,     Access.RWC,  0x00000040,  6,   signed=False)
            self.VSA_UVLO_LTC       =  self._VSA_UVLO_LTC(self,       Access.RWC,  0x00000080,  7,   signed=False)
            self.VDD_UVLO_LTC       =  self._VDD_UVLO_LTC(self,       Access.RWC,  0x00000100,  8,   signed=False)
            self.VDDA_UVLO_LTC      =  self._VDDA_UVLO_LTC(self,      Access.RWC,  0x00000200,  9,   signed=False)
            self.VCCIO_UVLO_LTC     =  self._VCCIO_UVLO_LTC(self,     Access.RWC,  0x00000400,  10,  signed=False)
            self.LDO1_READY_RE_LTC  =  self._LDO1_READY_RE_LTC(self,  Access.RWC,  0x00000800,  11,  signed=False)
            self.LDO2_READY_RE_LTC  =  self._LDO2_READY_RE_LTC(self,  Access.RWC,  0x00001000,  12,  signed=False)
            self.V_EN_OK_RE_LTC     =  self._V_EN_OK_RE_LTC(self,     Access.RWC,  0x00002000,  13,  signed=False)
            self.UC_FAULT           =  self._UC_FAULT(self,           Access.RW,   0x00008000,  15,  signed=False)

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
            self.BCK_UVLO_ENA_F       =  self._BCK_UVLO_ENA_F(self,       Access.RW,  0x00000001,  0,   signed=False)
            self.BCK_SHORT_RE_ENA_F   =  self._BCK_SHORT_RE_ENA_F(self,   Access.RW,  0x00000002,  1,   signed=False)
            self.LDOEXT_TSD_ENA_F     =  self._LDOEXT_TSD_ENA_F(self,     Access.RW,  0x00000004,  2,   signed=False)
            self.LDOEXT1_SHORT_ENA_F  =  self._LDOEXT1_SHORT_ENA_F(self,  Access.RW,  0x00000008,  3,   signed=False)
            self.LDOEXT2_SHORT_ENA_F  =  self._LDOEXT2_SHORT_ENA_F(self,  Access.RW,  0x00000010,  4,   signed=False)
            self.CHGP_OK_ENA_F        =  self._CHGP_OK_ENA_F(self,        Access.RW,  0x00000020,  5,   signed=False)
            self.CHGP_SHORT_ENA_F     =  self._CHGP_SHORT_ENA_F(self,     Access.RW,  0x00000040,  6,   signed=False)
            self.VSA_UVLO_ENA_F       =  self._VSA_UVLO_ENA_F(self,       Access.RW,  0x00000080,  7,   signed=False)
            self.VDD_UVLO_ENA_F       =  self._VDD_UVLO_ENA_F(self,       Access.RW,  0x00000100,  8,   signed=False)
            self.VDDA_UVLO_ENA_F      =  self._VDDA_UVLO_ENA_F(self,      Access.RW,  0x00000200,  9,   signed=False)
            self.VCCIO_UVLO_ENA_F     =  self._VCCIO_UVLO_ENA_F(self,     Access.RW,  0x00000400,  10,  signed=False)
            self.LDO1_READY_RE_ENA_F  =  self._LDO1_READY_RE_ENA_F(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.LDO2_READY_RE_ENA_F  =  self._LDO2_READY_RE_ENA_F(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.V_EN_OK_RE_ENA_F     =  self._V_EN_OK_RE_ENA_F(self,     Access.RW,  0x00002000,  13,  signed=False)

    class _FAULT_R_ENA_I(Register):

        class _LDOEXT_TSD_ENA_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT_TSD_ENA_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT1_SHORT_ENA_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT1_SHORT_ENA_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDOEXT2_SHORT_ENA_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDOEXT2_SHORT_ENA_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHGP_OK_ENA_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHGP_OK_ENA_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CHGP_SHORT_ENA_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CHGP_SHORT_ENA_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDO1_READY_RE_ENA_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDO1_READY_RE_ENA_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _LDO2_READY_RE_ENA_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("LDO2_READY_RE_ENA_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _V_EN_OK_RE_ENA_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_EN_OK_RE_ENA_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FAULT_R_ENA_I", parent, access, address, block, signed)
            self.LDOEXT_TSD_ENA_I     =  self._LDOEXT_TSD_ENA_I(self,     Access.RW,  0x00000004,  2,   signed=False)
            self.LDOEXT1_SHORT_ENA_I  =  self._LDOEXT1_SHORT_ENA_I(self,  Access.RW,  0x00000008,  3,   signed=False)
            self.LDOEXT2_SHORT_ENA_I  =  self._LDOEXT2_SHORT_ENA_I(self,  Access.RW,  0x00000010,  4,   signed=False)
            self.CHGP_OK_ENA_I        =  self._CHGP_OK_ENA_I(self,        Access.RW,  0x00000020,  5,   signed=False)
            self.CHGP_SHORT_ENA_I     =  self._CHGP_SHORT_ENA_I(self,     Access.RW,  0x00000040,  6,   signed=False)
            self.LDO1_READY_RE_ENA_I  =  self._LDO1_READY_RE_ENA_I(self,  Access.RW,  0x00000800,  11,  signed=False)
            self.LDO2_READY_RE_ENA_I  =  self._LDO2_READY_RE_ENA_I(self,  Access.RW,  0x00001000,  12,  signed=False)
            self.V_EN_OK_RE_ENA_I     =  self._V_EN_OK_RE_ENA_I(self,     Access.RW,  0x00002000,  13,  signed=False)

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

    class _FAULT_F_ENA_I(Register):

        class _V_EN_OK_FE_ENA_I(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("V_EN_OK_FE_ENA_I", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FAULT_F_ENA_I", parent, access, address, block, signed)
            self.V_EN_OK_FE_ENA_I  =  self._V_EN_OK_FE_ENA_I(self,  Access.RW,  0x00002000,  13,  signed=False)

    class _FREQ_TRIM_VAON(Register):

        class _FREQ_TRIM_VAON(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("FREQ_TRIM_VAON", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("FREQ_TRIM_VAON", parent, access, address, block, signed)
            self.FREQ_TRIM_VAON  =  self._FREQ_TRIM_VAON(self,  Access.R,  0x000000FF,  0,  signed=False)

    class _IZTAT_TRIM_VAON(Register):

        class _IZTAT_TRIM_VAON(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("IZTAT_TRIM_VAON", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("IZTAT_TRIM_VAON", parent, access, address, block, signed)
            self.IZTAT_TRIM_VAON  =  self._IZTAT_TRIM_VAON(self,  Access.R,  0x0000003F,  0,  signed=False)

    class _SW_LVL_OTP(Register):

        class _SW_LVL_OTP(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SW_LVL_OTP", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _BOOTLOADER_BYPASS(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("BOOTLOADER_BYPASS", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("SW_LVL_OTP", parent, access, address, block, signed)
            self.SW_LVL_OTP         =  self._SW_LVL_OTP(self,         Access.R,  0x00000007,  0,  signed=False)
            self.BOOTLOADER_BYPASS  =  self._BOOTLOADER_BYPASS(self,  Access.R,  0x000000F0,  4,  signed=False)

    class _READBACK_OTP(Register):

        class _MTP_READY(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MTP_READY", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _MTP_READY_CLR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("MTP_READY_CLR", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CP_READY_CLR(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CP_READY_CLR", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("READBACK_OTP", parent, access, address, block, signed)
            self.MTP_READY      =  self._MTP_READY(self,      Access.R,    0x00000001,  0,  signed=False)
            self.MTP_READY_CLR  =  self._MTP_READY_CLR(self,  Access.RWC,  0x00000002,  1,  signed=False)
            self.CP_READY_CLR   =  self._CP_READY_CLR(self,   Access.RWC,  0x00000004,  2,  signed=False)

    class _ADC_CFG0(Register):

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

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_CFG0", parent, access, address, block, signed)
            self.OFSL0  =  self._OFSL0(self,  Access.R,  0x0000003F,  0,   signed=False)
            self.OFSM0  =  self._OFSM0(self,  Access.R,  0x00000FC0,  6,   signed=False)
            self.OFSH0  =  self._OFSH0(self,  Access.R,  0x0003F000,  12,  signed=False)

    class _ADC_CFG1(Register):

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

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_CFG1", parent, access, address, block, signed)
            self.OFSL1  =  self._OFSL1(self,  Access.R,  0x0000003F,  0,   signed=False)
            self.OFSM1  =  self._OFSM1(self,  Access.R,  0x00000FC0,  6,   signed=False)
            self.OFSH1  =  self._OFSH1(self,  Access.R,  0x0003F000,  12,  signed=False)

    class _ADC_CFG2(Register):

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

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_CFG2", parent, access, address, block, signed)
            self.OFSL2  =  self._OFSL2(self,  Access.R,  0x0000003F,  0,   signed=False)
            self.OFSM2  =  self._OFSM2(self,  Access.R,  0x00000FC0,  6,   signed=False)
            self.OFSH2  =  self._OFSH2(self,  Access.R,  0x0003F000,  12,  signed=False)

    class _ADC_CFG3(Register):

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

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_CFG3", parent, access, address, block, signed)
            self.OFSL3  =  self._OFSL3(self,  Access.R,  0x0000003F,  0,   signed=False)
            self.OFSM3  =  self._OFSM3(self,  Access.R,  0x00000FC0,  6,   signed=False)
            self.OFSH3  =  self._OFSH3(self,  Access.R,  0x0003F000,  12,  signed=False)

    class _ADC_CFG4(Register):

        class _SKIP_OFSH_AZ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_OFSH_AZ", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_CMRN_AZ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_CMRN_AZ", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_OFSL_AZ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_OFSL_AZ", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _SKIP_OFSM_AZ(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("SKIP_OFSM_AZ", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CONFIG_VX2_TUNE_ADC0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CONFIG_VX2_TUNE_ADC0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CONFIG_VX2_TUNE_ADC1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CONFIG_VX2_TUNE_ADC1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CONFIG_VX2_TUNE_ADC2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CONFIG_VX2_TUNE_ADC2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CONFIG_VX2_TUNE_ADC3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CONFIG_VX2_TUNE_ADC3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_CFG4", parent, access, address, block, signed)
            self.SKIP_OFSH_AZ          =  self._SKIP_OFSH_AZ(self,          Access.R,  0x00000001,  0,   signed=False)
            self.SKIP_CMRN_AZ          =  self._SKIP_CMRN_AZ(self,          Access.R,  0x00000002,  1,   signed=False)
            self.SKIP_OFSL_AZ          =  self._SKIP_OFSL_AZ(self,          Access.R,  0x00000004,  2,   signed=False)
            self.SKIP_OFSM_AZ          =  self._SKIP_OFSM_AZ(self,          Access.R,  0x00000008,  3,   signed=False)
            self.CONFIG_VX2_TUNE_ADC0  =  self._CONFIG_VX2_TUNE_ADC0(self,  Access.R,  0x000003F0,  4,   signed=False)
            self.CONFIG_VX2_TUNE_ADC1  =  self._CONFIG_VX2_TUNE_ADC1(self,  Access.R,  0x0000FC00,  10,  signed=False)
            self.CONFIG_VX2_TUNE_ADC2  =  self._CONFIG_VX2_TUNE_ADC2(self,  Access.R,  0x003F0000,  16,  signed=False)
            self.CONFIG_VX2_TUNE_ADC3  =  self._CONFIG_VX2_TUNE_ADC3(self,  Access.R,  0x0FC00000,  22,  signed=False)

    class _ADC_CFG5(Register):

        class _CMRN_DAC0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRN_DAC0", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRP_DAC0(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRP_DAC0", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_CFG5", parent, access, address, block, signed)
            self.CMRN_DAC0  =  self._CMRN_DAC0(self,  Access.R,  0x000FF000,  12,  signed=False)
            self.CMRP_DAC0  =  self._CMRP_DAC0(self,  Access.R,  0x0FF00000,  20,  signed=False)

    class _ADC_CFG6(Register):

        class _CMRN_DAC1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRN_DAC1", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRP_DAC1(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRP_DAC1", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_CFG6", parent, access, address, block, signed)
            self.CMRN_DAC1  =  self._CMRN_DAC1(self,  Access.R,  0x000FF000,  12,  signed=False)
            self.CMRP_DAC1  =  self._CMRP_DAC1(self,  Access.R,  0x0FF00000,  20,  signed=False)

    class _ADC_CFG7(Register):

        class _CMRN_DAC2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRN_DAC2", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRP_DAC2(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRP_DAC2", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_CFG7", parent, access, address, block, signed)
            self.CMRN_DAC2  =  self._CMRN_DAC2(self,  Access.R,  0x000FF000,  12,  signed=False)
            self.CMRP_DAC2  =  self._CMRP_DAC2(self,  Access.R,  0x0FF00000,  20,  signed=False)

    class _ADC_CFG8(Register):

        class _CMRN_DAC3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRN_DAC3", parent, access, mask, shift, signed=signed)

                self.choice = None

        class _CMRP_DAC3(Field):

            def __init__(self, parent, access, mask, shift, signed):
                super().__init__("CMRP_DAC3", parent, access, mask, shift, signed=signed)

                self.choice = None

        def __init__(self, parent, access, address, block, signed):
            super().__init__("ADC_CFG8", parent, access, address, block, signed)
            self.CMRN_DAC3  =  self._CMRN_DAC3(self,  Access.R,  0x000FF000,  12,  signed=False)
            self.CMRP_DAC3  =  self._CMRP_DAC3(self,  Access.R,  0x0FF00000,  20,  signed=False)

    def __init__(self, block=None):
        super().__init__("ALL_REGISTERS", block)
        self.SW_RESET         =  self._SW_RESET(self,         Access.RW,   0x0000,  block,  False)
        self.SW_RESET_STATUS  =  self._SW_RESET_STATUS(self,  Access.RWC,  0x0001,  block,  False)
        self.PMU_CTRL         =  self._PMU_CTRL(self,         Access.RW,   0x0004,  block,  False)
        self.FAULT_STS        =  self._FAULT_STS(self,        Access.R,    0x0008,  block,  False)
        self.FAULT_R_INT      =  self._FAULT_R_INT(self,      Access.RWC,  0x0009,  block,  False)
        self.FAULT_R_ENA_F    =  self._FAULT_R_ENA_F(self,    Access.RW,   0x000A,  block,  False)
        self.FAULT_R_ENA_I    =  self._FAULT_R_ENA_I(self,    Access.RW,   0x000B,  block,  False)
        self.FAULT_F_INT      =  self._FAULT_F_INT(self,      Access.RWC,  0x000C,  block,  False)
        self.FAULT_F_ENA_F    =  self._FAULT_F_ENA_F(self,    Access.RW,   0x000D,  block,  False)
        self.FAULT_F_ENA_I    =  self._FAULT_F_ENA_I(self,    Access.RW,   0x000E,  block,  False)
        self.FREQ_TRIM_VAON   =  self._FREQ_TRIM_VAON(self,   Access.R,    0x0010,  block,  False)
        self.IZTAT_TRIM_VAON  =  self._IZTAT_TRIM_VAON(self,  Access.R,    0x0011,  block,  False)
        self.SW_LVL_OTP       =  self._SW_LVL_OTP(self,       Access.R,    0x0012,  block,  False)
        self.READBACK_OTP     =  self._READBACK_OTP(self,     Access.RWC,  0x0013,  block,  False)
        self.ADC_CFG0         =  self._ADC_CFG0(self,         Access.R,    0x0014,  block,  False)
        self.ADC_CFG1         =  self._ADC_CFG1(self,         Access.R,    0x0015,  block,  False)
        self.ADC_CFG2         =  self._ADC_CFG2(self,         Access.R,    0x0016,  block,  False)
        self.ADC_CFG3         =  self._ADC_CFG3(self,         Access.R,    0x0017,  block,  False)
        self.ADC_CFG4         =  self._ADC_CFG4(self,         Access.R,    0x0018,  block,  False)
        self.ADC_CFG5         =  self._ADC_CFG5(self,         Access.R,    0x0019,  block,  False)
        self.ADC_CFG6         =  self._ADC_CFG6(self,         Access.R,    0x001A,  block,  False)
        self.ADC_CFG7         =  self._ADC_CFG7(self,         Access.R,    0x001B,  block,  False)
        self.ADC_CFG8         =  self._ADC_CFG8(self,         Access.R,    0x001C,  block,  False)

