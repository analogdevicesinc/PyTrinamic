################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Dump all register values of the TMC5031 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5031_eval

pytrinamic.show_info()

my_interface = ConnectionManager().connect()
print(my_interface)

eval_board = TMC5031_eval(my_interface)
mc = eval_board.ics[0]

print("Motion controller info: " + str(mc.get_info()))
print("Register dump for " + str(mc.get_name()) + ":")

print("GCONF:           0x{0:08X}".format(eval_board.read_register(mc.REG.GCONF)))
print("GSTAT:           0x{0:08X}".format(eval_board.read_register(mc.REG.GSTAT)))
print("SLAVECONF:       0x{0:08X}".format(eval_board.read_register(mc.REG.SLAVECONF)))
print("INPUT:           0x{0:08X}".format(eval_board.read_register(mc.REG.INPUT)))
print("X_COMPARE:       0x{0:08X}".format(eval_board.read_register(mc.REG.X_COMPARE)))

for i in range(2):
    print("Motor" + str(i) + ":")
    print("\tRAMPMODE:    0x{0:08X}".format(eval_board.read_register(mc.REG.RAMPMODE[i])))
    print("\tXACTUAL:     0x{0:08X}".format(eval_board.read_register(mc.REG.XACTUAL[i])))
    print("\tVACTUAL:     0x{0:08X}".format(eval_board.read_register(mc.REG.VACTUAL[i])))
    print("\tVSTART:      0x{0:08X}".format(eval_board.read_register(mc.REG.VSTART[i])))
    print("\tA1:          0x{0:08X}".format(eval_board.read_register(mc.REG.A1[i])))
    print("\tV1:          0x{0:08X}".format(eval_board.read_register(mc.REG.V1[i])))
    print("\tAMAX:        0x{0:08X}".format(eval_board.read_register(mc.REG.AMAX[i])))
    print("\tVMAX:        0x{0:08X}".format(eval_board.read_register(mc.REG.VMAX[i])))
    print("\tDMAX:        0x{0:08X}".format(eval_board.read_register(mc.REG.DMAX[i])))
    print("\tD1:          0x{0:08X}".format(eval_board.read_register(mc.REG.D1[i])))
    print("\tVSTOP:       0x{0:08X}".format(eval_board.read_register(mc.REG.VSTOP[i])))
    print("\tTZEROWAIT:   0x{0:08X}".format(eval_board.read_register(mc.REG.TZEROWAIT[i])))
    print("\tXTARGET:     0x{0:08X}".format(eval_board.read_register(mc.REG.XTARGET[i])))
    print("\tIHOLD_IRUN:  0x{0:08X}".format(eval_board.read_register(mc.REG.IHOLD_IRUN[i])))
    print("\tVCOOLTHRS:   0x{0:08X}".format(eval_board.read_register(mc.REG.VCOOLTHRS[i])))
    print("\tVHIGH:       0x{0:08X}".format(eval_board.read_register(mc.REG.VHIGH[i])))
    print("\tSW_MODE:     0x{0:08X}".format(eval_board.read_register(mc.REG.SW_MODE[i])))
    print("\tRAMP_STAT:   0x{0:08X}".format(eval_board.read_register(mc.REG.RAMP_STAT[i])))
    print("\tXLATCH:      0x{0:08X}".format(eval_board.read_register(mc.REG.XLATCH[i])))

    print("\tMSLUT0:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT0[i])))
    print("\tMSLUT1:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT1[i])))
    print("\tMSLUT2:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT2[i])))
    print("\tMSLUT3:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT3[i])))
    print("\tMSLUT4:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT4[i])))
    print("\tMSLUT5:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT5[i])))
    print("\tMSLUT6:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT6[i])))
    print("\tMSLUT7:      0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUT7[i])))
    print("\tMSLUTSEL:    0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSEL[i])))
    print("\tMSLUTSTART:  0x{0:08X}".format(eval_board.read_register(mc.REG.MSLUTSTART[i])))

    print("\tMSCNT:       0x{0:08X}".format(eval_board.read_register(mc.REG.MSCNT[i])))
    print("\tMSCURACT:    0x{0:08X}".format(eval_board.read_register(mc.REG.MSCURACT[i])))
    print("\tCHOPCONF:    0x{0:08X}".format(eval_board.read_register(mc.REG.CHOPCONF[i])))
    print("\tCOOLCONF:    0x{0:08X}".format(eval_board.read_register(mc.REG.COOLCONF[i])))
    print("\tDRV_STATUS:  0x{0:08X}".format(eval_board.read_register(mc.REG.DRV_STATUS[i])))

my_interface.close()

print("\nReady.")
