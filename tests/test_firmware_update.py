################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import time
import dataclasses

from unittest.mock import call

import pytest

from intelhex import IntelHex


from pytrinamic.connections.connection_manager import ConnectionManager
from pytrinamic.connections.tmcl_interface import TmclInterface
from pytrinamic.tmcl import TMCLCommand
from pytrinamic.cli.tmclfwupload import main


@dataclasses.dataclass
class DeviceMetadata:
    mem_start_address: int
    mem_size: int
    mem_page_size: int
    module_number: int
    fw_version_major: int
    fw_version_minor: int


class MockTmclInterface(TmclInterface):
    
    def __init__(self, device_metadata, device_is_already_in_boot_mode):
        self._device_metadata = device_metadata
        self._in_boot = device_is_already_in_boot_mode

        self.get_checksum_result = None

    def send(self, opcode, op_type, motor, value, module_id=None, *, no_reply=False):
        class FakeReplyValue:
            def __init__(self, value):
                self.value = value
        class FakeReplyGetFirmwareVersion:
            def __init__(self, reply_str):
                self._reply_str = reply_str
            def version_string(self):
                return self._reply_str
            
        if opcode == TMCLCommand.GET_FIRMWARE_VERSION:
            if self._in_boot:
                mode_char = "B"
            else:
                mode_char = "V"
            return FakeReplyGetFirmwareVersion(f"{self._device_metadata.module_number:04}{mode_char}{self._device_metadata.fw_version_major}{self._device_metadata.fw_version_minor:02}")
        elif opcode == TMCLCommand.BOOT_GET_INFO:
            mp = {
                0: self._device_metadata.mem_page_size,
                1: self._device_metadata.mem_start_address,
                2: self._device_metadata.mem_size,
            }
            return FakeReplyValue(mp[op_type])
        elif opcode == TMCLCommand.BOOT_GET_CHECKSUM:
            return FakeReplyValue(self.get_checksum_result)
        elif opcode == TMCLCommand.BOOT:
            self._in_boot = True
            return None
        return None

    def close(self):
        pass


@pytest.mark.parametrize("extra_data", [[], [0xBD], [0x75, 0xA3], [0xCD, 0x54, 0x19], [0 for _ in range(1024)], [0 for _ in range(4096-9)]])
@pytest.mark.parametrize("module_number_str", ["1617", "0013"])
@pytest.mark.parametrize("inboot", [False, True])
def test_minimal_upload(tmp_path, monkeypatch, mocker, inboot, module_number_str, extra_data):
    """Create a valid hex file and upload it with tmclfwupload.main()"""

    device_metadata = DeviceMetadata(
        mem_start_address=0x0800_C000,
        mem_size=128*1024,
        mem_page_size=4096,
        module_number=int(module_number_str, base=10),
        fw_version_major=1,
        fw_version_minor=8,
    )

    hex_file = tmp_path / "my.hex"
    
    ih = IntelHex()
    identification_string = f"{module_number_str}V000"
    addr = device_metadata.mem_start_address
    ih.putsz(addr, identification_string)
    addr += len(identification_string) + 1
    ih.puts(addr, bytes(extra_data))

    ih.write_hex_file(hex_file)
    fw_checksum = sum(ih.tobinarray())
    fw_length = len(ih.tobinarray())

    mock_tmcl_interface = MockTmclInterface(device_metadata, device_is_already_in_boot_mode=inboot)
    spy_send = mocker.spy(mock_tmcl_interface, "send")

    def mock_init(self, _=None):
        pass

    def mock_connect(self):
        return mock_tmcl_interface

    def mock_sleep(_):
        pass

    monkeypatch.setattr(ConnectionManager, "__init__", mock_init)
    monkeypatch.setattr(ConnectionManager, "connect", mock_connect)
    monkeypatch.setattr(time, 'sleep', mock_sleep)

    mock_tmcl_interface.get_checksum_result = fw_checksum

    main([str(hex_file)])
    
    expected_calls = []
    expected_calls.extend([
        call(TMCLCommand.GET_FIRMWARE_VERSION, 0, 0, 0, None),
    ])
    if not inboot:
        expected_calls.extend([
            call(TMCLCommand.BOOT, 0x81, 0x92, 0xA3B4C5D6, module_id=1, no_reply=True),
        ])
    expected_calls.extend([
        call(TMCLCommand.GET_FIRMWARE_VERSION, 0, 0, 0, 1),
        call(TMCLCommand.BOOT_GET_INFO, 0, 0, 0),
        call(TMCLCommand.BOOT_GET_INFO, 1, 0, 0),
        call(TMCLCommand.BOOT_GET_INFO, 2, 0, 0),
        call(TMCLCommand.BOOT_ERASE_ALL, 0, 0, 0),
    ])
    addr = 0
    page = 0
    buffer = []
    for x in ih.tobinarray():
        buffer.append(x)
        if len(buffer) == 4:
            addr_low = (addr & 0x00FF) >> 0
            addr_high = (addr & 0xFF00) >> 8
            expected_calls.append(call(TMCLCommand.BOOT_WRITE_BUFFER, addr_low, addr_high, int.from_bytes(buffer, byteorder="little")))
            addr += 1
            buffer = []
        if addr > 0 and (addr*4 % device_metadata.mem_page_size) == 0:
            expected_calls.append(call(TMCLCommand.BOOT_WRITE_PAGE, 0, 0, device_metadata.mem_start_address + page*device_metadata.mem_page_size))
            addr = 0
            page += 1
    if len(buffer) > 0:
        addr_low = (addr & 0x00FF) >> 0
        addr_high = (addr & 0xFF00) >> 8
        expected_calls.append(call(TMCLCommand.BOOT_WRITE_BUFFER, addr_low, addr_high, int.from_bytes(buffer, byteorder="little")))
    if addr != 0:
        expected_calls.append(call(TMCLCommand.BOOT_WRITE_PAGE, 0, 0, device_metadata.mem_start_address + page*device_metadata.mem_page_size))
    expected_calls.extend([
        call(TMCLCommand.BOOT_GET_CHECKSUM, 0, 0, device_metadata.mem_start_address + fw_length - 1),
        call(TMCLCommand.BOOT_WRITE_LENGTH, 0, 0, fw_length),
        call(TMCLCommand.BOOT_WRITE_LENGTH, 1, 0, fw_checksum),
        call(TMCLCommand.BOOT_START_APPL, 0, 0, 0, module_id=None, no_reply=True),
    ])

    assert len(spy_send.call_args_list) == len(expected_calls)

    for call_n, expected_call_n in zip(spy_send.call_args_list, expected_calls):
        assert call_n == expected_call_n