'''
Created on 17.04.2020

@author: JM
'''

from pytrinamic.ic.TMC6300.TMC6300 import TMC6300

class TMC6300_eval(TMC6300):
    def __init__(self, connection, moduleID=1):

        TMC6300.__init__(self, moduleID)

        self.__connection = connection
        self._MODULE_ID = moduleID

        self.APs = _APs

    # Axis parameter access
    def getAxisParameter(self, apType, axis):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        return self.__connection.get_axis_parameter(apType, axis)

    def setAxisParameter(self, apType, axis, value):
        if not(0 <= axis < self.MOTORS):
            raise ValueError("Axis index out of range")

        self.__connection.set_axis_parameter(apType, axis, value)

    # Motion Control functions
    def rotate(self, motor, value):
        if not(0 <= motor < self.MOTORS):
            raise ValueError

        self.__connection.rotate(motor, value, moduleID=self._MODULE_ID)

    def setTargetPWM(self, motor, value):
        self.setAxisParameter(self.APs.TargetPWM, motor, value)

    def stop(self, motor):
        self.__connection.stop(motor, moduleID=self._MODULE_ID)

    def setCommutationMode(self, motor, value):
        self.setAxisParameter(self.APs.CommutationMode, motor, value)

    def ICStandby(self, motor, value):
        self.setAxisParameter(self.APs.ICStandby, motor, value)

    def setHallDirection(self, motor, value):
        self.setAxisParameter(self.APs.HallDirection, motor, value)

    def setHallOrder(self, motor, value):
        self.setAxisParameter(self.APs.HallOrder, motor, value)

class _APs():
    ActualControlledAngle          = 1
    ActualHallAngle                = 2
    ActualPWM                      = 3
    TargetPWM                      = 4
    CommutationMode                = 5
    OpenLoopStepTime               = 6
    Current                        = 7
    HallDirection                  = 8
    HallOrder                      = 9
    ICStandby                      = 10
    VMMeasurement                  = 11
