'''
Created on 02.01.2019

@author: ed
'''

from PyTrinamic.ic.tmc_ic import tmc_ic
from PyTrinamic.ic.TMC5130.TMC5130_register import TMC5130_register
from PyTrinamic.ic.TMC5130.TMC5130_register_variant import TMC5130_register_variant
#from PyTrinamic.ic.TMC5130.TMC5130_fields import TMC5130_fields
from PyTrinamic.helpers import TMC_helpers
import struct

class TMC5130(tmc_ic):

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
    def __init__(self, connection=None, comm=None, slave=0, registers=True, variants=True, fields=True):
        super().__init__()

        if(registers):
            from PyTrinamic.ic.TMC5130.TMC5130_register import TMC5130_registers
            self.registers = TMC5130_registers

        if(variants):
            from PyTrinamic.ic.TMC5130.TMC5130_register_variant import TMC5130_register_variants
            self.variants   = TMC5130_register_variants

        if(fields):
            from PyTrinamic.ic.TMC5130.TMC5130_fields import TMC5130_fields
            self.fields     = TMC5130_fields

        self.__connection = connection
        self.__comm = comm if (comm is not None) else TMC5130.COMM_SPI
        self.__slave = slave

        self.MOTORS     = 2

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

    def writeRegister(self, address, value):
        buf = bytearray(0)
        if(self.__comm == self.COMM_UART):
            buf = bytearray(struct.pack(self.__STRUCT_REGISTER_UART_WRITE, self.__UART_SYNC, self.__slave, address | self.__WRITE_BIT, value, 0))
            TMC5130.crc(buf)
        elif(self.__comm == self.COMM_SPI):
            buf = bytearray(struct.pack(self.__STRUCT_REGISTER_SPI, address | self.__WRITE_BIT, value))
        self.__connection.send(buf)

    def readRegister(self, address, signed=False):
        value = 0
        if(self.__comm == self.COMM_UART):
            buf = bytearray(struct.pack(self.__STRUCT_REGISTER_UART_READ, self.__UART_SYNC, self.__slave, address, 0))
            TMC5130.crc(buf)
            self.__connection.send(buf)
            buf = self.__connection.recv(8)
            value = struct.unpack(self.__STRUCT_REGISTER_UART_WRITE, buf)[3]
        elif(self.__comm == self.COMM_SPI):
            buf = bytearray(struct.pack(self.__STRUCT_REGISTER_SPI, address, 0))
            self.__connection.send_recv(buf, buf)
            value = struct.unpack(self.__STRUCT_REGISTER_SPI, buf)[1]
        return TMC_helpers.toSigned32(value) if signed else value

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
