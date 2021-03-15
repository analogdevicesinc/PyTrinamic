'''
Created on 20.09.2019

@author: JM
'''

from PyTrinamic.ic.tmc_ic import tmc_ic
from PyTrinamic.features.StallGuard2IC import StallGuard2IC
from PyTrinamic.features.LinearRampIC import LinearRampIC
from PyTrinamic.features.MotorControl import MotorControl
from PyTrinamic.helpers import TMC_helpers

class TMC5072(tmc_ic, StallGuard2IC, LinearRampIC, MotorControl):
    """
    Class for the TMC5072 IC
    """
    def __init__(self, module=None, channel=0, registers=True, variants=True, fields=True):
        tmc_ic.__init__(self, module, channel)

        if(registers):
            from PyTrinamic.ic.TMC5072.TMC5072_registers import TMC5072_registers
            self.registers = TMC5072_registers

        if(variants):
            from PyTrinamic.ic.TMC5072.TMC5072_register_variants import TMC5072_register_variants
            self.variants   = TMC5072_register_variants

        if(fields):
            from PyTrinamic.ic.TMC5072.TMC5072_fields import TMC5072_fields
            self.fields     = TMC5072_fields

        self.MOTORS = 2

    def showChipInfo(self):
        print("TMC5072 chip info: The TMC5072 is a dual high performance stepper motor controller and driver IC with serial communication interfaces. Voltage supply: 4,75 - 26V")

    def _address_axis(self, address, axis):
        if(0x10 <= address <= 0x11):
            address += (0x08 * axis)
        elif(0x20 <= address <= 0x3C):
            address += (0x20 * axis)
        elif(0x6A <= address <= 0x6F):
            address += (0x10 * axis)
        return address

    # Motion Control functions
    def rotate(self, axis, value):
        if not(0 <= axis < self.MOTORS):
            raise ValueError

        self.writeRegister(self.registers.AMAX_M1, 1000, axis=axis)
        if value >= 0:
            self.writeRegister(self.registers.VMAX_M1, value, axis=axis)
            self.writeRegister(self.registers.RAMPMODE_M1, 1, axis=axis)
        else:
            self.writeRegister(self.registers.VMAX_M1, -value, axis=axis)
            self.writeRegister(self.registers.RAMPMODE_M1, 2, axis=axis)

    def stop(self, axis):
        self.rotate(axis, 0)

    def moveTo(self, axis, position, velocity):
        if not(0 <= axis < self.MOTORS):
            raise ValueError

        self.writeRegister(self.registers.RAMPMODE_M1, 0, axis=axis)
        if velocity != 0:
            self.writeRegister(self.registers.VMAX_M1, velocity, axis=axis)
        self.writeRegister(self.registers.XTARGET_M1, position, axis=axis)
