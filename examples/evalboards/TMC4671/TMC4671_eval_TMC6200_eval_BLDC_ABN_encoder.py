import time
import pytrinamic2
from pytrinamic2.connections.connection_manager import ConnectionManager
from pytrinamic2.evalboards import TMC4671_eval
from pytrinamic2.evalboards import TMC6200_eval

pytrinamic2.show_info()

myInterface = ConnectionManager().connect()
print(myInterface)

with myInterface:
    # Create TMC4671-EVAL and TMC6200-EVAL class which communicate over the Landungsbrücke via TMCL
    TMC4671 = TMC4671_eval(myInterface)
    TMC6200 = TMC6200_eval(myInterface)

    # Configure TMC6100 pwm for use with TMC4671 (disable singleline)
    TMC6200.write_register_field(TMC6200.fields.SINGLELINE, 0)

    # Configure TMC4671 for a BLDC motor with ABN-Encoder

    # Motor type & PWM configuration
    TMC4671.write_register_field(TMC4671.fields.MOTOR_TYPE, TMC4671.ENUMs.MOTOR_TYPE_BLDC)
    TMC4671.write_register_field(TMC4671.fields.N_POLE_PAIRS, 4)
    TMC4671.write_register(TMC4671.registers.PWM_POLARITIES, 0x00000000)
    TMC4671.write_register(TMC4671.registers.PWM_MAXCNT, int(0x00000F9F))
    TMC4671.write_register(TMC4671.registers.PWM_BBM_H_BBM_L, 0x00001414)
    TMC4671.write_register_field(TMC4671.fields.PWM_CHOP, TMC4671.ENUMs.PWM_CENTERED_FOR_FOC)
    TMC4671.write_register_field(TMC4671.fields.PWM_SV, 1)

    # ADC configuration
    TMC4671.write_register(TMC4671.registers.ADC_I_SELECT, 0x24000100)
    TMC4671.write_register(TMC4671.registers.dsADC_MCFG_B_MCFG_A, 0x00100010)
    TMC4671.write_register(TMC4671.registers.dsADC_MCLK_A, 0x20000000)
    TMC4671.write_register(TMC4671.registers.dsADC_MCLK_B, 0x00000000)
    TMC4671.write_register(TMC4671.registers.dsADC_MDEC_B_MDEC_A, int(0x014E014E))
    TMC4671.write_register(TMC4671.registers.ADC_I0_SCALE_OFFSET, 0xFF00826D)
    TMC4671.write_register(TMC4671.registers.ADC_I1_SCALE_OFFSET, 0xFF0081F8)

    # ABN encoder settings
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_MODE, 0x00001000)
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_PPR, 4096)
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0)

    # Limits
    TMC4671.write_register(TMC4671.registers.PID_TORQUE_FLUX_LIMITS, 1000)

    # PI settings
    TMC4671.write_register(TMC4671.registers.PID_TORQUE_P_TORQUE_I, 0x01000100)
    TMC4671.write_register(TMC4671.registers.PID_FLUX_P_FLUX_I, 0x01000100)

    # ===== ABN encoder test drive =====

    # Init encoder (mode 0)
    print("Initializing Encoder...")
    TMC4671.write_register(TMC4671.registers.MODE_RAMP_MODE_MOTION, 0x00000008)
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x00000000)
    TMC4671.write_register(TMC4671.registers.PHI_E_SELECTION, TMC4671.ENUMs.PHI_E_EXTERNAL)
    TMC4671.write_register(TMC4671.registers.PHI_E_EXT, 0x00000000)
    TMC4671.write_register(TMC4671.registers.UQ_UD_EXT, 2000)
    time.sleep(1)

    # Clear abn_decoder_count
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_COUNT, 0)

    # Feedback selection
    TMC4671.write_register(TMC4671.registers.PHI_E_SELECTION, TMC4671.ENUMs.PHI_E_ABN)
    TMC4671.write_register(TMC4671.registers.VELOCITY_SELECTION, TMC4671.ENUMs.VELOCITY_PHI_M_ABN)

    # Switch to torque mode
    TMC4671.write_register(TMC4671.registers.MODE_RAMP_MODE_MOTION, TMC4671.ENUMs.MOTION_MODE_TORQUE)

    # Rotate right
    print("Rotate right...")
    TMC4671.write_register(TMC4671.registers.PID_TORQUE_FLUX_TARGET, 0x03E80000)
    time.sleep(3)

    # Rotate left
    print("Rotate left...")
    TMC4671.write_register(TMC4671.registers.PID_TORQUE_FLUX_TARGET, int(0xFC180000))
    time.sleep(3)

    # Stop
    print("Stop...")
    TMC4671.write_register(TMC4671.registers.PID_TORQUE_FLUX_TARGET, 0)

    myInterface.close()

print("\nReady.")
