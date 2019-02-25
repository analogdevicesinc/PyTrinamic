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
PyTrinamic.showAvailableComPorts()

myInterface = serial_tmcl_interface('COM5')
tmc5130_eval = TMC5130_eval(myInterface)
tmc5130_reg = tmc5130_eval.register()

print("GCONF:      " + str(tmc5130_eval.readRegister(tmc5130_reg.GCONF)))
print("GSTAT:      " + str(tmc5130_eval.readRegister(tmc5130_reg.GSTAT)))
print("IFCNT:      " + str(tmc5130_eval.readRegister(tmc5130_reg.IFCNT)))
print("SLAVECONF:  " + str(tmc5130_eval.readRegister(tmc5130_reg.SLAVECONF)))
print("INP_OUT:    " + str(tmc5130_eval.readRegister(tmc5130_reg.INP_OUT)))
print("X_COMPARE:  " + str(tmc5130_eval.readRegister(tmc5130_reg.X_COMPARE)))
print("IHOLD_IRUN: " + str(tmc5130_eval.readRegister(tmc5130_reg.IHOLD_IRUN)))
print("TPOWERDOWN: " + str(tmc5130_eval.readRegister(tmc5130_reg.TPOWERDOWN)))
print("TSTEP:      " + str(tmc5130_eval.readRegister(tmc5130_reg.TSTEP)))
print("TPWMTHRS:   " + str(tmc5130_eval.readRegister(tmc5130_reg.TPWMTHRS)))
print("TCOOLTHRS:  " + str(tmc5130_eval.readRegister(tmc5130_reg.TCOOLTHRS)))
print("THIGH:      " + str(tmc5130_eval.readRegister(tmc5130_reg.THIGH)))
print("RAMPMODE:   " + str(tmc5130_eval.readRegister(tmc5130_reg.RAMPMODE)))
print("XACTUAL:    " + str(tmc5130_eval.readRegister(tmc5130_reg.XACTUAL)))
print("VACTUAL:    " + str(tmc5130_eval.readRegister(tmc5130_reg.VACTUAL)))
print("VSTART:     " + str(tmc5130_eval.readRegister(tmc5130_reg.VSTART)))
print("A1:         " + str(tmc5130_eval.readRegister(tmc5130_reg.A1)))
print("V1:         " + str(tmc5130_eval.readRegister(tmc5130_reg.V1)))
print("AMAX:       " + str(tmc5130_eval.readRegister(tmc5130_reg.AMAX)))
print("VMAX:       " + str(tmc5130_eval.readRegister(tmc5130_reg.VMAX)))
print("DMAX:       " + str(tmc5130_eval.readRegister(tmc5130_reg.DMAX)))
print("D1:         " + str(tmc5130_eval.readRegister(tmc5130_reg.D1)))
print("VSTOP:      " + str(tmc5130_eval.readRegister(tmc5130_reg.VSTOP)))
print("TZEROWAIT:  " + str(tmc5130_eval.readRegister(tmc5130_reg.TZEROWAIT)))
print("XTARGET:    " + str(tmc5130_eval.readRegister(tmc5130_reg.XTARGET)))
print("VDCMIN:     " + str(tmc5130_eval.readRegister(tmc5130_reg.VDCMIN)))
print("SWMODE:     " + str(tmc5130_eval.readRegister(tmc5130_reg.SWMODE)))
print("RAMPSTAT:   " + str(tmc5130_eval.readRegister(tmc5130_reg.RAMPSTAT)))
print("XLATCH:     " + str(tmc5130_eval.readRegister(tmc5130_reg.XLATCH)))
print("ENCMODE:    " + str(tmc5130_eval.readRegister(tmc5130_reg.ENCMODE)))
print("XENC:       " + str(tmc5130_eval.readRegister(tmc5130_reg.XENC)))
print("ENC_CONST:  " + str(tmc5130_eval.readRegister(tmc5130_reg.ENC_CONST)))
print("ENC_STATUS: " + str(tmc5130_eval.readRegister(tmc5130_reg.ENC_STATUS)))
print("ENC_LATCH:  " + str(tmc5130_eval.readRegister(tmc5130_reg.ENC_LATCH)))
print("MSLUT0:     " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUT0)))
print("MSLUT1:     " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUT1)))
print("MSLUT2:     " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUT2)))
print("MSLUT3:     " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUT3)))
print("MSLUT4:     " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUT4)))
print("MSLUT5:     " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUT5)))
print("MSLUT6:     " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUT6)))
print("MSLUT7:     " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUT7)))
print("MSLUTSEL:   " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUTSEL)))
print("MSLUTSTART: " + str(tmc5130_eval.readRegister(tmc5130_reg.MSLUTSTART)))
print("MSCNT:      " + str(tmc5130_eval.readRegister(tmc5130_reg.MSCNT)))
print("MSCURACT:   " + str(tmc5130_eval.readRegister(tmc5130_reg.MSCURACT)))
print("CHOPCONF:   " + str(tmc5130_eval.readRegister(tmc5130_reg.CHOPCONF)))
print("COOLCONF:   " + str(tmc5130_eval.readRegister(tmc5130_reg.COOLCONF)))
print("DCCTRL:     " + str(tmc5130_eval.readRegister(tmc5130_reg.DCCTRL)))
print("DRVSTATUS:  " + str(tmc5130_eval.readRegister(tmc5130_reg.DRVSTATUS)))
print("PWMCONF:    " + str(tmc5130_eval.readRegister(tmc5130_reg.PWMCONF)))
print("PWMSTATUS:  " + str(tmc5130_eval.readRegister(tmc5130_reg.PWMSTATUS)))
print("ENCM_CTRL:  " + str(tmc5130_eval.readRegister(tmc5130_reg.ENCM_CTRL)))
print("LOST_STEPS: " + str(tmc5130_eval.readRegister(tmc5130_reg.LOST_STEPS)))

myInterface.close()