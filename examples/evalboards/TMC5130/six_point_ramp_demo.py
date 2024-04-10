################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

"""
Move a motor back and forth using velocity and position mode of the TMC5130

Line 31, we set a lower run/standby current for the motor. Using NEMA17, this should result in a coil current around 800mA.
If the motor is stalling due to too low current, set motorCurrent higher.
If a lower value still is needed, set GLOBAL_SCALER register to 128 to half motor current.

In the end, the script  has  3 plots of position, velocity and acceleration
The acceleration is calculated. Position and speed are read out. The values are not the actual ones.

In the current configuration, it uses a sixPoint ramp. That improves the control system ability.

This is an advanced version of rotate_demo.py . It is more complex and shows more use case.
For beginners it is recommended to understand at first the basic version!

"""
import time
import pytrinamic
import matplotlib.pyplot as plt

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5130_eval
from pytrinamic.helpers import to_signed_32

micro_steps_per_mechanical_revolution = 53687   # unit [ppt] = [µsteps / t]
"""
Definition in the Datasheet page 36 and 75
[ppt] = [µsteps / t]
[pps] = [µsteps / s]
f_CLK = 16 MHz   commonly   (page 52)

v_pps = v_ppt * (f_CKL / 2 /2^23)
a_pps = a_ppt * /2 *(512 * 265)/2^24

"""

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
    # For symetric "6 Point Mode" set V >>A1 = D1 > Amax = DMAX -> this is the mode right now

    print("Preparing parameters...")
    v_max = round(4 * micro_steps_per_mechanical_revolution)    # 4 rps --> [ppt]

    # Set - other - parameters
    #########################                               # Name      |         Task
    M_Res = 3                                               #           | M_res  = [0,1,2,3,4,5,6,7,8]
    v_max = round(4 * micro_steps_per_mechanical_revolution /pow(2, M_Res))     # Vmax = 4 rps
    eval_board.write_register_field(mc.FIELD.MRES, M_Res)   # MRES      | set Microstep resolution
    eval_board.write_register_field(mc.FIELD.XACTUAL, 0)    # XACTUAL   | Clear actual positions
    eval_board.write_register_field(mc.FIELD.VMAX,v_max)    # VMAX      | set max velocity
    eval_board.write_register_field(mc.FIELD.IRUN,2)        # IRUM      | set the standstill current
    eval_board.write_register_field(mc.FIELD.IHOLD,2)       # IHOLD     | set Motor run current
    eval_board.write_register_field(mc.FIELD.SG_STOP, 0)    # SG_STOP   | resets the StallGuard2 - Stop
    eval_board.write_register_field(mc.FIELD.SGT, 0)        # SGT       | turns StallGuard2 off
    def speed_step2rotation(x):
        return x / (micro_steps_per_mechanical_revolution / pow(2 , M_Res))
    def speed_rotation2step(x):
        return x * (micro_steps_per_mechanical_revolution / pow(2 , M_Res))

    # Set - ramp - parameters
    #########################                                               # Name     |  Mode   |           Task
    eval_board.write_register(mc.REG.A1,  round(8000 / pow(2, M_Res)))      # A1       | 6 piont | initial acceleration between VSTART and V1
    eval_board.write_register(mc.REG.AMAX, round(800 / pow(2, M_Res)))      # AMAX     | trapez. | accelaration in the end
    eval_board.write_register(mc.REG.V1, round(100000 / pow(2,M_Res)))      # V1       |         | threshold for the  first acceleration phase
    eval_board.write_register(mc.REG.D1,round(8000 / pow(2, M_Res)))        # D1       | 6 piont | de/acceleration in the  end / start
    eval_board.write_register(mc.REG.DMAX, round(800 / pow(2, M_Res)))      # DMAX     | trapez. | initial deacceleration
    eval_board.write_register(mc.REG.VSTART, 0 )                            # VSTART   |         | Motor start velocity
    eval_board.write_register(mc.REG.VSTOP, 10)                             # VSTOP    |         | Motor stop velocity threshold

    print("Rotating...")
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 2) # aktivate velocity mode in negative direction
    time.sleep(5)

    print("Stopping...")
    eval_board.write_register_field(mc.FIELD.VMAX, 0)       # set speed to 0
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 2)   # apply changes

    while eval_board.read_register_field(mc.FIELD.VACTUAL) != 0:
        time.sleep(0.1)

    print("Moving back to 0...")
    Traget_position = 0
    eval_board.write_register_field(mc.FIELD.VMAX, v_max)                   # set max speed
    eval_board.write_register_field(mc.FIELD.XTARGET, Traget_position)      # set traget position to 0
    eval_board.write_register_field(mc.FIELD.RAMPMODE, 0)                   # aktivate position mode

    # Wait until position 0 is reached
    i = 0         # Sample count
    T_s = 1E-3 # Sampling Time [seconds] = Resolution of the plot ; Rage (0.5 ; 0.005) for M_res = 0 else smaler is possible
    values_position = []
    values_speed = []
    values_time = []
    time_ref = time.perf_counter()

    while eval_board.read_register_field(mc.FIELD.XACTUAL) != Traget_position:
        values_position.append(to_signed_32(eval_board.read_register_field(mc.FIELD.XACTUAL)))
        values_speed.append(eval_board.read_register_field(mc.FIELD.VACTUAL))
        values_time.append(time.perf_counter() - time_ref)
        print(f"Time: {values_time[i]:.2f}s\t\tActual position: {values_position[i]} \t Actual speed: {values_speed[i]}")
        i += 1
        time.sleep(T_s)

    values_position.append(eval_board.read_register_field(mc.FIELD.XACTUAL))
    values_speed.append(eval_board.read_register_field(mc.FIELD.VACTUAL))
    values_time.append(time.perf_counter() - time_ref)
    print(f"Time: {time.perf_counter() - time_ref:.2f}s\t\tReached position 0\t\t Reached speed 0")

    #1. Plot: position
    fig1, ax1 = plt.subplots()
    ax1.plot(values_time, values_position)
    ax1.set_xlabel("Time [s]")
    ax1.set_ylabel("Position [Microsteps]")
    secax1 = ax1.secondary_yaxis('right', functions=(speed_step2rotation, speed_rotation2step))
    secax1.set_ylabel("Position [ruonds]")
    ax1.set_title("Position")
    ax1.ticklabel_format(axis="y", scilimits=[-3, 3])
    plt.show(block=False)

    # 2. Plot: speed
    fig2, ax2 = plt.subplots()
    ax2.plot(values_time, values_speed)
    ax2.set_xlabel("Time [s]")
    ax2.set_ylabel("Speed [Microsteps / second]")
    secax2 = ax2.secondary_yaxis('right', functions=(speed_step2rotation, speed_rotation2step))
    secax2.set_ylabel("Speed [rps]")
    ax2.ticklabel_format(axis="y", scilimits=[-3, 3])
    ax2.set_title("Speed")
    plt.show(block=False)

    #calculating the acceleration
    values_acceleration = [0]
    j = 0
    for _ in values_speed[1:]:
        values_acceleration.append((values_speed[j-1]-values_speed[j])/(values_time[j-1]-values_time[j]))
        j += 1
    values_acceleration.append(0)
    values_time.append(values_time[i]+T_s)

    # 3. Plot: acceleration
    fig3, ax3 = plt.subplots()
    ax3.plot(values_time, values_acceleration)
    ax3.set_xlabel("Time [s]")
    ax3.set_ylabel("Acceleration [Microsteps /s^2]")
    ax3.set_title("Acceleration")
    secax3 = ax3.secondary_yaxis("right", functions=(speed_step2rotation, speed_rotation2step))
    secax3.set_ylabel("Acceleration [round/s^2]")
    ax3.ticklabel_format(axis='y', scilimits=[-3, 3])
    plt.show()
    plt.close('all')

print("\nReady.")