################################################################################
# Copyright © 2021 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

if __name__ == '__main__':
    pass

import pytrinamic
import time
from pytrinamic.connections.connection_manager import ConnectionManager

from TMCM1690.TMCM1690 import TMCM1690

pytrinamic.show_info()

" please select your CAN adapter "
# myInterface = ConnectionManager("--interface pcan_tmcl").connect()
myInterface = ConnectionManager("--interface kvaser_tmcl").connect()
# myInterface = ConnectionManager("--interface serial_tmcl").connect()

module = TMCM1690(myInterface)
print(module)
motor = module.motors[0]

"""
    Define motor configuration for the TMCM-1690_DEV.

    The configuration is based on our standard BLDC motor (QBL4208-61-04-013-1024-AT).
    If you use a different motor be sure you have the right configuration setup otherwise the script may not work.
"""

" motor configuration "
motor.drive_settings.set_motor_type(motor.ENUM.MOTOR_TYPE_THREE_PHASE_BLDC)
motor.drive_settings.set_pole_pairs(4)
motor.drive_settings.set_max_current(2000)
print(motor.drive_settings)

" absolute encoder configuration "
motor.abs_encoder.set_type(motor.ENUM.ABS_ENCODER_AM4096)
motor.abs_encoder.set_direction(1)
motor.abs_encoder.set_init_mode(motor.ENUM.ABS_ENCODER_INIT_MODE_USE_OFFSET)

" motion settings "
motor.ramp_settings.set_max_velocity(2000)
motor.ramp_settings.set_max_acceleration(4000)
motor.ramp_settings.set_ramp_enabled(1)
motor.drive_settings.set_target_reached_distance(50)
motor.drive_settings.set_target_reached_velocity(500)
print(motor.ramp_settings)

" PI configuration "
motor.pid.set_torque_p_parameter(300)
motor.pid.set_torque_i_parameter(600)
motor.pid.set_velocity_p_parameter(300)
motor.pid.set_velocity_i_parameter(600)
motor.pid.set_position_p_parameter(10)

" Clear flags "
motor.set_axis_parameter(motor.AP.IITClearIITExceedFlags, 0)
motor.set_axis_parameter(motor.AP.ClearVelocityWindowFlag, 0)
motor.set_axis_parameter(motor.AP.PositionWindow, 1638400)
motor.set_axis_parameter(motor.AP.ClearPositionWindowFlag, 0)
motor.brake_chopper.set_enable_parameter(0)

" set commutation mode to absolute encoder "
motor.drive_settings.set_commutation_mode(motor.ENUM.COMM_MODE_FOC_ABS_ENCODER)

" set position counter to zero"
motor.set_actual_position(0)

" move to zero position"
motor.set_target_position(0)

" using sine ramp "
motor.ramp_settings.set_ramp_type(1)

print("starting positioning")
motor.set_target_position(640000)

" wait for position reached "
while not motor.get_position_reached():
    print("target position: %d | actual position: %d" % (motor.get_target_position(), motor.get_actual_position()))
    time.sleep(0.2)

" using linear ramp "
motor.ramp_settings.set_ramp_type(0)

" move back to zero"
motor.set_target_position(0)

" wait for position reached "
while not motor.get_position_reached():
    print("target position: %d | actual position: %d" % (motor.get_target_position(), motor.get_actual_position()))
    time.sleep(0.2)

myInterface.close()
print("\nReady.")
