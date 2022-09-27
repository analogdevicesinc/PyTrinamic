from pytrinamic.features.solenoid import Solenoid

class SolenoidIC(Solenoid):
    """
    Solenoid feature implementation for ICs
    """

    __K_CDR = 36700

    __map_pwm_freq = {
        0: 100E3,
        1: 80E3,
        2: 60E3,
        3: 50E3,
        4: 40E3,
        5: 30E3,
        6: 25E3,
        7: 20E3,
        8: 15E3,
        9: 10E3,
        10: 7.5E3,
        11: 5E3,
        12: 2.5E3
    }

    __map_fsf = {
        0: 1.0,
        1: 2.0 / 3.0,
        2: 1.0 / 3.0
    }

    def __init__(self, eval_board, ic, axis):
        super().__init__(eval_board, axis)
        self._ic = ic

    def set_voltage_supply(self, u_supply):
        """
        Set supply voltage buffer.
        This is used to calculate real-world values.

        Parameters:
        u_supply: Supply voltage
        """
        self.__u_supply = u_supply

    def get_voltage_supply(self):
        """
        Get supply voltage buffer.
        This is used to calculate real-world values.

        Returns:
        Supply voltage
        """
        return self.__u_supply

    @staticmethod
    def __f_AC(pwm_freq, delta_phi):
        return ((pwm_freq * delta_phi) / (2**16))

    @staticmethod
    def __delta_phi(pwm_freq, f_AC):
        return ((f_AC * (2**16)) / pwm_freq)

    @staticmethod
    def __u_dc_value(u_dc_real, u_supply, vdr, cdr, fsf):
        if cdr:
            return ((u_dc_real * 0xFFFF) / (SolenoidIC.__K_CDR * 0.000075 * fsf))
        else:
            return ((u_dc_real * 0xFFFF) / (36 if vdr else u_supply))

    @staticmethod
    def __u_dc_real(u_dc_value, u_supply, vdr, cdr, fsf):
        if cdr:
            return ((SolenoidIC.__K_CDR * 0.000075 * fsf * u_dc_value) / 0xFFFF)
        else:
            return ((u_dc_value * (36 if vdr else u_supply)) / 0xFFFF)

    @staticmethod
    def __u_ac_value(u_ac_real, u_supply, vdr):
        return ((u_ac_real * 0xFFFF) / (36 if vdr else u_supply))

    @staticmethod
    def __u_ac_real(u_ac_value, u_supply, vdr):
        return ((u_ac_value * (36 if vdr else u_supply)) / 0xFFFF)
    
    def set_voltage_high(self, u_dc_h):
        """
        Set high DC voltage.
        This value is stored in the DC_H field of the IC.

        Parameters:
        u_dc_h: High DC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        cdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE) == 1)
        fsf = self.__map_fsf.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE), 1.0)
        print("U_DC_H {}".format(round(self.__u_dc_value(u_dc_h, self.__u_supply, vdr, cdr, fsf))))
        self._parent.write_axis_field(self._axis, self._ic.FIELD.DC_H, round(self.__u_dc_value(u_dc_h, self.__u_supply, vdr, cdr, fsf)))

    def get_voltage_high(self):
        """
        Get high DC voltage.
        This value is stored in the DC_H field of the IC.

        Returns:
        High DC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        cdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE) == 1)
        fsf = self.__map_fsf.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE), 1.0)
        return self.__u_dc_real(self._parent.read_axis_field(self._axis, self._ic.FIELD.DC_H), self.__u_supply, vdr, cdr, fsf)

    def set_voltage_low(self, u_dc_l):
        """
        Set low DC voltage.
        This value is stored in the DC_L field of the IC.

        Parameters:
        u_dc_l: Low DC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        cdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE) == 1)
        fsf = self.__map_fsf.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE), 1.0)
        self._parent.write_axis_field(self._axis, self._ic.FIELD.DC_L, round(self.__u_dc_value(u_dc_l, self.__u_supply, vdr, cdr, fsf)))

    def get_voltage_low(self):
        """
        Get low DC voltage.
        This value is stored in the DC_L field of the IC.

        Returns:
        Low DC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        cdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE) == 1)
        fsf = self.__map_fsf.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE), 1.0)
        return self.__u_dc_real(self._parent.read_axis_field(self._axis, self._ic.FIELD.DC_L), self.__u_supply, vdr, cdr, fsf)

    def set_voltage_low_high(self, u_dc_l2h):
        """
        Set low to high DC voltage.
        This value is stored in the DC_L2H field of the IC.

        Parameters:
        u_dc_l2h: Low to high DC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        cdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE) == 1)
        fsf = self.__map_fsf.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE), 1.0)
        self._parent.write_axis_field(self._axis, self._ic.FIELD.DC_L2H, round(self.__u_dc_value(u_dc_l2h, self.__u_supply, vdr, cdr, fsf)))

    def get_voltage_low_high(self):
        """
        Get low to high DC voltage.
        This value is stored in the DC_L2H field of the IC.

        Returns:
        Low to high DC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        cdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE) == 1)
        fsf = self.__map_fsf.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE), 1.0)
        return self.__u_dc_real(self._parent.read_axis_field(self._axis, self._ic.FIELD.DC_L2H), self.__u_supply, vdr, cdr, fsf)

    def set_voltage_high_low(self, u_dc_h2l):
        """
        Set high to low DC voltage.
        This value is stored in the DC_H2L field of the IC.

        Parameters:
        u_dc_h2l: High to low DC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        cdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE) == 1)
        fsf = self.__map_fsf.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE), 1.0)
        self._parent.write_axis_field(self._axis, self._ic.FIELD.DC_H2L, round(self.__u_dc_value(u_dc_h2l, self.__u_supply, vdr, cdr, fsf)))

    def get_voltage_high_low(self):
        """
        Get high to low DC voltage.
        This value is stored in the DC_H2L field of the IC.

        Returns:
        High to low DC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        cdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE) == 1)
        fsf = self.__map_fsf.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.CTRL_MODE), 1.0)
        return self.__u_dc_real(self._parent.read_axis_field(self._axis, self._ic.FIELD.DC_H2L), self.__u_supply, vdr, cdr, fsf)

    def set_frequency(self, u_ac_freq):
        """
        Set AC frequency.
        This value is stored in the DELTA_PHI field of the IC.
        F_AC = F_PWM_M * (DELTA_PHI/2^16)

        Parameters:
        u_ac_freq: AC frequency.
        """
        pwm_freq = self.__map_pwm_freq.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.F_PWM_M), 100E3)
        self._parent.write_axis_field(self._axis, self._ic.FIELD.DELTA_PHI, round(self.__delta_phi(pwm_freq, u_ac_freq)))

    def get_frequency(self):
        """
        Get AC frequency.
        This value is stored in the DELTA_PHI field of the IC.
        F_AC = F_PWM_M * (DELTA_PHI/2^16)

        Returns:
        AC frequency.
        """
        pwm_freq = self.__map_pwm_freq.get(self._parent.read_axis_field(self._axis, self._ic.FIELD.F_PWM_M), 100E3)
        return self.__f_AC(pwm_freq, self._parent.read_axis_field(self._axis, self._ic.FIELD.DELTA_PHI))

    def set_voltage_ac(self, u_ac):
        """
        Set AC voltage.
        This value is stored in the U_AC field of the IC.

        Parameters:
        u_ac: AC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        self._parent.write_axis_field(self._axis, self._ic.FIELD.U_AC, round(self.__u_ac_value(u_ac, self.__u_supply, vdr)))

    def get_voltage_ac(self):
        """
        Get AC voltage.

        Returns:
        AC voltage.
        """
        vdr = (self._parent.read_axis_field(self._axis, self._ic.FIELD.VDR_NDUTY) == 1)
        return self.__u_ac_real(self._parent.read_axis_field(self._axis, self._ic.FIELD.U_AC), self.__u_supply, vdr)

    # Properties
    u_supply = property(get_voltage_supply, set_voltage_supply)
    u_dc_h = property(get_voltage_high, set_voltage_high)
    u_dc_l = property(get_voltage_low, set_voltage_low)
    u_dc_l2h = property(get_voltage_low_high, set_voltage_low_high)
    u_dc_h2l = property(get_voltage_high_low, set_voltage_high_low)
    u_ac = property(get_voltage_ac, set_voltage_ac)
    f_ac = property(get_frequency, set_frequency)

    def __str__(self):
        return "{} {}".format(
            "Solenoid",
            {
                "u_supply": self.u_supply,
                "u_dc_h": self.u_dc_h,
                "u_dc_l": self.u_dc_l,
                "u_dc_l2h": self.u_dc_l2h,
                "u_dc_h2l": self.u_dc_h2l,
                "u_ac": self.u_ac,
                "f_ac": self.f_ac
            }
        )
