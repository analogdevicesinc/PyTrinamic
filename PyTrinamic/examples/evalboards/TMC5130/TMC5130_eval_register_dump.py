'''
Created on 09.01.2019

@author: LK
'''

if __name__ == '__main__':
    pass

import PyTrinamic
from PyTrinamic.connections.serial_tmcl_interface import serial_tmcl_interface
from PyTrinamic.evalboards.TMC5130_eval import TMC5130_eval

PyTrinamic.showInfo()
PyTrinamic.showAvailableComPorts(USB=True)

myInterface = serial_tmcl_interface(PyTrinamic.firstAvailableComPort(USB=True))
TMC5130 = TMC5130_eval(myInterface)

print("GCONF:      " + str(TMC5130.readRegister(TMC5130.registers.GCONF)))
print("GSTAT:      " + str(TMC5130.readRegister(TMC5130.registers.GSTAT)))
print("IFCNT:      " + str(TMC5130.readRegister(TMC5130.registers.IFCNT)))
print("SLAVECONF:  " + str(TMC5130.readRegister(TMC5130.registers.SLAVECONF)))
print("INP_OUT:    " + str(TMC5130.readRegister(TMC5130.registers.INP_OUT)))
print("X_COMPARE:  " + str(TMC5130.readRegister(TMC5130.registers.X_COMPARE)))
print("IHOLD_IRUN: " + str(TMC5130.readRegister(TMC5130.registers.IHOLD_IRUN)))
print("TPOWERDOWN: " + str(TMC5130.readRegister(TMC5130.registers.TPOWERDOWN)))
print("TSTEP:      " + str(TMC5130.readRegister(TMC5130.registers.TSTEP)))
print("TPWMTHRS:   " + str(TMC5130.readRegister(TMC5130.registers.TPWMTHRS)))
print("TCOOLTHRS:  " + str(TMC5130.readRegister(TMC5130.registers.TCOOLTHRS)))
print("THIGH:      " + str(TMC5130.readRegister(TMC5130.registers.THIGH)))
print("RAMPMODE:   " + str(TMC5130.readRegister(TMC5130.registers.RAMPMODE)))
print("XACTUAL:    " + str(TMC5130.readRegister(TMC5130.registers.XACTUAL)))
print("VACTUAL:    " + str(TMC5130.readRegister(TMC5130.registers.VACTUAL)))
print("VSTART:     " + str(TMC5130.readRegister(TMC5130.registers.VSTART)))
print("A1:         " + str(TMC5130.readRegister(TMC5130.registers.A1)))
print("V1:         " + str(TMC5130.readRegister(TMC5130.registers.V1)))
print("AMAX:       " + str(TMC5130.readRegister(TMC5130.registers.AMAX)))
print("VMAX:       " + str(TMC5130.readRegister(TMC5130.registers.VMAX)))
print("DMAX:       " + str(TMC5130.readRegister(TMC5130.registers.DMAX)))
print("D1:         " + str(TMC5130.readRegister(TMC5130.registers.D1)))
print("VSTOP:      " + str(TMC5130.readRegister(TMC5130.registers.VSTOP)))
print("TZEROWAIT:  " + str(TMC5130.readRegister(TMC5130.registers.TZEROWAIT)))
print("XTARGET:    " + str(TMC5130.readRegister(TMC5130.registers.XTARGET)))
print("VDCMIN:     " + str(TMC5130.readRegister(TMC5130.registers.VDCMIN)))
print("SWMODE:     " + str(TMC5130.readRegister(TMC5130.registers.SWMODE)))
print("RAMPSTAT:   " + str(TMC5130.readRegister(TMC5130.registers.RAMPSTAT)))
print("XLATCH:     " + str(TMC5130.readRegister(TMC5130.registers.XLATCH)))
print("ENCMODE:    " + str(TMC5130.readRegister(TMC5130.registers.ENCMODE)))
print("XENC:       " + str(TMC5130.readRegister(TMC5130.registers.XENC)))
print("ENC_CONST:  " + str(TMC5130.readRegister(TMC5130.registers.ENC_CONST)))
print("ENC_STATUS: " + str(TMC5130.readRegister(TMC5130.registers.ENC_STATUS)))
print("ENC_LATCH:  " + str(TMC5130.readRegister(TMC5130.registers.ENC_LATCH)))
print("MSLUT0:     " + str(TMC5130.readRegister(TMC5130.registers.MSLUT0)))
print("MSLUT1:     " + str(TMC5130.readRegister(TMC5130.registers.MSLUT1)))
print("MSLUT2:     " + str(TMC5130.readRegister(TMC5130.registers.MSLUT2)))
print("MSLUT3:     " + str(TMC5130.readRegister(TMC5130.registers.MSLUT3)))
print("MSLUT4:     " + str(TMC5130.readRegister(TMC5130.registers.MSLUT4)))
print("MSLUT5:     " + str(TMC5130.readRegister(TMC5130.registers.MSLUT5)))
print("MSLUT6:     " + str(TMC5130.readRegister(TMC5130.registers.MSLUT6)))
print("MSLUT7:     " + str(TMC5130.readRegister(TMC5130.registers.MSLUT7)))
print("MSLUTSEL:   " + str(TMC5130.readRegister(TMC5130.registers.MSLUTSEL)))
print("MSLUTSTART: " + str(TMC5130.readRegister(TMC5130.registers.MSLUTSTART)))
print("MSCNT:      " + str(TMC5130.readRegister(TMC5130.registers.MSCNT)))
print("MSCURACT:   " + str(TMC5130.readRegister(TMC5130.registers.MSCURACT)))
print("CHOPCONF:   " + str(TMC5130.readRegister(TMC5130.registers.CHOPCONF)))
print("COOLCONF:   " + str(TMC5130.readRegister(TMC5130.registers.COOLCONF)))
print("DCCTRL:     " + str(TMC5130.readRegister(TMC5130.registers.DCCTRL)))
print("DRVSTATUS:  " + str(TMC5130.readRegister(TMC5130.registers.DRVSTATUS)))
print("PWMCONF:    " + str(TMC5130.readRegister(TMC5130.registers.PWMCONF)))
print("PWMSTATUS:  " + str(TMC5130.readRegister(TMC5130.registers.PWMSTATUS)))
print("ENCM_CTRL:  " + str(TMC5130.readRegister(TMC5130.registers.ENCM_CTRL)))
print("LOST_STEPS: " + str(TMC5130.readRegister(TMC5130.registers.LOST_STEPS)))

myInterface.close()