################################################################################
# Copyright © 2026 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytest

from pytrinamic.tmcl import TMCLRequest, TMCLReply, TMCLStatus, GetInfoNotAvailableError, GetInfoRequestError
from pytrinamic.connections.tmcl_interface import TMCLReplyStatusError, TmclInterface


class MockTmclInterface(TmclInterface):

    def __init__(self, raise_error=None):
        super().__init__()
        self.raise_error = raise_error

    def send_request(self, request: TMCLRequest, *, no_reply=False) -> TMCLReply | None:
        mapping_op_type_vs_value = {
            0: 1636,
            1: 0x5555 << 16 | 0xAAAA << 0,
            2: 0x0002,
            3: 3,
            10: 1639,
            11: 0xAAAA << 16 | 0x5555 << 0,
            20: 13,
            21: 11 + 1 * request.motorBank,
            30: 0x1 << 28 | 0xA275BA2 << 0,
        }
        value = mapping_op_type_vs_value[request.commandType]

        reply = TMCLReply(
            reply_address=0x01,
            module_address=request.moduleAddress,
            status=self.raise_error if self.raise_error else TMCLStatus.SUCCESS,
            command=request.command,
            value=value,
        )
        if self.raise_error:
            raise TMCLReplyStatusError(reply)
        else:
            return reply


def test_success():
    connection = MockTmclInterface()
    assert connection.get_info("FWModuleID").value == 1636
    assert connection.get_info("FWVersion").major == 0x5555
    assert connection.get_info("FWVersion").minor == 0xAAAA
    assert connection.get_info("FWCapability").bitfield["Bootloader"] == 0
    assert connection.get_info("FWCapability").bitfield["TMCL"] == 1
    assert connection.get_info("FWCapability").bitfield["CANopen"] == 0
    assert connection.get_info("FWCapability").bitfield["EtherCAT"] == 0
    assert connection.get_info("FWCapability").bitfield["IO-Link"] == 0
    assert connection.get_info("FWReleaseType").value == 3
    assert str(connection.get_info("FWReleaseType")) == "Local"
    assert connection.get_info("BLModuleIDCompatible").value == 1639
    assert connection.get_info("BLVersionInstalled").major == 0xAAAA
    assert connection.get_info("BLVersionInstalled").minor == 0x5555
    assert connection.get_info("APIndexBitWidth").value == 13
    assert connection.get_info("RegAddrBitWidth", 0).value == 11
    assert connection.get_info("RegAddrBitWidth", 1).value == 12
    assert connection.get_info("GitHash").hash == 0xA275BA2
    assert connection.get_info("GitHash").dirty_flag == 1


@pytest.mark.parametrize("entry", [
    "FWModuleID",
    "FWVersion",
    "FWCapability",
    "FWReleaseType",
    "BLModuleIDCompatible",
    "BLVersionInstalled",
    "APIndexBitWidth",
    "RegAddrBitWidth",
    "RegAddrBitWidth",
    "GitHash",
])
def test_fail_not_implemented(entry):
    connection = MockTmclInterface(raise_error=TMCLStatus.COMMAND_NOT_AVAILABLE)
    with pytest.raises(GetInfoNotAvailableError):
        connection.get_info(entry)


@pytest.mark.parametrize("entry", [
    "FWModuleID",
    "FWVersion",
    "FWCapability",
    "FWReleaseType",
    "BLModuleIDCompatible",
    "BLVersionInstalled",
    "APIndexBitWidth",
    "RegAddrBitWidth",
    "RegAddrBitWidth",
    "GitHash",
])
def test_fail_entry_missing(entry):
    connection = MockTmclInterface(raise_error=TMCLStatus.WRONG_TYPE)
    with pytest.raises(GetInfoRequestError):
        connection.get_info(entry)