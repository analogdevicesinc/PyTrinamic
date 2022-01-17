import time
import PyTrinamic
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.evalboards import TMC4671_eval
from PyTrinamic.ic import TMC4671 as TMC4671_IC

PyTrinamic.show_info()

myInterface = ConnectionManager().connect()
# myInterface.enable_debug(True)
print(myInterface)

with myInterface:

    if myInterface.supports_tmcl():
        # Create an TMC4671-EVAL class which communicates over the Landungsbrücke via TMCL
        TMC4671 = TMC4671_eval(myInterface)
    else:
        # Create an TMC4671 IC class which communicates directly over UART
        TMC4671 = TMC4671_IC(myInterface)

    # Configure TMC4671 for a BLDC motor in open loop mode

    # Motor type & PWM configuration
    TMC4671.write_register_field(TMC4671.fields.MOTOR_TYPE, TMC4671.ENUMs.MOTOR_TYPE_BLDC)
    TMC4671.write_register_field(TMC4671.fields.N_POLE_PAIRS, 4)
    TMC4671.write_register(TMC4671.registers.PWM_POLARITIES, 0x00000000)
    TMC4671.write_register(TMC4671.registers.PWM_MAXCNT, int(0x00000F9F))
    TMC4671.write_register(TMC4671.registers.PWM_BBM_H_BBM_L, 0x00000A0A)
    TMC4671.write_register_field(TMC4671.fields.PWM_CHOP, TMC4671.ENUMs.PWM_CENTERED_FOR_FOC)
    TMC4671.write_register_field(TMC4671.fields.PWM_SV, 1)

    # ADC configuration
    TMC4671.write_register(TMC4671.registers.ADC_I_SELECT, 0x18000100)
    TMC4671.write_register(TMC4671.registers.dsADC_MCFG_B_MCFG_A, 0x00100010)
    TMC4671.write_register(TMC4671.registers.dsADC_MCLK_A, 0x20000000)
    TMC4671.write_register(TMC4671.registers.dsADC_MCLK_B, 0x00000000)
    TMC4671.write_register(TMC4671.registers.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
    TMC4671.write_register(TMC4671.registers.ADC_I0_SCALE_OFFSET, 0x01008218)
    TMC4671.write_register(TMC4671.registers.ADC_I1_SCALE_OFFSET, 0x0100820A)

    # Open loop settings
    TMC4671.write_register(TMC4671.registers.OPENLOOP_MODE, 0x00000000)
    TMC4671.write_register(TMC4671.registers.OPENLOOP_ACCELERATION, 100)

    # Feedback selection
    TMC4671.write_register(TMC4671.registers.PHI_E_SELECTION, TMC4671.ENUMs.PHI_E_OPEN_LOOP)
    TMC4671.write_register(TMC4671.registers.UQ_UD_EXT, 2000)

    # ===== Open loop test drive =====

    # Switch to open loop velocity mode
    TMC4671.write_register(TMC4671.registers.MODE_RAMP_MODE_MOTION, TMC4671.ENUMs.MOTION_MODE_UQ_UD_EXT)

    # Rotate right
    print("Rotate right...")
    TMC4671.write_register(TMC4671.registers.OPENLOOP_VELOCITY_TARGET, 200)
    time.sleep(3)

    # Rotate left
    print("Rotate left...")
    TMC4671.write_register(TMC4671.registers.OPENLOOP_VELOCITY_TARGET, -200)
    time.sleep(6)

    # Stop
    print("Stop...")
    TMC4671.write_register(TMC4671.registers.OPENLOOP_VELOCITY_TARGET, 0)
    time.sleep(3)

    # Unpower
    print("Unpowered...")
    TMC4671.write_register(TMC4671.registers.UQ_UD_EXT, 0)

    myInterface.close()

print("\nReady.")
