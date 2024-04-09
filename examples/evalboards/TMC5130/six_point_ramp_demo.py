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

"""
import time
import pytrinamic
import numpy as np
import matplotlib.pyplot as plt

from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5130_eval

full_steps_per_mechanical_revolution = 200 # A full step = PolePairs * 4.
# Most motors have 200 full steps per revolution! a full step  = PolePairs * 4
micro_steps_per_mechanical_revolution = full_steps_per_mechanical_revolution * 256
# One mechanical revolution = 300 full steps * 256 Microsteps = 200 * 256 = 51200 microsteps per mechanical revolution


def speed_step2rotation(x): return x / full_steps_per_mechanical_revolution
def speed_rotation2step(x): return x * full_steps_per_mechanical_revolution


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

    print("Preparing parameters...")                 # Name     |  Mode   |           Task
    eval_board.write_register(mc.REG.A1, 8000)       # A1       | 6 piont | initial acceleration between VSTART and V1
    eval_board.write_register(mc.REG.AMAX, 800)      # AMAX     | trapez. | accelaration in the end
    eval_board.write_register(mc.REG.V1, 100000)     # V1       |         | threshold for the  first acceleration phase
    eval_board.write_register(mc.REG.D1, 8000)       # D1       | 6 piont | de/acceleration in the  end / start
    eval_board.write_register(mc.REG.DMAX, 800)      # DMAX     | trapez. | initial deacceleration
    eval_board.write_register(mc.REG.VSTART, 0)      # VSTART   |         | Motor start velocity
    eval_board.write_register(mc.REG.VSTOP, 10)      # VSTOP    |         | Motor stop velocity threshold
    v_max = round( 4 * micro_steps_per_mechanical_revolution)  # [rps]    | max velocity

    # Set lower run/standby current
    motor_current = 2
    motor.set_axis_parameter(motor.AP.RunCurrent, motor_current)
    motor.set_axis_parameter(motor.AP.StandbyCurrent, motor_current)

    # Clear actual positions
    motor.actual_position = 0

    print("Rotating...")
    motor.rotate(-v_max)
    time.sleep(5)

    print("Stopping...")
    motor.stop()

    while motor.actual_velocity != 0:
        time.sleep(0.1)

    print("Moving back to 0...")
    motor.move_to(0, -v_max)

    # Wait until position 0 is reached
    i = 0                         # Sample count
    T_s = 0.005                   #Sampling Time [seconds]  = Resolution of the plot ; Rage (0.5 ; 0.005)
    values_position = []
    values_speed = []
    values_time = []
    time_ref = time.perf_counter()

    while motor.actual_position != 0:
        values_position.append(motor.actual_position)
        values_speed.append(motor.actual_velocity)
        values_time.append(time.perf_counter() - time_ref)
        print(f"Time: {values_time[i]:.2f}s\t\tActual position: {values_position[i]} \t Actual speed: {values_speed[i]}")
        i += 1
        time.sleep(T_s)

    values_position.append(motor.actual_position)
    values_speed.append(motor.actual_velocity)
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
