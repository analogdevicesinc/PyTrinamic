import time
import pytrinamic2
from pytrinamic2.connections.connection_manager import ConnectionManager
from pytrinamic2.evalboards import TMC4671_eval
from pytrinamic2.ic import TMC4671 as TMC4671_IC

pytrinamic2.show_info()

myInterface = ConnectionManager().connect()
print(myInterface)

with myInterface:

    if myInterface.supports_tmcl():
        # Create an TMC4671-EVAL class which communicates over the Landungsbrücke via TMCL
        TMC4671 = TMC4671_eval(myInterface)
    else:
        # Create an TMC4671 IC class which communicates directly over UART
        TMC4671 = TMC4671_IC(myInterface)

    # ===== 1) Base configuration =====

    pole_pairs = 4
    encoder_resolution = 4096

    # Motor type & PWM configuration
    TMC4671.write_register_field(TMC4671.fields.MOTOR_TYPE, TMC4671.ENUMs.MOTOR_TYPE_BLDC)
    TMC4671.write_register_field(TMC4671.fields.N_POLE_PAIRS, pole_pairs)
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
#    TMC4671.write_register(TMC4671.registers.ADC_I0_SCALE_OFFSET, 0x01008218)
#    TMC4671.write_register(TMC4671.registers.ADC_I1_SCALE_OFFSET, 0x0100820A)
    TMC4671.write_register(TMC4671.registers.ADC_I0_SCALE_OFFSET, 0x01005D87)
    TMC4671.write_register(TMC4671.registers.ADC_I1_SCALE_OFFSET, 0x01005E0B)

    # ABN encoder settings
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_MODE, 0x00001000)
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_PPR, encoder_resolution)
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0)

    # Open loop settings
    TMC4671.write_register(TMC4671.registers.OPENLOOP_MODE, 0x00000000)
    TMC4671.write_register(TMC4671.registers.OPENLOOP_ACCELERATION, 100)

    # Limits
    TMC4671.write_register(TMC4671.registers.PID_TORQUE_FLUX_LIMITS, 1000)

    # PI settings
    TMC4671.write_register(TMC4671.registers.PID_TORQUE_P_TORQUE_I, 0x01000100)
    TMC4671.write_register(TMC4671.registers.PID_FLUX_P_FLUX_I, 0x01000100)

    # ===== 2) Estimate the encoder offset =====

    # Init encoder (mode 0)
    # Put a voltage on the motor and wait 1 second for alignment
    TMC4671.write_register(TMC4671.registers.MODE_RAMP_MODE_MOTION, 0x00000008)
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, 0x00000000)
    TMC4671.write_register(TMC4671.registers.PHI_E_SELECTION, TMC4671.ENUMs.PHI_E_EXTERNAL)
    TMC4671.write_register(TMC4671.registers.PHI_E_EXT, 0x00000000)
    TMC4671.write_register(TMC4671.registers.UQ_UD_EXT, 2000)
    time.sleep(1)

    # Clear abn_decoder_count
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_COUNT, 0)

    print("abn_decoder_count:" + str(TMC4671.read_register(TMC4671.registers.ABN_DECODER_COUNT)))

    # Switch to open loop velocity mode
    TMC4671.write_register(TMC4671.registers.PHI_E_SELECTION, TMC4671.ENUMs.PHI_E_OPEN_LOOP)
    TMC4671.write_register(TMC4671.registers.OPENLOOP_VELOCITY_TARGET, 60)

    start_time = time.time()
    while True:
        print("dec: " + str(TMC4671.read_register(TMC4671.registers.ABN_DECODER_COUNT)) +
              " dec_n: " + str(TMC4671.read_register(TMC4671.registers.ABN_DECODER_COUNT_N)))

        # Stop after 3 seconds
        if (time.time() - start_time) > 3:
            break

    # Read encoder offset at N channel
    decoder_count_n = TMC4671.read_register(TMC4671.registers.ABN_DECODER_COUNT_N)
    decoder_count_n_offset = decoder_count_n % (encoder_resolution / pole_pairs)

    print("abn_decoder_count_n:" + str(decoder_count_n))
    print("=> estimated encoder offset: " + str(decoder_count_n_offset))

    # ===== 3) Use the estimated offset =====

    # Write offset
    TMC4671.write_register(TMC4671.registers.ABN_DECODER_PHI_E_PHI_M_OFFSET, int(decoder_count_n_offset))

    #  ===== 4) Go to encoder mode =====

    # Feedback selection
    TMC4671.write_register(TMC4671.registers.PHI_E_SELECTION, TMC4671.ENUMs.PHI_E_ABN)
    TMC4671.write_register(TMC4671.registers.VELOCITY_SELECTION, TMC4671.ENUMs.VELOCITY_PHI_M_ABN)

    # Switch to torque mode
    TMC4671.write_register(TMC4671.registers.MODE_RAMP_MODE_MOTION, TMC4671.ENUMs.MOTION_MODE_TORQUE)

    # ===== 5) Make a test drive =====

    max_velocity = 0
    min_velocity = 0

    print("Rotate right...")
    TMC4671.write_register_field(TMC4671.fields.PID_TORQUE_TARGET, 1000)

    start_time = time.time()
    while True:
        velocity = TMC4671.read_register(TMC4671.registers.PID_VELOCITY_ACTUAL, signed=True)
        print("velocity: " + str(velocity))
        if velocity > max_velocity:
            max_velocity = velocity

        # Stop after 3 seconds
        if (time.time() - start_time) > 2:
            break

    print("Rotate left...")
    TMC4671.write_register_field(TMC4671.fields.PID_TORQUE_TARGET, -1000)

    start_time = time.time()
    while True:
        velocity = TMC4671.read_register(TMC4671.registers.PID_VELOCITY_ACTUAL, signed=True)
        print("velocity: " + str(velocity))
        if velocity < min_velocity:
            min_velocity = velocity

        # Stop after 3 seconds
        if (time.time() - start_time) > 2:
            break

    print("Stop motor")
    TMC4671.write_register(TMC4671.registers.PID_TORQUE_FLUX_TARGET, 0)

    # ===== 6) Short summary =====

    print(" === Summary === ")
    print("abn_decoder_count_n:" + str(decoder_count_n))
    print("estimated_encoder_offset: " + str(decoder_count_n_offset))
    print("max_velocity:" + str(max_velocity))
    print("min_velocity:" + str(min_velocity))

    myInterface.close()

print("\nReady.")
