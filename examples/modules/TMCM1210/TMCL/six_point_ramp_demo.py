################################################################################
# Copyright © 2019 TRINAMIC Motion Control GmbH & Co. KG
# (now owned by Analog Devices Inc.),
#
# Copyright © 2023 Analog Devices Inc. All Rights Reserved.
# This software is proprietary to Analog Devices, Inc. and its licensors.
################################################################################

import dataclasses

import matplotlib.pyplot as plt
import pytrinamic
from pytrinamic.connections import ConnectionManager
from pytrinamic.modules import TMCM1276
import time


@dataclasses.dataclass
class Sample:
    timestamp: float
    position: int
    velocity: int


pytrinamic.show_info()

# For more accurate position and velocity graph, change to data rate 115200 (after changing also the data rate on the module).
connection_manager = ConnectionManager("--interface serial_tmcl --data-rate 9600 --port interactive")

with connection_manager.connect() as my_interface:
    module = TMCM1276(my_interface)
    motor = module.motors[0]

    # Setting axis parameters for configuring SixPoint ramp
    motor.set_axis_parameter(motor.AP.MaxVelocity, 40000)
    motor.set_axis_parameter(motor.AP.MaxAcceleration, 30000)
    motor.set_axis_parameter(motor.AP.A1, 5000)
    motor.set_axis_parameter(motor.AP.V1, 10000)
    motor.set_axis_parameter(motor.AP.MaxDeceleration, 20000)
    motor.set_axis_parameter(motor.AP.D1, 5000)
    motor.set_axis_parameter(motor.AP.StartVelocity, 5000)
    motor.set_axis_parameter(motor.AP.StopVelocity, 5000)
    motor.set_axis_parameter(motor.AP.RampWaitTime, 31250)

    # Setting initial position to zero
    motor.actual_position = 0

    samples = []
    motor.move_to(100000)
    while not motor.get_position_reached():
        samples.append(Sample(time.perf_counter(), format(motor.actual_position), format(motor.actual_velocity)))

    motor.move_to(0)
    while not motor.get_position_reached():
        samples.append(Sample(time.perf_counter(), format(motor.actual_position), format(motor.actual_velocity)))

    fig, ax = plt.subplots(2)
    t = [float(s.timestamp - samples[0].timestamp) for s in samples]
    pos = [float(s.position) for s in samples]
    vel = [float(s.velocity) for s in samples]

    ax[0].plot(t, pos, label='Position')
    ax[0].set_title('Pos vs Time')
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Pos')
    ax[0].legend()
    ax[0].grid()

    ax[1].plot(t, vel, label='Velocity')
    ax[1].set_title('Vel vs Time')
    ax[1].set_xlabel('Time')
    ax[1].set_ylabel('Vel')
    ax[1].legend()
    ax[1].grid()
    plt.show()






