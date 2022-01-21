"""
Dump all register values of the TMC5062 IC.

The connection to a Landungsbrücke is established over USB. TMCL commands are used for communicating with the IC.
"""
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards import TMC5062_eval

PyTrinamic.show_info()

myInterface = ConnectionManager().connect()
print(myInterface)
TMC5062 = TMC5062_eval(myInterface)

print("GCONF:           0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.GCONF)))
print("GSTAT:           0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.GSTAT)))
print("SLAVECONF:       0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.SLAVECONF)))
print("INPUT:           0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.INPUT_OUTPUT)))
print("X_COMPARE:       0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.X_COMPARE)))

for i in range(2):
    print("Motor" + str(i) + ":")
    print("\tRAMPMODE:    0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.RAMPMODE[i])))
    print("\tXACTUAL:     0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.XACTUAL[i])))
    print("\tVACTUAL:     0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.VACTUAL[i])))
    print("\tVSTART:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.VSTART[i])))
    print("\tA1:          0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.A1[i])))
    print("\tV1:          0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.V1[i])))
    print("\tAMAX:        0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.AMAX[i])))
    print("\tVMAX:        0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.VMAX[i])))
    print("\tDMAX:        0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.DMAX[i])))
    print("\tD1:          0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.D1[i])))
    print("\tVSTOP:       0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.VSTOP[i])))
    print("\tTZEROWAIT:   0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.TZEROWAIT[i])))
    print("\tXTARGET:     0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.XTARGET[i])))
    print("\tIHOLD_IRUN:  0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.IHOLD_IRUN[i])))
    print("\tVCOOLTHRS:   0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.VCOOLTHRS[i])))
    print("\tVHIGH:       0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.VHIGH[i])))
    print("\tVDCMIN:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.VDCMIN[i])))
    print("\tSW_MODE:     0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.SW_MODE[i])))
    print("\tRAMP_STAT:   0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.RAMP_STAT[i])))
    print("\tXLATCH:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.XLATCH[i])))
    print("\tENCMODE:     0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.ENCMODE[i])))

    print("\tX_ENC:       0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.X_ENC[i])))
    print("\tENC_CONST:   0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.ENC_CONST[i])))
    print("\tENC_STATUS:  0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.ENC_STATUS[i])))
    print("\tENC_LATCH:   0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.ENC_LATCH[i])))

    print("\tMSLUT0:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUT0[i])))
    print("\tMSLUT1:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUT1[i])))
    print("\tMSLUT2:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUT2[i])))
    print("\tMSLUT3:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUT3[i])))
    print("\tMSLUT4:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUT4[i])))
    print("\tMSLUT5:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUT5[i])))
    print("\tMSLUT6:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUT6[i])))
    print("\tMSLUT7:      0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUT7[i])))
    print("\tMSLUTSEL:    0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUTSEL[i])))
    print("\tMSLUTSTART:  0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSLUTSTART[i])))

    print("\tMSCNT:       0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSCNT[i])))
    print("\tMSCURACT:    0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.MSCURACT[i])))
    print("\tCHOPCONF:    0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.CHOPCONF[i])))
    print("\tCOOLCONF:    0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.COOLCONF[i])))
    print("\tDRV_STATUS:  0x{0:08X}".format(TMC5062.read_register(TMC5062.registers.DRV_STATUS[i])))

myInterface.close()

print("\nReady.")
