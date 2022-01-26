import serial.tools.list_ports
from pytrinamic.connections.serial_tmcl_interface import serial_tmclInterface


class UsbTmclInterface(serial_tmclInterface):
    """
    Opens a USB TMCL connection.

    This class is almost the same as the class for serial TMCL connections.
    The only difference are the functions for the connection manager, which
    filter the available serial connections to only include the serial over
    USB ones.
    """

    # USB Vendor and Product IDs
    __USB_IDS = [
        {  # Landungsbrücke
            "VID": 0x2A3C,
            "PID": 0x0700
        },
        {  # TMCM1460
            "VID": 0x16D0,
            "PID": 0x0461
        },
        {  # Startrampe
            "VID": 0x16D0,
            "PID": 0x07E4
        },
        {  # TMC_CDC_DEV
            "VID": 0x2A3C,
            "PID": 0x0200
        },
        {  # TMCM1160, TMCM1161
            "VID": 0x2A3C,
            "PID": 0x0100
        },
        {  # TMCM1161
            "VID": 0x16D0,
            "PID": 0x05A1
        },
        {  # TMC_EvalShield
            "VID": 0x0483,
            "PID": 0x374B
        },
        {  # TMCM0960
            "VID": 0xF055,
            "PID": 0x9800
        }
    ]

    def __init__(self, com_port, datarate=115200, host_id=2, module_id=1, debug=False):
        super().__init__(com_port, datarate, host_id, module_id, debug)

    # override serial_tmcl_interface
    def list(self):
        """
            Return a list of available connection ports as a list of strings.

            This function is required for using this interface with the
            connection manager.
        """
        connected = []
        for element in sorted(serial.tools.list_ports.comports()):
            for entry in UsbTmclInterface.__USB_IDS:
                if entry["VID"] == element.vid and entry["PID"] == element.pid:
                    connected.append(element.device)

        return connected

    def __str__(self):
        info = "UsbTmclInterface {"
        info += "'com_port':" + self._serial.portstr + ", "
        info += "'baudrate':" + str(self._baudrate) + ", "
        if self.supports_tmcl():
            info += "'supports_tmcl': True, "
        if self.supports_canopen():
            info += "'supports_canopen': True, "
        if self.debug_enabled():
            info += "'debug_enabled':" + str(self._debug) + ", "
        info = info[:-2]
        info += "}"
        return info


if __name__ == "__main__":
    interface = UsbTmclInterface("COM5")

    print("version_string:" + interface.get_version_string())
    # interface.send_boot()

    interface.close()
