################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

import logging
import warnings
from abc import ABC
from ..tmcl import TMCL, TMCLRequest, TMCLCommand, TMCLReply, TMCLReplyChecksumError, TMCLReplyStatusError
from ..helpers import to_signed_32


class TmclInterface(ABC):
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
        _send(self, host_id, module_id, data)
        _recv(self, host_id, module_id)

    """

    def __init__(self, host_id=2, default_module_id=1, default_ap_index_bit_width=8):
        """
        :param int host_id: The ID of the TMCL host. This ID is the same for each module
            when communicating with multiple modules.
        :param int default_module_id: The default module ID to use when no ID is given to any of the
            tmcl_interface functions. When only communicating with one
            module a script can omit the moduleID for all TMCL interface
            calls by declaring this default value once at the start.
        :param int default_ap_index_bit_width: Axis parameter index bit-width.
        """
        self.logger = logging.getLogger("TmclInterfaceAbstractBaseClassObject")  # Will be overwritten in derived classes

        TMCL.validate_host_id(host_id)
        TMCL.validate_module_id(default_module_id)

        self._host_id = host_id
        self._default_module_id = default_module_id

        if not (8 <= default_ap_index_bit_width <= 15):
            raise ValueError(f"Value {default_ap_index_bit_width} for parameter default_ap_index_bit_width is outside the allowed range (8..15)!")

        self._default_ap_index_bit_width = default_ap_index_bit_width

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

    def _reply_check(self, reply):
        """
        Interface specific check of the reply.

        For Serial-TMCL we need to check the checksum.
        Per default no check is implemented.

        :param reply: The TMCLReply received in during _recv().
        """
        pass

    def send_request(self, request):
        """
        Send a TMCL_Request and read back a TMCL_Reply. This function blocks until
        the reply has been received.
        """
        self.logger.debug("Tx: %s", request)

        self._send(self._host_id, request.moduleAddress, request.to_buffer())
        reply = TMCLReply.from_buffer(self._recv(self._host_id, request.moduleAddress))

        self.logger.debug("Rx: %s", reply)

        self._reply_check(reply)

        # Status codes below 100 indicate an error response.
        if reply.status < 100:
            raise TMCLReplyStatusError(reply)

        return reply

    def send(self, opcode, op_type, motor, value, module_id=None):
        """
        Send a TMCL datagram and read back a reply. This function blocks until
        the reply has been received.
        """
        if any(not isinstance(arg, int) for arg in [opcode, op_type, motor, value]):
            raise TypeError("Expected integer values!")

        # If no module ID is given, use the default one
        if not module_id:
            module_id = self._default_module_id

        request = TMCLRequest(module_id, opcode, op_type, motor, value)

        return self.send_request(request)

    def send_boot(self, module_id=None):
        """
        Send the command for entering bootloader mode. This TMCL command does
        result in a reply.
        """
        # If no module ID is given, use the default one
        if not module_id:
            module_id = self._default_module_id

        request = TMCLRequest(module_id, TMCLCommand.BOOT, 0x81, 0x92, 0xA3B4C5D6)

        self.logger.debug("Tx: %s", request)

        # Send the request
        self._send(self._host_id, module_id, request.to_buffer())

    def get_version_string(self, module_id=None):
        """
        Request the ASCII version string.

        .. deprecated:: 0.2.0
        """
        try:
            reply = self.send(TMCLCommand.GET_FIRMWARE_VERSION, 0, 0, 0, module_id)
        except (TMCLReplyStatusError, TMCLReplyChecksumError) as exc:
            return exc.reply.version_string()
        else:
            return reply.version_string()

    # General parameter access functions
    def get_parameter(self, p_command, p_type, p_axis, p_value, module_id=None, signed=False):
        """
        General parameter read function.

        .. deprecated:: 0.3.0
        """
        warnings.warn("Function get_parameter() is going te be removed in future versions of pytrinamic!", FutureWarning)
        value = self.send(p_command, p_type, p_axis, p_value, module_id).value
        return to_signed_32(value) if signed else value

    def set_parameter(self, p_command, p_type, p_axis, p_value, module_id=None):
        """
        General parameter write function.

        .. deprecated:: 0.3.0
        """
        warnings.warn("Function set_parameter() is going te be removed in future versions of pytrinamic!", FutureWarning)
        return self.send(p_command, p_type, p_axis, p_value, module_id)

    def _send_ap_cmd(self, cmd, index, axis, value, module_id, index_bit_width):
        if not index_bit_width:
            index_bit_width = self._default_ap_index_bit_width

        if not (8 <= index_bit_width <= 15):
            raise ValueError(f"Value {index_bit_width} for parameter index_bit_width is outside the allowed range (8..15)!")

        axis_bit_width = 16 - index_bit_width

        if index >= 2**index_bit_width:
            raise ValueError(f"Value {index} for parameter index is outside the allowed range (0..{2**index_bit_width - 1})!")
        if axis >= 2**axis_bit_width:
            raise ValueError(f"Value {axis} for parameter axis is outside the allowed range (0..{2**axis_bit_width - 1})!")

        index_shift = 8 - axis_bit_width
        index_mask = ((2**index_bit_width) - 1) << 8
        tmcl_motor = axis | ((index & index_mask) >> index_shift)
        tmcl_type = index & 0xFF
        return self.send(cmd, tmcl_type, tmcl_motor, value, module_id)

    # Axis parameter access functions
    def get_axis_parameter(self, index, axis, module_id=None, signed=False, index_bit_width=None):
        value = self._send_ap_cmd(TMCLCommand.GAP, index, axis, 0, module_id, index_bit_width).value
        return to_signed_32(value) if signed else value

    def set_axis_parameter(self, index, axis, value, module_id=None, index_bit_width=None):
        return self._send_ap_cmd(TMCLCommand.SAP, index, axis, value, module_id, index_bit_width).value

    def store_axis_parameter(self, index, axis, module_id=None, index_bit_width=None):
        return self._send_ap_cmd(TMCLCommand.STAP, index, axis, 0, module_id, index_bit_width).value

    def set_and_store_axis_parameter(self, index, axis, value, module_id=None, index_bit_width=None):
        self._send_ap_cmd(TMCLCommand.SAP, index, axis, value, module_id, index_bit_width)
        self._send_ap_cmd(TMCLCommand.STAP, index, axis, 0, module_id, index_bit_width)

    # Global parameter access functions
    def get_global_parameter(self, command_type, bank, module_id=None, signed=False):
        value = self.send(TMCLCommand.GGP, command_type, bank, 0, module_id).value
        return to_signed_32(value) if signed else value

    def set_global_parameter(self, command_type, bank, value, module_id=None):
        return self.send(TMCLCommand.SGP, command_type, bank, value, module_id)

    def store_global_parameter(self, command_type, bank, module_id=None):
        return self.send(TMCLCommand.STGP, command_type, bank, 0, module_id)

    def set_and_store_global_parameter(self, command_type, bank, value, module_id=None):
        self.send(TMCLCommand.SGP, command_type, bank, value, module_id)
        self.send(TMCLCommand.STGP, command_type, bank, 0, module_id)

    # Register access functions
    def write_mc(self, register_address, value, module_id=None):
        return self.write_register(register_address, TMCLCommand.WRITE_MC, 0, value, module_id)

    def read_mc(self, register_address, module_id=None, signed=False):
        return self.read_register(register_address, TMCLCommand.READ_MC, 0, module_id, signed)

    def write_mc_by_id(self, ic_id, register_address, value, module_id=None):
        return self.write_register(register_address, TMCLCommand.WRITE_MC, ic_id, value, module_id)

    def read_mc_by_id(self, ic_id, register_address, module_id=None, signed=False):
        return self.read_register(register_address, TMCLCommand.READ_MC, ic_id, module_id, signed)

    def write_drv(self, register_address, value, module_id=None):
        return self.write_register(register_address, TMCLCommand.WRITE_DRV, 1, value, module_id)

    def read_drv(self, register_address, module_id=None, signed=False):
        return self.read_register(register_address, TMCLCommand.READ_DRV, 1, module_id, signed)

    def read_register(self, register_address, command, channel, module_id=None, signed=False):
        tmcl_motor = (channel & 0x0F) | ((register_address & 0x0F00) >> 4)
        tmcl_type = register_address & 0xFF
        value = self.send(command, tmcl_type, tmcl_motor, 0, module_id).value
        return to_signed_32(value) if signed else value

    def write_register(self, register_address, command, channel, value, module_id=None):
        tmcl_motor = (channel & 0x0F) | ((register_address & 0x0F00) >> 4)
        tmcl_type = register_address & 0xFF
        return self.send(command, tmcl_type, tmcl_motor, value, module_id)

    # Motion control functions
    def rotate(self, motor, velocity, module_id=None):
        return self.send(TMCLCommand.ROR, 0, motor, velocity, module_id)

    def stop(self, motor, module_id=None):
        return self.send(TMCLCommand.MST, 0, motor, 0, module_id)

    def move(self, move_type, motor, position, module_id=None):
        return self.send(TMCLCommand.MVP, move_type, motor, position, module_id)

    def move_to(self, motor, position, module_id=None):
        """
        Use the TMCL MVP command to perform an absolute movement.

        Returns the value of the reply. Refer to the documentation of your
        specific module for details on what is returned.
        """
        return self.move(0, motor, position, module_id).value

    def move_by(self, motor, distance, module_id=None):
        """
        Use the TMCL MVP command to perform a relative movement.

        Returns the value of the reply. Refer to the documentation of your
        specific module for details on what is returned.
        """
        return self.move(1, motor, distance, module_id).value

    def reference_search(self, command_type, motor, module_id=None):
        """
        Use the TMCL RFS command to search for the reference points.

        :param int command_type: 0 starts the search, 1 stops the search, and 2 returns the status.
        :param int motor: the index of the motor
        """
        return self.send(TMCLCommand.RFS, command_type, motor, 0, module_id).value

    # IO pin functions
    def get_analog_input(self, x, module_id=None):
        return self.send(TMCLCommand.GIO, x, 1, 0, module_id).value

    def get_digital_input(self, x, module_id=None):
        return self.send(TMCLCommand.GIO, x, 0, 0, module_id).value

    def get_digital_output(self, x, module_id=None):
        return self.send(TMCLCommand.GIO, x, 2, 0, module_id).value

    def set_digital_output(self, x, module_id=None):
        self.send(TMCLCommand.SIO, x, 2, 1, module_id)

    def clear_digital_output(self, x, module_id=None):
        self.send(TMCLCommand.SIO, x, 2, 0, module_id)
