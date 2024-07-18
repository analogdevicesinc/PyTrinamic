################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

"""
Move a motor back and forth using velocity and position mode of the TMC5130

Line 31, we set a lower run/standby current for the motor. Using NEMA17, this should result in a coil current around 800mA.
If the motor is stalling due to too low current, set motorCurrent higher.
If a lower value still is needed, set GLOBAL_SCALER register to 128 to half motor current.

In the end, the script  has  3 plots of position, velocity and acceleration
The acceleration is calculated. Position and speed are read out. The values are not the actual ones.

In the current configuration, it uses a sixPoint ramp. That improves the control system ability.

"""
import time
import pytrinamic

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5130_eval
from pytrinamic.helpers import to_signed_32

micro_steps_per_mechanical_revolution = 53687   # unit [ppt] = [µsteps / t]

M_RES = 0
def step2rotation(x):  # | converting Microsteps in rotation or rps or rps^2
    return x / (micro_steps_per_mechanical_revolution / pow(2, M_RES))
def rotation2step(x):  # | converting  rotation or rps or rps^2 in Microsteps
    return round(x * (micro_steps_per_mechanical_revolution / pow(2, M_RES)))

pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create TMC5130-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5130_eval(my_interface)
    mc = eval_board.ics[0]
    motor = eval_board.motors[0]

    # it can be used with "Trapezoid Mode" (tapez.) : acceleration, constant speed, deacceleration
    # or the "6 Point Mode" where the acceleration and deceleration, are splitted in two stages
    # For "Trapezoid Mode" set A1 = D1 = AMAX = DMAX
    # For symmetric "6 Point Mode" set V >>A1 = D1 > Amax = DMAX -> this is the mode right now

    print("Preparing parameters...")

    # Set - ramp - parameters
    #########################                                       # Name   |  Unit  |  Mode   |           Task
    eval_board.write_register(mc.REG.A1, rotation2step(0.018))      # A1     |  rps^2 | 6 piont | initial acceleration between VSTART and V1
    eval_board.write_register(mc.REG.AMAX, rotation2step(0.018))    # AMAX   |  rps^2 | trapez. | accelaration in the end
    eval_board.write_register(mc.REG.V1, rotation2step(2))          # V1     |  rps   |         | threshold for the  first acceleration phase
    eval_board.write_register(mc.REG.D1, rotation2step(0.018))      # D1     |  rps^2 | 6 piont | de/acceleration in the  end / start
    eval_board.write_register(mc.REG.DMAX, rotation2step(0.018))    # DMAX   |  rps^2 | trapez. | initial deacceleration
    eval_board.write_register(mc.REG.VSTART, 0)                     # VSTART | µsteps |         | Motor start velocity
    eval_board.write_register(mc.REG.VSTOP, 10)                     # VSTOP  | µsteps |         | Motor stop velocity threshold
    v_max = rotation2step(4)                                        #        |  rps   |         | max velocity = 4 rps

    # Set - other - parameters
    #########################                               # Name    |         Task
    eval_board.write_register_field(mc.FIELD.XACTUAL, 0)    # XACTUAL | Clear actual positions
    eval_board.write_register_field(mc.FIELD.VMAX, v_max)   # VMAX    | set max velocity
    eval_board.write_register_field(mc.FIELD.IRUN, 1)       # IRUM    | set the standstill current
    eval_board.write_register_field(mc.FIELD.IHOLD, 1)      # IHOLD   | set Motor run current
    eval_board.write_register_field(mc.FIELD.MRES, M_RES)   # MRES    | set Microstep resolution (don't change!)
                                                            #         | (have a look at six_point_ramp_demo)
    print("Rotating...")
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 2) # activate velocity mode in negative direction
    time.sleep(5)

    print("Stopping...")
    eval_board.write_register_field(mc.FIELD.VMAX, 0)  # set speed to 0
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 2)  # apply changes
    time.sleep(2)

    print("Moving back to 0...")
    target_position = 10000
    eval_board.write_register_field(mc.FIELD.VMAX, v_max)                   # set max speed
    eval_board.write_register_field(mc.FIELD.XTARGET, target_position)      # set target position to 0
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 0)                   # aktivate position mode

    # Wait until position 0 is reached
    T_s = 0.2                   #Sampling Time [seconds]  = Resolution of the plot ; Rage (0.5 ; 0.005)

    while eval_board.read_register_field(mc.FIELD.XACTUAL) != target_position:
        print(f"Actual position: {to_signed_32(eval_board.read_register_field(mc.FIELD.XACTUAL))} \t Actual speed: {eval_board.read_register_field(mc.FIELD.VACTUAL)}")
        time.sleep(T_s)

    print("Reached position 0\t Reached speed 0")

print("\nReady.")