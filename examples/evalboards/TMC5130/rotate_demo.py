################################################################################
# Copyright © 2024 Analog Devices Inc. All Rights Reserved. This software is
# proprietary & confidential to Analog Devices, Inc. and its licensors.
################################################################################

"""
Move a motor back and forth using velocity and position mode of the TMC5130

Line 31, we set a lower run/standby current for the motor. Using NEMA17, this should result in a coil current around 800mA.
If the motor is stalling due to too low current, set motorCurrent higher.
If a lower value still is needed, set GLOBAL_SCALER register to 128 to half motor current.

Created on 15.05.2019 by ME
"""
import time
import pytrinamic
import numpy as np
import math
import matplotlib.pyplot as plot
from pytrinamic.connections import ConnectionManager
from pytrinamic.evalboards import TMC5130_eval


pytrinamic.show_info()

with ConnectionManager().connect() as my_interface:
    print(my_interface)

    # Create TMC5130-EVAL class which communicates over the Landungsbrücke via TMCL
    eval_board = TMC5130_eval(my_interface)
    mc = eval_board.ics[0]
    motor = eval_board.motors[0]

    #it can be used with "Trapezoid Mode" (tapez.) : acceleration, constant speed, deacceleration
    #or the "6 Point Mode" where the acceleration and deceleration, are splitted in two stages
    #For "Trapezoid Mode" set A1 = D1 < AMAX = DMAX             -> this is the mode right now
    #For symetric "6 Point Mode" set V >>A1 = D1 > Amax = DMAX



    print("Preparing parameters...")                         #Name     |  Mode   |           Task
    eval_board.write_register(mc.REG.A1, 1000)         #A1       | 6 piont | initial acceleration between VSTART and V1
    eval_board.write_register(mc.REG.AMAX, 1000)       #AMAX     | trapez. | accelaration in the end
    eval_board.write_register(mc.REG.V1, 50000)        #V1       |         | threshold for the  first acceleration phase
    eval_board.write_register(mc.REG.D1, 1000)         #D1       | 6 piont | de/acceleration in the  end / start
    eval_board.write_register(mc.REG.DMAX, 1000)       #DMAX     | trapez. | initial deacceleration
    eval_board.write_register(mc.REG.VSTART, 0)        #VSTART   |         | Motor start velocity
    eval_board.write_register(mc.REG.VSTOP, 10)        #VSTOP    |         | Motor stop velocity threshold
    v_max=5 * 25600  #= 179'200                                                  | max velocity

    # Set lower run/standby current
    motorCurrent = 2
    motor.set_axis_parameter(motor.AP.RunCurrent, motorCurrent)
    motor.set_axis_parameter(motor.AP.StandbyCurrent, motorCurrent)

    # Clear actual positions
    motor.actual_position = 0

    print("Rotating...")
    motor.rotate(-7 * 25600)
    time.sleep(5)


    print("Stopping...")
    motor.stop()
    time.sleep(3)


    print("Moving back to 0...")
    motor.move_to(0, -v_max)

    # Wait until position 0 is reached
    i=0                    # Sample count
    T_s=0.2                #Sampling Time [seconds]  = Resolution of the plot ; Rage (0.5 ; 0.005)

    time_ref =time.perf_counter()

    while motor.actual_position != 0:
        print(f"time: {time.perf_counter()- time_ref:.1f} s\tActual position: {motor.actual_position} \t Actual speed: {motor.actual_velocity}")
        i+=1
        time.sleep(T_s)

    print("Reached position 0\t Reached speed 0")


print("\nReady.")