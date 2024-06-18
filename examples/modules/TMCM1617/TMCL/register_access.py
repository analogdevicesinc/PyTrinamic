################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1617

pytrinamic.show_info()
# connection_manager = ConnectionManager("--interface serial_tmcl --port COM4 --data-rate 115200")
connection_manager = ConnectionManager("--interface kvaser_tmcl --module-id 1")

with connection_manager.connect() as my_interface:

    # the module
    module = TMCM1617(my_interface)

    # axis parameter based feature access
    motor = module.motors[0]

    # direct register access to motion controller and driver
    mc_index = 0
    mc = module.ics[mc_index]

    drv_index = 1
    drv = module.ics[drv_index]

    print("\nMotionController: " + mc.get_name())
    print(mc.get_info())

    module.write_register(mc_index, mc.REG.CHIPINFO_ADDR, mc.VARIANT.CHIPINFO_ADDR_SI_TYPE)
    print("\tSI_TYPE:    0x{0:08X}".format(module.read_register(mc_index, mc.REG.CHIPINFO_DATA)))

    module.write_register(mc_index, mc.REG.CHIPINFO_ADDR, mc.VARIANT.CHIPINFO_ADDR_SI_VERSION)
    print("\tSI_VERSION: 0x{0:08X}".format(module.read_register(mc_index, mc.REG.CHIPINFO_DATA)))

    module.write_register(mc_index, mc.REG.CHIPINFO_ADDR, mc.VARIANT.CHIPINFO_ADDR_SI_DATE)
    print("\tSI_DATE:    0x{0:08X}".format(module.read_register(mc_index, mc.REG.CHIPINFO_DATA)))

    print("\nDriver: " + drv.get_name())
    print(drv.get_info())
    print("\tSI_VERSION:    0x{0:08X}".format(module.read_register_field(drv_index, drv.FIELD.VERSION)))
    print("\n")

print("\nReady.")
