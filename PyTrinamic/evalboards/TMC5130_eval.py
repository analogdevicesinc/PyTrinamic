'''
Created on 09.01.2019

@author: LK, ED, LH
'''

from PyTrinamic.ic.TMC5130.TMC5130 import TMC5130
from PyTrinamic.evalboards.tmc_eval import tmc_eval
from PyTrinamic.features.StallGuard2Module import StallGuard2Module
from PyTrinamic.features.LinearRampModule import LinearRampModule
from PyTrinamic.features.MotorControl import MotorControl
from PyTrinamic.features.StallGuard2Motor import StallGuard2Motor
from PyTrinamic.features.LinearRampMotor import LinearRampMotor
from PyTrinamic.features.MotorControlMotor import MotorControlMotor

class TMC5130_eval(tmc_eval, StallGuard2Module, LinearRampModule, MotorControl):
    """
    This class represents a TMC5130 Evaluation board.

    Communication is done over the TMCL commands writeMC and readMC. An
    implementation without TMCL may still use this class if these two functions
    are provided properly. See __init__ for details on the function
    requirements.
    """

    class APs:
        RampMode = 30

    __PIN_MAP = [
        # (pin_ic, pin_board)
        (2, 15),
        (3, 22),
        (4, 23),
        (5, 24),
        (7, 25),
        (8, 9),
        (9, 10),
        (23, 4),
        (24, 6),
        (25, 5),
        (26, 30),
        (27, 29),
        (28, 28)
    ]

    def __init__(self, connection, module_id=1):
        tmc_eval.__init__(self, connection, module_id)

        self.ics = [TMC5130(self)]
        self.MOTORS = [
            MotorManager.motor(0, [self, self.ics[0]], features=[LinearRampMotor, MotorControlMotor, StallGuard2Motor])
        ]

    # Use the motion controller functions for register access
    def writeRegister(self, channel, address, value):
        del channel
        return self.connection.writeMC(address, value, self.module_id)

    def readRegister(self, channel, address, signed=False):
        del channel
        return self.connection.readMC(address, self.module_id, signed)

    # Motion Control functions
    def rotate(self, axis, velocity):
        if velocity >= 0:
            self.setTargetVelocity(axis, velocity)
            self.setAxisParameter(self.APs.RampMode, axis, 1)
        else:
            self.setTargetVelocity(axis, -velocity)
            self.setAxisParameter(self.APs.RampMode, axis, 2)

    def stop(self, axis):
        self.rotate(0, axis)

    def moveTo(self, axis, position, velocity=None):
        if velocity:
            self.setMaxVelocity(axis, velocity)

        self.setAxisParameter(self.APs.RampMode, axis, 0)
        self.connection.move(0, axis, position, self.MODULE_ID)
        self.setTargetPosition(axis, position)

    def moveBy(self, axis, difference, velocity=None):
        position = difference + self.getActualPosition(axis)

        self.moveTo(axis, position, velocity)

        return position
