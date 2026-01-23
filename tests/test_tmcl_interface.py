################################################################################
# Copyright © 2026 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

from pytrinamic.tmcl import TMCLRequest, TMCLReply, TMCLStatus
from pytrinamic.connections.tmcl_interface import TmclInterface


class MockTmclInterface(TmclInterface):
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

        return TMCLReply(
            reply_address=0x01,
            module_address=request.moduleAddress,
            status=TMCLStatus.SUCCESS,
            command=request.command,
            value=value,
        )


def test():
    iface = MockTmclInterface()
    assert iface.get_info("FWModuleID").value == 1636
    assert iface.get_info("FWVersion").major == 0x5555
    assert iface.get_info("FWVersion").minor == 0xAAAA
    assert iface.get_info("FWCapability").bitfield["Bootloader"] == 0
    assert iface.get_info("FWCapability").bitfield["TMCL"] == 1
    assert iface.get_info("FWCapability").bitfield["CANopen"] == 0
    assert iface.get_info("FWCapability").bitfield["EtherCAT"] == 0
    assert iface.get_info("FWCapability").bitfield["IO-Link"] == 0
    assert iface.get_info("FWReleaseType").value == 3
    assert str(iface.get_info("FWReleaseType")) == "Local"
    assert iface.get_info("BLModuleIDCompatible").value == 1639
    assert iface.get_info("BLVersionInstalled").major == 0xAAAA
    assert iface.get_info("BLVersionInstalled").minor == 0x5555
    assert iface.get_info("APIndexBitWidth").value == 13
    assert iface.get_info("RegAddrBitWidth", 0).value == 11
    assert iface.get_info("RegAddrBitWidth", 1).value == 12
    assert iface.get_info("GitHash").hash == 0xA275BA2
    assert iface.get_info("GitHash").dirty_flag == 1
