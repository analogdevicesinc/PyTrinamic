from pytrinamic.tmcl import TMCLCommand
from pytrinamic.helpers import EEPROM


class Landungsbruecke:
    def __init__(self, connection):
        self.__connection = connection

        self._mcId = 0
        self._drvId = 0

        self.eeprom_mc = EEPROM(self._read_mc_eeprom, self._write_mc_eeprom)
        self.eeprom_drv = EEPROM(self._read_drv_eeprom, self._write_drv_eeprom)

    def get_board_ids(self):
        """
        Read out the IDs of the detected boards.

        This does not start a detection.
        Returns a tuple of IDs: (drvId, mcId)
        """
        value = self.__connection.get_global_parameter(self.GP.BoardAssignment, 0)

        drvStatus = (value >> 24) & 0xFF
        drvId     = (value >> 16) & 0xFF
        mcStatus  = (value >>  8) & 0xFF
        mcId      = (value      ) & 0xFF

        if mcStatus == 2:
            self._mcId = mcId
        if drvStatus == 2:
            self._drvId = drvId

        return self._mcId, self._drvId

    def detect_board_ids(self):
        """
        Start an IDDetection and read out the IDs of the detected boards.
        """
        while not self.__connection.send(TMCLCommand.ASSIGNMENT, 0, 0, 0).is_valid():
            pass

        return self.get_board_ids()

    def get_board_names(self):
        board_ids = self.get_board_ids()

        try:
            mc_name = self.mcIdNames[board_ids[0]]
        except KeyError:
            mc_name = str(board_ids[0])

        try:
            drv_name = self.drvIdNames[board_ids[1]]
        except KeyError:
            drv_name = str(board_ids[1])

        return mc_name, drv_name

    def _read_mc_eeprom(self, address):
        reply = self.__connection.send(TMCLCommand.TMCL_UF1, 1, 0, address)

        if not reply.is_valid():
            raise RuntimeError("Failed to read driver ID EEPROM")

        return reply.value

    def _write_mc_eeprom(self, address, value):
        self.__connection.send(TMCLCommand.TMCL_UF2, 1, value, address)

    def _read_drv_eeprom(self, address):
        reply = self.__connection.send(TMCLCommand.TMCL_UF1, 2, 0, address)

        if not reply.is_valid():
            raise RuntimeError("Failed to read driver ID EEPROM")

        return reply.value

    def _write_drv_eeprom(self, address, value):
        self.__connection.send(TMCLCommand.TMCL_UF2, 2, value & 0xFF, address)

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

    class GP:
        VitalSignsErrorMask  = 1
        DriversEnable        = 2
        DebugMode            = 3
        BoardAssignment      = 4
        HWID                 = 5
        PinState             = 6


if __name__ == "__main__":
    from pytrinamic.connections import ConnectionManager

    cm = ConnectionManager()
    interface = cm.connect()
    LB = Landungsbruecke(interface)

    print("ID EEPROM content:")
    print("Mc: ", LB.eeprom_drv.read_id_info())
    print("Drv:", LB.eeprom_mc.read_id_info())

    print("Board IDs:")
    print(LB.get_board_ids())

    print("Board Names:")
    print(LB.get_board_names())
