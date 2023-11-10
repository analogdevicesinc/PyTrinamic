################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

"""Testing the all CAN Adapters in a combined Network

To recreate the tests create a CAN network by combining:
    * Kvaser Leaf Light v2
    * PEAK PCAN
    * Ixxat USB-to-CAN
    * CANable (Original)
    * 3x TMCM-1241 with CAN-ID 3,4 and 5
"""

import pytest

from pytrinamic.modules import TMCLModule

from pytrinamic.connections import ConnectionManager

from pytrinamic.connections import KvaserTmclInterface
from pytrinamic.connections import PcanTmclInterface
from pytrinamic.connections import SlcanTmclInterface
from pytrinamic.connections import IxxatTmclInterface

slcan_com_port = 'COM15'

ap = {
    'Maximum current': 6,
    'Microstep resolution': 140,
}


@pytest.fixture(scope='function', params=[
    KvaserTmclInterface,
    PcanTmclInterface,
    SlcanTmclInterface,
    IxxatTmclInterface,
])
def can_adapter(request):
    can_tmcl_interface_class = request.param
    if can_tmcl_interface_class == PcanTmclInterface:
        ports = PcanTmclInterface.list()
        adptr = can_tmcl_interface_class(port=ports[0])
    elif can_tmcl_interface_class == SlcanTmclInterface:
        adptr = can_tmcl_interface_class(com_port=slcan_com_port)
    else:
        adptr = can_tmcl_interface_class()
    yield adptr
    adptr.close()


def test_adapter_classes(can_adapter):
    tmcm1241s = [TMCLModule(can_adapter, module_id=mid) for mid in range(3, 6)]
    for tmcm1241 in tmcm1241s:
        assert tmcm1241.get_global_parameter(71, 0) == tmcm1241.module_id
        assert tmcm1241.get_axis_parameter(ap['Microstep resolution'], 0) == 8
    for tmcm1241 in tmcm1241s:
        tmcm1241.set_axis_parameter(ap['Maximum current'], 0, 10+tmcm1241.module_id)
        assert tmcm1241.get_axis_parameter(ap['Maximum current'], 0) == 10+tmcm1241.module_id
    for tmcm1241 in tmcm1241s:
        tmcm1241.set_axis_parameter(ap['Maximum current'], 0, 20+tmcm1241.module_id)
        assert tmcm1241.get_axis_parameter(ap['Maximum current'], 0) == 20+tmcm1241.module_id


@pytest.mark.parametrize('cm_call', [
    f"--interface ixxat_tmcl",
    f"--interface kvaser_tmcl",
    f"--interface pcan_tmcl",
    f"--interface slcan_tmcl --port {slcan_com_port}",
])
def test_connection_manager(cm_call):
    cm = ConnectionManager(cm_call)
    with cm.connect() as interface:
        tmcm1241s = [TMCLModule(interface, module_id=mid) for mid in range(3, 6)]
        for tmcm1241 in tmcm1241s:
            assert tmcm1241.get_global_parameter(71, 0) == tmcm1241.module_id
            assert tmcm1241.get_axis_parameter(ap['Microstep resolution'], 0) == 8
        for tmcm1241 in tmcm1241s:
            tmcm1241.set_axis_parameter(ap['Maximum current'], 0, 10+tmcm1241.module_id)
            assert tmcm1241.get_axis_parameter(ap['Maximum current'], 0) == 10+tmcm1241.module_id
        for tmcm1241 in tmcm1241s:
            tmcm1241.set_axis_parameter(ap['Maximum current'], 0, 20+tmcm1241.module_id)
            assert tmcm1241.get_axis_parameter(ap['Maximum current'], 0) == 20+tmcm1241.module_id

