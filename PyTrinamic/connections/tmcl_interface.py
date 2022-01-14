from PyTrinamic.TMCL import TMCL, TMCL_Request, TMCL_Command, TMCL_Reply
from PyTrinamic.helpers import TMC_helpers

class tmcl_interface():
    """
    This class is a base class for sending TMCL commands over a communication
    interface.

    Each instance of this class represents one TMCL host. The bus connection for
    the TMCL communication is represented by a subclass inheriting this base
    class. An application with multiple busses should therefore use subclasses
    for all types of busses (e.g. one USB TMCL interface and one serial TMCL
    interface) and create exactly one instance of one of those subclasses per
    bus.

    A subclass is required to override the following functions:
        _send(self, hostID, moduleID, data)
        _recv(self, hostID, moduleID)

    A subclass may use the boolean _debug attribute to toggle printing further
    debug output.

    A subclass may read the _HOST_ID and _MODULE_ID parameters.
    """

    def __init__(self, host_id=2, default_module_id=1, debug=False):
        """
        Parameters:
            host_id:
                Type: int, optional, default value: 2
                The ID of the TMCL host. This ID is the same for each module
                when communicating with multiple modules.
            default_module_id:
                Type: int, optional, default value: 1
                The default module ID to use when no ID is given to any of the
                tmcl_interface functions. When only communicating with one
                module a script can omit the moduleID for all TMCL interface
                calls by declaring this default value once at the start.
            debug:
                Type: bool, optional, default: False
                A switch for enabling debug mode. Can be changed with
                enableDebug(). In debug mode all sent and received TMCL packets
                get dumped to stdout. The boolean _debug attribute holds the
                current state of debug mode - subclasses may read it to print
                further debug output.
        """

        TMCL.validate_host_id(host_id)
        TMCL.validate_module_id(default_module_id)

        if not type(debug) == bool:
            raise TypeError

        self._HOST_ID = host_id
        self._MODULE_ID = default_module_id
        self._debug = debug

    def _send(self, host_id, module_id, data):
        """
        Send the bytearray [data] representing a TMCL command. The length of
        [data] is 9. The hostID and moduleID parameters may be used for extended
        addressing options available on the implemented communication interface.
        """
        raise NotImplementedError("The TMCL interface requires an implementation of the send() function")

    def _recv(self, host_id, module_id):
        """
        Receive a TMCL reply and return it as a bytearray. The length of the
        returned byte array is 9. The hostID and moduleID parameters may be used
        for extended addressing options available on the implemented
        communication interface.
        """
        raise NotImplementedError("The TMCL interface requires an implementation of the receive() function")

    def enableDebug(self, enable):
        """
        Set the debug mode, which dumps all TMCL datagrams written and read.
        """
        if type(enable) != bool:
            raise TypeError("Expected boolean value")

        self._debug = enable

    def send_request(self, request, module_id=None):
        """
        Send a TMCL_Request and read back a TMCL_Reply. This function blocks until
        the reply has been received.
        """

        if not module_id:
            module_id = self._MODULE_ID

        if self._debug:
            request.dump()

        self._send(self._HOST_ID, module_id, request.toBuffer())
        reply = TMCL_Reply.from_buffer(self._recv(self._HOST_ID, module_id))

        if self._debug:
            reply.dump()

        return reply

    def send(self, opcode, op_type, motor, value, module_id=None):
        """
        Send a TMCL datagram and read back a reply. This function blocks until
        the reply has been received.
        """

        if not(type(opcode) == type(op_type) == type(motor) == type(value) == int):
            raise TypeError("Expected integer values")

        # If no module ID is given, use the default one
        if not module_id:
            module_id = self._MODULE_ID

        request = TMCL_Request(module_id, opcode, op_type, motor, value)

        if self._debug:
            request.dump()

        self._send(self._HOST_ID, module_id, request.toBuffer())
        reply = TMCL_Reply.from_buffer(self._recv(self._HOST_ID, module_id))

        if self._debug:
            reply.dump()

        return reply

    def sendBoot(self, module_id=None):
        """
        Send the command for entering bootloader mode. This TMCL command does
        result in a reply.
        """
        # If no module ID is given, use the default one
        if not module_id:
            module_id = self._MODULE_ID

        request = TMCL_Request(module_id, TMCL_Command.BOOT, 0x81, 0x92, 0xA3B4C5D6)

        if self._debug:
            request.dump()

        # Send the request
        self._send(self._HOST_ID, module_id, request.toBuffer())

    def getVersionString(self, module_id=None):
        """
        Request the ASCII version string.
        """
        reply = self.send(TMCL_Command.GET_FIRMWARE_VERSION, 0, 0, 0, module_id)

        return reply.versionString()

    # General parameter access functions
    def parameter(self, p_command, p_type, p_axis, p_value, module_id=None, signed=False):
        value = self.send(p_command, p_type, p_axis, p_value, module_id).value
        return TMC_helpers.toSigned32(value) if signed else value

    def setParameter(self, p_command, p_type, p_axis, p_value, module_id=None):
        return self.send(p_command, p_type, p_axis, p_value, module_id)

    # Axis parameter access functions
    def axisParameter(self, command_type, axis, module_id=None, signed=False):
        value = self.send(TMCL_Command.GAP, command_type, axis, 0, module_id).value
        return TMC_helpers.toSigned32(value) if signed else value

    def setAxisParameter(self, command_type, axis, value, module_id=None):
        return self.send(TMCL_Command.SAP, command_type, axis, value, module_id)

    def storeAxisParameter(self, command_type, axis, module_id=None):
        return self.send(TMCL_Command.STAP, command_type, axis, 0, module_id)

    def setAndStoreAxisParameter(self, command_type, axis, value, module_id=None):
        self.send(TMCL_Command.SAP, command_type, axis, value, module_id)
        self.send(TMCL_Command.STAP, command_type, axis, 0, module_id)

    # Global parameter access functions
    def globalParameter(self, command_type, bank, module_id=None, signed=False):
        value = self.send(TMCL_Command.GGP, command_type, bank, 0, module_id).value
        return TMC_helpers.toSigned32(value) if signed else value

    def setGlobalParameter(self, command_type, bank, value, module_id=None):
        return self.send(TMCL_Command.SGP, command_type, bank, value, module_id)

    def storeGlobalParameter(self, command_type, bank, module_id=None):
        return self.send(TMCL_Command.STGP, command_type, bank, 0, module_id)

    def setAndStoreGlobalParameter(self, command_type, bank, value, module_id=None):
        self.send(TMCL_Command.SGP, command_type, bank, value, module_id)
        self.send(TMCL_Command.STGP, command_type, bank, 0, module_id)

    # Register access functions
    def writeMC(self, register_address, value, module_id=None):
        return self.writeRegister(register_address, TMCL_Command.WRITE_MC, 0, value, module_id)

    def readMC(self, register_address, module_id=None, signed=False):
        return self.readRegister(register_address, TMCL_Command.READ_MC, 0, module_id, signed)

    def writeDRV(self, register_address, value, module_id=None):
        return self.writeRegister(register_address, TMCL_Command.WRITE_DRV, 1, value, module_id)

    def readDRV(self, register_address, module_id=None, signed=False):
        return self.readRegister(register_address, TMCL_Command.READ_DRV, 1, module_id, signed)

    def readRegister(self, register_address, command, channel, module_id=None, signed=False):
        value = self.send(command, register_address, channel, 0, module_id).value
        return TMC_helpers.toSigned32(value) if signed else value

    def writeRegister(self, register_address, command, channel, value, module_id=None):
        return self.send(command, register_address, channel, value, module_id)

    # Motion control functions
    def rotate(self, motor, velocity, module_id=None):
        return self.send(TMCL_Command.ROR, 0, motor, velocity, module_id)

    def stop(self, motor, module_id=None):
        return self.send(TMCL_Command.MST, 0, motor, 0, module_id)

    def move(self, move_type, motor, position, module_id=None):
        return self.send(TMCL_Command.MVP, move_type, motor, position, module_id)

    def moveTo(self, motor, position, module_id=None):
        """
        Use the TMCL MVP command to perform an absolute movement.

        Returns the value of the reply. Refer to the documentation of your
        specific module for details on what is returned.
        """
        return self.move(0, motor, position, module_id).value

    def moveBy(self, motor, distance, module_id=None):
        """
        Use the TMCL MVP command to perform a relative movement.

        Returns the value of the reply. Refer to the documentation of your
        specific module for details on what is returned.
        """
        return self.move(1, motor, distance, module_id).value

    # IO pin functions
    def analogInput(self, x, module_id=None):
        return self.send(TMCL_Command.GIO, x, 1, 0, module_id).value

    def digitalInput(self, x, module_id=None):
        return self.send(TMCL_Command.GIO, x, 0, 0, module_id).value

    def digitalOutput(self, x, module_id=None):
        return self.send(TMCL_Command.GIO, x, 2, 0, module_id).value

    def setDigitalOutput(self, x, module_id=None):
        self.send(TMCL_Command.SIO, x, 2, 1, module_id).value

    def clearDigitalOutput(self, x, module_id=None):
        self.send(TMCL_Command.SIO, x, 2, 0, module_id).value

    " testing new interface usage (ED) => "
    # axis parameter access functions
    def axisParameterRaw(self, module_id, axis, command_type):
        return self.send(TMCL_Command.GAP, command_type, axis, 0, module_id).value

    def setAxisParameterRaw(self, module_id, axis, command_type,  value):
        return self.send(TMCL_Command.SAP, command_type, axis, value, module_id)

    # global parameter access functions
    def globalParameterRaw(self, module_id, bank, command_type):
        return self.send(TMCL_Command.GGP, command_type, bank, 0, module_id).value

    def setGlobalParameterRaw(self, module_id, bank, command_type, value):
        return self.send(TMCL_Command.SGP, command_type, bank, value, module_id)

    def storeGlobalParameterRaw(self, module_id, bank, command_type):
        return self.send(TMCL_Command.STGP, command_type, bank, 0, module_id)

    def setAndStoreGlobalParameterRaw(self, module_id, bank, command_type, value):
        self.send(TMCL_Command.SGP, command_type, bank, value, module_id)
        return self.send(TMCL_Command.STGP, command_type, bank, 0, module_id)

    def restoreGlobalParameterRaw(self, module_id, bank, command_type):
        return self.send(TMCL_Command.RSGP, command_type, bank, 0, module_id)

    # IO pin functions
    def analogInputRaw(self, module_id, x):
        return self.send(TMCL_Command.GIO, x, 1, 0, module_id).value

    def digitalInputRaw(self, module_id, x):
        return self.send(TMCL_Command.GIO, x, 0, 0, module_id).value

    def digitalOutputRaw(self, module_id, x):
        return self.send(TMCL_Command.GIO, x, 2, 0, module_id).value

    def setDigitalOutputRaw(self, module_id, x):
        self.send(TMCL_Command.SIO, x, 2, 1, module_id).value

    def clearDigitalOutputRaw(self, module_id, x):
        self.send(TMCL_Command.SIO, x, 2, 0, module_id).value

    " <= testing new interface usage (ED) "
