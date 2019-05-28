'''
Created on 27.05.2019

@author: LH
'''

from PyTrinamic.TMCL import TMCL_Request, TMCL_Command, TMCL_Reply

from PyTrinamic.helpers import TMC_helpers

class tmcl_interface():
    """
    This class is a base class for sending TMCL commands over a communication
    interface.

    Constructor parameters:
        host_id:
            Type: int, optional, default value: 2
            The ID of the TMCL host. This id is the same for each module
            when communicating with multiple modules.
        module_id:
            Type: int, optional, default value: 1
            The default module ID to use when no ID is given to any of
            the tmcl_interface functions.
        debug:
            Type: bool, optional, default: False
            A switch for enabling debug mode. Can be changed with enableDebug().
            In debug mode results all sent and received TMCL packets get dumped
            to stdout. The boolean _debug attribute holds the current state of
            debug mode - subclasses may read it to print futher debug output.

    A subclass is required over override the following functions:

    _send(self, hostID, moduleID, data):
        Send the bytearray [data]. The length of [data] is 9. The hostID and
        moduleID parameters may be used for extended addressing options
        available on the implemented communication interface.
    _recv(self, hostID, moduleID):
        Receive a reply and return it as a bytearray. The length of the returned
        byte array is 9. The hostID and moduleID parameters may be used for
        extended addressing options available on the implemented communication
        interface.
    """

    def __init__(self, hostID=2, moduleID=1, debug=False):
        if not(type(hostID) == type(moduleID) == int):
            raise TypeError

        if not type(debug) == bool:
            raise TypeError

        self._hostID    = hostID   & 0xFF
        self._moduleID  = moduleID & 0xFF
        self._debug     = debug

    def _send(self, hostID, moduleID, data):
        """
        Send a bytearray representing a TMCL command
        """
        raise NotImplementedError("The TMCL interface requires an implementation of the _send() function")

    def _recv(self, hostID, moduleID):
        """
        Receive a TMCL reply and return it as a bytearray
        """
        raise NotImplementedError("The TMCL interface requires an implementation of the _recv() function")

    def enableDebug(self, enable):
        """
        Enable the debug mode, which dumps all TMCL datagrams written and read
        """
        if type(enable) != bool:
            raise TypeError("Expected boolean value")

        self._debug = enable

    def send(self, opcode, op_type, motor, value, moduleID=None):
        """
        Send a TMCL datagram and read back a reply. This function blocks until
        the reply has been received
        """
        if not(type(opcode) == type(op_type) == type(motor) == type(value) == int):
            raise TypeError("Expected integer values")

        # If no module ID is given, use the default one
        if not moduleID:
            moduleID = self._moduleID

        request = TMCL_Request(moduleID, opcode, op_type, motor, value)

        if self._debug:
            request.dump()

        # Send the request
        self._send(self._hostID, moduleID, request.toBuffer())

        # Read out the reply
        reply = TMCL_Reply(self._recv(self._hostID, moduleID))

        if self._debug:
            reply.dump()

        return reply

    def sendBoot(self, moduleID=None):
        """
        Send the command for entering bootloader mode. This command does not
        send a reply.
        """
        # If no module ID is given, use the default one
        if not moduleID:
            moduleID = self._moduleID

        request = TMCL_Request(moduleID, TMCL_Command.BOOT, 0x81, 0x92, 0xA3B4C5D6)

        if self._debug:
            request.dump()

        # Send the request
        self._send(self._hostID, moduleID, request.toBuffer())

    def getVersionString(self, moduleID=None):
        """
        Request the ASCII version string.
        """
        reply = self.send(TMCL_Command.GET_FIRMWARE_VERSION, 0, 0, 0, moduleID)

        return reply.versionString()

    " axis parameter access "
    def axisParameter(self, commandType, axis, moduleID=None):
        return TMC_helpers.toSigned32(self.send(TMCL_Command.GAP, commandType, axis, 0, moduleID).value)

    def setAxisParameter(self, commandType, axis, value, moduleID=None):
        return self.send(TMCL_Command.SAP, commandType, axis, value, moduleID)

    def storeAxisParameter(self, commandType, axis, moduleID=None):
        return self.send(TMCL_Command.STAP, commandType, axis, 0, moduleID)

    def setAndStoreAxisParameter(self, commandType, axis, value, moduleID=None):
        self.send(TMCL_Command.SAP, commandType, axis, value, moduleID)
        self.send(TMCL_Command.STAP, commandType, axis, 0, moduleID)

    " global parameter access "
    def globalParameter(self, commandType, axis, moduleID=None):
        return TMC_helpers.toSigned32(self.send(TMCL_Command.GGP, commandType, axis, 0, moduleID).value)

    def setGlobalParameter(self, commandType, axis, value, moduleID=None):
        return self.send(TMCL_Command.SGP, commandType, axis, value, moduleID)

    def storeGlobalParameter(self, commandType, axis, moduleID=None):
        return self.send(TMCL_Command.STGP, commandType, axis, 0, moduleID)

    def setAndStoreGlobalParameter(self, commandType, axis, value, moduleID=None):
        self.send(TMCL_Command.SGP, commandType, axis, value, moduleID)
        self.send(TMCL_Command.STGP, commandType, axis, 0, moduleID)

    " register access "
    def writeMC(self, registerAddress, value, moduleID=None):
        return self.send(TMCL_Command.WRITE_MC, registerAddress, 0, value, moduleID)

    def readMC(self, registerAddress, moduleID=None):
        return TMC_helpers.toSigned32(self.send(TMCL_Command.READ_MC, registerAddress, 0, 0, moduleID).value)

    def writeDRV(self, registerAddress, value, moduleID=None):
        return self.send(TMCL_Command.WRITE_DRV, registerAddress, 0, value, moduleID)

    def readDRV(self, registerAddress, moduleID=None):
        return TMC_helpers.toSigned32(self.send(TMCL_Command.READ_DRV, registerAddress, 0, 0, moduleID).value)

    # Motion control functions
    def rotate(self, motor, velocity, moduleID=None):
        return self.send(TMCL_Command.ROR, 0, motor, velocity, moduleID)

    def stop(self, motor, moduleID=None):
        return self.send(TMCL_Command.MST, 0, motor, 0, moduleID)

    def move(self, moveType, motor, position, moduleID=None):
        return self.send(TMCL_Command.MVP, moveType, motor, position, moduleID)

    " input / outputs "
    def analogInput(self, x, moduleID=None):
        return self.send(TMCL_Command.GIO, x, 1, 0, moduleID).value

    def digitalInput(self, x, moduleID=None):
        return self.send(TMCL_Command.GIO, x, 0, 0, moduleID).value