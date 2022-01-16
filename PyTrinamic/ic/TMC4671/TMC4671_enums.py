class TMC4671_enums:
    """
    Defines all constants usable with the TMC4671.
    """
    # motor types
    MOTOR_TYPE_NO           = 0
    MOTOR_TYPE_DC           = 1
    MOTOR_TYPE_STEPPER      = 2
    MOTOR_TYPE_BLDC         = 3

    # PWM modes
    PWM_OFF_FREE_RUNNING    = 0
    PWM_OFF_LOW_SIDE_ON     = 1
    PWM_OFF_HIGH_SIDE_ON    = 2
    PWM_LOW_SIDE_CHOPPER    = 5
    PWM_HIGH_SIDE_CHOPPER   = 6
    PWM_CENTERED_FOR_FOC    = 7

    # motion modes
    MOTION_MODE_STOPPED     = 0
    MOTION_MODE_TORQUE      = 1
    MOTION_MODE_VELOCITY    = 2
    MOTION_MODE_POSITION    = 3
    MOTION_MODE_UQ_UD_EXT   = 8

    # phi_e selections
    PHI_E_EXTERNAL      = 1
    PHI_E_OPEN_LOOP     = 2
    PHI_E_ABN           = 3
    PHI_E_HALL          = 5
    PHI_E_AENC          = 6
    PHI_A_AENC          = 7

    # velocity/position selection
    VELOCITY_PHI_E_SELECTION    = 0
    VELOCITY_PHI_E_EXT          = 1
    VELOCITY_PHI_E_OPENLOOP     = 2
    VELOCITY_PHI_E_ABN          = 3
    VELOCITY_PHI_E_HAL          = 5
    VELOCITY_PHI_E_AENC         = 6
    VELOCITY_PHI_A_AENC         = 7
    VELOCITY_PHI_M_ABN          = 9
    VELOCITY_PHI_M_ABN_2        = 10
    VELOCITY_PHI_M_AENC         = 11
    VELOCITY_PHI_M_HAL          = 12
