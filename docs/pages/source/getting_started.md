# Getting Started

## Requirements

* Python ≥ 3.7
* Platform: OS-independent.
* Windows: Some USB-to-CAN adapters may require manual driver installation (see manufacturer documentation).

## Installation

PyTrinamic can be installed form PyPI using:

```
python -m pip install pytrinamic
```

## TMCL-Interface

The core elements of PyTrinamic are the TMCL interface classes.

* `SerialTmclInterface` represents a serial connection and is used for the TMCL over UART, RS232 or RS485 protocol.
* `UsbTmclInterface` is used for Trinamic USB devices and is basically a virtual serial TMCL connection.
* `CanTmclInterface` represents a CAN connection and is used for the TMCL over CAN protocol.

With any `TmclInterface` class TMCL commands can be send to a device. The following example sends the GET_FIRMWARE_VERSION command to a device, and prints the response.
```py
from pytrinamic.connections import UsbTmclInterface
from pytrinamic.tmcl import TMCLCommand

with UsbTmclInterface("/dev/ttyACM0") as iface:
    response = iface.send(opcode=TMCLCommand.GET_FIRMWARE_VERSION, op_type=1, motor=0, value=0)
    print(response)
```

Instead of using the interface class constructor, TMCL interface objects are usually created using the `ConnectionManager`.
One of the benefits of the `ConnectionManager` is, that it can automatically detect and connect to Trinamic USB devices.
This is the adaption of the prior example to use the `ConnectionManager`:
```py
from pytrinamic.connections import ConnectionManager
from pytrinamic.tmcl import TMCLCommand

with ConnectionManager().connect() as iface:
    response = iface.send(opcode=TMCLCommand.GET_FIRMWARE_VERSION, op_type=1, motor=0, value=0)
    print(response)
```

## IC-Interface

A few Trinamic ICs implement dedicated serial UART protocol in hardware the `UartIcInterface` is used for.