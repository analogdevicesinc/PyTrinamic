#!/usr/bin/env python3.8
'''
Requires python3.8 to use asyncio funcionalities
Use the TMCM1161 module to perform a measurement
Rotate, read ADC input

If matplotlib availabe uncomment corresponding line to plot the result
Created on 17.03.2021

author: @amjadtaleb
'''
from PyTrinamic.modules.TMCM1161.TMCM_1161 import TMCM_1161
from PyTrinamic.connections.ConnectionManager import ConnectionManager
from PyTrinamic.TMCL import TMCL_Command
import asyncio
import time
import matplotlib.pyplot as plt
err_dict = {0: 'stallGuard', 1: 'Overtemperature',
            2: 'HighTemperature', 3: 'ShortGND_A', 4: 'ShortGND_B',
            5: 'OpenLoad_A', 6: 'OpenLoad_B', 7: 'StandStill'}


def initialize(ax):
    '''Set initial motor parameters for low noise and power consumption 

    freewheelingDelay: Time after which the power to the motor will be cut when
    its velocity has reached zero (a value of 0 (default setting) means never)
    values[0:65535]in 10ms 500=5sec

    Reduce motor heating and whining in standby:
    StandbyCurrent = 10% of MaxCurrent
    switch to standby 100*10ms after speed is 0
    '''
    ax.setAxisParameter(ax.APs.MicrostepResolution, 8)  # values[0:8] default 8
    ax.setAxisParameter(ax.APs.freewheelingDelay, 500)
    ax.setAxisParameter(ax.APs.StandbyCurrent, 10)
    ax.setAxisParameter(ax.APs.PowerDownDelay, 100)
    ax.connection.send(TMCL_Command.SIO, 0, 0, 0)  # set pull resistors to low
    ax.connection.setDigitalOutput(255)  # set outputs to 0V


async def move(ax: TMCM_1161, mode: str, to: int, at: int, id: str = '', verbose: bool = False):
    """
    Parameters:
        ax: TMCM_1161 instance
        mode: absolute or ralative
        to: int: target position
        at: int: speed
        id: str: idintifier to print in terminal
    return:
        int: actual position of motor
    """
    old_position = ax.getActualPosition()
    if verbose:
        print(f'{id} was at {old_position}')
    if mode == 'abs':
        ax.moveTo(to, at)
    elif mode == 'rel':
        ax.moveBy(to, at)
    else:
        print('unknown mode')
        return
    while not ax.positionReached():
        if verbose:
            print(id, ax.getActualPosition())
        await asyncio.sleep(0.001)
    await asyncio.sleep(0.001)
    pos = ax.getActualPosition()
    if verbose:
        print(id, pos)
    return pos


def get_all_inputs(ax):
    """Read selected input pins Analog and Digital
    """
    con = ax.connection
    con.setDigitalOutput(1)
    A = con.analogInput(0) # N0 GIO 0, 1 0. . . 4095
    T = con.analogInput(9) # Temperature GIO 9, 1 [°C]
    V = con.analogInput(8) # Voltage GIO 8, 1 [1/10V]
    # print(f'A:{A}    T:{T}       V:{V}')
    # I1, I2, I3 = (con.digitalInput(i) for i in [1,2,3])
    D = f'{con.digitalInput(255):04b}'
    D = list(int(i) for i in D)
    return A, T, V #, D


def update_val(old, new):
    """Utility function to use in set_speed
    """
    if new > old:
        return old + 1
    else:
        return old - 1


def set_speed(ax, speed, acceleration, pulseDivisor, rampDivisor):
    '''
    deliberatly made slow, otherwise motor goes crazy
    increase divisors by one every 0.25 sec, each divisor separetly
    Table 15 pages 78,79/110
    Althought this does not seem to work, the motor oscillates around target value before stabilizing.
    '''
    ax.stop()
    ax.setMaxVelocity(speed)
    ax.setMaxAcceleration(acceleration)
    while True:
        current_p = ax.getAxisParameter(ax.APs.PulseDivisor)
        if current_p == pulseDivisor:
            break
        ax.setAxisParameter(ax.APs.PulseDivisor,
                            update_val(current_p, pulseDivisor))
        time.sleep(0.5)
    while True:
        current_r = ax.getAxisParameter(ax.APs.rampDivisor)
        if current_r == rampDivisor:
            break
        ax.setAxisParameter(ax.APs.rampDivisor,
                            update_val(current_r, rampDivisor))
        time.sleep(0.5)


def report(ax):
    flag = ax.getAxisParameter(ax.APs.DrvStatusFlags)
    flag = f'{flag:08b}'
    if '1' in flag:
        error_list = []
        for i in range(len(flag)):
            if flag[-i-1] == '1':
                error_list.append(err_dict[i])
        print(f'Error Message: {flag}:: {error_list}')


async def main(reset=True):
    # connect to motor and set initial values
    connectionManager = ConnectionManager(argList='--port 1')
    x = TMCM_1161(connectionManager.connect())
    initialize(x)
    # stop motors before setActualPosition (data sheet p76/110, table 15)
    if reset:
        x.stop()
        x.setActualPosition(0)

    # Move motor to initial value
    print('moving to initial position')
    set_speed(x, 1600, 1000, 3, 7)
    await move(x, 'abs', 51200, 1000, 'x')
    x.stop()
    report(x)  # print info in case of an error

    print('Start measurement')
    # increase pulse division to 6 for a smoother movement during measurement
    set_speed(x, 2047, 2047, 5, 8)
    result = []


    now = time.time()
    x.connection.clearDigitalOutput(0) # sets digital output to high in my case
    x.connection.clearDigitalOutput(1) # sets digital output to high in my case

    for i in range(100):
        val = await move(x, 'rel', -1024, 2047, 'x')
        ans = get_all_inputs(x)
        result.append((val, ans))
        print(i, val, ans)


    x.connection.setDigitalOutput(0) # clears digital output in my case
    x.connection.setDigitalOutput(1)

    total = time.time() - now
    print(f'Finished measurement in {total:.2f}s')

    report(x)
    x.stop()

    # Plotting
    X = [i[0] for i in result]
    A = [i[1][0] for i in result]
    T = [i[1][1] for i in result]
    V = [i[1][2] for i in result]

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.plot(X, A)
    ax2.plot(X, T)
    ax3.plot(X, V)
    
    ax2.set_xlabel('Motor Position')
    ax1.set_ylabel('AIN_0 [0/4095]')
    ax2.set_ylabel('Temperature [°C]')
    ax3.set_ylabel('Voltage [1/10V]')
    plt.show()

if __name__ == '__main__':
    asyncio.run(main(reset=True))
