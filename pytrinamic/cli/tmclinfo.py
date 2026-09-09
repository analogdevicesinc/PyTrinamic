#!/usr/bin/env python
################################################################################
# Copyright © 2026 Analog Devices, Inc.
################################################################################
import argparse
import logging
import sys

import pytrinamic
import pytrinamic.tmcl
from pytrinamic.connections.connection_manager import ConnectionManager


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

    module_id         = tmcl.get_info("FWModuleID")
    firmware_version  = tmcl.get_info("FWVersion")
    fw_capability     = tmcl.get_info("FWCapability")
    fw_release_type   = tmcl.get_info("FWReleaseType")
    git_info          = tmcl.get_info("GitHash")

    device_specific_values = {}
    for i in range(200, 240+1):
        try:
            device_specific_values[i] = tmcl.get_info(i)
        except pytrinamic.tmcl.GetInfoRequestError:
            pass

    print(f"Module ID:        {module_id}")
    print(f"Firmware version: {firmware_version}")
    print(f"Firmware type:    {fw_capability}")
    print(f"Firmware release: {fw_release_type}")
    print(f"Git info:         {git_info}")

    if len(device_specific_values) > 0:
        print()
        print("Device specific values:")
        for k, v in device_specific_values.items():
            print(f"{k}:              {v} (0x{v:08X})")

    if fw_release_type.value != fw_release_type.LOCAL and git_info.hash == 0 and git_info.dirty_flag == 0:
        print("Error: Connected release firmware is missing git version information!")

if __name__ == "__main__":
    main()
