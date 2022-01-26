'''
Created on 24.07.2019

@author: LK
'''

from pytrinamic2.TMCL import TMCL_Command
from pytrinamic2.helpers import EEPROM

class Landungsbruecke():
    def __init__(self, connection):
        self.GP   = _GP
        self.__connection = connection

        self._mcId = 0
        self._drvId = 0

        self.EepromMc  = EEPROM(self._readMcEeprom, self._writeMcEeprom)
        self.EepromDrv = EEPROM(self._readDrvEeprom, self._writeDrvEeprom)

    def getBoardIDs(self):
        '''
        Read out the IDs of the detected boards.

        This does not start a detection.
        Returns a tuple of IDs: (drvId, mcId)
        '''
        value = self.__connection.get_global_parameter(self.GPs.BoardAssignment, 0)

        drvStatus = (value >> 24) & 0xFF
        drvId     = (value >> 16) & 0xFF
        mcStatus  = (value >>  8) & 0xFF
        mcId      = (value      ) & 0xFF

        if (mcStatus == 2):
            self._mcId = mcId
        if (drvStatus == 2):
            self._drvId = drvId

        return (self._mcId, self._drvId)

    def detectBoardIDs(self):
        '''
        Start an IDDetection and read out the IDs of the detected boards.
        '''

        while not self.__connection.send(TMCL_Command.ASSIGNMENT, 0, 0, 0).is_valid():
            pass

        return self.getBoardIDs()

    def getBoardNames(self):
        boardIDs = self.getBoardIDs()

        try:
            mcName = self.mcIdNames[boardIDs[0]]
        except KeyError:
            mcName = str(boardIDs[0])

        try:
            drvName = self.drvIdNames[boardIDs[1]]
        except KeyError:
            drvName = str(boardIDs[1])

        return (mcName, drvName)

    def _readMcEeprom(self, address):
        reply = self.__connection.send(TMCL_Command.TMCL_UF1, 1, 0, address)

        if not reply.is_valid():
            raise RuntimeError("Failed to read driver ID EEPROM")

        return reply.value

    def _writeMcEeprom(self, address, value):
        self.__connection.send(TMCL_Command.TMCL_UF2, 1, value, address)

    def _readDrvEeprom(self, address):
        reply = self.__connection.send(TMCL_Command.TMCL_UF1, 2, 0, address)

        if not reply.is_valid():
            raise RuntimeError("Failed to read driver ID EEPROM")

        return reply.value

    def _writeDrvEeprom(self, address, value):
        self.__connection.send(TMCL_Command.TMCL_UF2, 2, value & 0xFF, address)

    mcIdNames = {
        0  : "None",
        2  : "TMC5031",
        4  : "TMC4361",
        5  : "TMC5130",
        6  : "TMC5041",
        7  : "TMC5072",
        9  : "TMC4670",
        10 : "TMC4331",
        11 : "TMC4361A",
        13 : "TMC4671",
        15 : "TMC4330",
        16 : "TMC5160",
        18 : "TMC5161",
        25 : "TMC5062",
        26 : "TMC8461",
        27 : "TMC8462",
    }

    drvIdNames = {
        0  : "None",
        1  : "TMC2660",
        3  : "TMC2130",
        4  : "TMC2100",
        5  : "TMC2041",
        6  : "TMC2208",
        7  : "TMC2224",
        8  : "TMC2209",
        9  : "TMCC160",
        10 : "TMC6200",
        11 : "TMC2160",
        12 : "TMC7300",
        13 : "TMC2590",
        18 : "TMC2225",
        19 : "TMC6100",
        14 : "TMC2300",
        21 : "TMC6300",
        22 : "TMC2226",
    }

class _GP:
    VitalSignsErrorMask  = 1
    DriversEnable        = 2
    DebugMode            = 3
    BoardAssignment      = 4
    HWID                 = 5
    PinState             = 6

if __name__ == "__main__":
    from pytrinamic2.connections.connection_manager import ConnectionManager

    cm = ConnectionManager()
    interface = cm.connect()
    LB = Landungsbruecke(interface)

    print("ID EEPROM content:")
    print("Mc: ", LB.EepromDrv.read_id_info())
    print("Drv:", LB.EepromMc.read_id_info())

    print("Board IDs:")
    print(LB.getBoardIDs())

    print("Board Names:")
    print(LB.getBoardNames())
