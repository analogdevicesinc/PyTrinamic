################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC5271 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""

import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5271_eval

pytrinamic.show_info()

my_interface = ConnectionManager().connect()
print(my_interface)
eval_board = TMC5271_eval(my_interface)
drv = eval_board.ics[0]

print("Driver info: " + str(drv.get_info()))
print("Register dump for " + str(drv.get_name()) + ":")

print("GCONF            : 0x{0:08X}".format(eval_board.read_register(drv.REG.GCONF)))
print("GSTAT            : 0x{0:08X}".format(eval_board.read_register(drv.REG.GSTAT)))
print("IFCNT            : 0x{0:08X}".format(eval_board.read_register(drv.REG.IFCNT)))
print("SLAVECONF        : 0x{0:08X}".format(eval_board.read_register(drv.REG.SLAVECONF)))
print("IOIN             : 0x{0:08X}".format(eval_board.read_register(drv.REG.IOIN)))
print("DRV_CONF         : 0x{0:08X}".format(eval_board.read_register(drv.REG.DRV_CONF)))
print("GLOBAL_SCALER    : 0x{0:08X}".format(eval_board.read_register(drv.REG.GLOBAL_SCALER)))
print("RAMPMODE         : 0x{0:08X}".format(eval_board.read_register(drv.REG.RAMPMODE)))
print("MSLUT_ADDR       : 0x{0:08X}".format(eval_board.read_register(drv.REG.MSLUT_ADDR)))
print("MSLUT_DATA       : 0x{0:08X}".format(eval_board.read_register(drv.REG.MSLUT_DATA)))
print("X_COMPARE        : 0x{0:08X}".format(eval_board.read_register(drv.REG.X_COMPARE)))
print("X_COMPARE_REPEAT : 0x{0:08X}".format(eval_board.read_register(drv.REG.X_COMPARE_REPEAT)))
print("IHOLD_IRUN       : 0x{0:08X}".format(eval_board.read_register(drv.REG.IHOLD_IRUN)))
print("TPOWERDOWN       : 0x{0:08X}".format(eval_board.read_register(drv.REG.TPOWERDOWN)))
print("TSTEP            : 0x{0:08X}".format(eval_board.read_register(drv.REG.TSTEP)))
print("TPWMTHRS         : 0x{0:08X}".format(eval_board.read_register(drv.REG.TPWMTHRS)))
print("TCOOLTHRS        : 0x{0:08X}".format(eval_board.read_register(drv.REG.TCOOLTHRS)))
print("THIGH            : 0x{0:08X}".format(eval_board.read_register(drv.REG.THIGH)))
print("XACTUAL          : 0x{0:08X}".format(eval_board.read_register(drv.REG.XACTUAL)))
print("VACTUAL          : 0x{0:08X}".format(eval_board.read_register(drv.REG.VACTUAL)))
print("AACTUAL          : 0x{0:08X}".format(eval_board.read_register(drv.REG.AACTUAL)))
print("VSTART           : 0x{0:08X}".format(eval_board.read_register(drv.REG.VSTART)))
print("A1               : 0x{0:08X}".format(eval_board.read_register(drv.REG.A1)))
print("V1               : 0x{0:08X}".format(eval_board.read_register(drv.REG.V1)))
print("A2               : 0x{0:08X}".format(eval_board.read_register(drv.REG.A2)))
print("V2               : 0x{0:08X}".format(eval_board.read_register(drv.REG.V2)))
print("AMAX             : 0x{0:08X}".format(eval_board.read_register(drv.REG.AMAX)))
print("VMAX             : 0x{0:08X}".format(eval_board.read_register(drv.REG.VMAX)))
print("DMAX             : 0x{0:08X}".format(eval_board.read_register(drv.REG.DMAX)))
print("D2               : 0x{0:08X}".format(eval_board.read_register(drv.REG.D2)))
print("D1               : 0x{0:08X}".format(eval_board.read_register(drv.REG.D1)))
print("VSTOP            : 0x{0:08X}".format(eval_board.read_register(drv.REG.VSTOP)))
print("TVMAX            : 0x{0:08X}".format(eval_board.read_register(drv.REG.TVMAX)))
print("TZEROWAIT        : 0x{0:08X}".format(eval_board.read_register(drv.REG.TZEROWAIT)))
print("XTARGET          : 0x{0:08X}".format(eval_board.read_register(drv.REG.XTARGET)))
print("VDCMIN           : 0x{0:08X}".format(eval_board.read_register(drv.REG.VDCMIN)))
print("SW_MODE          : 0x{0:08X}".format(eval_board.read_register(drv.REG.SW_MODE)))
print("RAMP_STAT        : 0x{0:08X}".format(eval_board.read_register(drv.REG.RAMP_STAT)))
print("XLATCH           : 0x{0:08X}".format(eval_board.read_register(drv.REG.XLATCH)))
print("POSITION_PI_CTRL : 0x{0:08X}".format(eval_board.read_register(drv.REG.POSITION_PI_CTRL)))
print("X_ENC            : 0x{0:08X}".format(eval_board.read_register(drv.REG.X_ENC)))
print("ENCMODE          : 0x{0:08X}".format(eval_board.read_register(drv.REG.ENCMODE)))
print("ENC_CONST        : 0x{0:08X}".format(eval_board.read_register(drv.REG.ENC_CONST)))
print("ENC_STATUS       : 0x{0:08X}".format(eval_board.read_register(drv.REG.ENC_STATUS)))
print("ENC_LATCH        : 0x{0:08X}".format(eval_board.read_register(drv.REG.ENC_LATCH)))
print("ENC_DEVIATION    : 0x{0:08X}".format(eval_board.read_register(drv.REG.ENC_DEVIATION)))
print("VIRTUAL_STOP_L   : 0x{0:08X}".format(eval_board.read_register(drv.REG.VIRTUAL_STOP_L)))
print("VIRTUAL_STOP_R   : 0x{0:08X}".format(eval_board.read_register(drv.REG.VIRTUAL_STOP_R)))
print("MSCNT            : 0x{0:08X}".format(eval_board.read_register(drv.REG.MSCNT)))
print("MSCURACT         : 0x{0:08X}".format(eval_board.read_register(drv.REG.MSCURACT)))
print("CHOPCONF         : 0x{0:08X}".format(eval_board.read_register(drv.REG.CHOPCONF)))
print("COOLCONF         : 0x{0:08X}".format(eval_board.read_register(drv.REG.COOLCONF)))
print("DCCTRL           : 0x{0:08X}".format(eval_board.read_register(drv.REG.DCCTRL)))
print("DRV_STATUS       : 0x{0:08X}".format(eval_board.read_register(drv.REG.DRV_STATUS)))
print("PWMCONF          : 0x{0:08X}".format(eval_board.read_register(drv.REG.PWMCONF)))
print("PWM_SCALE        : 0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_SCALE)))
print("PWM_AUTO         : 0x{0:08X}".format(eval_board.read_register(drv.REG.PWM_AUTO)))
print("SG4_THRS         : 0x{0:08X}".format(eval_board.read_register(drv.REG.SG4_THRS)))
print("SG4_RESULT       : 0x{0:08X}".format(eval_board.read_register(drv.REG.SG4_RESULT)))
print("SG4_IND          : 0x{0:08X}".format(eval_board.read_register(drv.REG.SG4_IND)))

my_interface.close()

print("\nReady.")
