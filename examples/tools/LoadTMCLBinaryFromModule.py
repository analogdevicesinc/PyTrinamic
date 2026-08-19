################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################

# This program loads a TMCL binary file from a module.

import argparse
import logging
import sys
from pytrinamic.connections import ConnectionManager
from pytrinamic.tmcl import TMCLCommand, GetInfo, TMCLRequest

def main():
    parser = argparse.ArgumentParser()

    # Add ConnectionManager arguments
    ConnectionManager.argparse(parser)

    parser.add_argument("-v", dest="verbose", action="count", default=0, help="Verbosity level")

    args = parser.parse_args()

    if args.verbose == 0:
        log_level = logging.ERROR
    elif args.verbose == 1:
        log_level = logging.WARNING
    elif args.verbose == 2:
        log_level = logging.INFO
    else:
        log_level = logging.DEBUG
    logging.basicConfig(stream=sys.stdout, level=log_level)


    connection_manager = ConnectionManager(sys.argv)
    tmcl = connection_manager.connect()

    # Check the GET_INFO feature flags to determine which variant of TMCL_ReadMem we must use
    use_legacy_readmem = not tmcl.get_info("FirmwareFeatureFlags").is_flag_set(GetInfo.FirmwareFeatureFlags.FirmwareFeatureFlag.TMCLSCRIPT_USE_NEW_READMEM)
    if use_legacy_readmem:
        print("Using legacy TMCL_ReadMem command")
    else:
        print("Using updated TMCL_ReadMem command")

    commands = []
    while True:
        if use_legacy_readmem:
            # TMCL_ReadMem returns a nonstandard reply holding 7 bytes, representing one stored TMCL command.
            # In this legacy command, the type field is ignored.
            reply = tmcl.send(TMCLCommand.READ_TMCL_MEMORY, 0, 0, len(commands))

            tmcl_opcode = reply.module_address
            tmcl_type   = reply.status
            tmcl_motor  = reply.command
            tmcl_value  = reply.value
        else:
            # TMCL_ReadMem returns the 7 bytes of the stored TMCL command in two steps.
            # The stored opcode, type and motor/bank bytes are available using type=1,
            # the stored value is available using type=2.

            # Grab the stored TMCL opcode, type, and motor fields
            reply = tmcl.send(TMCLCommand.READ_TMCL_MEMORY, 1, 0, len(commands)).value
            tmcl_opcode = (reply >>  0) & 0xFF
            tmcl_type   = (reply >>  8) & 0xFF
            tmcl_motor  = (reply >> 16) & 0xFF

            # Grab the stored TMCL value field
            tmcl_value = tmcl.send(TMCLCommand.READ_TMCL_MEMORY, 2, 0, len(commands)).value

        # The end of the stored program is signalled by an opcode of 0
        if tmcl_opcode == 0:
            print("Download completed")
            break

        commands.append(TMCLRequest(address=1, command=tmcl_opcode, command_type=tmcl_type, motor_bank=tmcl_motor, value=tmcl_value))

    if len(commands) == 0:
        print("No TMCL Script stored")
        sys.exit(1)

    print("Downloaded TMCL Script:")
    max_i = len(str(len(commands)))
    for i, cmd in enumerate(commands):
        print(f"    {i:{max_i}}: {cmd}")

    print("Done")

if __name__ == "__main__":
    main()
