"""Module to run different ramp motions.

Please note that thees functions work in blocking mode.
"""

import time
import math


class VelocityRampRunner:
    """The VelocityRampRunner allows you to ramp up or down the velocity of a motor.

    This is helpful for modules/drives that do not have a velocity ramp features build in.

    You just give a start velocity, a target velocity and the time in which you like the velocity to go up/down from
    the start to the target velocity, and run_linear_ramp will update the velocity at the maximum possible interval, or
    by the interval given in the constructor (update_cycle_time_ms).
    """

    def __init__(self, velocity_update_callback, update_cycle_time_ms=0):
        """If update_cycle_time_ms is set to 0, the velocity is updated as fast as possible.

        :argument velocity_update_callback: You need to give a function that updates the velocity of your motor.
                                            The signature of the function should look like this:
                                            def callback(int velocity):
        :argument update_cycle_time_ms: Optional update interval, if set to zero or omitted the velocity will be updated
                                        as fast as possible.
        """
        self._velocity_update_callback = velocity_update_callback
        self._update_cycle_time_ms = update_cycle_time_ms

    def run_linear_ramp(self, start_velocity_rpm, target_velocity_rpm, time_delta_ms):
        """Update the velocity on a linear basis from start_velocity to the target_velocity within the given time."""
        if self._update_cycle_time_ms:
            self._velocity_ramp_fixed_cycle(start_velocity_rpm, target_velocity_rpm, time_delta_ms)
        else:
            self._velocity_ramp_fast(start_velocity_rpm, target_velocity_rpm, time_delta_ms)

    def _velocity_ramp_fixed_cycle(self, start_velocity_rpm, target_velocity_rpm, time_delta_ms):
        """Sub function that updates the velocity on a update_cycle_time_ms basis.

        Note that if time_delta_ms can not be divided by update_cycle_time_ms,
        the linear ramp will be longer than expected. This way we make sure there is
        no high acceleration at the end.
        """
        update_cycles = math.ceil(time_delta_ms / self._update_cycle_time_ms)
        acceleration = (target_velocity_rpm - start_velocity_rpm) / time_delta_ms
        for i in range(update_cycles):
            start_time = self._time_ms()
            velocity_update = acceleration * (i * self._update_cycle_time_ms) + start_velocity_rpm
            self._velocity_update_callback(int(velocity_update))
            stop_time = self._time_ms()
            delay_time_ms = (stop_time - start_time)
            if delay_time_ms < self._update_cycle_time_ms:
                time.sleep((self._update_cycle_time_ms - delay_time_ms) / 1000)
        # always set the target_velocity_rpm at the end
        self._velocity_update_callback(int(target_velocity_rpm))

    def _velocity_ramp_fast(self, start_velocity_rpm, target_velocity_rpm, time_delta_ms):
        """Sub function that updates the velocity as fast as possible.

        Remark: Seems to update the velocity on a 1/4 ms basis on my machine
        """
        start_time = self._time_ms()
        acceleration = (target_velocity_rpm - start_velocity_rpm) / time_delta_ms
        self._velocity_update_callback(start_velocity_rpm)
        stop_time = self._time_ms()
        delay_time_ms = (stop_time - start_time)
        while delay_time_ms < time_delta_ms:
            velocity_update = acceleration * delay_time_ms + start_velocity_rpm
            self._velocity_update_callback(int(velocity_update))
            stop_time = self._time_ms()
            delay_time_ms = (stop_time - start_time)
        self._velocity_update_callback(target_velocity_rpm)

    @classmethod
    def _time_ms(cls):
        return time.perf_counter() * 1000
