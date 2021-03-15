'''
Created on 02.01.2019

@author: ed
'''

from PyTrinamic.ic.tmc_ic import tmc_ic
from PyTrinamic.features.StallGuard2IC import StallGuard2IC
from PyTrinamic.features.LinearRampIC import LinearRampIC
from PyTrinamic.features.MotorControl import MotorControl
from PyTrinamic.helpers import TMC_helpers
import struct

class TMC5130(tmc_ic, StallGuard2IC, LinearRampIC, MotorControl):

    COMM_UART = 0
    COMM_SPI = 1

    __STRUCT_REGISTER_SPI = ">BI"
    __STRUCT_REGISTER_UART_WRITE = ">BBBIB"
    __STRUCT_REGISTER_UART_READ = ">BBBB"
    __UART_SYNC = 0b00000101
    __WRITE_BIT = 0x80
    __CRC_POLY = 0b100000111

    """
    Class for the TMC5130 IC
    """
    def __init__(self, module=None, channel=0, registers=True, variants=True, fields=True):
        tmc_ic.__init__(self, module, channel)

        if(registers):
            from PyTrinamic.ic.TMC5130.TMC5130_register import TMC5130_registers
            self.registers = TMC5130_registers

        if(variants):
            from PyTrinamic.ic.TMC5130.TMC5130_register_variant import TMC5130_register_variants
            self.variants   = TMC5130_register_variants

        if(fields):
            from PyTrinamic.ic.TMC5130.TMC5130_fields import TMC5130_fields
            self.fields     = TMC5130_fields

        self.MOTORS = 1

    @staticmethod
    def crc(buf):
        for b in buf[:-1]:
            current = b
            for i in range(0, 8):
                if((buf[-1] >> 7) ^ (current & 0x01)):
                    buf[-1] = (buf[-1] << 1) ^ 0x07
                else:
                    buf[-1] = buf[-1] << 1
                current = current >> 1


    def showChipInfo(self):
        print("TMC5130 chip info: The TMC5130/A is a high-performance stepper motor controller and driver IC with serial communication interfaces. Voltage supply: 4,75 - 46V")

    # Motion Control functions
    def rotate(self, motor, velocity):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        if velocity >= 0:
            self.writeRegister(self.registers.VMAX, velocity)
            self.writeRegister(self.registers.RAMPMODE, 1)
        else:
            self.writeRegister(self.registers.VMAX, -velocity)
            self.writeRegister(self.registers.RAMPMODE, 2)

    def stop(self, motor):
        self.rotate(motor, 0)

    def moveTo(self, motor, position):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        self.writeRegister(self.registers.RAMPMODE, 0)

        self.writeRegister(self.registers.XTARGET, position)

    def moveBy(self, motor, distance):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        position = self.readRegister(self.registers.XACTUAL, signed=True)

        self.moveTo(motor, position + distance)

        return position + distance

    def get_pin_state(self):
        pass
